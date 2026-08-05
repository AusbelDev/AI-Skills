# Troubleshooting Live Atrium Interfaces

Use this when a feed is misbehaving in a running system — messages stuck, a service
degraded, or failures with no obvious cause. Work from the symptom to the layer:
Integrator (Camel) → queue (ActiveMQ/Qpid) → IOServer worker → ARA/DB.

## Trace a message through the IOServer logs

Every message leaves a trail in the IOServer logs. Two log statements bracket processing:

- **`"Calling"`** — the worker *fetched* the message and started the handler.
- **`"Committing the message (id:"`** — the handler *completed* and the transaction committed.

If you see `Calling` but never `Committing` for a message, it entered the handler and didn't
finish — look for an exception, a timeout, or a block (below). Trace a specific message
across the logs using its `msgId`, `jcms_traceid`, or `cid`.

## Read the response code

Outgoing messages carry a `jcms_responsecode` header. It tells you the disposition:

| Value | Meaning | Implication |
| :--- | :--- | :--- |
| `MESSAGE_OK` | Success | Processed and committed. |
| `MESSAGE_SKIPPED` | Failed and dropped | The message errored and was discarded — check the handler logic / payload. |
| `MESSAGE_BLOCKED` | Failed and returned to the queue | **Halts the service.** The message is put back and reprocessed, so a poison message stops everything behind it. This is the usual cause of a "stuck" feed. |

A `MESSAGE_BLOCKED` poison message is the most common reason a whole interface appears
frozen — the same bad message is retried forever, blocking the queue.

## "Processed OK, but the editor/table didn't change"

A distinct and confusing signature: the file is consumed, the queue drains, a downstream
message (e.g. EMH) is generated — every outward sign says success — yet the values in the
Tracking/Data Editor are unchanged. This is rarely a *write* bug. It is almost always a
**failed reference/key lookup** upstream of the write:

- **Silent no-op update.** The handler's "find the existing record, then update it" logic
  keys on a value that doesn't match what the sender transmitted (e.g. resolving an
  `aircraft_group` by internal `id` `A330` when the file carries the IATA code `330`). The
  find returns nothing, the update loop iterates zero times, and nothing is written — with
  no error at all.
- **Skipped-but-looks-successful.** The resolver raises `Unable to find <x>` on the
  unmatched key; the message is `MESSAGE_SKIPPED` (failed and dropped). From the outside the
  feed "ran," but the row was discarded.

How to confirm: trace the message in the IOServer logs. `Calling` **without** `Committing`,
or a `MESSAGE_SKIPPED` disposition, points at a lookup that raised. If it committed cleanly
yet nothing changed, suspect the no-op path — check what key the `find`/`searchByPrototype`
uses against the exact value in the payload. The fix belongs in the resolver (match on the
representation the sender actually uses, with a fallback), and the regression test must use
a fixture built from the real payload — see the fixture-fidelity note in
`references/testing.md`.

## How a trigger fails (the trigger analogue of a poison message)

Triggers don't consume an inbound queue, so they don't `MESSAGE_BLOCKED` — but they have
their own wedge. A trigger processes its work inside a single transaction: if any write in
its `on_event` throws, the handler raises and the framework issues a `PlanAction.ROLLBACK`
of the **entire cycle**. Two consequences make this hard to diagnose:

- **Unrelated rows stop committing too.** Everything the cycle would have written rolls
  back together, so a throw on record A silently blanks record B. The reported symptom
  ("table X isn't updating") is often *not* about table X — chase the failing write, not
  the empty table.
- **It re-throws every cycle.** A trigger re-evaluates the same work each run, so a bad
  record wedges the service continuously rather than dropping once. This is why
  `ioserver clear_hastore` alone doesn't cure it — clearing state just replays the same
  failing cycle. Fix the throwing write, then clear.

## Constraint violations as a root cause

A frequent reason for a `Calling`-without-`Committing` gap (above) is a value that violates
a Dave attribute constraint on save — most often a string longer than the column's declared
`size=N`. Free-text fields (`reason`, comments, descriptions, names) are the usual
offenders: they overflow only on unusual inputs, so the feed runs for months and then wedges
the first time an over-length value arrives. When you see a save-time exception, check the
attribute's `size=` in the model XML against the value being written.

## System commands (cmsshell)

Enter the shell with `cmsshell`, then:

- **`ioserver selftest`** — verify active queues, processes, and services are healthy. Start
  here to confirm the interface is even registered and listening.
- **`ioserverctl status <service_name>`** — check whether a specific worker has become
  *degraded* or *unresponsive* (usually from timeouts). A degraded worker won't drain its
  queue.
- **`ioserver clear_hastore`** (run inside `cmsshell`) — clear the High Availability
  persistent store when a **trigger** service is stuck. Triggers persist state in the HA
  store; a wedged trigger often needs this to recover.

## A workflow for "the feed is stuck"

1. `ioserver selftest` — is the service registered and are its queues present?
2. `ioserverctl status <service>` — is the worker degraded/unresponsive?
3. Check the queue depth and look for a `MESSAGE_BLOCKED` poison message being retried.
4. Grep the logs for the message's `msgId`/`traceid`: did it get `Calling` without
   `Committing`? Read the exception there.
5. If it's a trigger and nothing else explains it, `ioserver clear_hastore`.
6. Fix the root cause (handler bug, bad payload, downstream/external timeout) — clearing
   state without fixing the cause just defers the next block.

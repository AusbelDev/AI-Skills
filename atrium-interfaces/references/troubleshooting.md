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

### Per-worker control with `ioserverctl`

`ioserverctl` operates at the *service* (worker) level and takes `-p <process>` (the
IOServer process the service runs under; see `sysmondctl` below to find it):

- **`ioserverctl list -p <process>`** — the status table for every service in a process.
  Columns are `Service | Status | Requested Workers | Running Workers`. Status is one of
  `active` / `stopped` / `broken`; **`Running Workers` is the real "is it up" signal**
  (`Requested Workers` reads 0 even for healthy services). A `broken` row with 0 running
  workers is the degraded state to chase.
- **`ioserverctl -p <process> -s <service> start|stop`** — bounce a *single* wedged worker
  without restarting the whole IOServer process (and everything else sharing it). `start`
  on an already-running service reports `has already started`; `stop` reports
  `Stopping service '<name>'`. This is the surgical alternative to a process restart.

### Which process runs a service — `sysmondctl`

- **`sysmondctl status`** — lists every sysmond-managed process with its running state
  (`Running with PID …` vs `is not running`) plus scheduled jobs. Use it to find which
  IOServer process (`ioserver_single1`, `ioserver_batch`, …) hosts the service you want to
  target with `ioserverctl -p`. Note the mapping is **many-to-many**: the `ioserver_*`
  process files are alternative deployment topologies, so one interface may be declared in
  several, and only some are running.

## Inspecting queues (`amqctlpy`) — and the physical-name trap

To see queue depth and consumers directly on the broker:

```
amqctlpy -b <broker> list -a -m -P <admin-password>
```

- **`-a` is essential.** Without it, `list` shows only queues declared in the config files,
  which can print *nothing* even when queues are live on the broker. `-a`
  (`--broker-queues`) asks the broker itself. `-m` (`--more`) adds the metric columns:
  `QueueSize` (depth), `ConsumerCount`, `EnqueueCount`, `DequeueCount`.
- **Read the health from the columns.** A `to.ioservice.<name>` with depth climbing and
  `ConsumerCount = 0` is a stuck consumer; a `.error` queue with `QueueSize > 0` is the
  accumulating-error signature. A healthy inbound queue shows `ConsumerCount ≥ 1`.

> **The logical/physical queue-name trap.** The broker reports **physical** queue names
> carrying the CCF `%(ccf/prefix)` (the `<instance_name>` in `ccf.xml`) — commonly
> `<prefix>.to.ioservice.<name>`, e.g. `carmen.to.ioservice.FlightInput_5_plainxml`. But
> the interface config and your mental model use the **logical** `<queue_reference>`
> (`to.ioservice.<name>`, no prefix). So when matching a config queue to a broker queue,
> account for the prefix. This bites hardest when *sending* (below): addressing the logical
> name creates a brand-new, unconsumed queue that the worker never reads, so the message
> silently goes nowhere.

## Reproducing a live feed with a captured payload

To exercise a running interface with a real payload (e.g. to reproduce a reported failure),
put the message straight on its inbound queue and watch the outcome:

```
amqctlpy -b <broker> send -q <PHYSICAL-inbound-queue> <file>       # or -c '<inline content>'
```

- **Use the PHYSICAL (prefixed) queue name** — see the trap above. Sending to the logical
  name looks like it works but the worker never consumes it.
- Then re-run the `list -a -m` above: a consumed message shows `EnqueueCount` and
  `DequeueCount` both incremented; a rejected one lands on the `.error` queue
  (`QueueSize > 0`). Combined with the `Calling`/`Committing` log trace, this pins whether
  the handler accepted or skipped the payload. Clean up afterward with
  `amqctlpy -b <broker> purge <queue> -P <pwd>` (note: `purge`/`drop` take the queue
  **positionally**, unlike `send`'s `-q`).

## A workflow for "the feed is stuck"

1. `ioserver selftest` — is the service registered and are its queues present?
2. `ioserverctl list -p <process>` (or `status <service>`) — is the worker `broken` /
   degraded, or running with 0 workers?
3. `amqctlpy … list -a -m` — is the inbound queue backing up with no consumer, or is the
   `.error` queue non-empty? (Remember the physical-name prefix.) Look for a
   `MESSAGE_BLOCKED` poison message being retried.
4. Grep the logs for the message's `msgId`/`traceid`: did it get `Calling` without
   `Committing`? Read the exception there.
5. If it's a trigger and nothing else explains it, `ioserver clear_hastore`.
6. Fix the root cause (handler bug, bad payload, downstream/external timeout) — clearing
   state without fixing the cause just defers the next block. To recover a single wedged
   worker after the fix, `ioserverctl -p <process> -s <service> stop` then `start` rather
   than bouncing the whole process.

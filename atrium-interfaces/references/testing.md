# Integration Testing for Atrium Interfaces

Atrium interfaces are validated with high-fidelity integration tests that exercise the real
handler against a simulated database — so you confirm behavior without touching production.
Both SMOG and Custom ARA interfaces use the same framework.

Tests live alongside the interface package, e.g.
`usr/lib/python/datafeeds/<interface>/test/handler_test.py` (and `parser_test.py` for
parser-only logic).

## Framework

- **Base classes:** inherit from `IOServiceTestBase` and `BehaveStepRunner` (uses
  Python `unittest2`).
- **For SMOG tests:** set the `builder_config` property to point at your
  `ioservice_builder.xml`, so the generated artifacts are loaded.

## The test rhythm

1. **Set up state with Gherkin.** Use `self.run_behave_steps()` with Gherkin/behave syntax
   to populate the simulated database — aircraft, airlines, existing records, etc. This is
   how you establish preconditions readably.
2. **Queue a message.** `self.put_msg(payload)` enqueues a mock incoming message
   (CSV/JSON/XML, whatever the interface consumes).
3. **Run the handler.** `self.process()` executes the worker against the queued message.
4. **Verify.**
   - `self.assertMaveChanges(...)` — assert the exact number of insert/modify/delete
     operations. This catches a handler that does too much or too little.
   - `self.assertMaveFixture(...)` — strictly validate the actual values written to the
     database columns. This catches mapping/normalization mistakes.

> **Test against the simulated DB, not hand-mocked objects.** Constraint violations —
> string longer than a column's `size=N`, missing required fields, unique-index clashes —
> only surface when the handler writes through the real (simulated) Dave layer. A test that
> mocks the ARA/Dave objects with plain Python attributes has no column to violate, so it
> passes while production throws on save. If the behavior you're guarding is "this value
> must fit the column," the test must go through the simulated schema (Gherkin setup +
> `assertMaveFixture`), not a stubbed object.

## What to cover

The existing interfaces converged on three canonical cases — use them as a template:

- **`test_010_basic_request`** — a normal message creates the expected records with the
  correct field values. (For clockwork: `ground_task`, `aircraft_ground_asmt`, and
  `maintenance_wp_dd`.)
- **`test_020_clear_existing`** — for total-state feeds, a second/overlapping message
  atomically purges the old state and replaces it. This is where total-state logic lives or
  dies; test it deliberately.
- **`test_030_faulty_request`** — a malformed message is rejected cleanly: parsing errors
  don't corrupt state, and an error payload lands on `from.ioservice.<interface>.error`.

## Running tests

`ioservice_testrunner` needs the Carmen environment (`$CARMSYS`, `$CARMUSR`, `$CARMTMP`) set.
A bare login shell usually doesn't have these, so run it **through `cmsshell -c`**, which
sources the environment first. Running the bin directly (`$CARMSYS/bin/ioservice_testrunner`)
fails with "CARMSYS must be defined" when the env isn't loaded.

```bash
# One test class (fastest feedback loop):
cmsshell -c 'ioservice_testrunner -c datafeeds.<interface>.test.handler_test.<TestClass>'

# A whole directory — pass the project's python root as the discovery start dir with -s,
# otherwise discovery may find nothing:
cmsshell -c 'ioservice_testrunner -s usr/lib/python usr/lib/python/datafeeds/<interface>/test'
```

A green run prints `PASSED: N tests OK`; per-class lines read `PASSED:/FAILED: <class>
(N seconds)`. **Parse the text summary, not JSON** — the `-j`/JSON flag has been seen to
crash in some builds (`argument of type 'float' is not iterable`), so the human-readable
lines are the reliable signal. Runs can be slow (tens of seconds per class) since each
exercises the simulated DB. After a model extension, run `dave_model_migrator` first so the
simulated schema matches your new fields — otherwise fixture assertions on those columns
will fail confusingly.

### Finding an interface's test package

The test directory name is a snake_case slug (`usr/lib/python/datafeeds/crew_on_flight_4/`)
that is **not** mechanically derivable from the `<ioservice name>` (`CrewOnFlight_4_event`).
Don't guess the slug. Instead, every test module declares the interface it targets:

```python
ioservice_name = 'CrewOnFlight_4_event'
```

So to locate the tests for a given interface, grep for its exact name:
`grep -rl "ioservice_name = ['\"]<Name>['\"]" usr/lib/python/datafeeds/*/test/`. One slug can
hold tests for several related services (e.g. the `_event`, `_soap`, and vendor variants),
each in its own `test_*.py` with its own `ioservice_name`.

## Fixtures must mirror the real external payload

A test is only as honest as its input message. The most dangerous failure mode is a suite
that is **all green while production silently does nothing** — and it almost always traces
to a fixture that sends a value production never sends.

The classic trap is a reference-data code with **several representations**. An
`aircraft_group`, for example, has both an internal `id` (`A330`) and an `iata` code
(`330`); a station or function may likewise be addressable by more than one key. If the
external party transmits the IATA code but the fixture uses the internal id, and the
handler's lookup keys on `id`, then:

- the **fixture path** finds the record and passes, but
- the **production path** never matches — so a "find existing then update" becomes a no-op,
  or the resolver raises and the message is skipped (see the "processed OK but nothing
  changed" signature in `references/troubleshooting.md`).

Rule of thumb: **build the fixture from a real captured payload** (an actual file drop, the
EMH/queue message, the vendor's sample), not from what is convenient to look up in the test
plan. When an inbound field is a coded reference, confirm *which* representation the sender
uses and encode that. It is worth keeping one fixture on each representation the handler is
supposed to accept, so the resolver's fallback logic is genuinely exercised.

## Reopened tickets: reproduce before fixing

When a ticket comes back reopened, the prior fix was usually *partially* right — it solved
one facet and left another, or it was verified only against a fixture that didn't match
production. Resist re-reading the code and re-deriving a theory. Instead:

1. **Diff the current behavior against the prior fix commit** to see exactly what was
   changed and what it did *not* cover.
2. **Write a failing test that replays the real production input** — the actual codes,
   formats, and edge values from the evidence (file, message, screenshot). If it reproduces
   the reported symptom, you have pinned the root cause empirically rather than by
   inspection. Only then change code, and keep that test as the regression guard.

## Gotcha: local↔UTC conversion needs timezone data in the fixture

If your handler converts local time to UTC (or back) via `station.toUTCTime(...)` /
`toLocalTime(...)`, the test's airports must carry timezone data — otherwise the conversion
returns an *invalid* `AbsTime`, and the downstream `create` fails with a baffling error like
`Attribute GroundTask.StartTime cannot be null`. A bare `airport` override (just `id`/`name`)
has no `tzprofile`, so it can't convert.

Seed a minimal profile and point the airports at it (a `00:00` std_offset keeps stored UTC
equal to the input, which makes assertions easy to reason about):

```gherkin
Given table "timezone_profile" is overridden with the following
     | name |
     | UTC0 |
Given table "timezone_period" is overridden with the following
     | tzprofile | validfrom       | std_offset |
     | UTC0      | 01JAN2000 00:00 | 00:00      |
Given table "airport" is overridden with the following
     | id  | name     | tzprofile |
     | SCL | Santiago | UTC0      |
```

The reference feeds (clockwork/limops) don't hit this because they store UTC directly and
never call `toUTCTime` — so their tests get away with bare airports. The moment your feed does
its own conversion, this becomes mandatory.

## Debugging failing tests

- A failing `assertMaveChanges` count usually means total-state clearing is over- or
  under-removing — check the clear scope/window before the insert loop.
- A failing `assertMaveFixture` is typically a mapping or normalization bug (e.g. hyphens
  not stripped from a registration, wrong dynamic lookup) — check the parser and the
  handler's runtime lookups.
- Unique-index errors in a single test message point at missing `RelTime` offsets for
  batch-created records (see the ARA reference).
- `assertMaveChanges` only lists tables that actually changed. Asserting a no-op row like
  `('aircraft_ground_asmt', 0, 0, 0)` fails against an actual list that simply omits the
  table. To assert a table was *not* touched (e.g. an unassigned box that creates no
  assignment), leave it out of `assertMaveChanges` and instead check
  `self.assertNotIn('aircraft_ground_asmt', self.get_mave_changes(state_before))`.

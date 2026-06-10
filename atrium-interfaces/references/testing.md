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

```bash
$CARMSYS/bin/ioservice_testrunner <test_directory>
```

`ioservice_testrunner` discovers and runs the datafeed tests. After a model extension, run
`dave_model_migrator` first so the simulated schema matches your new fields — otherwise
fixture assertions on those columns will fail confusingly.

## Debugging failing tests

- A failing `assertMaveChanges` count usually means total-state clearing is over- or
  under-removing — check the clear scope/window before the insert loop.
- A failing `assertMaveFixture` is typically a mapping or normalization bug (e.g. hyphens
  not stripped from a registration, wrong dynamic lookup) — check the parser and the
  handler's runtime lookups.
- Unique-index errors in a single test message point at missing `RelTime` offsets for
  batch-created records (see the ARA reference).

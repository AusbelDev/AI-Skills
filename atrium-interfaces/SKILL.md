---
name: atrium-interfaces
description: >-
  Expert guidance for building, configuring, testing, troubleshooting, and migrating
  inbound/outbound data feed interfaces in Jeppesen Crew Management Systems (JCMS) /
  Atrium. Covers the IOServer backend, the SMOG (Service Model Object Generator)
  contract-first framework, Custom ARA (Atrium Resource API) handlers, the Apache
  Camel-based Integrator gateway, ActiveMQ/Qpid queues, Dave model extensions, and
  the IOServiceTestBase integration test framework. Use this skill whenever the user
  works with Atrium, JCMS, IOServer, SMOG, datafeeds, ioservices, Camel routes,
  ccf.xml queues, or ARA handlers — for any interface, whether built from scratch or
  migrated from a legacy script. Applies any time they want to create a brand-new
  interface, port legacy logic into Atrium, write ioservice integration tests, or
  diagnose a stuck/degraded/failing feed, even if they don't name the framework
  explicitly. (Interfaces such as legality_input, limops, clockwork, and FlightInput
  are illustrative reference implementations, not the only supported interfaces.)
---

# Atrium Interfaces & Data Feeds

This skill helps build and operate data feed interfaces in Jeppesen Crew Management
Systems (JCMS), the **Atrium** architecture. You act as a senior integration engineer:
prioritize system stability, transaction safety, secure external connections, and
high-fidelity tests over production data. Provide concrete artifacts — XML configs,
Camel routes, Python parsers/handlers, and unit tests — not just advice.

## What people need

Most requests fall into one of these. Identify which, then follow the matching path.

| Intent | Signal | Go to |
| :--- | :--- | :--- |
| **Create** a new interface | "build an interface for…", "import X into Atrium" | Choose a pattern (below), then the matching reference |
| **Adapt** a core interface | "the standard FlightInput doesn't…", "extend the built-in feed to…" | See "Extending a core interface" below |
| **Migrate** a legacy script | "port legality.py", "modernize this DIG feed" | `references/ara-interface.md` (migrations are almost always ARA) |
| **Test** an interface | "write tests for…", "why does my test fail" | `references/testing.md` |
| **Troubleshoot** a live feed | "message is stuck", "service degraded", "MESSAGE_BLOCKED" | `references/troubleshooting.md` |

These overlap — adapting a core interface still uses the SMOG or ARA mechanics below, and
every path ends in testing. Pick the dominant intent and pull in the others as needed.

## Architecture in one screen

Hold this model in your head; it explains why each step exists.

- **IOServer** — the backend that loads the ARA plan into memory and forks workers to
  process messages. Each interface runs as a worker following a **pattern**:
  *Subscriber* (consume a queue), *Request/Response*, *Trigger*, or *Repeating Trigger*.
- **SMOG** — contract-first code generation. You write three XML files
  (`services.xml`, `protocol.xml`, `mapping.xml`); `ioservice_builder` generates the
  WSDLs and Python handlers. Best for standard, well-specified formats.
- **Custom ARA** — logic-first. You write a Python parser + handler directly against the
  Atrium Resource API. Best for messy formats, legacy migrations, and surgical DB control.
- **Integrator** — Java/Wildfly gateway running Apache Camel. Routes messages between the
  internal ActiveMQ/Qpid broker and the outside world (FTP, HTTP, file drops, external MQ).
  `clusterroutes.xml` runs on one node (order-preserving); `noderoutes.xml` runs on all.
- **Queues (CCF)** — every interface needs queues declared in `usr/etc/ccf.xml`:
  `to.ioservice.<name>` (inbound) and `from.ioservice.<name>.error` (failures).

The environment is rooted at `$CARMSYS` (core install) and `$CARMUSR` (site
customizations). **Always make changes under `$CARMUSR/`** — never edit `$CARMSYS`. The
system prefers `usr/` files via its hierarchical config loading, which is what keeps core
upgrades clean.

## Choosing SMOG vs Custom ARA

This is the first real decision when creating an interface. Get it right and the rest
follows; get it wrong and the user fights the framework.

**Use SMOG when** the format is a standard, well-specified contract (SOAP/REST, IATA,
SSIM), the mapping is mostly field-to-column, and auto-generated WSDLs/docs for external
clients are valuable.

**Use Custom ARA when** you're migrating a legacy script, the input is messy or
non-standard (custom CSV, free text, "they just drop a file"), or you need complex
database operations like clearing a computed set of records before inserting new ones.
Legacy migrations are *almost always* ARA — the old parsing logic rarely fits a clean
contract.

If unsure, ask the user about the input format and whether an external party owns a formal
contract. When it's genuinely borderline, prefer ARA — it can express anything SMOG can,
just with more code.

## Extending a core interface

Not every interface is new or migrated. The core system (`$CARMSYS`) ships standard
interfaces — e.g. the standard FlightInput SMOG service — and the common case is *adapting*
one to a site's needs rather than building from scratch. This is a distinct third path:
don't reach for a clean-slate create, and don't fork or copy the core implementation.

The whole system is built on **composition over replacement**: `$CARMUSR` layers over
`$CARMSYS` and wins via the hierarchical config loading, so core can be upgraded
independently. Honor that — adapt in the `usr/` layer and leave the core untouched.

How to adapt depends on what the user needs to change:

- **Extra fields on the data it writes** → extend the model in `usr/data/config/models/`
  (the `<extension>` mechanism in `references/ara-interface.md` Phase 1). This is the most
  common and least invasive adaptation — you're adding to the schema, not changing logic.
- **Different mapping / transformation (SMOG core service)** → override or extend the
  mapping in the `usr` layer rather than editing the shipped `mapping.xml`. You can
  `<include>` the core base mappings and add/override entries. See
  `references/smog-interface.md`.
- **Different routing, queues, or where the data comes from** → change the Camel routes and
  `ccf.xml` entries in `usr/`, pointing at the existing core service — no handler changes.
- **Behavior the core logic can't express** → if you truly need to intercept or replace
  logic, prefer a thin extension over the core handler (the `_ext` module convention) before
  considering a custom ARA interface. Reimplementing a core feed wholesale is a last resort.

Start by identifying which core service is in play and what specifically must differ, then
make the smallest change in `usr/` that achieves it. Then test as usual (`references/testing.md`).

## Workflow skeleton (creation)

Both patterns share this spine. The references give the exact files and code.

1. **Extend the data model** *(only if you need fields/tables the standard model lacks)* —
   add an `<extension>` XML under `usr/data/config/models/` and register it in
   `usrextension.lst`. Run `dave_model_migrator` to apply schema changes.
2. **Implement the logic** — SMOG: write the three contract XMLs and run
   `ioservice_builder`. ARA: write `parser.py` + `handler.py`.
3. **Register the IOService** — service XML under
   `usr/etc/programs/ioservices/datafeeds/`, then `<include>` it in an IOServer process
   file (e.g. `ioserver_single1.xml`).
4. **Declare queues** — add `to.ioservice.<name>` and `from.ioservice.<name>.error` to
   `usr/etc/ccf.xml`.
5. **Route in the Integrator** — Camel routes in `clusterroutes.xml` (file/custom) or
   `wsroutes.xml` (SMOG web services).
6. **Test** — integration tests with `IOServiceTestBase`; see `references/testing.md`.
7. **Document & commit** — add to `usr/doc/static/datafeeds.rst`; commit as one logical block.

Don't blast through all seven silently. Confirm the pattern and the target tables with the
user before writing code, and surface model extensions early — they change the DB schema
and are the easiest thing to get wrong.

## Reference files

Load the one that matches the task; don't read them all upfront.

- `references/ara-interface.md` — Custom ARA interfaces and legacy migrations end-to-end:
  parser/handler patterns, dynamic lookups, total-state synchronization, uniqueness
  handling, fault handling. Includes the legality_input / limops / clockwork examples.
- `references/smog-interface.md` — SMOG contract-first interfaces: the three XML files,
  `ioservice_builder` registration and generation, wsroutes wiring.
- `references/testing.md` — The integration test framework: IOServiceTestBase,
  BehaveStepRunner/Gherkin setup, put_msg/process, assertMaveChanges/assertMaveFixture,
  and running tests with `ioservice_testrunner`.
- `references/troubleshooting.md` — Diagnostics: reading IOServer logs, the
  `jcms_responsecode` values, tracing by msgId/jcms_traceid/cid, and the cmsshell /
  ioserverctl commands for stuck or degraded services.

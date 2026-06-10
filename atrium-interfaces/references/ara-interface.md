# Custom ARA Interfaces & Legacy Migrations

Use this for logic-first interfaces: messy/custom formats, legacy script migrations, or
any case needing surgical control over the Atrium data model. You write the Python
directly against the **ARA (Atrium Resource API)** instead of generating it from a contract.

These patterns apply to **any** custom interface — most will be ones not listed here. A few
existing implementations are worth studying as worked examples of the patterns below:
`legality_input` (custom CSV migration), `limops` (JSON, total-clear), `clockwork` (JSON,
computed replacement period). Treat them as illustrations, not a menu — adapt the patterns
to whatever the interface at hand actually needs. The shared base is
`std_interfaces.common.BaseInterfaceHandler`.

## Table of contents
1. Phase 1 — Data model extension
2. Phase 2 — Parser
3. Phase 3 — Handler
4. Phase 4 — IOService registration & activation
5. Phase 5 — Queues (CCF)
6. Phase 6 — Integrator routing (Camel)
7. Phase 7 — Document & commit
8. Migration playbook (legacy script → Atrium)

---

## Phase 1 — Data model extension *(only if needed)*

Skip this if your data fits the standard model. If you need site-specific fields, extend
the entity in the `usr` layer rather than altering core tables.

Create a model XML in `usr/data/config/models/` (e.g. `jta_legality.xml`). Prefer
consolidating related site fields into one module (e.g. `jta_ots.xml`) rather than
proliferating files:

```xml
<?xml version="1.0"?>
<!DOCTYPE davemodel SYSTEM "davemodel.dtd">
<davemodel>
  <module name="jta_legality" desc="JTA Legality Extensions">
    <extension entityname="aircraft_restriction">
      <field name="flt_owner" reference="airline" desc="Owner for legality"/>
      <field name="arr_area" type="string" size="20" desc="Restricted area"/>
    </extension>
  </module>
</davemodel>
```

Register the module name (no `.xml`) in `usr/data/config/models/usrextension.lst`, then run
`dave_model_migrator` to apply the schema change. Surface model extensions to the user
early — they touch the DB schema and are the riskiest part to get wrong.

## Phase 2 — Parser (`parser.py`)

Create a package `usr/lib/python/datafeeds/<interface>/` with an empty `__init__.py`,
`parser.py`, and `handler.py`.

The parser turns the raw message into clean Python structures. Keep it free of database
logic — that separation makes it testable in isolation and easier to reason about.

- **Be robust to format variation.** Legacy text/CSV formats are rarely clean; regex and
  defensive parsing beat brittle index math.
- **Normalize on the way in.** E.g. strip hyphens from registrations so they match system
  standards.
- **Don't hardcode lookup codes.** Don't bake IATA/country/airline codes into the parser.
  Let the handler fetch them from the DB and pass them in (see dynamic mappings below).
- **JSON vs CSV.** JSON shifts from index-based to key-based mapping (`json.loads(msg)`).
  A common convention is to wrap core data in a `payload` key (with a `metadata` sibling)
  for clean extraction — see the clockwork/limops message format.
- **For total-state feeds**, the parser should return *every* entity seen in the message
  (even rows with no data), so the handler can clear stale state for all of them.

## Phase 3 — Handler (`handler.py`)

The handler uses ARA (`jcms.ara.core`) to apply changes to the plan. Key requirements:

1. **Interface version** — implement `handler_interface_version` returning
   `InterfaceVersion.TEN`.
2. **RST docs** — include an `<rst>` block at the top for automated system documentation.
3. **Return code** — return `PlanAction.SAVE` for subscriber services (or `UNCHANGED` /
   `ROLLBACK` as appropriate).
4. **Fault handling** — implement `on_fault` using `StandardErrorMessageCreator` so failures
   produce a proper error payload on the `.error` queue.

**Dynamic mappings (best practice).** Resolve codes at runtime in the handler, not the
parser: fetch airlines from `ara.Airline` to map ICAO→IATA; fetch countries from the
`country` collection for ISO codes. Pass the resolved maps into the parser.

**Heuristic lookup.** When the message omits a field, derive it from the DB: e.g. resolve
the airline owner by finding the aircraft and reading `aircraft.getOwner(time)`, or the
subfleet type via `aircraft.getType(time)`.

**Total-state synchronization.** When a message represents the *current complete state*
(legality, limops, clockwork), clear the old state before inserting:
- Determine the scope to clear. It may be all records of a restriction type (limops clears
  every `LIMOPS` record), or a computed window — clockwork derives a replacement period from
  `min`/`max` of the `start` times and removes only tasks/workpackages inside it.
- Iterate over *all* entities seen in the message and clear their specific records *before*
  adding new ones, so aircraft that lost all their markers still get cleaned up.
- Typical ARA ops: `searchByPrototype(...)` / search by attribute, `obj.remove()`,
  `ara.DomainObject.create(...)`, `ara.ProtoObject.create(...)`.

**Uniqueness handling.** If the target table has a unique index (e.g. `ac + restr + st`),
records created in the same batch can collide. Add a small `RelTime` offset (e.g. 1 minute)
to successive records' start times. Note this is per-interface: limops explicitly assumes
its data is already unique and applies *no* offset — don't add one blindly.

## Phase 4 — IOService registration & activation

Create the service definition `usr/etc/programs/ioservices/datafeeds/<interface>.xml`:
- `class="subscriber"` (most datafeeds), binding `datafeeds.<interface>.handler`.
- Define source/sink Qpid queues.

Activate it by `<include>`-ing it in an IOServer process file, typically
`usr/etc/programs/ioserver_single1.xml`:

```xml
<include href="${CARMUSR}/etc/programs/ioservices/datafeeds/<interface>.xml" />
```

## Phase 5 — Queues (CCF)

Add to `usr/etc/ccf.xml`:
- `to.ioservice.<interface>` — inbound from the Integrator.
- `from.ioservice.<interface>.error` — error/failure tracking.

## Phase 6 — Integrator routing (Camel)

Custom feeds are usually file drops, so wire a file watcher in
`usr/integrator/routes/clusterroutes.xml` (use `clusterroutes`, not `noderoutes`, when order
matters):
1. **Global option** to enable message logging:
   `<globalOption key="import_<interface>.msg.log" value="true"/>`
2. **File watcher** monitoring the import directory.
3. **Processor**: convert body to string, upload to Filehub, and notify the IOService queue.

## Phase 7 — Document & commit

Include the handler in `usr/doc/static/datafeeds.rst` via `.. include::`. Commit all the
changes as one logical block.

**Files-created checklist** (clockwork is a complete example):
`__init__.py`, `parser.py`, `handler.py`, `test/__init__.py`, `test/parser_test.py`,
`test/handler_test.py`, the ioservice XML, the ioserver process file, `ccf.xml`,
`clusterroutes.xml`, `datafeeds.rst`.

---

## Migration playbook (legacy script → Atrium)

When porting any legacy script into Atrium (a DIG feed, an old `.py` importer, a custom
loader — `legality.py` / `limops.py` are just examples of ones already done), follow this
order — it's how the existing migrations were done:

1. **Functional analysis.** Read the legacy script and write down exactly what it does:
   what it clears, what it parses (headers, data rows, markers like a `'0'` meaning
   "illegal"), and what records it writes (target table + every column + start/end times).
2. **Map legacy entities → Atrium (ARA) entities.** Legacy DIG/Dave tables have modern
   equivalents — e.g. clockwork mapped `flight_leg → ground_task`,
   `aircraft_flight_duty → aircraft_ground_asmt`,
   `maintenance_workpackage → maintenance_wp_dd`. Establish this table first.
3. **Decide on model extensions** for any legacy columns with no home in the standard model.
4. **Re-implement parsing in `parser.py`** — preserve the legacy format quirks but clean up
   the structure.
5. **Re-implement writes in `handler.py`** using ARA, applying total-state clearing if the
   legacy script rewrote the whole table each run.
6. **Wire config/queues/routing/tests** as in Phases 4–7.

Present a short migration plan and **wait for approval before creating files** — schema and
table-mapping decisions are expensive to undo.

# SMOG Contract-First Interfaces

Use this for standard, well-specified formats (SOAP/REST, IATA, SSIM) where the mapping is
mostly field-to-column and auto-generated WSDLs/docs for external clients add value. SMOG
(Service Model Object Generator) is **contract-first**: you write XML, and
`ioservice_builder` generates the WSDLs and Python handlers for you.

This applies to any SMOG interface you build. `FlightInput_5_soap` is one existing example
worth studying as a worked illustration — not the only SMOG interface. Core logic to study:
`lib/python/std_interfaces/flight_types_mave2.py`. Shared base mappings:
`data/config/smog/v2/std_interfaces.common/base_4_mapping.xml`.

## Phase 1 — Define the SMOG contract

Create three files in `usr/data/config/smog/v2/<interface>/`:

- **`services.xml`** — the service specification: `<operation>`, `<input-message>`, and
  `<complex-type>` definitions. This is the schema of what comes in.
- **`protocol.xml`** — how the service is exposed. For SOAP: namespaces, SOAP actions,
  element names. For JSON: field naming conventions.
- **`mapping.xml`** — the core logic, mapping incoming fields onto the Atrium Data Model
  (MAVE/UDM). Target is usually `target="air2_mave2"`. Use `<assign>`, `<choose>`, and
  `<call-function>` to transform data. You can `<include>` base mappings (e.g.
  `base_4_mapping.xml`) to reuse common aircraft/flight attributes rather than redefining them.

Keep the mapping declarative — if you find yourself wanting arbitrary control flow or
complex DB operations, that's a signal the interface should be Custom ARA instead.

## Phase 2 — Register & generate

Register the service in `usr/data/config/ioservice_builder.xml`:

```xml
<ioservice name="MyInterface_1_soap" pattern="subscriber">
  <description>Standard SOAP interface for data import</description>
  <smog-service name="MyInterface" version="1" protocol="soap">
    <service-spec location="$CARMUSR/data/config/smog/v2/my_interface/services.xml"/>
    <protocol-spec location="$CARMUSR/data/config/smog/v2/my_interface/protocol.xml"/>
    <service-mapping location="$CARMUSR/data/config/smog/v2/my_interface/mapping.xml"/>
  </smog-service>
</ioservice>
```

Generate the implementation:

```bash
$CARMSYS/bin/ioservice_builder /opt/jeppesen/jcms/usr/data/config/ioservice_builder.xml
```

This writes into `$CARMTMP/ioservice_builder/`:
- **WSDL/XSD** → `contract/`
- **Python handlers** → `lib/python/ioservice_impl/`
- **Service configs** → `config/`

These are *generated* — don't hand-edit them; change the contract XML and regenerate.

## Phase 3 — Integration

**Web service route** in `usr/integrator/routes/wsroutes.xml` (SMOG web services use
`wsroutes`, not `clusterroutes`):

```xml
<route id="MyInterface_1">
  <from uri="cxf:/MyService/v1?wsdlURL=file://{{env:CARMTMP}}/ioservice_builder/contract/MyInterface_1.wsdl&amp;dataFormat=MESSAGE" />
  <to uri="internalBroker:queue:{{env:CCF_PREFIX}}to.ioservice.MyInterface_1_soap" />
</route>
```

**Queues** in `usr/etc/ccf.xml`:
- `to.ioservice.MyInterface_1_soap`
- `from.ioservice.MyInterface_1_soap.error`

**Activation** — include the *generated* config in your IOServer process file:

```xml
<include href="${CARMTMP}/ioservice_builder/config/MyInterface_1_soap.xml" />
```

## Phase 4 — Testing

Test by putting XML/JSON messages on the queue and verifying MAVE changes. Use
`IOServiceTestBase`, and make sure the test's `builder_config` property points at your
`ioservice_builder.xml` so the generated artifacts are available. Use `self.put_msg(xml_content)`
to simulate external requests. See `testing.md` for the full framework.

---

**Workflow summary:** design XML contract → register in builder → run `ioservice_builder`
→ add wsroutes → add CCF queues → verify with integration tests.

## API reference


#### `carmensystems.basics.uuid.uuid` — UUID support

*class* `carmensystems.basics.uuid.uuid.``UUID`
:   `__init__`()
    :   Initialize self. See help(type(self)) for accurate signature.

    `clock_seq_hi_and_reserved`

    `clock_seq_low`

    `node`

    `time_hi_and_version`

    `time_low`

    `time_mid`

`carmensystems.basics.uuid.uuid.``uuidMake`()

`carmensystems.basics.uuid.uuid.``uuidMake64`()

`carmensystems.basics.uuid.uuid.``uuidFinish`()

`carmensystems.basics.uuid.uuid.``uuidShow`()

`carmensystems.basics.uuid.uuid.``uuidEncode64`()

`carmensystems.basics.uuid.uuid.``uuidDecode64`()

`carmensystems.basics.uuid.uuid.``makeUUID64`()
:   Generate a UUID and encode it as a base64 string.

    *makeUUID64() -> str*

    This function will generate a unique identifier and return it as a
    base64-encoded string.

    **deprecated** - Use basics.uuid.UUID.randomUUID().toBase64() instead

    > * **Return**: Generated UUID encoded as a base64 string

### carmensystems.basics.uuid.uuid — UUID support
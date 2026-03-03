## API reference


#### [`carmensystems.common.Config`](#module-carmensystems.common.Config "carmensystems.common.Config")

*class* `carmensystems.common.Config.``Config`(*configFile=None*, *debuglevel=0*)
:   This base class requires name attributes on:
    :   * system
        * component

    Public methods;

    > * getProperties(xpath\_key) -> [(full key, value),…] or []
    > * getProperty(xpath\_key) -> (full key, value) or (None, None)
    > * getPropertyValue(xpath\_key) -> value or None
    > * isChanged() -> boolean
    > * refresh() -> boolean

    `getProperties`(*xpath\_key*, *do\_expand=True*)
    :   Get list of (key, value) tuples for given xpath\_key.

        Will expand variables if do\_expand is True, which is the default.

        |  |  |
        | --- | --- |
        | Parameters: | **xpath\_key** – search key |
        | Returns: | list of (key, value) tuples. |
        | Raises: | **ValueError** – if the configuration can’t be parsed. |

    `getProperty`(*xpath\_key*)
    :   Get the first property (key, value) tuple found for given xpath\_key.

        A property may refer to other properties by including:
        $(p), %(p), ${p} or %{p} in the value. This will be replaced
        with the value of other\_property or remain unexpanded if not
        defined.

        See: [`getProperties`](#carmensystems.common.Config.Config.getProperties "carmensystems.common.Config.Config.getProperties")

        |  |  |
        | --- | --- |
        | Parameters: | **xpath\_key** – search key |
        | Returns: | (key, value) tuples. |
        | Raises: | **ValueError** – if the configuration can’t be parsed. |

    `getPropertyValue`(*xpath\_key*)
    :   Get the first property value found for given xpath\_key.

        See: [`getProperty`](#carmensystems.common.Config.Config.getProperty "carmensystems.common.Config.Config.getProperty")

        |  |  |
        | --- | --- |
        | Parameters: | **xpath\_key** – search key |
        | Returns: | value |
        | Raises: | **ValueError** – if the configuration can’t be parsed. |

    `isChanged`()
    :   Check if parsed configuration is changed on disk.

        Done by checking current parsed files modification time and the

        existens of all [include@href](mailto:include%40href) and theirs [fallback@hrefs](mailto:fallback%40hrefs).

        |  |  |
        | --- | --- |
        | Returns: | True if configuration is chanched since last refresh. |

    `refresh`()
    :   Reload configuration if changed on disk.

        See: [`isChanged`](#carmensystems.common.Config.Config.isChanged "carmensystems.common.Config.Config.isChanged")

        |  |  |
        | --- | --- |
        | Returns: | True if configuration is reloaded. |

#### [`carmensystems.common.ServiceConfig`](#module-carmensystems.common.ServiceConfig "carmensystems.common.ServiceConfig")

*class* `carmensystems.common.ServiceConfig.``ServiceConfig`(*configFile=None*, *debuglevel=0*)
:   Bases: [`carmensystems.common.Config.Config`](#carmensystems.common.Config.Config "carmensystems.common.Config.Config")

    A service config requires name attributes on:
    :   * interface
        * process
        * process\_group

    Additional public methods:

    > * getServiceUrl(service, process) -> url
    > * getServicePort(service, process) -> portno
    > * getServiceHostname(service, process) -> host
    > * getProcessProperties(self, relpath, program, process)
    > * getProcessProperty(self, relpath, program, process)
    > * getProcessPropertyValue(self, relpath, program, process)

    Static methods:

    > * version() -> (component name, version, description)

    `getProcessProperties`(*relpath*, *program*, *process*)
    :   Get list of key-value for the given relative xpath for a process.

        The following subtrees are searched:

        > * /config/programs/<program><process>/<xpath>
        > * /config/programs/<program>/<xpath>
        > * /config/global/default/<xpath>

        The values from the process, program and default
        are concatenated.

        See: `Config.getProperties`

        |  |  |
        | --- | --- |
        | Parameters: | * **relpath** – relative search key * **program** – program key * **process** – process key |
        | Returns: | array array of Strings where element 0 is the absolute xpath for |

        the match and element 1 is the value.

        |  |  |
        | --- | --- |
        | Raises: | **ValueError** – if the configuration can’t be parsed. |

    `getProcessProperty`(*relpath*, *program*, *process*)
    :   Get property key-value for the given relative xpath for a process.

        If there are multiple matches, the first one is returned. If
        no matches are found, the returned key and value are both None.

        See: [`getProcessProperties`](#carmensystems.common.ServiceConfig.ServiceConfig.getProcessProperties "carmensystems.common.ServiceConfig.ServiceConfig.getProcessProperties")

        |  |  |
        | --- | --- |
        | Parameters: | * **relpath** – relative search key * **program** – program key * **process** – process key |
        | Returns: | (key, value) Strings where key is the absolute xpath for |

        the match and value is the propery value

        |  |  |
        | --- | --- |
        | Raises: | **ValueError** – if the configuration can’t be parsed |

    `getProcessPropertyValue`(*relpath*, *program*, *process*)
    :   Get property value for the given relative xpath for a process.

        If there are multiple matches, the first one is returned. If
        no matches are found, the returned value is None.

        See: [`getProcessProperty`](#carmensystems.common.ServiceConfig.ServiceConfig.getProcessProperty "carmensystems.common.ServiceConfig.ServiceConfig.getProcessProperty")

        |  |  |
        | --- | --- |
        | Parameters: | * **relpath** – relative search key * **program** – program key * **process** – process key |
        | Returns: | String value of the property |
        | Raises: | **ValueError** – if the configuration can’t be parsed |

    `getServicePort`(*service*, *host=None*, *process=None*)
    :   Get listener port for the selected service, optionally on a host/process

        $see: [`get.ServiceUrl`](#carmensystems.common.ServiceConfig.ServiceConfig.getServiceUrl "carmensystems.common.ServiceConfig.ServiceConfig.getServiceUrl")

        |  |  |
        | --- | --- |
        | Parameters: | * **service** – service key * **host** – host key * **process** – process key |
        | Returns: | port number for the service |
        | Raises: | **ValueError** – if the configuration can’t be parsed. |

    `getServiceUrl`(*service*, *host=None*, *process=None*)
    :   Get url for the given service, optionally on a host/process

        |  |  |
        | --- | --- |
        | Parameters: | * **service** – service key * **host** – host key * **process** – process key |
        | Returns: | URL for the service |
        | Raises: | **ValueError** – if the configuration can’t be parsed. |

    *static* `version`()
    :   |  |  |
        | --- | --- |
        | Returns: | (name, version, description) of the module. |

### carmensystems.common.Config

### carmensystems.common.ServiceConfig
## API reference

### jcms.log — Base module

##### [`jcms.log`](#module-jcms.log "jcms.log") — Base module

`jcms.log.``init`(*appname=None*, *config=None*, *external=True*, *terse=False*, *force=False*)
:   Load definitions from common config and create logger instances
    accordingly, using `logging.config.fileConfig()`.

    If configuration fails, `logging.basicConfig()` will be called
    with format options as for the `SimpleFormatter` formatter.

    |  |  |
    | --- | --- |
    | Parameters: | * **appname** ([*str*](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Process/application name to use for configuration. Will be used   as RFC-5424 `APP-NAME` attribute if not specified at formatter   or message levels.  Used when searching within config paths:  ```   /system/config/programs/program/process   /system/config/programs/program   /system/config/applications/application   ```  Since value may be used as `APP-NAME` attribute, it must   contain RFC-5424 printable characters only, i e having   ascii values 33 - 126.  If not specified, the environment variable `CARM_PROCESS_NAME`   will be used as value. * **config** (*carmensystems.common.Config*) – Config instance to use. If not specified common config   default is used. * **external** ([*bool*](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – If set to True, SWIG-based external log module will   be called for initialization after successful configuration. * **terse** ([*bool*](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – If set to True, set logging optimizations to minimize system   information collected and hide exceptions as:  ```   logging._srcfile = None   logging.logThreads = 0   logging.logMultiprocessing = 0   logging.logProcesses = 0   logging.raiseExceptions = 0   ``` * **force** ([*bool*](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – If set to True jcmslog will reload the configuration even if   the new configuration in the XML file is identical with the   old XML configuration. |

`jcms.log.``set_log_level`(*logger\_name*, *log\_level*, *category=None*)
:   Set the log level on the logger\_name to the specified level.

    |  |  |
    | --- | --- |
    | Parameters: | * **logger\_name** ([*str*](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Name of the logger to change log level on * **log\_level** (*The logging module's log levels*) – * **category** – ‘’OPERATIONAL’‘, ‘’PERFORMANCE’‘, ‘’CONFIGURATION’‘.   Or ‘’None’’ (the default) if all categories should be set. |

`jcms.log.``reset_log_level`(*logger\_name*, *category=None*)
:   Reset the log level on the logger\_name back to the value it had
    in the configuration.

    |  |  |
    | --- | --- |
    | Parameters: | * **logger\_name** ([*str*](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Name of the logger to change log level on * **category** – ‘’OPERATIONAL’‘, ‘’PERFORMANCE’‘, ‘’CONFIGURATION’‘.   Or ‘’None’’ (the default) if all categories should be set. |

`jcms.log.``reset_all_loglevels`()
:   Reset all changed log levels back to the values specified in the
    configuration.

`jcms.log.``get_logger`(*name*)
:   Get logger for category operational.

    |  |  |
    | --- | --- |
    | Parameters: | **name** ([*str*](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Flow name as specified in config, e g `.` or `a.b.c` |
    | Returns: | Operational logger for name specified. |
    | Return type: | [logging.Logger](https://docs.python.org/2.7/library/logging.html#logging.Logger "(in Python v2.7)") |

`jcms.log.``get_performance_logger`(*name*)
:   Get logger for category performance.

    |  |  |
    | --- | --- |
    | Parameters: | **name** ([*str*](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Flow name as specified in config, e g `.` or `a.b.c` |
    | Returns: | Performance logger for name specified. |
    | Return type: | [logging.Logger](https://docs.python.org/2.7/library/logging.html#logging.Logger "(in Python v2.7)") |

`jcms.log.``get_configuration_logger`(*name*)
:   Get logger for category configuration.

    |  |  |
    | --- | --- |
    | Parameters: | **name** ([*str*](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Flow name as specified in config, e g `.` or `a.b.c` |
    | Returns: | Configuration logger for name specified. |
    | Return type: | [logging.Logger](https://docs.python.org/2.7/library/logging.html#logging.Logger "(in Python v2.7)") |

`jcms.log.``get_time_logger`(*name*, *level=10*)
:   Get logger for time-based logging with specified level. Wraps a
    performance logger. If logger isn’t enabled for level at time for call,
    a NOP logger will be returned.

    |  |  |
    | --- | --- |
    | Parameters: | * **name** ([*str*](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Flow name as specified in config, e g `.` or `a.b.c` * **level** ([*int*](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")) – Log level for messages. Will always be used for logging. |
    | Returns: | Time logger wrapping a performance logger for specified name, if enabled for specified level. Else a NOP time logger instance, which won’t perform any actions when its methods are called. |
    | Return type: | [TimeLogger](#jcms.log.TimeLogger "jcms.log.TimeLogger") |

`jcms.log.``get_flow_name_for_class`(*obj*)
:   Return a flow name based on the module and class name.

    |  |  |
    | --- | --- |
    | Parameters: | **obj** ([*object*](https://docs.python.org/2.7/library/functions.html#object "(in Python v2.7)")) – Object to get name for |
    | Returns: | Flow name based on object class path. |
    | Return type: | [str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)") |

*class* `jcms.log.``TimeLogger`(*logger*, *level*)
:   Wrapper class for `logging.Logger`, adding performance-related
    time information to log record as RFC-5424 structured data.

    `__init__`(*logger*, *level*)
    :   Creates a time logger object, logging at specified level. Starts
        timer corresponding to a `stop()` call. Increments
        thread-specific call-depth counter.

        |  |  |
        | --- | --- |
        | Parameters: | * **logger** ([*logging.Logger*](https://docs.python.org/2.7/library/logging.html#logging.Logger "(in Python v2.7)")) – Performance logger from `get_performance_logger()` call to use   for logging. If not enabled for level timer won’t be started. * **level** ([*int*](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")) – Log level for all messages created in `log()` call. |

    `isEnabled`()
    :   Get enabled state for logger.

        |  |  |
        | --- | --- |
        | Returns: | True if time logger is enabled for logging, else False |
        | Return type: | [bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)") |

    `log`(*msg*, *\*args*, *\*\*kwargs*)
    :   Log message after adding time information as structured data, with
        level specified at initialization. Delegates logging call to wrapped
        performance logger.
        Stops timer corresponding to `stop()` call.

        |  |  |
        | --- | --- |
        | Parameters: | * **msg** – Same parameter as for `logging.Logger.log()`. * **args** – Same parameter as for `logging.Logger.log()`. * **kwargs** – Same parameter as for `logging.Logger.log()`. |

    `start`()
    :   Start timer if suspended. Time from this point up to next
        `suspend()` or `stop()` call will be added to total time.

    `stop`()
    :   Stop timer if started and decrement thread-specific call-depth
        counter (once for instance). Time since last `start()` call
        (or init) added to total time. A stopped timer may not be restarted.

    `suspend`()
    :   Suspend timer if started. Time since last `start()` call (or init)
        added to total time.

*class* `jcms.log.``_MDC`
:   Class that implements the MDC behaviour. See <http://logback.qos.ch/manual/mdc.html>

    This class should not be instantiated. A default instance is available as
    module member `mdc`.

    Any instance of this class will be thread-local. The behaviour is quite
    similar to a dictionary object.

    Sample usage:

    ```
    from jcms.log import mdc

    mdc.example_key = "example_value"
    ```

    To empty the MDC if needed, call:

    ```
    mdc.clear()
    ```

    `__iter__`()

    `empty`()
    :   |  |  |
        | --- | --- |
        | Returns: | True if the object is empty |
        | Return type: | [bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)") |
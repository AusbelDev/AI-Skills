## Jcmslog Python package


This is an extension to the standard Python [`logging`](https://docs.python.org/2.7/library/logging.html#module-logging "(in Python v2.7)") package,
providing these additional features:

* A logging configurator using XML-based definitions.
* A formatter producing log records according to [**RFC 5424**](https://tools.ietf.org/html/rfc5424.html) syslog standard.
* A formatter to be used with the legacy carmlog server.
* A handler sending syslog records over TCP/IP.

API documentation is [here](api.html#jcmslog-api).

For details about configuration and usage, see [Jcmslog Documentation](../../log.doc/index.html).
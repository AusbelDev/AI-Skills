## IOServer


Document Information

*Doc Version:* DevGuide 1.0.104-SNAPSHOT, *Date:* 2023-11-06,
*Security Class:* External

This document describes the IOServer and the use of the testutils.

* [1. Introduction](introduction.html)
* [2. Concepts](concepts.html)
  + [2.1. IOServer process](concepts.html#ioserver-process)
  + [2.2. IOService](concepts.html#ioservice)
  + [2.3. Pattern](concepts.html#pattern)
  + [2.4. Handler](concepts.html#handler)
  + [2.5. Trigger](concepts.html#trigger)
  + [2.6. Plan generation](concepts.html#plan-generation)
* [3. Overview](overview.html)
* [4. Patterns](patterns.html)
  + [4.1. Subscriber](patterns.html#subscriber)
  + [4.2. Request/response](patterns.html#request-response)
  + [4.3. Trigger](patterns.html#trigger)
  + [4.4. Repeating trigger](patterns.html#repeating-trigger)
  + [4.5. Event trigger](patterns.html#event-trigger)
  + [4.6. Timer](patterns.html#timer)
  + [4.7. Dispatch](patterns.html#dispatch)
  + [4.8. Dispatch Scenario](patterns.html#dispatch-scenario)
* [5. Messaging](messaging.html)
  + [5.1. Communication protocol](messaging.html#communication-protocol)
  + [5.2. Application headers](messaging.html#application-headers)
    - [5.2.1. Incoming messages](messaging.html#incoming-messages)
    - [5.2.2. Outgoing messages](messaging.html#outgoing-messages)
* [6. Handler interface](handlers.html)
  + [6.1. Interface versions](handlers.html#interface-versions)
  + [6.2. Message types](handlers.html#message-types)
  + [6.3. Handler method](handlers.html#handler-method)
    - [6.3.1. Current Interface Version: TEN](handlers.html#current-interface-version-ten)
    - [6.3.2. Previous Interface Version: NINE](handlers.html#previous-interface-version-nine)
  + [6.4. on\_load](handlers.html#on-load)
    - [6.4.1. Current Interface Version: TEN](handlers.html#id2)
    - [6.4.2. Previous Interface Version: NINE](handlers.html#id3)
  + [6.5. on\_fault](handlers.html#on-fault)
    - [6.5.1. Current Interface Version: TEN](handlers.html#id4)
    - [6.5.2. Previous Interface Version: NINE](handlers.html#id5)
* [7. Trigger interface](triggers.html)
  + [7.1. Interface versions](triggers.html#interface-versions)
  + [7.2. Message types](triggers.html#message-types)
  + [7.3. on\_load](triggers.html#on-load)
  + [7.4. on\_event](triggers.html#on-event)
    - [7.4.1. Current Interface Version: TEN](triggers.html#current-interface-version-ten)
    - [7.4.2. Previous Interface Version: NINE](triggers.html#previous-interface-version-nine)
* [8. Migration](migration.html)
  + [8.1. Mandatory migration from interface version NINE to TEN](migration.html#mandatory-migration-from-interface-version-nine-to-ten)
    - [8.1.1. Python imports](migration.html#python-imports)
    - [8.1.2. Handler interface version](migration.html#handler-interface-version)
    - [8.1.3. The on\_load method](migration.html#the-on-load-method)
  + [8.2. Mandatory migration from interface version SEVEN to NINE](migration.html#mandatory-migration-from-interface-version-seven-to-nine)
    - [8.2.1. Python imports](migration.html#id1)
    - [8.2.2. Handler interface version](migration.html#id2)
    - [8.2.3. The on\_fault method](migration.html#the-on-fault-method)
    - [8.2.4. The on\_event method](migration.html#the-on-event-method)
    - [8.2.5. Accessing Rave rulesets](migration.html#accessing-rave-rulesets)
  + [8.3. Optional migration from version SEVEN to version NINE](migration.html#optional-migration-from-version-seven-to-version-nine)
    - [8.3.1. Access different viewpoints of the plan](migration.html#access-different-viewpoints-of-the-plan)
    - [8.3.2. Service context instead of handler context and trigger context](migration.html#service-context-instead-of-handler-context-and-trigger-context)
    - [8.3.3. Possible to save in repeatingtrigger](migration.html#possible-to-save-in-repeatingtrigger)
    - [8.3.4. Possible to use the same handler for plain and SOAP](migration.html#possible-to-use-the-same-handler-for-plain-and-soap)
  + [8.4. Mandatory migration in IOServer version 28.0.0](migration.html#mandatory-migration-in-ioserver-version-28-0-0)
    - [8.4.1. Multiple sinks must be named](migration.html#multiple-sinks-must-be-named)
  + [8.5. Recommended migration in IOServer version 28.0.0](migration.html#recommended-migration-in-ioserver-version-28-0-0)
    - [8.5.1. Change <skipconflict> to <conflict\_detection> in configuration](migration.html#change-skipconflict-to-conflict-detection-in-configuration)
    - [8.5.2. Use repeatingtrigger rather than timer + eventtrigger](migration.html#use-repeatingtrigger-rather-than-timer-eventtrigger)
  + [8.6. Mandatory migration in IOServer version 32.0.0](migration.html#mandatory-migration-in-ioserver-version-32-0-0)
    - [8.6.1. Configuration for data model has changed](migration.html#configuration-for-data-model-has-changed)
* [9. High Availability](high_availability.html)
  + [9.1. Active / Active](high_availability.html#active-active)
  + [9.2. Active / Passive](high_availability.html#active-passive)
  + [9.3. HA Store](high_availability.html#ha-store)
* [10. Error handling](error_handling.html)
  + [10.1. Trigger services](error_handling.html#trigger-services)
  + [10.2. Handler services](error_handling.html#handler-services)
  + [10.3. Deactivated services](error_handling.html#deactivated-services)
  + [10.4. Timed-out services](error_handling.html#timed-out-services)
  + [10.5. IOServer defined exceptions](error_handling.html#ioserver-defined-exceptions)
    - [10.5.1. Message errors](error_handling.html#message-errors)
    - [10.5.2. System errors (non-message errors)](error_handling.html#system-errors-non-message-errors)
* [11. Best Practices](best_practices.html)
  + [11.1. IOServices sharing IOServer](best_practices.html#ioservices-sharing-ioserver)
  + [11.2. Number of worker processes](best_practices.html#number-of-worker-processes)
  + [11.3. Services sharing worker](best_practices.html#services-sharing-worker)
  + [11.4. Pre-load of Rave tables](best_practices.html#pre-load-of-rave-tables)
  + [11.5. Running the same IOServices on different nodes](best_practices.html#running-the-same-ioservices-on-different-nodes)
  + [11.6. Monitoring service deactivation](best_practices.html#monitoring-service-deactivation)
  + [11.7. Worker time-out and pings](best_practices.html#worker-time-out-and-pings)
  + [11.8. Handling of errors in IOService](best_practices.html#handling-of-errors-in-ioservice)
* [12. Configuration](configuration.html)
  + [12.1. program](configuration.html#program)
  + [12.2. process](configuration.html#process)
  + [12.3. refresh](configuration.html#refresh)
  + [12.4. datamodel](configuration.html#datamodel)
    - [12.4.1. preload\_tables](configuration.html#preload-tables)
  + [12.5. db](configuration.html#db)
  + [12.6. ioservice](configuration.html#ioservice)
  + [12.7. pattern](configuration.html#pattern)
    - [12.7.1. jcmsstatemessagereplace](configuration.html#jcmsstatemessagereplace)
  + [12.8. binding](configuration.html#binding)
    - [12.8.1. profile](configuration.html#profile)
  + [12.9. source](configuration.html#source)
  + [12.10. sink](configuration.html#sink)
  + [12.11. message\_retention](configuration.html#message-retention)
  + [12.12. hastore](configuration.html#hastore)
  + [12.13. extra\_indexes](configuration.html#extra-indexes)
  + [12.14. refresh\_boundary](configuration.html#refresh-boundary)
  + [12.15. errors](configuration.html#errors)
    - [12.15.1. retrycount](configuration.html#retrycount)
    - [12.15.2. blockmsg](configuration.html#blockmsg)
  + [12.16. dispatch](configuration.html#dispatch)
  + [12.17. Dispatch Scenario](configuration.html#dispatch-scenario)
* [13. Command-line arguments](starting_ioserver.html)
* [14. Cmsshell integration](cmsshell.html)
  + [14.1. cmsshell plugin](cmsshell.html#cmsshell-plugin)
    - [14.1.1. help](cmsshell.html#help)
    - [14.1.2. clear\_hastore](cmsshell.html#clear-hastore)
    - [14.1.3. list\_config](cmsshell.html#list-config)
    - [14.1.4. selftest](cmsshell.html#selftest)
    - [14.1.5. service](cmsshell.html#service)
  + [14.2. Self tests](cmsshell.html#self-tests)
    - [14.2.1. Queues](cmsshell.html#queues)
    - [14.2.2. Processes](cmsshell.html#processes)
    - [14.2.3. Services](cmsshell.html#services)
* [15. IOServer control tool](ioserver_control_tool.html)
  + [15.1. Purpose](ioserver_control_tool.html#purpose)
  + [15.2. Command-line arguments](ioserver_control_tool.html#command-line-arguments)
  + [15.3. Examples](ioserver_control_tool.html#examples)
* [16. IOServer Python API reference](python_api_reference.html)
  + [16.1. IOServer Python API Reference Version 10](python_api_reference.html#ioserver-python-api-reference-version-10)
    - [16.1.1. `jcms.ioserver.versions`](python_api_ver10_reference.html)
    - [16.1.2. `jcms.ioserver.constants`](python_api_ver10_reference.html#jcms-ioserver-constants)
    - [16.1.3. `jcms.ioserver.exceptions`](python_api_ver10_reference.html#jcms-ioserver-exceptions)
    - [16.1.4. `jcms.ioserver.version10.config`](python_api_ver10_reference.html#module-jcms.ioserver.version10.config)
    - [16.1.5. `jcms.ioserver.version10.actions`](python_api_ver10_reference.html#module-jcms.ioserver.version10.actions)
    - [16.1.6. `jcms.ioserver.version10.message`](python_api_ver10_reference.html#module-jcms.ioserver.version10.message)
    - [16.1.7. `jcms.ioserver.version10.context`](python_api_ver10_reference.html#module-jcms.ioserver.version10.context)
    - [16.1.8. `jcms.ioserver.version10.mave2.IPlanHolder`](python_api_ver10_reference.html#jcms-ioserver-version10-mave2-iplanholder)
  + [16.2. IOServer Python API Reference Version 9](python_api_reference.html#ioserver-python-api-reference-version-9)
    - [16.2.1. `jcms.ioserver.versions`](python_api_ver9_reference.html)
    - [16.2.2. `jcms.ioserver.constants`](python_api_ver9_reference.html#jcms-ioserver-constants)
    - [16.2.3. `jcms.ioserver.exceptions`](python_api_ver9_reference.html#jcms-ioserver-exceptions)
    - [16.2.4. `jcms.ioserver.version9.config`](python_api_ver9_reference.html#module-jcms.ioserver.version9.config)
    - [16.2.5. `jcms.ioserver.version9.actions`](python_api_ver9_reference.html#module-jcms.ioserver.version9.actions)
    - [16.2.6. `jcms.ioserver.version9.message`](python_api_ver9_reference.html#module-jcms.ioserver.version9.message)
    - [16.2.7. `jcms.ioserver.version9.context`](python_api_ver9_reference.html#module-jcms.ioserver.version9.context)
    - [16.2.8. `jcms.ioserver.version9.mave2.IPlanHolder`](python_api_ver9_reference.html#jcms-ioserver-version9-mave2-iplanholder)
* [17. Testutils Python API reference](python_api_reference.html#testutils-python-api-reference)
  + [17.1. TestUtils Python API Reference Version 10](python_api_reference.html#testutils-python-api-reference-version-10)
    - [17.1.1. Conflict Detection Strategy Constants](python_testutils_api_ver10_reference.html)
    - [17.1.2. `jcms.ioserver.testutils.version10.main.TestMain`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-main-testmain)
    - [17.1.3. `jcms.ioserver.testutils.version10.main.IMemoryHAStore`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-main-imemoryhastore)
    - [17.1.4. `jcms.ioserver.testutils.version10.main.IMemoryQueue`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-main-imemoryqueue)
    - [17.1.5. `jcms.ioserver.testutils.version10.main.ITestConfig`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-main-itestconfig)
    - [17.1.6. `jcms.ioserver.testutils.version10.TestRunner`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-testrunner)
  + [17.2. TestUtils Python API Reference Version 9](python_api_reference.html#testutils-python-api-reference-version-9)
    - [17.2.1. `jcms.ioserver.testutils.version9.main.TestMain`](python_testutils_api_ver9_reference.html)
    - [17.2.2. `jcms.ioserver.testutils.version9.main.IMemoryHAStore`](python_testutils_api_ver9_reference.html#jcms-ioserver-testutils-version9-main-imemoryhastore)
    - [17.2.3. `jcms.ioserver.testutils.version9.main.IMemoryQueue`](python_testutils_api_ver9_reference.html#jcms-ioserver-testutils-version9-main-imemoryqueue)
    - [17.2.4. `jcms.ioserver.testutils.version9.main.ITestConfig`](python_testutils_api_ver9_reference.html#jcms-ioserver-testutils-version9-main-itestconfig)
    - [17.2.5. `jcms.ioserver.testutils.version9.TestRunner`](python_testutils_api_ver9_reference.html#jcms-ioserver-testutils-version9-testrunner)
* [18. IOServer logs](logging.html)
  + [18.1. Configuring logging](logging.html#configuring-logging)
  + [18.2. Flow](logging.html#flow)
  + [18.3. Logging from an IOService](logging.html#logging-from-an-ioservice)
  + [18.4. Getting the correct log level for an integration service](logging.html#getting-the-correct-log-level-for-an-integration-service)
    - [18.4.1. Log level contents](logging.html#log-level-contents)
  + [18.5. Connecting log entries to messages](logging.html#connecting-log-entries-to-messages)
  + [18.6. Log format](logging.html#log-format)
* [19. IOServer TestUtils](testutils.html)
  + [19.1. How to use TestUtils](testutils.html#how-to-use-testutils)
    - [19.1.1. How to setup initial data to reuse between tests](testutils.html#how-to-setup-initial-data-to-reuse-between-tests)
    - [19.1.2. Logging with testutils](testutils.html#logging-with-testutils)
* [20. Configuration only relevant for testing](testutils.html#configuration-only-relevant-for-testing)
  + [20.1. datamodel](testutils.html#datamodel)
  + [20.2. pattern](testutils.html#pattern)
  + [20.3. simulated time](testutils.html#simulated-time)
    - [20.3.1. Simulated time configuration](testutils.html#simulated-time-configuration)
    - [20.3.2. Limitations](testutils.html#limitations)
* [21. IOServer Metrics](metrics.html)
  + [21.1. Process metrics](metrics.html#process-metrics)
  + [21.2. Service metrics](metrics.html#service-metrics)
* [22. Message Retention](message_retention.html)
  + [22.1. Example Content of a Metadata Message](message_retention.html#example-content-of-a-metadata-message)
  + [22.2. Application Context](message_retention.html#application-context)

### Introduction

### Concepts


##### 2.1. IOServer process

An IOServer process loads a single plan (data context) that can be used by one or more IOServices.

##### 2.2. IOService

An IOService is a service running on an IOServer instance. It can fetch messages from a message source or react on events,
handle them, and provide responses. The service-specific logic is placed in a handler or trigger.
Timer services do not need a handler or trigger, but produce event messages based on a
configured timing.

Services sharing the same plan can be handled by a single IOServer process.

##### 2.3. Pattern

A pattern is an implementation of the framework for handling a particular class of services with common
characteristics. See [Patterns](patterns.html#pattern-top).

##### 2.4. Handler

A handler is a service-specific piece of Python code that is called when a request is
received from a message source. The handler interprets the request and performs the appropriate actions,
which can include applying changes to the loaded plan, doing business evaluations, and formulating
a response. The actual save is done by the IOServer framework, not the handler.

##### 2.5. Trigger

A trigger is a service-specific piece of Python code that is called based on events.

A *trigger* event occurs every time IOServer loads a new change set into the cached plan. The
trigger evaluates the change set and checks for types of changes that should lead to actions,
typically producing messages. A common use case is feeding data changes to downstream systems
online.

An *eventtrigger* event is typically generated by a timer. The trigger evaluates the
current state of the plan to detect needed actions based on the data state and current time. The
typical use case is to produce and send messages on a time condition, for example two
hours before a flight departure.

A variant of the *eventtrigger* is the *repeatingtrigger*, which is executed repeatedly with a
configured delay between the executions. Alternatively, it can be configured with a cron style time
specification, similar to the timer used by *eventtrigger*.

##### 2.6. Plan generation

There is a single generation of the plan holder/builder called “mave2”, which
is used on both the Studio (Major Release) and Atrium architectures.

#### IOServer process

#### IOService

#### Pattern

#### Handler

#### Trigger

#### Plan generation

### Overview

### Patterns


The IOServer framework has a set of patterns that implement common use cases of I/O interfaces.

##### 4.1. Subscriber

The subscriber pattern serves inbound interfaces that update the database based
on incoming messages. Typically the response messages have no data, but may contain
acknowledge, status, or fault messages.

In this pattern incoming messages may be processed in chunks, so that more than
one message is processed in one go.

The database save happens based on these conditions:
:   * If the maximum number of messages to aggregate has been reached.
    * If the maximum time in milliseconds to wait for incoming messages has been reached.
      The intention is to not have handled messages unsaved for longer than necessary in case of
      an empty queue.
    * If the maximum time in seconds that the subscriber can spend aggregating messages
      has been reached.

The error handling can be configured to behave differently based on the error type and the
error context, see [the error paragraph in the configuration chapter](configuration.html#conf-errors).
The final action when handling an error is either skip or block.

##### 4.2. Request/response

The request/response pattern serves interfaces where a request message is received, and an
output message with requested data is returned.

In this pattern messages are processed one by one, and not in chunks.

This pattern may update the plan as well, so the handler can specify that
the pattern implementation should save the modified plan.

##### 4.3. Trigger

The trigger pattern executes a trigger based on database changes, causing outgoing
messages to be sent.

In trigger interface version NINE and higher, a trigger can make changes
and have the pattern implementation save them in the plan.
However, as the changes are likely to be part of the next triggered change set,
much care must be taken in the trigger code (in the `on_event`
method) so that it does not trigger on its own changes and creates an endless
loop.

If the trigger throws any exception, the current state is not
regarded successfully handled and the change set presented next time will be
bigger. If the trigger does not throw an exception, the current state is
considered successfully handled, no matter whether any messages were emitted,
and the next run does not show the changes again.

##### 4.4. Repeating trigger

The repeating trigger pattern repeatedly executes a trigger according to a given delay
or a cron style time specification.

The typical use case is to send outgoing messages that are not dependent on
changes to the plan.

In trigger interface version NINE and higher, a repeating trigger can make changes
and have the pattern implementation save them in the plan.
If there are errors in the trigger or when saving, both the plan changes and
the outgoing messages are rolled back.

##### 4.5. Event trigger

The event trigger pattern executes a trigger when an incoming message arrives.
The message content is ignored, only its arrival is of importance.

This is typically used together with the timer pattern to trigger at specific times.

In trigger interface version NINE and higher, an event trigger can make changes
and have the pattern implementation save them in the plan.
If there are errors in the trigger or when saving, both the plan changes and
the outgoing messages are rolled back.

##### 4.6. Timer

The timer pattern sends an empty message based on a simplified cron based timer.

This is typically used together with the event trigger pattern to trigger at specific times.

There is no way to call a handler or trigger in the timer pattern itself.

##### 4.7. Dispatch

Not strictly speaking an IOServer pattern, the dispatch feature groups handlers together into a
“super-service”, which is able to monitor multiple queues, and route messages to different
sub-handlers depending on what queue a message came in on.

Each of these sub-handers must adhere to the same handler interface as a normal handler,
specifically they must use the same [Interface versions](handlers.html#handler-interface-version) as the dispatcher itself.
Essentially becoming part of a common service, each sub-handler will share the common characteristics
of the service, i.e. sharing `pattern`, `binding` etc. (see [ioservice](configuration.html#conf-ioservice)).

The dispatch feature has two main use-cases:

* A single service supporting multiple versions of messages by directing them to different handlers.
* Grouping multiple services in order to share workers, thus reducing the total number of workers
  needed to run the services. Mostly useful for low-frequency services (see best practices,
  section [Services sharing worker](best_practices.html#best-practices-worker-sharing)).

For configuration, see [dispatch](configuration.html#conf-dispatch).

##### 4.8. Dispatch Scenario

Note

Supported only on Python 3

Same usage pattern as [Dispatch](#pattern-dispatch), but the result will *not be saved* to the live plan,
it will only be saved into a scenario.

For configuration, see [Dispatch Scenario](configuration.html#conf-dispatch-scenario).

Each request message that is handled by the `jcms.ioserver.version10.dispatch_scenario_handler`
can have the following properties set in the header. The properties will be written to the scenario.

| Sub-element | Mandatory | Type | Description |
| --- | --- | --- | --- |
| `jcms_scenario_name` | Yes | string | The name of the scenario. |
| `jcms_scenario_author` | No | string | The name of the author of the scenario. |
| `jcms_scenario_description` | No | string | The description of the scenario. |
| `jcms_scenario_source_system` | No | string | The system which sent the scenario. |
| `jcms_scenario_reference` | No | string | The scenario ID in the source system. |

#### Subscriber

#### Request/response

#### Trigger

#### Repeating trigger

#### Event trigger

#### Timer

#### Dispatch

#### Dispatch Scenario

### Messaging


##### 5.1. Communication protocol

Messages are typically received and sent using Apache Qpid or Apache ActiveMQ brokers.
In both cases, IOServer uses Qpid client libraries for source and sink.
This works because both brokers support the AMQP protocol,
albeit with different protocol versions.

| Broker | Protocol |
| --- | --- |
| Qpid | amqp0-10 |
| ActiveMQ | amqp1.0 |

##### 5.2. Application headers

IOServer uses some application-specific headers in messages.

###### 5.2.1. Incoming messages

IOServer recognizes the following application headers in incoming messages:

| Application header | Type | Description |
| --- | --- | --- |
| `jcms_role` | string | cacs role to use when handling the request |
| `jcms_state` | integer | state of the plan that the request is based on (The Dave commit id.) |
| `jcms_client` | string | name of client user |
| `jcms_crew` | string | crew ID for the crew that a request concerns |
| `jcms_traceid` | string | trace ID logged in the MDC area (as X-B3-TraceId) in the log file |

IOServer adds the following headers in its incoming messages:

| Application header | Type | Description |
| --- | --- | --- |
| `jcms_source_queue` | string | name of the queue reference the message came in on, as specified in the configuration. |

###### 5.2.2. Outgoing messages

IOServer adds the following headers in outgoing messages:

| Application header | Type | Description |
| --- | --- | --- |
| `jcms_responsecode` | string | Status about how IOServer managed to handle the incoming message. |
| `jcms_state` | integer | The state of the plan when the request handled. (The Dave commit id) |
| `jcms_traceid` | string | Copied from the incoming message. |

#### Communication protocol

#### Application headers

##### Incoming messages

##### Outgoing messages

### Handler interface


A handler is a Python module that implements methods for
all operations in the format specification of the messages it handles.

##### 6.1. Interface versions

IOServer supports handlers with different versions of the handler interface at the same time.
The current version is version TEN, but all supported versions are enumerated in the
`jcms.ioserver.versions.InterfaceVersion` Python class.

To determine which interface version a handler implements IOServer calls a special method,
`handler_interface_version`, which should return one of the following values:

| Return value | Interface |
| --- | --- |
| `InterfaceVersion.NINE` | version NINE (**deprecated**) |
| `InterfaceVersion.TEN` | version TEN |

##### 6.2. Message types

Depending on the configuration of a handler, IOServer interprets the messages exchanged with the handler
in one of the following ways:

SOAP-XML handler
:   The exchanged messages are expected to be SOAP envelopes
    and the request is the (single) child of the SOAP body element.

Plain text handler
:   The exchanged messages can be of any format and no
    interpretation is made outside of the handler.

The type of messages to use is defined by the `protocol` tag in the [binding](configuration.html#conf-binding) section
of the handler configuration.
If `protocol` is set to `mixed`, the decision to use SOAP or plain text is based on the content type
of the incoming message.

##### 6.3. Handler method

When calling a handler, IOServer finds the name of the method to use in one of the following ways:

* For a SOAP-XML handler, the name is read from the `SOAPAction` message header.
* For a plain text handler, the name is read from the handler configuration. The default name is `handle`.

###### 6.3.1. Current Interface Version: TEN

In handler interface version TEN, the handler method has the following signature:

```
<method_name>(planholder, service_context)
```

The `planholder` argument is a version TEN `IPlanHolder` object, which gives
access to the ARA plan and ruleset currently loaded in IOServer.
There are two variants of the `planholder` object, `version10.planholder_macao`
for the Atrium architecture and `version10.planholder_militaris` for the Studio architecture.
Which variant to use is specified by the `planholder` setting in the configuration.

The `service_context` argument is a [`version10.context.ServiceContext`](python_api_ver10_reference.html#jcms.ioserver.version10.context.ServiceContext "jcms.ioserver.version10.context.ServiceContext") object,
from which the handler can retrieve the request message and set response message.
The service context also provides additional information, for example access to the configuration.

The [`version10.context.ServiceContext`](python_api_ver10_reference.html#jcms.ioserver.version10.context.ServiceContext "jcms.ioserver.version10.context.ServiceContext") that is used by handlers is the same that is used by triggers.

The handler method has to return one of the following values, defined in [`version10.actions.PlanAction`](python_api_ver10_reference.html#jcms.ioserver.version10.actions.PlanAction "jcms.ioserver.version10.actions.PlanAction"):

`PlanAction.UNCHANGED`
:   no changes in the plan, nothing needs to be saved

`PlanAction.SAVE`
:   changes in the plan need to be saved

`PlanAction.ROLLBACK`
:   changes in the plan must be rolled back.

When the plan action has been executed successfully, any provided response message is sent out
and the request is removed from the in queue.

####### 6.3.1.1. The ContentModel API

The `ContentModel` API parses `SoapIOMessages` and has two variants;
`version10.PyxbContent` for pyxb, and `version10.LxmlContent` for Lxml.

The nodes are created by using a factory, as shown in the following example:

> ```
> import jcms.ioserver.version10.LxmlContent as ContentModel
>
> # Create a factory for SOAP messages.
> # LxmlContentFactory accepts xsd and soap_xsd as either strings (as in this example)
> # or file paths.
> xsd = open('MyService.xsd').read()
> soap_xsd = open('Envelope.xsd').read()
> factory = ContentModel.LxmlContentFactory(xsd, tnsname="myservice", soap_xsd=soap_xsd)
>
> # Parse request message using factory.
> payload = factory.parseMsgAndGetPayload(handler_context.request_message)
> print payload.attribute
> # ...
>
> # Create a response.
> response_msg = handler_context.create_io_message("")
> response_payload = factory.makeNode("MyResponseType", "response")
> response_payload.myString = "some string"
>
> # Add payload to message.
> factory.formatMsgAndSetPayload(response_msg, response_payload)
> handler_context.response_message = response_msg
> ```

###### 6.3.2. Previous Interface Version: NINE

Warning

This API version is deprecated and will be removed in a future ioserver release.

In handler interface version NINE, the handler method has the following signature:

```
<method_name>(planholder, service_context)
```

The `planholder` argument is a version NINE `IPlanHolder` object, which gives
access to the ARA plan and rule set currently loaded in IOServer.
There are two variants of the `planholder` object, `version9.planholder_macao`
for the Atrium architecture and `version9.planholder_militaris` for the Studio architecture.
Which variant to use is specified by the `planbuilder` setting in the configuration.

With the Atrium version of the `planholder` object, handlers must use the RaveSession APIs to access rule sets.

The `service_context` argument is a [`version9.context.ServiceContext`](python_api_ver9_reference.html#jcms.ioserver.version9.context.ServiceContext "jcms.ioserver.version9.context.ServiceContext") object,
from which the handler can retrieve the request message and set response message.
The service context also provides additional information, for example access to the configuration.
Handlers and triggers use the same service context.
Note that some convenience methods that were present in earlier versions have been removed.

The handler method has to return one of the following values, defined in [`version9.actions.PlanAction`](python_api_ver9_reference.html#jcms.ioserver.version9.actions.PlanAction "jcms.ioserver.version9.actions.PlanAction"):

`PlanAction.UNCHANGED`
:   no changes in the plan, nothing needs to be saved

`PlanAction.SAVE`
:   changes in the plan need to be saved

`PlanAction.ROLLBACK`
:   changes in the plan must be rolled back.

When the plan action has been executed successfully, any provided response message is sent out
and the request is removed from the in queue.

####### 6.3.2.1. The ContentModel API

The `ContentModel` API parses `SoapIOMessages` and has two variants;
`version9.PyxbContent` for pyxb, and `version9.LxmlContent` for Lxml.

The nodes are created by using a factory, as shown in the following example:

> ```
> import jcms.ioserver.version9.LxmlContent as ContentModel
>
> # Create a factory for SOAP messages.
> # LxmlContentFactory accepts xsd and soap_xsd as either strings (as in this example)
> # or file paths.
> xsd = open('MyService.xsd').read()
> soap_xsd = open('Envelope.xsd').read()
> factory = ContentModel.LxmlContentFactory(xsd, tnsname="myservice", soap_xsd=soap_xsd)
>
> # Parse request message using factory.
> payload = factory.parseMsgAndGetPayload(handler_context.request_message)
> print payload.attribute
> # ...
>
> # Create a response.
> response_msg = handler_context.create_io_message("")
> response_payload = factory.makeNode("MyResponseType", "response")
> response_payload.myString = "some string"
>
> # Add payload to message.
> factory.formatMsgAndSetPayload(response_msg, response_payload)
> handler_context.response_message = response_msg
> ```

##### 6.4. on\_load

A handler may implement a method called `on_load`.
This method is called once just after the plan has been loaded,
and can be used to cache and share objects between workers.
Note that any modifications to the plan, such as setting up indices, are shared by all IOServices.

###### 6.4.1. Current Interface Version: TEN

The `on_load` method has the following signature:

```
on_load(planholder, context)
```

The `planholder` argument is a `planholder` object, which gives
access to the ARA plan and rule set currently loaded in IOServer.

The `context` argument is a [`version10.context.OnLoadServiceContext`](python_api_ver10_reference.html#jcms.ioserver.version10.context.OnLoadServiceContext "jcms.ioserver.version10.context.OnLoadServiceContext"),
which provides service name and configuration to the handler.

The `on_load` method does not have to return anything.

###### 6.4.2. Previous Interface Version: NINE

The `on_load` method has the following signature:

```
on_load(planholder)
```

The `planholder` argument is a `planholder` object, which gives
access to the ARA plan and rule set currently loaded in IOServer.

The `on_load` method does not have to return anything.

##### 6.5. on\_fault

A handler may implement a method called `on_fault`.
This method is called when an error occurs, and lets the handler influence what type of
error response to send.

###### 6.5.1. Current Interface Version: TEN

In handler interface version TEN, the `on_fault` method has the following signature:

```
on_fault(planholder, service_context, exception)
```

The `planholder` argument is a version TEN `IPlanHolder` object, which gives
access to the ARA plan and ruleset currently loaded in IOServer.

The `service_context` argument is the service context, the same as passed to the handler method.

The `exception` argument is the raised exception.

The possible return values are defined in [`version10.actions.FaultAction`](python_api_ver10_reference.html#jcms.ioserver.version10.actions.FaultAction "jcms.ioserver.version10.actions.FaultAction").
There are three possible actions the `on_fault` method can take:

* Set a custom response message in the service context, and return `FaultAction.SEND_RESPONSE`.
  In this case the response will be sent.
* Return `FaultAction.NO_RESPONSE`.
  In this case no response message is sent, even if one was set.
* Return `FaultAction.DEFAULT_RESPONSE`.
  In this case the default response action for the given protocol is taken.
  For the `plain` protocol the error is logged and no response message is sent.
  For the `soap` protocol the error generates a standard SOAP fault message.

###### 6.5.2. Previous Interface Version: NINE

In handler interface version NINE, the `on_fault` method has the following signature:

```
on_fault(planholder, service_context, exception)
```

The `planholder` and `service_context` arguments are the same as passed to the handler method.

The `exception` argument is the raised exception.

The possible return values are defined in [`version9.actions.FaultAction`](python_api_ver9_reference.html#jcms.ioserver.version9.actions.FaultAction "jcms.ioserver.version9.actions.FaultAction").
There are three possible actions the `on_fault` method can take:

* Set a custom response message in the service context, and return `FaultAction.SEND_RESPONSE`.
  In this case the response is sent.
* Return `FaultAction.NO_RESPONSE`.
  In this case no response message is sent, even if one was set.
* Return `FaultAction.DEFAULT_RESPONSE`.
  In this case the default response action for the given protocol is taken.
  For the `plain` protocol the error is logged and no response message is sent.
  For the `soap` protocol the error generates a standard SOAP fault message.

#### Interface versions

#### Message types

#### Handler method

##### Current Interface Version: TEN

###### The ContentModel API

##### Previous Interface Version: NINE

###### The ContentModel API

#### on_load

##### Current Interface Version: TEN

##### Previous Interface Version: NINE

#### on_fault

##### Current Interface Version: TEN

##### Previous Interface Version: NINE

### Trigger interface


A trigger is a Python module that implements methods for the trigger interface,
which consists of the `on_load` and `on_event` methods.

##### 7.1. Interface versions

As for handlers, IOServer supports triggers with different versions of the trigger interface at the same time.
The current version is version TEN, but all supported versions are enumerated in the
`jcms.ioserver.versions.InterfaceVersion` Python class.

To determine which interface version a trigger implements IOServer calls a special method,
`handler_interface_version`, which should return one of the following values:

| Return value | Interface |
| --- | --- |
| `InterfaceVersion.NINE` | version NINE (**deprecated**) |
| `InterfaceVersion.TEN` | version TEN |

##### 7.2. Message types

Triggers can use both the SOAP and plain text protocols, just as [handlers](handlers.html#handler-messages),
but the `mixed` option is not available.

##### 7.3. on\_load

For a description of the `on_load` method, see the [handler interface](handlers.html#handler-on-load).

##### 7.4. on\_event

The `on_event` method is called according to the [pattern](patterns.html#pattern-top) given in the configuration.

For the `trigger` pattern this happens when the plan is changed in the
latest refresh. In this case the `ChangeSet` property of the `PlanHolder` object can be used to determine if the
changes are relevant for the `on_event` method.

For timer-based trigger patterns, such as `repeatingtrigger` and `timer` + `eventtrigger`, the `on_event` method
is typically called regularly based on timer events.

Usually the `on_event` method sends outgoing messages by using methods available in the `service_context` object.

###### 7.4.1. Current Interface Version: TEN

In trigger interface version TEN, the `on_event` method has the following signature:

```
on_event(planholder, service_context)
```

The `planholder` argument is a version TEN `IPlanHolder` object. It supports the RaveSession APIs
and gives access to the ARA plan and rule set currently loaded in IOServer.
There are two variants of the `planholder` object, `version10.planholder_macao`
for the Atrium architecture and `version10.planholder_militaris` for the Studio architecture.
Which variant to use is specified by the `planbuilder` setting in the configuration.

The `service_context` argument is a [`version10.context.ServiceContext`](python_api_ver10_reference.html#jcms.ioserver.version10.context.ServiceContext "jcms.ioserver.version10.context.ServiceContext") object,
from which the trigger can create and send the generated requests.
The service context also provides additional information, for example access to the configuration.

The `service_context` that is used by triggers is the same that is used by handlers.

The `on_event` method has to return one of the following values, defined in the [`version10.actions.PlanAction`](python_api_ver10_reference.html#jcms.ioserver.version10.actions.PlanAction "jcms.ioserver.version10.actions.PlanAction") class:

`PlanAction.UNCHANGED`
:   no changes in the plan, nothing needs to be saved

`PlanAction.SAVE`
:   changes in the plan need to be saved

`PlanAction.ROLLBACK`
:   changes in the plan must be rolled back.

When the plan action has been executed successfully, any messages the `on_event` method has sent are
committed to the outgoing queue. If there was an error, any uncommitted outgoing messages are rolled back.

Note

The possiliblity to save plan changes caused by an `on_event` method is primarily intended for timer based trigger
patterns, such as `repeatingtrigger` or `eventtrigger`, but it can be done in a `trigger` pattern as well.
In that case care must be taken so that the `on_event` method does not trigger on its own changes,
thus creating an endless loop.

Note

`PlanAction.SAVE` is not allowed when using stepwise refresh mode, see [refresh\_boundary](configuration.html#conf-refresh-boundary) configuration.
This causes the service to be disabled.

###### 7.4.2. Previous Interface Version: NINE

Warning

This API version is deprecated and will be removed in a future IOServer release.

In trigger interface version NINE, the `on_event` method has the following signature:

```
on_event(planholder, service_context)
```

The `planholder` argument is a version NINE `IPlanHolder` object, which gives
access to the ARA plan and rule set currently loaded in IOServer.
There are two variants of the `planholder` object, `version9.planholder_macao`
for the Atrium architecture and `version9.planholder_militaris` for the Studio architecture.
Which variant to use is specified by the `planbuilder` setting in the configuration.
With the Atrium variant of the `planholder` object, triggers must use the RaveSession APIs to access rule sets.

The `service_context` argument is a [`version9.context.ServiceContext`](python_api_ver9_reference.html#jcms.ioserver.version9.context.ServiceContext "jcms.ioserver.version9.context.ServiceContext") object,
from which the trigger can retrieve the request message and set response message.
The service context also provides additional information, for example access to the configuration.
Handlers and triggers use the same service context.

The `on_event` method has to return one of the following values, defined in the [`version9.actions.PlanAction`](python_api_ver9_reference.html#jcms.ioserver.version9.actions.PlanAction "jcms.ioserver.version9.actions.PlanAction") class:

`PlanAction.UNCHANGED`
:   no changes in the plan, nothing needs to be saved

`PlanAction.SAVE`
:   changes in the plan need to be saved

`PlanAction.ROLLBACK`
:   changes in the plan must be rolled back.

When the plan action has been executed successfully, any messages the `on_event` method has sent are
committed to the outgoing queue. If there was an error, any uncommitted outgoing messages are rolled back.

Note

The possiliblity to save plan changes caused by an `on_event` method is primarily intended for timer based trigger
patterns, such as `repeatingtrigger` or `eventtrigger`, but it can be done in a `trigger` pattern as well.
In that case care must be taken so that the `on_event` method does not trigger on its own changes,
thus creating an endless loop.

Note

`PlanAction.SAVE` is not allowed when using stepwise refresh mode, see [refresh\_boundary](configuration.html#conf-refresh-boundary) configuration.
This causes the service to be disabled.

#### Interface versions

#### Message types

#### on_load

#### on_event

##### Current Interface Version: TEN

##### Previous Interface Version: NINE

### Migration


##### 8.1. Mandatory migration from interface version NINE to TEN

###### 8.1.1. Python imports

Python import specifications need to refer to `version10` instead of `version9`.

###### 8.1.2. Handler interface version

The `handler_interface_version` method must return `InterfaceVersion.TEN`.

###### 8.1.3. The on\_load method

The signature of the `on_load` method has changed, and now takes an additional `context`
argument, see [on\_load](handlers.html#handler-on-load).

Implementations of `on_load` must be migrated to take the `context` argument.
This applies to both Handlers and Triggers.

##### 8.2. Mandatory migration from interface version SEVEN to NINE

###### 8.2.1. Python imports

Python import specifications need to refer to `version9` instead of `version7`.

###### 8.2.2. Handler interface version

The `handler_interface_version` method must return `InterfaceVersion.NINE`.

###### 8.2.3. The on\_fault method

The signature of the `on_fault` method in handler modules has been changed and
now takes an additional `planholder` argument, see [on\_fault](handlers.html#handler-on-fault).

Implementations of `on_fault` must be migrated to take the `planholder` argument.

###### 8.2.4. The on\_event method

Trigger services may now save data. For this reason the `on_event` methods must return
a `PlanAction`, just as handler methods do. See [on\_event](triggers.html#trigger-on-event) for details.

###### 8.2.5. Accessing Rave rulesets

In interface versions SIX and SEVEN there were two ways to access Rave rule sets
when using the Mave2 version of the `planholder` object:

* Using the `getRuleset` method (or `getMave2Ruleset`) on `planholder`. **No longer supported.**
* Using the `getRaveSession` method on `planholder`, and then use the ARA
  RaveSession APIs.

In version NINE, only the second variant is available and all code using the the first
variant must be migrated to use `getRaveSession` instead.

Warning

The `brave2` variant is no longer supported for any version.

Warning

Versions SIX and SEVEN of the IOServer API are deprecated and will be removed
in a future IOServer release.

##### 8.3. Optional migration from version SEVEN to version NINE

###### 8.3.1. Access different viewpoints of the plan

For handler or trigger code that needs to access both live and
published data, the following new utility methods on the Mave2 planholder may be useful:

`getMave2PlanWithViewpoint(dataset)`
:   returns the ARA plan with the Viewpoint for the specified dataset.

`getRaveSessionWithViewpoint(dataset)`
:   returns the RaveSession associated with the ARA plan with the Viewpoint for the specified dataset.

See the ARA documentation for an explanation of Plan Viewpoints.

###### 8.3.2. Service context instead of handler context and trigger context

In version SEVEN and earlier, different types were passed
to handlers (handler context) and triggers (trigger context) to provide
context and utility functions.

These types have been merged to a common type (service context) in
version NINE.
There is no required migration for this, as the new type contains
all methods that were available in the old types.

Optionally the name of the arguments to the handler methods, `on_fault`
and `on_event`, can be changed to `service_context`.

###### 8.3.3. Possible to save in repeatingtrigger

Certain services need to be executed repeatedly, or according to some time pattern, and
also to both send outgoing messages and save a new state to the database.

Previously this had to be separated into two IOServices, one `repeatingtrigger` to get the
repetition and another IOService that could perform the save.

By using the new possibility to save in `repeatingtrigger` patterns, such services can now be
combined to avoid the need for an extra IOService.

###### 8.3.4. Possible to use the same handler for plain and SOAP

In some cases the same business operation is needed for different interfaces
that only differ in the used message format, `plain` or `soap`.
For those cases it is now possible to use the same handler and specify `mixed`
as the protocol in the configuration. See [binding](configuration.html#conf-binding) in the configuration
reference.

##### 8.4. Mandatory migration in IOServer version 28.0.0

###### 8.4.1. Multiple sinks must be named

When using multiple output queues (sinks), all sinks must now be named.
It is possible to specify that one of the sinks is the default sink, but
it must still have a name.

See [sink](configuration.html#conf-sink) in the configuration reference.

When there is only one sink, it does not have to have a name.

##### 8.5. Recommended migration in IOServer version 28.0.0

###### 8.5.1. Change <skipconflict> to <conflict\_detection> in configuration

There is new way to configure whether an IOService should have conflict detection:

The previous configuration:

```
<skipconflict>true</skipconflict>
```

corresponds to the new configuration:

```
<conflict_detection>disabled</conflict_detection>
```

and the previous configuration:

```
<skipconflict>false</skipconflict>
```

corresponds to the new configuration:

```
<conflict_detection>message</conflict_detection>
```

See the configuration reference for [pattern](configuration.html#conf-pattern) for more information.

It is good practice to always specify the conflict detection setting for
IOServices, as the default will be changed in a future release.

###### 8.5.2. Use repeatingtrigger rather than timer + eventtrigger

In earlier versions it required two services to execute a trigger at specific times:

1. A `timer` service that could be configured to send a message at specific
   times according to a crontab-style pattern. This service could not execute
   any handler or trigger code.
2. An `eventtrigger` service that ran a trigger each time it received a
   message from the timer service.

This use case can now be implemented by a single service that uses the
`repeatingtrigger` pattern, as that pattern now supports the crontab-style
time specification in addition to what it handled earlier.

Using one service instead of two reduces the IOServer overhead.

##### 8.6. Mandatory migration in IOServer version 32.0.0

###### 8.6.1. Configuration for data model has changed

The configuration for the data model is a bit more logical now, but some changes are needed.

| Pre-migration planbuilder | Pre-migration domain | Post-migration planbuilder | Post-migration domain |
| --- | --- | --- | --- |
| air1 | air1 | mave1 or mave2 | air1 |
| air2 | air2 | mave2 | air2 |
| mave2 | air1 | No migration needed |  |
| mave2 | air2 | No migration needed |  |
| air1 | air2 | Not supported, use *planbuilder* mave2, *domain* air2 |  |

#### Mandatory migration from interface version NINE to TEN

##### Python imports

##### Handler interface version

##### The on_load method

#### Mandatory migration from interface version SEVEN to NINE

##### Python imports

##### Handler interface version

##### The on_fault method

##### The on_event method

##### Accessing Rave rulesets

#### Optional migration from version SEVEN to version NINE

##### Access different viewpoints of the plan

##### Service context instead of handler context and trigger context

##### Possible to save in repeatingtrigger

##### Possible to use the same handler for plain and SOAP

#### Mandatory migration in IOServer version 28.0.0

##### Multiple sinks must be named

#### Recommended migration in IOServer version 28.0.0

##### Change <skipconflict> to <conflict_detection> in configuration

##### Use repeatingtrigger rather than timer + eventtrigger

#### Mandatory migration in IOServer version 32.0.0

##### Configuration for data model has changed

### High Availability


##### 9.1. Active / Active

It is possible to run the same service on multiple nodes, balancing the load between them. The
messaging system (ActiveMQ) can handle multiple consumers at the same time.

Warning

Active/active cannot be used with inbound services that have strict ordering requirements (incoming
messages must be processed in order), nor with trigger-based outbound services.

##### 9.2. Active / Passive

Sysmond can be configured so that the same IOServer service runs at multiple nodes, but
only one of them is active at a time. All such IOServer processes load the database plan and keep it
up to date via refresh, but only the active one has worker processes.

Warning

Active/passive cannot be used with inbound services that have strict ordering requirements (incoming
messages must be processed in order).

##### 9.3. HA Store

An HA store keeps track of how far an IOService has progressed (database state). This is
mostly used by trigger services, but other service patterns may also store additional information.

The storage has two purposes:

* When the IOServer restarts, it resumes operation at saved database state.
* When fail-over occurs in an active/passive system, the new master resumes where the old one left off.

#### Active / Active

#### Active / Passive

#### HA Store

### Error handling


If a message fails, the general error handling is that IOServer:

1. puts back the message on the queue
2. refreshes its plan to get the latest state of the system
3. retries to handle the message

which hopefully solves the problem.

How many times a message is retried, and what happens when if it
eventually fails, are configurable per service.

##### 10.1. Trigger services

If an error occurs for a trigger service:

* the current worker is terminated
* no changes are saved to the database
* no messages are sent
* the service restarts the trigger from the last successful commit id.

Note

Some messages may be sent if the trigger sends multiple messages to destinations on different brokers.

If the service continues to fail, it is eventually [deactivated](#error-deactivated) and
the issue has to be resolved manually.

##### 10.2. Handler services

How a handler reacts on failure is configurable per service.
If a failure occurs, the handler retries the message causing the error
a [configurable](configuration.html#conf-retrycount) number of times.

If the number of retries are exhausted the handler can be
[configured](configuration.html#conf-blockmsg) to either:

* block the message
  :   which puts the message back first on the queue,
      effectively blocking any subsequent reading from the queue.
* skip the message
  :   which removes the message from the queue allowing
      the service to continue with the rest of the messages.

Which action to choose depends mainly on if the service can be allowed to lose a message.
If the message is skipped, the service continues without the need for manual intervention but the message is lost.
If the message is blocked, the service is [deactivated](#error-deactivated)
until the message is manually handled or removed.

If the number of retries for a message is exhausted, the `on_fault` method of the service is called.
In the `on_fault` method, a message with error information may be created to be sent as a response.
IOServer adds a message property, `jcms_responsecode`, to the response message.
The property contains the action taken due to the failure:

`MESSAGE_OK`
:   Message has been handled and no error has occurred

`MESSAGE_SKIPPED`
:   Message has failed and the message has been removed from the queue

`MESSAGE_BLOCKED`
:   Message has failed and the message has been put back to the queue

The property can be overridden in the `on_fault` method by adding a custom value to the `jcms_responsecode` property.

##### 10.3. Deactivated services

Deactivated services are restarted with roughly 5 minutes interval.
If the service can handle messages it continues as if nothing has happened
from where it was deactivated.
If it still has problems it is deactivated again and restarted 5 minutes later.

##### 10.4. Timed-out services

During normal operation a worker process pings the main process between calls to the handler,
and also pings repeatedly if the worker is idle for a while.

If a worker has not pinged within the configured worker time-out, see [worker\_time\_out](configuration.html#conf-persist-cid), the main
process prints a warning to the log file. After three missed pings in a row, the log message level is changed to error.

If some workers for a service have timed out, missed three pings in a row, the service is considered “degraded”.
If all workers for a service have timed out, the service is considered “unresponsive”.
If a timed out worker pings the main process, it is considered active again.
All these statuses can be viewed by using `ioserverctl status` or `ioserverctl list`.

##### 10.5. IOServer defined exceptions

The `exceptions` module defines a hierarchy of exceptions for handlers and pattern
implementations to use when signalling error conditions.
All of the exceptions inherit from the `IOSError` base class.

It is the pattern that implements an error handling strategy, the handler
only signals errors by raising the appropriate exception.

###### 10.5.1. Message errors

Errors that are specific to a particular incoming message inherit from the `MessageError` class.

There are three kinds of message errors:

####### 10.5.1.1. Transient message errors

Transient message errors (`TransientMsgError` class) are used for temporary conditions that
may be resolved if the operation is retried.

Typically the pattern retries the operation that failed a number of times,
and if there is still an error it is converted to either
a `SkipMsgError` or a `BlockingMsgError` error.
The retries can be performed locally in the pattern implementation in the worker process,
or via a round trip to the main processes.

The [configuration](configuration.html#conf-errors) defines how many local and global retries to perform,
and which error type to convert the transient message to if it still fails.

There are two predefined exceptions that inherit from `TransientMsgError`:

`DatabaseConflictError`
:   denotes a multirecord conflict exception in the database when saving

`DatabaseDataTooOldException`
:   denotes a single-record conflict in the database when saving.

####### 10.5.1.2. Blocking message errors

A blocking message error (`BlockingMsgError` class) leaves the failing message
in the queue so that it is read again the next time messages are fetched.

####### 10.5.1.3. Skip message errors

A skip message error (`SkipMsgError` class) causes the failing message to be removed
from the in-queue so that the service can proceed with the following messages.

###### 10.5.2. System errors (non-message errors)

System errors are errors that are not specific to a particular message,
for example general I/O errors.

The base class for system errors is [`SystemError`](https://docs.python.org/3/library/exceptions.html#SystemError "(in Python v3.12)").

####### 10.5.2.1. Transient errors

Transient errors (`TransientError` class) are used for temporary conditions that
may be resolved if the operation is retried.

The typical action is to retry the operation a number of times according to the configuration.
If the error remains it is converted to a static error.

####### 10.5.2.2. Static errors

A static error (`StaticError` class) is an error that is not a temporary condition.

#### Trigger services

#### Handler services

#### Deactivated services

#### Timed-out services

#### IOServer defined exceptions

##### Message errors

###### Transient message errors

###### Blocking message errors

###### Skip message errors

##### System errors (non-message errors)

###### Transient errors

###### Static errors

### Best Practices


##### 11.1. IOServices sharing IOServer

It is often desirable to have multiple IOServices share the same IOServer process.
For this to work, the IOServices must be able to:

* share the same [datacontext](configuration.html#conf-datamodel)
* share the same [refresh strategy](configuration.html#conf-refresh).
  For instance, services that need the [exact CID refresh strategy](configuration.html#conf-exactcid) usually
  need their own IOServer process.

Another consideration is whether some of the services are likely to trigger refreshes often,
and if that behavior is suboptimal for other services.

Also, IOServices that use the [refresh\_boundary](configuration.html#conf-refresh-boundary) feature should probably not be grouped with IOServices
that do not need it, mainly for performance reasons.

The total number of worker processes for all services should not be too high, as discussed below
in [Number of worker processes](#best-practices-number-of-processes).

##### 11.2. Number of worker processes

If a service is slow the performance can be improved by adding another worker process to the service,
but this only works up to a certain point. When there are too many worker processes, the overhead of
forking after each refresh affects the performance, mainly the latency.
The best way to find a suitable worker pool size is to try different alternatives and measure performance.
It is possible to use the `ioserverctl` tool to modify the worker pool size, see [IOServer control tool](ioserver_control_tool.html#ioserverctl).

Note that there are services that cannot have more than one worker process. For example inbound
services with strict ordering requirements (incoming messages must be processed in order) and
also to trigger-based outbound services.

##### 11.3. Services sharing worker

While individual services may benefit from larger worker pools, reducing the overall number of workers for
an IOServer is desirable, since it reduces resource usage.
This is especially true for services that needs to be constantly available, but only sporadically receive
messages. Defining such a service separately will force the IOServer to spawn workers for it on each new
generation, even though they are rarely used, causing unnecessary overhead.
IOServer provides the [Dispatch](patterns.html#pattern-dispatch) feature, which groups low-frequency services together in
a “super-service”, which will share worker(s). This can reduce the total number of workers, while maintaining
service availability.

##### 11.4. Pre-load of Rave tables

To improve performance, Rave tables used in the rule set should be pre-loaded.
Otherwise Rave loads them on demand in the worker processes, for each new worker generation.
It is much better to do this once in the main process.
See [preload\_tables](configuration.html#conf-preload-tables) for information.

To avoid degradation of performance over time, the Rave tables should be refreshed in the main process,
right after plan refresh. This behavior is controlled by the `refresh_tables` setting in the
[datamodel](configuration.html#conf-datamodel) section.

##### 11.5. Running the same IOServices on different nodes

For load-balancing and availability reasons, it can be a good idea to run the same service in different
IOServer processes on different nodes. See [High Availability](high_availability.html#high-availability).

##### 11.6. Monitoring service deactivation

An IOService can be deactivated for a few different reasons:

* failure to process incoming messages, resulting in `BlockingMsgErrors`
* failure to execute handler, resulting in `StaticErrors`
* manually deactivated using `ioserverctl`, see [IOServer control tool](ioserver_control_tool.html#ioserverctl).

A service that is deactivated because of too many errors is restarted periodically,
see [restart\_attempt\_interval](configuration.html#conf-persist-cid), but in some cases the restart may never succeed without
manual intervention. For example if the error is caused by an incorrect message that has to be removed from the queue.
For this reason it is important that a monitoring system detects service deactivation and generates alerts or similar.
This can be done by looking at the IOServer log file, where the string “Deactivating service”
is written whenever an IOService is deactivated.

##### 11.7. Worker time-out and pings

During normal operation a worker process pings the main process between calls to the handler,
and also pings repeatedly if the worker is idle for a while.

If a worker has not pinged within the configured worker time-out, see [worker\_time\_out](configuration.html#conf-persist-cid), the main
process prints a warning to the log file. After three missed pings in a row, the log message level is changed to error.

If some workers for a service have timed out, missed three pings in a row, the service is considered “degraded”.
If all workers for a service have timed out, the service is considered “unresponsive”.
If a timed out worker pings the main process, it is considered active again.
All these statuses can be viewed by using `ioserverctl status` or `ioserverctl list`.

There are two ways to avoid time-out of a worker:

1. Set a long enough worker time-out so that it does not happen.
2. Have the handler code call the `report_progress()` method in `ServiceContext` periodically,
   which makes the worker send pings to the main process.

A risk with setting a too long worker time-out is that the main process does not detect
a hanging worker process until the worker time-out has passed three times.

##### 11.8. Handling of errors in IOService

The recommended way to handle errors is to catch all expected errors in the handler/trigger.
The service should convert it to an IOServer exception when appropriate.
Regarding logging the handler/trigger should log the errors on the level it sees fit and should not rely on the IOServer logging the error.

Unexpected exceptions can be ignored and IOServer will handle them according to configuration.

#### IOServices sharing IOServer

#### Number of worker processes

#### Services sharing worker

#### Pre-load of Rave tables

#### Running the same IOServices on different nodes

#### Monitoring service deactivation

#### Worker time-out and pings

#### Handling of errors in IOService

### Configuration

#### program

###### 12.1. program

The top node of the IOServer configuration is a `program` element with the
mandatory name `ioserver`. It contains one or more [process](#conf-process) elements.

#### process

###### 12.2. process

A `process` element configures an IOServer process. It provides a process name and
contains global process configuration, such as [refresh](#conf-refresh) and [datamodel](#conf-datamodel),
as well as one or more [ioservice](#conf-ioservice) elements.

A `process` element has the following attribute:

| Attribute | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of the process. Must be unique for each host, i.e it is possible to have multiple “ioserver\_all” processes, but they must run on different hosts. |

and can have the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `refresh` | container | No | See the [refresh](#conf-refresh) element.  Default: Interval refresh strategy |
| `refresh_rate` | integer | No | **Deprecated**: please use the [refresh](#conf-refresh) element instead.  Maximum time interval in seconds between refreshes of the plan. |
| `localtmpdir` | string | No | **Deprecated** |
| `servicecontrol` | string | No | **Deprecated** |
| `datamodel` | container | Yes | See the [datamodel](#conf-datamodel) element. |
| `message_retention` | container | No | See the [message\_retention](#conf-message-retention) element. |
| `ioservice` | container | Yes | See the [ioservice](#conf-ioservice) element. |

Note

The `refresh_rate` element is deprecated, use [refresh](#conf-refresh) instead.

#### refresh

###### 12.3. refresh

IOServer refreshes the loaded plan according to one of the following strategies:

Interval refresh strategy
:   The plan is refreshed according to a given refresh interval.
    If a refresh does not contain any changes the next interval is increased by a factor
    2, until the maximum interval is reached or changes are detected in the plan. After that the interval is
    reset to the configured or default interval. The absolute minimum refresh interval is one second.

Exact CID refresh strategy
:   The plan is refreshed to a specific commit ID needed by an incoming request.
    This strategy can only be used by a single `requestresponse` service.

A `refresh` element can have the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `strategy` | string | No | Refresh strategy to use.  Supported values: `interval`, `exactcid`  Default: `interval` |
| `interval` | integer | No | Time interval in seconds between refresh of the plan. Only valid in `interval` refresh strategy.  Minimum: `1`  Default: `20` |
| `max_interval` | integer | No | Maximum time interval in seconds. Only valid in `interval` refresh strategy.  Default: `120` |

#### datamodel

###### 12.4. datamodel

A `datamodel` element contains information about which data context to load, as well as which rule set
and parameter set.

A `datamodel` element can have the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `datacontext` | string | Yes | Name of the data context to load. |
| `domain` | string | Yes | ARA domain to use.  Only certain combinations of this value and the `planbuilder` value are supported, depending on the type of system:   * For Atrium architecture, set `domain` to `air2` and   `planbuilder` to `mave2`. * For Studio architecture (Major Release), set `domain` to   `air1` and `planbuilder` to `mave2`. |
| `planbuilder` | string | Yes | See `domain` for how to set this value. |
| `ruleset` | string | No | Name of the rule set to use. |
| `refresh_tables` | boolean | No | Whether Rave tables should be updated after refresh (in the main process). See also [preload\_tables](#conf-preload-tables).  Default: `true` |
| `rulesettype` | string | No | **Deprecated** |
| `snapshotpath` | string | No | **Deprecated** |
| `mave_etables` | boolean | No | **Deprecated** |
| `parameterset` | string | No | Name of the parameter set to use. Applies to all services running in the IOServer instance, but can be overridden per `ioservice`. See [pattern](#conf-pattern) section. |
| `now` | abstime | No | If specified, this value is used as fixed time and current time refers to Rave only (only for testing purposes). |
| `deadcount_now` | boolean | No | If true, IOServer will reduce the number of requests to the timeserver (by deadcounting the time since last poll).  Normally, this should be turned on, but in certain cases (e.g. during testing), it may be necessary to poll the timeserver more often - in that case set this to `false`.  Only applicable if the system is using a timeserver. Default: `true` |
| `nowupdateinterval` | int | No | **Deprecated** |
| `preload_tables` | container | No | See the [preload\_tables](#conf-preload-tables) element. |

####### 12.4.1. preload\_tables

The `preload_tables` element lists Rave tables that should be pre-loaded.

Example of `preload_tables` configuration:

```
<preload_tables>
  <table>
    <rave_name>_topmodule.airport</rave_name>
    <external_name>airport</external_name>
  </table>
  <table>
    <rave_name>crew.crew_rank_category</rave_name>
    <external_name>crew_rank</external_name>
  </table>
</preload_tables>
```

The `preload_tables` element contains one or more `table` elements,
which has the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `rave_name` | string | Yes | Table name as defined in the rule set, including module name. (`_topmodule` for tables in the top module). |
| `external_name` | string | Yes | Name of the underlying table, for example `crew_rank`. |

##### preload_tables

#### db

###### 12.5. db

A `db` element contains database information
and is often inherited from a `global/default` section, since it typically is shared
between a number of programs.

A `db` element has the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `connect` | string | Yes | Connect string to the database. |
| `schema` | string | No | Schema to use in the database. |

#### ioservice

#### pattern

##### jcmsstatemessagereplace

######## 12.7.1. jcmsstatemessagereplace

A `jcmsstatemessagereplace` element configures how to update outgoing messages with the correct jcms
state and has the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `find` | string | Yes | String matching the part of the outgoing message where to do the replacement. |
| `replace` | string | Yes | Part of the `find` string to replace with the jcms state. This string is only allowed to occur once in the `find` string. |

**Example:**

```
<jcmsstatemessagereplace>
  <find>jcms_state="0"</find>
  <replace>0</replace>
</jcmsstatemessagereplace>
```

An outgoing message is searched for the `jcms_state="0"` string, and the `0` is replaced
by the correct jcms state.

#### binding

###### 12.8. binding

A `binding` element configures a handler or a trigger, and data binding. It can have the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `language` | string | Yes | Programming language the handler or trigger is written in. Currently only `python` is supported. |
| `protocol` | string | No | Message protocol to use. The supported values are:   * `soap`, for a SOAP handler (with or without data binding) * `plain`, for a plain text handler * `mixed`, for a handler that accepts both SOAP and plain text   The protocol to use is determined per message by looking at the content type of the incoming message. The mixed option is only valid for a handler.  Default: `soap` |
| `handler` | string | Yes (one of `handler` or `trigger`) | Python module that contains the handler code. Exactly one `handler` or `trigger` element must be specified. |
| `trigger` | string | Yes (one of `handler` or `trigger`) | Python module that contains the trigger code. Exactly one `handler` or `trigger` element must be specified. |
| `databinding` | string | No | Python module that contains the PyXB-generated data binding code. If this element is not specified, no data binding module is loaded and the handler code is responsible for parsing the message. |
| `operation` | string | No | Name of the operation method to call in the handler.  Default: `handle` |
| `profile` | boolean | No | Whether profiling should be enabled for the handler/trigger code. See [profile](#conf-profile).  Default: `false` |

####### 12.8.1. profile

If profiling is enabled then a `<random>.pstat` file is created for each call to the handler or trigger.
These files are put into the `${CARMTMP}/ioservice_profiling/<service_name>` directory.

The `join_pstats` tool, which is delivered as part of the carmsys, can be used to merge all profile
output files in a directory into a single file.

Other tools can then be used to visualize the output.
A good one is [gprof2dot](https://github.com/jrfonseca/gprof2dot).

##### profile

#### source

###### 12.9. source

A `source` element specifies from where to fetch incoming messages.
The [requestresponse](patterns.html#pattern-requestresponse) pattern supports multiple sources, in which
case messages are read from the sources in a round robin fashion.

A `source` element can have the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `class` | string | Yes | Type of source. Supported values are:   * `qpid` (Apache ActiveMQ) * `memory` (internal memory queues, testing only) |
| `queue_reference` | string | Yes | Logical name of the queue to use. See the *ccf* configuration for details. |
| `prefetch` | integer | No | For ActiveMQ, the prefetch capacity (number of messages) of the receiver.  Default: `50`  **Important**: This value must be greater than 0. |
| `correlation_id` | string | No | For `qpid` sources, information about each fetched message is logged. If this element is not set, the correlation id of the fetched message is part of the log. If this element is set, the given message property is logged instead.  Default: “” (logs correlation id) |

#### sink

###### 12.10. sink

A `sink` element specifies where to send outgoing messages.
It is possible to specify several sinks for a service; in which case all sinks must be given a
name.

A `sink` element has the following attribute:

| Attribute | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `name` | string | No (Yes if multiple sinks configured) | Name of the sink. Must be unique for each service. The name `sink` is not allowed. |

and the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `class` | string | Yes | Type of sink. Supported values are:   * `qpid` (Apache ActiveMQ) * `memory` (internal memory queues, testing only) |
| `queue_reference` | string | No | Logical name of the queue to use. See the *ccf* configuration for details.  If not set, the request message needs to provide the reply\_queue. |
| `batch_size` | integer | No | For ActiveMQ, the number of messages to buffer before they are automatically committed.  If this parameter is set to `0`, messages are committed on handler/trigger success.  Note: Only enable this if the receiver can handle retransmitted messages, that is, no transaction semantics is needed.  Default: `0` |
| `capacity` | integer | No | For ActiveMQ, the sender capacity (number of messages).  If this parameter is set to `0`, each message is sent synchronously.  Default: `50` |
| `compress` | boolean | No | Whether the message content should be compressed by using gzip. If so, the message property `uncompressed-size` is set to the uncompressed size of the message content. The message encoding is also set to `gzip`.  Default: `false` |
| `maxcontentsize` | int | No | Maximum content size of the message in bytes, compressed or not. If the size exceeds this limit, a `MessageError` is thrown.  Default: `0` (no check) |
| `large_message_url` | string | No | URL for upload of large messages. If a message is considered large, as defined by the `large_message_size` element, then the message content is uploaded to this URL and the message property `DeferredContentUrl` is set to a URL where the content can be downloaded. The message that is sent has no content.  Default: “” (disabled). |
| `large_message_size` | int | No | The size of a large message in bytes. This setting is only regarded if `large_message_url` is set.  Default: `1000000` |
| `durable` | boolean | No | Whether messages written by this sink should be durable. This value is used by default if the `durable` property is not set on the IOMessage.  Default: `false` |
| `ttl` | int | No | The time-to-live in seconds of messages written by the sink. This value is used by default if the `ttl` property is not set on the IOMessage.  If this element is not set, the default value depends on the value of the `durable` element in the following way. If `durable` is `false`, or not set at all, the default value is 3600 seconds (one hour). If `durable` is `true`, the default value is 0 seconds, which means that the messages never time out.  Default: `3600` or `0` |
| `default` | boolean | No | Whether this is the default sink for the service. That is, the sink used if the `send` method (without sink) on the service context is used.  Default: `false` |

**Example (single sink):**

```
<sink>
  <class>qpid</class>
  <queue_reference>queueName</queue_reference>
</sink>
```

**Example (multiple sinks):**

```
<sink name="sink1">
  <class>qpid</class>
  <queue_reference>queue1</queue_reference>
  <durable>true</durable>
  <ttl>120</ttl>  <!-- 2 minutes -->
  <default>true</default>
</sink>
<sink name="sink2">
  <class>qpid</class>
  <queue_reference>queue2</queue_reference>
  <durable>true</durable>
  <ttl>120</ttl>  <!-- 2 minutes -->
</sink>
```

#### message_retention

###### 12.11. message\_retention

A `message_retention` element specifies how message retention is configured for this service
(or services if configured on the [process](#conf-process) tag).

For more details, see [Message Retention](message_retention.html#ioserver-message-retention).

It has the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `sink` | container | Yes | See the [sink](#conf-sink) element. |

#### hastore

###### 12.12. hastore

An `hastore` element specifies how persistent data should be stored.
Currently, this configuration is only needed by [persist\_cid](#conf-persist-cid).

An `hastore` element can have the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `class` | string | Yes | Type of HA store. Supported values are:   * `consul`, Consul based storage. * `file`, basic file based storage. |
| `location` | string | No (Yes if ``` class``=``file ```) | Path to file based HA store (`file` only). |

A `consul` HA store uses [Consul](https://www.consul.io/) to store HA values. This requires that
a Consul service is running on the same machine. The service name is used as part of the key for
all HA values. This means that if a service is running on multiple machines, they share the
same HA store.

#### extra_indexes

###### 12.13. extra\_indexes

An `extra_indexes` element adds indexes needed by the service to the model (only
supported for mave2). Within the `extra_indexes` element, each index has an
`index` element with the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `collection` | string | Yes | Name of collection to add the index to. |
| `property` | string | Yes | Property to sort the index by. Several properties can be given. |

**Example:**

```
<extra_indexes>
  <index>
    <collection>rotation</collection>
    <property>adhoc</property>
    <property>dt</property>
  </index>
  <index>
    <collection>crewmember</collection>
    <property>givenname</property>
  </index>
</extra_indexes>
```

#### refresh_boundary

###### 12.14. refresh\_boundary

A `refresh_boundary` element specifies that a refresh needs to be done in steps. If
there is data in any of the given collections, the refresh is done in
steps where the boundaries are the revisions with data in the collections.
This can be useful in some special cases of triggers.

A `refresh_boundary` element contains one or more `collection` elements,
which have the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name of collection/entity to use as a refresh boundary. By adding two collections with the same name it is possible to specify both `true` and `false` for `inclusive`. |
| `inclusive` | boolean | No | Whether to include the revision containing data for this collection in the refresh.  Assume the following abbreviations: C0: Commit before the revision containing data C1: Commit at the revision containing data LC: Last commit done  If `false` the commits C0 and LC are included in the refresh.  If `true` the commits C1 and LC are included in the refresh.  If `true` and `false` the commits C0, C1 and LC are included in the refresh.  Default: `false` |
| `bundle_program_name` | string | No | Name of program where consecutive revisions shall be bundled into the same change set for this collection. The program name refer to what is stored in the `cliprogram` column in the `dave_revision` table.  If multiple `bundle_program_name` are specified, revisions matching any of the programs will be bundled together. |

**Example:**

```
<refresh_boundary>
  <collection>
    <name>publ_hold_period</name>
    <inclusive>false</inclusive>
    <bundle_program_names>
      <bundle_program_name>CrewExchange</bundle_program_name>
    </bundle_program_names>
  </collection>
  <collection>
    <name>crew_pend_publ_status</name>
    <inclusive>true</inclusive>
  </collection>
  <collection>
    <name>crew_pend_publ_status</name>
    <inclusive>false</inclusive>
  </collection>
</refresh_boundary>
```

#### errors

###### 12.15. errors

An `errors` element configures the error handling strategy for the service and
has the following sub-elements:

* [retrycount](#conf-retrycount), which specifies the number of retries to perform
* [blockmsg](#conf-blockmsg), which defines whether transient message errors shall be converted to
  `BlockingMsgError` or `SkipMsgError` when the retry attempts have been exhausted.

####### 12.15.1. retrycount

A `retrycount` element specifies the number of times to retry a message in the event of an transient
message error. The element has the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `local` | integer | No | Number of retry attempts to execute in the worker process in the event of a transient error. A local refresh will be performed between attempts. Only relevant for `subscriber` and `requestresponse` patterns, other patterns do not retry in the worker process.  Default: `0` |
| `system` | integer | No | Number of retry attempts to execute in the main process for transient non message-specific errors.  Default: `3` |
| `message` | integer | No | Number of retry attempts to execute in the main process for transient message errors.  Default: `3` |

####### 12.15.2. blockmsg

A `blockmsg` element specifies what to do with a transient message error if the number of retry
attempts have been exhausted. By default it is converted to a `SkipMsgError` error, but it is
possible to define cases where it is converted to a `BlockingMsgError` error instead.
The `requestresponse` pattern ignores this setting and converts transient message errors to
`SkipMsgErrors` when the retry attempts have been exhausted.

A `blockmsg` element has the following sub-elements:

| Sub-element | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `handling` | boolean | No | Whether transient message errors raised in the handler should be converted to blocking message errors.  Default: `false` (`SkipMsgError`) |
| `plan` | boolean | No | Whether transient message errors raised during plan handling, such as save, should be converted to blocking message errors.  Default: `false` (`SkipMsgError`) |
| `io` | boolean | No | Whether transient message errors raised during I/O operations, fetching from queues etc., should be converted to blocking message errors.  Default: `false` (`SkipMsgError`) |
| `marshal` | boolean | No | Whether transient message errors raised during marshalling should be converted to blocking message errors.  Default: `false` (`SkipMsgError`) |

##### retrycount

##### blockmsg

#### dispatch

#### Dispatch Scenario

### Command-line arguments


The synopsis is:

```
 ioserver -p process [-s service-name] [-a]
 ioserver [-s service-name] [-a] process
 ioserver -h
 ioserver -V


Options:
 -p process, --process=process
    Process tag in configuration (required argument)
 -s service-name, --service=service-name
    The name of the single service to run (optional).
    The default is to run all services configured for the process.
 -a, --use-aping
    Whether the IOServer receives signals from sysmond using the APing protocol.
    Default is to not use APing.
 -h, --help
    Print this help message and exit
 -V, --version
    Print version string and exit
```

### Cmsshell integration


IOServer provides both a cmsshell plugin and self tests that can
be run with cmsshell selftest command.

##### 14.1. cmsshell plugin

The plugin provided by IOServer can be accessed by using
the prefix ioserver in cmsshell.

###### 14.1.1. help

Prints a help text with the available commands.

###### 14.1.2. clear\_hastore

This command clears the HA store for a specific service if an argument is provided.
Otherwise it will clear the ha store for all services on all processes.

| Argument | Mandatory | Description |
| --- | --- | --- |
| `--service=service_name` | No | Delete HA store only for the provided IOService. |

###### 14.1.3. list\_config

This command lists the configuration for a specific service if an argument is provided.
Otherwise it will list the configuration for all services on all processes,
regardless the node the are run on.

| Argument | Mandatory | Description |
| --- | --- | --- |
| `--service=service_name` | No | List configuration only for the provided IOService. |

###### 14.1.4. selftest

Run the IOServer [self tests](#self-tests).

###### 14.1.5. service

Execute an ioserverctl command for the specified service on all IOServer instances.
For start and stop the command will wait for the service to be up/down and show final status before returning the prompt.

| Argument | Mandatory | Description |
| --- | --- | --- |
| `service` | Yes | Name of the service to affect, as retrieved from e.g. list\_config |
| `command` | Yes | The command to run.   * start: Will enable the service. * stop: Will disable the service. * status: prints the status of the service. |
| `--wait=timeout` | No | Set the time to wait before timeout. Default: 5s |

##### 14.2. Self tests

Run tests to try to verify that the IOServers are functioning properly.

###### 14.2.1. Queues

Validate that the IOServer and ccf configuration is consistent.

###### 14.2.2. Processes

Verify that all processes configured to run on this node are running.

###### 14.2.3. Services

Verify that all configured services are running and are in active state.

#### cmsshell plugin

##### help

##### clear_hastore

##### list_config

##### selftest

##### service

#### Self tests

##### Queues

##### Processes

##### Services

### IOServer control tool


##### 15.1. Purpose

The `ioserverctl` tool is used to control and list the services run by an IOServer.

##### 15.2. Command-line arguments

The synopsis is:

```
Usage:
  ioserverctl [options] [-p process-name] start [-s service-name]
  ioserverctl [options] [-p process-name] stop [-s service-name]
  ioserverctl [options] [-p process-name] status [-s service-name]
  ioserverctl [options] [-p process-name] clear-statistics [-s service-name]
  ioserverctl [options] [-p process-name] set-workers [-s service-name] <pool-size>
  ioserverctl [options] [-p process-name] getcid
  ioserverctl [options] [-p process-name] list
  ioserverctl [options] [-p process-name] refresh
  ioserverctl -h
  ioserverctl -V

Options:
    -h, --help
        Print this help message and exit.
    -V, --version
        Print version string and exit.
    -t <seconds>, --timeout=<seconds>
        Command timeout in seconds (default: 30)
        a timeout of -1 blocks indefinitely.
    -j, --json
        Generate single-line JSON output suitable for parsing by other programs
        (default is a human-readable plain-text format)
    -J, --json-multiline
        Generate multi-line JSON output
        (default is a human-readable plain-text format)
    -p <process name>, --process <process name>
        Specify the process on which the action should be performed.
        The process name must be defined in the configuration.
        If no process is specfied the action will be performed on all IOServers.
    -s <service name>, --service <service name>
        Specify the service on which the action should be performed.
        Multiple service options may be provided.
        The service name must be defined in the configuration.
        If no service is specfied the action will be performed on all IOServices.

Actions:
    start [-p process-name] [-s service-name]
        Start the specified IOService on the specified process

    stop [-p process-name] [-s service-name]
        Stop the specified IOService on the specified process.

    status [-p process-name] [-s service-name]
        Print status of the specified IOService on the specified process.

    clear-statistics [-p process-name] [-s service-name]
        Clear the statistics of the specified IOService on the specified process.

    set-workers [-p process-name] [-s service-name] <pool-size>
        Set the size of the specified IOService's worker-pool on the specified process.
        The pool size must be larger than zero.

    getcid [-p process-name]
        Get latest generation (cid) loaded in the specified IOServer main.

    list [-p process-name]
        List configured IOServices with status information for specified IOServer.

    refresh [-p process-name]
        Request IOServer to refresh the plan.
```

##### 15.3. Examples

Get a list of all services in the `ioserver_all` process:

```
ioserverctl -p ioserver_all list
```

Get a list of all services for all IOServer processes on node:

```
ioserverctl list
```

Get the current plan generation in the `ioserver_all` process:

```
ioserverctl -p ioserver_all getcid
```

Check the status for the `crew_checkin` service in the `ioserver_all` process:

```
ioserverctl -p ioserver_all status -s crew_checkin
```

Check the status for two of the services in the `ioserver_all` process:

```
ioserverctl -p ioserver_all status -s crew_checkin -s roster_in
```

Check the status for all services in the `ioserver_all` process:

```
ioserverctl -p ioserver_all status
```

Clear the statistics for the `crew_checkin` service in the `ioserver_all` process:

```
ioserverctl -p ioserver_all clear-statistics -s crew_checkin
```

Clear the statistics for two of the services in the `ioserver_all` process:

```
ioserverctl -p ioserver_all clear-statistics -s crew_checkin -s roster_in
```

Clear the statistics for all services in the `ioserver_all` process:

```
ioserverctl -p ioserver_all clear-statistics
```

Deactivate the `crew_checkin` service in the `ioserver_all` process:

```
ioserverctl -p ioserver_all stop -s crew_checkin
```

Reactivate the `crew_checkin` service in the `ioserver_all` process:

```
ioserverctl -p ioserver_all start -s crew_checkin
```

Reactivate all services in the `ioserver_all` process:

```
ioserverctl -p ioserver_all start
```

Change the worker pool size to five workers for the `crew_checkin` service in the `ioserver_all` process:

```
ioserverctl -p ioserver_all set-workers -s crew_checkin 5
```

Tell the `ioserver_all` process to refresh:

```
ioserverctl -p ioserver_all refresh
```

Tell all ioserver processes on the current node to to refresh:

```
ioserverctl refresh
```

#### Purpose

#### Command-line arguments

#### Examples

### IOServer Python API reference


API reference for the IOServer public python interface.
Used by handlers and triggers.

##### 16.1. IOServer Python API Reference Version 10

* [16.1.1. `jcms.ioserver.versions`](python_api_ver10_reference.html)
* [16.1.2. `jcms.ioserver.constants`](python_api_ver10_reference.html#jcms-ioserver-constants)
* [16.1.3. `jcms.ioserver.exceptions`](python_api_ver10_reference.html#jcms-ioserver-exceptions)
* [16.1.4. `jcms.ioserver.version10.config`](python_api_ver10_reference.html#module-jcms.ioserver.version10.config)
* [16.1.5. `jcms.ioserver.version10.actions`](python_api_ver10_reference.html#module-jcms.ioserver.version10.actions)
* [16.1.6. `jcms.ioserver.version10.message`](python_api_ver10_reference.html#module-jcms.ioserver.version10.message)
* [16.1.7. `jcms.ioserver.version10.context`](python_api_ver10_reference.html#module-jcms.ioserver.version10.context)
* [16.1.8. `jcms.ioserver.version10.mave2.IPlanHolder`](python_api_ver10_reference.html#jcms-ioserver-version10-mave2-iplanholder)

##### 16.2. IOServer Python API Reference Version 9

* [16.2.1. `jcms.ioserver.versions`](python_api_ver9_reference.html)
* [16.2.2. `jcms.ioserver.constants`](python_api_ver9_reference.html#jcms-ioserver-constants)
* [16.2.3. `jcms.ioserver.exceptions`](python_api_ver9_reference.html#jcms-ioserver-exceptions)
* [16.2.4. `jcms.ioserver.version9.config`](python_api_ver9_reference.html#module-jcms.ioserver.version9.config)
* [16.2.5. `jcms.ioserver.version9.actions`](python_api_ver9_reference.html#module-jcms.ioserver.version9.actions)
* [16.2.6. `jcms.ioserver.version9.message`](python_api_ver9_reference.html#module-jcms.ioserver.version9.message)
* [16.2.7. `jcms.ioserver.version9.context`](python_api_ver9_reference.html#module-jcms.ioserver.version9.context)
* [16.2.8. `jcms.ioserver.version9.mave2.IPlanHolder`](python_api_ver9_reference.html#jcms-ioserver-version9-mave2-iplanholder)

#### IOServer Python API Reference Version 10

##### jcms.ioserver.versions


This module defines the supported Python Interface Versions.

All handlers and triggers must implement the method `handler_interface_version()`
that returns one of these values.

The PlanHolder and context objects provided to the handler/trigger will be adopted to the version in
which the service is implemented.

*class* `jcms.ioserver.versions.``InterfaceVersion`
:   Specifies the version of the interface used in the handler or trigger implementation.

    `NINE` *= 9*
    :   Interface version 9, introduced in IOServer version 28.0.0

    `TEN` *= 10*
    :   Interface version 10, introduced in IOServer version 33.0.0

##### jcms.ioserver.constants


This module defines the public constants that handlers and triggers have access to.

*class* `jcms.ioserver.constants.``PropertyNames`
:   Names of predefined message properties.

    `SOAP_ACTION` *= 'SOAPAction'*
    :   The soap action contains the name of the SOAP operation, format `urn:<operation>`.

    `STATE_REFERENCE` *= 'jcms\_state'*
    :   The state header contains the JCMS state reference CID if any.

    `USER_ATTRIBUTES` *= 'jcms\_attributes'*
    :   The user attribute header contains the security attributes.

##### jcms.ioserver.exceptions


*exception* `jcms.ioserver.exceptions.``BlockingMsgError`(*description=''*, *source\_exc\_type=None*)
:   A non-transient error in message that cannot be skipped

*exception* `jcms.ioserver.exceptions.``DatabaseConflictError`(*description=''*, *source\_exc\_type=None*)
:   An error caused by a database conflict trigger.

*exception* `jcms.ioserver.exceptions.``DatabaseDataTooOldError`(*description=''*, *source\_exc\_type=None*)
:   An error caused by a database data too old conflict.

*exception* `jcms.ioserver.exceptions.``FormatterError`(*description=''*, *source\_exc\_type=None*)
:   A problem in message formatting or output validation.

*exception* `jcms.ioserver.exceptions.``IOSError`(*description=''*, *source\_exc\_type=None*)
:   Base class for IOServer exceptions.

    `__init__`(*description=''*, *source\_exc\_type=None*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `get_description`()
    :   |  |  |
        | --- | --- |
        | Returns: | the error description. |

    `get_error_code`()
    :   |  |  |
        | --- | --- |
        | Returns: | the error code. |

*exception* `jcms.ioserver.exceptions.``MarshallingError`(*description=''*, *source\_exc\_type=None*)
:   Base class for Marshalling exceptions.

    `__init__`(*description=''*, *source\_exc\_type=None*)
    :   Initialize self. See help(type(self)) for accurate signature.

*exception* `jcms.ioserver.exceptions.``MessageError`(*description=''*, *source\_exc\_type=None*)
:   An error caused by incorrect information or syntax in a message.

*exception* `jcms.ioserver.exceptions.``ParserError`(*description=''*, *source\_exc\_type=None*)
:   A problem in message parsing or input validation.

*exception* `jcms.ioserver.exceptions.``SendError`(*description=''*, *source\_exc\_type=None*)
:   An error caused by failure to send or acknowledge a message.

*exception* `jcms.ioserver.exceptions.``SkipMsgError`(*description=''*, *source\_exc\_type=None*)
:   A non-transient error in a message that can be skipped.

*exception* `jcms.ioserver.exceptions.``StaticError`(*description=''*, *source\_exc\_type=None*)
:   A non-transient error condition in the system as opposed to the message.

*exception* `jcms.ioserver.exceptions.``SystemError`(*description=''*, *source\_exc\_type=None*)
:   An error condition in the IOServer system as opposed to the message.

*exception* `jcms.ioserver.exceptions.``TransientError`(*description=''*, *source\_exc\_type=None*)
:   An error caused by a possibly temporary condition in the system.

*exception* `jcms.ioserver.exceptions.``TransientMsgError`(*description=''*, *source\_exc\_type=None*)
:   An error caused by a possibly temporary condition in the message.

##### jcms.ioserver.version10.config


####### 16.1.4.1. [`IConfig`](#jcms.ioserver.version10.config.IConfig "jcms.ioserver.version10.config.IConfig")

*class* `jcms.ioserver.version10.config.``IConfig`(*\*args*, *\*\*kwargs*)
:   Provides access to the IO-server configuration.

    The ioserver configuration is organized in global (per process) and service level configuration groups. A configuration group is a set of values (and potentially subgroups) that can be fetched by name. In the jcms configuration file syntax a configuration group corresponds to a tag that has complex content, while a value is a tag with only string content.

    The IConfig interface encapsulates the lookup logic and override hierarchy within the configuration and provides the values that are effective for this ioserver instance. Lookups with a service-specific group tag will provide the effective value for that service and sub-group, standard fallback logic to process-global and global-default values is handled by the config implementation.

    Components should lookup the values they need within their provided configuration group using getConfigValue(group, key, defvalue) or the typed equivalents.

    `getConfigValue`(*self*)
    :   lookup a configuration value with given key within a group

        Each component has a configuration group provided in the constructor and should call the method with that group. Global settings directly defined on the process level can get fetched with an empty group.

        |  |  |
        | --- | --- |
        | Parameters: | * **group** – the group key of the requested configuration group * **key** – the name of the configuration value to fetch * **defValue** – a fallback value to use if no configuration is found |
        | Returns: | the value of the configuration property if found, defValue else |

        **Types**
        - Parameter group: `std` ::`string`
        - Parameter key: `std` ::`string`
        - Parameter defValue: `std` ::`string`
        - Return type: `std` ::`string`

    `getGlobalConfigGroup`(*self*)
    :   provide the lookup key for a ioserver global configuration group

        Use this method to get a group key for process-global settings.

        |  |  |
        | --- | --- |
        | Parameters: | * **groupTag** – the tag of the configuration group, like “db” or “datamodel” * **name** – the name of an instance of the configuration group if there can be more than one, otherwise empty |
        | Returns: | the group key to use for lookups of configuration in that group |

        **Types**
        - Parameter groupTag: `std` ::`string`
        - Parameter name: `std` ::`string`
        - Return type: `std` ::`string`

    `getGlobalGroupNames`(*self*)
    :   get the list of all names for parallel global configuration groups with same tag

        |  |  |
        | --- | --- |
        | Parameters: | **groupTag** – the tag of the configuration group, like “db” or “datamodel” |

        **Types**
        - Parameter groupTag: `std` ::`string`
        - Return type: `StringVectorPointer`

    `getServiceConfigGroup`(*self*)
    :   provide the lookup key for a ioserver service local configuration group

        Use this method to get a group key for service specific settings.

        |  |  |
        | --- | --- |
        | Parameters: | * **service** – the name of the service * **groupTag** – the tag of the configuration group, like “pattern” or “source” * **name** – the name of an instance of the configuration group if there can be more than one, otherwise empty |
        | Returns: | the group key to use for lookups of configuration in that group |

        **Types**
        - Parameter service: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Parameter name: `std` ::`string`
        - Return type: `std` ::`string`

    `getServiceGroupNames`(*self*)
    :   get the list of all names for parallel service configuration groups with same tag

        |  |  |
        | --- | --- |
        | Parameters: | * **service** – the name of the service * **groupTag** – the tag of the configuration group, like “pattern” or “source” |

        **Types**
        - Parameter service: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Return type: `StringVectorPointer`

    `getProcessServicePort`(*self*)
    :   Get the service port to use for the process when communicating with sysmond.

        |  |  |
        | --- | --- |
        | Parameters: | * **systemService** – The system service to look up * **hostName** – The host name to look up (default: use the current host name) * **processName** – The process name (default: use the current process name) |
        | Returns: | port number to the service or -1 if the service cannot be found |

        **Types**
        - Parameter systemService: `std` ::`string`
        - Parameter hostName: `std` ::`string`
        - Parameter processName: `std` ::`string`
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `getConfigSubGroup`(*self*)
    :   provide the lookup key for a detailed ioserver configuration group

        |  |  |
        | --- | --- |
        | Parameters: | * **parentGroup** – the group key of the requested configuration group * **groupTag** – the tag of the configuration group, like “db” or “datamodel” * **name** – the name of an instance of the configuration group if there can be more than one |
        | Returns: | the group key to use for lookups of configuration in that group |

        **Types**
        - Parameter parentGroup: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Parameter name: `std` ::`string`
        - Return type: `std` ::`string`

    `getSubGroupNames`(*self*)
    :   get the list of all names for parallel configuration groups

        **Types**
        - Parameter parentGroup: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Return type: `StringVectorPointer`

    `getServiceNames`(*self*)
    :   get the list of all service names

        **Types**
        - Return type: `StringVectorPointer`

    `getenv`(*self*)
    :   get the value of an environment variable

        |  |  |
        | --- | --- |
        | Parameters: | * **key** – the name of the variable to fetch * **defValue** – a fallback value to use if the variable is not set |
        | Returns: | the value of the environment variable if set, otherwise defValue |

        **Types**
        - Parameter key: `std` ::`string`
        - Parameter defValue: `std` ::`string`
        - Return type: `std` ::`string`

    `getConfigInt`(*self*)
    :   helper to fetch integer value

        find the configuration value and convert it to an integer.
        getConfigValue(const std::string&, const std::string& ,const std::string& )

        |  |  |
        | --- | --- |
        | Parameters: | * **group** – the group key of the requested configuration group * **key** – the configuration key (within the group) * **defValue** – a fallback value to use if no configuration is found |
        | Returns: | the value of the configuration property if its found, defValue else |
        | Raises: | **ioserver.base.ConfigurationError** – if the value doesn’t convert to int |

        **Types**
        - Parameter group: `std` ::`string`
        - Parameter key: `std` ::`string`
        - Parameter defValue: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `getConfigBool`(*self*)
    :   helper to fetch boolean value

        find the configuration value and convert it to a boolean. A value of “true” is regarded true, all other values are false.

        |  |  |
        | --- | --- |
        | Parameters: | * **group** – the group key of the requested configuration group * **key** – the configuration key (within the group) * **defValue** – a fallback value to use if no configuration is found |
        | Returns: | the value of the configuration property if its found, defValue else |

        **Types**
        - Parameter group: `std` ::`string`
        - Parameter key: `std` ::`string`
        - Parameter defValue: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")

    `getProcessName`(*self*)
    :   Get the proccess name.

        |  |  |
        | --- | --- |
        | Returns: | the name of the process |

        **Types**
        - Return type: `std` ::`string`

    `getPortBase`(*self*)
    :   Get the portbase.

        |  |  |
        | --- | --- |
        | Returns: | the portbase number, -1 on error |

        **Types**
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `getProcessServiceUrl`(*self*)
    :   get the service URL for a given system service

        |  |  |
        | --- | --- |
        | Parameters: | * **systemService** – The system service to look up * **hostName** – The host where to look for the service. Empty string means localhost. Default is empty string. * **processName** – The name of the process which provides the service. Empty string means use the process name which was given when calling the constructor (in this class). |
        | Returns: | URL with the format <service://host:port> or empty string if service is not found. |

        **Types**
        - Parameter systemService: `std` ::`string`
        - Parameter hostName: `std` ::`string`
        - Parameter processName: `std` ::`string`
        - Return type: `std` ::`string`

    `getSubGroups`(*self*)
    :   get the list of all groups for parallel configuration groups

        **Types**
        - Parameter parentGroup: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Return type: `StringVector`

    `getConfigAttribute`(*self*)
    :   Get a configuration attribute with given key within a group.

        |  |  |
        | --- | --- |
        | Parameters: | * **group** – the group key of the requested configuration group * **attribute** – the name of the configuration attribute to fetch * **defValue** – a fallback value to use if no configuration is found |
        | Returns: | the value of the configuration attribute if found, defValue else |

        **Types**
        - Parameter group: `std` ::`string`
        - Parameter attribute: `std` ::`string`
        - Parameter defValue: `std` ::`string`
        - Return type: `std` ::`string`

    `getConfigAttributes`(*self*)
    :   Get all configuration attributes, including values, within a group.

        Any “name” attributes are ignored as the configuration API handles them separately.

        |  |  |
        | --- | --- |
        | Parameters: | **group** – the group key of the requested configuration group |
        | Returns: | map of attribute name to attribute value. |

        **Types**
        - Parameter group: `std` ::`string`
        - Return type: `StringMap`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

###### IConfig

##### jcms.ioserver.version10.actions


This module defines the action codes that version TEN handlers can return.

####### 16.1.5.1. [`PlanAction`](#jcms.ioserver.version10.actions.PlanAction "jcms.ioserver.version10.actions.PlanAction")

*class* `jcms.ioserver.version10.actions.``PlanAction`
:   Version 10 Handler actions. Specifies what the pattern should do when a handler returns.
    Return value from handler methods.

    `ROLLBACK` *= 2*
    :   Roll back the modifications in the plan.

    `SAVE` *= 0*
    :   Save the current state of the plan.

    `UNCHANGED` *= 1*
    :   The plan does not need to be saved.

####### 16.1.5.2. [`FaultAction`](#jcms.ioserver.version10.actions.FaultAction "jcms.ioserver.version10.actions.FaultAction")

*class* `jcms.ioserver.version10.actions.``FaultAction`
:   Version 10 Fault actions. Specifies what the pattern should respond when an exception is raised.
    Return value from the on\_fault method in the handler module.

    `DEFAULT_RESPONSE` *= 0*
    :   Create a default error response message. Only supported for SOAP messages.

    `NO_RESPONSE` *= 1*
    :   Do not send a response.

    `SEND_RESPONSE` *= 2*
    :   Send the response message that the handler module has produced.

###### PlanAction

###### FaultAction

##### jcms.ioserver.version10.message


This module defines the Message classes available to version TEN handlers/triggers.

####### 16.1.6.1. [`PlainIOMessage`](#jcms.ioserver.version10.message.PlainIOMessage "jcms.ioserver.version10.message.PlainIOMessage")

*class* `jcms.ioserver.version10.message.``PlainIOMessage`(*io\_message*, *pyxb\_binding=None*, *skipMsgOnMarshalError=True*)
:   IOMessage with plain text or XML content.

    `__init__`(*io\_message*, *pyxb\_binding=None*, *skipMsgOnMarshalError=True*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `content`
    :   Get or set the message content.

    `content_type`
    :   Get or set the message content-type.

    *classmethod* `create_io_message`(*content*, *contentType=None*, *encoding=None*, *msgId=None*)
    :   Factory method for creating a Plain IOMessage.

        |  |  |
        | --- | --- |
        | Parameters: | * **content** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.12)")) – the message content * **contentType** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the type of the content, can be e.g. text or binary * **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the text encoding used * **msgId** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – id for the message |
        | Returns: | IOMessage SWIG object without wrapper |

    `encoding`
    :   Get or set the message encoding.

    `full_message_text`
    :   |  |  |
        | --- | --- |
        | Returns: | full text of the message. |

    *classmethod* `get_default_content_type`()
    :   Default content type for new messages.

    `get_meta`()
    :   Get message retention business context metadata.

    `get_properties`()
    :   Get the message properties.
        The properties are copied into a dict(str:str)

        |  |  |
        | --- | --- |
        | Returns: | dictionary of properties |

    `get_property`(*key*, *default=''*)
    :   Get the message property by key.

        |  |  |
        | --- | --- |
        | Parameters: | * **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – property key * **default** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – default value used if property does not exist. |
        | Returns: | value of the property based on key |

    *classmethod* `get_system_encoding`()
    :   |  |  |
        | --- | --- |
        | Returns: | the system character encoding name |

    `get_user_attributes`()
    :   Get user attributes as a dict.

        |  |  |
        | --- | --- |
        | Returns: | dictionary containing user attributes |

    `id`
    :   Get or set the message Id.

    `meta_enabled`
    :   Get message retention enabled status.

        If the value is true, then a message retention message will be sent on the message retention sink,
        if one is configured for the ioservice.

    `pyxb_encoding` *= 'utf-8'*

    `set_meta`(*meta*)
    :   Set message retention business context metadata.

        The value must be JSON compatible.

        |  |  |
        | --- | --- |
        | Parameters: | **meta** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.12)")) – message retention business context metadata. |

    `set_property`(*key*, *value*)
    :   Set a message property by key.

        |  |  |
        | --- | --- |
        | Parameters: | * **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – property key * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – set the property to this value |

###### PlainIOMessage

##### jcms.ioserver.version10.context


This module defines the context interface for version TEN.

####### 16.1.7.1. [`OnLoadServiceContext`](#jcms.ioserver.version10.context.OnLoadServiceContext "jcms.ioserver.version10.context.OnLoadServiceContext")

*class* `jcms.ioserver.version10.context.``OnLoadServiceContext`(*service\_name*, *swigged\_config*)
:   A context that provides basic information to the handlers on\_load method.

    `__init__`(*service\_name*, *swigged\_config*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `config`
    :   |  |  |
        | --- | --- |
        | Returns: | IOServer configuration ([`IConfig`](#jcms.ioserver.version10.config.IConfig "jcms.ioserver.version10.config.IConfig")) |

    `service_logger`
    :   Return a jcms logger that contains the service name
        e.g. ioserver.service\_name.service.

        |  |  |
        | --- | --- |
        | Returns: | Logger instance |

    `service_name`
    :   |  |  |
        | --- | --- |
        | Returns: | the name of the service |

####### 16.1.7.2. [`ServiceContext`](#jcms.ioserver.version10.context.ServiceContext "jcms.ioserver.version10.context.ServiceContext")

*class* `jcms.ioserver.version10.context.``ServiceContext`(*swig\_service\_context*, *is\_soap=False*, *binding\_module=None*, *skipMsgOnMarshalError=False*)
:   `__init__`(*swig\_service\_context*, *is\_soap=False*, *binding\_module=None*, *skipMsgOnMarshalError=False*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `config`
    :   |  |  |
        | --- | --- |
        | Returns: | IOServer configuration ([`IConfig`](#jcms.ioserver.version10.config.IConfig "jcms.ioserver.version10.config.IConfig")) |

    `create_io_message`(*content*, *contentType=None*, *encoding=None*, *msgId=None*)
    :   Create a new IOMessage from the complete content.

        |  |  |
        | --- | --- |
        | Parameters: | * **content** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the full message text (including envelope if its soap) * **contentType** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – content type for the new message, if omitted a message type |

        dependent default will be used
        :param str encoding: encoding for the new message, if omitted system encoding will be used
        :param str msgId: the message id for the new message, if omitted an UUID will be generated
        :return: a Python wrapped IOMessage ([`PlainIOMessage`](#jcms.ioserver.version10.message.PlainIOMessage "jcms.ioserver.version10.message.PlainIOMessage") or
        `SoapIOMessage`)

    `create_io_message_from_content`(*content*, *encoding=None*, *msgId=None*)
    :   Create a new IOMessage from the payload text. A message type dependent default will be used.

        |  |  |
        | --- | --- |
        | Parameters: | * **content** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the payload text (no envelope if its soap) * **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – encoding for the new message, if omitted system encoding will be used * **msgId** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the message id for the new message, if omitted an UUID will be generated |
        | Returns: | a Python wrapped IOMessage ([`PlainIOMessage`](#jcms.ioserver.version10.message.PlainIOMessage "jcms.ioserver.version10.message.PlainIOMessage") or |

        `SoapIOMessage`)

    `get_available_sinks`()
    :   |  |  |
        | --- | --- |
        | Returns: | list with the names of the available sinks |

    `get_default_sink_name`()
    :   Get the name of the default sink.

        If there is only a single unnamed sink, then this method returns “default”.
        If there are named sinks without any of them being designated as the
        default sink, then this method returns “”.

        |  |  |
        | --- | --- |
        | Returns: | Name of the default sink. |

    `has_request`
    :   Check if there is a request.

        |  |  |
        | --- | --- |
        | Returns: | True if context has a saved request, False otherwise |

    `has_response`
    :   Check if there is a response message.

        |  |  |
        | --- | --- |
        | Returns: | True if context has a saved response, False otherwise |

    `report_progress`()
    :   Report progress in case of long-running handle/trigger operations.

        This function lets the worker process ping main to avoid timing out
        because IOServer main thinks the process is hanging.

    `request_message`
    :   Get or set python wrapped request message.
        [`PlainIOMessage`](#jcms.ioserver.version10.message.PlainIOMessage "jcms.ioserver.version10.message.PlainIOMessage") or `SoapIOMessage`.
        :raises: ioserver.base.StaticError if trying to replace an incoming message which
        is the most common case for a handler

    `response_message`
    :   Get or set python wrapped response message.
        [`PlainIOMessage`](#jcms.ioserver.version10.message.PlainIOMessage "jcms.ioserver.version10.message.PlainIOMessage") or `SoapIOMessage`.

    `send`(*msg*)
    :   Send a message to the default queue.

        If jcms\_state property is not set in the message,
        it will be set to the current plan cid.

        |  |  |
        | --- | --- |
        | Parameters: | **msg** ([`PlainIOMessage`](#jcms.ioserver.version10.message.PlainIOMessage "jcms.ioserver.version10.message.PlainIOMessage") or) – Message to be sent |

        `SoapIOMessage`

    `send_to_sink`(*msg*, *sinkName*)
    :   Send a message to a named sink.

        If jcms\_state property is not set in the message,
        it will be set to the current plan cid.

        |  |  |
        | --- | --- |
        | Parameters: | **msg** ([`PlainIOMessage`](#jcms.ioserver.version10.message.PlainIOMessage "jcms.ioserver.version10.message.PlainIOMessage") or) – message to send |

        `SoapIOMessage`
        :param str sinkName: name of the sink as specified in the configuration.

    `service_logger`
    :   Return a jcms logger that contains the service name
        e.g. ioserver.service\_name.service.

        |  |  |
        | --- | --- |
        | Returns: | Logger instance |

    `service_name`
    :   |  |  |
        | --- | --- |
        | Returns: | the name of the service |

    `set_response_sink`(*sinkName*)
    :   Set the sink to use for response messages

        If named sinks have been configured for the service, this method can
        be used to specify which of these sinks to use for the response message.

        If the “reply-to” property has been set on the request message, that value
        will take precedence, and the sink set here will be ignored.

        If this method has not been called, the default sink for the service will be used.

        Only handler based patterns care about this value.

        |  |  |
        | --- | --- |
        | Parameters: | **sinkName** – The name of the sink to use for the response message |

###### OnLoadServiceContext

###### ServiceContext

##### jcms.ioserver.version10.mave2.IPlanHolder


####### 16.1.8.1. [`IPlanHolder`](#jcms.ioserver.version10.planholder_militaris.IPlanHolder "jcms.ioserver.version10.planholder_militaris.IPlanHolder")

*class* `jcms.ioserver.version10.planholder_militaris.``IPlanHolder`(*\*args*, *\*\*kwargs*)
:   The public API to the IOServer plan cache.

    This API provides the functions that handler implementations and tests need access to. It basically provides access to the loaded plan and ruleset objects so that their public API’s can be used.

    Handlers shall never call any undo/redo/prune, refresh save or load/unload methods on the plan which would potentially lead the plan outside the local version tree that the handler has started on. Instead they shall throw a TransientMsgError if they encounter problems that can potentially be solved by retry.

    `getMaveGeneration`(*self*)
    :   Get the mave generation of the plan (and ruleset).

        Depending on the returned number, only one kind of plan can be retrieved.

        |  |  |
        | --- | --- |
        | Returns: | * 2 for mave2/ara.macao or mave2/ara.militaris |

        **Types**
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `getDomainGeneration`(*self*)
    :   Get the domain generation of the loaded plan.

        This is the same string that will be needed to load the python binding module.

        |  |  |
        | --- | --- |
        | Returns: | the domain generation as a string |
        | Raises: | **ioserver.base.StaticError** – if no plan is loaded. |

        **Types**
        - Return type: `std` ::`string`

    `isPlanLoaded`(*self*)
    :   Check if we have a plan loaded.

        |  |  |
        | --- | --- |
        | Returns: | true if plan is loaded |

        **Types**
        - Return type: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")

    `isRulesetLoaded`(*self*)
    :   Check if we have a ruleset loaded.

        |  |  |
        | --- | --- |
        | Returns: | true if ruleset is loaded |

        **Types**
        - Return type: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")

    `getNowTime`(*self*)
    :   Get the now-timestamp used by the ruleset.

        This is a cached value from last refresh, not wall-time.

        |  |  |
        | --- | --- |
        | Returns: | now time |

        **Types**
        - Return type: `AbsTime`

    `getPlanPeriodStart`(*self*)
    :   Get the start time of the plan period, as defined in the datacontext.

        |  |  |
        | --- | --- |
        | Returns: | start time of the period |
        | Raises: | **ioserver.base.StaticError** – if time is not found in datacontext |

        **Types**
        - Return type: `AbsTime`

    `getPlanPeriodEnd`(*self*)
    :   Get the end time of the plan period, as defined in the datacontext.

        |  |  |
        | --- | --- |
        | Returns: | end time of the period |
        | Raises: | **ioserver.base.StaticError** – if time is not found in datacontext |

        **Types**
        - Return type: `AbsTime`

    `getContextParameter`(*self*, *\*args*)
    :   Get the value of a datacontext parameter.

        |  |  |
        | --- | --- |
        | Parameters: | **name** – datacontext parameter name |
        | Returns: | string representation of parameter value |
        | Raises: | **ioserver.base.StaticError** – if parameter is not found in datacontext |

        **Types**
        - Parameter name: `std` ::`string`
        - Return type: `std` ::`string`

    `getMave2ChangeSet`(*self*)
    :   Provide access to the last refresh changeset for an ara.macao Plan. the reference is only locally valid, please assign to an instance of correct type immediately.

        |  |  |
        | --- | --- |
        | Returns: | Mave2 Changeset |
        | Raises: | **ioserver.base.StaticError** – if no ara.macao plan is loaded. |

        **Types**
        - Return type: `Mave2ChangeSet`

    `getMave2PreviousVersion`(*self*)
    :   Provide access to the previous version for an ara.macao Plan. the reference is only locally valid, please assign to an instance of correct type immediately.

        |  |  |
        | --- | --- |
        | Returns: | Mave2 Version |
        | Raises: | **ioserver.base.StaticError** – if no ara.macao plan is loaded. |

        **Types**
        - Return type: `Mave2Version`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `getChangeSet`(*self*) → Mave2ChangeSet
    :   provide access to the changeset.

    `getMave2Plan`(*self*) → Mave2Plan
    :   provide access to the ara.militaris plan.

    `getMave2PlanWithViewpoint`(*self*, *dataset*) → Mave2Plan
    :   provide access to the ara.militaris plan with the specified ara Viewpoint.

    `getPlan`(*self*) → Mave2Plan
    :   provide access to the ara.militaris plan.

    `getPreviousVersion`()
    :   getMave2PreviousVersion(self) -> Mave2Version.
        provide access to the previous version for an ara.militaris Plan.

    `getRaveSession`(*self*) → ara::RaveSession.
    :   provide access to the RaveSession, if one has been loaded

    `getRaveSessionWithViewpoint`(*self*, *dataset*) → ara::RaveSession.
    :   provide access to the RaveSession with the specified ara Viewpoint,
        if one has been loaded

    *static* `getThePlan`(*\*args*)
    :   Provide access to the global plan holder instance.

        |  |  |
        | --- | --- |
        | Returns: | a shared pointer to the global plan holder instance if it has been initiated already, NULL otherwise |

        **Types**
        - Return type: [`IPlanHolder`](#jcms.ioserver.version10.planholder_militaris.IPlanHolder "jcms.ioserver.version10.planholder_militaris.IPlanHolder") ::`Pointer`

###### IPlanHolder

#### IOServer Python API Reference Version 9

##### jcms.ioserver.versions

##### jcms.ioserver.constants

##### jcms.ioserver.exceptions

##### jcms.ioserver.version9.config


####### 16.2.4.1. [`IConfig`](#jcms.ioserver.version9.config.IConfig "jcms.ioserver.version9.config.IConfig")

*class* `jcms.ioserver.version9.config.``IConfig`(*\*args*, *\*\*kwargs*)
:   Provides access to the IO-server configuration.

    The ioserver configuration is organized in global (per process) and service level configuration groups. A configuration group is a set of values (and potentially subgroups) that can be fetched by name. In the jcms configuration file syntax a configuration group corresponds to a tag that has complex content, while a value is a tag with only string content.

    The IConfig interface encapsulates the lookup logic and override hierarchy within the configuration and provides the values that are effective for this ioserver instance. Lookups with a service-specific group tag will provide the effective value for that service and sub-group, standard fallback logic to process-global and global-default values is handled by the config implementation.

    Components should lookup the values they need within their provided configuration group using getConfigValue(group, key, defvalue) or the typed equivalents.

    @deprecated Use ioserver::base::IConfig instead.

    `getConfigValue`(*self*)
    :   lookup a configuration value with given key within a group

        Each component has a configuration group provided in the constructor and should call the method with that group. Global settings directly defined on the process level can get fetched with an empty group.

        |  |  |
        | --- | --- |
        | Parameters: | * **group** – the group key of the requested configuration group * **key** – the name of the configuration value to fetch * **defValue** – a fallback value to use if no configuration is found |
        | Returns: | the value of the configuration property if found, defValue else |

        **Types**
        - Parameter group: `std` ::`string`
        - Parameter key: `std` ::`string`
        - Parameter defValue: `std` ::`string`
        - Return type: `std` ::`string`

    `getGlobalConfigGroup`(*self*)
    :   provide the lookup key for a ioserver global configuration group

        Use this method to get a group key for process-global settings.

        |  |  |
        | --- | --- |
        | Parameters: | * **groupTag** – the tag of the configuration group, like “db” or “datamodel” * **name** – the name of an instance of the configuration group if there can be more than one, otherwise empty |
        | Returns: | the group key to use for lookups of configuration in that group |

        **Types**
        - Parameter groupTag: `std` ::`string`
        - Parameter name: `std` ::`string`
        - Return type: `std` ::`string`

    `getGlobalGroupNames`(*self*)
    :   get the list of all names for parallel global configuration groups with same tag

        |  |  |
        | --- | --- |
        | Parameters: | **groupTag** – the tag of the configuration group, like “db” or “datamodel” |

        **Types**
        - Parameter groupTag: `std` ::`string`
        - Return type: `StringVectorPointer`

    `getServiceConfigGroup`(*self*)
    :   provide the lookup key for a ioserver service local configuration group

        Use this method to get a group key for service specific settings.

        |  |  |
        | --- | --- |
        | Parameters: | * **service** – the name of the service * **groupTag** – the tag of the configuration group, like “pattern” or “source” * **name** – the name of an instance of the configuration group if there can be more than one, otherwise empty |
        | Returns: | the group key to use for lookups of configuration in that group |

        **Types**
        - Parameter service: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Parameter name: `std` ::`string`
        - Return type: `std` ::`string`

    `getServiceGroupNames`(*self*)
    :   get the list of all names for parallel service configuration groups with same tag

        |  |  |
        | --- | --- |
        | Parameters: | * **service** – the name of the service * **groupTag** – the tag of the configuration group, like “pattern” or “source” |

        **Types**
        - Parameter service: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Return type: `StringVectorPointer`

    `getProcessServicePort`(*self*)
    :   Get the service port to use for the process when communicating with sysmond.

        |  |  |
        | --- | --- |
        | Parameters: | * **systemService** – The system service to look up * **hostName** – The host name to look up (default: use the current host name) * **processName** – The process name (default: use the current process name) |
        | Returns: | port number to the service or -1 if the service cannot be found |

        **Types**
        - Parameter systemService: `std` ::`string`
        - Parameter hostName: `std` ::`string`
        - Parameter processName: `std` ::`string`
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `getConfigSubGroup`(*self*)
    :   provide the lookup key for a detailed ioserver configuration group

        |  |  |
        | --- | --- |
        | Parameters: | * **parentGroup** – the group key of the requested configuration group * **groupTag** – the tag of the configuration group, like “db” or “datamodel” * **name** – the name of an instance of the configuration group if there can be more than one |
        | Returns: | the group key to use for lookups of configuration in that group |

        **Types**
        - Parameter parentGroup: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Parameter name: `std` ::`string`
        - Return type: `std` ::`string`

    `getSubGroupNames`(*self*)
    :   get the list of all names for parallel configuration groups

        **Types**
        - Parameter parentGroup: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Return type: `StringVectorPointer`

    `getServiceNames`(*self*)
    :   get the list of all service names

        **Types**
        - Return type: `StringVectorPointer`

    `getenv`(*self*)
    :   get the value of an environment variable

        |  |  |
        | --- | --- |
        | Parameters: | * **key** – the name of the variable to fetch * **defValue** – a fallback value to use if the variable is not set |
        | Returns: | the value of the environment variable if set, otherwise defValue |

        **Types**
        - Parameter key: `std` ::`string`
        - Parameter defValue: `std` ::`string`
        - Return type: `std` ::`string`

    `getConfigInt`(*self*)
    :   helper to fetch integer value

        find the configuration value and convert it to an integer.
        getConfigValue(const std::string&, const std::string& ,const std::string& )

        |  |  |
        | --- | --- |
        | Parameters: | * **group** – the group key of the requested configuration group * **key** – the configuration key (within the group) * **defValue** – a fallback value to use if no configuration is found |
        | Returns: | the value of the configuration property if its found, defValue else |
        | Raises: | **ioserver.base.ConfigurationError** – if the value doesn’t convert to int |

        **Types**
        - Parameter group: `std` ::`string`
        - Parameter key: `std` ::`string`
        - Parameter defValue: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `getConfigBool`(*self*)
    :   helper to fetch boolean value

        find the configuration value and convert it to a boolean. A value of “true” is regarded true, all other values are false.

        |  |  |
        | --- | --- |
        | Parameters: | * **group** – the group key of the requested configuration group * **key** – the configuration key (within the group) * **defValue** – a fallback value to use if no configuration is found |
        | Returns: | the value of the configuration property if its found, defValue else |

        **Types**
        - Parameter group: `std` ::`string`
        - Parameter key: `std` ::`string`
        - Parameter defValue: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")

    `getProcessName`(*self*)
    :   Get the proccess name.

        |  |  |
        | --- | --- |
        | Returns: | the name of the process |

        **Types**
        - Return type: `std` ::`string`

    `getPortBase`(*self*)
    :   Get the portbase.

        |  |  |
        | --- | --- |
        | Returns: | the portbase number, -1 on error |

        **Types**
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `getProcessServiceUrl`(*self*)
    :   get the service URL for a given system service

        |  |  |
        | --- | --- |
        | Parameters: | * **systemService** – The system service to look up * **hostName** – The host where to look for the service. Empty string means localhost. Default is empty string. * **processName** – The name of the process which provides the service. Empty string means use the process name which was given when calling the constructor (in this class). |
        | Returns: | URL with the format <service://host:port> or empty string if service is not found. |

        **Types**
        - Parameter systemService: `std` ::`string`
        - Parameter hostName: `std` ::`string`
        - Parameter processName: `std` ::`string`
        - Return type: `std` ::`string`

    `getSubGroups`(*self*)
    :   get the list of all groups for parallel configuration groups

        **Types**
        - Parameter parentGroup: `std` ::`string`
        - Parameter groupTag: `std` ::`string`
        - Return type: `StringVector`

    `getConfigAttribute`(*self*)
    :   Get a configuration attribute with given key within a group.

        |  |  |
        | --- | --- |
        | Parameters: | * **group** – the group key of the requested configuration group * **attribute** – the name of the configuration attribute to fetch * **defValue** – a fallback value to use if no configuration is found |
        | Returns: | the value of the configuration attribute if found, defValue else |

        **Types**
        - Parameter group: `std` ::`string`
        - Parameter attribute: `std` ::`string`
        - Parameter defValue: `std` ::`string`
        - Return type: `std` ::`string`

    `getConfigAttributes`(*self*)
    :   Get all configuration attributes, including values, within a group.

        Any “name” attributes are ignored as the configuration API handles them separately.

        |  |  |
        | --- | --- |
        | Parameters: | **group** – the group key of the requested configuration group |
        | Returns: | map of attribute name to attribute value. |

        **Types**
        - Parameter group: `std` ::`string`
        - Return type: `StringMap`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

###### IConfig

##### jcms.ioserver.version9.actions


This module defines the action codes that version NINE handlers can return.

####### 16.2.5.1. [`PlanAction`](#jcms.ioserver.version9.actions.PlanAction "jcms.ioserver.version9.actions.PlanAction")

*class* `jcms.ioserver.version9.actions.``PlanAction`
:   Version 9 Handler actions. Specifies what the pattern should do when a handler returns.
    Return value from handler methods.

    `ROLLBACK` *= 2*
    :   Roll back the modifications in the plan.

    `SAVE` *= 0*
    :   Save the current state of the plan.

    `UNCHANGED` *= 1*
    :   The plan does not need to be saved.

####### 16.2.5.2. [`FaultAction`](#jcms.ioserver.version9.actions.FaultAction "jcms.ioserver.version9.actions.FaultAction")

*class* `jcms.ioserver.version9.actions.``FaultAction`
:   Version 9 Fault actions. Specifies what the pattern should respond when an exception is raised.
    Return value from the on\_fault method in the handler module.

    `DEFAULT_RESPONSE` *= 0*
    :   Create a default error response message. Only supported for SOAP messages.

    `NO_RESPONSE` *= 1*
    :   Do not send a response.

    `SEND_RESPONSE` *= 2*
    :   Send the response message that the handler module has produced.

###### PlanAction

###### FaultAction

##### jcms.ioserver.version9.message


This module defines the Message classes available to version NINE handlers/triggers.

####### 16.2.6.1. [`PlainIOMessage`](#jcms.ioserver.version9.message.PlainIOMessage "jcms.ioserver.version9.message.PlainIOMessage")

*class* `jcms.ioserver.version9.message.``PlainIOMessage`(*io\_message*, *pyxb\_binding=None*, *skipMsgOnMarshalError=True*)
:   IOMessage with plain text or XML content.

    `__init__`(*io\_message*, *pyxb\_binding=None*, *skipMsgOnMarshalError=True*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `content`
    :   Get or set the message content.

    `content_type`
    :   Get or set the message content-type.

    *classmethod* `create_io_message`(*content*, *contentType=None*, *encoding=None*, *msgId=None*)
    :   Factory method for creating a Plain IOMessage.

        |  |  |
        | --- | --- |
        | Parameters: | * **content** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.12)")) – the message content * **contentType** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the type of the content, can be e.g. text or binary * **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the text encoding used * **msgId** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – id for the message |
        | Returns: | IOMessage SWIG object without wrapper |

    `encoding`
    :   Get or set the message encoding.

    `full_message_text`
    :   |  |  |
        | --- | --- |
        | Returns: | full text of the message. |

    *classmethod* `get_default_content_type`()
    :   Default content type for new messages.

    `get_properties`()
    :   Get the message properties.
        The properties are copied into a dict(str:str)

        |  |  |
        | --- | --- |
        | Returns: | dictionary of properties |

    `get_property`(*key*, *default=''*)
    :   Get the message property by key.

        |  |  |
        | --- | --- |
        | Parameters: | * **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – property key * **default** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – default value used if property does not exist. |
        | Returns: | value of the property based on key |

    *classmethod* `get_system_encoding`()
    :   |  |  |
        | --- | --- |
        | Returns: | the system character encoding name |

    `get_user_attributes`()
    :   Get user attributes as a dict.

        |  |  |
        | --- | --- |
        | Returns: | dictionary containing user attributes |

    `id`
    :   Get or set the message Id.

    `pyxb_encoding` *= 'utf-8'*

    `set_property`(*key*, *value*)
    :   Set a message property by key.

        |  |  |
        | --- | --- |
        | Parameters: | * **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – property key * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – set the property to this value |

###### PlainIOMessage

##### jcms.ioserver.version9.context


This module defines the context interface for version NINE.

####### 16.2.7.1. [`ServiceContext`](#jcms.ioserver.version9.context.ServiceContext "jcms.ioserver.version9.context.ServiceContext")

*class* `jcms.ioserver.version9.context.``ServiceContext`(*swig\_service\_context*, *is\_soap=False*, *binding\_module=None*, *skipMsgOnMarshalError=False*)
:   `__init__`(*swig\_service\_context*, *is\_soap=False*, *binding\_module=None*, *skipMsgOnMarshalError=False*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `config`
    :   |  |  |
        | --- | --- |
        | Returns: | IOServer configuration ([`IConfig`](#jcms.ioserver.version9.config.IConfig "jcms.ioserver.version9.config.IConfig")) |

    `create_io_message`(*content*, *contentType=None*, *encoding=None*, *msgId=None*)
    :   Create a new IOMessage from the complete content.

        |  |  |
        | --- | --- |
        | Parameters: | * **content** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the full message text (including envelope if its soap) * **contentType** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – content type for the new message, if omitted a message type |

        dependent default will be used
        :param str encoding: encoding for the new message, if omitted system encoding will be used
        :param str msgId: the message id for the new message, if omitted an UUID will be generated
        :return: a Python wrapped IOMessage ([`PlainIOMessage`](#jcms.ioserver.version9.message.PlainIOMessage "jcms.ioserver.version9.message.PlainIOMessage") or
        `SoapIOMessage`)

    `create_io_message_from_content`(*content*, *encoding=None*, *msgId=None*)
    :   Create a new IOMessage from the payload text. A message type dependent default will be used.

        |  |  |
        | --- | --- |
        | Parameters: | * **content** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the payload text (no envelope if its soap) * **encoding** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – encoding for the new message, if omitted system encoding will be used * **msgId** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – the message id for the new message, if omitted an UUID will be generated |
        | Returns: | a Python wrapped IOMessage ([`PlainIOMessage`](#jcms.ioserver.version9.message.PlainIOMessage "jcms.ioserver.version9.message.PlainIOMessage") or |

        `SoapIOMessage`)

    `get_available_sinks`()
    :   |  |  |
        | --- | --- |
        | Returns: | list with the names of the available sinks |

    `has_request`
    :   Check if there is a request.

        |  |  |
        | --- | --- |
        | Returns: | True if context has a saved request, False otherwise |

    `has_response`
    :   Check if there is a response message.

        |  |  |
        | --- | --- |
        | Returns: | True if context has a saved response, False otherwise |

    `report_progress`()
    :   Report progress in case of long-running handle/trigger operations.

        This function lets the worker process ping main to avoid timing out
        because IOServer main thinks the process is hanging.

    `request_message`
    :   Get or set python wrapped request message.
        [`PlainIOMessage`](#jcms.ioserver.version9.message.PlainIOMessage "jcms.ioserver.version9.message.PlainIOMessage") or `SoapIOMessage`.
        :raises: ioserver.base.StaticError if trying to replace an incoming message which
        is the most common case for a handler

    `response_message`
    :   Get or set python wrapped response message.
        [`PlainIOMessage`](#jcms.ioserver.version9.message.PlainIOMessage "jcms.ioserver.version9.message.PlainIOMessage") or `SoapIOMessage`.

    `send`(*msg*)
    :   Send a message to the default queue.

        If jcms\_state property is not set in the message,
        it will be set to the current plan cid.

        |  |  |
        | --- | --- |
        | Parameters: | **msg** ([`PlainIOMessage`](#jcms.ioserver.version9.message.PlainIOMessage "jcms.ioserver.version9.message.PlainIOMessage") or) – Message to be sent |

        `SoapIOMessage`

    `send_to_sink`(*msg*, *sinkName*)
    :   Send a message to a named sink.

        If jcms\_state property is not set in the message,
        it will be set to the current plan cid.

        |  |  |
        | --- | --- |
        | Parameters: | **msg** ([`PlainIOMessage`](#jcms.ioserver.version9.message.PlainIOMessage "jcms.ioserver.version9.message.PlainIOMessage") or) – message to send |

        `SoapIOMessage`
        :param str sinkName: name of the sink as specified in the configuration.

    `service_logger`
    :   Return a jcms logger that contains the service name
        e.g. ioserver.service\_name.service.

        |  |  |
        | --- | --- |
        | Returns: | Logger instance |

    `service_name`
    :   |  |  |
        | --- | --- |
        | Returns: | the name of the service |

    `set_response_sink`(*sinkName*)
    :   Set the sink to use for response messages

        If named sinks have been configured for the service, this method can
        be used to specify which of these sinks to use for the response message.

        If the “reply-to” property has been set on the request message, that value
        will take precedence, and the sink set here will be ignored.

        If this method has not been called, the default sink for the service will be used.

        Only handler based patterns care about this value.

        |  |  |
        | --- | --- |
        | Parameters: | **sinkName** – The name of the sink to use for the response message |

###### ServiceContext

##### jcms.ioserver.version9.mave2.IPlanHolder


####### 16.2.8.1. [`IPlanHolder`](#jcms.ioserver.version9.planholder_militaris.IPlanHolder "jcms.ioserver.version9.planholder_militaris.IPlanHolder")

*class* `jcms.ioserver.version9.planholder_militaris.``IPlanHolder`(*\*args*, *\*\*kwargs*)
:   The public API to the IOServer plan cache.

    This API provides the functions that handler implementations and tests need access to. It basically provides access to the loaded plan and ruleset objects so that their public API’s can be used.

    Handlers shall never call any undo/redo/prune, refresh save or load/unload methods on the plan which would potentially lead the plan outside the local version tree that the handler has started on. Instead they shall throw a TransientMsgError if they encounter problems that can potentially be solved by retry.

    @deprecated Use ioserver::base::IPlanHolder instead.

    `getMaveGeneration`(*self*)
    :   Get the mave generation of the plan (and ruleset).

        Depending on the returned number, only one kind of plan can be retrieved.

        |  |  |
        | --- | --- |
        | Returns: | * 2 for mave2/ara.macao or mave2/ara.militaris |

        **Types**
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `getDomainGeneration`(*self*)
    :   Get the domain generation of the loaded plan.

        This is the same string that will be needed to load the python binding module.

        |  |  |
        | --- | --- |
        | Returns: | the domain generation as a string |
        | Raises: | **ioserver.base.StaticError** – if no plan is loaded. |

        **Types**
        - Return type: `std` ::`string`

    `isPlanLoaded`(*self*)
    :   Check if we have a plan loaded.

        |  |  |
        | --- | --- |
        | Returns: | true if plan is loaded |

        **Types**
        - Return type: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")

    `isRulesetLoaded`(*self*)
    :   Check if we have a ruleset loaded.

        |  |  |
        | --- | --- |
        | Returns: | true if ruleset is loaded |

        **Types**
        - Return type: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")

    `getNowTime`(*self*)
    :   Get the now-timestamp used by the ruleset.

        This is a cached value from last refresh, not wall-time.

        |  |  |
        | --- | --- |
        | Returns: | now time |

        **Types**
        - Return type: `AbsTime`

    `getPlanPeriodStart`(*self*)
    :   Get the start time of the plan period, as defined in the datacontext.

        |  |  |
        | --- | --- |
        | Returns: | start time of the period |
        | Raises: | **ioserver.base.StaticError** – if time is not found in datacontext |

        **Types**
        - Return type: `AbsTime`

    `getPlanPeriodEnd`(*self*)
    :   Get the end time of the plan period, as defined in the datacontext.

        |  |  |
        | --- | --- |
        | Returns: | end time of the period |
        | Raises: | **ioserver.base.StaticError** – if time is not found in datacontext |

        **Types**
        - Return type: `AbsTime`

    `getContextParameter`(*self*, *\*args*)
    :   Get the value of a datacontext parameter.

        |  |  |
        | --- | --- |
        | Parameters: | **name** – datacontext parameter name |
        | Returns: | string representation of parameter value |
        | Raises: | **ioserver.base.StaticError** – if parameter is not found in datacontext |

        **Types**
        - Parameter name: `std` ::`string`
        - Return type: `std` ::`string`

    `getMave2ChangeSet`(*self*)
    :   Provide access to the last refresh changeset for an ara.macao Plan. the reference is only locally valid, please assign to an instance of correct type immediately.

        |  |  |
        | --- | --- |
        | Returns: | Mave2 Changeset |
        | Raises: | **ioserver.base.StaticError** – if no ara.macao plan is loaded. |

        **Types**
        - Return type: `Mave2ChangeSet`

    `getMave2PreviousVersion`(*self*)
    :   Provide access to the previous version for an ara.macao Plan. the reference is only locally valid, please assign to an instance of correct type immediately.

        |  |  |
        | --- | --- |
        | Returns: | Mave2 Version |
        | Raises: | **ioserver.base.StaticError** – if no ara.macao plan is loaded. |

        **Types**
        - Return type: `Mave2Version`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `getChangeSet`(*self*) → Mave2ChangeSet
    :   provide access to the changeset.

    `getMave2Plan`(*self*) → Mave2Plan
    :   provide access to the ara.militaris plan.

    `getMave2PlanWithViewpoint`(*self*, *dataset*) → Mave2Plan
    :   provide access to the ara.militaris plan with the specified ara Viewpoint.

    `getPlan`(*self*) → Mave2Plan
    :   provide access to the ara.militaris plan.

    `getPreviousVersion`()
    :   getMave2PreviousVersion(self) -> Mave2Version.
        provide access to the previous version for an ara.militaris Plan.

    `getRaveSession`(*self*) → ara::RaveSession.
    :   provide access to the RaveSession, if one has been loaded

    `getRaveSessionWithViewpoint`(*self*, *dataset*) → ara::RaveSession.
    :   provide access to the RaveSession with the specified ara Viewpoint,
        if one has been loaded

    *static* `getThePlan`(*\*args*)
    :   Provide access to the global plan holder instance.

        |  |  |
        | --- | --- |
        | Returns: | a shared pointer to the global plan holder instance if it has been initiated already, NULL otherwise |

        **Types**
        - Return type: [`IPlanHolder`](#jcms.ioserver.version9.planholder_militaris.IPlanHolder "jcms.ioserver.version9.planholder_militaris.IPlanHolder") ::`Pointer`

###### IPlanHolder

### Testutils Python API reference


API reference for the Testutils public python interface.
Used for developing and testing of handlers and triggers.

##### 17.1. TestUtils Python API Reference Version 10

* [17.1.1. Conflict Detection Strategy Constants](python_testutils_api_ver10_reference.html)
* [17.1.2. `jcms.ioserver.testutils.version10.main.TestMain`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-main-testmain)
* [17.1.3. `jcms.ioserver.testutils.version10.main.IMemoryHAStore`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-main-imemoryhastore)
* [17.1.4. `jcms.ioserver.testutils.version10.main.IMemoryQueue`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-main-imemoryqueue)
* [17.1.5. `jcms.ioserver.testutils.version10.main.ITestConfig`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-main-itestconfig)
* [17.1.6. `jcms.ioserver.testutils.version10.TestRunner`](python_testutils_api_ver10_reference.html#jcms-ioserver-testutils-version10-testrunner)

##### 17.2. TestUtils Python API Reference Version 9

* [17.2.1. `jcms.ioserver.testutils.version9.main.TestMain`](python_testutils_api_ver9_reference.html)
* [17.2.2. `jcms.ioserver.testutils.version9.main.IMemoryHAStore`](python_testutils_api_ver9_reference.html#jcms-ioserver-testutils-version9-main-imemoryhastore)
* [17.2.3. `jcms.ioserver.testutils.version9.main.IMemoryQueue`](python_testutils_api_ver9_reference.html#jcms-ioserver-testutils-version9-main-imemoryqueue)
* [17.2.4. `jcms.ioserver.testutils.version9.main.ITestConfig`](python_testutils_api_ver9_reference.html#jcms-ioserver-testutils-version9-main-itestconfig)
* [17.2.5. `jcms.ioserver.testutils.version9.TestRunner`](python_testutils_api_ver9_reference.html#jcms-ioserver-testutils-version9-testrunner)

#### TestUtils Python API Reference Version 10

##### Conflict Detection Strategy Constants


`ConflictDetectionDisabled`
:   No conflict detection during save.

`ConflictDetectionMessage`
:   Use the commit id from the message (JCMS\_STATE) for detecting conflicts during save.

`ConflictDetectionPlan`
:   Use the commit id from the plan for detecting conflicts during save.

##### jcms.ioserver.testutils.version10.main.TestMain


*class* `jcms.ioserver.testutils.version10.main.``TestMain`(*serviceName*)
:   Describes an IO-server test runner object that keeps the whole functionality together for unittesting.

    `getConfig`(*self*)
    :   Get the configuration object.

        |  |  |
        | --- | --- |
        | Returns: | a pointer to the global configuration. Use this to setup the ioserver parameters. |

        **Types**
        - Return type: `ioserver` ::`testbase` ::[`ITestConfig`](#jcms.ioserver.testutils.version10.main.ITestConfig "jcms.ioserver.testutils.version10.main.ITestConfig") ::`Pointer`

    `getMemoryQueue`(*self*)
    :   Get the memory global queue.

        If the config was set to use memory queue then the handler will use this queue.

        |  |  |
        | --- | --- |
        | Returns: | a pointer to the global memory queue. |

        **Types**
        - Return type: `ioserver` ::`testbase` ::[`IMemoryQueue`](#jcms.ioserver.testutils.version10.main.IMemoryQueue "jcms.ioserver.testutils.version10.main.IMemoryQueue") ::`Pointer`

    `getMemoryHAStore`(*self*)
    :   Get the memory HA store object.

        |  |  |
        | --- | --- |
        | Returns: | a pointer to the memory HA store object. |

        **Types**
        - Return type: `ioserver` ::`testbase` ::[`IMemoryHAStore`](#jcms.ioserver.testutils.version10.main.IMemoryHAStore "jcms.ioserver.testutils.version10.main.IMemoryHAStore") ::`Pointer`

    `getRunner`(*self*)
    :   Get the runner object.

        After setting up the configuration the runner is initialized on first access.
        The runner is the test engine of the IOServer, it will load the plan and
        execute the service under test.

        Once the runner has been obtained, the configuration will be locked,
        all attempts to set more configuration values will result in an exception.

        |  |  |
        | --- | --- |
        | Returns: | a pointer to the runner object. |

    `__init__`(*serviceName*)
    :   constructor

        **Types**
        - Parameter serviceName: `std` ::`string`

##### jcms.ioserver.testutils.version10.main.IMemoryHAStore


*class* `jcms.ioserver.testutils.version10.main.``IMemoryHAStore`(*\*args*, *\*\*kwargs*)
:   This interface provides access to a memory based HA store for testing purposes.

    The most commonly used HA store key is “generation”. It is used to specify the latest handled commit id.

    `hasValue`(*self*)
    :   Check if there is a value in the HA key-value store for the given key.

        |  |  |
        | --- | --- |
        | Parameters: | **key** – The key to check for. |

        **Types**
        - Parameter key: `std` ::`string`
        - Return type: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")

    `getValue`(*self*)
    :   Get a value from the HA key-value store.

        |  |  |
        | --- | --- |
        | Parameters: | **key** – The key for which to retrieve a value. |
        | Returns: | The value associated with the given key. |
        | Raises: | **ioserver.base.StaticError** – if there is no value for key. |

        **Types**
        - Parameter key: `std` ::`string`
        - Return type: `std` ::`string`

    `setValue`(*self*)
    :   Set a key-value pair in the HA key-value store.

        |  |  |
        | --- | --- |
        | Parameters: | * **key** – The key to write. * **value** – The value associated with key. |

        **Types**
        - Parameter key: `std` ::`string`
        - Parameter value: `std` ::`string`
        - Return type: `void`

    `clear`(*self*)
    :   Clear all internal state.

        **Types**
        - Return type: `void`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

##### jcms.ioserver.testutils.version10.main.IMemoryQueue


*class* `jcms.ioserver.testutils.version10.main.``IMemoryQueue`(*\*args*, *\*\*kwargs*)
:   This interface provides access to the built in memory queue for testing purposes.

    `reset`(*self*)
    :   Reset content of input and output message lists.

        **Types**
        - Return type: `void`

    `getDefaultInputContentType`(*self*)
    :   Get the default content type to use for new input messages.

        |  |  |
        | --- | --- |
        | Returns: | the default content type |

        **Types**
        - Return type: `std` ::`string`

    `setDefaultInputContentType`(*self*, *\*args*)
    :   Set the default content type to use for new input messages.

        |  |  |
        | --- | --- |
        | Parameters: | **content\_type** – the content type |

        **Types**
        - Parameter content\_type: `std` ::`string`
        - Return type: `void`

    `getDefaultInputEncoding`(*self*)
    :   Get the default encoding to use for new input messages.

        |  |  |
        | --- | --- |
        | Returns: | the default encoding |

        **Types**
        - Return type: `std` ::`string`

    `setDefaultInputEncoding`(*self*, *\*args*)
    :   Set the default encoding to use for new input messages.

        |  |  |
        | --- | --- |
        | Parameters: | **encoding** – the encoding |

        **Types**
        - Parameter encoding: `std` ::`string`
        - Return type: `void`

    `setStartId`(*self*, *\*args*)
    :   Provide a start value for generating the msgIds, default is 0.

        |  |  |
        | --- | --- |
        | Parameters: | **index** – start value for generating msgIds |

        **Types**
        - Parameter index: `size_t`
        - Return type: `void`

    `getStartId`(*self*)
    :   **Types**
        - Return type: `size_t`

    `addInputIOMessage`(*self*, *\*args*)
    :   Add an IOMessage to the input queue.

        |  |  |
        | --- | --- |
        | Parameters: | **msg** – the input message |
        | Returns: | index of message in the queue |

        **Types**
        - Parameter msg: `IOMessagePointer`
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `setInputIOMessages`(*self*, *\*args*)
    :   Replace current input queue content with a new message list.

        |  |  |
        | --- | --- |
        | Parameters: | **msgVec** – list of messages to be put on the queue |

        **Types**
        - Parameter msgVec: `IOMessageList`
        - Return type: `void`

    `getInputSize`(*self*)
    :   Get the size of input message queue.

        |  |  |
        | --- | --- |
        | Returns: | size of the input message list |

        **Types**
        - Return type: `size_t`

    `getInputIOMessages`(*self*)
    :   Get the current input queue content.

        |  |  |
        | --- | --- |
        | Returns: | list of the messages on the input queue |

        **Types**
        - Return type: `IOMessageList`

    `getInputIOMessage`(*self*, *\*args*)
    :   Get the input message at given index.

        |  |  |
        | --- | --- |
        | Parameters: | **index** – the message index to get |
        | Returns: | message at index |

        **Types**
        - Parameter index: `size_t`
        - Return type: `IOMessagePointer`

    `getOutputSize`(*self*)
    :   Get size of output message queue of default sink.

        |  |  |
        | --- | --- |
        | Returns: | size of the output message list |

        **Types**
        - Return type: `size_t`

    `getOutputIOMessages`(*self*)
    :   Get the current output queue content of default sink.

        |  |  |
        | --- | --- |
        | Returns: | list of the messages on the output queue |

        **Types**
        - Return type: `IOMessageList`

    `getOutputIOMessage`(*self*, *\*args*)
    :   Get the output message at given index of default sink.

        |  |  |
        | --- | --- |
        | Parameters: | **index** – the message index to get |
        | Returns: | message at index |

        **Types**
        - Parameter index: `size_t`
        - Return type: `IOMessagePointer`

    `getOutputSizeByName`(*self*, *\*args*)
    :   Get size of output message queue.

        |  |  |
        | --- | --- |
        | Parameters: | **sinkName** – name of the sink |
        | Returns: | size of the output message list |

        **Types**
        - Parameter sinkName: `std` ::`string`
        - Return type: `size_t`

    `getOutputIOMessagesByName`(*self*, *\*args*)
    :   Get the current output queue content.

        |  |  |
        | --- | --- |
        | Parameters: | **sinkName** – name of the sink |
        | Returns: | list of the messages on the output queue |

        **Types**
        - Parameter sinkName: `std` ::`string`
        - Return type: `IOMessageList`

    `getOutputIOMessageByName`(*self*, *\*args*)
    :   Get the output message at given index.

        |  |  |
        | --- | --- |
        | Parameters: | * **sinkName** – name of the sink * **index** – the message index to get |
        | Returns: | message at index |

        **Types**
        - Parameter sinkName: `std` ::`string`
        - Parameter index: `size_t`
        - Return type: `IOMessagePointer`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

##### jcms.ioserver.testutils.version10.main.ITestConfig


*class* `jcms.ioserver.testutils.version10.main.``ITestConfig`(*\*args*, *\*\*kwargs*)
:   Provides configuration for an IOServer mock-instance

    The interface allows steering the mock implementation, chose which real components should be used and which others to replace by mock-objects (e.g memory queue instead of qpid)

    `debugPrint`(*self*)
    :   Print the configuration content.

        **Types**
        - Parameter s: `std` ::`ostream`
        - Return type: `void`

    `importProcessConfig`(*self*, *\*args*)
    :   Import from system configuration.

        Imports the settings for the tests serviceName from the configuration for the given IOServer process.

        |  |  |
        | --- | --- |
        | Parameters: | * **process** – the name of the IOServer process to copy from * **cfgFile** – the name of the config root file if not standard. |

        **Types**
        - Parameter process: `std` ::`string`
        - Parameter cfgFile: `std` ::`string`
        - Return type: `void`

    `getProcessName`(*self*)
    :   Get the common config process name.

        |  |  |
        | --- | --- |
        | Returns: | process name |

        **Types**
        - Return type: `std` ::`string`

    `getServiceNames`(*self*)
    :   Get the list of all service names.

        |  |  |
        | --- | --- |
        | Returns: | list containing all service names |

        **Types**
        - Return type: `StringVectorPointer`

    `getProcessServicePort`(*self*, *\*args*)
    :   Get the service port to use for the process when communicating with sysmond.

        |  |  |
        | --- | --- |
        | Parameters: | * **systemService** – the system service to look up * **hostName** – the host name to look up (default: use the current host name) * **processName** – the process name (default: use the current process name) |
        | Returns: | port number |

        **Types**
        - Parameter systemService: `std` ::`string`
        - Parameter hostName: `std` ::`string`
        - Parameter processName: `std` ::`string`
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `setTestBinding`(*self*, *\*args*)
    :   Use a test-provided bridge.

        |  |  |
        | --- | --- |
        | Parameters: | * **isHandler** – whether this is a handler or trigger * **bridgeName** – name of the test bridge * **handlerName** – name of the handler or trigger |

        **Types**
        - Parameter isHandler: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter bridgeName: `std` ::`string`
        - Parameter handlerName: `std` ::`string`
        - Return type: `void`

    `setPythonBinding`(*self*, *\*args*)
    :   Use a python bridge.

        |  |  |
        | --- | --- |
        | Parameters: | * **isHandler** – whether this is a handler or trigger * **protocol** – the name of the message protocol (plain or soap) * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter isHandler: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter protocol: `std` ::`string`
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `setPythonHandlerPlainBinding`(*self*, *\*args*)
    :   Use python bridge with plain handler.

        |  |  |
        | --- | --- |
        | Parameters: | * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `setPythonHandlerSoapBinding`(*self*, *\*args*)
    :   Use python bridge with a soap xml handler.

        |  |  |
        | --- | --- |
        | Parameters: | * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `setPythonTriggerPlainBinding`(*self*, *\*args*)
    :   Use python bridge with a plain trigger.

        |  |  |
        | --- | --- |
        | Parameters: | * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `setPythonTriggerSoapBinding`(*self*, *\*args*)
    :   Use python bridge with a soap xml trigger.

        |  |  |
        | --- | --- |
        | Parameters: | * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `skipPlan`(*self*)
    :   Prepare a plan and ruleset configuration that will not load any ARA plan or ruleset.

        |  |  |
        | --- | --- |
        | Raises: | **StaticError** – if a plan has already been chosen |

        **Types**
        - Return type: `void`

    `setDatabase`(*self*, *\*args*)
    :   Prepare the database connection configuration.

        Prepare database connection configuration with explicit schema setup.

        |  |  |
        | --- | --- |
        | Parameters: | * **connectString** – the Dave connectstring to use * **dbschema** – the schema name (default = “”) |

        **Types**
        - Parameter connectString: `std` ::`string`
        - Parameter dbschema: `std` ::`string`
        - Return type: `void`

    `setDomainGeneration`(*self*, *\*args*)
    :   Override the domain generation for the plan.

        |  |  |
        | --- | --- |
        | Parameters: | * **domain** – the domain generation string “air1” or “air2” * **planBuilder** – name of a custom plan builder type, this requires a special driver lib that registers a driver with this name. Typical value is “mave2”. |

        **Types**
        - Parameter domain: `std` ::`string`
        - Parameter planBuilder: `std` ::`string`
        - Return type: `void`

    `getDomainGeneration`(*self*)
    :   Retrieve the domain generation setting.

        |  |  |
        | --- | --- |
        | Returns: | the domain generation setting (“air1” or “air2”) |

        **Types**
        - Return type: `std` ::`string`

    `getPlanBuilderName`(*self*)
    :   Retrieve the plan builder setting.

        |  |  |
        | --- | --- |
        | Returns: | the name of the plan builder types, typical “mave2” |

        **Types**
        - Return type: `std` ::`string`

    `setRulesetType`(*self*, *\*args*)
    :   Set the ruleset type that will be used.

        Only valid when using mave2 based plans.

        |  |  |
        | --- | --- |
        | Parameters: | **rulesetType** – name of ruleset type to use. Requires that a driver lib has registered a driver with support for this ruleset. Typical value is “rave” (for rave::Ruleset type). |

        **Types**
        - Parameter rulesetType: `std` ::`string`
        - Return type: `void`

    `getRulesetType`(*self*)
    :   Get the ruleset type used.

        Only valid for mave2 plans.

        |  |  |
        | --- | --- |
        | Returns: | Name of ruleset type to use (“rave”). Default is an empty string. |

        **Types**
        - Return type: `std` ::`string`

    `setPlan`(*self*, *\*args*)
    :   Prepare the plan configuration.

        Use this to specify a datacontext but no ruleset.

        |  |  |
        | --- | --- |
        | Parameters: | * **datacontext** – the name of the datacontext to load * **snapshotpath** – path to snapshot location for this datacontext this will be given to the plan factory if provided. |

        **Types**
        - Parameter datacontext: `std` ::`string`
        - Parameter snapshotpath: `std` ::`string`
        - Return type: `void`

    `setRuleset`(*self*, *\*args*)
    :   Prepare the ruleset configuration.

        |  |  |
        | --- | --- |
        | Parameters: | * **ruleset** – the name of the global ruleset to load * **parameterset** – the name of the parameter set to load, if empty no parameters are set |

        **Types**
        - Parameter ruleset: `std` ::`string`
        - Parameter parameterset: `std` ::`string`
        - Return type: `void`

    `setNow`(*self*, *\*args*)
    :   Provide an override for now.

        This will influence the datacontext selections as well as rave.

        |  |  |
        | --- | --- |
        | Parameters: | **nowString** – a valid Rave datetime expression as in basics::time::minutes\_from\_expr() |

        **Types**
        - Parameter nowString: `std` ::`string`
        - Return type: `void`

    `setMemoryQueue`(*self*)
    :   Setup configuration to use the builtin memory queue.

        The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure. This is a convenience menthod that will set up a defult source queue and a defualt sink queue.

        To set up named sinks, use :meth:setNamedMemorySink and :meth:setMemorySource

        **Types**
        - Return type: `void`

    `setQpid`(*self*, *\*args*)
    :   Setup parameters for qpid.

        Use this to run tests against real ActiveMQ queues.

        |  |  |
        | --- | --- |
        | Parameters: | * **host** – the host to connect to ActiveMQ * **port** – the port on host * **queueName** – the queue name to work on * **prefetchCapacity** – the prefetch capacity of qpid receiver * **compress** – the switch for compressing the content of the message * **maxContentSize** – the maximum content size of the message compressed or not. |

        **Types**
        - Parameter host: `std` ::`string`
        - Parameter port: `std` ::`string`
        - Parameter queueName: `std` ::`string`
        - Parameter prefetchCapacity: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter compress: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter maxContentSize: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setQpidMessageSource`(*self*, *\*args*)
    :   Setup parameters for qpid message source.

        Use this to run tests against real ActiveMQ queues.

        |  |  |
        | --- | --- |
        | Parameters: | * **brokerHost** – ActiveMQ broker host address * **brokerPort** – ActiveMQ broker host port * **queueName** – queue name to use * **prefetchCapacity** – number of messages to prefetch in the background |

        **Types**
        - Parameter brokerHost: `std` ::`string`
        - Parameter brokerPort: `std` ::`string`
        - Parameter queueName: `std` ::`string`
        - Parameter prefetchCapacity: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setQpidMessageSink`(*self*, *\*args*)
    :   Setup parameters for qpid message sink.

        Use this to run tests with real ActiveMQ queues.

        |  |  |
        | --- | --- |
        | Parameters: | * **brokerHost** – ActiveMQ broker host address * **brokerPort** – ActiveMQ broker host port * **queueName** – queue name to use * **sinkName** – name of this sink. Default sets default sink * **senderCapacity** – Number of messages to buffer up when using asynchronous send(). Default 0 (synchronous send) * **compress** – set to true if the message should be gzipped. Default false * **maxContentSize** – Maximum content size. Default 0 |

        **Types**
        - Parameter brokerHost: `std` ::`string`
        - Parameter brokerPort: `std` ::`string`
        - Parameter queueName: `std` ::`string`
        - Parameter sinkName: `std` ::`string`
        - Parameter senderCapacity: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter compress: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter maxContentSize: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setSubscriberPattern`(*self*, *\*args*)
    :   Setup parameters for the subscriber pattern.

        Use the subscriber pattern with default settings for test.

        All messages in the inqueue will be handled before returning. No retry will be attempted and any exceptions from the handler or surrounding modules will just be raised up to the calling test.

        This doesn’t affect the pattern-neutral error strategy settings, like global retries (default 3 ) or skipmessage (default true).

        |  |  |
        | --- | --- |
        | Parameters: | * **cacsRole** – name of the cacs role to use * **saving** – whether the plan should be saved after handling the messages, default false. * **chunkSize** – how many message to save per chunk, -1 for no limit * **savetimeout** – how long to wait for a save at most, -1 for no limit |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Parameter saving: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter chunkSize: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter savetimeout: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setSubscriberPatternSaving`(*self*, *\*args*)
    :   Setup parameters for the subscriber pattern with saving set.

        |  |  |
        | --- | --- |
        | Parameters: | * **cacsRole** – name of the cacs role to use * **changeReason** – what change reason to use when saving |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Parameter changeReason: `std` ::`string`
        - Return type: `void`

    `setSubscriberPatternChunkSize`(*self*, *\*args*)
    :   Setup parameters for the subscriber pattern with chunks used.

        |  |  |
        | --- | --- |
        | Parameters: | * **cacsRole** – name of the cacs role to use * **chunkSize** – how many message to save per chunk, -1 for no limit * **savetimeout** – how long to wait for a save at most, -1 for no limit * **changeReason** – what change reason to use when saving |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Parameter chunkSize: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter savetimeout: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter changeReason: `std` ::`string`
        - Return type: `void`

    `setRequestResponsePattern`(*self*, *\*args*)
    :   Setup parameters for the request/response pattern.

        Use the request/response pattern with default settings for test.

        All messages in the inqueue will be handled before returning. No retry will be attempted and any exceptions from the handler or surrounding modules will just be raised up to the calling test.

        This doesn’t affect the pattern-neutral error strategy settings, like global retries (default 3 ) or skipmessage (default true).

        |  |  |
        | --- | --- |
        | Parameters: | * **cacsRole** – name of the cacs role to use * **saving** – if the plan should be saved |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Parameter saving: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `setChangeReason`(*self*, *\*args*)
    :   Set changeReason to use for save.

        This is only relevant if saving has been set to true.

        |  |  |
        | --- | --- |
        | Parameters: | **changeReason** – what change reason to use when saving |

        **Types**
        - Parameter changeReason: `std` ::`string`
        - Return type: `void`

    `setConflictDetectionStrategy`(*self*, *\*args*)
    :   Enable or disable conflict detection during save.

        This is only relevant if saving has been set to true.

        |  |  |
        | --- | --- |
        | Parameters: | **strategy** – which conflict detection strategy to use. |

        **Types**
        - Parameter strategy: `ioserver` ::`base` ::`ConflictDetectionStrategy`
        - Return type: `void`

    `setTriggerPattern`(*self*, *\*args*)
    :   Setup parameters for the trigger pattern.

        Use the trigger pattern with default settings for test.

        |  |  |
        | --- | --- |
        | Parameters: | **cacsRole** – name of the cacs role to use |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Return type: `void`

    `setEventTriggerPattern`(*self*, *\*args*)
    :   Setup parameters for the eventtrigger pattern.

        Use the eventtrigger pattern with default settings for test.

        |  |  |
        | --- | --- |
        | Parameters: | **cacsRole** – name of the cacs role to use |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Return type: `void`

    `setMsgErrorStrategy`(*self*, *\*args*)
    :   Define parameters that steer the error strategy for message related errors.

        |  |  |
        | --- | --- |
        | Parameters: | **skipMsg** – whether to remove a message from the inqueue if it failed, independent from context |

        **Types**
        - Parameter skipMsg: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `setErrorRetryCount`(*self*, *\*args*)
    :   Set value for retry counters.

        Note that TransientErrors are raised to the test even when retry is set, when calling handle again they might be resolved or transform into StaticError/MessageError when the retries are exhausted.

        |  |  |
        | --- | --- |
        | Parameters: | **retry** – how often to retry on transient errors (same for message and system erros) |

        **Types**
        - Parameter retry: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setTimeServicePort`(*self*, *\*args*)
    :   Provide a port for time server communication.

        |  |  |
        | --- | --- |
        | Parameters: | **port** – port for time server |

        **Types**
        - Parameter port: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setPortBase`(*self*, *\*args*)
    :   Provide a base port for sysmond communication.

        |  |  |
        | --- | --- |
        | Parameters: | **port** – base port for sysmmond |

        **Types**
        - Parameter port: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setMemorySource`(*self*)
    :   Setup configuration to use the default memory source queue.

        The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure.

        **Types**
        - Return type: `void`

    `setNamedMemorySink`(*self*, *\*args*)
    :   Setup configuration to use a named memory sink queue.

        The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure.

        |  |  |
        | --- | --- |
        | Parameters: | **sinkName** – the name of the sink |

        **Types**
        - Parameter sinkName: `std` ::`string`
        - Return type: `void`

    `setPersistCid`(*self*, *\*args*)
    :   Set persist\_cid property.

        |  |  |
        | --- | --- |
        | Parameters: | **value** – If persist\_cid should be set to “true” or “false”. |

        **Types**
        - Parameter value: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `setConfigValue`(*self*, *\*args*)
    :   Set custom config value.

        This is an “escape hatch” when all other convenience methods doesn’t provide the needed functionality.

        |  |  |
        | --- | --- |
        | Parameters: | * **path** – the path to the config value (xpathish) * **value** – the value to set |

        **Types**
        - Parameter path: `std` ::`string`
        - Parameter value: `std` ::`string`
        - Return type: `void`

    `setServiceValue`(*self*, *\*args*)
    :   Set custom config value for service.

        This is an “escape hatch” when all other convenience methods doesn’t provide the needed functionality.

        |  |  |
        | --- | --- |
        | Parameters: | * **path** – the path to the config value relative the service root (xpathish) * **value** – the value to set |

        **Types**
        - Parameter path: `std` ::`string`
        - Parameter value: `std` ::`string`
        - Return type: `void`

    `convertToMemoryQueues`(*self*)
    :   Convert configuration to use memory queues.

        Convert all sources and sinks for service to use memory queues. Typically called after importProcessConfig.

        **Types**
        - Return type: `void`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `enableMessageRetention`()
    :   Enable message retention for service.

        This configures the message retention queue and sets the mongodb url in global default

        **Types**
        - Return type: `void`

##### jcms.ioserver.testutils.version10.TestRunner


*class* `jcms.ioserver.testutils.version10.runner_militaris.``TestRunner`(*impl*)
:   Describes an IO-server test runner object that keeps the whole functionality together for unittesting.

    `begin`(*self*, *\*args*)
    :   Start the testsuite by constructing the worker and preparing the plan.

        Use defaults for all optional configuration that hasn’t been provided. This will call the handlers on\_load if it exists.

        |  |  |
        | --- | --- |
        | Parameters: | **cid** – set the cid for which the worker will start work (Default=0 (latest)) |
        | Raises: | * **StaticError** – if some required configuration hasn’t been provided * **exception** – if other errors occur (all errors are just forwarded to the test) |

        **Types**
        - Parameter cid: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `end`(*self*)
    :   clean up all resources, test suite is done. Will unload the plan.

        |  |  |
        | --- | --- |
        | Raises: | **exception** – if other errors occur (all errors are just forwarded to the test) |

        **Types**
        - Return type: `void`

    `reset`(*self*, *\*args*)
    :   Reset internal state (including the plan) to situation after begin() call this between tests within a testsuite.

        Will also clean the memory queue.

        |  |  |
        | --- | --- |
        | Parameters: | **shouldRefresh** – set to true if the controller should perform a refresh as well as the reset (Default = false) |

        **Types**
        - Parameter shouldRefresh: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `process`(*self*, *\*args*)
    :   Process the prepared messages from the configured MessageSource.

        |  |  |
        | --- | --- |
        | Parameters: | **callOnFault** – set to true if the controller should call the service’s “on\_fault” method if the “handler” method throws. Default is false, i.e. the exception from “handler” is propagated up into the test. |

        **Types**
        - Parameter callOnFault: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `refresh`(*self*)
    :   Refresh the the loaded plan to latest cid.

        **Types**
        - Return type: `void`

    `getPlan`(*self*)
    :   Access the loaded plan.

        The PlanHolder object will always exist. It gives access to the loaded plan and ruleset if any.

        |  |  |
        | --- | --- |
        | Returns: | the plan |

        **Types**
        - Return type: `PlanPointer`

    `bookmarkCurrentVersion`(*self*, *\*args*)
    :   Bookmark the current mave version.

        Sets a named bookmark on current mave version to be able to rollback to it with :meth:rollbackToBookmark. If a bookmark with this name already exists the old bookmark will be replaced with the current mave version.

        |  |  |
        | --- | --- |
        | Parameters: | **bookmarkName** – a bookmark name |

        **Types**
        - Parameter bookmarkName: `std` ::`string`
        - Return type: `void`

    `rollbackToBookmark`(*self*, *\*args*)
    :   Rollback to a previous mave version.

        Rollback to a mave version that was previously bookbacked with :meth:bookmarkCurrentVersion. The bookmark is deleted after rollback.

        |  |  |
        | --- | --- |
        | Parameters: | **bookmarkName** – a bookmark name |
        | Raises: | **exception** – if bookmark doesn’t exists or the mave version is already pruned |

        **Types**
        - Parameter bookmarkName: `std` ::`string`
        - Return type: `void`

    `__init__`(*impl*)
    :   constructor

        **Types**
        - Parameter impl: `std` ::`shared_ptr` < `internal` ::`TestRunnerImpl` >

#### TestUtils Python API Reference Version 9

##### jcms.ioserver.testutils.version9.main.TestMain


*class* `jcms.ioserver.testutils.version9.main.``TestMain`(*serviceName*)
:   Describes an IO-server test runner object that keeps the whole functionality together for unittesting.

    @deprecated Use ioserver::testutils::TestMain instead.

    `getConfig`(*self*)
    :   Get the configuration object.

        |  |  |
        | --- | --- |
        | Returns: | a pointer to the global configuration. Use this to setup the ioserver parameters. |

        **Types**
        - Return type: ::`ioserver` ::`testbase` ::`internal` ::`version9` ::[`ITestConfig`](#jcms.ioserver.testutils.version9.main.ITestConfig "jcms.ioserver.testutils.version9.main.ITestConfig") ::`Pointer`

    `getMemoryQueue`(*self*)
    :   Get the memory global queue.

        If the config was set to use memory queue then the handler will use this queue.

        |  |  |
        | --- | --- |
        | Returns: | a pointer to the global memory queue. |

        **Types**
        - Return type: ::`ioserver` ::`testbase` ::`internal` ::`version9` ::[`IMemoryQueue`](#jcms.ioserver.testutils.version9.main.IMemoryQueue "jcms.ioserver.testutils.version9.main.IMemoryQueue") ::`Pointer`

    `getMemoryHAStore`(*self*)
    :   Get the memory HA store object.

        |  |  |
        | --- | --- |
        | Returns: | a pointer to the memory HA store object. |

        **Types**
        - Return type: ::`ioserver` ::`testbase` ::`internal` ::`version9` ::[`IMemoryHAStore`](#jcms.ioserver.testutils.version9.main.IMemoryHAStore "jcms.ioserver.testutils.version9.main.IMemoryHAStore") ::`Pointer`

    `getRunner`(*self*)
    :   Get the runner object.

        After setting up the configuration the runner is initialized on first access.
        The runner is the test engine of the IOServer, it will load the plan and
        execute the service under test.

        Once the runner has been obtained, the configuration will be locked,
        all attempts to set more configuration values will result in an exception.

        |  |  |
        | --- | --- |
        | Returns: | a pointer to the runner object. |

    `__init__`(*serviceName*)
    :   constructor

        **Types**
        - Parameter serviceName: `std` ::`string`

##### jcms.ioserver.testutils.version9.main.IMemoryHAStore


*class* `jcms.ioserver.testutils.version9.main.``IMemoryHAStore`(*\*args*, *\*\*kwargs*)
:   This interface provides access to a memory based HA store for testing purposes.

    The most commonly used HA store key is “generation”. It is used to specify the latest handled commit id.

    @deprecated Use ioserver::testbase::IMemoryHAStore instead.

    `hasValue`(*self*)
    :   Check if there is a value in the HA key-value store for the given key.

        |  |  |
        | --- | --- |
        | Parameters: | **key** – The key to check for. |

        **Types**
        - Parameter key: `std` ::`string`
        - Return type: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")

    `getValue`(*self*)
    :   Get a value from the HA key-value store.

        |  |  |
        | --- | --- |
        | Parameters: | **key** – The key for which to retrieve a value. |
        | Returns: | The value associated with the given key. |
        | Raises: | **ioserver.base.StaticError** – if there is no value for key. |

        **Types**
        - Parameter key: `std` ::`string`
        - Return type: `std` ::`string`

    `setValue`(*self*)
    :   Set a key-value pair in the HA key-value store.

        |  |  |
        | --- | --- |
        | Parameters: | * **key** – The key to write. * **value** – The value associated with key. |

        **Types**
        - Parameter key: `std` ::`string`
        - Parameter value: `std` ::`string`
        - Return type: `void`

    `clear`(*self*)
    :   Clear all internal state.

        **Types**
        - Return type: `void`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

##### jcms.ioserver.testutils.version9.main.IMemoryQueue


*class* `jcms.ioserver.testutils.version9.main.``IMemoryQueue`(*\*args*, *\*\*kwargs*)
:   This interface provides access to the built in memory queue for testing purposes.

    @deprecated Use ioserver::testbase::IMemoryQueue instead.

    `reset`(*self*)
    :   Reset content of input and output message lists.

        **Types**
        - Return type: `void`

    `getDefaultInputContentType`(*self*)
    :   Get the default content type to use for new input messages.

        |  |  |
        | --- | --- |
        | Returns: | the default content type |

        **Types**
        - Return type: `std` ::`string`

    `setDefaultInputContentType`(*self*, *\*args*)
    :   Set the default content type to use for new input messages.

        |  |  |
        | --- | --- |
        | Parameters: | **content\_type** – the content type |

        **Types**
        - Parameter content\_type: `std` ::`string`
        - Return type: `void`

    `getDefaultInputEncoding`(*self*)
    :   Get the default encoding to use for new input messages.

        |  |  |
        | --- | --- |
        | Returns: | the default encoding |

        **Types**
        - Return type: `std` ::`string`

    `setDefaultInputEncoding`(*self*, *\*args*)
    :   Set the default encoding to use for new input messages.

        |  |  |
        | --- | --- |
        | Parameters: | **encoding** – the encoding |

        **Types**
        - Parameter encoding: `std` ::`string`
        - Return type: `void`

    `setStartId`(*self*, *\*args*)
    :   Provide a start value for generating the msgIds, default is 0.

        |  |  |
        | --- | --- |
        | Parameters: | **index** – start value for generating msgIds |

        **Types**
        - Parameter index: `size_t`
        - Return type: `void`

    `getStartId`(*self*)
    :   **Types**
        - Return type: `size_t`

    `addInputIOMessage`(*self*, *\*args*)
    :   Add an IOMessage to the input queue.

        |  |  |
        | --- | --- |
        | Parameters: | **msg** – the input message |
        | Returns: | index of message in the queue |

        **Types**
        - Parameter msg: `IOMessagePointer`
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `setInputIOMessages`(*self*, *\*args*)
    :   Replace current input queue content with a new message list.

        |  |  |
        | --- | --- |
        | Parameters: | **msgVec** – list of messages to be put on the queue |

        **Types**
        - Parameter msgVec: `IOMessageList`
        - Return type: `void`

    `getInputSize`(*self*)
    :   Get the size of input message queue.

        |  |  |
        | --- | --- |
        | Returns: | size of the input message list |

        **Types**
        - Return type: `size_t`

    `getInputIOMessages`(*self*)
    :   Get the current input queue content.

        |  |  |
        | --- | --- |
        | Returns: | list of the messages on the input queue |

        **Types**
        - Return type: `IOMessageList`

    `getInputIOMessage`(*self*, *\*args*)
    :   Get the input message at given index.

        |  |  |
        | --- | --- |
        | Parameters: | **index** – the message index to get |
        | Returns: | message at index |

        **Types**
        - Parameter index: `size_t`
        - Return type: `IOMessagePointer`

    `getOutputSize`(*self*)
    :   Get size of output message queue of default sink.

        |  |  |
        | --- | --- |
        | Returns: | size of the output message list |

        **Types**
        - Return type: `size_t`

    `getOutputIOMessages`(*self*)
    :   Get the current output queue content of default sink.

        |  |  |
        | --- | --- |
        | Returns: | list of the messages on the output queue |

        **Types**
        - Return type: `IOMessageList`

    `getOutputIOMessage`(*self*, *\*args*)
    :   Get the output message at given index of default sink.

        |  |  |
        | --- | --- |
        | Parameters: | **index** – the message index to get |
        | Returns: | message at index |

        **Types**
        - Parameter index: `size_t`
        - Return type: `IOMessagePointer`

    `getOutputSizeByName`(*self*, *\*args*)
    :   Get size of output message queue.

        |  |  |
        | --- | --- |
        | Parameters: | **sinkName** – name of the sink |
        | Returns: | size of the output message list |

        **Types**
        - Parameter sinkName: `std` ::`string`
        - Return type: `size_t`

    `getOutputIOMessagesByName`(*self*, *\*args*)
    :   Get the current output queue content.

        |  |  |
        | --- | --- |
        | Parameters: | **sinkName** – name of the sink |
        | Returns: | list of the messages on the output queue |

        **Types**
        - Parameter sinkName: `std` ::`string`
        - Return type: `IOMessageList`

    `getOutputIOMessageByName`(*self*, *\*args*)
    :   Get the output message at given index.

        |  |  |
        | --- | --- |
        | Parameters: | * **sinkName** – name of the sink * **index** – the message index to get |
        | Returns: | message at index |

        **Types**
        - Parameter sinkName: `std` ::`string`
        - Parameter index: `size_t`
        - Return type: `IOMessagePointer`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

##### jcms.ioserver.testutils.version9.main.ITestConfig


*class* `jcms.ioserver.testutils.version9.main.``ITestConfig`(*\*args*, *\*\*kwargs*)
:   Provides configuration for an IOServer mock-instance

    The interface allows steering the mock implementation, chose which real components should be used and which others to replace by mock-objects (e.g memory queue instead of qpid)

    @deprecated Use ioserver::testbase::ITestConfig instead.

    `debugPrint`(*self*)
    :   Print the configuration content.

        **Types**
        - Parameter s: `std` ::`ostream`
        - Return type: `void`

    `importProcessConfig`(*self*, *\*args*)
    :   Import from system configuration.

        Imports the settings for the tests serviceName from the configuration for the given IOServer process.

        |  |  |
        | --- | --- |
        | Parameters: | * **process** – the name of the IOServer process to copy from * **cfgFile** – the name of the config root file if not standard. |

        **Types**
        - Parameter process: `std` ::`string`
        - Parameter cfgFile: `std` ::`string`
        - Return type: `void`

    `getProcessName`(*self*)
    :   Get the common config process name.

        |  |  |
        | --- | --- |
        | Returns: | process name |

        **Types**
        - Return type: `std` ::`string`

    `getServiceNames`(*self*)
    :   Get the list of all service names.

        |  |  |
        | --- | --- |
        | Returns: | list containing all service names |

        **Types**
        - Return type: `StringVectorPointer`

    `getProcessServicePort`(*self*, *\*args*)
    :   Get the service port to use for the process when communicating with sysmond.

        |  |  |
        | --- | --- |
        | Parameters: | * **systemService** – the system service to look up * **hostName** – the host name to look up (default: use the current host name) * **processName** – the process name (default: use the current process name) |
        | Returns: | port number |

        **Types**
        - Parameter systemService: `std` ::`string`
        - Parameter hostName: `std` ::`string`
        - Parameter processName: `std` ::`string`
        - Return type: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")

    `setTestBinding`(*self*, *\*args*)
    :   Use a test-provided bridge.

        |  |  |
        | --- | --- |
        | Parameters: | * **isHandler** – whether this is a handler or trigger * **bridgeName** – name of the test bridge * **handlerName** – name of the handler or trigger |

        **Types**
        - Parameter isHandler: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter bridgeName: `std` ::`string`
        - Parameter handlerName: `std` ::`string`
        - Return type: `void`

    `setPythonBinding`(*self*, *\*args*)
    :   Use a python bridge.

        |  |  |
        | --- | --- |
        | Parameters: | * **isHandler** – whether this is a handler or trigger * **protocol** – the name of the message protocol (plain or soap) * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter isHandler: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter protocol: `std` ::`string`
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `setPythonHandlerPlainBinding`(*self*, *\*args*)
    :   Use python bridge with plain handler.

        |  |  |
        | --- | --- |
        | Parameters: | * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `setPythonHandlerSoapBinding`(*self*, *\*args*)
    :   Use python bridge with a soap xml handler.

        |  |  |
        | --- | --- |
        | Parameters: | * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `setPythonTriggerPlainBinding`(*self*, *\*args*)
    :   Use python bridge with a plain trigger.

        |  |  |
        | --- | --- |
        | Parameters: | * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `setPythonTriggerSoapBinding`(*self*, *\*args*)
    :   Use python bridge with a soap xml trigger.

        |  |  |
        | --- | --- |
        | Parameters: | * **moduleName** – the python module that implements the service * **handleMethod** – the main handle method to call if this is a handler * **databindingName** – the databinding module to use |

        **Types**
        - Parameter moduleName: `std` ::`string`
        - Parameter handleMethod: `std` ::`string`
        - Parameter databindingName: `std` ::`string`
        - Return type: `void`

    `skipPlan`(*self*)
    :   Prepare a plan and ruleset configuration that will not load any ARA plan or ruleset.

        |  |  |
        | --- | --- |
        | Raises: | **StaticError** – if a plan has already been chosen |

        **Types**
        - Return type: `void`

    `setDatabase`(*self*, *\*args*)
    :   Prepare the database connection configuration.

        Prepare database connection configuration with explicit schema setup.

        |  |  |
        | --- | --- |
        | Parameters: | * **connectString** – the Dave connectstring to use * **dbschema** – the schema name (default = “”) |

        **Types**
        - Parameter connectString: `std` ::`string`
        - Parameter dbschema: `std` ::`string`
        - Return type: `void`

    `setDomainGeneration`(*self*, *\*args*)
    :   Override the domain generation for the plan.

        |  |  |
        | --- | --- |
        | Parameters: | * **domain** – the domain generation string “air1” or “air2” * **planBuilder** – name of a custom plan builder type, this requires a special driver lib that registers a driver with this name. Typical value is “mave2”. |

        **Types**
        - Parameter domain: `std` ::`string`
        - Parameter planBuilder: `std` ::`string`
        - Return type: `void`

    `getDomainGeneration`(*self*)
    :   Retrieve the domain generation setting.

        |  |  |
        | --- | --- |
        | Returns: | the domain generation setting (“air1” or “air2”) |

        **Types**
        - Return type: `std` ::`string`

    `getPlanBuilderName`(*self*)
    :   Retrieve the plan builder setting.

        |  |  |
        | --- | --- |
        | Returns: | the name of the plan builder types, typical “mave2” |

        **Types**
        - Return type: `std` ::`string`

    `setRulesetType`(*self*, *\*args*)
    :   Set the ruleset type that will be used.

        Only valid when using mave2 based plans.

        |  |  |
        | --- | --- |
        | Parameters: | **rulesetType** – name of ruleset type to use. Requires that a driver lib has registered a driver with support for this ruleset. Typical value is “rave” (for rave::Ruleset type). |

        **Types**
        - Parameter rulesetType: `std` ::`string`
        - Return type: `void`

    `getRulesetType`(*self*)
    :   Get the ruleset type used.

        Only valid for mave2 plans.

        |  |  |
        | --- | --- |
        | Returns: | Name of ruleset type to use (“rave”). Default is an empty string. |

        **Types**
        - Return type: `std` ::`string`

    `setPlan`(*self*, *\*args*)
    :   Prepare the plan configuration.

        Use this to specify a datacontext but no ruleset.

        |  |  |
        | --- | --- |
        | Parameters: | * **datacontext** – the name of the datacontext to load * **snapshotpath** – path to snapshot location for this datacontext this will be given to the plan factory if provided. |

        **Types**
        - Parameter datacontext: `std` ::`string`
        - Parameter snapshotpath: `std` ::`string`
        - Return type: `void`

    `setRuleset`(*self*, *\*args*)
    :   Prepare the ruleset configuration.

        |  |  |
        | --- | --- |
        | Parameters: | * **ruleset** – the name of the global ruleset to load * **parameterset** – the name of the parameter set to load, if empty no parameters are set |

        **Types**
        - Parameter ruleset: `std` ::`string`
        - Parameter parameterset: `std` ::`string`
        - Return type: `void`

    `setNow`(*self*, *\*args*)
    :   Provide an override for now.

        This will influence the datacontext selections as well as rave.

        |  |  |
        | --- | --- |
        | Parameters: | **nowString** – a valid Rave datetime expression as in basics::time::minutes\_from\_expr() |

        **Types**
        - Parameter nowString: `std` ::`string`
        - Return type: `void`

    `setMemoryQueue`(*self*)
    :   Setup configuration to use the builtin memory queue.

        The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure. This is a convenience menthod that will set up a defult source queue and a defualt sink queue.

        To set up named sinks, use :meth:setNamedMemorySink and :meth:setMemorySource

        **Types**
        - Return type: `void`

    `setQpid`(*self*, *\*args*)
    :   Setup parameters for qpid.

        Use this to run tests against real ActiveMQ queues.

        |  |  |
        | --- | --- |
        | Parameters: | * **host** – the host to connect to ActiveMQ * **port** – the port on host * **queueName** – the queue name to work on * **prefetchCapacity** – the prefetch capacity of qpid receiver * **compress** – the switch for compressing the content of the message * **maxContentSize** – the maximum content size of the message compressed or not. |

        **Types**
        - Parameter host: `std` ::`string`
        - Parameter port: `std` ::`string`
        - Parameter queueName: `std` ::`string`
        - Parameter prefetchCapacity: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter compress: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter maxContentSize: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setQpidMessageSource`(*self*, *\*args*)
    :   Setup parameters for qpid message source.

        Use this to run tests against real ActiveMQ queues.

        |  |  |
        | --- | --- |
        | Parameters: | * **brokerHost** – ActiveMQ broker host address * **brokerPort** – ActiveMQ broker host port * **queueName** – queue name to use * **prefetchCapacity** – number of messages to prefetch in the background |

        **Types**
        - Parameter brokerHost: `std` ::`string`
        - Parameter brokerPort: `std` ::`string`
        - Parameter queueName: `std` ::`string`
        - Parameter prefetchCapacity: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setQpidMessageSink`(*self*, *\*args*)
    :   Setup parameters for qpid message sink.

        Use this to run tests with real ActiveMQ queues.

        |  |  |
        | --- | --- |
        | Parameters: | * **brokerHost** – ActiveMQ broker host address * **brokerPort** – ActiveMQ broker host port * **queueName** – queue name to use * **sinkName** – name of this sink. Default sets default sink * **senderCapacity** – Number of messages to buffer up when using asynchronous send(). Default 0 (synchronous send) * **compress** – set to true if the message should be gzipped. Default false * **maxContentSize** – Maximum content size. Default 0 |

        **Types**
        - Parameter brokerHost: `std` ::`string`
        - Parameter brokerPort: `std` ::`string`
        - Parameter queueName: `std` ::`string`
        - Parameter sinkName: `std` ::`string`
        - Parameter senderCapacity: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter compress: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter maxContentSize: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setSubscriberPattern`(*self*, *\*args*)
    :   Setup parameters for the subscriber pattern.

        Use the subscriber pattern with default settings for test.

        All messages in the inqueue will be handled before returning. No retry will be attempted and any exceptions from the handler or surrounding modules will just be raised up to the calling test.

        This doesn’t affect the pattern-neutral error strategy settings, like global retries (default 3 ) or skipmessage (default true).

        |  |  |
        | --- | --- |
        | Parameters: | * **cacsRole** – name of the cacs role to use * **saving** – whether the plan should be saved after handling the messages, default false. * **chunkSize** – how many message to save per chunk, -1 for no limit * **savetimeout** – how long to wait for a save at most, -1 for no limit |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Parameter saving: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Parameter chunkSize: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter savetimeout: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setSubscriberPatternSaving`(*self*, *\*args*)
    :   Setup parameters for the subscriber pattern with saving set.

        |  |  |
        | --- | --- |
        | Parameters: | * **cacsRole** – name of the cacs role to use * **changeReason** – what change reason to use when saving |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Parameter changeReason: `std` ::`string`
        - Return type: `void`

    `setSubscriberPatternChunkSize`(*self*, *\*args*)
    :   Setup parameters for the subscriber pattern with chunks used.

        |  |  |
        | --- | --- |
        | Parameters: | * **cacsRole** – name of the cacs role to use * **chunkSize** – how many message to save per chunk, -1 for no limit * **savetimeout** – how long to wait for a save at most, -1 for no limit * **changeReason** – what change reason to use when saving |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Parameter chunkSize: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter savetimeout: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Parameter changeReason: `std` ::`string`
        - Return type: `void`

    `setRequestResponsePattern`(*self*, *\*args*)
    :   Setup parameters for the request/response pattern.

        Use the request/response pattern with default settings for test.

        All messages in the inqueue will be handled before returning. No retry will be attempted and any exceptions from the handler or surrounding modules will just be raised up to the calling test.

        This doesn’t affect the pattern-neutral error strategy settings, like global retries (default 3 ) or skipmessage (default true).

        |  |  |
        | --- | --- |
        | Parameters: | * **cacsRole** – name of the cacs role to use * **saving** – if the plan should be saved |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Parameter saving: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `setChangeReason`(*self*, *\*args*)
    :   Set changeReason to use for save.

        This is only relevant if saving has been set to true.

        |  |  |
        | --- | --- |
        | Parameters: | **changeReason** – what change reason to use when saving |

        **Types**
        - Parameter changeReason: `std` ::`string`
        - Return type: `void`

    `setConflictDetectionStrategy`(*self*, *\*args*)
    :   Enable or disable conflict detection during save.

        This is only relevant if saving has been set to true.

        |  |  |
        | --- | --- |
        | Parameters: | **strategy** – which conflict detection strategy to use. |

        **Types**
        - Parameter strategy: `ioserver` ::`base` ::`ConflictDetectionStrategy`
        - Return type: `void`

    `setTriggerPattern`(*self*, *\*args*)
    :   Setup parameters for the trigger pattern.

        Use the trigger pattern with default settings for test.

        |  |  |
        | --- | --- |
        | Parameters: | **cacsRole** – name of the cacs role to use |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Return type: `void`

    `setEventTriggerPattern`(*self*, *\*args*)
    :   Setup parameters for the eventtrigger pattern.

        Use the eventtrigger pattern with default settings for test.

        |  |  |
        | --- | --- |
        | Parameters: | **cacsRole** – name of the cacs role to use |

        **Types**
        - Parameter cacsRole: `std` ::`string`
        - Return type: `void`

    `setMsgErrorStrategy`(*self*, *\*args*)
    :   Define parameters that steer the error strategy for message related errors.

        |  |  |
        | --- | --- |
        | Parameters: | **skipMsg** – whether to remove a message from the inqueue if it failed, independent from context |

        **Types**
        - Parameter skipMsg: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `setErrorRetryCount`(*self*, *\*args*)
    :   Set value for retry counters.

        Note that TransientErrors are raised to the test even when retry is set, when calling handle again they might be resolved or transform into StaticError/MessageError when the retries are exhausted.

        |  |  |
        | --- | --- |
        | Parameters: | **retry** – how often to retry on transient errors (same for message and system erros) |

        **Types**
        - Parameter retry: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setTimeServicePort`(*self*, *\*args*)
    :   Provide a port for time server communication.

        |  |  |
        | --- | --- |
        | Parameters: | **port** – port for time server |

        **Types**
        - Parameter port: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setPortBase`(*self*, *\*args*)
    :   Provide a base port for sysmond communication.

        |  |  |
        | --- | --- |
        | Parameters: | **port** – base port for sysmmond |

        **Types**
        - Parameter port: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `setMemorySource`(*self*)
    :   Setup configuration to use the default memory source queue.

        The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure.

        **Types**
        - Return type: `void`

    `setNamedMemorySink`(*self*, *\*args*)
    :   Setup configuration to use a named memory sink queue.

        The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure.

        |  |  |
        | --- | --- |
        | Parameters: | **sinkName** – the name of the sink |

        **Types**
        - Parameter sinkName: `std` ::`string`
        - Return type: `void`

    `setPersistCid`(*self*, *\*args*)
    :   Set persist\_cid property.

        |  |  |
        | --- | --- |
        | Parameters: | **value** – If persist\_cid should be set to “true” or “false”. |

        **Types**
        - Parameter value: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `setConfigValue`(*self*, *\*args*)
    :   Set custom config value.

        This is an “escape hatch” when all other convenience methods doesn’t provide the needed functionality.

        |  |  |
        | --- | --- |
        | Parameters: | * **path** – the path to the config value (xpathish) * **value** – the value to set |

        **Types**
        - Parameter path: `std` ::`string`
        - Parameter value: `std` ::`string`
        - Return type: `void`

    `setServiceValue`(*self*, *\*args*)
    :   Set custom config value for service.

        This is an “escape hatch” when all other convenience methods doesn’t provide the needed functionality.

        |  |  |
        | --- | --- |
        | Parameters: | * **path** – the path to the config value relative the service root (xpathish) * **value** – the value to set |

        **Types**
        - Parameter path: `std` ::`string`
        - Parameter value: `std` ::`string`
        - Return type: `void`

    `convertToMemoryQueues`(*self*)
    :   Convert configuration to use memory queues.

        Convert all sources and sinks for service to use memory queues. Typically called after importProcessConfig.

        **Types**
        - Return type: `void`

    `__init__`(*\*args*, *\*\*kwargs*)
    :   Initialize self. See help(type(self)) for accurate signature.

##### jcms.ioserver.testutils.version9.TestRunner


*class* `jcms.ioserver.testutils.version9.runner_militaris.``TestRunner`(*\*args*)
:   Describes an IO-server test runner object that keeps the whole functionality together for unittesting.

    @deprecated Use ioserver::testutils::TestRunner instead.

    `begin`(*self*, *\*args*)
    :   Start the testsuite by constructing the worker and preparing the plan.

        Use defaults for all optional configuration that hasn’t been provided. This will call the handlers on\_load if it exists.

        |  |  |
        | --- | --- |
        | Parameters: | **cid** – set the cid for which the worker will start work (Default=0 (latest)) |
        | Raises: | * **StaticError** – if some required configuration hasn’t been provided * **exception** – if other errors occur (all errors are just forwarded to the test) |

        **Types**
        - Parameter cid: [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.12)")
        - Return type: `void`

    `end`(*self*)
    :   clean up all resources, test suite is done. Will unload the plan.

        |  |  |
        | --- | --- |
        | Raises: | **exception** – if other errors occur (all errors are just forwarded to the test) |

        **Types**
        - Return type: `void`

    `reset`(*self*, *\*args*)
    :   Reset internal state (including the plan) to situation after begin() call this between tests within a testsuite.

        Will also clean the memory queue.

        |  |  |
        | --- | --- |
        | Parameters: | **shouldRefresh** – set to true if the controller should perform a refresh as well as the reset (Default = false) |

        **Types**
        - Parameter shouldRefresh: [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")
        - Return type: `void`

    `process`(*self*)
    :   Process the prepared messages from the configured MessageSource.

        **Types**
        - Return type: `void`

    `refresh`(*self*)
    :   Refresh the the loaded plan to latest cid.

        **Types**
        - Return type: `void`

    `getPlan`(*self*)
    :   Access the loaded plan.

        The PlanHolder object will always exist. It gives access to the loaded plan and ruleset if any.

        |  |  |
        | --- | --- |
        | Returns: | the plan |

        **Types**
        - Return type: `PlanPointer`

    `bookmarkCurrentVersion`(*self*, *\*args*)
    :   Bookmark the current mave version.

        Sets a named bookmark on current mave version to be able to rollback to it with :meth:rollbackToBookmark. If a bookmark with this name already exists the old bookmark will be replaced with the current mave version.

        |  |  |
        | --- | --- |
        | Parameters: | **bookmarkName** – a bookmark name |

        **Types**
        - Parameter bookmarkName: `std` ::`string`
        - Return type: `void`

    `rollbackToBookmark`(*self*, *\*args*)
    :   Rollback to a previous mave version.

        Rollback to a mave version that was previously bookbacked with :meth:bookmarkCurrentVersion. The bookmark is deleted after rollback.

        |  |  |
        | --- | --- |
        | Parameters: | **bookmarkName** – a bookmark name |
        | Raises: | **exception** – if bookmark doesn’t exists or the mave version is already pruned |

        **Types**
        - Parameter bookmarkName: `std` ::`string`
        - Return type: `void`

    `__init__`(*\*args*)
    :   constructor

        **Types**
        - Parameter impl: `std` ::`shared_ptr` < `internal` ::`TestRunnerImpl` >

### IOServer logs


##### 18.1. Configuring logging

The recommended way to set up logging from the IOServer is to use jcmslog’s `TcpAppender`, and log to a rsyslogd server.

Using a jcmslog `FileAppender` is possible, but log file rotation is not supported. This is due to the fact that the
IOServer consists of several processes, that all log to the same file; if one of them rotated the log, the others would
not notice, and would therefore be unable to continue logging.

##### 18.2. Flow

A flow is an identifier that is written as prefix in the lines of the log.
Each integration service has its own separate flow name,
which makes it possible to find all log lines for a particular service.
How much and which information that is included in the log is set by the log level of that flow.

##### 18.3. Logging from an IOService

The service context provides a logger, `version10.context.ServiceContext.service_logger()`, to log from within a service.
This logger can be used as an ordinary logger from the standard Python logging module.

```
def handle(planholder, service_context):
    logger = service_context.service_logger
    logger.debug(u"Debug message")
    logger.warning(u"Warning message")
```

This prints the messages in the IOServer log file on the flow:

```
ioserver.<service_name>.service
```

where `<service_name>` is the configured name of the service.

Note

Print statements are not visible when running an IOService in the IOServer.

##### 18.4. Getting the correct log level for an integration service

The name of the logging flow for an integration service is based on the name of the service in the configuration,
or more precisely the name attribute of the `ioservice` element found in the file:

`.../usr/etc/programs/ioservice/\*.xml`

**Example:**

```
<ioservice name="flight_schedule">
  <pattern>
    <class>subscriber</class>
    <cacs_role>Administrator</cacs_role>
    <changereason>Other</changereason>
  </pattern>
<binding>
```

The flow name follows the pattern in the example below:

**Example:**

`ioserver.flight_schedule.service`

To enable a specific log level on a flow, add or modify a `flow` element in the file:

`.../usr/etc/programs/ioserver.xml`

For the flow element, set the `name` attribute to the flow name and the `level` attribute to the desired log level.
Then restart the service.
The following example sets the log level to `debug` for the `flight_schedule` service:

**Example:**

```
<jcmslog>
  <flow name="ioserver.flight_schedule.handler" level="DEBUG"/>
</jcmslog>
```

For a general description with more details of logging, see the Jcmslog documentation.

###### 18.4.1. Log level contents

| Level | Description |
| --- | --- |
| `DEBUG` | Flow information on a detailed level (`<15>`).  Examples:   * Info about choices that depend on data in the database,   for example if a leg in a trip was found or created. * Info about modified data in the database. * Info about the data in the database that is processed. * Which internal parts of the source code is being run. |
| `INFO` | Flow information on a high level (`<14>`).  Examples:   * Start and end of processing a message. * Which crew is processed, for multi-crew messages. * Which part of a complex message that is processed. |
| `WARNING` | Info about potential problems, which is not severe or is automatically recovered, that is fall backs (`<12>`).  Examples:   * Overwrites an already existing CSDL file. * Could not write an optional attribute on a database object. |
| `ERROR` | Information of occurred errors (`<11>`).  Examples:   * Internal errors, like failing components or connections. * Errors in input data. * Failed conditions on database data. * Missing catalog data, for example base or aircraft type. * Failed business checks. |

Note that a higher log level in the table also contains all the lower levels,
and that `INFO` is the default.

##### 18.5. Connecting log entries to messages

The message id (`msgId`) and current commit id (`cid`) are included in all IOServer log lines where
applicable. This can be used to track a certain interesting message in logs of other system,
or finding the actual message content.

##### 18.6. Log format

The log messages follow the *syslog* format (RFC 5424).

```
<14>1 2016-10-26T18:38:41.386Z hostname process_name 9469 OPER [details@38555 cid="44" msgId="apa-bepa-cepa" service="ReserveCoverageHandler" flow="ioserver.Something"] Doing good stuff.
^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^ ^^^^^^^^^^^^ ^^^^                     ^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^
|     |                        |        |            |                        |        |                     |                                |
|     Date                     |        Process name Pid                      |        Message id            IOServer service name            Log flow name
Log level                      Host name                                      Current plan generation
```

#### Configuring logging

#### Flow

#### Logging from an IOService

#### Getting the correct log level for an integration service

##### Log level contents

#### Connecting log entries to messages

#### Log format

### IOServer TestUtils


The IOServer TestUtils package available in the `ioserver.sdk` component provides a convenient way
to create component tests for IOServer plugins like handlers and triggers. It allows the developer to run the plugin
in much the same way as it would run in a real IOServer, but without a forking main process.
Any exception that is raised during the execution of the handler will first be handled internally but then
raised further to the test to allow checking for error conditions without relying on side-effects.

The TestUtils API has historically been versioned in a different cycle than the IOServer API itself.
Beginning with version 9 they will use the same numbering.
The current version is version 10, available in [`jcms.ioserver.testutils.version10.main`](python_testutils_api_ver10_reference.html#module-jcms.ioserver.testutils.version10.main "jcms.ioserver.testutils.version10.main").

Each major of TestUtils is tightly connected to one major
of the IOServer API itself by the fact that the PlanHolder that can be obtained from the TestRunner
is of a certain version.
This is only applicable for the API exposed to the test itself. It is possible to test plugins of any supported
version with TestUtils of any supported version.

##### 19.1. How to use TestUtils

To use TestUtils for testing, a test class is needed based on `unittest2.TestCase`.
In the `setUpClass` method we instantiate the TestUtils [`TestMain`](python_testutils_api_ver10_reference.html#jcms.ioserver.testutils.version10.main.TestMain "jcms.ioserver.testutils.version10.main.TestMain") class.
To access the configuration we use [`getConfig()`](python_testutils_api_ver10_reference.html#jcms.ioserver.testutils.version10.main.TestMain.getConfig "jcms.ioserver.testutils.version10.main.TestMain.getConfig") which returns
an [`ITestConfig`](python_testutils_api_ver10_reference.html#jcms.ioserver.testutils.version10.main.ITestConfig "jcms.ioserver.testutils.version10.main.ITestConfig").
The configuration is then set with necessary values for the tests such as database,
handler binding, pattern and queue.

When configuration is ready a `TestRunner`
is received from the function [`getRunner()`](python_testutils_api_ver10_reference.html#jcms.ioserver.testutils.version10.main.TestMain.getRunner "jcms.ioserver.testutils.version10.main.TestMain.getRunner"). The runner can
then be started by calling `begin()`.

Example of setup class and configuration settings:

```
from jcms.ioserver.testutils.version10 import main
from jcms.ioserver.version10.message import PlainIOMessage


class TestMain(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestMain, cls).setUpClass()
        cls._main = main.TestMain("TestMockInterface")
        # initialize configuration
        cfg = cls._main.getConfig()
        cfg.setDatabase("profile:default")
        cfg.skipPlan()
        cfg.setPythonHandlerPlainBinding("helloWorldService","")
        cfg.setSubscriberPattern("myRole", False)
        cfg.setMemoryQueue()
        cfg.setDomainGeneration("air2", "mave2")
        # obtain runner and start
        cls._runner = cls._main.getRunner()
        cls._runner.begin()
```

For each test `setUp()` method should be called on the parent class `unittest2.TestCase`.
Example of setup:

```
def setUp(self):
    super(TestMain, self).setUp()
```

To be able to run a simple test, a message must be put on the input queue.
TestUtils provides a simple memory queue [`IMemoryQueue`](python_testutils_api_ver10_reference.html#jcms.ioserver.testutils.version10.main.IMemoryQueue "jcms.ioserver.testutils.version10.main.IMemoryQueue") that can be used for testing purposes.

When the message is on the queue, the runner can `process()` the message.
Example of a test case:

```
def testMsgOk(self):
    io_msg = PlainIOMessage.create_io_message("Hello world")
    queue = self._main.getMemoryQueue()
    queue.addInputIOMessage(io_msg)
    self._runner.process()
    self.assertEqual(1, queue.getOutputSize())
    self.assertEqual(0, queue.getInputSize())
    msg = queue.getOutputIOMessage(0)
    self.assertEqual("Hello World", msg.getContent())
```

For every test the function `reset()` should be called on the runner.
This will empty the queue and refresh the plan if needed.
Example of tear down:

```
def tearDown(self):
    self._runner.reset(False)
    super(TestMain, self).tearDown()
```

Finally the resources should be cleaned up with the `end()` method
which unloads the plan.
Tear down class:

```
@classmethod
def tearDownClass(cls):
    cls._runner.end()
    super(TestMain, cls).tearDownClass()
```

###### 19.1.1. How to setup initial data to reuse between tests

One use case for testutils is that there exist a schema that should not be altered (skipsave should be used).
This shema contains most of the data needed for the test suite, but a small adjustment is needed.

This can be made by setting a bookmark called *initalLoad* after the modification.
The *initialLoad* bookmark is used as reset point by `reset()`
when *skipsave* is configured.

```
@classmethod
def setUpClass(cls):
    super(TestMain, cls).setUpClass()
    cls._main = main.TestMain("TestMockInterface")
    # initialize configuration
    cfg = cls._main.getConfig()
    cfg.setDatabase("profile:default")
    cfg.setPythonHandlerPlainBinding("helloWorldService","")
    cfg.setSubscriberPattern("myRole", False)
    cfg.setMemoryQueue()
    cfg.setDomainGeneration("air2", "mave2")
    # obtain runner and start
    cls._runner = cls._main.getRunner()
    cls._runner.begin()

    planHolder = cls._runner.getPlan()
    araPlan = planHolder.getMave2Plan()
    # Do the relevant changes on the araPlan
    cls._runner.bookmarkCurrentVersion('initialLoad')
```

###### 19.1.2. Logging with testutils

To enable logging with testrunner the easiest way may be to use jcmslogs python api.

```
import jcms.log
jcms.log.config.set_log_level('ioserver', logging.DEBUG)
```

#### How to use TestUtils

##### How to setup initial data to reuse between tests

##### Logging with testutils

### Configuration only relevant for testing


Some configuration elements are only (or mainly) relevant for testing
handlers or the IOServer itself. They are documented in this section
for completeness.

##### 20.1. datamodel

The [datamodel](configuration.html#conf-datamodel) element has a few settings that are only or mainly
relevant for test.

| Element | Type | Description |
| --- | --- | --- |
| skipplan | boolean | Whether plan handling shall be skipped. |
| skipsave | boolean | Whether to skip saving the plan. |

##### 20.2. pattern

Test-specific settings for [pattern](configuration.html#conf-pattern).

| Element | Type | Description |
| --- | --- | --- |
| skipsave | boolean | Whether to skip saving the plan. Deprecated, use <datamodel><skipsave> |

##### 20.3. simulated time

It is possible to use simulated time for testing, debugging, or simulations without changing the
system time of the server.

Warning

Simulated time must not be used in production.

Simulated time allows IOServer to behave as if the current time was different, or as if
time progressed in another pace.

For instance, it is possible to run regression tests with a fixed data set. Even if
a report is generated for the *current* month, the result is always the same.
Another example is to reproduce a defect that occurrs only at midnight etc.

Simulated time is enabled by setting a fixed time in the configuration, or by using an external
time server. In both cases, the data context used when loading a plan and the Rave `now` keyword
are changed according to the simulated time.

A fixed time means that “time stands still” during the lifetime of IOServer.

Using a time server allows both to set a time offset and make the simulated time progress
faster or slower. The time server settings can be changed during the lifetime of IOServer.

###### 20.3.1. Simulated time configuration

There are three modes of `now` time:

* If the `datamodel/now` element is set in the configuration, IOServer uses this fixed time as
  :   simulated `now` time.
* If a system service “time” is configured, IOServer uses that for simulated time.
* If none of these above are set, IOServer defaults to Unix time. This is the only
  :   permitted option for a production system.

A time server has to be started from Sysmond. Below is an example how to
configure a time server:

```
<?xml version="1.0" encoding="UTF-8" ?>
<!--
  A time server controls the time (diff, speed) in simulations.
-->
<program name="timeserver">
  <log_path>%(programs/sysmond/log/directory)</log_path>

  <process name="simulated_time">
    <service name="time" protocol="http"/>

    <start_cmd>clock --server</start_cmd>
    <stop_cmd></stop_cmd>

    <start_time>15Nov2012 08:42</start_time>
    <speed>1</speed>

    <log_level>INFO</log_level>
    <log_file>${CARMTMP}/logfiles/clock</log_file>
    <log_stdout>true</log_stdout>
  </process>
</program>
```

###### 20.3.2. Limitations

* The time server must run at the same host as IOServer.
* The time server must be started before IOServer.
* `now` can never be set to a year before 1986.
* `now` can never be set to later than 06Feb2036.

#### datamodel

#### pattern

#### simulated time

##### Simulated time configuration

##### Limitations

### IOServer Metrics


##### 21.1. Process metrics

**ioserver.etables.load\_duration\_ms**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * process [processName] |
| Description: | How long it took to preload etables from the database. |

**ioserver.etables.refresh\_duration\_ms**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * process [processName] |
| Description: | How long it took to refresh etables from the database. |

**ioserver.plan.load\_duration\_ms**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * process [processName] |
| Description: | How long it took to load the plan from the database. |

**ioserver.plan.refresh\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * process [processName] * result [changed, unchanged, transient\_failure, failure] |
| Description: | Number of plan refreshes. Tag `result` indicates the outcome of the refresh. |

**ioserver.plan.refresh\_duration\_ms**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * process [processName] |
| Description: | How long it took to refresh the plan from the database. |

**ioserver.worker.start\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * process [processName] |
| Description: | Number of times an IOServer worker process has started. |

**ioserver.worker.terminate\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * process [processName] * result [success, timeout, error, signal] |
| Description: | Number of times an IOServer worker process has stopped. `result` indicates how the worker terminated. |

**ioserver.start\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * process [processName] |
| Description: | Number of times an IOServer main process has started. |

**ioserver.terminate\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * process [processName] |
| Description: | Number of times an IOServer main process has stopped. |

**ioserver.worker\_factory.start\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * process [processName] |
| Description: | Number of times an IOServer worker factory process has started. |

**ioserver.worker\_factory.terminate\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * process [processName] * result [success, timeout, error, signal] |
| Description: | Number of times an IOServer worker factory process has stopped. `result` indicates how the worker factory terminated. |

##### 21.2. Service metrics

**ioserver.plan.save\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] * result [success, conflict\_error, other\_error] |
| Description: | Number of times the plan has been saved. Tag `result` indicates the outcome of the save operation. |

**ioserver.plan.save\_duration\_ms**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * service [serviceName] |
| Description: | How long it took to save the plan to the database. |

**ioserver.trigger.event\_duration\_ms**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * service [serviceName] |
| Description: | How long it took to run a trigger (i.e. its on\_event method). |

**ioserver.trigger.event\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] * result [success, failure] |
| Description: | Number of times that a trigger has run (i.e. its on\_event method). |

**ioserver.service.reactivate\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] |
| Description: | Number of times a service has been reactivated after being deactivated because of an error. |

**ioserver.activemq.message.outgoing\_commit\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] * sink [sinkName] * result [success, failure] |
| Description: | Number of committed (added to queue) messages in a message sink, e.g. response messages. `result` indicates if the commit was successful, or if the messages were discarded (failure). |

**ioserver.activemq.message.incoming\_commit\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] * result [success, failure] |
| Description: | Number of committed (deleted from queue) messages in a message source. `result` indicates if the commit was successful, or if the messages were rolled back (because of failure, not included in `incoming_rollback_count`). |

**ioserver.activemq.message.incoming\_rollback\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] * result [success, failure] |
| Description: | Number of rolled back (returned to queue) messages in a message source. |

**ioserver.activemq.message.incoming\_fetch\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] |
| Description: | Number of fetched (read from queue) messages from a message source. |

**ioserver.message.process\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] * result [success, failure] * phase [fetch, check\_state, security\_context, handle, save] |
| Description: | Number of times that messages has been processed by a service. `result` indicates if processing was successful or not. If `result` is failure, `phase` indicates at which part of the handling process the failure occurred. |

**ioserver.message.sent\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] * result [success, failure] |
| Description: | Number of messages sent (e.g. response messages). |

**ioserver.message.fetched\_bytes**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * service [serviceName] |
| Description: | Fetched message size in bytes, implemented as a timing. |

**ioserver.message.handle\_duration\_ms**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * service [serviceName] |
| Description: | How long it took to process a message in a handler (e.g. the `handle()` method). |

**ioserver.message.sent\_bytes**

|  |  |
| --- | --- |
| Type: | timer |
| Tags: | * service [serviceName] |
| Description: | Sent message size in bytes, implemented as a timing. |

**ioserver.message.block\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] |
| Description: | Number of times message processing has failed and it has been decided to keep the message on the incoming queue. |

**ioserver.message.skip\_count**

|  |  |
| --- | --- |
| Type: | counter |
| Tags: | * service [serviceName] |
| Description: | Number of times message processing has failed and it has been decided to delete the message from the incoming queue. |

#### Process metrics

#### Service metrics

### Message Retention

#### Example Content of a Metadata Message

###### 22.1. Example Content of a Metadata Message

All of these values is regarding the original message’s data.
The message retention message can for example have their own headers.

```
{
    "version": 1,  // Message retention format version.
    "content": "bXlfY29udGVudA==",  // Original message content Base64 encoded.
    "content_type": "my_content_type",
    "content_encoding": "my_encoding",
    "message_id": "my_id", // Original message ID
    "headers": {
        // Original message headers (ActiveMQ).
    },
    "created": {
        // Relaxed extended JSON for datetime support in MongoDb. Needed for TTL.
        "$date": "2021-03-16T13:44:11Z"
    },
    "application_context": {
        "ioserver": "my_process",
        "ioservice": "my_service",

        // Either incoming or outgoing
        "direction": "incoming",

        // Order of the retention message
        "send_count": 1,

        "save_cid": 333,  // Last saved commitid.
        "plan_cid": 222,  // Worker generation.
        "now_time": "2021-03-16T13:44:00Z"
    },
    "business_context": {
        // Set by message.set_meta() in handler/trigger (any JSON).
    }
}
```

| Keys in content | Meaning & Comments |
| --- | --- |
| version | Version of the message retention structure. |
| content | Content of the original message encoded in Base64. |
| content\_type | Type of content for the original message. |
| content\_encoding | Content encoding for the original message. |
| message\_id | Original message’s message id. |
| headers | Header fields for the original message. |
| created | ISO-8601 formatted timestamp of when the IOServer created the message retention message. |
| application\_context | See table below for description of [Application Context](#app-context) keys. |
| business\_context | This could be any JSON set by the IOService implementation intended for business purposes. |

#### Application Context

###### 22.2. Application Context

| Keys | Meaning & Comments |
| --- | --- |
| ioserver | Name of the IOServer process that handled the message. |
| ioservice | Name of the IOService that handled the message. |
| direction | If it is regarding an “incoming” or “outgoing” message. |
| send\_count | Counter of number of messages sent in a trigger/handle call, eg. to sort multiple messages generated by a trigger. |
| save\_cid | The commit id which was saved by the handler. Only set for incoming and response messages. If omitted then no save occured. |
| plan\_cid | The commit id of the plan when the trigger/handle generated the message. |
| now\_time | “Now time” of the plan in ISO-8601 format. |
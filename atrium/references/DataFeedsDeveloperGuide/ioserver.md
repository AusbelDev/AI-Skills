# IOServer

Document Information
Doc Version: DevGuide 1.0.126-SNAPSHOT, Date: 2026-03-03,
Security Class: External

This document describes the IOServer and the use of the testutils.

1. Introduction
2. Concepts
2.1. IOServer process
2.2. IOService
2.3. Pattern
2.4. Handler
2.5. Trigger
2.6. Plan generation

3. Overview
4. Patterns
4.1. Subscriber
4.2. Request/response
4.3. Trigger
4.4. Repeating trigger
4.5. Event trigger
4.6. Timer
4.7. Dispatch
4.8. Dispatch Scenario

5. Messaging
5.1. Communication protocol
5.2. Large messages
5.3. Application headers
5.3.1. Incoming messages
5.3.2. Outgoing messages

6. Handler interface
6.1. Interface versions
6.2. Message types
6.3. Handler method
6.3.1. Current Interface Version: TEN
6.3.2. Previous Interface Version: NINE

6.4. on_load
6.4.1. Current Interface Version: TEN
6.4.2. Previous Interface Version: NINE

6.5. on_fault
6.5.1. Current Interface Version: TEN
6.5.2. Previous Interface Version: NINE

7. Trigger interface
7.1. Interface versions
7.2. Message types
7.3. on_load
7.4. on_event
7.4.1. Current Interface Version: TEN
7.4.2. Previous Interface Version: NINE

8. Migration
8.1. Mandatory migration from interface version NINE to TEN
8.1.1. Python imports
8.1.2. Handler interface version
8.1.3. The on_load method

8.2. Mandatory migration from interface version SEVEN to NINE
8.2.1. Python imports
8.2.2. Handler interface version
8.2.3. The on_fault method
8.2.4. The on_event method
8.2.5. Accessing Rave rulesets

8.3. Optional migration from version SEVEN to version NINE
8.3.1. Access different viewpoints of the plan
8.3.2. Service context instead of handler context and trigger context
8.3.3. Possible to save in repeatingtrigger
8.3.4. Possible to use the same handler for plain and SOAP

8.4. Mandatory migration in IOServer version 28.0.0
8.4.1. Multiple sinks must be named

8.5. Recommended migration in IOServer version 28.0.0
8.5.1. Change &lt;skipconflict&gt; to &lt;conflict_detection&gt; in configuration
8.5.2. Use repeatingtrigger rather than timer + eventtrigger

8.6. Mandatory migration in IOServer version 32.0.0
8.6.1. Configuration for data model has changed

9. High Availability
9.1. Active / Active
9.2. Active / Passive
9.3. HA Store

10. Error handling
10.1. Trigger services
10.2. Handler services
10.3. Deactivated services
10.4. Timed-out services
10.5. IOServer defined exceptions
10.5.1. Message errors
10.5.2. System errors (non-message errors)

11. Best Practices
11.1. IOServices sharing IOServer
11.2. Number of worker processes
11.3. Services sharing worker
11.4. Pre-load of Rave tables
11.5. Running the same IOServices on different nodes
11.6. Monitoring service deactivation
11.7. Worker time-out and pings
11.8. Handling of errors in IOService

12. Configuration
12.1. program
12.2. process
12.3. refresh
12.4. datamodel
12.4.1. preload_tables

12.5. db
12.6. ioservice
12.7. pattern
12.7.1. jcmsstatemessagereplace

12.8. binding
12.8.1. profile

12.9. source
12.10. sink
12.11. message_retention
12.12. hastore
12.13. extra_indexes
12.14. refresh_boundary
12.15. errors
12.15.1. retrycount
12.15.2. blockmsg

12.16. dispatch
12.17. Dispatch Scenario

13. Command-line arguments
14. Cmsshell integration
14.1. cmsshell plugin
14.1.1. help
14.1.2. clear_hastore
14.1.3. list_config
14.1.4. selftest
14.1.5. service

14.2. Self tests
14.2.1. Queues
14.2.2. Processes
14.2.3. Services

15. IOServer control tool
15.1. Purpose
15.2. Command-line arguments
15.3. Examples

16. IOServer Python API reference
16.1. IOServer Python API Reference Version 10
16.1.1. jcms.ioserver.versions
16.1.2. jcms.ioserver.constants
16.1.3. jcms.ioserver.exceptions
16.1.4. jcms.ioserver.version10.config
16.1.5. jcms.ioserver.version10.actions
16.1.6. jcms.ioserver.version10.message
16.1.7. jcms.ioserver.version10.context
16.1.8. jcms.ioserver.version10.mave2.IPlanHolder

16.2. IOServer Python API Reference Version 9
16.2.1. jcms.ioserver.versions
16.2.2. jcms.ioserver.constants
16.2.3. jcms.ioserver.exceptions
16.2.4. jcms.ioserver.version9.config
16.2.5. jcms.ioserver.version9.actions
16.2.6. jcms.ioserver.version9.message
16.2.7. jcms.ioserver.version9.context
16.2.8. jcms.ioserver.version9.mave2.IPlanHolder

17. Testutils Python API reference
17.1. TestUtils Python API Reference Version 10
17.1.1. Conflict Detection Strategy Constants
17.1.2. jcms.ioserver.testutils.version10.main.TestMain
17.1.3. jcms.ioserver.testutils.version10.main.IMemoryHAStore
17.1.4. jcms.ioserver.testutils.version10.main.IMemoryQueue
17.1.5. jcms.ioserver.testutils.version10.main.ITestConfig
17.1.6. jcms.ioserver.testutils.version10.TestRunner

17.2. TestUtils Python API Reference Version 9
17.2.1. jcms.ioserver.testutils.version9.main.TestMain
17.2.2. jcms.ioserver.testutils.version9.main.IMemoryHAStore
17.2.3. jcms.ioserver.testutils.version9.main.IMemoryQueue
17.2.4. jcms.ioserver.testutils.version9.main.ITestConfig
17.2.5. jcms.ioserver.testutils.version9.TestRunner

18. IOServer logs
18.1. Configuring logging
18.2. Flow
18.3. Logging from an IOService
18.4. Getting the correct log level for an integration service
18.4.1. Log level contents

18.5. Connecting log entries to messages
18.6. Log format

19. IOServer TestUtils
19.1. How to use TestUtils
19.1.1. How to setup initial data to reuse between tests
19.1.2. Logging with testutils

20. Configuration only relevant for testing
20.1. datamodel
20.2. pattern
20.3. simulated time
20.3.1. Simulated time configuration
20.3.2. Limitations

21. IOServer Metrics
21.1. Process metrics
21.2. Service metrics

22. Message Retention
22.1. Example Content of a Metadata Message
22.2. Application Context



--- SUBPAGE: introduction.html ---

# 1. Introduction

IOServer is the central application for serving I/O interfaces and web applications. It holds an
ARA plan instance and a Rave rule set, and refreshes continuously to catch changes in
the central data store. The plan is shared by a set of IOServices that can
apply and save changes, as well as extract data to send to the IOService client.

The cached ARA plan does not support multiple parallel isolated working sessions, where each
interface saves its own changes. Instead IOServer spawns workers for the
different tasks. Each worker only modifies its own private image of the plan and
while the workers are busy the main plan is only updated by refreshing from the central data store.
Any save operation initiated by a worker is done by the IOServer framework.
This leads to an important characteristic of IOServer interfaces, the
handlers always work on a version of the plan that is the result of the lastest refresh cycle and not
directly against the database. Even if a message B is handled later than A, it is not certain that the
result of A is visible when handling B. The possible actions to
guarantee this visibility are expensive and limit the scalability, performance, and throughput of
all interfaces running on the same server instance, thus we should avoid them as much as possible.

IOServer is not exposed at the system border and uses only the internal message
protocol (currently ActiveMQ) to communicate with its clients. The clients are expected to be part of the
system itself and IOServer does not perform any authentication, message receipt logging, or other actions
required at the system border. For external interfaces, IOServer is always combined
with a system-border application that deals with all external communication.

IOServer instances are started as native processes that can be monitored by, for example, sysmond. Because a
single instance can serve several services, the options for high availability and scalability are
flexible including active/active setups. The only exceptions are interfaces that have
strong requirements on ordering, and thus only can be served by a single service instance at a time.

--- SUBPAGE: concepts.html ---

# 2. Concepts

## 2.1. IOServer process

An IOServer process loads a single plan (data context) that can be used by one or more IOServices.

## 2.2. IOService

An IOService is a service running on an IOServer instance. It can fetch messages from a message source or react on events,
handle them, and provide responses. The service-specific logic is placed in a handler or trigger.
Timer services do not need a handler or trigger, but produce event messages based on a
configured timing.

Services sharing the same plan can be handled by a single IOServer process.

## 2.3. Pattern

A pattern is an implementation of the framework for handling a particular class of services with common
characteristics. See Patterns.

## 2.4. Handler

A handler is a service-specific piece of Python code that is called when a request is
received from a message source. The handler interprets the request and performs the appropriate actions,
which can include applying changes to the loaded plan, doing business evaluations, and formulating
a response. The actual save is done by the IOServer framework, not the handler.

## 2.5. Trigger

A trigger is a service-specific piece of Python code that is called based on events.

A trigger event occurs every time IOServer loads a new change set into the cached plan. The
trigger evaluates the change set and checks for types of changes that should lead to actions,
typically producing messages. A common use case is feeding data changes to downstream systems
online.

An eventtrigger event is typically generated by a timer. The trigger evaluates the
current state of the plan to detect needed actions based on the data state and current time. The
typical use case is to produce and send messages on a time condition, for example two
hours before a flight departure.

A variant of the eventtrigger is the repeatingtrigger, which is executed repeatedly with a
configured delay between the executions. Alternatively, it can be configured with a cron style time
specification, similar to the timer used by eventtrigger.

## 2.6. Plan generation

There is a single generation of the plan holder/builder called “mave2”, which
is used on both the Studio (Major Release) and Atrium architectures.

--- SUBPAGE: overview.html ---

# 3. Overview

For each IOServer process in the configuration, a main OS process is started. This process can serve
one or more IOServices.

The main process is responsible for:

- initializing all that is needed at startup
- loading the plan and associated rule set and parameters
- refreshing the plan periodically
- spawning worker processes to do the actual work
- keeping track of worker processes and restarting them if needed
- shutting down worker processes periodically
- communicating with sysmond.

When a worker process
is started it inherits the current state of the loaded plan from the main process, since the
memory is shared. The worker serves requests as determined by the configuration, the pattern
implementation, and the handler. Actions can be triggered by incoming messages or trigger events
in the application. The results can be outgoing messages or updates to the plan. The pattern
implementation in the worker process is responsible for saving changes to the database.
An IOService can be served by one or more worker processes. Using more than one worker
process means that messages are handled in parallel.

--- SUBPAGE: patterns.html ---

# 4. Patterns

The IOServer framework has a set of patterns that implement common use cases of I/O interfaces.

## 4.1. Subscriber

The subscriber pattern serves inbound interfaces that update the database based
on incoming messages. Typically the response messages have no data, but may contain
acknowledge, status, or fault messages.

In this pattern incoming messages may be processed in chunks, so that more than
one message is processed in one go.

The database save happens based on these conditions:
- If the maximum number of messages to aggregate has been reached.
If the maximum time in milliseconds to wait for incoming messages has been reached.
The intention is to not have handled messages unsaved for longer than necessary in case of
an empty queue.

If the maximum time in seconds that the subscriber can spend aggregating messages
has been reached.

The error handling can be configured to behave differently based on the error type and the
error context, see the error paragraph in the configuration chapter.
The final action when handling an error is either skip or block.

## 4.2. Request/response

The request/response pattern serves interfaces where a request message is received, and an
output message with requested data is returned.

In this pattern messages are processed one by one, and not in chunks.

This pattern may update the plan as well, so the handler can specify that
the pattern implementation should save the modified plan.

## 4.3. Trigger

The trigger pattern executes a trigger based on database changes, causing outgoing
messages to be sent.

In trigger interface version NINE and higher, a trigger can make changes
and have the pattern implementation save them in the plan.
However, as the changes are likely to be part of the next triggered change set,
much care must be taken in the trigger code (in the on_event
method) so that it does not trigger on its own changes and creates an endless
loop.

If the trigger throws any exception, the current state is not
regarded successfully handled and the change set presented next time will be
bigger. If the trigger does not throw an exception, the current state is
considered successfully handled, no matter whether any messages were emitted,
and the next run does not show the changes again.

## 4.4. Repeating trigger

The repeating trigger pattern repeatedly executes a trigger according to a given delay
or a cron style time specification.

The typical use case is to send outgoing messages that are not dependent on
changes to the plan.

In trigger interface version NINE and higher, a repeating trigger can make changes
and have the pattern implementation save them in the plan.
If there are errors in the trigger or when saving, both the plan changes and
the outgoing messages are rolled back.

## 4.5. Event trigger

The event trigger pattern executes a trigger when an incoming message arrives.
The message content is ignored, only its arrival is of importance.

This is typically used together with the timer pattern to trigger at specific times.

In trigger interface version NINE and higher, an event trigger can make changes
and have the pattern implementation save them in the plan.
If there are errors in the trigger or when saving, both the plan changes and
the outgoing messages are rolled back.

## 4.6. Timer

The timer pattern sends an empty message based on a simplified cron based timer.

This is typically used together with the event trigger pattern to trigger at specific times.

There is no way to call a handler or trigger in the timer pattern itself.

## 4.7. Dispatch

Not strictly speaking an IOServer pattern, the dispatch feature groups handlers together into a
“super-service”, which is able to monitor multiple queues, and route messages to different
sub-handlers depending on what queue a message came in on.

Each of these sub-handers must adhere to the same handler interface as a normal handler,
specifically they must use the same Interface versions as the dispatcher itself.
Essentially becoming part of a common service, each sub-handler will share the common characteristics
of the service, i.e. sharing pattern, binding etc. (see ioservice).

The dispatch feature has two main use-cases:

- A single service supporting multiple versions of messages by directing them to different handlers.
Grouping multiple services in order to share workers, thus reducing the total number of workers
needed to run the services. Mostly useful for low-frequency services (see best practices,
section Services sharing worker).

For configuration, see dispatch.

## 4.8. Dispatch Scenario

Note
Supported only on Python 3

Same usage pattern as Dispatch, but the result will not be saved to the live plan,
it will only be saved into a scenario.

For configuration, see Dispatch Scenario.

Each request message that is handled by the jcms.ioserver.version10.dispatch_scenario_handler
can have the following properties set in the header. The properties will be written to the scenario.

Sub-element

Mandatory

Type

Description

jcms_scenario_name

Yes

string

The name of the scenario.

jcms_scenario_author

No

string

The name of the author of the scenario.

jcms_scenario_description

No

string

The description of the scenario.

jcms_scenario_source_system

No

string

The system which sent the scenario.

jcms_scenario_reference

No

string

The scenario ID in the source system.

--- SUBPAGE: messaging.html ---

# 5. Messaging

## 5.1. Communication protocol

Messages are typically received and sent using Apache Qpid or Apache ActiveMQ brokers.
In both cases, IOServer uses Qpid client libraries for source and sink.
This works because both brokers support the AMQP protocol,
albeit with different protocol versions.

Broker

Protocol

Qpid

amqp0-10

ActiveMQ

amqp1.0

## 5.2. Large messages

For applications sending large messages it is a good idea to set up a filehub to
handle those messages reliably. In order to use the filehub for large messages the
IOServer sink should be configured with large_message_url and
large_message_size to decide which messages should be considered large and where
the filehub is located.  Sending messages through the filehub is transparent after
this config is done so the receiver will not need to handle these messages
differently, this is handled internally.

## 5.3. Application headers

IOServer uses some application-specific headers in messages.

### 5.3.1. Incoming messages

IOServer recognizes the following application headers in incoming messages:

Application header

Type

Description

jcms_role

string

cacs role to use when handling the request

jcms_state

integer

state of the plan that the request is based on
(The Dave commit id.)

jcms_client

string

name of client user

jcms_crew

string

crew ID for the crew that a request concerns

jcms_traceid

string

trace ID logged in the MDC area (as X-B3-TraceId)
in the log file

IOServer adds the following headers in its incoming messages:

Application header

Type

Description

jcms_source_queue

string

name of the queue reference the message came in
on, as specified in the configuration.

### 5.3.2. Outgoing messages

IOServer adds the following headers in outgoing messages:

Application header

Type

Description

jcms_responsecode

string

Status about how IOServer managed to handle
the incoming message.

jcms_state

integer

The state of the plan when the request handled.
(The Dave commit id)

jcms_traceid

string

Copied from the incoming message.

--- SUBPAGE: handlers.html ---

# 6. Handler interface

A handler is a Python module that implements methods for
all operations in the format specification of the messages it handles.

## 6.1. Interface versions

IOServer supports handlers with different versions of the handler interface at the same time.
The current version is version TEN, but all supported versions are enumerated in the
jcms.ioserver.versions.InterfaceVersion Python class.

To determine which interface version a handler implements IOServer calls a special method,
handler_interface_version, which should return one of the following values:

Return value

Interface

InterfaceVersion.NINE

version NINE (deprecated)

InterfaceVersion.TEN

version TEN

## 6.2. Message types

Depending on the configuration of a handler, IOServer interprets the messages exchanged with the handler
in one of the following ways:

SOAP-XML handlerThe exchanged messages are expected to be SOAP envelopes
and the request is the (single) child of the SOAP body element.

Plain text handlerThe exchanged messages can be of any format and no
interpretation is made outside of the handler.

The type of messages to use is defined by the protocol tag in the binding section
of the handler configuration.
If protocol is set to mixed, the decision to use SOAP or plain text is based on the content type
of the incoming message.

## 6.3. Handler method

When calling a handler, IOServer finds the name of the method to use in one of the following ways:

- For a SOAP-XML handler, the name is read from the SOAPAction message header.
- For a plain text handler, the name is read from the handler configuration. The default name is handle.

### 6.3.1. Current Interface Version: TEN

In handler interface version TEN, the handler method has the following signature:

&lt;method_name&gt;(planholder, service_context)

The planholder argument is a version TEN IPlanHolder object, which gives
access to the ARA plan and ruleset currently loaded in IOServer.
There are two variants of the planholder object, version10.planholder_macao
for the Atrium architecture and version10.planholder_militaris for the Studio architecture.
Which variant to use is specified by the planholder setting in the configuration.

The service_context argument is a version10.context.ServiceContext object,
from which the handler can retrieve the request message and set response message.
The service context also provides additional information, for example access to the configuration.

The version10.context.ServiceContext that is used by handlers is the same that is used by triggers.

The handler method has to return one of the following values, defined in version10.actions.PlanAction:

PlanAction.UNCHANGEDno changes in the plan, nothing needs to be saved

PlanAction.SAVEchanges in the plan need to be saved

PlanAction.ROLLBACKchanges in the plan must be rolled back.

When the plan action has been executed successfully, any provided response message is sent out
and the request is removed from the in queue.

6.3.1.1. The ContentModel API
The ContentModel API parses SoapIOMessages and has two variants;
version10.PyxbContent for pyxb, and version10.LxmlContent for Lxml.

The nodes are created by using a factory, as shown in the following example:

import jcms.ioserver.version10.LxmlContent as ContentModel

# Create a factory for SOAP messages.
# LxmlContentFactory accepts xsd and soap_xsd as either strings (as in this example)
# or file paths.
xsd = open(&#39;MyService.xsd&#39;).read()
soap_xsd = open(&#39;Envelope.xsd&#39;).read()
factory = ContentModel.LxmlContentFactory(xsd, tnsname=&quot;myservice&quot;, soap_xsd=soap_xsd)

# Parse request message using factory.
payload = factory.parseMsgAndGetPayload(handler_context.request_message)
print payload.attribute
# ...

# Create a response.
response_msg = handler_context.create_io_message(&quot;&quot;)
response_payload = factory.makeNode(&quot;MyResponseType&quot;, &quot;response&quot;)
response_payload.myString = &quot;some string&quot;

# Add payload to message.
factory.formatMsgAndSetPayload(response_msg, response_payload)
handler_context.response_message = response_msg

### 6.3.2. Previous Interface Version: NINE

Warning
This API version is deprecated and will be removed in a future ioserver release.

In handler interface version NINE, the handler method has the following signature:

&lt;method_name&gt;(planholder, service_context)

The planholder argument is a version NINE IPlanHolder object, which gives
access to the ARA plan and rule set currently loaded in IOServer.
There are two variants of the planholder object, version9.planholder_macao
for the Atrium architecture and version9.planholder_militaris for the Studio architecture.
Which variant to use is specified by the planbuilder setting in the configuration.

With the Atrium version of the planholder object, handlers must use the RaveSession APIs to access rule sets.

The service_context argument is a version9.context.ServiceContext object,
from which the handler can retrieve the request message and set response message.
The service context also provides additional information, for example access to the configuration.
Handlers and triggers use the same service context.
Note that some convenience methods that were present in earlier versions have been removed.

The handler method has to return one of the following values, defined in version9.actions.PlanAction:

PlanAction.UNCHANGEDno changes in the plan, nothing needs to be saved

PlanAction.SAVEchanges in the plan need to be saved

PlanAction.ROLLBACKchanges in the plan must be rolled back.

When the plan action has been executed successfully, any provided response message is sent out
and the request is removed from the in queue.

6.3.2.1. The ContentModel API
The ContentModel API parses SoapIOMessages and has two variants;
version9.PyxbContent for pyxb, and version9.LxmlContent for Lxml.

The nodes are created by using a factory, as shown in the following example:

import jcms.ioserver.version9.LxmlContent as ContentModel

# Create a factory for SOAP messages.
# LxmlContentFactory accepts xsd and soap_xsd as either strings (as in this example)
# or file paths.
xsd = open(&#39;MyService.xsd&#39;).read()
soap_xsd = open(&#39;Envelope.xsd&#39;).read()
factory = ContentModel.LxmlContentFactory(xsd, tnsname=&quot;myservice&quot;, soap_xsd=soap_xsd)

# Parse request message using factory.
payload = factory.parseMsgAndGetPayload(handler_context.request_message)
print payload.attribute
# ...

# Create a response.
response_msg = handler_context.create_io_message(&quot;&quot;)
response_payload = factory.makeNode(&quot;MyResponseType&quot;, &quot;response&quot;)
response_payload.myString = &quot;some string&quot;

# Add payload to message.
factory.formatMsgAndSetPayload(response_msg, response_payload)
handler_context.response_message = response_msg

## 6.4. on_load

A handler may implement a method called on_load.
This method is called once just after the plan has been loaded,
and can be used to cache and share objects between workers.
Note that any modifications to the plan, such as setting up indices, are shared by all IOServices.

### 6.4.1. Current Interface Version: TEN

The on_load method has the following signature:

on_load(planholder, context)

The planholder argument is a planholder object, which gives
access to the ARA plan and rule set currently loaded in IOServer.

The context argument is a version10.context.OnLoadServiceContext,
which provides service name and configuration to the handler.

The on_load method does not have to return anything.

### 6.4.2. Previous Interface Version: NINE

The on_load method has the following signature:

on_load(planholder)

The planholder argument is a planholder object, which gives
access to the ARA plan and rule set currently loaded in IOServer.

The on_load method does not have to return anything.

## 6.5. on_fault

A handler may implement a method called on_fault.
This method is called when an error occurs, and lets the handler influence what type of
error response to send.

### 6.5.1. Current Interface Version: TEN

In handler interface version TEN, the on_fault method has the following signature:

on_fault(planholder, service_context, exception)

The planholder argument is a version TEN IPlanHolder object, which gives
access to the ARA plan and ruleset currently loaded in IOServer.

The service_context argument is the service context, the same as passed to the handler method.

The exception argument is the raised exception.

The possible return values are defined in version10.actions.FaultAction.
There are three possible actions the on_fault method can take:

Set a custom response message in the service context, and return FaultAction.SEND_RESPONSE.
In this case the response will be sent.

Return FaultAction.NO_RESPONSE.
In this case no response message is sent, even if one was set.

Return FaultAction.DEFAULT_RESPONSE.
In this case the default response action for the given protocol is taken.
For the plain protocol the error is logged and no response message is sent.
For the soap protocol the error generates a standard SOAP fault message.

### 6.5.2. Previous Interface Version: NINE

In handler interface version NINE, the on_fault method has the following signature:

on_fault(planholder, service_context, exception)

The planholder and service_context arguments are the same as passed to the handler method.

The exception argument is the raised exception.

The possible return values are defined in version9.actions.FaultAction.
There are three possible actions the on_fault method can take:

Set a custom response message in the service context, and return FaultAction.SEND_RESPONSE.
In this case the response is sent.

Return FaultAction.NO_RESPONSE.
In this case no response message is sent, even if one was set.

Return FaultAction.DEFAULT_RESPONSE.
In this case the default response action for the given protocol is taken.
For the plain protocol the error is logged and no response message is sent.
For the soap protocol the error generates a standard SOAP fault message.

--- SUBPAGE: triggers.html ---

# 7. Trigger interface

A trigger is a Python module that implements methods for the trigger interface,
which consists of the on_load and on_event methods.

## 7.1. Interface versions

As for handlers, IOServer supports triggers with different versions of the trigger interface at the same time.
The current version is version TEN, but all supported versions are enumerated in the
jcms.ioserver.versions.InterfaceVersion Python class.

To determine which interface version a trigger implements IOServer calls a special method,
handler_interface_version, which should return one of the following values:

Return value

Interface

InterfaceVersion.NINE

version NINE (deprecated)

InterfaceVersion.TEN

version TEN

## 7.2. Message types

Triggers can use both the SOAP and plain text protocols, just as handlers,
but the mixed option is not available.

## 7.3. on_load

For a description of the on_load method, see the handler interface.

## 7.4. on_event

The on_event method is called according to the pattern given in the configuration.

For the trigger pattern this happens when the plan is changed in the
latest refresh. In this case the ChangeSet property of the PlanHolder object can be used to determine if the
changes are relevant for the on_event method.

For timer-based trigger patterns, such as repeatingtrigger and timer + eventtrigger, the on_event method
is typically called regularly based on timer events.

Usually the on_event method sends outgoing messages by using methods available in the service_context object.

### 7.4.1. Current Interface Version: TEN

In trigger interface version TEN, the on_event method has the following signature:

on_event(planholder, service_context)

The planholder argument is a version TEN IPlanHolder object. It supports the RaveSession APIs
and gives access to the ARA plan and rule set currently loaded in IOServer.
There are two variants of the planholder object, version10.planholder_macao
for the Atrium architecture and version10.planholder_militaris for the Studio architecture.
Which variant to use is specified by the planbuilder setting in the configuration.

The service_context argument is a version10.context.ServiceContext object,
from which the trigger can create and send the generated requests.
The service context also provides additional information, for example access to the configuration.

The service_context that is used by triggers is the same that is used by handlers.

The on_event method has to return one of the following values, defined in the version10.actions.PlanAction class:

PlanAction.UNCHANGEDno changes in the plan, nothing needs to be saved

PlanAction.SAVEchanges in the plan need to be saved

PlanAction.ROLLBACKchanges in the plan must be rolled back.

When the plan action has been executed successfully, any messages the on_event method has sent are
committed to the outgoing queue. If there was an error, any uncommitted outgoing messages are rolled back.

Note
The possiliblity to save plan changes caused by an on_event method is primarily intended for timer based trigger
patterns, such as repeatingtrigger or eventtrigger, but it can be done in a trigger pattern as well.
In that case care must be taken so that the on_event method does not trigger on its own changes,
thus creating an endless loop.

Note
PlanAction.SAVE is not allowed when using stepwise refresh mode, see refresh_boundary configuration.
This causes the service to be disabled.

### 7.4.2. Previous Interface Version: NINE

Warning
This API version is deprecated and will be removed in a future IOServer release.

In trigger interface version NINE, the on_event method has the following signature:

on_event(planholder, service_context)

The planholder argument is a version NINE IPlanHolder object, which gives
access to the ARA plan and rule set currently loaded in IOServer.
There are two variants of the planholder object, version9.planholder_macao
for the Atrium architecture and version9.planholder_militaris for the Studio architecture.
Which variant to use is specified by the planbuilder setting in the configuration.
With the Atrium variant of the planholder object, triggers must use the RaveSession APIs to access rule sets.

The service_context argument is a version9.context.ServiceContext object,
from which the trigger can retrieve the request message and set response message.
The service context also provides additional information, for example access to the configuration.
Handlers and triggers use the same service context.

The on_event method has to return one of the following values, defined in the version9.actions.PlanAction class:

PlanAction.UNCHANGEDno changes in the plan, nothing needs to be saved

PlanAction.SAVEchanges in the plan need to be saved

PlanAction.ROLLBACKchanges in the plan must be rolled back.

When the plan action has been executed successfully, any messages the on_event method has sent are
committed to the outgoing queue. If there was an error, any uncommitted outgoing messages are rolled back.

Note
The possiliblity to save plan changes caused by an on_event method is primarily intended for timer based trigger
patterns, such as repeatingtrigger or eventtrigger, but it can be done in a trigger pattern as well.
In that case care must be taken so that the on_event method does not trigger on its own changes,
thus creating an endless loop.

Note
PlanAction.SAVE is not allowed when using stepwise refresh mode, see refresh_boundary configuration.
This causes the service to be disabled.

--- SUBPAGE: migration.html ---

# 8. Migration

## 8.1. Mandatory migration from interface version NINE to TEN

### 8.1.1. Python imports

Python import specifications need to refer to version10 instead of version9.

### 8.1.2. Handler interface version

The handler_interface_version method must return InterfaceVersion.TEN.

### 8.1.3. The on_load method

The signature of the on_load method has changed, and now takes an additional context
argument, see on_load.

Implementations of on_load must be migrated to take the context argument.
This applies to both Handlers and Triggers.

## 8.2. Mandatory migration from interface version SEVEN to NINE

### 8.2.1. Python imports

Python import specifications need to refer to version9 instead of version7.

### 8.2.2. Handler interface version

The handler_interface_version method must return InterfaceVersion.NINE.

### 8.2.3. The on_fault method

The signature of the on_fault method in handler modules has been changed and
now takes an additional planholder argument, see on_fault.

Implementations of on_fault must be migrated to take the planholder argument.

### 8.2.4. The on_event method

Trigger services may now save data. For this reason the on_event methods must return
a PlanAction, just as handler methods do. See on_event for details.

### 8.2.5. Accessing Rave rulesets

In interface versions SIX and SEVEN there were two ways to access Rave rule sets
when using the Mave2 version of the planholder object:

- Using the getRuleset method  (or getMave2Ruleset) on planholder. No longer supported.
Using the getRaveSession method on planholder, and then use the ARA
RaveSession APIs.

In version NINE, only the second variant is available and all code using the the first
variant must be migrated to use getRaveSession instead.

Warning
The brave2 variant is no longer supported for any version.

Warning
Versions SIX and SEVEN of the IOServer API are deprecated and will be removed
in a future IOServer release.

## 8.3. Optional migration from version SEVEN to version NINE

### 8.3.1. Access different viewpoints of the plan

For handler or trigger code that needs to access both live and
published data, the following new utility methods on the Mave2 planholder may be useful:

getMave2PlanWithViewpoint(dataset)returns the ARA plan with the Viewpoint for the specified dataset.

getRaveSessionWithViewpoint(dataset)returns the RaveSession associated with the ARA plan with the Viewpoint for the specified dataset.

See the ARA documentation for an explanation of Plan Viewpoints.

### 8.3.2. Service context instead of handler context and trigger context

In version SEVEN and earlier, different types were passed
to handlers (handler context) and triggers (trigger context) to provide
context and utility functions.

These types have been merged to a common type (service context) in
version NINE.
There is no required migration for this, as the new type contains
all methods that were available in the old types.

Optionally the name of the arguments to the handler methods, on_fault
and on_event, can be changed to service_context.

### 8.3.3. Possible to save in repeatingtrigger

Certain services need to be executed repeatedly, or according to some time pattern, and
also to both send outgoing messages and save a new state to the database.

Previously this had to be separated into two IOServices, one repeatingtrigger to get the
repetition and another IOService that could perform the save.

By using the new possibility to save in repeatingtrigger patterns, such services can now be
combined to avoid the need for an extra IOService.

### 8.3.4. Possible to use the same handler for plain and SOAP

In some cases the same business operation is needed for different interfaces
that only differ in the used message format, plain or soap.
For those cases it is now possible to use the same handler and specify mixed
as the protocol in the configuration. See binding in the configuration
reference.

## 8.4. Mandatory migration in IOServer version 28.0.0

### 8.4.1. Multiple sinks must be named

When using multiple output queues (sinks), all sinks must now be named.
It is possible to specify that one of the sinks is the default sink, but
it must still have a name.

See sink in the configuration reference.

When there is only one sink, it does not have to have a name.

## 8.5. Recommended migration in IOServer version 28.0.0

### 8.5.1. Change &lt;skipconflict&gt; to &lt;conflict_detection&gt; in configuration

There is new way to configure whether an IOService should have conflict detection:

The previous configuration:

&lt;skipconflict&gt;true&lt;/skipconflict&gt;

corresponds to the new configuration:

&lt;conflict_detection&gt;disabled&lt;/conflict_detection&gt;

and the previous configuration:

&lt;skipconflict&gt;false&lt;/skipconflict&gt;

corresponds to the new configuration:

&lt;conflict_detection&gt;message&lt;/conflict_detection&gt;

See the configuration reference for pattern for more information.

It is good practice to always specify the conflict detection setting for
IOServices, as the default will be changed in a future release.

### 8.5.2. Use repeatingtrigger rather than timer + eventtrigger

In earlier versions it required two services to execute a trigger at specific times:

A timer service that could be configured to send a message at specific
times according to a crontab-style pattern. This service could not execute
any handler or trigger code.

An eventtrigger service that ran a trigger each time it received a
message from the timer service.

This use case can now be implemented by a single service that uses the
repeatingtrigger pattern, as that pattern now supports the crontab-style
time specification in addition to what it handled earlier.

Using one service instead of two reduces the IOServer overhead.

## 8.6. Mandatory migration in IOServer version 32.0.0

### 8.6.1. Configuration for data model has changed

The configuration for the data model is a bit more logical now, but some changes are needed.

Pre-migration planbuilder

Pre-migration domain

Post-migration planbuilder

Post-migration domain

air1

air1

mave1 or mave2

air1

air2

air2

mave2

air2

mave2

air1

No migration needed

mave2

air2

No migration needed

air1

air2

Not supported, use
planbuilder mave2, domain air2

--- SUBPAGE: high_availability.html ---

# 9. High Availability

## 9.1. Active / Active

It is possible to run the same service on multiple nodes, balancing the load between them. The
messaging system (ActiveMQ) can handle multiple consumers at the same time.

Warning
Active/active cannot be used with inbound services that have strict ordering requirements (incoming
messages must be processed in order), nor with trigger-based outbound services.

## 9.2. Active / Passive

Sysmond can be configured so that the same IOServer service runs at multiple nodes, but
only one of them is active at a time. All such IOServer processes load the database plan and keep it
up to date via refresh, but only the active one has worker processes.

Warning
Active/passive cannot be used with inbound services that have strict ordering requirements (incoming
messages must be processed in order).

## 9.3. HA Store

An HA store keeps track of how far an IOService has progressed (database state). This is
mostly used by trigger services, but other service patterns may also store additional information.

The storage has two purposes:

- When the IOServer restarts, it resumes operation at saved database state.
- When fail-over occurs in an active/passive system, the new master resumes where the old one left off.

--- SUBPAGE: error_handling.html ---

# 10. Error handling

If a message fails, the general error handling is that IOServer:

- puts back the message on the queue
- refreshes its plan to get the latest state of the system
- retries to handle the message

which hopefully solves the problem.

How many times a message is retried, and what happens when if it
eventually fails, are configurable per service.

## 10.1. Trigger services

If an error occurs for a trigger service:

- the current worker is terminated
- no changes are saved to the database
- no messages are sent
- the service restarts the trigger from the last successful commit id.

Note
Some messages may be sent if the trigger sends multiple messages to destinations on different brokers.

If the service continues to fail, it is eventually deactivated and
the issue has to be resolved manually.

## 10.2. Handler services

How a handler reacts on failure is configurable per service.
If a failure occurs, the handler retries the message causing the error
a configurable number of times.

If the number of retries are exhausted the handler can be
configured to either:

block the messagewhich puts the message back first on the queue,
effectively blocking any subsequent reading from the queue.

skip the messagewhich removes the message from the queue allowing
the service to continue with the rest of the messages.

Which action to choose depends mainly on if the service can be allowed to lose a message.
If the message is skipped, the service continues without the need for manual intervention but the message is lost.
If the message is blocked, the service is deactivated
until the message is manually handled or removed.

If the number of retries for a message is exhausted, the on_fault method of the service is called.
In the on_fault method, a message with error information may be created to be sent as a response.
IOServer adds a message property, jcms_responsecode, to the response message.
The property contains the action taken due to the failure:

MESSAGE_OKMessage has been handled and no error has occurred

MESSAGE_SKIPPEDMessage has failed and the message has been removed from the queue

MESSAGE_BLOCKEDMessage has failed and the message has been put back to the queue

The property can be overridden in the on_fault method by adding a custom value to the jcms_responsecode property.

## 10.3. Deactivated services

Deactivated services are restarted with roughly 5 minutes interval.
If the service can handle messages it continues as if nothing has happened
from where it was deactivated.
If it still has problems it is deactivated again and restarted 5 minutes later.

## 10.4. Timed-out services

During normal operation a worker process pings the main process between calls to the handler,
and also pings repeatedly if the worker is idle for a while.

If a worker has not pinged within the configured worker time-out, see worker_time_out, the main
process prints a warning to the log file. After three missed pings in a row, the log message level is changed to error.

If some workers for a service have timed out, missed three pings in a row, the service is considered “degraded”.
If all workers for a service have timed out, the service is considered “unresponsive”.
If a timed out worker pings the main process, it is considered active again.
All these statuses can be viewed by using ioserverctl status or ioserverctl list.

## 10.5. IOServer defined exceptions

The exceptions module defines a hierarchy of exceptions for handlers and pattern
implementations to use when signalling error conditions.
All of the exceptions inherit from the IOSError base class.

It is the pattern that implements an error handling strategy, the handler
only signals errors by raising the appropriate exception.

### 10.5.1. Message errors

Errors that are specific to a particular incoming message inherit from the MessageError class.

There are three kinds of message errors:

10.5.1.1. Transient message errors
Transient message errors (TransientMsgError class) are used for temporary conditions that
may be resolved if the operation is retried.

Typically the pattern retries the operation that failed a number of times,
and if there is still an error it is converted to either
a SkipMsgError or a BlockingMsgError error.
The retries can be performed locally in the pattern implementation in the worker process,
or via a round trip to the main processes.

The configuration defines how many local and global retries to perform,
and which error type to convert the transient message to if it still fails.

There are two predefined exceptions that inherit from TransientMsgError:

DatabaseConflictErrordenotes a multirecord conflict exception in the database when saving

DatabaseDataTooOldExceptiondenotes a single-record conflict in the database when saving.

10.5.1.2. Blocking message errors
A blocking message error (BlockingMsgError class) leaves the failing message
in the queue so that it is read again the next time messages are fetched.

10.5.1.3. Skip message errors
A skip message error (SkipMsgError class) causes the failing message to be removed
from the in-queue so that the service can proceed with the following messages.

### 10.5.2. System errors (non-message errors)

System errors are errors that are not specific to a particular message,
for example general I/O errors.

The base class for system errors is [SystemError](https://docs.python.org/3/library/exceptions.html#SystemError).

10.5.2.1. Transient errors
Transient errors (TransientError class) are used for temporary conditions that
may be resolved if the operation is retried.

The typical action is to retry the operation a number of times according to the configuration.
If the error remains it is converted to a static error.

10.5.2.2. Static errors
A static error (StaticError class) is an error that is not a temporary condition.

--- SUBPAGE: best_practices.html ---

# 11. Best Practices

## 11.1. IOServices sharing IOServer

It is often desirable to have multiple IOServices share the same IOServer process.
For this to work, the IOServices must be able to:

- share the same datacontext
share the same refresh strategy.
For instance, services that need the exact CID refresh strategy usually
need their own IOServer process.

Another consideration is whether some of the services are likely to trigger refreshes often,
and if that behavior is suboptimal for other services.

Also, IOServices that use the refresh_boundary feature should probably not be grouped with IOServices
that do not need it, mainly for performance reasons.

The total number of worker processes for all services should not be too high, as discussed below
in Number of worker processes.

## 11.2. Number of worker processes

If a service is slow the performance can be improved by adding another worker process to the service,
but this only works up to a certain point. When there are too many worker processes, the overhead of
forking after each refresh affects the performance, mainly the latency.
The best way to find a suitable worker pool size is to try different alternatives and measure performance.
It is possible to use the ioserverctl tool to modify the worker pool size, see IOServer control tool.

Note that there are services that cannot have more than one worker process. For example inbound
services with strict ordering requirements (incoming messages must be processed in order) and
also to trigger-based outbound services.

## 11.3. Services sharing worker

While individual services may benefit from larger worker pools, reducing the overall number of workers for
an IOServer is desirable, since it reduces resource usage.
This is especially true for services that needs to be constantly available, but only sporadically receive
messages. Defining such a service separately will force the IOServer to spawn workers for it on each new
generation, even though they are rarely used, causing unnecessary overhead.
IOServer provides the Dispatch feature, which groups low-frequency services together in
a “super-service”, which will share worker(s). This can reduce the total number of workers, while maintaining
service availability.

## 11.4. Pre-load of Rave tables

To improve performance, Rave tables used in the rule set should be pre-loaded.
Otherwise Rave loads them on demand in the worker processes, for each new worker generation.
It is much better to do this once in the main process.
See preload_tables for information.

To avoid degradation of performance over time, the Rave tables should be refreshed in the main process,
right after plan refresh. This behavior is controlled by the refresh_tables setting in the
datamodel section.

## 11.5. Running the same IOServices on different nodes

For load-balancing and availability reasons, it can be a good idea to run the same service in different
IOServer processes on different nodes. See High Availability.

## 11.6. Monitoring service deactivation

An IOService can be deactivated for a few different reasons:

- failure to process incoming messages, resulting in BlockingMsgErrors
- failure to execute handler, resulting in StaticErrors
- manually deactivated using ioserverctl, see IOServer control tool.

A service that is deactivated because of too many errors is restarted periodically,
see restart_attempt_interval, but in some cases the restart may never succeed without
manual intervention. For example if the error is caused by an incorrect message that has to be removed from the queue.
For this reason it is important that a monitoring system detects service deactivation and generates alerts or similar.
This can be done by looking at the IOServer log file, where the string “Deactivating service”
is written whenever an IOService is deactivated.

## 11.7. Worker time-out and pings

During normal operation a worker process pings the main process between calls to the handler,
and also pings repeatedly if the worker is idle for a while.

If a worker has not pinged within the configured worker time-out, see worker_time_out, the main
process prints a warning to the log file. After three missed pings in a row, the log message level is changed to error.

If some workers for a service have timed out, missed three pings in a row, the service is considered “degraded”.
If all workers for a service have timed out, the service is considered “unresponsive”.
If a timed out worker pings the main process, it is considered active again.
All these statuses can be viewed by using ioserverctl status or ioserverctl list.

There are two ways to avoid time-out of a worker:

- Set a long enough worker time-out so that it does not happen.
Have the handler code call the report_progress() method in ServiceContext periodically,
which makes the worker send pings to the main process.

A risk with setting a too long worker time-out is that the main process does not detect
a hanging worker process until the worker time-out has passed three times.

## 11.8. Handling of errors in IOService

The recommended way to handle errors is to catch all expected errors in the handler/trigger.
The service should convert it to an IOServer exception when appropriate.
Regarding logging the handler/trigger should log the errors on the level it sees fit and should not rely on the IOServer logging the error.

Unexpected exceptions can be ignored and IOServer will handle them according to configuration.

--- SUBPAGE: configuration.html ---

# 12. Configuration

The IOServer configuration uses the Common Configuration framework, where
each IOServer instance has its own process element within an IOServer program element.

Example of a configuration file:

&lt;program name=&quot;ioserver&quot;&gt;
  &lt;process name=&quot;ios_triphandler&quot;&gt;
    &lt;refresh&gt;
      &lt;strategy&gt;interval&lt;/strategy&gt;
      &lt;interval&gt;20&lt;/interval&gt;
      &lt;max_interval&gt;600&lt;/max_interval&gt;
    &lt;/refresh&gt;

    &lt;datamodel&gt;
      &lt;datacontext&gt;rs_ccp_n90_p90&lt;/datacontext&gt;
      &lt;ruleset&gt;ccp&lt;/ruleset&gt;
    &lt;/datamodel&gt;

    &lt;!-- Message retention can be configured on a per-process basis. --&gt;
    &lt;message_retention&gt;
      &lt;sink&gt;
        &lt;class&gt;qpid&lt;/class&gt;
        &lt;queue_reference&gt;message_retention&lt;/queue_reference&gt;
      &lt;/sink&gt;
    &lt;/message_retention&gt;

    &lt;ioservice name=&quot;TripHandler&quot;&gt;
      &lt;pattern&gt;
        &lt;class&gt;subscriber&lt;/class&gt;
        &lt;maxmsg&gt;1&lt;/maxmsg&gt;
        &lt;cacs_role&gt;crew_updater&lt;/cacs_role&gt;
        &lt;changereason&gt;OTHER&lt;/changereason&gt; &lt;!-- Change reason to use when saving. --&gt;
        &lt;username&gt;anonymous&lt;/username&gt; &lt;!-- User name to use when saving. --&gt;
      &lt;/pattern&gt;

      &lt;binding&gt;
        &lt;language&gt;python&lt;/language&gt;
        &lt;handler&gt;inbound.triphandler_ioserver.triphandler&lt;/handler&gt;
        &lt;protocol&gt;plain&lt;/protocol&gt;
        &lt;operation&gt;handle&lt;/operation&gt;
        &lt;profile&gt;false&lt;/profile&gt;
      &lt;/binding&gt;

      &lt;errors&gt;
        &lt;retrycount&gt;
          &lt;message&gt;3&lt;/message&gt;
        &lt;/retrycount&gt;

        &lt;blockmsg&gt;
          &lt;plan&gt;false&lt;/plan&gt;
          &lt;io&gt;true&lt;/io&gt;
          &lt;handling&gt;false&lt;/handling&gt;
          &lt;marshal&gt;false&lt;/marshal&gt;
        &lt;/blockmsg&gt;
      &lt;/errors&gt;

      &lt;source&gt;
        &lt;class&gt;qpid&lt;/class&gt;
        &lt;queue_reference&gt;inbound_trips&lt;/queue_reference&gt;
        &lt;prefetch&gt;100&lt;/prefetch&gt;
      &lt;/source&gt;

      &lt;sink&gt;
        &lt;class&gt;memory&lt;/class&gt;
        &lt;durable&gt;false&lt;/durable&gt;
        &lt;ttl&gt;120&lt;/ttl&gt; &lt;!-- Time-to-live in seconds --&gt;
      &lt;/sink&gt;

      &lt;!--
        Message retention can also be configured on a per-ioservice basis.
        This overrides the configuration on the process tag.
      --&gt;
      &lt;message_retention&gt;
        &lt;sink&gt;
          &lt;class&gt;qpid&lt;/class&gt;
          &lt;queue_reference&gt;TripHandler_message_retention&lt;/queue_reference&gt;
        &lt;/sink&gt;
      &lt;/message_retention&gt;

      &lt;hastore&gt;
        &lt;class&gt;consul&lt;/class&gt;
      &lt;/hastore&gt;

      &lt;persist_cid&gt;true&lt;/persist_cid&gt;

      &lt;worker_time_out&gt;30&lt;/worker_time_out&gt; &lt;!-- seconds --&gt;
      &lt;worker_pool_size&gt;1&lt;/worker_pool_size&gt;
    &lt;/ioservice&gt;
  &lt;/process&gt;
&lt;/program&gt;

The configuration details are explained in the following sub-sections.

## 12.1. program

The top node of the IOServer configuration is a program element with the
mandatory name ioserver. It contains one or more process elements.

## 12.2. process

A process element configures an IOServer process. It provides a process name and
contains global process configuration, such as refresh and datamodel,
as well as one or more ioservice elements.

A process element has the following attribute:

Attribute

Type

Mandatory

Description

name

string

Yes

Name of the process.
Must be unique for each host, i.e it is possible to have multiple
“ioserver_all” processes, but they must run on different hosts.

and can have the following sub-elements:

Sub-element

Type

Mandatory

Description

refresh

container

No

See the refresh element.

Default: Interval refresh strategy

refresh_rate

integer

No

Deprecated: please use the refresh element instead.

Maximum time interval in seconds between refreshes of the plan.

localtmpdir

string

No

Deprecated

servicecontrol

string

No

Deprecated

datamodel

container

Yes

See the datamodel element.

message_retention

container

No

See the message_retention element.

ioservice

container

Yes

See the ioservice element.

Note
The refresh_rate element is deprecated, use refresh instead.

## 12.3. refresh

IOServer refreshes the loaded plan according to one of the following strategies:

Interval refresh strategyThe plan is refreshed according to a given refresh interval.
If a refresh does not contain any changes the next interval is increased by a factor
2, until the maximum interval is reached or changes are detected in the plan. After that the interval is
reset to the configured or default interval. The absolute minimum refresh interval is one second.

Exact CID refresh strategyThe plan is refreshed to a specific commit ID needed by an incoming request.
This strategy can only be used by a single requestresponse service.

A refresh element can have the following sub-elements:

Sub-element

Type

Mandatory

Description

strategy

string

No

Refresh strategy to use.

Supported values: interval, exactcid

Default: interval

interval

integer

No

Time interval in seconds between refresh of the plan.
Only valid in interval refresh strategy.

Minimum: 1

Default: 20

max_interval

integer

No

Maximum time interval in seconds.
Only valid in interval refresh strategy.

Default: 120

## 12.4. datamodel

A datamodel element contains information about which data context to load, as well as which rule set
and parameter set.

A datamodel element can have the following sub-elements:

Sub-element

Type

Mandatory

Description

datacontext

string

Yes

Name of the data context to load.

domain

string

Yes

ARA domain to use.

Only certain combinations of this value and the planbuilder
value are supported, depending on the type of system:

For Atrium architecture, set domain to air2 and
planbuilder to mave2.

For Studio architecture (Major Release), set domain to
air1 and planbuilder to mave2.

planbuilder

string

Yes

See domain for how to set this value.

ruleset

string

No

Name of the rule set to use.

refresh_tables

boolean

No

Whether Rave tables should be updated after refresh (in the main
process). See also preload_tables.

Default: true

rulesettype

string

No

Deprecated

snapshotpath

string

No

Deprecated

mave_etables

boolean

No

Deprecated

parameterset

string

No

Name of the parameter set to use. Applies to all services
running in the IOServer instance, but can be overridden per
ioservice. See pattern section.

now

abstime

No

If specified, this value is used as fixed time and current
time refers to Rave only (only for testing purposes).

deadcount_now

boolean

No

If true, IOServer will reduce the number of requests to the
timeserver (by deadcounting the time since last poll).

Normally, this should be turned on, but in certain cases
(e.g. during testing), it may be necessary to poll the
timeserver more often - in that case set this to false.

Only applicable if the system is using a timeserver.
Default: true

nowupdateinterval

int

No

Deprecated

preload_tables

container

No

See the preload_tables element.

### 12.4.1. preload_tables

The preload_tables element lists Rave tables that should be pre-loaded.

Example of preload_tables configuration:

&lt;preload_tables&gt;
  &lt;table&gt;
    &lt;rave_name&gt;_topmodule.airport&lt;/rave_name&gt;
    &lt;external_name&gt;airport&lt;/external_name&gt;
  &lt;/table&gt;
  &lt;table&gt;
    &lt;rave_name&gt;crew.crew_rank_category&lt;/rave_name&gt;
    &lt;external_name&gt;crew_rank&lt;/external_name&gt;
  &lt;/table&gt;
&lt;/preload_tables&gt;

The preload_tables element contains one or more table elements,
which has the following sub-elements:

Sub-element

Type

Mandatory

Description

rave_name

string

Yes

Table name as defined in the rule set, including module name.
(_topmodule for tables in the top module).

external_name

string

Yes

Name of the underlying table, for example crew_rank.

## 12.5. db

A db element contains database information
and is often inherited from a global/default section, since it typically is shared
between a number of programs.

A db element has the following sub-elements:

Sub-element

Type

Mandatory

Description

connect

string

Yes

Connect string to the database.

schema

string

No

Schema to use in the database.

## 12.6. ioservice

An ioservice element configure a service handled by an IOServer process and contains
settings to control the number of worker processes and their lifetime.

An ioservice element has the following attribute:

Attribute

Type

Mandatory

Description

name

string

Yes

Name of the service.

and can have the following sub-elements:

Sub-element

Type

Mandatory

Description

worker_time_out

integer

No

Ping time-out of a worker process in seconds.
If a worker process has not pinged the main process in this time
a warning is written to the log. After three consecutive
missed pings, the log message is on error level.

Default: 60

worker_pool_size

integer

No

Maximum number of worker processes for the service.

Default: 1

persist_cid

boolean

No

Whether the current CID should be persisted between IOServer process
restarts.
Available for triggers and the exactcid refresh
strategy. Requires a hastore to store the persistent CID.

Default: false

restart_attempt_interval

integer

No

Time interval in seconds between restart attempts if the service fails.
Services that have been deactivated because of too many errors is by
default restarted periodically. 0 means that no restart attempts
are performed for the service.

Default: 300

enforce_latest_cid

boolean

No

Setting this to true enforces that a spawning worker knows about the
save of the last worker. If a worker spawn is prevented, a refresh
is triggered and a new spawn is attempted.
Note that enforce_latest_cid only works when worker_pool_size
is equal to 1.

Default: false

pattern

container

Yes

See the pattern element.

binding

container

Yes

See the binding element.

source

container

No

See the source element.

sink

container

No

See the sink element.

message_retention

container

No

See the message_retention element.

hastore

container

No

See the hastore element.

extra_indexes

container

No

See the extra_indexes element.

refresh_boundary

container

No

See the refresh_boundary element.

errors

container

No

See the errors element.

## 12.7. pattern

A pattern element configures the pattern of an IOService and can have the following sub-elements:

Sub-element

Type

Mandatory

Description

class

string

Yes

Pattern to use. The following are available:

- eventtrigger
- repeatingtrigger
- requestresponse
- subscriber
- timer
- trigger

maxmsg

integer

No

Number of messages to process in each chunk

Valid pattern: subscriber

Default: 1

savetimeout

integer

No

Maximum number of seconds until the plan is saved.

Valid pattern: subscriber

Default: 10

fetchtimeout

integer

No

Timeout in milliseconds when fetching messages from the message
source.

Valid patterns: requestresponse, subscriber

Default: 1000

cacs_role

string

No

CACS role to use for permission checking.
In the requestresponse pattern this value can be overridden
by the jcms_role message header.

Valid patterns: all except timer

changereason

string

No

Change reason to use when saving. Must be one of the values
defined in the change_reason table.

Valid patterns: all except timer

Default: “”

username

string

No

User name to use when saving.
In the requestresponse pattern this value can be overridden
by the jcms_client message header.

Valid patterns: all except timer

Default: unknown

skipconflict

boolean

No

Deprecated*: please use conflict_detection instead.

Whether to ignore state information in messages for conflict
detection purposes. It is still used to refresh the plan.

Valid patterns: requestresponse, subscriber

Default: true

conflict_detection

string

No

How to detect conflicts when saving.
Regardless of this setting, the jcms_state header is
used to refresh the plan when needed.

Valid patterns: all except timer

Supported values:

- disabled, no conflict detection
plan, conflict detection using the state of the
currently loaded plan.

message, conflict detection using the jcms_state header
in the message. If the header is not set, the state of the
currently loaded plan is used.
This options is not available for the trigger pattern.

Default: disabled

execution_pattern

string

No

Simplified cron-like expression to control when a timer executes.
See below for more details.

Valid patterns: timer, repeatingtrigger

Default: 0 0 0

delay

integer

No

Delay in seconds between each run (“repeatingtrigger”).

Default: 60

delay_from_start

boolean

No

Delay from the start of the previous run.

Valid pattern: repeatingtrigger

Default: false

run_if_no_changes

boolean

No

Whether to run even if there is no changes, that is,
when the change set is empty.

Valid pattern: repeatingtrigger

Default: false

run_on_change

boolean

No

Whether to run if time has passed or a change occurred, whatever
is earlier.

Valid pattern: repeatingtrigger

Default: false

parameterset

string

No

Override of the default parameter set for this service.

Valid patterns: all except timer

jcmsstatemessagereplace

container

No

See the jcmsstatemessagereplace element.

publish_changes

string

No

Whether the ioservice should publish changes on save.

Warning: Use of this parameter can cause unintended side
effects. Only use after consulting the Jeppesen core teams.

Valid patterns: all except timer

Default: true

An execution_pattern element text consists of three space-separated sub-strings denoting seconds,
minutes, and hours, respectively. Each sub-string should be either a wildcard or a comma-separated
list of integer values.

Examples:

Timer expression

Interval

* * *

every second

0 0,15,30,45 *

every 15 minutes

0 0 4

at 4 a.m. every morning

Note
Time is in localtime.

### 12.7.1. jcmsstatemessagereplace

A jcmsstatemessagereplace element configures how to update outgoing messages with the correct jcms
state and has the following sub-elements:

Sub-element

Type

Mandatory

Description

find

string

Yes

String matching the part of the outgoing message where to do the replacement.

replace

string

Yes

Part of the find string to replace with the jcms state. This
string is only allowed to occur once in the find string.

Example:

&lt;jcmsstatemessagereplace&gt;
  &lt;find&gt;jcms_state=&quot;0&quot;&lt;/find&gt;
  &lt;replace&gt;0&lt;/replace&gt;
&lt;/jcmsstatemessagereplace&gt;

An outgoing message is searched for the jcms_state=&quot;0&quot; string, and the 0 is replaced
by the correct jcms state.

## 12.8. binding

A binding element configures a handler or a trigger, and data binding. It can have the following sub-elements:

Sub-element

Type

Mandatory

Description

language

string

Yes

Programming language the handler or trigger is written in.
Currently only python is supported.

protocol

string

No

Message protocol to use.
The supported values are:

- soap, for a SOAP handler (with or without data binding)
- plain, for a plain text handler
- mixed, for a handler that accepts both SOAP and plain text

The protocol to use is determined per message by looking at the
content type of the incoming message.
The mixed option is only valid for a handler.

Default: soap

handler

string

Yes
(one of handler or trigger)

Python module that contains the handler code.
Exactly one handler or trigger element must be specified.

trigger

string

Yes
(one of handler or trigger)

Python module that contains the trigger code.
Exactly one handler or trigger element must be specified.

databinding

string

No

Python module that contains the PyXB-generated data binding code.
If this element is not specified, no data binding module is loaded and
the handler code is responsible for parsing the message.

operation

string

No

Name of the operation method to call in the handler.

Default: handle

profile

boolean

No

Whether profiling should be enabled for the handler/trigger code.
See profile.

Default: false

### 12.8.1. profile

If profiling is enabled then a &lt;random&gt;.pstat file is created for each call to the handler or trigger.
These files are put into the ${CARMTMP}/ioservice_profiling/&lt;service_name&gt; directory.

The join_pstats tool, which is delivered as part of the carmsys, can be used to merge all profile
output files in a directory into a single file.

Other tools can then be used to visualize the output.
A good one is [gprof2dot](https://github.com/jrfonseca/gprof2dot).

## 12.9. source

A source element specifies from where to fetch incoming messages.
The requestresponse pattern supports multiple sources, in which
case messages are read from the sources in a round robin fashion.

A source element can have the following sub-elements:

Sub-element

Type

Mandatory

Description

class

string

Yes

Type of source. Supported values are:

- qpid (Apache ActiveMQ)
- memory (internal memory queues, testing only)

queue_reference

string

Yes

Logical name of the queue to use.
See the ccf configuration for details.

prefetch

integer

No

For ActiveMQ, the prefetch capacity (number of messages)
of the receiver. By default prefetch is disabled. Consider
increasing if you are using enforce_latest_cid or have many
more messages than workers.

Default: 0

correlation_id

string

No

For qpid sources, information about each fetched message is
logged. If this element is not set, the correlation id of
the fetched message is part of the log. If this element is set,
the given message property is logged instead.

Default: “” (logs correlation id)

## 12.10. sink

A sink element specifies where to send outgoing messages.
It is possible to specify several sinks for a service; in which case all sinks must be given a
name.

A sink element has the following attribute:

Attribute

Type

Mandatory

Description

name

string

No
(Yes if multiple
sinks configured)

Name of the sink. Must be unique for each service.
The name sink is not allowed.

and the following sub-elements:

Sub-element

Type

Mandatory

Description

class

string

Yes

Type of sink. Supported values are:

- qpid (Apache ActiveMQ)
- memory (internal memory queues, testing only)

queue_reference

string

No

Logical name of the queue to use.
See the ccf configuration for details.

If not set, the request message needs to provide the reply_queue.

batch_size

integer

No

For ActiveMQ, the number of messages to buffer
before they are automatically committed.

If this parameter is set to 0, messages are
committed on handler/trigger success.

Note: Only enable this if the receiver can handle retransmitted
messages, that is, no transaction semantics is needed.

Default: 0

capacity

integer

No

For ActiveMQ, the sender capacity (number of messages).

If this parameter is set to 0, each message is
sent synchronously.

Default: 50

compress

boolean

No

Whether the message content should be compressed by using
gzip. If so, the message property uncompressed-size is
set to the uncompressed size of the message content. The message
encoding is also set to gzip.

Default: false

maxcontentsize

int

No

Maximum content size of the message in bytes, compressed or not.
If the size exceeds this limit, a MessageError is thrown.

Default: 0 (no check)

large_message_url

string

No

URL for upload of large messages. If a
message is considered large, as defined by the
large_message_size element, then the message content is
uploaded to this URL and the message property
DeferredContentUrl is set to a URL where the content can be
downloaded. The message that is sent has no content.

Default: “” (disabled).

large_message_size

int

No

The size of a large message in bytes.
This setting is only regarded if large_message_url is set.

Default: 1000000

durable

boolean

No

Whether messages written by this sink should be durable.
This value is used by default if the durable
property is not set on the IOMessage.

Default: false

ttl

int

No

The time-to-live in seconds of messages written by
the sink. This value is used by default if the ttl
property is not set on the IOMessage.

If this element is not set, the default value depends on
the value of the durable element in the following way.
If durable is false, or not set at all, the default
value is 3600 seconds (one hour). If durable is true, the
default value is 0 seconds, which means that the messages
never time out.

Default: 3600 or 0

default

boolean

No

Whether this is the default sink for the service.
That is, the sink used if the send method (without
sink) on the service context is used.

Default: false

Example (single sink):

&lt;sink&gt;
  &lt;class&gt;qpid&lt;/class&gt;
  &lt;queue_reference&gt;queueName&lt;/queue_reference&gt;
&lt;/sink&gt;

Example (multiple sinks):

&lt;sink name=&quot;sink1&quot;&gt;
  &lt;class&gt;qpid&lt;/class&gt;
  &lt;queue_reference&gt;queue1&lt;/queue_reference&gt;
  &lt;durable&gt;true&lt;/durable&gt;
  &lt;ttl&gt;120&lt;/ttl&gt;  &lt;!-- 2 minutes --&gt;
  &lt;default&gt;true&lt;/default&gt;
&lt;/sink&gt;
&lt;sink name=&quot;sink2&quot;&gt;
  &lt;class&gt;qpid&lt;/class&gt;
  &lt;queue_reference&gt;queue2&lt;/queue_reference&gt;
  &lt;durable&gt;true&lt;/durable&gt;
  &lt;ttl&gt;120&lt;/ttl&gt;  &lt;!-- 2 minutes --&gt;
&lt;/sink&gt;

## 12.11. message_retention

A message_retention element specifies how message retention is configured for this service
(or services if configured on the process tag).

For more details, see Message Retention.

It has the following sub-elements:

Sub-element

Type

Mandatory

Description

sink

container

Yes

See the sink element.

## 12.12. hastore

An hastore element specifies how persistent data should be stored.
Currently, this configuration is only needed by persist_cid.

An hastore element can have the following sub-elements:

Sub-element

Type

Mandatory

Description

class

string

Yes

Type of HA store. Supported values are:

- consul, Consul based storage.
database, Database based storage
(see below).

etcd, etcd based storage. Only
available in kubernetes.

- file, basic file based storage.

location

string

No
(Yes if class``=``file)

Path to file based HA store (file only).

The service name is used as part of the key for all HA values. This means that if a service is running
on multiple machines, they share the same HA store. A consul HA store uses
[Consul](https://www.consul.io/) to store HA values. This requires that a Consul service is running
on the same machine. An etcd HA store uses [etcd](https://etcd.io/) to store HA values.

A database HA store uses a database (Oracle or Postgres) to stora HA values.
It requires certain environment variables to be set:

- KV_DB_CONNECT_STRING - Dave database connect string.
- KV_DB_SCHEMA - Schema name.

The schema needs to exist and contain a table called store which has two columns:

- key - Primary key (string).
- val - Value (string).

Note that the HA store schema should not contain a dave model.

Example of Postgres SQL script that can be used to create the table:

CREATE TABLE store (
  key VARCHAR(1024) PRIMARY KEY,
  val TEXT NOT NULL
);

## 12.13. extra_indexes

An extra_indexes element adds indexes needed by the service to the model (only
supported for mave2). Within the extra_indexes element, each index has an
index element with the following sub-elements:

Sub-element

Type

Mandatory

Description

collection

string

Yes

Name of collection to add the index to.

property

string

Yes

Property to sort the index by. Several properties can be given.

Example:

&lt;extra_indexes&gt;
  &lt;index&gt;
    &lt;collection&gt;rotation&lt;/collection&gt;
    &lt;property&gt;adhoc&lt;/property&gt;
    &lt;property&gt;dt&lt;/property&gt;
  &lt;/index&gt;
  &lt;index&gt;
    &lt;collection&gt;crewmember&lt;/collection&gt;
    &lt;property&gt;givenname&lt;/property&gt;
  &lt;/index&gt;
&lt;/extra_indexes&gt;

## 12.14. refresh_boundary

A refresh_boundary element specifies that a refresh needs to be done in steps. If
there is data in any of the given collections, the refresh is done in
steps where the boundaries are the revisions with data in the collections.
This can be useful in some special cases of triggers.

A refresh_boundary element contains one or more collection elements,
which have the following sub-elements:

Sub-element

Type

Mandatory

Description

name

string

Yes

Name of collection/entity to use as a refresh boundary.
By adding two collections with the same name it is possible
to specify both true and false for inclusive.

inclusive

boolean

No

Whether to include the revision containing data for this
collection in the refresh.

Assume the following abbreviations:
C0: Commit before the revision containing data
C1: Commit at the revision containing data
LC: Last commit done

If false the commits C0 and LC are included in the
refresh.

If true the commits C1 and LC are included in the
refresh.

If true and false the commits C0, C1 and LC are
included in the refresh.

Default: false

bundle_program_name

string

No

Name of program where consecutive revisions shall be bundled
into the same change set for this collection. The program
name refer to what is stored in the cliprogram column
in the dave_revision table.

If multiple bundle_program_name are specified, revisions
matching any of the programs will be bundled together.

Example:

&lt;refresh_boundary&gt;
  &lt;collection&gt;
    &lt;name&gt;publ_hold_period&lt;/name&gt;
    &lt;inclusive&gt;false&lt;/inclusive&gt;
    &lt;bundle_program_names&gt;
      &lt;bundle_program_name&gt;CrewExchange&lt;/bundle_program_name&gt;
    &lt;/bundle_program_names&gt;
  &lt;/collection&gt;
  &lt;collection&gt;
    &lt;name&gt;crew_pend_publ_status&lt;/name&gt;
    &lt;inclusive&gt;true&lt;/inclusive&gt;
  &lt;/collection&gt;
  &lt;collection&gt;
    &lt;name&gt;crew_pend_publ_status&lt;/name&gt;
    &lt;inclusive&gt;false&lt;/inclusive&gt;
  &lt;/collection&gt;
&lt;/refresh_boundary&gt;

## 12.15. errors

An errors element configures the error handling strategy for the service and
has the following sub-elements:

- retrycount, which specifies the number of retries to perform
blockmsg, which defines whether transient message errors shall be converted to
BlockingMsgError or SkipMsgError when the retry attempts have been exhausted.

### 12.15.1. retrycount

A retrycount element specifies the number of times to retry a message in the event of an transient
message error. The element has the following sub-elements:

Sub-element

Type

Mandatory

Description

local

integer

No

Number of retry attempts to execute in the worker process in the event
of a transient error. A local refresh will be performed between attempts.
Only relevant for requestresponse pattern, other patterns do not
retry in the worker process.

Default: 0

system

integer

No

Number of retry attempts to execute in the main process for transient
non message-specific errors.

Default: 3

message

integer

No

Number of retry attempts to execute in the main process for transient
message errors.

Default: 3

### 12.15.2. blockmsg

A blockmsg element specifies what to do with a transient message error if the number of retry
attempts have been exhausted. By default it is converted to a SkipMsgError error, but it is
possible to define cases where it is converted to a BlockingMsgError error instead.
The requestresponse pattern ignores this setting and converts transient message errors to
SkipMsgErrors when the retry attempts have been exhausted.

A blockmsg element has the following sub-elements:

Sub-element

Type

Mandatory

Description

handling

boolean

No

Whether transient message errors raised in the handler should be
converted to blocking message errors.

Default: false (SkipMsgError)

plan

boolean

No

Whether transient message errors raised during plan handling, such as
save, should be converted to blocking message errors.

Default: false (SkipMsgError)

io

boolean

No

Whether transient message errors raised during I/O operations, fetching
from queues etc., should be converted to blocking message errors.

Default: false (SkipMsgError)

marshal

boolean

No

Whether transient message errors raised during marshalling should be
converted to blocking message errors.

Default: false (SkipMsgError)

## 12.16. dispatch

For a description of the Dispatch feature, see Dispatch.

A dispatch element configures the mapping between queues and handlers, default sink and how error messages
should be formatted. This element is only applicable in an ioservice configuration section where the handler
has been defined as jcms.ioserver.version&lt;N&gt;.dispatch_handler.

Sub-element

Mandatory

Attribute

Type

Mandatory

Description

map

Yes

header

string

Yes

Name of the message header that the dispatch hander
should look at to decide which handler to call.
The header jcms_source_queue is set by IOServer
to the queue reference that the message came in on.

value

string

Yes

The value IOServer should match on. If
jcms_source_queue is used, this is the queue
reference.

handler

string

Yes

Name of the handler to use.

sink

string

Yes

Name of the sink to use. Note that this is the
name of the sink, not the sink’s queue reference.

service_name

string

No

Jcmslog MDC service name to use for this handler.
Default: handler attribute value.

default

No

handler

string

Yes

Name of the handler to use if no match was found in
the mapping.

sink

string

Yes

Name of sink to use by the default handler. This
sink is also used to send out error messages
generated by the dispatch handler itself.

service_name

string

No

Jcmslog MDC service name to use for this handler.
Default: handler attribute value.

Example of a configuration file:

&lt;program name=&quot;ioserver&quot;&gt;
   &lt;process name=&quot;ios_triphandler&quot;&gt;
      &lt;ioservice name=&quot;TripHandler&quot;&gt;
         &lt;pattern&gt;
            &lt;class&gt;requestresponse&lt;/class&gt;
            &lt;cacs_role&gt;myRole&lt;/cacs_role&gt;
         &lt;/pattern&gt;

         &lt;binding&gt;
            &lt;language&gt;python&lt;/language&gt;
            &lt;handler&gt;jcms.ioserver.version10.dispatch_handler&lt;/handler&gt;
            &lt;protocol&gt;plain&lt;/protocol&gt;
         &lt;/binding&gt;

         &lt;dispatch&gt;
            &lt;map header=&quot;jcms_source_queue&quot; value=&quot;handlerA.source&quot;
                 handler=&quot;dispatcher.handlerA&quot;
                 sink=&quot;handlerA.sink.name&quot; /&gt;
            &lt;map header=&quot;jcms_source_queue&quot; value=&quot;handlerB.source&quot;
                 handler=&quot;dispatcher.handlerB&quot;
                 sink=&quot;handlerB.sink.name&quot;
                 service_name=&quot;mapped_B&quot;/&gt;
            &lt;map header=&quot;jcms_source_queue&quot; value=&quot;handlerC.source&quot;
                 handler=&quot;dispatcher.handlerC&quot;
                 sink=&quot;handlerC.sink.name&quot; /&gt;
            &lt;default handler=&quot;dispatcher.handlerB&quot;
                     sink=&quot;default.sink.name&quot;
                     service_name=&quot;default_B&quot;/&gt;
         &lt;/dispatch&gt;

         &lt;source&gt;
            &lt;class&gt;memory&lt;/class&gt;
            &lt;queue_reference&gt;handlerA.source&lt;/queue_reference&gt;
         &lt;/source&gt;

         &lt;source&gt;
            &lt;class&gt;memory&lt;/class&gt;
            &lt;queue_reference&gt;handlerB.source&lt;/queue_reference&gt;
         &lt;/source&gt;

         &lt;source&gt;
            &lt;class&gt;memory&lt;/class&gt;
            &lt;queue_reference&gt;handlerC.source&lt;/queue_reference&gt;
         &lt;/source&gt;

         &lt;sink name=&quot;handlerA.sink.name&quot;&gt;
            &lt;class&gt;memory&lt;/class&gt;
            &lt;queue_reference&gt;handlerA.sink&lt;/queue_reference&gt;
         &lt;/sink&gt;

         &lt;sink name=&quot;handlerB.sink.name&quot;&gt;
            &lt;class&gt;memory&lt;/class&gt;
            &lt;queue_reference&gt;handlerB.sink&lt;/queue_reference&gt;
         &lt;/sink&gt;

         &lt;sink name=&quot;handlerC.sink.name&quot;&gt;
            &lt;class&gt;memory&lt;/class&gt;
            &lt;queue_reference&gt;handlerC.sink&lt;/queue_reference&gt;
         &lt;/sink&gt;

         &lt;sink name=&quot;default.sink.name&quot;&gt;
            &lt;default&gt;true&lt;/default&gt;
            &lt;class&gt;memory&lt;/class&gt;
            &lt;queue_reference&gt;default.sink&lt;/queue_reference&gt;
         &lt;/sink&gt;
      &lt;/ioservice&gt;
   &lt;/process&gt;
&lt;/program&gt;

## 12.17. Dispatch Scenario

For a description of the Dispatch Scenario feature, see
Dispatch Scenario and Dispatch.

A custom_attributes element configures the scenario server url and
the optional overriden values for datacontext and ruleset name. This
element is only applicable in an ioservice configuration section where
the handler has been defined as jcms.ioserver.version10.dispatch_scenario_handler.

Sub-element

Mandatory

Type

Description

scenario_server_url

Yes

string

The url of the scenario server that will store the
scenario.

scenario_datacontext

No

string

Alternative datacontext to be saved with the
scenario. Default is to use the same datacontext as
is loaded in the ioserver.

scenario_ruleset

No

string

Alternative ruleset name to be saved with the
scenario. Default is to use the same ruleset name as
is loaded in the ioserver.

Example of a configuration file:

&lt;program name=&quot;ioserver&quot;&gt;
   &lt;datamodel&gt;
     &lt;datacontext&gt;IOServer&lt;/datacontext&gt;
     &lt;ruleset&gt;jct&lt;/ruleset&gt;
     &lt;rulesettype&gt;rave&lt;/rulesettype&gt;
     &lt;parameterset&gt;default&lt;/parameterset&gt;
     &lt;mave_version&gt;mave2&lt;/mave_version&gt;
     &lt;domain&gt;air2&lt;/domain&gt;
     &lt;planbuilder&gt;mave2&lt;/planbuilder&gt;
   &lt;/datamodel&gt;

   &lt;process name=&quot;ios_dispatch_handler_service&quot;&gt;
      &lt;ioservice name=&quot;scenario&quot;&gt;
         &lt;pattern&gt;
           &lt;class&gt;requestresponse&lt;/class&gt;
           &lt;cacs_role&gt;interface&lt;/cacs_role&gt;
           &lt;username&gt;ioservice_scenario&lt;/username&gt;
         &lt;/pattern&gt;

         &lt;binding&gt;
           &lt;language&gt;python&lt;/language&gt;
           &lt;handler&gt;jcms.ioserver.version10.dispatch_scenario_handler&lt;/handler&gt;
           &lt;protocol&gt;plain&lt;/protocol&gt;
         &lt;/binding&gt;

         &lt;custom_attributes&gt;
           &lt;scenario_server_url&gt;%(API/getServiceUrl/scenarioserver)&lt;/scenario_server_url&gt;
           &lt;scenario_datacontext&gt;Tracking&lt;/scenario_datacontext&gt; &lt;!-- override IOServer datacontext when saving scenario --&gt;
           &lt;scenario_ruleset&gt;jct_opt&lt;/scenario_ruleset&gt; &lt;!-- override jct ruleset when saving scenario --&gt;
         &lt;/custom_attributes&gt;

         &lt;dispatch&gt;
           &lt;map header=&quot;jcms_source_queue&quot;
                value=&quot;to.ioservice.scenario.FlightInput_5_soap&quot;
                handler=&quot;ioservice_impl.FlightInput_5_soap_handler&quot; /&gt;
         &lt;/dispatch&gt;

         &lt;source&gt;
           &lt;class&gt;qpid&lt;/class&gt;
           &lt;queue_reference&gt;to.ioservice.scenario.FlightInput_5_soap&lt;/queue_reference&gt;
         &lt;/source&gt;

         &lt;sink&gt;
           &lt;class&gt;qpid&lt;/class&gt;
         &lt;/sink&gt;
      &lt;/ioservice&gt;
   &lt;/process&gt;
&lt;/program&gt;

--- SUBPAGE: starting_ioserver.html ---

# 13. Command-line arguments

The synopsis is:

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

--- SUBPAGE: cmsshell.html ---

# 14. Cmsshell integration

IOServer provides both a cmsshell plugin and self tests that can
be run with cmsshell selftest command.

## 14.1. cmsshell plugin

The plugin provided by IOServer can be accessed by using
the prefix ioserver in cmsshell.

### 14.1.1. help

Prints a help text with the available commands.

### 14.1.2. clear_hastore

This command clears the HA store for a specific service if an argument is provided.
Otherwise it will clear the ha store for all services on all processes.

Argument

Mandatory

Description

--service=service_name

No

Delete HA store only for the provided IOService.

### 14.1.3. list_config

This command lists the configuration for a specific service if an argument is provided.
Otherwise it will list the configuration for all services on all processes,
regardless the node the are run on.

Argument

Mandatory

Description

--service=service_name

No

List configuration only for the provided IOService.

### 14.1.4. selftest

Run the IOServer self tests.

### 14.1.5. service

Execute an ioserverctl command for the specified service on all IOServer instances.
For start and stop the command will  wait for the service to be up/down and show final status before returning the prompt.

Argument

Mandatory

Description

service

Yes

Name of the service to affect,
as retrieved from e.g. list_config

command

Yes

The command to run.

- start: Will enable the service.
- stop: Will disable the service.
- status: prints the status of the service.

--wait=timeout

No

Set the time to wait before timeout.
Default: 5s

## 14.2. Self tests

Run tests to try to verify that the IOServers are functioning properly.

### 14.2.1. Queues

Validate that the IOServer and ccf configuration is consistent.

### 14.2.2. Processes

Verify that all processes configured to run on this node are running.

### 14.2.3. Services

Verify that all configured services are running and are in active state.

--- SUBPAGE: ioserver_control_tool.html ---

# 15. IOServer control tool

## 15.1. Purpose

The ioserverctl tool is used to control and list the services run by an IOServer.

## 15.2. Command-line arguments

The synopsis is:

Usage:
  ioserverctl [options] [-p process-name] start [-s service-name]
  ioserverctl [options] [-p process-name] stop [-s service-name]
  ioserverctl [options] [-p process-name] status [-s service-name]
  ioserverctl [options] [-p process-name] clear-statistics [-s service-name]
  ioserverctl [options] [-p process-name] set-workers [-s service-name] &lt;pool-size&gt;
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
    -t &lt;seconds&gt;, --timeout=&lt;seconds&gt;
        Command timeout in seconds (default: 30)
        a timeout of -1 blocks indefinitely.
    -j, --json
        Generate single-line JSON output suitable for parsing by other programs
        (default is a human-readable plain-text format)
    -J, --json-multiline
        Generate multi-line JSON output
        (default is a human-readable plain-text format)
    -p &lt;process name&gt;, --process &lt;process name&gt;
        Specify the process on which the action should be performed.
        The process name must be defined in the configuration.
        If no process is specfied the action will be performed on all IOServers.
    -s &lt;service name&gt;, --service &lt;service name&gt;
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

    set-workers [-p process-name] [-s service-name] &lt;pool-size&gt;
        Set the size of the specified IOService&#39;s worker-pool on the specified process.
        The pool size must be larger than zero.

    getcid [-p process-name]
        Get latest generation (cid) loaded in the specified IOServer main.

    list [-p process-name]
        List configured IOServices with status information for specified IOServer.

    refresh [-p process-name]
        Request IOServer to refresh the plan.

## 15.3. Examples

Get a list of all services in the ioserver_all process:

ioserverctl -p ioserver_all list

Get a list of all services for all IOServer processes on node:

ioserverctl list

Get the current plan generation in the ioserver_all process:

ioserverctl -p ioserver_all getcid

Check the status for the crew_checkin service in the ioserver_all process:

ioserverctl -p ioserver_all status -s crew_checkin

Check the status for two of the services in the ioserver_all process:

ioserverctl -p ioserver_all status -s crew_checkin -s roster_in

Check the status for all services in the ioserver_all process:

ioserverctl -p ioserver_all status

Clear the statistics for the crew_checkin service in the ioserver_all process:

ioserverctl -p ioserver_all clear-statistics -s crew_checkin

Clear the statistics for two of the services in the ioserver_all process:

ioserverctl -p ioserver_all clear-statistics -s crew_checkin -s roster_in

Clear the statistics for all services in the ioserver_all process:

ioserverctl -p ioserver_all clear-statistics

Deactivate the crew_checkin service in the ioserver_all process:

ioserverctl -p ioserver_all stop -s crew_checkin

Reactivate the crew_checkin service in the ioserver_all process:

ioserverctl -p ioserver_all start -s crew_checkin

Reactivate all services in the ioserver_all process:

ioserverctl -p ioserver_all start

Change the worker pool size to five workers for the crew_checkin service in the ioserver_all process:

ioserverctl -p ioserver_all set-workers -s crew_checkin 5

Tell the ioserver_all process to refresh:

ioserverctl -p ioserver_all refresh

Tell all ioserver processes on the current node to to refresh:

ioserverctl refresh

--- SUBPAGE: python_api_reference.html ---

# 16. IOServer Python API reference

API reference for the IOServer public python interface.
Used by handlers and triggers.

## 16.1. IOServer Python API Reference Version 10

16.1.1. jcms.ioserver.versions
16.1.2. jcms.ioserver.constants
16.1.3. jcms.ioserver.exceptions
16.1.4. jcms.ioserver.version10.config
16.1.5. jcms.ioserver.version10.actions
16.1.6. jcms.ioserver.version10.message
16.1.7. jcms.ioserver.version10.context
16.1.8. jcms.ioserver.version10.mave2.IPlanHolder

## 16.2. IOServer Python API Reference Version 9

16.2.1. jcms.ioserver.versions
16.2.2. jcms.ioserver.constants
16.2.3. jcms.ioserver.exceptions
16.2.4. jcms.ioserver.version9.config
16.2.5. jcms.ioserver.version9.actions
16.2.6. jcms.ioserver.version9.message
16.2.7. jcms.ioserver.version9.context
16.2.8. jcms.ioserver.version9.mave2.IPlanHolder

# 17. Testutils Python API reference

API reference for the Testutils public python interface.
Used for developing and testing of handlers and triggers.

## 17.1. TestUtils Python API Reference Version 10

17.1.1. Conflict Detection Strategy Constants
17.1.2. jcms.ioserver.testutils.version10.main.TestMain
17.1.3. jcms.ioserver.testutils.version10.main.IMemoryHAStore
17.1.4. jcms.ioserver.testutils.version10.main.IMemoryQueue
17.1.5. jcms.ioserver.testutils.version10.main.ITestConfig
17.1.6. jcms.ioserver.testutils.version10.TestRunner

## 17.2. TestUtils Python API Reference Version 9

17.2.1. jcms.ioserver.testutils.version9.main.TestMain
17.2.2. jcms.ioserver.testutils.version9.main.IMemoryHAStore
17.2.3. jcms.ioserver.testutils.version9.main.IMemoryQueue
17.2.4. jcms.ioserver.testutils.version9.main.ITestConfig
17.2.5. jcms.ioserver.testutils.version9.TestRunner

--- SUBPAGE: python_api_ver10_reference.html ---

# 16.1.1. jcms.ioserver.versions

This module defines the supported Python Interface Versions.

All handlers and triggers must implement the method handler_interface_version()
that returns one of these values.

The PlanHolder and context objects provided to the handler/trigger will be adopted to the version in
which the service is implemented.

class jcms.ioserver.versions.InterfaceVersion
Specifies the version of the interface used in the handler or trigger implementation.

NINE = 9
Interface version 9, introduced in IOServer version 28.0.0

TEN = 10
Interface version 10, introduced in IOServer version 33.0.0

# 16.1.2. jcms.ioserver.constants

This module defines the public constants that handlers and triggers have access to.

class jcms.ioserver.constants.PropertyNames
Names of predefined message properties.

SOAP_ACTION = 'SOAPAction'
The soap action contains the name of the SOAP operation, format urn:&lt;operation&gt;.

STATE_REFERENCE = 'jcms_state'
The state header contains the JCMS state reference CID if any.

USER_ATTRIBUTES = 'jcms_attributes'
The user attribute header contains the security attributes.

# 16.1.3. jcms.ioserver.exceptions

exception jcms.ioserver.exceptions.BlockingMsgError(description='', source_exc_type=None)
A non-transient error in message that cannot be skipped

exception jcms.ioserver.exceptions.DatabaseConflictError(description='', source_exc_type=None)
An error caused by a database conflict trigger.

exception jcms.ioserver.exceptions.DatabaseDataTooOldError(description='', source_exc_type=None)
An error caused by a database data too old conflict.

exception jcms.ioserver.exceptions.FormatterError(description='', source_exc_type=None)
A problem in message formatting or output validation.

exception jcms.ioserver.exceptions.IOSError(description='', source_exc_type=None)
Base class for IOServer exceptions.

__init__(description='', source_exc_type=None)

get_description()

Returns:
the error description.

get_error_code()

Returns:
the error code.

exception jcms.ioserver.exceptions.MarshallingError(description='', source_exc_type=None)
Base class for Marshalling exceptions.

__init__(description='', source_exc_type=None)

exception jcms.ioserver.exceptions.MessageError(description='', source_exc_type=None)
An error caused by incorrect information or syntax in a message.

exception jcms.ioserver.exceptions.ParserError(description='', source_exc_type=None)
A problem in message parsing or input validation.

exception jcms.ioserver.exceptions.SendError(description='', source_exc_type=None)
An error caused by failure to send or acknowledge a message.

exception jcms.ioserver.exceptions.SkipMsgError(description='', source_exc_type=None)
A non-transient error in a message that can be skipped.

exception jcms.ioserver.exceptions.StaticError(description='', source_exc_type=None)
A non-transient error condition in the system as opposed to the message.

exception jcms.ioserver.exceptions.SystemError(description='', source_exc_type=None)
An error condition in the IOServer system as opposed to the message.

exception jcms.ioserver.exceptions.TransientError(description='', source_exc_type=None)
An error caused by a possibly temporary condition in the system.

exception jcms.ioserver.exceptions.TransientMsgError(description='', source_exc_type=None)
An error caused by a possibly temporary condition in the message.

# 16.1.4. jcms.ioserver.version10.config

## 16.1.4.1. IConfig

class jcms.ioserver.version10.config.IConfig(*args, **kwargs)¶
Provides access to the IO-server configuration.

The ioserver configuration is organized in global (per process) and service level configuration groups. A configuration group is a set of values (and potentially subgroups) that can be fetched by name. In the jcms configuration file syntax a configuration group corresponds to a tag that has complex content, while a value is a tag with only string content.

The IConfig interface encapsulates the lookup logic and override hierarchy within the configuration and provides the values that are effective for this ioserver instance. Lookups with a service-specific group tag will provide the effective value for that service and sub-group, standard fallback logic to process-global and global-default values is handled by the config implementation.

Components should lookup the values they need within their provided configuration group using getConfigValue(group, key, defvalue) or the typed equivalents.

__init__(*args, **kwargs)¶

getConfigAttribute(group, attribute, defValue)¶
Get a configuration attribute with given key within a group.

Parameters:

- group – the group key of the requested configuration group
- attribute – the name of the configuration attribute to fetch
- defValue – a fallback value to use if no configuration is found

Returns:
the value of the configuration attribute if found, defValue else

Types
- Parameter group: std ::string
- Parameter attribute: std ::string
- Parameter defValue: std ::string
- Return type: std ::string

getConfigAttributes(group)¶
Get all configuration attributes, including values, within a group.

Any “name” attributes are ignored as the configuration API handles them separately.

Parameters:
group – the group key of the requested configuration group

Returns:
map of attribute name to attribute value.

Types
- Parameter group: std ::string
- Return type: StringMap

getConfigBool(group, key, defValue)¶
helper to fetch boolean value

find the configuration value and convert it to a boolean. A value of “true” is regarded true, all other values are false.

Parameters:

- group – the group key of the requested configuration group
- key – the configuration key (within the group)
- defValue – a fallback value to use if no configuration is found

Returns:
the value of the configuration property if its found, defValue else

Types
- Parameter group: std ::string
- Parameter key: std ::string
- Parameter defValue: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: [bool](https://docs.python.org/3/library/functions.html#bool)

getConfigInt(group, key, defValue)¶
helper to fetch integer value

find the configuration value and convert it to an integer.
getConfigValue(const std::string&amp;, const std::string&amp; ,const std::string&amp; )

Parameters:

- group – the group key of the requested configuration group
- key – the configuration key (within the group)
- defValue – a fallback value to use if no configuration is found

Returns:
the value of the configuration property if its found, defValue else

Raises:
ioserver.base.ConfigurationError – if the value doesn’t convert to int

Types
- Parameter group: std ::string
- Parameter key: std ::string
- Parameter defValue: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getConfigSubGroup(parentGroup, groupTag, name)¶
provide the lookup key for a detailed ioserver configuration group

Parameters:

- parentGroup – the group key of the requested configuration group
- groupTag – the tag of the configuration group, like “db” or “datamodel”
- name – the name of an instance of the configuration group if there can be more than one

Returns:
the group key to use for lookups of configuration in that group

Types
- Parameter parentGroup: std ::string
- Parameter groupTag: std ::string
- Parameter name: std ::string
- Return type: std ::string

getConfigValue(group, key, defValue)¶
lookup a configuration value with given key within a group

Each component has a configuration group provided in the constructor and should call the method with that group. Global settings directly defined on the process level can get fetched with an empty group.

Parameters:

- group – the group key of the requested configuration group
- key – the name of the configuration value to fetch
- defValue – a fallback value to use if no configuration is found

Returns:
the value of the configuration property if found, defValue else

Types
- Parameter group: std ::string
- Parameter key: std ::string
- Parameter defValue: std ::string
- Return type: std ::string

getGlobalConfigGroup(groupTag, name)¶
provide the lookup key for a ioserver global configuration group

Use this method to get a group key for process-global settings.

Parameters:

- groupTag – the tag of the configuration group, like “db” or “datamodel”
- name – the name of an instance of the configuration group if there can be more than one, otherwise empty

Returns:
the group key to use for lookups of configuration in that group

Types
- Parameter groupTag: std ::string
- Parameter name: std ::string
- Return type: std ::string

getGlobalGroupNames(groupTag)¶
get the list of all names for parallel global configuration groups with same tag

Parameters:
groupTag – the tag of the configuration group, like “db” or “datamodel”

Types
- Parameter groupTag: std ::string
- Return type: StringVectorPointer

getPortBase()¶
Get the portbase.

Returns:
the portbase number, -1 on error

Types
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getProcessName()¶
Get the proccess name.

Returns:
the name of the process

Types
- Return type: std ::string

getProcessServicePort(*args)¶
Get the service port to use for the process when communicating with sysmond.

Parameters:

- systemService – The system service to look up
- hostName – The host name to look up (default: use the current host name)
- processName – The process name (default: use the current process name)

Returns:
port number to the service or -1 if the service cannot be found

Types
- Parameter systemService: std ::string
- Parameter hostName: std ::string
- Parameter processName: std ::string
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getProcessServiceUrl(*args)¶
get the service URL for a given system service

Parameters:

- systemService – The system service to look up
- hostName – The host where to look for the service. Empty string means localhost. Default is empty string.
- processName – The name of the process which provides the service. Empty string means use the process name which was given when calling the constructor (in this class).

Returns:
URL with the format service://host:port or empty string if service is not found.

Types
- Parameter systemService: std ::string
- Parameter hostName: std ::string
- Parameter processName: std ::string
- Return type: std ::string

getServiceConfigGroup(service, groupTag, name)¶
provide the lookup key for a ioserver service local configuration group

Use this method to get a group key for service specific settings.

Parameters:

- service – the name of the service
- groupTag – the tag of the configuration group, like “pattern” or “source”
- name – the name of an instance of the configuration group if there can be more than one, otherwise empty

Returns:
the group key to use for lookups of configuration in that group

Types
- Parameter service: std ::string
- Parameter groupTag: std ::string
- Parameter name: std ::string
- Return type: std ::string

getServiceGroupNames(service, groupTag)¶
get the list of all names for parallel service configuration groups with same tag

Parameters:

- service – the name of the service
- groupTag – the tag of the configuration group, like “pattern” or “source”

Types
- Parameter service: std ::string
- Parameter groupTag: std ::string
- Return type: StringVectorPointer

getServiceNames()¶
get the list of all service names

Types
- Return type: StringVectorPointer

getSubGroupNames(parentGroup, groupTag)¶
get the list of all names for parallel configuration groups

Types
- Parameter parentGroup: std ::string
- Parameter groupTag: std ::string
- Return type: StringVectorPointer

getSubGroups(parentGroup, groupTag)¶
get the list of all groups for parallel configuration groups

Types
- Parameter parentGroup: std ::string
- Parameter groupTag: std ::string
- Return type: StringVector

getenv(key, defValue)¶
get the value of an environment variable

Parameters:

- key – the name of the variable to fetch
- defValue – a fallback value to use if the variable is not set

Returns:
the value of the environment variable if set, otherwise defValue

Types
- Parameter key: std ::string
- Parameter defValue: std ::string
- Return type: std ::string

# 16.1.5. jcms.ioserver.version10.actions

This module defines the action codes that version TEN handlers can return.

## 16.1.5.1. PlanAction

class jcms.ioserver.version10.actions.PlanAction¶
Version 10 Handler actions. Specifies what the pattern should do when a handler returns.
Return value from handler methods.

ROLLBACK = 2¶
Roll back the modifications in the plan.

SAVE = 0¶
Save the current state of the plan.

UNCHANGED = 1¶
The plan does not need to be saved.

## 16.1.5.2. FaultAction

class jcms.ioserver.version10.actions.FaultAction¶
Version 10 Fault actions. Specifies what the pattern should respond when an exception is raised.
Return value from the on_fault method in the handler module.

DEFAULT_RESPONSE = 0¶
Create a default error response message. Only supported for SOAP messages.

NO_RESPONSE = 1¶
Do not send a response.

SEND_RESPONSE = 2¶
Send the response message that the handler module has produced.

# 16.1.6. jcms.ioserver.version10.message

This module defines the Message classes available to version TEN handlers/triggers.

## 16.1.6.1. PlainIOMessage

class jcms.ioserver.version10.message.PlainIOMessage(io_message, pyxb_binding=None, skipMsgOnMarshalError=True)¶
IOMessage with plain text or XML content.

__init__(io_message, pyxb_binding=None, skipMsgOnMarshalError=True)¶

property content¶
Get or set the message content.

property content_type¶
Get or set the message content-type.

classmethod create_io_message(content, contentType=None, encoding=None, msgId=None)¶
Factory method for creating a Plain IOMessage.

Parameters:

- content ([bytes](https://docs.python.org/3/library/stdtypes.html#bytes)) – the message content
- contentType ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the type of the content, can be e.g. text or binary
- encoding ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the text encoding used
- msgId ([str](https://docs.python.org/3/library/stdtypes.html#str)) – id for the message

Returns:
IOMessage SWIG object without wrapper

property encoding¶
Get or set the message encoding.

property full_message_text¶

Returns:
full text of the message.

classmethod get_default_content_type()¶
Default content type for new messages.

get_meta()¶
Get message retention business context metadata.

get_properties()¶
Get the message properties.
The properties are copied into a dict(str:str)

Returns:
dictionary of properties

get_property(key, default='')¶
Get the message property by key.

Parameters:

- key ([str](https://docs.python.org/3/library/stdtypes.html#str)) – property key
- default ([str](https://docs.python.org/3/library/stdtypes.html#str)) – default value used if property does not exist.

Returns:
value of the property based on key

classmethod get_system_encoding()¶

Returns:
the system character encoding name

get_user_attributes()¶
Get user attributes as a dict.

Returns:
dictionary containing user attributes

property id¶
Get or set the message Id.

property meta_enabled¶
Get message retention enabled status.

If the value is true, then a message retention message will be sent on the message retention sink,
if one is configured for the ioservice.

pyxb_encoding = 'utf-8'¶

set_meta(meta)¶
Set message retention business context metadata.

The value must be JSON compatible.

Parameters:
meta ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – message retention business context metadata.

set_property(key, value)¶
Set a message property by key.

Parameters:

- key ([str](https://docs.python.org/3/library/stdtypes.html#str)) – property key
- value ([str](https://docs.python.org/3/library/stdtypes.html#str)) – set the property to this value

# 16.1.7. jcms.ioserver.version10.context

This module defines the context interface for version TEN.

## 16.1.7.1. OnLoadServiceContext

class jcms.ioserver.version10.context.OnLoadServiceContext(service_name, swigged_config)¶
A context that provides basic information to the handlers on_load method.

__init__(service_name, swigged_config)¶

property config¶

Returns:
IOServer configuration (IConfig)

property service_logger¶
Return a jcms logger that contains the service name
e.g. ioserver.service_name.service.

Returns:
Logger instance

property service_name¶

Returns:
the name of the service

## 16.1.7.2. ServiceContext

class jcms.ioserver.version10.context.ServiceContext(swig_service_context, is_soap=False, binding_module=None, skipMsgOnMarshalError=False)¶

__init__(swig_service_context, is_soap=False, binding_module=None, skipMsgOnMarshalError=False)¶

property config¶

Returns:
IOServer configuration (IConfig)

create_io_message(content, contentType=None, encoding=None, msgId=None)¶
Create a new IOMessage from the complete content.

Parameters:

- content ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the full message text (including envelope if its soap)
- contentType ([str](https://docs.python.org/3/library/stdtypes.html#str)) – content type for the new message, if omitted a message type

dependent default will be used
:param str encoding: encoding for the new message, if omitted system encoding will be used
:param str msgId: the message id for the new message, if omitted an UUID will be generated
:return: a Python wrapped IOMessage (PlainIOMessage or
SoapIOMessage)

create_io_message_from_content(content, encoding=None, msgId=None)¶
Create a new IOMessage from the payload text. A message type dependent default will be used.

Parameters:

- content ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the payload text (no envelope if its soap)
- encoding ([str](https://docs.python.org/3/library/stdtypes.html#str)) – encoding for the new message, if omitted system encoding will be used
- msgId ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the message id for the new message, if omitted an UUID will be generated

Returns:
a Python wrapped IOMessage (PlainIOMessage or

SoapIOMessage)

get_available_sinks()¶

Returns:
list with the names of the available sinks

get_default_sink_name()¶
Get the name of the default sink.

If there is only a single unnamed sink, then this method returns “default”.
If there are named sinks without any of them being designated as the
default sink, then this method returns “”.

Returns:
Name of the default sink.

property has_request¶
Check if there is a request.

Returns:
True if context has a saved request, False otherwise

property has_response¶
Check if there is a response message.

Returns:
True if context has a saved response, False otherwise

report_progress()¶
Report progress in case of long-running handle/trigger operations.

This function lets the worker process ping main to avoid timing out
because IOServer main thinks the process is hanging.

property request_message¶
Get or set python wrapped request message.
PlainIOMessage or SoapIOMessage.
:raises: ioserver.base.StaticError if trying to replace an incoming message which
is the most common case for a handler

property response_message¶
Get or set python wrapped response message.
PlainIOMessage or SoapIOMessage.

send(msg)¶
Send a message to the default queue.

If jcms_state property is not set in the message,
it will be set to the current plan cid.

Parameters:
msg (PlainIOMessage or) – Message to be sent

SoapIOMessage

send_to_sink(msg, sinkName)¶
Send a message to a named sink.

If jcms_state property is not set in the message,
it will be set to the current plan cid.

Parameters:
msg (PlainIOMessage or) – message to send

SoapIOMessage
:param str sinkName: name of the sink as specified in the configuration.

property service_logger¶
Return a jcms logger that contains the service name
e.g. ioserver.service_name.service.

Returns:
Logger instance

property service_name¶

Returns:
the name of the service

set_response_sink(sinkName)¶
Set the sink to use for response messages

If named sinks have been configured for the service, this method can
be used to specify which of these sinks to use for the response message.

If the “reply-to” property has been set on the request message, that value
will take precedence, and the sink set here will be ignored.

If this method has not been called, the default sink for the service will be used.

Only handler based patterns care about this value.

Parameters:
sinkName – The name of the sink to use for the response message

# 16.1.8. jcms.ioserver.version10.mave2.IPlanHolder

## 16.1.8.1. IPlanHolder

class jcms.ioserver.version10.planholder_militaris.IPlanHolder(*args, **kwargs)¶
The public API to the IOServer plan cache.

This API provides the functions that handler implementations and tests need access to. It basically provides access to the loaded plan and ruleset objects so that their public API’s can be used.

Handlers shall never call any undo/redo/prune, refresh save or load/unload methods on the plan which would potentially lead the plan outside the local version tree that the handler has started on. Instead they shall throw a TransientMsgError if they encounter problems that can potentially be solved by retry.

__init__(*args, **kwargs)¶

getChangeSet(self) &#x2192; Mave2ChangeSet¶
provide access to the changeset.

getContextParameter(*args)¶
Get the value of a datacontext parameter.

Parameters:
name – datacontext parameter name

Returns:
string representation of parameter value

Raises:
ioserver.base.StaticError – if parameter is not found in datacontext

Types
- Parameter name: std ::string
- Return type: std ::string

getDomainGeneration(*args)¶
Get the domain generation of the loaded plan.

This is the same string that will be needed to load the python binding module.

Returns:
the domain generation as a string

Raises:
ioserver.base.StaticError – if no plan is loaded.

Types
- Return type: std ::string

getMave2ChangeSet(*args)¶
Provide access to the last refresh changeset for an ara.macao Plan. the reference is only locally valid, please assign to an instance of correct type immediately.

Returns:
Mave2 Changeset

Raises:
ioserver.base.StaticError – if no ara.macao plan is loaded.

Types
- Return type: Mave2ChangeSet

getMave2Plan(self) &#x2192; Mave2Plan¶
provide access to the ara.militaris plan.

getMave2PlanWithViewpoint(self, dataset) &#x2192; Mave2Plan¶
provide access to the ara.militaris plan with the specified ara Viewpoint.

getMave2PreviousVersion(*args)¶
Provide access to the previous version for an ara.macao Plan. the reference is only locally valid, please assign to an instance of correct type immediately.

Returns:
Mave2 Version

Raises:
ioserver.base.StaticError – if no ara.macao plan is loaded.

Types
- Return type: Mave2Version

getMaveGeneration(*args)¶
Get the mave generation of the plan (and ruleset).

Depending on the returned number, only one kind of plan can be retrieved.

Returns:

- 2 for mave2/ara.macao or mave2/ara.militaris

Types
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getNowTime(*args)¶
Get the now-timestamp used by the ruleset.

This is a cached value from last refresh, not wall-time.

Returns:
now time

Types
- Return type: AbsTime

getPlan(self) &#x2192; Mave2Plan¶
provide access to the ara.militaris plan.

getPlanPeriodEnd(*args)¶
Get the end time of the plan period, as defined in the datacontext.

Returns:
end time of the period

Raises:
ioserver.base.StaticError – if time is not found in datacontext

Types
- Return type: AbsTime

getPlanPeriodStart(*args)¶
Get the start time of the plan period, as defined in the datacontext.

Returns:
start time of the period

Raises:
ioserver.base.StaticError – if time is not found in datacontext

Types
- Return type: AbsTime

getPreviousVersion()¶
getMave2PreviousVersion(self) -&gt; Mave2Version.
provide access to the previous version for an ara.militaris Plan.

getRaveSession(self) &#x2192; ara::RaveSession.¶
provide access to the RaveSession, if one has been loaded

getRaveSessionWithViewpoint(self, dataset) &#x2192; ara::RaveSession.¶
provide access to the RaveSession with the specified ara Viewpoint,
if one has been loaded

static getThePlan(*args)¶
Provide access to the global plan holder instance.

Returns:
a shared pointer to the global plan holder instance if it has been initiated already, NULL otherwise

Types
- Return type: IPlanHolder ::Pointer

isPlanLoaded(*args)¶
Check if we have a plan loaded.

Returns:
true if plan is loaded

Types
- Return type: [bool](https://docs.python.org/3/library/functions.html#bool)

isRulesetLoaded(*args)¶
Check if we have a ruleset loaded.

Returns:
true if ruleset is loaded

Types
- Return type: [bool](https://docs.python.org/3/library/functions.html#bool)

--- SUBPAGE: python_api_ver9_reference.html ---

# 16.2.1. jcms.ioserver.versions

This module defines the supported Python Interface Versions.

All handlers and triggers must implement the method handler_interface_version()
that returns one of these values.

The PlanHolder and context objects provided to the handler/trigger will be adopted to the version in
which the service is implemented.

class jcms.ioserver.versions.InterfaceVersion
Specifies the version of the interface used in the handler or trigger implementation.

NINE = 9
Interface version 9, introduced in IOServer version 28.0.0

TEN = 10
Interface version 10, introduced in IOServer version 33.0.0

# 16.2.2. jcms.ioserver.constants

This module defines the public constants that handlers and triggers have access to.

class jcms.ioserver.constants.PropertyNames
Names of predefined message properties.

SOAP_ACTION = 'SOAPAction'
The soap action contains the name of the SOAP operation, format urn:&lt;operation&gt;.

STATE_REFERENCE = 'jcms_state'
The state header contains the JCMS state reference CID if any.

USER_ATTRIBUTES = 'jcms_attributes'
The user attribute header contains the security attributes.

# 16.2.3. jcms.ioserver.exceptions

exception jcms.ioserver.exceptions.BlockingMsgError(description='', source_exc_type=None)
A non-transient error in message that cannot be skipped

exception jcms.ioserver.exceptions.DatabaseConflictError(description='', source_exc_type=None)
An error caused by a database conflict trigger.

exception jcms.ioserver.exceptions.DatabaseDataTooOldError(description='', source_exc_type=None)
An error caused by a database data too old conflict.

exception jcms.ioserver.exceptions.FormatterError(description='', source_exc_type=None)
A problem in message formatting or output validation.

exception jcms.ioserver.exceptions.IOSError(description='', source_exc_type=None)
Base class for IOServer exceptions.

__init__(description='', source_exc_type=None)

get_description()

Returns:
the error description.

get_error_code()

Returns:
the error code.

exception jcms.ioserver.exceptions.MarshallingError(description='', source_exc_type=None)
Base class for Marshalling exceptions.

__init__(description='', source_exc_type=None)

exception jcms.ioserver.exceptions.MessageError(description='', source_exc_type=None)
An error caused by incorrect information or syntax in a message.

exception jcms.ioserver.exceptions.ParserError(description='', source_exc_type=None)
A problem in message parsing or input validation.

exception jcms.ioserver.exceptions.SendError(description='', source_exc_type=None)
An error caused by failure to send or acknowledge a message.

exception jcms.ioserver.exceptions.SkipMsgError(description='', source_exc_type=None)
A non-transient error in a message that can be skipped.

exception jcms.ioserver.exceptions.StaticError(description='', source_exc_type=None)
A non-transient error condition in the system as opposed to the message.

exception jcms.ioserver.exceptions.SystemError(description='', source_exc_type=None)
An error condition in the IOServer system as opposed to the message.

exception jcms.ioserver.exceptions.TransientError(description='', source_exc_type=None)
An error caused by a possibly temporary condition in the system.

exception jcms.ioserver.exceptions.TransientMsgError(description='', source_exc_type=None)
An error caused by a possibly temporary condition in the message.

# 16.2.4. jcms.ioserver.version9.config

## 16.2.4.1. IConfig

class jcms.ioserver.version9.config.IConfig(*args, **kwargs)¶
Provides access to the IO-server configuration.

The ioserver configuration is organized in global (per process) and service level configuration groups. A configuration group is a set of values (and potentially subgroups) that can be fetched by name. In the jcms configuration file syntax a configuration group corresponds to a tag that has complex content, while a value is a tag with only string content.

The IConfig interface encapsulates the lookup logic and override hierarchy within the configuration and provides the values that are effective for this ioserver instance. Lookups with a service-specific group tag will provide the effective value for that service and sub-group, standard fallback logic to process-global and global-default values is handled by the config implementation.

Components should lookup the values they need within their provided configuration group using getConfigValue(group, key, defvalue) or the typed equivalents.

&#64;deprecated Use ioserver::base::IConfig instead.

__init__(*args, **kwargs)¶

getConfigAttribute(group, attribute, defValue)¶
Get a configuration attribute with given key within a group.

Parameters:

- group – the group key of the requested configuration group
- attribute – the name of the configuration attribute to fetch
- defValue – a fallback value to use if no configuration is found

Returns:
the value of the configuration attribute if found, defValue else

Types
- Parameter group: std ::string
- Parameter attribute: std ::string
- Parameter defValue: std ::string
- Return type: std ::string

getConfigAttributes(group)¶
Get all configuration attributes, including values, within a group.

Any “name” attributes are ignored as the configuration API handles them separately.

Parameters:
group – the group key of the requested configuration group

Returns:
map of attribute name to attribute value.

Types
- Parameter group: std ::string
- Return type: StringMap

getConfigBool(group, key, defValue)¶
helper to fetch boolean value

find the configuration value and convert it to a boolean. A value of “true” is regarded true, all other values are false.

Parameters:

- group – the group key of the requested configuration group
- key – the configuration key (within the group)
- defValue – a fallback value to use if no configuration is found

Returns:
the value of the configuration property if its found, defValue else

Types
- Parameter group: std ::string
- Parameter key: std ::string
- Parameter defValue: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: [bool](https://docs.python.org/3/library/functions.html#bool)

getConfigInt(group, key, defValue)¶
helper to fetch integer value

find the configuration value and convert it to an integer.
getConfigValue(const std::string&amp;, const std::string&amp; ,const std::string&amp; )

Parameters:

- group – the group key of the requested configuration group
- key – the configuration key (within the group)
- defValue – a fallback value to use if no configuration is found

Returns:
the value of the configuration property if its found, defValue else

Raises:
ioserver.base.ConfigurationError – if the value doesn’t convert to int

Types
- Parameter group: std ::string
- Parameter key: std ::string
- Parameter defValue: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getConfigSubGroup(parentGroup, groupTag, name)¶
provide the lookup key for a detailed ioserver configuration group

Parameters:

- parentGroup – the group key of the requested configuration group
- groupTag – the tag of the configuration group, like “db” or “datamodel”
- name – the name of an instance of the configuration group if there can be more than one

Returns:
the group key to use for lookups of configuration in that group

Types
- Parameter parentGroup: std ::string
- Parameter groupTag: std ::string
- Parameter name: std ::string
- Return type: std ::string

getConfigValue(group, key, defValue)¶
lookup a configuration value with given key within a group

Each component has a configuration group provided in the constructor and should call the method with that group. Global settings directly defined on the process level can get fetched with an empty group.

Parameters:

- group – the group key of the requested configuration group
- key – the name of the configuration value to fetch
- defValue – a fallback value to use if no configuration is found

Returns:
the value of the configuration property if found, defValue else

Types
- Parameter group: std ::string
- Parameter key: std ::string
- Parameter defValue: std ::string
- Return type: std ::string

getGlobalConfigGroup(groupTag, name)¶
provide the lookup key for a ioserver global configuration group

Use this method to get a group key for process-global settings.

Parameters:

- groupTag – the tag of the configuration group, like “db” or “datamodel”
- name – the name of an instance of the configuration group if there can be more than one, otherwise empty

Returns:
the group key to use for lookups of configuration in that group

Types
- Parameter groupTag: std ::string
- Parameter name: std ::string
- Return type: std ::string

getGlobalGroupNames(groupTag)¶
get the list of all names for parallel global configuration groups with same tag

Parameters:
groupTag – the tag of the configuration group, like “db” or “datamodel”

Types
- Parameter groupTag: std ::string
- Return type: StringVectorPointer

getPortBase()¶
Get the portbase.

Returns:
the portbase number, -1 on error

Types
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getProcessName()¶
Get the proccess name.

Returns:
the name of the process

Types
- Return type: std ::string

getProcessServicePort(*args)¶
Get the service port to use for the process when communicating with sysmond.

Parameters:

- systemService – The system service to look up
- hostName – The host name to look up (default: use the current host name)
- processName – The process name (default: use the current process name)

Returns:
port number to the service or -1 if the service cannot be found

Types
- Parameter systemService: std ::string
- Parameter hostName: std ::string
- Parameter processName: std ::string
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getProcessServiceUrl(*args)¶
get the service URL for a given system service

Parameters:

- systemService – The system service to look up
- hostName – The host where to look for the service. Empty string means localhost. Default is empty string.
- processName – The name of the process which provides the service. Empty string means use the process name which was given when calling the constructor (in this class).

Returns:
URL with the format service://host:port or empty string if service is not found.

Types
- Parameter systemService: std ::string
- Parameter hostName: std ::string
- Parameter processName: std ::string
- Return type: std ::string

getServiceConfigGroup(service, groupTag, name)¶
provide the lookup key for a ioserver service local configuration group

Use this method to get a group key for service specific settings.

Parameters:

- service – the name of the service
- groupTag – the tag of the configuration group, like “pattern” or “source”
- name – the name of an instance of the configuration group if there can be more than one, otherwise empty

Returns:
the group key to use for lookups of configuration in that group

Types
- Parameter service: std ::string
- Parameter groupTag: std ::string
- Parameter name: std ::string
- Return type: std ::string

getServiceGroupNames(service, groupTag)¶
get the list of all names for parallel service configuration groups with same tag

Parameters:

- service – the name of the service
- groupTag – the tag of the configuration group, like “pattern” or “source”

Types
- Parameter service: std ::string
- Parameter groupTag: std ::string
- Return type: StringVectorPointer

getServiceNames()¶
get the list of all service names

Types
- Return type: StringVectorPointer

getSubGroupNames(parentGroup, groupTag)¶
get the list of all names for parallel configuration groups

Types
- Parameter parentGroup: std ::string
- Parameter groupTag: std ::string
- Return type: StringVectorPointer

getSubGroups(parentGroup, groupTag)¶
get the list of all groups for parallel configuration groups

Types
- Parameter parentGroup: std ::string
- Parameter groupTag: std ::string
- Return type: StringVector

getenv(key, defValue)¶
get the value of an environment variable

Parameters:

- key – the name of the variable to fetch
- defValue – a fallback value to use if the variable is not set

Returns:
the value of the environment variable if set, otherwise defValue

Types
- Parameter key: std ::string
- Parameter defValue: std ::string
- Return type: std ::string

# 16.2.5. jcms.ioserver.version9.actions

This module defines the action codes that version NINE handlers can return.

## 16.2.5.1. PlanAction

class jcms.ioserver.version9.actions.PlanAction¶
Version 9 Handler actions. Specifies what the pattern should do when a handler returns.
Return value from handler methods.

ROLLBACK = 2¶
Roll back the modifications in the plan.

SAVE = 0¶
Save the current state of the plan.

UNCHANGED = 1¶
The plan does not need to be saved.

## 16.2.5.2. FaultAction

class jcms.ioserver.version9.actions.FaultAction¶
Version 9 Fault actions. Specifies what the pattern should respond when an exception is raised.
Return value from the on_fault method in the handler module.

DEFAULT_RESPONSE = 0¶
Create a default error response message. Only supported for SOAP messages.

NO_RESPONSE = 1¶
Do not send a response.

SEND_RESPONSE = 2¶
Send the response message that the handler module has produced.

# 16.2.6. jcms.ioserver.version9.message

This module defines the Message classes available to version NINE handlers/triggers.

## 16.2.6.1. PlainIOMessage

class jcms.ioserver.version9.message.PlainIOMessage(io_message, pyxb_binding=None, skipMsgOnMarshalError=True)¶
IOMessage with plain text or XML content.

__init__(io_message, pyxb_binding=None, skipMsgOnMarshalError=True)¶

property content¶
Get or set the message content.

property content_type¶
Get or set the message content-type.

classmethod create_io_message(content, contentType=None, encoding=None, msgId=None)¶
Factory method for creating a Plain IOMessage.

Parameters:

- content ([bytes](https://docs.python.org/3/library/stdtypes.html#bytes)) – the message content
- contentType ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the type of the content, can be e.g. text or binary
- encoding ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the text encoding used
- msgId ([str](https://docs.python.org/3/library/stdtypes.html#str)) – id for the message

Returns:
IOMessage SWIG object without wrapper

property encoding¶
Get or set the message encoding.

property full_message_text¶

Returns:
full text of the message.

classmethod get_default_content_type()¶
Default content type for new messages.

get_properties()¶
Get the message properties.
The properties are copied into a dict(str:str)

Returns:
dictionary of properties

get_property(key, default='')¶
Get the message property by key.

Parameters:

- key ([str](https://docs.python.org/3/library/stdtypes.html#str)) – property key
- default ([str](https://docs.python.org/3/library/stdtypes.html#str)) – default value used if property does not exist.

Returns:
value of the property based on key

classmethod get_system_encoding()¶

Returns:
the system character encoding name

get_user_attributes()¶
Get user attributes as a dict.

Returns:
dictionary containing user attributes

property id¶
Get or set the message Id.

pyxb_encoding = 'utf-8'¶

set_property(key, value)¶
Set a message property by key.

Parameters:

- key ([str](https://docs.python.org/3/library/stdtypes.html#str)) – property key
- value ([str](https://docs.python.org/3/library/stdtypes.html#str)) – set the property to this value

# 16.2.7. jcms.ioserver.version9.context

This module defines the context interface for version NINE.

## 16.2.7.1. ServiceContext

class jcms.ioserver.version9.context.ServiceContext(swig_service_context, is_soap=False, binding_module=None, skipMsgOnMarshalError=False)¶

__init__(swig_service_context, is_soap=False, binding_module=None, skipMsgOnMarshalError=False)¶

property config¶

Returns:
IOServer configuration (IConfig)

create_io_message(content, contentType=None, encoding=None, msgId=None)¶
Create a new IOMessage from the complete content.

Parameters:

- content ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the full message text (including envelope if its soap)
- contentType ([str](https://docs.python.org/3/library/stdtypes.html#str)) – content type for the new message, if omitted a message type

dependent default will be used
:param str encoding: encoding for the new message, if omitted system encoding will be used
:param str msgId: the message id for the new message, if omitted an UUID will be generated
:return: a Python wrapped IOMessage (PlainIOMessage or
SoapIOMessage)

create_io_message_from_content(content, encoding=None, msgId=None)¶
Create a new IOMessage from the payload text. A message type dependent default will be used.

Parameters:

- content ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the payload text (no envelope if its soap)
- encoding ([str](https://docs.python.org/3/library/stdtypes.html#str)) – encoding for the new message, if omitted system encoding will be used
- msgId ([str](https://docs.python.org/3/library/stdtypes.html#str)) – the message id for the new message, if omitted an UUID will be generated

Returns:
a Python wrapped IOMessage (PlainIOMessage or

SoapIOMessage)

get_available_sinks()¶

Returns:
list with the names of the available sinks

property has_request¶
Check if there is a request.

Returns:
True if context has a saved request, False otherwise

property has_response¶
Check if there is a response message.

Returns:
True if context has a saved response, False otherwise

report_progress()¶
Report progress in case of long-running handle/trigger operations.

This function lets the worker process ping main to avoid timing out
because IOServer main thinks the process is hanging.

property request_message¶
Get or set python wrapped request message.
PlainIOMessage or SoapIOMessage.
:raises: ioserver.base.StaticError if trying to replace an incoming message which
is the most common case for a handler

property response_message¶
Get or set python wrapped response message.
PlainIOMessage or SoapIOMessage.

send(msg)¶
Send a message to the default queue.

If jcms_state property is not set in the message,
it will be set to the current plan cid.

Parameters:
msg (PlainIOMessage or) – Message to be sent

SoapIOMessage

send_to_sink(msg, sinkName)¶
Send a message to a named sink.

If jcms_state property is not set in the message,
it will be set to the current plan cid.

Parameters:
msg (PlainIOMessage or) – message to send

SoapIOMessage
:param str sinkName: name of the sink as specified in the configuration.

property service_logger¶
Return a jcms logger that contains the service name
e.g. ioserver.service_name.service.

Returns:
Logger instance

property service_name¶

Returns:
the name of the service

set_response_sink(sinkName)¶
Set the sink to use for response messages

If named sinks have been configured for the service, this method can
be used to specify which of these sinks to use for the response message.

If the “reply-to” property has been set on the request message, that value
will take precedence, and the sink set here will be ignored.

If this method has not been called, the default sink for the service will be used.

Only handler based patterns care about this value.

Parameters:
sinkName – The name of the sink to use for the response message

# 16.2.8. jcms.ioserver.version9.mave2.IPlanHolder

## 16.2.8.1. IPlanHolder

class jcms.ioserver.version9.planholder_militaris.IPlanHolder(*args, **kwargs)¶
The public API to the IOServer plan cache.

This API provides the functions that handler implementations and tests need access to. It basically provides access to the loaded plan and ruleset objects so that their public API’s can be used.

Handlers shall never call any undo/redo/prune, refresh save or load/unload methods on the plan which would potentially lead the plan outside the local version tree that the handler has started on. Instead they shall throw a TransientMsgError if they encounter problems that can potentially be solved by retry.

&#64;deprecated Use ioserver::base::IPlanHolder instead.

__init__(*args, **kwargs)¶

getChangeSet(self) &#x2192; Mave2ChangeSet¶
provide access to the changeset.

getContextParameter(*args)¶
Get the value of a datacontext parameter.

Parameters:
name – datacontext parameter name

Returns:
string representation of parameter value

Raises:
ioserver.base.StaticError – if parameter is not found in datacontext

Types
- Parameter name: std ::string
- Return type: std ::string

getDomainGeneration(*args)¶
Get the domain generation of the loaded plan.

This is the same string that will be needed to load the python binding module.

Returns:
the domain generation as a string

Raises:
ioserver.base.StaticError – if no plan is loaded.

Types
- Return type: std ::string

getMave2ChangeSet(*args)¶
Provide access to the last refresh changeset for an ara.macao Plan. the reference is only locally valid, please assign to an instance of correct type immediately.

Returns:
Mave2 Changeset

Raises:
ioserver.base.StaticError – if no ara.macao plan is loaded.

Types
- Return type: Mave2ChangeSet

getMave2Plan(self) &#x2192; Mave2Plan¶
provide access to the ara.militaris plan.

getMave2PlanWithViewpoint(self, dataset) &#x2192; Mave2Plan¶
provide access to the ara.militaris plan with the specified ara Viewpoint.

getMave2PreviousVersion(*args)¶
Provide access to the previous version for an ara.macao Plan. the reference is only locally valid, please assign to an instance of correct type immediately.

Returns:
Mave2 Version

Raises:
ioserver.base.StaticError – if no ara.macao plan is loaded.

Types
- Return type: Mave2Version

getMaveGeneration(*args)¶
Get the mave generation of the plan (and ruleset).

Depending on the returned number, only one kind of plan can be retrieved.

Returns:

- 2 for mave2/ara.macao or mave2/ara.militaris

Types
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getNowTime(*args)¶
Get the now-timestamp used by the ruleset.

This is a cached value from last refresh, not wall-time.

Returns:
now time

Types
- Return type: AbsTime

getPlan(self) &#x2192; Mave2Plan¶
provide access to the ara.militaris plan.

getPlanPeriodEnd(*args)¶
Get the end time of the plan period, as defined in the datacontext.

Returns:
end time of the period

Raises:
ioserver.base.StaticError – if time is not found in datacontext

Types
- Return type: AbsTime

getPlanPeriodStart(*args)¶
Get the start time of the plan period, as defined in the datacontext.

Returns:
start time of the period

Raises:
ioserver.base.StaticError – if time is not found in datacontext

Types
- Return type: AbsTime

getPreviousVersion()¶
getMave2PreviousVersion(self) -&gt; Mave2Version.
provide access to the previous version for an ara.militaris Plan.

getRaveSession(self) &#x2192; ara::RaveSession.¶
provide access to the RaveSession, if one has been loaded

getRaveSessionWithViewpoint(self, dataset) &#x2192; ara::RaveSession.¶
provide access to the RaveSession with the specified ara Viewpoint,
if one has been loaded

static getThePlan(*args)¶
Provide access to the global plan holder instance.

Returns:
a shared pointer to the global plan holder instance if it has been initiated already, NULL otherwise

Types
- Return type: IPlanHolder ::Pointer

isPlanLoaded(*args)¶
Check if we have a plan loaded.

Returns:
true if plan is loaded

Types
- Return type: [bool](https://docs.python.org/3/library/functions.html#bool)

isRulesetLoaded(*args)¶
Check if we have a ruleset loaded.

Returns:
true if ruleset is loaded

Types
- Return type: [bool](https://docs.python.org/3/library/functions.html#bool)

--- SUBPAGE: python_testutils_api_ver10_reference.html ---

# 17.1.1. Conflict Detection Strategy Constants

ConflictDetectionDisabled¶
No conflict detection during save.

ConflictDetectionMessage¶
Use the commit id from the message (JCMS_STATE) for detecting conflicts during save.

ConflictDetectionPlan¶
Use the commit id from the plan for detecting conflicts during save.

# 17.1.2. jcms.ioserver.testutils.version10.main.TestMain

class jcms.ioserver.testutils.version10.main.TestMain(serviceName)¶
Describes an IO-server test runner object that keeps the whole functionality together for unittesting.

__init__(serviceName)¶
constructor

Types
- Parameter serviceName: std ::string

getConfig()¶
Get the configuration object.

Returns:
a pointer to the global configuration. Use this to setup the ioserver parameters.

Types
- Return type: ioserver ::testbase ::ITestConfig ::Pointer

getMemoryHAStore()¶
Get the memory HA store object.

Returns:
a pointer to the memory HA store object.

Types
- Return type: ioserver ::testbase ::IMemoryHAStore ::Pointer

getMemoryQueue()¶
Get the memory global queue.

If the config was set to use memory queue then the handler will use this queue.

Returns:
a pointer to the global memory queue.

Types
- Return type: ioserver ::testbase ::IMemoryQueue ::Pointer

getRunner()¶
Get the runner object.

After setting up the configuration the runner is initialized on first access.
The runner is the test engine of the IOServer, it will load the plan and
execute the service under test.

Once the runner has been obtained, the configuration will be locked,
all attempts to set more configuration values will result in an exception.

Returns:
a pointer to the runner object.

# 17.1.3. jcms.ioserver.testutils.version10.main.IMemoryHAStore

class jcms.ioserver.testutils.version10.main.IMemoryHAStore(*args, **kwargs)¶
This interface provides access to a memory based HA store for testing purposes.

The most commonly used HA store key is “generation”. It is used to specify the latest handled commit id.

__init__(*args, **kwargs)¶

clear()¶
Clear all internal state.

Types
- Return type: void

getValue(key)¶
Get a value from the HA key-value store.

Parameters:
key – The key for which to retrieve a value.

Returns:
The value associated with the given key.

Raises:
ioserver.base.StaticError – if there is no value for key.

Types
- Parameter key: std ::string
- Return type: std ::string

hasValue(key)¶
Check if there is a value in the HA key-value store for the given key.

Parameters:
key – The key to check for.

Types
- Parameter key: std ::string
- Return type: [bool](https://docs.python.org/3/library/functions.html#bool)

setValue(key, value)¶
Set a key-value pair in the HA key-value store.

Parameters:

- key – The key to write.
- value – The value associated with key.

Types
- Parameter key: std ::string
- Parameter value: std ::string
- Return type: void

# 17.1.4. jcms.ioserver.testutils.version10.main.IMemoryQueue

class jcms.ioserver.testutils.version10.main.IMemoryQueue(*args, **kwargs)¶
This interface provides access to the built in memory queue for testing purposes.

__init__(*args, **kwargs)¶

addInputIOMessage(msg)¶
Add an IOMessage to the input queue.

Parameters:
msg – the input message

Returns:
index of message in the queue

Types
- Parameter msg: IOMessagePointer
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getDefaultInputContentType()¶
Get the default content type to use for new input messages.

Returns:
the default content type

Types
- Return type: std ::string

getDefaultInputEncoding()¶
Get the default encoding to use for new input messages.

Returns:
the default encoding

Types
- Return type: std ::string

getInputIOMessage(index)¶
Get the input message at given index.

Parameters:
index – the message index to get

Returns:
message at index

Types
- Parameter index: size_t
- Return type: IOMessagePointer

getInputIOMessages()¶
Get the current input queue content.

Returns:
list of the messages on the input queue

Types
- Return type: IOMessageList

getInputSize()¶
Get the size of input message queue.

Returns:
size of the input message list

Types
- Return type: size_t

getOutputIOMessage(index)¶
Get the output message at given index of default sink.

Parameters:
index – the message index to get

Returns:
message at index

Types
- Parameter index: size_t
- Return type: IOMessagePointer

getOutputIOMessageByName(sinkName, index)¶
Get the output message at given index.

Parameters:

- sinkName – name of the sink
- index – the message index to get

Returns:
message at index

Types
- Parameter sinkName: std ::string
- Parameter index: size_t
- Return type: IOMessagePointer

getOutputIOMessages()¶
Get the current output queue content of default sink.

Returns:
list of the messages on the output queue

Types
- Return type: IOMessageList

getOutputIOMessagesByName(sinkName)¶
Get the current output queue content.

Parameters:
sinkName – name of the sink

Returns:
list of the messages on the output queue

Types
- Parameter sinkName: std ::string
- Return type: IOMessageList

getOutputSize()¶
Get size of output message queue of default sink.

Returns:
size of the output message list

Types
- Return type: size_t

getOutputSizeByName(sinkName)¶
Get size of output message queue.

Parameters:
sinkName – name of the sink

Returns:
size of the output message list

Types
- Parameter sinkName: std ::string
- Return type: size_t

getStartId()¶
Types
- Return type: size_t

reset()¶
Reset content of input and output message lists.

Types
- Return type: void

setDefaultInputContentType(content_type)¶
Set the default content type to use for new input messages.

Parameters:
content_type – the content type

Types
- Parameter content_type: std ::string
- Return type: void

setDefaultInputEncoding(encoding)¶
Set the default encoding to use for new input messages.

Parameters:
encoding – the encoding

Types
- Parameter encoding: std ::string
- Return type: void

setInputIOMessages(msgVec)¶
Replace current input queue content with a new message list.

Parameters:
msgVec – list of messages to be put on the queue

Types
- Parameter msgVec: IOMessageList
- Return type: void

setStartId(index)¶
Provide a start value for generating the msgIds, default is 0.

Parameters:
index – start value for generating msgIds

Types
- Parameter index: size_t
- Return type: void

# 17.1.5. jcms.ioserver.testutils.version10.main.ITestConfig

class jcms.ioserver.testutils.version10.main.ITestConfig(*args, **kwargs)¶
Provides configuration for an IOServer mock-instance

The interface allows steering the mock implementation, chose which real components should be used and which others to replace by mock-objects (e.g memory queue instead of qpid)

__init__(*args, **kwargs)¶

convertToMemoryQueues()¶
Convert configuration to use memory queues.

Convert all sources and sinks for service to use memory queues. Typically called after importProcessConfig.

Types
- Return type: void

debugPrint(*args)¶
Print the configuration content.

Types
- Parameter s: std ::ostream
- Return type: void

enableMessageRetention()¶
Enable message retention for service.

This configures the message retention queue in global default

Types
- Return type: void

getDomainGeneration()¶
Retrieve the domain generation setting.

Returns:
the domain generation setting (“air1” or “air2”)

Types
- Return type: std ::string

getPlanBuilderName()¶
Retrieve the plan builder setting.

Returns:
the name of the plan builder types, typical “mave2”

Types
- Return type: std ::string

getProcessName()¶
Get the common config process name.

Returns:
process name

Types
- Return type: std ::string

getProcessServicePort(*args)¶
Get the service port to use for the process when communicating with sysmond.

Parameters:

- systemService – the system service to look up
- hostName – the host name to look up (default: use the current host name)
- processName – the process name (default: use the current process name)

Returns:
port number

Types
- Parameter systemService: std ::string
- Parameter hostName: std ::string
- Parameter processName: std ::string
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getRulesetType()¶
Get the ruleset type used.

Only valid for mave2 plans.

Returns:
Name of ruleset type to use (“rave”). Default is an empty string.

Types
- Return type: std ::string

getServiceNames()¶
Get the list of all service names.

Returns:
list containing all service names

Types
- Return type: StringVectorPointer

importProcessConfig(*args)¶
Import from system configuration.

Imports the settings for the tests serviceName from the configuration for the given IOServer process.

Parameters:

- process – the name of the IOServer process to copy from
- cfgFile – the name of the config root file if not standard.

Types
- Parameter process: std ::string
- Parameter cfgFile: std ::string
- Return type: void

setChangeReason(changeReason)¶
Set changeReason to use for save.

This is only relevant if saving has been set to true.

Parameters:
changeReason – what change reason to use when saving

Types
- Parameter changeReason: std ::string
- Return type: void

setConfigValue(path, value)¶
Set custom config value.

This is an “escape hatch” when all other convenience methods doesn’t provide the needed functionality.

Parameters:

- path – the path to the config value (xpathish)
- value – the value to set

Types
- Parameter path: std ::string
- Parameter value: std ::string
- Return type: void

setConflictDetectionStrategy(strategy)¶
Enable or disable conflict detection during save.

This is only relevant if saving has been set to true.

Parameters:
strategy – which conflict detection strategy to use.

Types
- Parameter strategy: ioserver ::base ::ConflictDetectionStrategy
- Return type: void

setCppBinding(isHandler, handlerName, pluginName)¶
Use a C++ bridge.

Parameters:

- isHandler – whether this is a handler or trigger
- handlerName – name of handler to instantiate
- pluginName – name of plugin (shared library) to load

Types
- Parameter isHandler: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter handlerName: std ::string
- Parameter pluginName: std ::string
- Return type: void

setCppHandlerBinding(handlerName, pluginName)¶
use C++ bridge handler

Parameters:

- handlerName – name of handler to instantiate
- pluginName – name of plugin (shared library) to load

Types
- Parameter handlerName: std ::string
- Parameter pluginName: std ::string
- Return type: void

setCppTriggerBinding(handlerName, pluginName)¶
use C++ bridge trigger

Parameters:

- handlerName – name of handler to instantiate
- pluginName – name of plugin (shared library) to load

Types
- Parameter handlerName: std ::string
- Parameter pluginName: std ::string
- Return type: void

setDatabase(*args)¶
Prepare the database connection configuration.

Prepare database connection configuration with explicit schema setup.

Parameters:

- connectString – the Dave connectstring to use
- dbschema – the schema name (default = “”)

Types
- Parameter connectString: std ::string
- Parameter dbschema: std ::string
- Return type: void

setDomainGeneration(*args)¶
Override the domain generation for the plan.

Parameters:

- domain – the domain generation string “air1” or “air2”
- planBuilder – name of a custom plan builder type, this requires a special driver lib that registers a driver with this name. Typical value is “mave2”.

Types
- Parameter domain: std ::string
- Parameter planBuilder: std ::string
- Return type: void

setErrorRetryCount(*args)¶
Set value for retry counters.

Note that TransientErrors are raised to the test even when retry is set, when calling handle again they might be resolved or transform into StaticError/MessageError when the retries are exhausted.

Parameters:
retry – how often to retry on transient errors (same for message and system erros)

Types
- Parameter retry: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setEventTriggerPattern(cacsRole)¶
Setup parameters for the eventtrigger pattern.

Use the eventtrigger pattern with default settings for test.

Parameters:
cacsRole – name of the cacs role to use

Types
- Parameter cacsRole: std ::string
- Return type: void

setMemoryQueue()¶
Setup configuration to use the builtin memory queue.

The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure. This is a convenience menthod that will set up a defult source queue and a defualt sink queue.

To set up named sinks, use :meth:setNamedMemorySink and :meth:setMemorySource

Types
- Return type: void

setMemorySource()¶
Setup configuration to use the default memory source queue.

The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure.

Types
- Return type: void

setMsgErrorStrategy(*args)¶
Define parameters that steer the error strategy for message related errors.

Parameters:
skipMsg – whether to remove a message from the inqueue if it failed, independent from context

Types
- Parameter skipMsg: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

setNamedMemorySink(sinkName)¶
Setup configuration to use a named memory sink queue.

The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure.

Parameters:
sinkName – the name of the sink

Types
- Parameter sinkName: std ::string
- Return type: void

setNow(nowString)¶
Provide an override for now.

This will influence the datacontext selections as well as rave.

Parameters:
nowString – a valid Rave datetime expression as in basics::time::minutes_from_expr()

Types
- Parameter nowString: std ::string
- Return type: void

setPersistCid(value)¶
Set persist_cid property.

Parameters:
value – If persist_cid should be set to “true” or “false”.

Types
- Parameter value: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

setPlan(*args)¶
Prepare the plan configuration.

Use this to specify a datacontext but no ruleset.

Parameters:

- datacontext – the name of the datacontext to load
- snapshotpath – path to snapshot location for this datacontext this will be given to the plan factory if provided.

Types
- Parameter datacontext: std ::string
- Parameter snapshotpath: std ::string
- Return type: void

setPortBase(port)¶
Provide a base port for sysmond communication.

Parameters:
port – base port for sysmmond

Types
- Parameter port: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setPythonBinding(*args)¶
Use a python bridge.

Parameters:

- isHandler – whether this is a handler or trigger
- protocol – the name of the message protocol (plain or soap)
- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter isHandler: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter protocol: std ::string
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setPythonHandlerPlainBinding(*args)¶
Use python bridge with plain handler.

Parameters:

- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setPythonHandlerSoapBinding(*args)¶
Use python bridge with a soap xml handler.

Parameters:

- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setPythonTriggerPlainBinding(*args)¶
Use python bridge with a plain trigger.

Parameters:

- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setPythonTriggerSoapBinding(*args)¶
Use python bridge with a soap xml trigger.

Parameters:

- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setQpid(host, port, queueName, prefetchCapacity=0, compress=False, maxContentSize=0)¶
Setup parameters for qpid.

Use this to run tests against real ActiveMQ queues.

Parameters:

- host – the host to connect to ActiveMQ
- port – the port on host
- queueName – the queue name to work on
- prefetchCapacity – the prefetch capacity of qpid receiver
- compress – the switch for compressing the content of the message
- maxContentSize – the maximum content size of the message compressed or not.

Types
- Parameter host: std ::string
- Parameter port: std ::string
- Parameter queueName: std ::string
- Parameter prefetchCapacity: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter compress: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter maxContentSize: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setQpidMessageSink(*args)¶
Setup parameters for qpid message sink.

Use this to run tests with real ActiveMQ queues.

Parameters:

- brokerHost – ActiveMQ broker host address
- brokerPort – ActiveMQ broker host port
- queueName – queue name to use
- sinkName – name of this sink. Default sets default sink
- senderCapacity – Number of messages to buffer up when using asynchronous send(). Default 0 (synchronous send)
- compress – set to true if the message should be gzipped. Default false
- maxContentSize – Maximum content size. Default 0

Types
- Parameter brokerHost: std ::string
- Parameter brokerPort: std ::string
- Parameter queueName: std ::string
- Parameter sinkName: std ::string
- Parameter senderCapacity: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter compress: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter maxContentSize: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setQpidMessageSource(brokerHost, brokerPort, queueName, prefetchCapacity)¶
Setup parameters for qpid message source.

Use this to run tests against real ActiveMQ queues.

Parameters:

- brokerHost – ActiveMQ broker host address
- brokerPort – ActiveMQ broker host port
- queueName – queue name to use
- prefetchCapacity – number of messages to prefetch in the background

Types
- Parameter brokerHost: std ::string
- Parameter brokerPort: std ::string
- Parameter queueName: std ::string
- Parameter prefetchCapacity: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setRequestResponsePattern(cacsRole, saving=False)¶
Setup parameters for the request/response pattern.

Use the request/response pattern with default settings for test.

All messages in the inqueue will be handled before returning. No retry will be attempted and any exceptions from the handler or surrounding modules will just be raised up to the calling test.

This doesn’t affect the pattern-neutral error strategy settings, like global retries (default 3 ) or skipmessage (default true).

Parameters:

- cacsRole – name of the cacs role to use
- saving – if the plan should be saved

Types
- Parameter cacsRole: std ::string
- Parameter saving: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

setRuleset(*args)¶
Prepare the ruleset configuration.

Parameters:

- ruleset – the name of the global ruleset to load
- parameterset – the name of the parameter set to load, if empty no parameters are set

Types
- Parameter ruleset: std ::string
- Parameter parameterset: std ::string
- Return type: void

setRulesetType(rulesetType)¶
Set the ruleset type that will be used.

Only valid when using mave2 based plans.

Parameters:
rulesetType – name of ruleset type to use. Requires that a driver lib has registered a driver with support for this ruleset. Typical value is “rave” (for rave::Ruleset type).

Types
- Parameter rulesetType: std ::string
- Return type: void

setServiceValue(path, value)¶
Set custom config value for service.

This is an “escape hatch” when all other convenience methods doesn’t provide the needed functionality.

Parameters:

- path – the path to the config value relative the service root (xpathish)
- value – the value to set

Types
- Parameter path: std ::string
- Parameter value: std ::string
- Return type: void

setSubscriberPattern(cacsRole, saving=False, chunkSize=1, savetimeout=10)¶
Setup parameters for the subscriber pattern.

Use the subscriber pattern with default settings for test.

All messages in the inqueue will be handled before returning. No retry will be attempted and any exceptions from the handler or surrounding modules will just be raised up to the calling test.

This doesn’t affect the pattern-neutral error strategy settings, like global retries (default 3 ) or skipmessage (default true).

Parameters:

- cacsRole – name of the cacs role to use
- saving – whether the plan should be saved after handling the messages, default false.
- chunkSize – how many message to save per chunk, -1 for no limit
- savetimeout – how long to wait for a save at most, -1 for no limit

Types
- Parameter cacsRole: std ::string
- Parameter saving: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter chunkSize: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter savetimeout: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setSubscriberPatternChunkSize(*args)¶
Setup parameters for the subscriber pattern with chunks used.

Parameters:

- cacsRole – name of the cacs role to use
- chunkSize – how many message to save per chunk, -1 for no limit
- savetimeout – how long to wait for a save at most, -1 for no limit
- changeReason – what change reason to use when saving

Types
- Parameter cacsRole: std ::string
- Parameter chunkSize: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter savetimeout: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter changeReason: std ::string
- Return type: void

setSubscriberPatternSaving(*args)¶
Setup parameters for the subscriber pattern with saving set.

Parameters:

- cacsRole – name of the cacs role to use
- changeReason – what change reason to use when saving

Types
- Parameter cacsRole: std ::string
- Parameter changeReason: std ::string
- Return type: void

setTestBinding(*args)¶
Use a test-provided bridge.

Parameters:

- isHandler – whether this is a handler or trigger
- bridgeName – name of the test bridge
- handlerName – name of the handler or trigger

Types
- Parameter isHandler: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter bridgeName: std ::string
- Parameter handlerName: std ::string
- Return type: void

setTimeServicePort(port)¶
Provide a port for time server communication.

Parameters:
port – port for time server

Types
- Parameter port: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setTriggerPattern(cacsRole)¶
Setup parameters for the trigger pattern.

Use the trigger pattern with default settings for test.

Parameters:
cacsRole – name of the cacs role to use

Types
- Parameter cacsRole: std ::string
- Return type: void

skipPlan()¶
Prepare a plan and ruleset configuration that will not load any ARA plan or ruleset.

Raises:
StaticError – if a plan has already been chosen

Types
- Return type: void

# 17.1.6. jcms.ioserver.testutils.version10.TestRunner

class jcms.ioserver.testutils.version10.runner_militaris.TestRunner(impl)¶
Describes an IO-server test runner object that keeps the whole functionality together for unittesting.

__init__(impl)¶
constructor

Types
- Parameter impl: std ::shared_ptr &lt; internal ::TestRunnerImpl  &gt;

begin(cid=0)¶
Start the testsuite by constructing the worker and preparing the plan.

Use defaults for all optional configuration that hasn’t been provided. This will call the handlers on_load if it exists.

Parameters:
cid – set the cid for which the worker will start work (Default=0 (latest))

Raises:

- StaticError – if some required configuration hasn’t been provided
- exception – if other errors occur (all errors are just forwarded to the test)

Types
- Parameter cid: ioserver ::CommitId
- Return type: void

bookmarkCurrentVersion(bookmarkName)¶
Bookmark the current mave version.

Sets a named bookmark on current mave version to be able to rollback to it with :meth:rollbackToBookmark. If a bookmark with this name already exists the old bookmark will be replaced with the current mave version.

Parameters:
bookmarkName – a bookmark name

Types
- Parameter bookmarkName: std ::string
- Return type: void

end()¶
clean up all resources, test suite is done. Will unload the plan.

Raises:
exception – if other errors occur (all errors are just forwarded to the test)

Types
- Return type: void

getPlan()¶
Access the loaded plan.

The PlanHolder object will always exist. It gives access to the loaded plan and ruleset if any.

Returns:
the plan

Types
- Return type: PlanPointer

process(callOnFault=False)¶
Process the prepared messages from the configured MessageSource.

Parameters:
callOnFault – set to true if the controller should call the service’s “on_fault” method if the “handler” method throws. Default is false, i.e. the exception from “handler” is propagated up into the test.

Types
- Parameter callOnFault: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

refresh()¶
Refresh the the loaded plan to latest cid.

Types
- Return type: void

reset(shouldRefresh=False)¶
Reset internal state (including the plan) to situation after begin() call this between tests within a testsuite.

Will also clean the memory queue.

Parameters:
shouldRefresh – set to true if the controller should perform a refresh as well as the reset (Default = false)

Types
- Parameter shouldRefresh: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

rollbackToBookmark(bookmarkName)¶
Rollback to a previous mave version.

Rollback to a mave version that was previously bookbacked with :meth:bookmarkCurrentVersion. The bookmark is deleted after rollback.

Parameters:
bookmarkName – a bookmark name

Raises:
exception – if bookmark doesn’t exists or the mave version is already pruned

Types
- Parameter bookmarkName: std ::string
- Return type: void

--- SUBPAGE: python_testutils_api_ver9_reference.html ---

# 17.2.1. jcms.ioserver.testutils.version9.main.TestMain

class jcms.ioserver.testutils.version9.main.TestMain(serviceName)¶
Describes an IO-server test runner object that keeps the whole functionality together for unittesting.

&#64;deprecated Use ioserver::testutils::TestMain instead.

__init__(serviceName)¶
constructor

Types
- Parameter serviceName: std ::string

getConfig()¶
Get the configuration object.

Returns:
a pointer to the global configuration. Use this to setup the ioserver parameters.

Types
- Return type: ::ioserver ::testbase ::internal ::version9 ::ITestConfig ::Pointer

getMemoryHAStore()¶
Get the memory HA store object.

Returns:
a pointer to the memory HA store object.

Types
- Return type: ::ioserver ::testbase ::internal ::version9 ::IMemoryHAStore ::Pointer

getMemoryQueue()¶
Get the memory global queue.

If the config was set to use memory queue then the handler will use this queue.

Returns:
a pointer to the global memory queue.

Types
- Return type: ::ioserver ::testbase ::internal ::version9 ::IMemoryQueue ::Pointer

getRunner()¶
Get the runner object.

After setting up the configuration the runner is initialized on first access.
The runner is the test engine of the IOServer, it will load the plan and
execute the service under test.

Once the runner has been obtained, the configuration will be locked,
all attempts to set more configuration values will result in an exception.

Returns:
a pointer to the runner object.

# 17.2.2. jcms.ioserver.testutils.version9.main.IMemoryHAStore

class jcms.ioserver.testutils.version9.main.IMemoryHAStore(*args, **kwargs)¶
This interface provides access to a memory based HA store for testing purposes.

The most commonly used HA store key is “generation”. It is used to specify the latest handled commit id.

&#64;deprecated Use ioserver::testbase::IMemoryHAStore instead.

__init__(*args, **kwargs)¶

clear()¶
Clear all internal state.

Types
- Return type: void

getValue(key)¶
Get a value from the HA key-value store.

Parameters:
key – The key for which to retrieve a value.

Returns:
The value associated with the given key.

Raises:
ioserver.base.StaticError – if there is no value for key.

Types
- Parameter key: std ::string
- Return type: std ::string

hasValue(key)¶
Check if there is a value in the HA key-value store for the given key.

Parameters:
key – The key to check for.

Types
- Parameter key: std ::string
- Return type: [bool](https://docs.python.org/3/library/functions.html#bool)

setValue(key, value)¶
Set a key-value pair in the HA key-value store.

Parameters:

- key – The key to write.
- value – The value associated with key.

Types
- Parameter key: std ::string
- Parameter value: std ::string
- Return type: void

# 17.2.3. jcms.ioserver.testutils.version9.main.IMemoryQueue

class jcms.ioserver.testutils.version9.main.IMemoryQueue(*args, **kwargs)¶
This interface provides access to the built in memory queue for testing purposes.

&#64;deprecated Use ioserver::testbase::IMemoryQueue instead.

__init__(*args, **kwargs)¶

addInputIOMessage(msg)¶
Add an IOMessage to the input queue.

Parameters:
msg – the input message

Returns:
index of message in the queue

Types
- Parameter msg: IOMessagePointer
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getDefaultInputContentType()¶
Get the default content type to use for new input messages.

Returns:
the default content type

Types
- Return type: std ::string

getDefaultInputEncoding()¶
Get the default encoding to use for new input messages.

Returns:
the default encoding

Types
- Return type: std ::string

getInputIOMessage(index)¶
Get the input message at given index.

Parameters:
index – the message index to get

Returns:
message at index

Types
- Parameter index: size_t
- Return type: IOMessagePointer

getInputIOMessages()¶
Get the current input queue content.

Returns:
list of the messages on the input queue

Types
- Return type: IOMessageList

getInputSize()¶
Get the size of input message queue.

Returns:
size of the input message list

Types
- Return type: size_t

getOutputIOMessage(index)¶
Get the output message at given index of default sink.

Parameters:
index – the message index to get

Returns:
message at index

Types
- Parameter index: size_t
- Return type: IOMessagePointer

getOutputIOMessageByName(sinkName, index)¶
Get the output message at given index.

Parameters:

- sinkName – name of the sink
- index – the message index to get

Returns:
message at index

Types
- Parameter sinkName: std ::string
- Parameter index: size_t
- Return type: IOMessagePointer

getOutputIOMessages()¶
Get the current output queue content of default sink.

Returns:
list of the messages on the output queue

Types
- Return type: IOMessageList

getOutputIOMessagesByName(sinkName)¶
Get the current output queue content.

Parameters:
sinkName – name of the sink

Returns:
list of the messages on the output queue

Types
- Parameter sinkName: std ::string
- Return type: IOMessageList

getOutputSize()¶
Get size of output message queue of default sink.

Returns:
size of the output message list

Types
- Return type: size_t

getOutputSizeByName(sinkName)¶
Get size of output message queue.

Parameters:
sinkName – name of the sink

Returns:
size of the output message list

Types
- Parameter sinkName: std ::string
- Return type: size_t

getStartId()¶
Types
- Return type: size_t

reset()¶
Reset content of input and output message lists.

Types
- Return type: void

setDefaultInputContentType(content_type)¶
Set the default content type to use for new input messages.

Parameters:
content_type – the content type

Types
- Parameter content_type: std ::string
- Return type: void

setDefaultInputEncoding(encoding)¶
Set the default encoding to use for new input messages.

Parameters:
encoding – the encoding

Types
- Parameter encoding: std ::string
- Return type: void

setInputIOMessages(msgVec)¶
Replace current input queue content with a new message list.

Parameters:
msgVec – list of messages to be put on the queue

Types
- Parameter msgVec: IOMessageList
- Return type: void

setStartId(index)¶
Provide a start value for generating the msgIds, default is 0.

Parameters:
index – start value for generating msgIds

Types
- Parameter index: size_t
- Return type: void

# 17.2.4. jcms.ioserver.testutils.version9.main.ITestConfig

class jcms.ioserver.testutils.version9.main.ITestConfig(*args, **kwargs)¶
Provides configuration for an IOServer mock-instance

The interface allows steering the mock implementation, chose which real components should be used and which others to replace by mock-objects (e.g memory queue instead of qpid)

&#64;deprecated Use ioserver::testbase::ITestConfig instead.

__init__(*args, **kwargs)¶

convertToMemoryQueues()¶
Convert configuration to use memory queues.

Convert all sources and sinks for service to use memory queues. Typically called after importProcessConfig.

Types
- Return type: void

debugPrint(*args)¶
Print the configuration content.

Types
- Parameter s: std ::ostream
- Return type: void

getDomainGeneration()¶
Retrieve the domain generation setting.

Returns:
the domain generation setting (“air1” or “air2”)

Types
- Return type: std ::string

getPlanBuilderName()¶
Retrieve the plan builder setting.

Returns:
the name of the plan builder types, typical “mave2”

Types
- Return type: std ::string

getProcessName()¶
Get the common config process name.

Returns:
process name

Types
- Return type: std ::string

getProcessServicePort(*args)¶
Get the service port to use for the process when communicating with sysmond.

Parameters:

- systemService – the system service to look up
- hostName – the host name to look up (default: use the current host name)
- processName – the process name (default: use the current process name)

Returns:
port number

Types
- Parameter systemService: std ::string
- Parameter hostName: std ::string
- Parameter processName: std ::string
- Return type: [int](https://docs.python.org/3/library/functions.html#int)

getRulesetType()¶
Get the ruleset type used.

Only valid for mave2 plans.

Returns:
Name of ruleset type to use (“rave”). Default is an empty string.

Types
- Return type: std ::string

getServiceNames()¶
Get the list of all service names.

Returns:
list containing all service names

Types
- Return type: StringVectorPointer

importProcessConfig(*args)¶
Import from system configuration.

Imports the settings for the tests serviceName from the configuration for the given IOServer process.

Parameters:

- process – the name of the IOServer process to copy from
- cfgFile – the name of the config root file if not standard.

Types
- Parameter process: std ::string
- Parameter cfgFile: std ::string
- Return type: void

setChangeReason(changeReason)¶
Set changeReason to use for save.

This is only relevant if saving has been set to true.

Parameters:
changeReason – what change reason to use when saving

Types
- Parameter changeReason: std ::string
- Return type: void

setConfigValue(path, value)¶
Set custom config value.

This is an “escape hatch” when all other convenience methods doesn’t provide the needed functionality.

Parameters:

- path – the path to the config value (xpathish)
- value – the value to set

Types
- Parameter path: std ::string
- Parameter value: std ::string
- Return type: void

setConflictDetectionStrategy(strategy)¶
Enable or disable conflict detection during save.

This is only relevant if saving has been set to true.

Parameters:
strategy – which conflict detection strategy to use.

Types
- Parameter strategy: ioserver ::base ::ConflictDetectionStrategy
- Return type: void

setCppBinding(isHandler, handlerName, pluginName)¶
Use a C++ bridge.

Parameters:

- isHandler – whether this is a handler or trigger
- handlerName – name of handler to instantiate
- pluginName – name of plugin (shared library) to load

Types
- Parameter isHandler: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter handlerName: std ::string
- Parameter pluginName: std ::string
- Return type: void

setCppHandlerBinding(handlerName, pluginName)¶
use C++ bridge handler

Parameters:

- handlerName – name of handler to instantiate
- pluginName – name of plugin (shared library) to load

Types
- Parameter handlerName: std ::string
- Parameter pluginName: std ::string
- Return type: void

setCppTriggerBinding(handlerName, pluginName)¶
use C++ bridge trigger

Parameters:

- handlerName – name of handler to instantiate
- pluginName – name of plugin (shared library) to load

Types
- Parameter handlerName: std ::string
- Parameter pluginName: std ::string
- Return type: void

setDatabase(*args)¶
Prepare the database connection configuration.

Prepare database connection configuration with explicit schema setup.

Parameters:

- connectString – the Dave connectstring to use
- dbschema – the schema name (default = “”)

Types
- Parameter connectString: std ::string
- Parameter dbschema: std ::string
- Return type: void

setDomainGeneration(*args)¶
Override the domain generation for the plan.

Parameters:

- domain – the domain generation string “air1” or “air2”
- planBuilder – name of a custom plan builder type, this requires a special driver lib that registers a driver with this name. Typical value is “mave2”.

Types
- Parameter domain: std ::string
- Parameter planBuilder: std ::string
- Return type: void

setErrorRetryCount(*args)¶
Set value for retry counters.

Note that TransientErrors are raised to the test even when retry is set, when calling handle again they might be resolved or transform into StaticError/MessageError when the retries are exhausted.

Parameters:
retry – how often to retry on transient errors (same for message and system erros)

Types
- Parameter retry: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setEventTriggerPattern(cacsRole)¶
Setup parameters for the eventtrigger pattern.

Use the eventtrigger pattern with default settings for test.

Parameters:
cacsRole – name of the cacs role to use

Types
- Parameter cacsRole: std ::string
- Return type: void

setMemoryQueue()¶
Setup configuration to use the builtin memory queue.

The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure. This is a convenience menthod that will set up a defult source queue and a defualt sink queue.

To set up named sinks, use :meth:setNamedMemorySink and :meth:setMemorySource

Types
- Return type: void

setMemorySource()¶
Setup configuration to use the default memory source queue.

The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure.

Types
- Return type: void

setMsgErrorStrategy(*args)¶
Define parameters that steer the error strategy for message related errors.

Parameters:
skipMsg – whether to remove a message from the inqueue if it failed, independent from context

Types
- Parameter skipMsg: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

setNamedMemorySink(sinkName)¶
Setup configuration to use a named memory sink queue.

The memory queue is a special test utility that allows the test to locally handle message flows without extra infrastructure.

Parameters:
sinkName – the name of the sink

Types
- Parameter sinkName: std ::string
- Return type: void

setNow(nowString)¶
Provide an override for now.

This will influence the datacontext selections as well as rave.

Parameters:
nowString – a valid Rave datetime expression as in basics::time::minutes_from_expr()

Types
- Parameter nowString: std ::string
- Return type: void

setPersistCid(value)¶
Set persist_cid property.

Parameters:
value – If persist_cid should be set to “true” or “false”.

Types
- Parameter value: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

setPlan(*args)¶
Prepare the plan configuration.

Use this to specify a datacontext but no ruleset.

Parameters:

- datacontext – the name of the datacontext to load
- snapshotpath – path to snapshot location for this datacontext this will be given to the plan factory if provided.

Types
- Parameter datacontext: std ::string
- Parameter snapshotpath: std ::string
- Return type: void

setPortBase(port)¶
Provide a base port for sysmond communication.

Parameters:
port – base port for sysmmond

Types
- Parameter port: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setPythonBinding(*args)¶
Use a python bridge.

Parameters:

- isHandler – whether this is a handler or trigger
- protocol – the name of the message protocol (plain or soap)
- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter isHandler: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter protocol: std ::string
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setPythonHandlerPlainBinding(*args)¶
Use python bridge with plain handler.

Parameters:

- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setPythonHandlerSoapBinding(*args)¶
Use python bridge with a soap xml handler.

Parameters:

- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setPythonTriggerPlainBinding(*args)¶
Use python bridge with a plain trigger.

Parameters:

- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setPythonTriggerSoapBinding(*args)¶
Use python bridge with a soap xml trigger.

Parameters:

- moduleName – the python module that implements the service
- handleMethod – the main handle method to call if this is a handler
- databindingName – the databinding module to use

Types
- Parameter moduleName: std ::string
- Parameter handleMethod: std ::string
- Parameter databindingName: std ::string
- Return type: void

setQpid(host, port, queueName, prefetchCapacity=0, compress=False, maxContentSize=0)¶
Setup parameters for qpid.

Use this to run tests against real ActiveMQ queues.

Parameters:

- host – the host to connect to ActiveMQ
- port – the port on host
- queueName – the queue name to work on
- prefetchCapacity – the prefetch capacity of qpid receiver
- compress – the switch for compressing the content of the message
- maxContentSize – the maximum content size of the message compressed or not.

Types
- Parameter host: std ::string
- Parameter port: std ::string
- Parameter queueName: std ::string
- Parameter prefetchCapacity: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter compress: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter maxContentSize: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setQpidMessageSink(*args)¶
Setup parameters for qpid message sink.

Use this to run tests with real ActiveMQ queues.

Parameters:

- brokerHost – ActiveMQ broker host address
- brokerPort – ActiveMQ broker host port
- queueName – queue name to use
- sinkName – name of this sink. Default sets default sink
- senderCapacity – Number of messages to buffer up when using asynchronous send(). Default 0 (synchronous send)
- compress – set to true if the message should be gzipped. Default false
- maxContentSize – Maximum content size. Default 0

Types
- Parameter brokerHost: std ::string
- Parameter brokerPort: std ::string
- Parameter queueName: std ::string
- Parameter sinkName: std ::string
- Parameter senderCapacity: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter compress: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter maxContentSize: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setQpidMessageSource(brokerHost, brokerPort, queueName, prefetchCapacity)¶
Setup parameters for qpid message source.

Use this to run tests against real ActiveMQ queues.

Parameters:

- brokerHost – ActiveMQ broker host address
- brokerPort – ActiveMQ broker host port
- queueName – queue name to use
- prefetchCapacity – number of messages to prefetch in the background

Types
- Parameter brokerHost: std ::string
- Parameter brokerPort: std ::string
- Parameter queueName: std ::string
- Parameter prefetchCapacity: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setRequestResponsePattern(cacsRole, saving=False)¶
Setup parameters for the request/response pattern.

Use the request/response pattern with default settings for test.

All messages in the inqueue will be handled before returning. No retry will be attempted and any exceptions from the handler or surrounding modules will just be raised up to the calling test.

This doesn’t affect the pattern-neutral error strategy settings, like global retries (default 3 ) or skipmessage (default true).

Parameters:

- cacsRole – name of the cacs role to use
- saving – if the plan should be saved

Types
- Parameter cacsRole: std ::string
- Parameter saving: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

setRuleset(*args)¶
Prepare the ruleset configuration.

Parameters:

- ruleset – the name of the global ruleset to load
- parameterset – the name of the parameter set to load, if empty no parameters are set

Types
- Parameter ruleset: std ::string
- Parameter parameterset: std ::string
- Return type: void

setRulesetType(rulesetType)¶
Set the ruleset type that will be used.

Only valid when using mave2 based plans.

Parameters:
rulesetType – name of ruleset type to use. Requires that a driver lib has registered a driver with support for this ruleset. Typical value is “rave” (for rave::Ruleset type).

Types
- Parameter rulesetType: std ::string
- Return type: void

setServiceValue(path, value)¶
Set custom config value for service.

This is an “escape hatch” when all other convenience methods doesn’t provide the needed functionality.

Parameters:

- path – the path to the config value relative the service root (xpathish)
- value – the value to set

Types
- Parameter path: std ::string
- Parameter value: std ::string
- Return type: void

setSubscriberPattern(cacsRole, saving=False, chunkSize=1, savetimeout=10)¶
Setup parameters for the subscriber pattern.

Use the subscriber pattern with default settings for test.

All messages in the inqueue will be handled before returning. No retry will be attempted and any exceptions from the handler or surrounding modules will just be raised up to the calling test.

This doesn’t affect the pattern-neutral error strategy settings, like global retries (default 3 ) or skipmessage (default true).

Parameters:

- cacsRole – name of the cacs role to use
- saving – whether the plan should be saved after handling the messages, default false.
- chunkSize – how many message to save per chunk, -1 for no limit
- savetimeout – how long to wait for a save at most, -1 for no limit

Types
- Parameter cacsRole: std ::string
- Parameter saving: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter chunkSize: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter savetimeout: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setSubscriberPatternChunkSize(*args)¶
Setup parameters for the subscriber pattern with chunks used.

Parameters:

- cacsRole – name of the cacs role to use
- chunkSize – how many message to save per chunk, -1 for no limit
- savetimeout – how long to wait for a save at most, -1 for no limit
- changeReason – what change reason to use when saving

Types
- Parameter cacsRole: std ::string
- Parameter chunkSize: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter savetimeout: [int](https://docs.python.org/3/library/functions.html#int)
- Parameter changeReason: std ::string
- Return type: void

setSubscriberPatternSaving(*args)¶
Setup parameters for the subscriber pattern with saving set.

Parameters:

- cacsRole – name of the cacs role to use
- changeReason – what change reason to use when saving

Types
- Parameter cacsRole: std ::string
- Parameter changeReason: std ::string
- Return type: void

setTestBinding(*args)¶
Use a test-provided bridge.

Parameters:

- isHandler – whether this is a handler or trigger
- bridgeName – name of the test bridge
- handlerName – name of the handler or trigger

Types
- Parameter isHandler: [bool](https://docs.python.org/3/library/functions.html#bool)
- Parameter bridgeName: std ::string
- Parameter handlerName: std ::string
- Return type: void

setTimeServicePort(port)¶
Provide a port for time server communication.

Parameters:
port – port for time server

Types
- Parameter port: [int](https://docs.python.org/3/library/functions.html#int)
- Return type: void

setTriggerPattern(cacsRole)¶
Setup parameters for the trigger pattern.

Use the trigger pattern with default settings for test.

Parameters:
cacsRole – name of the cacs role to use

Types
- Parameter cacsRole: std ::string
- Return type: void

skipPlan()¶
Prepare a plan and ruleset configuration that will not load any ARA plan or ruleset.

Raises:
StaticError – if a plan has already been chosen

Types
- Return type: void

# 17.2.5. jcms.ioserver.testutils.version9.TestRunner

class jcms.ioserver.testutils.version9.runner_militaris.TestRunner(*args)¶
Describes an IO-server test runner object that keeps the whole functionality together for unittesting.

&#64;deprecated Use ioserver::testutils::TestRunner instead.

__init__(*args)¶
constructor

Types
- Parameter impl: std ::shared_ptr &lt; internal ::TestRunnerImpl  &gt;

begin(*args)¶
Start the testsuite by constructing the worker and preparing the plan.

Use defaults for all optional configuration that hasn’t been provided. This will call the handlers on_load if it exists.

Parameters:
cid – set the cid for which the worker will start work (Default=0 (latest))

Raises:

- StaticError – if some required configuration hasn’t been provided
- exception – if other errors occur (all errors are just forwarded to the test)

Types
- Parameter cid: ioserver ::CommitId
- Return type: void

bookmarkCurrentVersion(*args)¶
Bookmark the current mave version.

Sets a named bookmark on current mave version to be able to rollback to it with :meth:rollbackToBookmark. If a bookmark with this name already exists the old bookmark will be replaced with the current mave version.

Parameters:
bookmarkName – a bookmark name

Types
- Parameter bookmarkName: std ::string
- Return type: void

end(*args)¶
clean up all resources, test suite is done. Will unload the plan.

Raises:
exception – if other errors occur (all errors are just forwarded to the test)

Types
- Return type: void

getPlan(*args)¶
Access the loaded plan.

The PlanHolder object will always exist. It gives access to the loaded plan and ruleset if any.

Returns:
the plan

Types
- Return type: PlanPointer

process(*args)¶
Process the prepared messages from the configured MessageSource.

Types
- Return type: void

refresh(*args)¶
Refresh the the loaded plan to latest cid.

Types
- Return type: void

reset(*args)¶
Reset internal state (including the plan) to situation after begin() call this between tests within a testsuite.

Will also clean the memory queue.

Parameters:
shouldRefresh – set to true if the controller should perform a refresh as well as the reset (Default = false)

Types
- Parameter shouldRefresh: [bool](https://docs.python.org/3/library/functions.html#bool)
- Return type: void

rollbackToBookmark(*args)¶
Rollback to a previous mave version.

Rollback to a mave version that was previously bookbacked with :meth:bookmarkCurrentVersion. The bookmark is deleted after rollback.

Parameters:
bookmarkName – a bookmark name

Raises:
exception – if bookmark doesn’t exists or the mave version is already pruned

Types
- Parameter bookmarkName: std ::string
- Return type: void

--- SUBPAGE: logging.html ---

# 18. IOServer logs

## 18.1. Configuring logging

The recommended way to set up logging from the IOServer is to use jcmslog’s TcpAppender, and log to a rsyslogd server.

Using a jcmslog FileAppender is possible, but log file rotation is not supported. This is due to the fact that the
IOServer consists of several processes, that all log to the same file; if one of them rotated the log, the others would
not notice, and would therefore be unable to continue logging.

## 18.2. Flow

A flow is an identifier that is written as prefix in the lines of the log.
Each integration service has its own separate flow name,
which makes it possible to find all log lines for a particular service.
How much and which information that is included in the log is set by the log level of that flow.

## 18.3. Logging from an IOService

The service context provides a logger, version10.context.ServiceContext.service_logger(), to log from within a service.
This logger can be used as an ordinary logger from the standard Python logging module.

def handle(planholder, service_context):
    logger = service_context.service_logger
    logger.debug(u&quot;Debug message&quot;)
    logger.warning(u&quot;Warning message&quot;)

This prints the messages in the IOServer log file on the flow:

ioserver.&lt;service_name&gt;.service

where &lt;service_name&gt; is the configured name of the service.

Note
Print statements are not visible when running an IOService in the IOServer.

## 18.4. Getting the correct log level for an integration service

The name of the logging flow for an integration service is based on the name of the service in the configuration,
or more precisely the name attribute of the ioservice element found in the file:

.../usr/etc/programs/ioservice/\*.xml

Example:

&lt;ioservice name=&quot;flight_schedule&quot;&gt;
  &lt;pattern&gt;
    &lt;class&gt;subscriber&lt;/class&gt;
    &lt;cacs_role&gt;Administrator&lt;/cacs_role&gt;
    &lt;changereason&gt;Other&lt;/changereason&gt;
  &lt;/pattern&gt;
&lt;binding&gt;

The flow name follows the pattern in the example below:

Example:

ioserver.flight_schedule.service

To enable a specific log level on a flow, add or modify a flow element in the file:

.../usr/etc/programs/ioserver.xml

For the flow element, set the name attribute to the flow name and the level attribute to the desired log level.
Then restart the service.
The following example sets the log level to debug for the flight_schedule service:

Example:

&lt;jcmslog&gt;
  &lt;flow name=&quot;ioserver.flight_schedule.handler&quot; level=&quot;DEBUG&quot;/&gt;
&lt;/jcmslog&gt;

For a general description with more details of logging, see the Jcmslog documentation.

### 18.4.1. Log level contents

Level

Description

DEBUG

Flow information on a detailed level (&lt;15&gt;).

Examples:

Info about choices that depend on data in the database,
for example if a leg in a trip was found or created.

- Info about modified data in the database.
- Info about the data in the database that is processed.
- Which internal parts of the source code is being run.

INFO

Flow information on a high level (&lt;14&gt;).

Examples:

- Start and end of processing a message.
- Which crew is processed, for multi-crew messages.
- Which part of a complex message that is processed.

WARNING

Info about potential problems, which is not severe
or is automatically recovered, that is fall backs (&lt;12&gt;).

Examples:

- Overwrites an already existing CSDL file.
- Could not write an optional attribute on a database object.

ERROR

Information of occurred errors (&lt;11&gt;).

Examples:

- Internal errors, like failing components or connections.
- Errors in input data.
- Failed conditions on database data.
- Missing catalog data, for example base or aircraft type.
- Failed business checks.

Note that a higher log level in the table also contains all the lower levels,
and that INFO is the default.

## 18.5. Connecting log entries to messages

The message id (msgId) and current commit id (cid) are included in all IOServer log lines where
applicable. This can be used to track a certain interesting message in logs of other system,
or finding the actual message content.

## 18.6. Log format

The log messages follow the syslog format (RFC 5424).

&lt;14&gt;1 2016-10-26T18:38:41.386Z hostname process_name 9469 OPER [details@38555 cid=&quot;44&quot; msgId=&quot;apa-bepa-cepa&quot; service=&quot;ReserveCoverageHandler&quot; flow=&quot;ioserver.Something&quot;] Doing good stuff.
^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^ ^^^^^^^^^^^^ ^^^^                     ^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^
|     |                        |        |            |                        |        |                     |                                |
|     Date                     |        Process name Pid                      |        Message id            IOServer service name            Log flow name
Log level                      Host name                                      Current plan generation

--- SUBPAGE: testutils.html ---

# 19. IOServer TestUtils

The IOServer TestUtils package available in the ioserver.sdk component provides a convenient way
to create component tests for IOServer plugins like handlers and triggers. It allows the developer to run the plugin
in much the same way as it would run in a real IOServer, but without a forking main process.
Any exception that is raised during the execution of the handler will first be handled internally but then
raised further to the test to allow checking for error conditions without relying on side-effects.

The TestUtils API has historically been versioned in a different cycle than the IOServer API itself.
Beginning with version 9 they will use the same numbering.
The current version is version 10, available in jcms.ioserver.testutils.version10.main.

Each major of TestUtils is tightly connected to one major
of the IOServer API itself by the fact that the PlanHolder that can be obtained from the TestRunner
is of a certain version.
This is only applicable for the API exposed to the test itself. It is possible to test plugins of any supported
version with TestUtils of any supported version.

## 19.1. How to use TestUtils

To use TestUtils for testing, a test class is needed based on unittest2.TestCase.
In the setUpClass method we instantiate the TestUtils TestMain class.
To access the configuration we use getConfig() which returns
an ITestConfig.
The configuration is then set with necessary values for the tests such as database,
handler binding, pattern and queue.

When configuration is ready a TestRunner
is received from the function getRunner(). The runner can
then be started by calling begin().

Example of setup class and configuration settings:

from jcms.ioserver.testutils.version10 import main
from jcms.ioserver.version10.message import PlainIOMessage

class TestMain(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestMain, cls).setUpClass()
        cls._main = main.TestMain(&quot;TestMockInterface&quot;)
        # initialize configuration
        cfg = cls._main.getConfig()
        cfg.setDatabase(&quot;profile:default&quot;)
        cfg.skipPlan()
        cfg.setPythonHandlerPlainBinding(&quot;helloWorldService&quot;,&quot;&quot;)
        cfg.setSubscriberPattern(&quot;myRole&quot;, False)
        cfg.setMemoryQueue()
        cfg.setDomainGeneration(&quot;air2&quot;, &quot;mave2&quot;)
        # obtain runner and start
        cls._runner = cls._main.getRunner()
        cls._runner.begin()

For each test setUp() method should be called on the parent class unittest2.TestCase.
Example of setup:

def setUp(self):
    super(TestMain, self).setUp()

To be able to run a simple test, a message must be put on the input queue.
TestUtils provides a simple memory queue IMemoryQueue that can be used for testing purposes.

When the message is on the queue, the runner can process() the message.
Example of a test case:

def testMsgOk(self):
    io_msg = PlainIOMessage.create_io_message(&quot;Hello world&quot;)
    queue = self._main.getMemoryQueue()
    queue.addInputIOMessage(io_msg)
    self._runner.process()
    self.assertEqual(1, queue.getOutputSize())
    self.assertEqual(0, queue.getInputSize())
    msg = queue.getOutputIOMessage(0)
    self.assertEqual(&quot;Hello World&quot;, msg.getContent())

For every test the function reset() should be called on the runner.
This will empty the queue and refresh the plan if needed.
Example of tear down:

def tearDown(self):
    self._runner.reset(False)
    super(TestMain, self).tearDown()

Finally the resources should be cleaned up with the end() method
which unloads the plan.
Tear down class:

@classmethod
def tearDownClass(cls):
    cls._runner.end()
    super(TestMain, cls).tearDownClass()

### 19.1.1. How to setup initial data to reuse between tests

One use case for testutils is that there exist a schema that should not be altered (skipsave should be used).
This shema contains most of the data needed for the test suite, but a small adjustment is needed.

This can be made by setting a bookmark called initalLoad after the modification.
The initialLoad bookmark is used as reset point by reset()
when skipsave is configured.

@classmethod
def setUpClass(cls):
    super(TestMain, cls).setUpClass()
    cls._main = main.TestMain(&quot;TestMockInterface&quot;)
    # initialize configuration
    cfg = cls._main.getConfig()
    cfg.setDatabase(&quot;profile:default&quot;)
    cfg.setPythonHandlerPlainBinding(&quot;helloWorldService&quot;,&quot;&quot;)
    cfg.setSubscriberPattern(&quot;myRole&quot;, False)
    cfg.setMemoryQueue()
    cfg.setDomainGeneration(&quot;air2&quot;, &quot;mave2&quot;)
    # obtain runner and start
    cls._runner = cls._main.getRunner()
    cls._runner.begin()

    planHolder = cls._runner.getPlan()
    araPlan = planHolder.getMave2Plan()
    # Do the relevant changes on the araPlan
    cls._runner.bookmarkCurrentVersion(&#39;initialLoad&#39;)

### 19.1.2. Logging with testutils

To enable logging with testrunner the easiest way may be to use jcmslogs python api.

import jcms.log
jcms.log.config.set_log_level(&#39;ioserver&#39;, logging.DEBUG)

# 20. Configuration only relevant for testing

Some configuration elements are only (or mainly) relevant for testing
handlers or the IOServer itself. They are documented in this section
for completeness.

## 20.1. datamodel

The datamodel element has a few settings that are only or mainly
relevant for test.

Element

Type

Description

skipplan

boolean

Whether plan handling shall be
skipped.

skipsave

boolean

Whether to skip saving the plan.

## 20.2. pattern

Test-specific settings for pattern.

Element

Type

Description

skipsave

boolean

Whether to skip saving the plan.
Deprecated, use &lt;datamodel&gt;&lt;skipsave&gt;

## 20.3. simulated time

It is possible to use simulated time for testing, debugging, or simulations without changing the
system time of the server.

Warning
Simulated time must not be used in production.

Simulated time allows IOServer to behave as if the current time was different, or as if
time progressed in another pace.

For instance, it is possible to run regression tests with a fixed data set. Even if
a report is generated for the current month, the result is always the same.
Another example is to reproduce a defect that occurrs only at midnight etc.

Simulated time is enabled by setting a fixed time in the configuration, or by using an external
time server. In both cases, the data context used when loading a plan and the Rave now keyword
are changed according to the simulated time.

A fixed time means that “time stands still” during the lifetime of IOServer.

Using a time server allows both to set a time offset and make the simulated time progress
faster or slower. The time server settings can be changed during the lifetime of IOServer.

### 20.3.1. Simulated time configuration

There are three modes of now time:

If the datamodel/now element is set in the configuration, IOServer uses this fixed time assimulated now time.

- If a system service “time” is configured, IOServer uses that for simulated time.

If none of these above are set, IOServer defaults to Unix time. This is the onlypermitted option for a production system.

A time server has to be started from Sysmond. Below is an example how to
configure a time server:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; ?&gt;
&lt;!--
  A time server controls the time (diff, speed) in simulations.
--&gt;
&lt;program name=&quot;timeserver&quot;&gt;
  &lt;log_path&gt;%(programs/sysmond/log/directory)&lt;/log_path&gt;

  &lt;process name=&quot;simulated_time&quot;&gt;
    &lt;service name=&quot;time&quot; protocol=&quot;http&quot;/&gt;

    &lt;start_cmd&gt;clock --server&lt;/start_cmd&gt;
    &lt;stop_cmd&gt;&lt;/stop_cmd&gt;

    &lt;start_time&gt;15Nov2012 08:42&lt;/start_time&gt;
    &lt;speed&gt;1&lt;/speed&gt;

    &lt;log_level&gt;INFO&lt;/log_level&gt;
    &lt;log_file&gt;${CARMTMP}/logfiles/clock&lt;/log_file&gt;
    &lt;log_stdout&gt;true&lt;/log_stdout&gt;
  &lt;/process&gt;
&lt;/program&gt;

### 20.3.2. Limitations

- The time server must run at the same host as IOServer.
- The time server must be started before IOServer.
- now can never be set to a year before 1986.
- now can never be set to later than 06Feb2036.

--- SUBPAGE: metrics.html ---

# 21. IOServer Metrics

## 21.1. Process metrics

ioserver.etables.load_duration_ms

Type:
timer

Tags:

- process [processName]

Description:
How long it took to preload etables from the database.

ioserver.etables.refresh_duration_ms

Type:
timer

Tags:

- process [processName]

Description:
How long it took to refresh etables from the database.

ioserver.plan.load_duration_ms

Type:
timer

Tags:

- process [processName]

Description:
How long it took to load the plan from the database.

ioserver.ruleset.load_duration_ms

Type:
timer

Tags:

- process [processName]

Description:
The load duration for the ruleset.

ioserver.parameters.load_duration_ms

Type:
timer

Tags:

- process [processName]

Description:
The load duration of the rave parameter set.

ioserver.plan.refresh_count

Type:
counter

Tags:

- process [processName]
- result [changed, unchanged, transient_failure, failure]

Description:
Number of plan refreshes.
Tag result indicates the outcome of the refresh.

ioserver.plan.refresh_duration_ms

Type:
timer

Tags:

- process [processName]

Description:
How long it took to refresh the plan from the database.

ioserver.worker.start_count

Type:
counter

Tags:

- process [processName]

Description:
Number of times an IOServer worker process has started.

ioserver.worker.terminate_count

Type:
counter

Tags:

- process [processName]
- result [success, timeout, error, signal]

Description:
Number of times an IOServer worker process has stopped.
result indicates how the worker terminated.

ioserver.main.prevent_outdated_spawn_count

Type:
counter

Tags:

- process [processName]

Description:
If a service tries to spawn a new worker based on a plan
generation older than the last saved plan generation it
will be prevented (if it is configured to do so). This metric
will increase once per prevented generation.

ioserver.start_count

Type:
counter

Tags:

- process [processName]

Description:
Number of times an IOServer main process has started.

ioserver.terminate_count

Type:
counter

Tags:

- process [processName]

Description:
Number of times an IOServer main process has stopped.

ioserver.worker_factory.start_count

Type:
counter

Tags:

- process [processName]

Description:
Number of times an IOServer worker factory process has started.

ioserver.worker_factory.terminate_count

Type:
counter

Tags:

- process [processName]
- result [success, timeout, error, signal]

Description:
Number of times an IOServer worker factory process has stopped.
result indicates how the worker factory terminated.

ioserver.main.service_status

Type:
gauge

Tags:

- service [serviceName]

Description:
The state of the tagged service:
0: Not started
1: Active
2: Stopped
3: Failed
4: Broken
5: Unresponsive
6: Degraded

## 21.2. Service metrics

ioserver.plan.save_count

Type:
counter

Tags:

- service [serviceName]
- result [success, conflict_error, other_error]

Description:
Number of times the plan has been saved.
Tag result indicates the outcome of the save operation.

ioserver.plan.save_duration_ms

Type:
timer

Tags:

- service [serviceName]

Description:
How long it took to save the plan to the database.

ioserver.trigger.event_duration_ms

Type:
timer

Tags:

- service [serviceName]

Description:
How long it took to run a trigger (i.e. its on_event method).

ioserver.trigger.event_count

Type:
counter

Tags:

- service [serviceName]
- result [success, failure]

Description:
Number of times that a trigger has run (i.e. its on_event method).

ioserver.trigger.processed_cid

Type:
gauge

Tags:

- service [serviceName]

Description:
The CID successfully processed by a trigger service.

ioserver.service.reactivate_count

Type:
counter

Tags:

- service [serviceName]

Description:
Number of times a service has been reactivated after being
deactivated because of an error.

ioserver.activemq.message.outgoing_commit_count

Type:
counter

Tags:

- service [serviceName]
- sink [sinkName]
- result [success, failure]

Description:
Number of committed (added to queue) messages in a message sink, e.g.
response messages.
result indicates if the commit was successful, or if the messages
were discarded (failure).

ioserver.activemq.message.incoming_commit_count

Type:
counter

Tags:

- service [serviceName]
- result [success, failure]

Description:
Number of committed (deleted from queue) messages in a message source.
result indicates if the commit was successful, or if the messages
were rolled back (because of failure, not included in
incoming_rollback_count).

ioserver.activemq.message.incoming_rollback_count

Type:
counter

Tags:

- service [serviceName]
- result [success, failure]

Description:
Number of rolled back (returned to queue) messages in a message source.

ioserver.activemq.message.incoming_fetch_count

Type:
counter

Tags:

- service [serviceName]

Description:
Number of fetched (read from queue) messages from a message source.

ioserver.message.process_count

Type:
counter

Tags:

- service [serviceName]
- result [success, failure]
- phase [fetch, check_state, security_context, handle, save]

Description:
Number of times that messages has been processed by a service.
result indicates if processing was successful or not. If
result is failure, phase indicates at which part of the
handling process the failure occurred.

ioserver.message.sent_count

Type:
counter

Tags:

- service [serviceName]
- result [success, failure]

Description:
Number of messages sent (e.g. response messages).

ioserver.message.fetched_bytes

Type:
timer

Tags:

- service [serviceName]

Description:
Fetched message size in bytes, implemented as a timing.

ioserver.message.handle_duration_ms

Type:
timer

Tags:

- service [serviceName]

Description:
How long it took to process a message in a handler
(e.g. the handle() method).

ioserver.message.sent_bytes

Type:
timer

Tags:

- service [serviceName]

Description:
Sent message size in bytes, implemented as a timing.

ioserver.message.block_count

Type:
counter

Tags:

- service [serviceName]

Description:
Number of times message processing has failed and
it has been decided to keep the message on the incoming queue.

ioserver.message.skip_count

Type:
counter

Tags:

- service [serviceName]

Description:
Number of times message processing has failed and it has been
decided to delete the message from the incoming queue.

ioserver.ipc.command_communication_duration_ms

Type:
timer

Tags:

- service [serviceName]

Description:
IPC timer for worker to communicate and handle response messages.

--- SUBPAGE: message_retention.html ---

# 22. Message Retention

Message retention is a feature that is used to store incoming and outgoing messages together with
metadata about the messages in a searchable storage (MongoDB).

An IOService handler (or trigger) can specify metadata on a message object using the set_meta method.
The parameter to this method is a dictionary containing JSON compatible values.

The IOService needs to set the meta_enabled property on the message object to True for a
retention message to be generated by the IOServer. In this way it is possible to separate the
logic of generating the metadata from the logic that decides if message retention should be enabled
for a particular message.

Finally, the IOService needs to be configured with where to send retention messages.
This is done either on the &lt;ioservice&gt; tag (for one IOService) or on the &lt;process&gt; tag
(for all IOServices in that process). Configuration on the &lt;ioservice&gt; tag
takes precedence over configuration on the &lt;process&gt; tag. If no such configuration
is found, the feature is disabled. Thus it is possible to disable the message retention feature
through the configuration instead of modifying the service.

## 22.1. Example Content of a Metadata Message

All of these values is regarding the original message’s data.
The retention message can for example have their own headers.

{
    &quot;version&quot;: 1,  // Message retention format version.
    &quot;content&quot;: &quot;bXlfY29udGVudA==&quot;,  // Original message content Base64 encoded.
    &quot;content_type&quot;: &quot;my_content_type&quot;,
    &quot;content_encoding&quot;: &quot;my_encoding&quot;,
    &quot;message_id&quot;: &quot;my_id&quot;, // Original message ID
    &quot;headers&quot;: {
        // Original message headers (ActiveMQ).
    },
    &quot;created&quot;: {
        // Relaxed extended JSON for datetime support in MongoDb. Needed for TTL.
        &quot;$date&quot;: &quot;2021-03-16T13:44:11Z&quot;
    },
    &quot;application_context&quot;: {
        &quot;ioserver&quot;: &quot;my_process&quot;,
        &quot;ioservice&quot;: &quot;my_service&quot;,

        // Either incoming or outgoing
        &quot;direction&quot;: &quot;incoming&quot;,

        // Order of the retention message
        &quot;send_count&quot;: 1,

        &quot;save_cid&quot;: 333,  // Last saved commitid.
        &quot;plan_cid&quot;: 222,  // Worker generation.
        &quot;now_time&quot;: &quot;2021-03-16T13:44:00Z&quot;
    },
    &quot;business_context&quot;: {
        // Set by message.set_meta() in handler/trigger (any JSON).
    }
}

Keys in content

Meaning &amp; Comments

version

Version of the message retention structure.

content

Content of the original message encoded in Base64.

content_type

Type of content for the original message.

content_encoding

Content encoding for the original message.

message_id

Original message’s message id.

headers

Header fields for the original message.

created

ISO-8601 formatted timestamp of when the IOServer created the retention message.

application_context

See table below for description of Application Context keys.

business_context

This could be any JSON set by the IOService implementation intended for business purposes.

## 22.2. Application Context

Keys

Meaning &amp; Comments

ioserver

Name of the IOServer process that handled the message.

ioservice

Name of the IOService that handled the message.

direction

If it is regarding an “incoming” or “outgoing” message.

send_count

Counter of number of messages sent in a trigger/handle call,
eg. to sort multiple messages generated by a trigger.

save_cid

The commit id which was saved by the handler.
Only set for incoming and response messages. If omitted then no save occured.

plan_cid

The commit id of the plan when the trigger/handle generated the message.

now_time

“Now time” of the plan in ISO-8601 format.
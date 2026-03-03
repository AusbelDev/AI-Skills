## Contents

### Overview


* [IO server](#io-server)
* [Interface Builder](#interface-builder)
* [Standard and Custom Interfaces](#standard-and-custom-interfaces)
* [Integrator](#integrator)
* [Jobrunner](#jobrunner)
* [Summary](#summary)

A crew tracking system will always have a number of interfaces to external systems for different purposes, for example:

* Receive flight schedule information from flight planning and operations systems
* Receive flight movement information from aircraft and airports
* Send crew data to and from HR and payroll systems
* Send trip and roster information between JCT and the rostering system
* Create and send ticket reservations and hotel bookings

##### [IO server](#id1)

Interfaces in JCT are realized within the IO server framework.

A number of IO server processes are running in the system. An IO server process runs a number of services, where each service is configured to handle an interface. A service always uses ActiveMQ message queues for input and output. Processes, services and message queues are configured using XML in the JCT XML configuration.

The IO server main process loads the plan from the JCT database and repeatedly does a refresh from the database. After each refresh, main process forks subprocesses for each service. A service may have one or more parallel worker processes depending on the expected usage pattern.

[![../_images/Slide2.PNG](../_images/Slide2.PNG)](../_images/Slide2.PNG)

There are a number of IO server processes in a JCT system. An example setup is:

* ioserver\_batch - services that do not need high availability support since they are only used for batch processing
* ioserver\_singleton - services that can only run in one instance at a time
* ioserver\_web - services used by Crew Access and TIC
* ioserver\_datafeeds - services used by external services (none batch interfaces)
* ioserver\_historical - used by Report Manager to generate reports containing historical data.

When implementing a service, there are a number of different patterns to choose from:

[![../_images/Slide1.PNG](../_images/Slide1.PNG)](../_images/Slide1.PNG)

**Subscriber**
:   A subscriber service reads from an input queue, processes the message and writes to the JCT database. The client of the service does not expect any response. Flight schedule and movement messages are examples of interfaces that are implemented with the subscriber pattern.

**Request/response**
:   A request/response service reads from an input queue, processes the message, optionally saves data in the JCT database and sends a response on an output queue. Most interfaces are implemented using the this pattern, for example roster, trip and crew input and output interfaces.

**Trigger**
:   A trigger service examines the changes in the JCT database since last refresh and writes messages on an output queue or saves data in the database, based on what changes there are. Triggers are used for sending out information to e.g. ticket and hotel reservation systems and crew facing applications when rosters change.

**Repeating trigger**
:   A repeating trigger service runs at specified time intervals and writes messages on an output queue or saves data in the database, depending on the contents of the database. Repeating triggers are typically used for generating scheduled reports to e.g. HR and payroll systems.

Patterns can also be combined. For example, a common usage scenario is to have a trigger service that creates a request for a request/response service. The output queue for the trigger is the input queue for the request/response service.

##### [Interface Builder](#id2)

The interface builder is a tool for building interfaces where the message payload is based on XML. The message syntax can be based on either pure XML or SOAP. Both the interface specification and implementation is defined using an XML based domain specific lanuage - CSDL. The CSDL language allows interface and implementation to be separated from each other. It also has constructs for defining customized extensions to both interface and implementation.

Based on the CSDL specification, the Interface Builder will generate interface definitions in the form of WSDL or XSD files, to be used by clients, as well as an IO server service handler script. The configuration of the IO service will point out the handler script.

[![../_images/Slide3.PNG](../_images/Slide3.PNG)](../_images/Slide3.PNG)

##### [Standard and Custom Interfaces](#id3)

There are a number of predefined standard interfaces in the JCT core product, for example for:

* Airport Data import
* Flight schedule import
* Flight movements import
* Flight export
* Trip import and export
* Crew data import and export
* Roster import and export
* Plan synchronization
* Crew messages
* Crew check-in

The standard interfaces are described in detail in [Standard Interfaces](../std_interfaces/index.html#stdif-index)

When defining the interfaces in a customization project, there are a number of options:

**Use a standard interface**
:   Using a standard interface requires a very minor configuration effort in the customization layer. The interface need to be defined, but no CSDL code or other form of adaptation is needed.

**Extend a standard interface**
:   It is also possible to define a new interface that is based on a standard interface. This requires that some customization CSDL code is written. The customized interface inherits the standard interface.

**Write a CSDL based interface from scratch**
:   The Interface Builder can also be used to write a customer specific interface from scratch. This requires that all CSDL code is written in the customization layer.

**Write a non-CSDL based interface**
:   For non-CSDL based interfaces, service handler needs to be handcrafted. The handler should implement a service handler API defined by the IO server. Handlers for triggers and repreating triggers always need to be implemented using this method, since trigger patterns are not supported by the Interface Builder. For request/response and subscriber interfaces, there are often requirements that input or output should follow non-XML legacy formats. This is another example of a case when a non-CSDL based interface handler needs to be implemented.

##### [Integrator](#id4)

The IO server always uses message queues for communication. In most cases there are requirements that input/output is handled using other endpoint types, for example importing/exporting files, SOAP or plain HTTP requests/responses, outgoing HTTP requests for outbound interfaces or FTP transfers.

The main purpose with the Integrator component is to route input and output between the IO server message queues and the preferred endpoints. The Integrator is also used to transform messages between external message formats and Jeppesen standard interface formats.

The Integrator is a WildFly application server with Apache Camel - a Java framework for implementing enterprise integration patterns - installed. Using the concept of routes and contexts in Camel, messages can be routed to any type of endpoint. Routes in the Integrator are defined with XML.

[![../_images/Slide4.PNG](../_images/Slide4.PNG)](../_images/Slide4.PNG)

##### [Jobrunner](#id5)

Jobrunner is a framework for scheduling and manually running interface jobs, for example file exports and imports. Jobs are started and monitored from a web user interface. Jobrunner is implemented as two IO server services - one SOAP web service for reading configuration and starting jobs and a trigger service that starts jobs based on the schedule in the configuration. Static configuration is defined in python code and Apach Camel routes. Information about running jobs is stored in a simple presistent key-value store.

Each type of job needs to be defined in the customization implementation. Job configuration consists of two parts:

* Static job definitions
  :   Job name, job parameters, default values and lists of permissible parameter values is defined in python code.
* Job implementation
  :   The implementation of the job, i.e. what actions to take, consists of a Camel route. The route will call the appropriate IO service and also call the Jobrunner SOAP web service to update the status of running jobs.

[![../_images/Slide5.PNG](../_images/Slide5.PNG)](../_images/Slide5.PNG)

##### [Summary](#id6)

The Standard Interfaces, IO server, Integrator, and Jobrunner are the core components that enables customized interface development in an implementation project.

The customer implementation layer will need the following:

* Interfaces
  :   + CSDL specification/implementation or hand-written interface handlers.
* IO server configuration
  :   + Configuration of IO services, defining services, mapping services to interface handlers
      + Configuration of message queues
* Integrator
  :   + Defining Camel routes and endpoints for services
      + Defining Camel routes for Jobrunner jobs
* Jobrunner
  :   + Defining jobs, custom handling of e.g. parameter values and default values.

#### IO server

#### Interface Builder

#### Standard and Custom Interfaces

#### Integrator

#### Jobrunner

#### Summary

### Creating a standalone custom interface


This chapter describes the steps needed to write a pure request/response or subscriber custom interface (not built by the SMOG/IOService Builder or the IFBuilder tools) to be run by the IOServer.

See the [IOServer](../ioserver/main/index.html#ioserver-index) documentation for reference information.

* [Defining a handler](#defining-a-handler)
* [Configuration](#configuration)
* [Testing the interface](#testing-the-interface)

##### [Defining a handler](#id1)

The main difference between writing an interface using the IFBuilder and writing standalone interface is that in the latter case, a handler script needs to be written - it will not be generated automatically.

A python module should to be defined in `$CARMUSR/lib/python/datafeeds/<interface name>/`, e.g. request\_handler.py.

The module need to implement `handler_interface_version` and a handler method, which are called from the IOServer.
The module may optionally implement an `on_fault` method.

See [Handler interface](../ioserver/main/handlers.html#handler-top).

The handler method name is given by:

* For a SOAP-XML handler, the name is read from the SOAPAction message header. (Having standalone SOAP XML handlers will not be very common.)
* For a plain text handler, the name is read from the handler configuration, `binding/operation`. The default name is handle.

###### Implementing the handler

Example of a handler implementation using the plain data format:

```
from jcms.ioserver.versions import InterfaceVersion
from jcms.ioserver.version10.actions import PlanAction, FaultAction

def handler_interface_version():
    """
    Define the ioserver interfaces version
    """
    return InterfaceVersion.TEN

def on_fault(planholder, service_context, excp):
    error_response = "Failed to handle request with error: %s" % excp
    io_message = service_context.create_io_message(error_response, encoding='utf-8')
    service_context.response_message = io_message
    return FaultAction.SEND_RESPONSE

def handle(planholder, service_context):
    try:
        request_body = service_context.request_message.content
        response_body = handle_request(request_body)
        io_message = service_context.create_io_message(response_body, encoding='utf-8')
        service_context.response_message = io_message

        return PlanAction.UNCHANGED
    except Exception as e:
        service_context.service_logger.exception("Failed to handle request: %s", str(e))
        raise ios_exceptions.SkipMsgError(e)
```

The `handle` method is called whenever a request message is available and it receives two arguments:

* The planholder provides access to the ARA plan and Rave session.
* The service context contains e.g.
  :   + Member variables for the request and response message, making it possible for the handler to read the request and write the response.
        To return a message, the handler should set the `response_message` of the `service_context` argument.
      + Methods for creating messages
      + A logger object, making it possible to log from the service handler.

To return a message, the handler sets the `response_message` of the `service_context` argument.

The handler should return one of these constants, indicating how the IO server should handle any possible changes to the plan that the handler has done:

`PlanAction.UNCHANGED`
:   no changes in the plan, nothing needs to be saved

`PlanAction.SAVE`
:   changes in the plan need to be saved

`PlanAction.ROLLBACK`
:   changes in the plan must be rolled back.

When the plan action has been executed successfully, any provided response message is sent out
and the request is removed from the source (input) queue.

The [IOServer Python API reference](../ioserver/main/python_api_reference.html#ioserver-api-ref) is used to get access to the IOServer version, public constants, exceptions, the IOServer configuration, return actions, the message and the ARA plan.

##### [Configuration](#id2)

See [Configuration](../ioserver/main/configuration.html#ioserver-configuration).

To configure an interface to be run by the IOServer, an service needs to be defined by a configuration xml file in `$CARMUSR/usr/etc/programs/ioservices/datafeeds/`. The file and the IO service should have the same name and they should be named with an interface name, prefixed by `df_` (as in datafeeds) and suffixed by the direction of the interface, either `_in` or `_out`, for example `df_crew_data_in.xml` or `df_layover_out.xml`.

The service configuration file needs to be included by a specific IOServer process xml file, for example `ioserver_datafeeds.xml` in
`$CARMUSR/usr/etc/programs/`. New IOServer processes can also be defined if there is a need for it.

Example:

```
<include href="${CARMUSR}/etc/programs/ioservices/datafeeds/df_preassignments_out.xml" />
```

An example of a service configuration file is shown below.

```
<ioservice name="df_preassignments_out">
  <pattern>
    <class>requestresponse</class>
    <cacs_role>interface</cacs_role>
    <changereason>Other</changereason>
  </pattern>
  <binding>
    <language>python</language>
    <handler>datafeeds.df_preassignments_out.request_handler</handler>
    <protocol>plain</protocol>
  </binding>
  <source>
    <class>qpid</class>
    <queue_reference>to.ioservice.df_preassignments_out</queue_reference>
  </source>
  <sink>
    <class>qpid</class>
    <queue_reference>to.camelroute.export_preassignments</queue_reference>
  </sink>
</ioservice>
```

The pattern `class` element indicates that this is a request/response interface.

The `binding` element points out the implementation code that handles the requests. The handler represents the python module that contains the implementation of the service handler. It is possible to write handlers in C++, but all customer specific handlers should be written in python. The handler should implement an interface defined by the IO server component. The interface is different for different service patterns.

The protocol can be either `plain` or `soap`.

For each service, a `source` message queue and a `sink` message queue should be defined. For request/response services, responses are sent to the sink. For subscriber services, only error messages are sent to the sink.

##### [Testing the interface](#id3)

The [IOService builder](../ioservice_builder.doc/index.html#ioservice-builder-index) provides a test class `IOServiceTestBase` that makes it easy to test standalone custom IOServices. The framework is based on Python unit tests and the following example shows how to test the service once it has been added to a service configuration as shown above.

```
from ioservice_builder.testsupport import IOServiceTestBase

class TestPreassignmentsService(IOServiceTestBase):

    ioserver_name = "ioserver_datafeeds" # name of the IOServer process that provides the IOServer to test.
    ioservice_name = "df_preassignments_out" # name of the IOService to test
    schema_name = "tiny" # Name of Firebird schema to use, must exist as $CARMTMP/firebird/unit_test/<schema_name>.fdb

    def test_something(self):
        # Create a request message on a format that the custom handler understands
        request = "CREWID: 12345, MONTH: MAR2020"

        # Put the message on the IOService source queue
        self.put_msg(request)

        # Let the IOService process messages on the source queue
        self.testrunner.process()

        # Get content and headers for the response message from the IOService sink queue
        content, headers = self.get_msg()

        # Assert response message
        self.assertEquals(content, ...)
        self.assertHeaders(headers, ...)
```

#### Defining a handler

##### Implementing the handler

#### Configuration

#### Testing the interface

### Creating a trigger service


This chapter describes the steps needed to write a trigger service to be run by the IOServer. Triggers cannot be implemented using IFBuilder.

See the [IOServer](../ioserver/main/index.html#ioserver-index) documentation for reference information.

* [Defining a handler](#defining-a-handler)
* [Configuration](#configuration)

##### [Defining a handler](#id1)

A python module should to be defined in `$CARMUSR/lib/python/datafeeds/triggers/<trigger name>/`, e.g. `handler.py`.
The module need to implement `handler_interface_version`, an `on_event` method and optionally an `on_load` method, which are called from the IOServer.

See [Trigger interface](../ioserver/main/triggers.html#trigger-top).

###### Implementing the trigger handler

Example of a handler implementation using the plain data format:

```
from jcms.ioserver.versions import InterfaceVersion
from jcms.ioserver.version9.actions import PlanAction

def handler_interface_version():
    """
    Define the ioserver interfaces version
    """
    return InterfaceVersion.TEN

def on_load(planholder, context):
    pass

def on_event(planholder, service_context):

    finder = BookingOperationFinder(planholder.getMave2ChangeSet(), planholder.getPlan())
    booking_ops = finder.find_booking_operations()

    # Generate messages and send requests
    if len(booking_ops) > 0:
        generator = MessageGenerator(planholder.getMave2Plan(), service_context)
        for booking_op in booking_ops:
            message  = generator.generate_message(planholder, booking_op)
            generator.send_message(message)
            booking_op.set_sent_status(planholder.getMave2Plan())

        return PlanAction.SAVE

      return PlanAction.UNCHANGED
```

The `on_load` method is called after the IO server main process has finished the initial load of data from the database.

The `on_event` method is called by the IO server after each refresh, or in the case of repreating triggers, with the specified time interval.

The `on_event` method receives two arguments:

* The planholder provides access to the ARA plan and Rave session. For triggers, the plan holder also provides the changeset, i.e. a table-by-table difference between the current state of the data and the state after the previous call to on\_event.
* The service context contains e.g.
  :   + Member variable for the response message, making it possible for the handler to write the response.
        To return a message, the handler should set the response\_message of the service\_context argument.
      + Methods for creating messages
      + A logger object, making it possible to log from the service handler.

The purpose of the `on_event` method is to deduce what messages to send to the sink queue, from the changeset provided by the planholder (for triggers) or from the current state of the plan (for repeating triggers).

The handler should return one of these constants, indicating how the IO server should handle any possible changes to the plan that the handler has done:

`PlanAction.UNCHANGED`
:   no changes in the plan, nothing needs to be saved

`PlanAction.SAVE`
:   changes in the plan need to be saved

`PlanAction.ROLLBACK`
:   changes in the plan must be rolled back.

In the example above, records of sent messages is maintained in the database, and the trigger will instruct the IO server to save the changes it has made if the `on_event` method has processed any data. However, most triggers will be “read-only” and return `PlanAction.UNCHANGED`.

When the plan action has been executed successfully, any provided response message is sent to the sink queue.

The [IOServer Python API reference](../ioserver/main/python_api_reference.html#ioserver-api-ref) is used to get access to the IOServer version, public constants, exceptions, the IOServer configuration, return actions, the message and the ARA plan.

###### Creating the response

The response message can have any format - the format is entirely defines by the requirements of the receiver of the sink message.

In the simple example below, the content of the message is a plain text string. The outgoing message also has a property `example_header`.

```
def on_event(planholder, service_context):

    content = "12345"
    io_message = service_context.create_io_message(content, contentType="text/plain", encoding='US-ASCII')
    io_message.set_property("example_header", "ABC")
    service_context.send(io_message)
    return PlanAction.UNCHANGED
```

The IO server API also has support for creating XML messages. It is not uncommon that the output of the trigger is input to a request/response service.

In the following example, the message created by the trigger is sent to the source of a request/response service created with the IFBuilder. The service handler of the request/response service holds the XSD as a member variable. An XML content factory is created by the trigger handler and used to build a request message for the request/response service.

```
import jcms.ioserver.version9.LxmlContent as ContentModel
import ioservice_impl.ticket_reservation_output_1_0_ext.ticketreservationoutput_handler as handler_module

def generate_message(self, planholder):

    content_factory = ContentModel.LxmlContentFactory(handler_module.xsd, tnsname="tns")
    request_node = content_factory.makeNode("TicketReservationRequestMsg", "ticketReservationRequest")
    request_node.setValue("version", "1.0")
    request_node.setValue("source", "df_ticket_res_out_trigger")
    request_node.setValue("created", self.now)

    #
    # ...more content filled in here...
    #
```

##### [Configuration](#id2)

See [Configuration](../ioserver/main/configuration.html#ioserver-configuration).

> To configure a trigger to be run by the IOServer, a service needs to be defined by a configuration xml file in
> `$CARMUSR/usr/etc/programs/ioservices/datafeeds/`. A good convention is to let the file and the IO service should have the same name and name them with `df_` followed by a name of the trigger ,and suffixed with `_trigger`, for example `df_roster_state_out_trigger.xml`.

The service configuration file needs to be included by a specific IOServer process xml file, for example `ioserver_singleton.xml` in
`$CARMUSR/usr/etc/programs/`. New IOServer processes can also be defined if there is a need for it.

Example:

```
<include href="${CARMUSR}/etc/programs/ioservices/datafeeds/df_ticket_res_out_trigger.xml" />
```

Note that triggers must never run in multiple workers or processes at the same time. Typically there will be an IOServer process (e.g. `ioserver_singleton.xml`) that runs services that must always have exactly one worker.

An example of a service configuration file is shown below.

```
<?xml version="1.0" encoding="ISO-8859-1" ?>
<!-- IOService definition for crew seat booking trigger -->
<ioservice name="df_ticket_res_out_trigger">

  <pattern>
    <class>trigger</class>
    <cacs_role>interface</cacs_role>
    <changereason>Other</changereason>
  </pattern>

  <binding>
    <language>python</language>
    <trigger>datafeeds.triggers.ticket_res_out_trigger.handler</trigger>
    <protocol>plain</protocol>
  </binding>

  <sink>
    <class>qpid</class>
    <queue_reference>to.camelroute.export_ticket_reservation</queue_reference>
    <capacity>0</capacity>
  </sink>

  <persist_cid>true</persist_cid>
  <hastore>
    <class>consul</class>
  </hastore>

  <worker_time_out>360</worker_time_out>
  <worker_pool_size>1</worker_pool_size>

</ioservice>
```

The pattern class element indicates that this is a trigger.

The `binding` element points out the implementation code that handles the requests. The `handler` represents the python module that contains the implementation of the trigger. It is possible to write handlers in C++, but all customer specific handlers sshould be written in python. The handler should implement an interface defined by the IO server component. The interface is different for different service patterns.

The protocol can be either `plain` or `soap`.

For each service, a sink message queue should be defined. Triggers do not need a source message queue, since they react on changes in the database and not on input messages.

The `persist_cid` and `hastore` elements specify that he service should maintain the commit id from the database, to make sure that no changes will be skipped. The commit id will be stored in Consul, which is a distributed key-value and service discovery store.

#### Defining a handler

##### Implementing the trigger handler

##### Creating the response

#### Configuration

### IOService builder


The purpose of this document is to describe the how to use IOService builder, a tool that can be used for developing IOServices.

* [1. Introduction](ioservice_builder.html)
* [2. Building IOServices](ioservice_builder.html#building-ioservices)
  + [2.1. Subscriber and request/response patterns](ioservice_builder.html#subscriber-and-request-response-patterns)
  + [2.2. Trigger and repeatingtrigger pattern](ioservice_builder.html#trigger-and-repeatingtrigger-pattern)
  + [2.3. Managed subscription pattern](ioservice_builder.html#managed-subscription-pattern)
* [3. Configuration templates](ioservice_builder.html#configuration-templates)
* [4. Type conversions in service mapping](ioservice_builder.html#type-conversions-in-service-mapping)
* [5. Testing IOServices](ioservice_builder.html#testing-ioservices)
  + [5.1. Request/Response and Subscriber pattern](ioservice_builder.html#request-response-and-subscriber-pattern)
  + [5.2. Trigger pattern](ioservice_builder.html#trigger-pattern)
  + [5.3. Running tests](ioservice_builder.html#running-tests)

##### Indices and tables

* [Index](../genindex.html)
* [Search Page](../search.html)

#### Introduction


IOServer is the main application used for deploying backend services in JCMS. Services provided by an IOServer are called IOServices. An IOService typically fetch input request message from a source queue, handles message by applying business logic and produce output response message to a response queue.

The IOService Builder is a tool that simplifies development of IOServices by using SMOG for defining the services. The tool use SMOG for generating service implementation classes but also Python handlers that can be deployed in the IOServer.

The IOService Builder is replacing the ifbuilder tool, which is deprecated and should not be used for new development.

#### Building IOServices


IOServies to build are declared in `$CARMUSR/data/config/ioservice_builder.xml`.

Each IOService provides one SMOG service on a specific protocol. This is done by specifying the service name, version and protocol as used in the referenced SMOG files.

```
<?xml version="1.0" encoding="UTF-8"?>
<build-ioservices xmlns="http://namespace.jeppesen.com/ioservice_builder_v1">
  <ioservice pattern="requestresponse">
    <description>IOService providing the Flight service version 1 on xml protocol.</description>
    <smog-service name="Flight" version="1" protocol="plainxml">
        <service-spec location="$CARMUSR/data/config/smog/flight/service.xml"/>
        <protocol-spec location="$CARMUSR/data/config/smog/flight/protocol.xml"/>
        <service-mapping location="$CARMUSR/data/config/smog/flight/server_mapping.xml"/>
    </smog-service>
  </ioservice>
</build-ioservices>
```

The IOServices are automatically build when the system is configured with atriumorc. It’s also possible to build the IOServices from the command line:

```
$CARMSYS/bin/ioservice_builder
```

As a result the following artifacts are built:

* IOService Python handlers: `$CARMTMP/lib/python/ioservice_impl`
* SMOG service implementation classes: `$CARMTMP/lib/python/ioservice_impl/<target>`, where `<target>` is specified in the service mapping.
* Service contracts: `$CARMTMP/ioservice_builder/contract/<target>`, where `<target>` is specified in the protocol specification.
* IOService configuration templates: `$CARMTMP/ioservice_builder/config_template`

The pattern of each IOService must be specified in `ioservice_builder.xml` since it affects how the Python handler is generated.
IOService builder supports the following IOService patterns.

###### 2.1. Subscriber and request/response patterns

These are the main patterns used for deploying a back end service implementations in the IOServer.

```
<ioservice pattern="subscriber|requestresponse" default_exception="SkipMsgError|TransientMsgError|BlockingMsgError">
    <description>IOService providing the Flight service version 1 on xml protocol.</description>
    <smog-service name="Flight" version="1" protocol="plainxml">
        <service-spec location="$CARMUSR/data/config/smog/flight/service.xml"/>
        <protocol-spec location="$CARMUSR/data/config/smog/flight/protocol.xml"/>
        <service-mapping location="$CARMUSR/data/config/smog/flight/server_mapping.xml"/>
    </smog-service>
</ioservice>
```

IOServices are automatically named based on the SMOG service they provide, the example above would build an IOService named Flight\_1\_plainxml. The `<ioservice>` element can optionally specify a `name` to override the default name of the IOService.

The SMOG service mapping must be of type `<server-impl>` with language set to Python. Parameters `planholder` and `service_context` must be provided as `<runtime-parameters>`.

```
<service-mapping language="Python" target="air2_macao" xmlns="http://namespace.jeppesen.com/smog/v1">
    <server-impl service_name="Flight" service_version="1">
        <runtime-parameters>
            <parameter name="planholder" desc="Plan holder instance from IOServer"/>
            <parameter name="service_context" desc="Service context instance from IOServer"/>
        </runtime-parameters>
    </server-impl>
</service-mapping>
```

The attribute `default_exception` specifies what IOServer exception to raise in case of errors other than `jcms.ioserver.IOSError`
(or descendants thereof), or `ParseMsgError` as raised by SMOG if message parsing fails. Request messages are skipped (ignored) by
raising `SkipMsgError` if no other default exception type is specified. It’s recommended to use `TransientMsgError` for services where race
conditions and message order dependency applies. The exception type `TransientMsgError` forces the IOServer to refresh the plan before
retrying to handle it again. See error handling of the IOServer for more information.

IOServices of these pattern must be configured to use default queues for source, sink and errors using the following a specific naming convention:

* **Source queue**: `to.ioservice.<ioservice-name>`
* **Sink queue**: `from.ioservice.<ioservice-name>`
* **Error sink queue**: `from.ioservice.<ioservice-name>.error`

###### 2.2. Trigger and repeatingtrigger pattern

This pattern is used for deploying outbound interfaces, producing data
repeatedly or when events occur in the plan.

```
<ioservice name="flight_trigger" pattern="trigger|repeatingtrigger" handler_module="datafeeds_ext.triggers.flight_trigger_handler">
    <description>A trigger calling the Flight_1_plainxml service when a flight is updated in the plan.</description>
    <smog-service name="MyService1" version="1.0" protocol="soap">
        <service-spec location="$CARMUSR/data/config/smog/flight/service.xml"/>
        <protocol-spec location="$CARMUSR/data/config/smog/flight/protocol.xml"/>
        <service-mapping location="$CARMUSR/data/config/smog/flight/client_mapping.xml"/>
    </smog-service>
</ioservice>
```

IOServices using the trigger pattern must specify a Python handler module that implements
at least the IOServer `on_event` function. Additionally it is possible to also provide `on_load` and `on_fault` functions.

The functions can either import the SMOG client class and use it for generating the request messages on the service protocol,
or letting the generated handler pass the SMOG client by adding the additional `client` argument.
If additional dependencies have been declared, those are passed in as well (in order of declaration) if further parameters are added.

```
def on_load(planholder, service_context, client):
    pass

def on_event(planholder, service_context, client):
    client.make_getFlights_request(plan=planholder.getPlan(),
                                   changeset=planholder.getMave2ChangeSet())
    msg = service_context.create_io_message(client.request_payload)
    service_context.send_to_sink(msg, "from.ioservice.flight_trigger")
    return PlanAction.ROLLBACK

def on_fault(planholder, service_context, exception, client):
    return FaultAction.NO_RESPONSE
```

To create input messages for a standard interface, the SMOG service mapping should be
of type `<client-impl>` with language set to Python. Any parameters are allowed as `<runtime-parameters>`,
it is the responsibility of the handler module to call the smog service with correct parameters.
Usually it specifies either `planholder` and `service_context`,
or a parameter `plan` for the ARA plan and `changeset` for the Mave changeset
used for identifying what messages to produce.

```
<service-mapping language="Python" target="air2_macao" xmlns="http://namespace.jeppesen.com/smog/v1">
    <client-impl service_name="Flight" service_version="1">
        <runtime-parameters>
            <parameter name="plan" desc="ARA Plan."/>
            <parameter name="changeset" desc="Mave changeset."/>
        </runtime-parameters>
    </client-impl>
</service-mapping>
```

To create the same messages as an existing requestresponse interface, the trigger can either use a client mapping
as above to produce request messages and place them on the requestresponse input queue
or the handler module can invoke the server mappings directly after placing a request in the service\_context.

###### 2.3. Managed subscription pattern

A managed subscription is an IOService with pattern `trigger` or `repeatingtrigger` that sends a subset of data to receiving systems,
managing the subscription on behalf of that system. For a more in depth explanation of the pattern see the chapter
*Subscription Management* in the std-interfaces documentation.
A managed subscription differs from a basic trigger in the fact that it captures information about the subscription itself,
and that it can emit delta and load messages in the same run to ensure strict ordering of messages that are emitted.

```
<ioservice name="flight_opswindow" pattern="trigger|repeatingtrigger" >
    <description>A trigger sending flight data for a daily moving operational window.</description>
    <subscription>
      <moving name="moving" before="0:00" after="48:00" floor="day" time_of_day="0:30"/>
      <filter name="period" />
    </subscription>
    <delta-service name="MyFlightService1" version="1.0" protocol="soap"
       method="make_updateFlights_request">
        <service-spec location="$CARMUSR/data/config/smog/flight/service.xml"/>
        <protocol-spec location="$CARMUSR/data/config/smog/flight/protocol.xml"/>
        <service-mapping location="$CARMUSR/data/config/smog/flight/delta_mapping.xml"/>
        <parameter name="source" value="Me"/>
    </delta-service>
    <load-service name="MyFlightService1" version="1.0" protocol="soap"
       method="make_updateFlights_request">
        <service-spec location="$CARMUSR/data/config/smog/flight/service.xml"/>
        <protocol-spec location="$CARMUSR/data/config/smog/flight/protocol.xml"/>
        <service-mapping location="$CARMUSR/data/config/smog/flight/load_mapping.xml"/>
        <parameter name="source" value="Me"/>
    </load-service>
</ioservice>
```

The delta and load mappings should have `<runtime-parameters>` that are recognized by the pattern,
which is currently the following list:

* planholder: planholder from ioserver
* service\_context: service context from ioserver
* plan: the ARA plan from planholder
* changeset: current changeset from planholder
* now\_time: now time from planholder
* service\_logger: service logger from service context
* subscription\_manager: subscription manager, this is also available as `service_context.subscription_manager`

Additional parameters required for the method invocation must be constants and
declared in the load|delta-service element, as illustrated by the source parameter above.

```
<service-mapping language="Python" target="air2_macao" xmlns="http://namespace.jeppesen.com/smog/v1">
    <client-impl service_name="Flight" service_version="1">
        <runtime-parameters>
            <parameter name="planholder" desc="Plan holder instance from IOServer"/>
            <parameter name="service_context" desc="Service context instance from IOServer"/>
            <parameter name="source" desc="message source name from configuration"/>
        </runtime-parameters>
    </client-impl>
</service-mapping>
```

A subscription manager is a `subscription.Manager` instance and the member `manager.filter` encapsulates the
active subscription filter. It is expected that the delta mapping produces message(s) for all changes
in the changeset that are accepted by the filter and the load mapping should produce message(s)
for a full state of the plan data accepted by the filter.

In case of triggers that require more logic than simple invocation of the smog services,
e.g. preparing a request for a server implementation, it is possible to use a
`handler_module` as for basic triggers. In that case the `method`,``parameter`` and
`default_sink` configuration in the delta and load services are ignored
and the handler module is responsible to initialize the `subscription.TriggerBase`
before invoking its `on_event` method which will run through the phases.
It is also possible to create a class that inherits
from `subscription.TriggerBase` to override more behavior. Have a look at a
generated trigger and the documentation of the `subscription.TriggerBase` class for
the required logic. To get the generated smog service instances passed in, it is
possible to have additional parameters in the functions, e.g. `delta_service, load_service` or `*services`.
Service instances are always passed in the same order independent of the naming of the additional parameters,
first all delta services, then all load services and finally additional dependencies if any.

```
from jcms.ioservice_builder.subscription import TriggerBase

def on_event(planholder, service_context, delta_service,load_service=None):
    # prepare the default subscription
    if service_context.subscription_manager.configuration_empty():
        cfg = service_context.subscription_manager.get_config()
        cfg.update({ 'schedule' : 'gliding', 'filter' : 'period',
        "params" : {'before' : "30,00:00", 'after' : "60,00:00", 'floor' : "day" }})
        service_context.subscription_manager.save()

    # register a request
    request_message = delta_service.GetStuffRequest( version = delta_service.version,
        source = 'Me', created = planholder.getNowTime())
    request_message.set_name('getStuffRequest')
    request_payload = delta_service.format(request_message)
    service_context.request_message = self.service_context.create_io_message(request_payload,
        contentType = "text/xml", encoding = delta_service.encoding)

    # prepare the handler
    handler = TriggerBase(service_context.subscription_manager)
    handler.register_delta_service(delta_service,delta_service.operation_getStuff,
        request_payload=request_payload, request_headers={}, source='Me')
    if load_service is not None:
        handler.register_load_service(load_service,load_service.operation_getStuff,
            request_payload=request_payload, request_headers={}, source='Me')

    # run the handler
    handler.on_event(planholder, service_context)
    return PlanAction.ROLLBACK
```

For such a service, the `subscription` can still be used in the `ioservice_builder.xml`
to override the default subscription setup in the trigger. Settings provided in the
configuration are applied before the triggers `on_event` function is called, so that
`subscription_manager.configuration_empty()` will be false and the default settings are not applied.

##### Subscriber and request/response patterns

##### Trigger and repeatingtrigger pattern

##### Managed subscription pattern

#### Configuration templates


A template configuration is generated for each IOService. The template can be used as a starting point for getting the IOService configuration correct.

**Note!** It’s important to understand that the configuration must be tailored for each IOService. Values, such as time to live, messaging persistence, large message handling etc. must still be configured for each service.

#### Type conversions in service mapping


The IOService builder provides support for working with AbsTime, AbsDate and RelTime objects in the service mapping. The following methods can be imported and used in the service mapping for parsing incoming values.

```
<input-mapping struct="Message">
    <import name="ioservice_builder.functions.abstime" alias="abstime" />
    <import name="ioservice_builder.functions.absdate" alias="absdate" />
    <import name="ioservice_builder.functions.reltime" alias="reltime" />

    <assign name="my_abstime" expr="abstime(@{struct}.datetimeValue)" />
    <assign name="my_absdate" expr="absdate(@{struct}.dateValue)" />
    <assign name="my_reltime" expr="reltime(@{struct}.durationValue)" />
</input-mapping>
```

#### Testing IOServices


IOService Builder provides a test class `IOServiceBuilderTestBase` that makes it easy to test the built IOServices. The framework is based on Python unit tests and the following example shows how to test an IOService.

###### 5.1. Request/Response and Subscriber pattern

```
from ioservice_builder.testsupport import IOServiceBuilderTestBase

class TestFlightService(IOServiceBuilderTestBase):

    ioserver_name = "ioserver_all" # name of the IOServer process that provides the IOServer to test.
    ioservice_name = "Flight_1_plainxml" # name of the IOService to test
    schema_name = "tiny" # Name of Firebird schema to use, must exist as $CARMTMP/firebird/unit_test/<schema_name>.fdb

    # imports the service module generated by SMOG and sets the SMOG service class to test.
    def setSmogService(self):
        from ioservice_impl.air2_macao.Flight_1_server import ServiceFlight_plainxml
        self.smog_service = ServiceFlight_plainxml()

    def test_request_response(self):
        # Use the SMOG service class for creating a request message for the operation
        request = self.smog_service.create_struct_getFlightStatus(airline="JP", number=2)

        # Put the message on the IOService source queue
        self.put_msg(request)

        # Let the IOService process messages on the source queue
        self.testrunner.process()

        # Get content and headers for the response message from the IOService sink queue
        content, headers = self.get_msg()

        # Assert response message
        self.assertXmlEqual(content, ...)
        self.assertHeaders(headers, ...)
```

###### 5.2. Trigger pattern

```
from ioservice_builder.testsupport import IOServiceBuilderTestBase
import jcms.ara.air as ara_air

class TestTriggerService(IOServiceBuilderTestBase):

    ioserver_name = "ioserver_singleton"  # name of the IOServer process that provides the IOServer to test.
    ioservice_name = "flight_trigger" # name of the IOService to test
    schema_name = "tiny" # Name of Firebird schema to use, must exist as $CARMTMP/firebird/unit_test/<schema_name>.fdb
    skipsave = False # Indicate that we are going to save changes to the plan, a copy of the Firebird schema is used.

    def test_trigger_handler(self):
        # Use ARA for creating a flight leg in the plan
        ara_air.FlightLeg.create(self.plan)

        # Save the updated plan and refresh the IOServer.
        self.plan.getSession().save()
        self.testrunner.refresh()

        # Let the IOService handle the updated plan, on_event function the handler_module is called.
        self.testrunner.process()

        # Get content and headers for message(s) from the IOService sink queue
        content, headers = self.get_msg(sink_queue="from.ioservice.flight_trigger")

        # Assert response message
        self.assertXmlEqual(content, ...)
        self.assertHeaders(headers, ...)
```

###### 5.3. Running tests

The IOService Builder provides a tool that can be used for running Python unit tests. The tool is run from the command line:

```
$CARMSYS/bin/ioservice_testrunner discover <path1> <path2> ...
```

where `<path1>` and `<path2>` are directories containing the Python unit tests.

####### 5.3.1. Full synopsis of `ioservice_testrunner`

```
ioservice_testrunner discover [-w WORKER_THREADS -t TIMEOUT -s START_DIR -v -d -j] PATHS

ioservice_testrunner -c FULL_CLASS_NAME


Discovers Python unit test classes in PATHS and runs tests.


positional arguments:

 paths Path to directories to test.


optional arguments:

 -h, --help show this help message and exit

 -c FULL_CLASS_NAME Full name of the class to test, for example "datafeeds.my_service.test.MyServiceTestClass".


discover:

 Optional arguments

 -w WORKER_THREADS Number of worker threads to use for parallel testing.

 -t TIMEOUT Timeout for each discovered test class in seconds.

 -s START_DIR Top level Python directory of project.

 -v More verbose output.

 -d Collect and show deprecation warnings.

 -j Output results in json format.

 -p Pattern to match test files (*test*.py default).
```

##### Request/Response and Subscriber pattern

##### Trigger pattern

##### Running tests

###### Full synopsis of ioservice_testrunner

#### Indices and tables

### Integrator

#### Purpose


The purpose of the Integrator is to allow external systems to communicate with JCMS.
The Integrator provides entry points for exposing JCMS services to external systems.

#### Overview

#### Integrator features


###### 3.1. Camel routes

The Integrator supports using [Camel Routes](http://camel.apache.org/book-getting-started.html#BookGettingStarted-routes) for routing messages between JCMS internal [endpoints](http://camel.apache.org/book-getting-started.html#BookGettingStarted-endpoint) and endpoints exposed to or by external systems.
Where endpoints are Rest-services, webservices, queue-systems, ftp-servers etc.

Camel Routes are defined using the [Camel XML language](http://camel.apache.org/xml-reference.html). The integrator runs all Camel Routes defined for the Camel Contexts called `clusterroutes`, `noderoutes`, and `message_retention_routes`.
The routes are specified in the following files:

```
$CARMUSR/integrator/routes/clusterroutes.xml
$CARMUSR/integrator/routes/noderoutes.xml
$CARMUSR/integrator/routes/message_retention_routes.xml (optional)
$CARMSYS/integrator-site/routes/message_retention_routes.xml (default, used if the corresponding file does not exist in the $CARMUSR)
```

Routes defined in the `clusterroutes` Camel Context are only active on one node in the JBoss/Wildfly cluster at the time, this ensures
messages are routed between the endpoints in correct order.

Routes defined in the `noderoutes` Camel Context are activated on all nodes in the JBoss/Wildfly cluster at the same time, hence messages are routed in
parallel and between endpoints in random order.

Routes defined in the `message_retention_routes` Camel Context are only active on one node in the JBoss/Wildfly cluster at the time, this ensures
messages are routed between the endpoints in correct order.
These routes are used to support the Message Retention feature and are only loaded if `message_retention_mongodb_url` is set in the `environment.yml` file.
The default message retention route reads messages from the “${CCF\_PREFIX}message\_retention” queue and stores the message content in a MongoDb
database with database name “message\_retention” and collection name “message\_retention”. This route configuration can be
overridden in the CARMUSR. Note that the database name and collection name is hard coded in some applications and cannot therefore be changed.

Furthermore, parameter `feature_mrm` enables forwarding messages from the message retention route to Message Recipient Management (MRM).

**Example Route**

This example shows a definition of a Camel Route, using Camel XML language, which routes messages from
a specific queue on a specific message broker to an external file endpoint.

```
<route id="example-camel-route">
  <from uri="internalBroker:queue:{{env:CCF_PREFIX}}some-queue-name"/>
  <to pattern="InOnly" uri="file://outputdir?fileName=roster_report_${date:now:yyyyMMdd}.xml"/>
</route>
```

Inside the Camel Route, the URI defines what type of endpoint that should be used, in this case the external endpoint is a directory where the message is stored as a file.

![../_images/integrator_clusterroutes.png](../_images/integrator_clusterroutes.png)

Integrator supports several endpoint types, see [Appendix A: Supported Camel components](#appendix-a-supported-camel-components) for full list of supported endpoints.

####### 3.1.1. Using JMS endpoints in Camel Routes

JMS (Java Messaging System) provides support for defining endpoints in Camel Routes for queues on different message brokers.
JMS components must be configured with a unique id in `$CARMUSR/integrator/routes/jms.xml`.

The JCMS internal ActiveMQ broker is pre-configured with the following component ids:

* internalBroker (no transactional support)
* internalXABroker (transactional support)

The following URI syntax should be used in a Camel Route definition when using a JMS endpoint:

> `uri=<JMS-component-id>:queue:<name of queue>`

Below is an example Camel Route using JMS for routing messages from one a queue on one broker to another.

```
<route id="jsmbroker-example-camel-route">
  <from uri="external-wsmq-broker:queue:some-queue-name"/>
  <to pattern="InOnly" uri="internalBroker:queue:{{env:CCF_PREFIX}}some-other-queue-name"/>
</route>
```

If there is a need to have a transacted route, we need to use ‘internalXABroker’ and declare the route as ‘transacted’

The internal broker is configured as both a transactional and a non-transactional broker.
Any inbound route using the transactional broker `internalXABroker` and marking them with the transacted tag, will enlist the route in the transaction context coming from the broker.
All outbound routes that are called by the transacted route will also be included in the transaction.

In the following example the route “foo” will be included in transaction, and if it fails to deliver to “externalBroker” the message will be rolled back to the queue on “internalXABroker”.

```
<route id="export_apis_fcm">
  <from uri="internalXABroker:queue:{{env:CCF_PREFIX}}from.ioservice.apis_fcm_trigger" />
  <transacted />
  <to uri="direct:outbound_foo" />
</route>

<route id="foo">
  <from uri="direct::outbound_foo" />
  <to uri="externalBroker:queue:foofoo" />
</route>
```

A transacted Camel route uses the [TransactionErrorHandler](http://camel.apache.org/transactionerrorhandler.html) as error handler.
If an exception is raised in a route it will propagate to the error handler and unless it is caught there it will rollback the transaction. When the transaction is rolled back to the broker it will try to redeliver the message.
Redelivery configuration is done in the resource adapter or in the broker.

See [Configuring message brokers](#configuring-message-brokers) for more information on how to configure the logical names of message brokers in JBoss/Wildfly.

reference:
:   * [Transactional client](http://camel.apache.org/transactional-client.html) EI pattern.
    * [JMS component](http://camel.apache.org/jms.html)
    * [TransactionErrorHandler](http://camel.apache.org/transactionerrorhandler.html)

####### 3.1.2. Supporting beans and processors

**FileProcessor**

The file processor bean reads file and sets the message body to the contents of the file.
The file name and path are taken from the exchange properties filename and filepath, respectively.

Usage example:

```
<setProperty name="filename"><simple>${header[filename]}</simple></setProperty>
<setProperty name="filepath"><simple>{{env:INTEGRATOR_IMPORT_DIR}}/jobrunner/</simple></setProperty>
<process ref="FileProcessor"/>
```

**ExchangeStateBean**

In some cases there is a need to temporary change the body and headers of the message inside a Camel route and later
restore the message by resetting the message back to the original body and headers. An example of such a use case is when a
Camel route starts by reading a message that is should exported at the end of the route, but inside the route
you must call some other service that decides whether the message actually should be exported or not.
The other service must be called from within the Camel rotue and it expects some other message body or headers.
Consider the Camel route below where the incoming message should be exported to file, but an other service is invoked in between
for deciding if the file should be exported or not.

```
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
  http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
  http://camel.apache.org/schema/spring file:///opt/jeppesen/jcms/data/config/integrator/schema/spring/camel-spring-3.4.5.xsd">

  <bean id="ExchangeState" class="com.jeppesen.jcms.integrator.bean.ExchangeStateBean" />
  <camelContext id="clusterroutes" xmlns="http://camel.apache.org/schema/spring" useMDCLogging="true" useBreadcrumb="true">
    <route id="example-restore-message">
      <from uri="direct:example-restore-message"/>

      <setBody><simple>shouldItBeExported</simple></setBody>
      <to pattern="InOut" uri="http:/someservice" />

      <when>
        <simple>${body} == 'yes'</simple>
        <to pattern="InOnly" uri="file://outputdir?fileName=myfile.txt"/>
      </when>

      <when>
        <simple>${body} == 'no'</simple>
        <log message="This message should not be exported." />
      </when>

    </route>
  </camelContext>
</beans>
```

The body that should be exported is lost when the message body is changed for calling the other service.
The integrator contains a bean that can be used for saving and restoring the state of the message.

```
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
  http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
  http://camel.apache.org/schema/spring file:///opt/jeppesen/jcms/data/config/integrator/schema/spring/camel-spring-3.4.5.xsd">

  <bean id="ExchangeState" class="com.jeppesen.jcms.integrator.bean.ExchangeStateBean" />
  <camelContext id="clusterroutes" xmlns="http://camel.apache.org/schema/spring" useMDCLogging="true" useBreadcrumb="true">
    <route id="example-restore-message">
      <from uri="direct:example-restore-message"/>

       <to uri="bean:ExchangeState?method=save" />

       <setBody><simple>shouldItBeExported</simple></setBody>
       <to pattern="InOut" uri="http:/someservice" />

       <when>
         <simple>${body} == 'yes'</simple>
         <to uri="bean:ExchangeState?method=restore" />
         <to pattern="InOnly" uri="file://outputdir?fileName=myfile.txt"/>
       </when>

       <when>
         <simple>${body} == 'no'</simple>
         <log message="This message should not be exported." />
       </when>

     </route>
  </camelContext>
</beans>
```

In the example Camel route above, the *ExchangeState* bean is used for saving the state of the message
before changing the body and calling the external service. The message is restored to the original state when
the response from the external service has been analyzed and the correct data is exported.

**AttachmentAttacherBean**

The AttachmentAttacher bean is used to attach a file to a message for e-mail sending.
The file can be plain text, PDF or any other Mime Typer, which is defined in the constructor of the Bean.
The header *CamelFileAbsolutePath* is used to define the file that should be attached.
Since not all Camel components supports attachments, the attachment should be done just before sending the e-mail.

```
<beans xmlns="http://www.springframework.org/schema/beans"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://camel.apache.org/schema/spring file:///opt/jeppesen/jcms/data/config/integrator/schema/spring/camel-spring-3.4.5.xsd
              http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

      <bean id="attacher" class="com.jeppesen.jcms.integrator.bean.AttachmentAttacherBean" >
        <constructor-arg value="text/plain"/>
    </bean>
      <camelContext autoStartup="true" id="camelContext" trace="true"
              xmlns="http://camel.apache.org/schema/spring">

              <route id="test_1">
                      <from uri="direct:attach_file_example" />
          <bean ref="attacher"/>
                      <to uri="smtp://${sysenv.SMTP_HOST}:${sysenv.SMTP_PORT}" />
              </route>
      </camelContext>
</beans>
```

**MultipartFileAttacherBean**

The MultipartFileAttacher bean is used when uploading files to HTTP servers that expects a multipart form containing a single file.
The header *CamelFileAbsolutePath* is used to define the file that should be uploaded to the HTTP server.

```
<beans xmlns="http://www.springframework.org/schema/beans"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://camel.apache.org/schema/spring file:///opt/jeppesen/jcms/data/config/integrator/schema/spring/camel-spring-3.4.5.xsd
              http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

 <bean id="multi_part_attacher" class="com.jeppesen.jcms.integrator.bean.MultipartFileAttacherBean" />
 <camelContext autoStartup="true" id="clusterroutes" xmlns="http://camel.apache.org/schema/spring">

    <route id="test_http_upload">
       <from uri="direct:test_http_upload" />
       <!-- store the message body to a file -->
       <to uri="file:///tmp?fileName="temp.xml" />
       <!-- specify file to upload -->
       <setHeader name="CamelFileAbsolutePath">
         <constant>/tmp/temp.xml</constant>
       </setHeader>
       <!-- convert body into a multipart form containing the specified file -->
       <bean ref="multi_part_attacher"/>
       <!-- upload to HTTP server -->
       <to uri="http://some.host.com:8080/some/url"/>
    </route>
 </camelContext>
</beans>
```

**FileListerBean**

The FileLister bean is used for listing files in a specified directory in json format.
The body should be set to the path that should be listed.

```
<beans xmlns="http://www.springframework.org/schema/beans"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://camel.apache.org/schema/spring file:///opt/jeppesen/jcms/data/config/integrator/schema/spring/camel-spring-3.4.5.xsd
              http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

 <bean id="FileLister" class="com.jeppesen.jcms.integrator.bean.FileListerBean" />
 <camelContext autoStartup="true" id="clusterroutes" xmlns="http://camel.apache.org/schema/spring">

  <route id="list_job_files" streamCache="true">
    <from uri="internalBroker:queue:{{env:CCF_PREFIX}}to.camelroute.list_job_files" />
    <setBody><simple>{{env:INTEGRATOR_IMPORT_DIR}}/jobrunner</simple></setBody>
    <to uri="bean:FileLister" />
  </route>

 </camelContext>
</beans>
```

####### 3.1.3. Monitoring

The Integrator has support for logging events and metrics that can be monitored in the Domus (Kibana) Dashboards.
The Camel Routes must use the Bean `com.jeppesen.jcms.integrator.bean.LogMetricsBean` for logging the events.
It’s also important that the Camel Context is configured to use the options `useMDCLogging=true` and `useBreadcrumb=true`.

Custom metrics can be specified by setting Exchange properties starting with the prefix `metric.`.

Metrics for exceptions are logged if the Exchange has caught an exception or if the Exchange property `metric.exception` contains an Exception instance.

Below is an example for logging an event that indicates that this specific Camel Route is handing a message.The event also contains custom
metrics.

```
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
          http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
          http://camel.apache.org/schema/spring file:///opt/jeppesen/jcms/data/config/integrator/schema/spring/camel-spring-3.4.5.xsd">

  <!-- Supporting Bean for logging metrics to Domus (Kibana) Dashboards -->
  <bean id="LogMetrics" class="com.jeppesen.jcms.integrator.bean.LogMetricsBean"/>

  <camelContext id="clusterroutes" xmlns="http://camel.apache.org/schema/spring" useMDCLogging="true" useBreadcrumb="true">
    <route id="myRoute">
      <from uri="direct:myRoute" />
      <setProperty name="metric.firstChar">
        <simple>${body.substring(0,1)}</simple>
      </setProperty>
      <to uri="bean:LogMetrics" />
      <choice>
        <when>
          <simple>${body.substring(0,1)} in 'A,B,C,D'</simple>
          <!-- OK -->
        </when>
        <otherwise>
           <setProperty name="metric.errorReason">
             <simple>None supported character: ${body.substring(0,1)}</simple>
           </setProperty>
           <to uri="bean:LogMetrics?method=error" />
        </otherwise>
      </choice>
    </route>

  </camelContext>
</beans>
```

These metrics becomes available as fields in the Elastic seach database and can be displayed in Kibana dashboards.

![../_images/log-metric-kibana.png](../_images/log-metric-kibana.png)

The Bean automatically logs metrics for some JCMS internal message headers.
The loglevel can be controlled by invoking different methods of the Bean,
supported methods are *info*, *warning* and *error*. The event is logged on info level if no method is specified.

####### 3.1.4. Message logging

The Integrator contains a Camel component that can be used for logging messages that are being routed.
Each message is logged with a timestamp, headers and the actual body of the message.
The logged message body is encoded with UTF-8 charset by default, but you can set the exchange property `Exchange.CHARSET_NAME` to use a specific charset.
Files logged during an exchange (that may span multiple routes) can be deleted with the undo verb, for use in onException or other error handling.
Files logged in the exchange is kept in a comma separated list in property IntegratorMsgLoggedFiles.

The default file and directory permissions can be override with configuration, either by parameter settings in the environment.yaml file,
which will effect all routes logging or as an option in a specific msglog statement in a given route. If both configurations apply for a given
msglog statement, the local route option will override the environment parameter.
See URI options and the supported environment parameters under Configuration.

**Note!** Logged messages are not automatically removed, it’s important to set up a some job that removes old messages for not running out of disk space.

**URI formats**

`msglog:<logname>:<storage-uri>?options`
`msglog:undo`

* `<logname>` is the name that is used for grouping logged messages.
* `<storage-uri>` specifies where the logged message should be stored.

It’s possible to control whether messages should be logged for a specific `<logname>` by
setting the Camel Context globalOption `<logname>.msg.log` to either *true* or *false*.
Messages are only logged for `<logname>` if the Camel Context globalOption `<logname>.msg.log` is *true*.
The Camel Context globalOptions can be changed during runtime, without restarting the Integrator,
by using the [Admin tool](#admin-tool).

**Supported storage-uri**

| Name | Example uri | Description |
| --- | --- | --- |
| file: | `msglog:foo:file:/tmp/log_here` | Stores the logged message as a file in specified directory on the local file system. |
| undo | `msglog:undo` | Deletes all files previously written by msglog in the exchange. |

**URI options**

| Name | Default | Description |
| --- | --- | --- |
| suffix | null | Used for differentiating messages that has been logged with same `<logname>`. |
| logAlways | false | When set to true, logs messages regardless the value of Camel context globalOption `<logname>.msg.log`. |
| dirPerms | `"rwxrwxr-x"` | Used for permission of directories created by msglog. |
| filePerms | `"rw-rw-r--"` | Used for permission of files created by msglog. |

Note

For created directories the umask set for the integrator process will have an impact on actual permission. (as stated in Java public interface PosixFileAttributeView)

Below is an example Camel route that logs each message to a file in a directory by
dynamically looking at an environment variable and the name of the Camel route.
On a ConnectException the file written by msglog will be deleted.

```
<camelContext id="clusterroutes" xmlns="http://camel.apache.org/schema/spring" useMDCLogging="true" useBreadcrumb="true">
  <globalOptions>
    <globalOption key="myRoute.msg.log" value="true" />
  </globalOptions>
  <onException>
    <exception>java.net.ConnectException</exception>
    <to uri="msglog:undo"/>
  </onException>
  <route id="myRoute">
    <from uri="direct:myRoute" />
    <toD uri="msglog:${routeId}:file:{{env:INTEGRATOR_LOG_MSG_DIR}}?filePerms=rw-rw----"/>
  </route>
</camelContext>
```

####### 3.1.5. Jobrunner

The Integrator contains a Camel component that can be used for creating jobs and also updating status and reporting
progress of jobs that have been initiated by the Jobrunner and are executed in Camel routes.

**URI format**

`jobrunner:<operation>?options`
or
`jobrunner:scheduleJob:<jobId>?options`

**Supported operations**

| Operation | Example uri | Description |
| --- | --- | --- |
| `reportProgress` | `jobrunner:reportProgress?options` | Set status and remark for current job being executed by the Camel route. |
| `reportFailure` | `jobrunner:reportFailure?options` | Indicate that job failed. This operation should typically used inside `<onException>` of the Camel route executing the job. |
| `scheduleJob` | `jobrunner:scheduleJob:jobid?params` | Create and send `CreateJobInstanceRequest` for given jobid and parameters eg) `jobrunner:scheduleJob:export_catalogdata?additional_table=aircraft_type` |

**URI options**

| Name | Default | Description |
| --- | --- | --- |
| `status` | `running` | Only used for operation `reportProgress`. Sets the status of the job. Valid values are `running`, `completed`, `failed`. |
| `remark` | For operation `reportFailure`: Exception caught by Camel, otherwise `null`. | Provides remark for the job, indicating it’s current progress. |
| `queue` | `env:CCF_PREFIXto.ioservice.JobrunnerService_1_0_soap` | Queue for communicating with Jobrunner SOAP service. |

Note

Above options are not applicable for the `scheduleJob` operation, in `scheduleJob` any option is sent in `CreateJobInstanceRequest`.

This component requires Exchange property `job.id` to contain the unique number identifying the job being executed.
The component automatically populates Exchange property `job.id` if not set, by trying to fetch it from message header `jcms_job_id`.

It’s also possible to provide status and remark in the reportProgress and reportFailure operations by setting
Exchange properties `job.status` and `job.remark` when not using the uri options.

Below is an example Camel route executes a shell script and uses the jobrunner component for updating the progress while
executing the job.

```
<route>
  <from uri="internalBroker:queue:{{env:CCF_PREFIX}}to.job.run_my_script" />
  <onException>
    <exception>java.lang.Exception</exception>
    <handled>
      <constant>true</constant>
    </handled>
    <to uri="jobrunner:reportFailure" />
  </onException>

  <setProperty name="job.remark"><simple>Running my_script.sh</simple></setProperty>
  <to uri="jobrunner:reportProgress" />

  <toD uri="exec:{{env:CARMUSR}}/bin/my_script.sh" />
  <when>
    <simple>${header[CamelExecExitValue]} != 0</simple>
    <throwException exceptionType="java.lang.Exception" message="Failed to run 'my_script.sh'." />
  </when>
  <to uri="jobrunner:reportProgress?status=completed&amp;remark=my_script.sh%20successfully%20executed." />
</route>
```

###### 3.2. Exposing SOAP web services

The Integrator exposes SOAP web services for the Camel Routes defined in the Camel Context called `wsroutes`.
This feature is used for defining SOAP services in JCMS that external systems can call, it cannot be used for calling external SOAP services from JCMS.

Exposed SOAP web services for a running Integrator are listed at the following URL:

> <http://integrator-host:20100/integrator-wsrouter/services>

The route definitions, with details on how each SOAP web service is defined, are located in `$CARMUSR/integrator/routes/wsroutes.xml`.

**Example route**

```
<route id="MySOAPWebService">
     <from uri="cxf:/MySOAPWebService?wsdlURL=file://{{env:CARMUSR}}/integrator/wsdl/mywebservice.wsdl&amp;dataFormat=MESSAGE"/>
     <to uri="internalBroker:queue:{{env:CFF_PREFIX}}to.ioservice.myioservice?requestTimeout=10000&amp;deliveryPersistent=false"/>
     <bean beanType="com.jeppesen.jcms.filehubutils.ReadProcessor" method="process"/>
     <bean beanType="com.jeppesen.jcms.filehubutils.BytesToStringProcessor" method="process"/>
     <removeHeaders pattern="JMS*"/>
     <removeHeaders pattern="qpid*"/>
     <bean beanType="com.jeppesen.jcms.filehubutils.DeleteProcessor" method="process"/>
 </route>
```

The example Camel Route above becomes exposed at <http://integrator-host:20100/integrator-wsrouter/services/MySOAPWebService>.

The service maps the WSDL `mywebservice.wsdl` to the JCMS backend service (typically an IOService) available on ActiveMQ queue with name `to.ioservice.myioservice`.
When the web service is called by an external system, the SOAP request is forwarded to ActiveMQ queue `to.ioservice.myioservice` where some backend service consumes the request and provide a response message back to the Camel Route, some headers
are then removed from the response message before it’s finally send back to the external system.
The requestTimeout option specifies the timeout for a reply after the request has been forwarded to the backend service (in milliseconds).

See [Camel CXF](http://camel.apache.org/cxf.html) for more configuration options.

![../_images/integrator_wsroutes.png](../_images/integrator_wsroutes.png)

###### 3.3. REST Gateway web service

The Integrator provides a REST web service that can be used for sending messages to Camel Routes defined in Camel Context called `camelrestroutes`.
This feature can be used by external systems for posting messages to subscription services in JCMS, i.e. services that doesn’t provide any response to the external system (fire and forget).

The service is available on the following URL:

> <http://integrator-host:20100/integrator-camelrest/services>

The service defines the following operations:

GET Operations

> * WADL descriptor of the service.
>   <http://integrator-host:20100/integrator-camelrest/services/rest?_wadl>
> * Returns a list of all avaliable service.
>   <http://integrator-host:20100/integrator-camelrest/services/rest/list>

PUT operations

> * Puts a message to a service
>   <http://integrator-host:20100/integrator-wsrouter/services/rest>?service=<service-name>

The route definitions, with details on how each subscription service is defined, are located in: `$CARMUSR/integrator/routes/camelrestroutes.xml`.

**Example route**

```
<route id="myservice" streamCache="true">
      <from uri="direct:route_myservice"/>
      <log message="breadcrumbId: ${header[breadcrumbId]}"/>
      <doTry>
          <bean method="process" ref="WriteProcessor"/>
          <to pattern="InOnly" uri="internalBroker:queue:{{env:CCF_PREFIX}}to.ioservice.myservice"/>
          <bean ref="SuccessProcessor"/>
          <doCatch>
              <exception>java.lang.Exception</exception>
              <bean ref="FailureProcessor"/>
          </doCatch>
      </doTry>
  </route>
```

Note that the end point URI `uri="direct:route_myservice"` must match the route id with the `route_` prefix.

![../_images/integrator_camelrestroutes.png](../_images/integrator_camelrestroutes.png)

The example Camel Route above becomes exposed at <http://integrator-host:20100/integrator-wsrouter/services/rest?service=myservice>.

The Camel route maps the service name `myservice` to the JCMS backend service (typically an IOService) available on ActiveMQ queue with name `to.ioservice.myioservice`.
When the web service is called by an external system, the request body is farwared to ActiveMQ queue `to.ioservice.myioservice`.
HTTP response code 200 is returned when the request is successfully received by the Integrator, otherwise HTTP response code 500 is returned and the external system must hold the message and retry to send the
request again.

###### 3.4. Web services security

Integrator doesn’t come with any security configuration by default since security typically is something that is system installation specific and varies for different implementation projects.
It’s possible to configure [security domains](https://docs.jboss.org/author/display/WFLY/Security+subsystem+configuration) in JBoss/Wildfly in the configuration layer, see [Custom configuration of integrator](#custom-configuration-of-integrator) for more information.
Camel also provides several ways for setting up [security](http://camel.apache.org/security.html) for routes and end points which can be used in the route definition xml files.

###### 3.5. JMS REST API

The integrator provides a REST API for performing operations on messages queues for configured message brokers.

PUT operations

* Puts a message on a queue
  :   <http://integrator-host:20100/integrator-jmsbroker/camel/jmsbroker?broker=broker-logical-name&queue=queue-name>

GET operations

* Fetch and remove first message from a queue
  :   <http://integrator-host:20100/integrator-jmsbroker/jmsbroker?broker=broker-logical-name&queue=queue-name>
* Count messages on a queue
  :   <http://integrator-host:20100/integrator-jmsbroker/jmsbroker?broker=broker-logical-name&queue=queue-name&count>
* Show all messages on a queue, without removing any messages
  :   <http://integrator-host:20100/integrator-jmsbroker/jmsbroker?broker=broker-logical-name&queue=queue-name&browse>
* Remove all messages on a queue
  :   <http://integrator-host:20100/integrator-jmsbroker/jmsbroker?broker=broker-logical-name&queue=queue-name&drain>
* Show the body of all messages on a queue, without removing any messages
  :   <http://integrator-host:20100/integrator-jmsbroker/jmsbroker?broker=broker-logical-name&queue=queue-name&browse_body_as_text>

See [Configuring message brokers](#configuring-message-brokers) for more information on how to configure the logical names of message brokers.

###### 3.6. Large Message Handling

Sending large payloads over a messaging system like ActiveMQ has some definite downsides, like large memory consumption and temporary performance degradations.
Integrator comes with [Camel Processors](http://camel.apache.org/processor.html) that can be used in Camel Routes for sending large messages out-of-band by calling the JCMS *Filehub* service. The purpose
of the Processors is to make it easy to upload, download and delete content from the JCMS *Filehub* service.

The following Processors are provided by the Integrator:

**WriteProcessor**
:   Checks if the message body is considered as large by comparing the size of the body with environment variable `JCMS_FILE_HUB_THRESHOLD`.
    If the message is large, it’s uploads the message body to *Filehub* and sets message header *DeferredContentURL* to URL where content can later be downloaded.
    Finally it and clears the message body.

**ReadProcessor**
:   If message header *DeferredContentURL* is set, download URL the and set the message body to the downloaded Byte Array (in memory).

**ReadToStreamProcessor**
:   If message header *DeferredContentURL* is set, initialize a ByteInputStream from the URL and set the message body to that steam.

**DeleteProcessor**
:   If message header *DeferredContentURL* is set, delete the content from URL from the *Filehub*.
    DeleteProcessor removes *DeferredContentURL* header.

**BytesToStringProcessor**
:   If the message body is a Byte Array (steam), read the stream (download) and set message body to a string with the downloaded content.

####### 3.6.1. Usage in Camel routes

The Camel Processors are used in Camel Routes by including a the “bean” element.

```
<route id="process_large_data">
    <from uri="uri="file://tmp?fileName=largefile"/>
    <bean beanType="com.jeppesen.jcms.filehubutils.WriteProcessor" method="process"/>
    <to pattern="InOnly" uri="internalBroker:queue:{{env:CCF_PREFIX}}test.out_of_band"/>
</route>
```

The route above reads a file, and upload to to *Filehub* if the size is considered large. The message body is empty, but the message will have the
header *DeferredContentUrl* set to a URL similar to:
“<http://infra-host:8008/uploaded-files/20160517T014944519_3caa116b-7d07-41b9-a358-7eb0589a88ef>”.
The URL in this header is later used by the recipient of the message to download and delete the content from *Filehub*.

When a Camel route receives a message with the *“DeferredContentUrl”* header in it, and needs to download content from the URL, the ReadProcessor is
used.

```
<route id="route_example">
    <from uri=internalBroker:queue:{{env:CCF_PREFIX}}test.out_of_band"/>
    <bean beanType="com.jeppesen.jcms.filehubutils.ReadProcessor" method="process"/>
    <to pattern="InOnly" uri="file://tmp?fileName=largefile"/>
    <bean beanType="com.jeppesen.jcms.filehubutils.DeleteProcessor" method="process"/>
</route>
```

Note that *two* processors are used, one ReadProcessor to download the data, and one DeleteProcessor to delete the data from FileHub
after it is written to file. Calls to DeleteProcessor shall only be done at the end of a route when all work has been done since the
delete cannot be rolled back if the route crashes. DeleteProcessor does nothing if the file to delete doesn’t exist.

###### 3.7. MQ-router

The Integrator provides support for routing messages from/to queues between the Atrium internal ActiveMQ broker and
other external message brokers (ActiveMQ, WSMQ, etc.). This feature is called `MQ-router` and should be used when
integrating Atrium with external message brokers.

The `MQ-router` uses transactions for guaranteeing that all messages are routed in correct order and no messages are
skipped or lost. Multiple messages are routed in same transaction as part of a batch for providing high thoughput even if the
network latency between message brokers is poor. The `MQ-router` is active on one node and the other nodes are passive.

####### 3.7.1. Configuration

The `MQ-router` is configured in file `CARMUSR/integrator/mqrouter.yml`.
The configuration defines a set of message brokers and specifies how messages
should be routed between queues of the message brokers. Environment variables can be used in the configuration file
by using the `${env:NAME}` notation.

See [Custom Integrator environment variables](#custom-integrator-environment-variables) for more information on how to define environment variables.

The configuration file contains four blocks:

`version`

> Specifies the version of MQ Router to use, current version is 0.2.

Example of `version`:

```
version: "0.2"
```

`settings`

> Configures settings for the MQ router.

Example of `settings`:

```
settings:
  msgLogDir: ${env:INTEGRATOR_LOG_MSG_DIR} # File system path where routed messages should be logged.
  connectionRetryDelay: 20                 # Number of seconds to wait before retrying to connect to a message broker if connection was lost. Defaults to 30.
```

`messageBrokers`

> Defines the set of message brokers to integrate.

Example of `messageBrokers`:

```
messageBrokers:
  - name: ATRIUM_BROKER        # Name of the message broker.
    className: ActiveMQ        # Name of Java class to use when connecting, supported values are: 'ActiveMQ'.
    url: ${env:INT_BROKER_URL} # Connection URL.
    fileHub: true              # Wheater this message broker uses Filehub for out of band communication of large messages.

  - name: EXT_BROKER
    className: ActiveMQ
    url: tcp://${EXT_BROKER_HOST}:${EXT_BROKER_PORT}
    userName: ${EXT_BROKER_USERNAME}  # Username
    password: ${EXT_BROKER_PASSWORD}  # Password
```

`routes`

> Specifies how messages should be routed between queues of the defined message brokers.

Example of `routes`:

```
routes:
 - name: inbound_example_route            # Name of the route.
   from: EXT_BROKER:atrium.example.to     # Source broker/queue to consume messages from.
   to: ATRIUM_BROKER:to.ioservice.example # Target broker/queue to produce messages to.
   batchTimeout : 2000                    # Maximum time (in milliseconds) to spend when fetching messages from the message source queue before routing fetched messages to target queue. Defaults to 1000.
   batchSize: 20                          # Max number of messages to fetch from source queue before routing fetched messages to target queue. Defaults to 10.
   msgLog: true                           # Wheather routed messages should be logged to file system directory ``msgLogDir`` or not.
   setHeaders:                            # Specifies message headers to set to routed messages.
     foo: 123
     prio: ${JMSPriority}                 # Set property header prio to JMSPriority.
     jms_id: ${id}                        # Set property header jms_id to JMSId.
     now_time: ${now:yyyyMMdd'T'HHmmss}   # Set property header now_time to current date in format given.
     jmsnprio: ${JMSPriority}_${id}       # Set property header jmsnprio to JMSPriority and '_' and JMSId.

 - name: outbound_example_route
   from: ATRIUM_BROKER:from.ioservice.example
   to: EXT_BROKER:atrium.example.from
   removeHeaders:                         # Specifies patterns for message headers to remove from routed messages.
     - JMS_AMQP*
     - jcms_response_code

 - name: internal_example_route
   from: ATRIUM_BROKER:from.ioservice.example
   to: ATRIUM_BROKER:to.camelroute.example
```

####### 3.7.2. Monitoring

`MQ-router` updates status and statistics of the routes in JMX under `com.jeppesen.jcms.integrator.mqrouter`.
`MQ-router` reports status in consul under service `Integrator`.
Metrics are sent when a batch has been processed, with additional key:values `app:integrator` and `function:mqrouter`.

##### Camel routes

###### Using JMS endpoints in Camel Routes

###### Supporting beans and processors

###### Monitoring

###### Message logging

###### Jobrunner

##### Exposing SOAP web services

##### REST Gateway web service

##### Web services security

##### JMS REST API

##### Large Message Handling

###### Usage in Camel routes

##### MQ-router

###### Configuration

###### Monitoring

#### Admin tool


Integrator provides [Hawtio](http://hawt.io/getstarted/index.html) as an administration tool for managing, diagnose and monitor JBoss/Wildfly, Camel Routes, endpoints,
message queues and more.

The tool is available on the following URL:

> <http://integrator-host:20100/hawtio>

###### 4.1. Authentication

It’s possible to control whether authentication is required during login to Hawtio, by default authentication is disabled.

It is recommended to specify the variables in the `environment.yml` and run configure for the atriumctl integrator. The following
varibles is need to be specified:

> * **integrator\_hawtio\_user: “admin”**
> * **integrator\_hawtio\_password: “admin”**

###### 4.2. Troubleshooting

There is a setting in Hawtio that will limit the maximum number of elements that Hawtio can handle. This will affect the camel routes and there
is a chance that not all routes will show up in Hawtio. If this occur the limit value can be increased in the Hawtio Preferences.

To reach the Hawtio Preferences click the ‘User’ item in the top right of you browser window.

![../_images/hawtio-menu.png](../_images/hawtio-menu.png)

To reach the Max Collection Size value, click the ‘Jolokia’ tab and change the value in the ‘Max Collection Size’ input field (5000 should be enough)
and hit the ‘Apply’ button.

![../_images/hawtio-jolokia-preferences.png](../_images/hawtio-jolokia-preferences.png)

##### Authentication

##### Troubleshooting

#### Configuration


The Integrator is configured with `atriumorc` as part of the installation process, please run following command for
listing parameters related to the Integrator which can be specified in the system `environment.yml` file.

```
$ atriumorc -c help
```

Following table list parameters used by the integrator that are configurable in environment.yml

| Parameter | Default value | Description |
| --- | --- | --- |
| integrator\_hawtio\_user | hawtio-admin | User name for Hawtio admin web console if authentication is enabled. |
| integrator\_hawtio\_password | <generated> | Password for the Hawtio user |
| integrator\_int\_broker\_max\_connections | 100 | Max connections to internal message broker. |
| integrator\_int\_broker\_max\_redeliveries | 6 | Max redelivery attempts for transacted messages from internal message broker |
| integrator\_int\_broker\_username |  |  |
| integrator\_int\_broker\_password |  |  |
| integrator\_java\_opts | -Xmx2500m -Xms2500m -Duser.timezone=UTC | Heap memory and timezone settings, and other JVM settings for integrator wildfly instance |
| integrator\_jgroupsdefaultstack | tcpping | Defines protocol for cluster setup. Possible values [“tcpping”, “udp”]. If any other Atrium system is on the same network use tcpping, or make sure you have a unique multicast\_address for this system. |
| integrator\_tcpping\_port | 20105 | The port that the integrator uses for jgroups tcpping. |
| integrator\_tcpping\_servers |  | List of tcpping servers for integrator. Defaults to all web nodes. |
| integrator\_log\_max\_backup\_index | 5 | Number of Wildfly server log files that Integrator should keep before rotating the logs. |
| integrator\_log\_rotate\_size | 100000k | Max file size of Wildfly server log file before rotating the logs. |
| integrator\_https\_keystore\_file\_path |  | Absolute file path to the java keystore file containing the server certificate. |
| integrator\_https\_keystore\_alias |  | Unique alias name for the server certificate in the keystore. Must be specified if integrator\_https\_keystore\_file\_path is set. |
| integrator\_https\_keystore\_password |  | Password needed to access the keystore, e.g. to list the aliases. Must be specified if integrator\_https\_keystore\_file\_path is set. |
| integrator\_https\_keystore\_key\_password |  | Password for a certificate represented by a certain alias. Must be specified if integrator\_https\_keystore\_file\_path is set. |
| integrator\_disable\_http | False | Disables non local plain http calls if set to True. |
| message\_retention\_mongodb\_url | mongodb://mongohost:27017?ssl=true | MongoDb URL including all parameters for SSL, authentication, etc. No need to specify a database in the URL as that is set by the Camel route. |
| feature\_mrm | False | Enables integrating the Atrium system with Message Recipient Management (MRM) by forwarding messages from the “message\_retention” Camel route. |
| integrator\_healthcheck\_disable\_count\_routes | False | Disable health check that all configured camel routes are started. |
| integrator\_msglog\_dir\_permission | None | Used for permission of directories created by msglog. |
| integrator\_msglog\_file\_permission | None | Used for permission of files created by msglog. |

###### 5.1. HTTPS

Integrator uses port 20102 for https. By default, the server generates a self signed certificate if no other configuration is provided.
The default configuration is not recommended for production installations. Instead it’s recommended to issue a signed and trusted wildcard certificate for the servers.
The certificate to use should be provided as a Java keystore file and the keystore file must manually be installed on the server filesystem by system administrator.

It’s recommended to use java [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html) to manage your certificates.

Following values must be updated in the `environment.yml` when the keystore file has been installed on the server filesystem:

| Parameter | Example value | Description |
| --- | --- | --- |
| integrator\_https\_keystore\_file\_path | /etc/jeppesen/files/integrator.keystore | Absolute file location of keystore file on the server. |
| integrator\_https\_keystore\_alias | integrator | Alias of the key in the keystore file to use. |
| integrator\_https\_keystore\_password | password1 | Password of the keystore file. |
| integrator\_https\_keystore\_key\_password | password2 | Password of the key in the keystore file. |
| integrator\_disable\_http | true | Disables inbound http connections for additional security. Defaults to false. |

###### 5.2. Integrator directory structure

The following subdirectories and files can be found inside the Integrator installation directory: `$CARMSYS/integrator-site/`

| Directory / file | Description |
| --- | --- |
| addons/ | Contains additional applications that can be deployed. |
| cli/ | Contains core CLI scripts to configure JBoss/Wildfly. |
| deploy/ | Contains the applications to deploy when starting JBoss/Wildfly. |
| routes/ | Contains default configuration for routes that can be overridden in the CARMUSR. |
| script/ | Scripts for configuring, starting and stopping the JBoss/Wildfly application server. |
| server/standalone/configuration/ | Configuration files for the standalone server that runs this installation. |
| server/standalone/log/ | JBoss/Wildfly log files. |
| server/modules/ | JBoss/Wildfly modules installed with the integrator, mostly camel and spring. |
| env.source | Specifies default values for environment variables required for running the Integrator, default values can be overridden by the site.source file. |
| internal\_env.source | Specifies environment variables, required for running the Integrator, that are static and should not change. |
| jboss\_home | Contains path to JBoss/Wildfly installation. |
| site.source | Specifies custom specific environment variables, based on system environment.yml. |

The following sub directories and files are expected to exist in the Integrator `CARMUSR` directory: `$CARMUSR/integrator/`

| Directory / file | Description |
| --- | --- |
| routes/camelrestroutes.xml | Defines the `camelrestroutes` Camel Context. |
| routes/clusterroutesroutes.xml | Defines the `clusterroutes` Camel Context. |
| routes/message\_retention\_routes.xml | Defines the `message_retention_routes` Camel Context (optional). |
| routes/noderoutes.xml | Defines the `noderoutes` Camel Context. |
| routes/wsroutes.xml | Defines the `wsroutes` Camel Context. |
| wildfly/custom\_cli\_scripts.lst | Lists custom CLI scripts that should run for configuring JBoss/Wildfly. |
| environment.json | Defines custom environment variables that must be set when running the Integrator. |

###### 5.3. Environment variables

Some environment variables must be set when running the Integrator. Variables are sourced from the following files, in the following order, when Integrator is starting:

1. `$CARMSYS/integrator-site/env.source`
2. `$CARMSYS/integrator-site/internal_env.source`
3. `$CARMSYS/integrator-site/site.source`

The last definition of a variable will override any earlier definition of the same. Values that are specific for different system installations are specified in the file `site.source`
which is generated by `atriumorc` during the system configuration phase.

Description of variables in `site.source`

| Environment variable | Description | Example value |
| --- | --- | --- |
| CCF\_PREFIX | Queue prefix used for JCMS ActiveMQ broker, read from common configuration. | carmen. |
| JCMS\_FILE\_HUB\_URL | Service URL to JcmsFileHub/File service for uploading large messages, read from common configuration. |  |
| INT\_ACTIVEMQ\_BROKER\_URL | Connection url to internal ActiveMQ broker, read from common configuration. | <tcp://infra-host:61616?jms.rmIdFromConnectionId=true> |
| HAWTIO\_AUTHENTICATION | value from integrator\_hawtio\_authentication in environment.yml | false |
| HAWTIO\_USER | value from integrator\_hawtio\_user in environment.yml | hawtio-admin |
| LOG\_MAX\_BACKUP\_INDEX | value from integrator\_max\_log\_backup\_index in environment.yml | 5 |
| LOG\_ROTATE\_SIZE | value from integrator\_log\_rotate\_size, hard coded. | 100000k |
| MESSAGE\_RETENTION\_MONGODB\_URL | Value from message\_retention\_mongodb\_url in environment.yml (if set). | mongodb://mongohost:27017?ssl=true |
| MSGLOG\_DIR\_PERMISSION | value for permission of directories created by msglog. | `"rwxrwx---"` |
| MSGLOG\_FILE\_PERMISSION | value for permission of files created by msglog. | `"rw-rw----"` |

Description of variables in `env.source`

| Environment variable | Description | Example value |
| --- | --- | --- |
| SITE\_CONSOLE\_LOG | Logging of Wildfly console. | /dev/null |
| LOG\_LEVEL | Global log level for integrator | INFO |
| JCMS\_FILE\_HUB\_THRESHOLD | Messages with a body larger that this value (in bytes) are considered as large by WriteProcessor and are uploaded to Filehub. | 1000000 |

Note

When LOG\_LEVEL is set to DEBUG or TRACE but not SITE\_CONSOLE\_LOG then the startup stdout is logged to /tmp/integrator-site\_stdout.log.

###### 5.4. Custom configuration of integrator

There are two ways for adding custom specific configuration of Integrator:

####### 5.4.1. Custom Integrator JBoss/Wildfly configuration

It’s possible to change the configuration of the JBoss/Wildfly applications server by creating custom [CLI scripts](https://docs.jboss.org/author/display/WFLY/CLI+Recipes) and add them to the `CARMUSR`.

CLI scripts listed in `$CARMUSR/integrator/wildfly/cli/custom_cli_scripts.lst` are executed by `atriumorc` during the system configuration phase.

Please note that this is the **only** way of reconfiguring the JBoss/Wildfly server, it’s not possible to manually edit any files in `$CARMSYS/integrator-site/`, since they
are reset to default during the system configuration phase.

####### 5.4.2. Custom Integrator environment variables

Custom specific environment variables that must be set when running the integrator can be declared in `$CARMUSR/integrator/environment.json`.

Variables defined in this file becomes available in the system environment.yml file and also as environment variables in `$CARMSYS/integrator-site/site.source`,
making them available to use in Camel Routes and JBoss/Wilfly configuration files.

The file should contain a json-list that declares the variables with following attributes:

| Attribute | description | required |
| --- | --- | --- |
| name | the variable name in lower case | yes |
| description | A description of the variable and it’s purpose | no |
| default | A default value | no |

Default values can reference an other environment variables by using the notation ${var} where var is a variable defined in `environment.yml`.

Example of file `$CARMUSR/integrator/environment.json`:

```
{"environment-variables":
  [{"name": "ext_wsmq_broker_host",
    "description": "Host name of IBM WebSphere MQ server that JCMS should connect to.",
  },
  {"name": "ext_wsmq_broker_port",
    "description": " IBM WebSphere MQ port",
    "default": "1414"
  },
  {
    "name": "integrator_export_dir",
    "description": "Directory where files exported to disk are stored by integrator.",
    "default": "${shared_filesystem}/integrator/export"
  }]
}
```

In the system `environment.yml` we can add the following two lines to define the system specific values for the variables:

```
ext_wsmq_broker_host: testmqbroker.jeppesen_air.com
ext_wsmq_server_port: 7474
```

The values specified in the `environment.yml` gets propagated to `$CARMSYS/integrator-site/site.source` during the system configuration phase when that file is generated.

For the example above, the following lines are added to `$CARMSYS/integrator-site/site.source`:

```
EXPORT EXT_WSMQ_BROKER_HOST="testmqbroker.jeppesen_air.com"
EXPORT EXT_WSMQ_BROKER_PORT="7474"
```

The variable `ext_wsmq_broker_host` is declared without any default value in `$CARMUSR/integrator/environment.json`,
the system configuration phase fails if no value is specified in the `environment.yml` file.

###### 5.5. Configuring message brokers

Message brokers (ActiveMQ, WSMQ or similar) should typically be configured only in the [MQ-Router](#mq-router) configuration.
Additional configuration of the Integrator is however needed in order access the message brokers from Camel routes.
Configuration is done on two levels, first a [Resource adapters](https://docs.jboss.org/author/display/WFLY/Resource+adapters) configuration as Wildfly CLI script and secondly a [Camel JMS component](http://camel.apache.org/jms.html) configuration in `$CARMUSR/integrator/routes/jms.xml`.

####### 5.5.1. Resource adapters configuration

Message brokers are added as [Resource adapters](https://docs.jboss.org/author/display/WFLY/Resource+adapters) in the Wildfly configuration with a logical name.
This enables Camel routes to connect with the broker.

Resource adapters are configured by adding CLI scripts in the `CARMUSR` as described in [Custom Integrator JBoss/Wildfly configuration](#custom-integrator-jboss-wildfly-configuration).

Below is an example CLI script that adds a resource adaptor for IBM Websphere MQ Broker with the logical name `ext-wsmq-broker`.

```
##### Mark the commands below to be run as a batch
batch

/subsystem=resource-adapters/resource-adapter=websphere-mq:add(archive=wmq.jmsra.rar, transaction-support=NoTransaction)
/subsystem=resource-adapters/resource-adapter=websphere-mq/connection-definitions=WSMQFactory:add(class-name="com.ibm.mq.connector.outbound.ManagedConnectionFactoryImpl",jndi-name="java:jboss/jmsbroker/ext-wsmq-broker",enabled="true")
/subsystem=resource-adapters/resource-adapter=websphere-mq/connection-definitions=WSMQFactory/config-properties=hostName:add(value="${env.EXT_WSMQ_BROKER_HOST}")
/subsystem=resource-adapters/resource-adapter=websphere-mq/connection-definitions=WSMQFactory/config-properties=port:add(value="${env.EXT_WSMQ_BROKER_PORT}")
/subsystem=resource-adapters/resource-adapter=websphere-mq/connection-definitions=WSMQFactory/config-properties=channel:add(value="${env.EXT_WSMQ_BROKER_CHANNEL}")
/subsystem=resource-adapters/resource-adapter=websphere-mq/connection-definitions=WSMQFactory/config-properties=queueManager:add(value="${env.EXT_WSMQ_BROKER_QMGR}")
/subsystem=resource-adapters/resource-adapter=websphere-mq/connection-definitions=WSMQFactory/config-properties=transportType:add(value=CLIENT)
/subsystem=resource-adapters/resource-adapter=websphere-mq/connection-definitions=WSMQFactory/config-properties=username:add(value="${env.EXT_WSMQ_BROKER_USERNAME}")
/subsystem=resource-adapters/resource-adapter=websphere-mq/connection-definitions=WSMQFactory/config-properties=password:add(value="${env.EXT_WSMQ_BROKER_PASSWORD}")
run-batch
```

In this example the following environment variables has to be set when the Integrator is running:

EXT\_WSMQ\_BROKER\_HOST

EXT\_WSMQ\_BROKER\_PORT

EXT\_WSMQ\_BROKER\_CHANNEL

EXT\_WSMQ\_BROKER\_QMGR

EXT\_WSMQ\_BROKER\_USERNAME

EXT\_WSMQ\_BROKER\_PASSWORD

Therefore they must be declared in `$CARMUSR/integrator/environment.json` and the values should be provided by system `environment.yml`.

The resource-adapter comes as an .rar file that need to be put in `$CARMUSR/integrator/wildfly/deploy/`

####### 5.5.2. Camel JMS component configuration

A JMS component must be defined in order to communicate with the broker from Camel routes.
All JMS components are defined and configured in `$CARMUSR/integrator/routes/jms.xml`.
Each JMS component is given a unique id and is configured to use a specific resource adapter.
The resource adapter to use is looked up with jndi by pointing to the connection factory declared in the resource adapter.

Example jndi-lookup

```
<jee:jndi-lookup id="WSMQConnectionFactory" jndi-name="java:jboss/jmsbroker/ext-wsmq-broker" />
```

Example JMS component with id “wsmqBroker”.

```
<bean id="wsmqBroker" class="org.apache.activemq.camel.component.ActiveMQComponent">
  <property name="connectionFactory" ref="WSMQConnectionFactory" />
  <property name="cacheLevelName" value="CACHE_CONSUMER" />
  <property name="acknowledgementModeName" value="SESSION_TRANSACTED" />
</bean>
```

####### 5.5.3. Transactional JMS component

A JMS component can be configured to use transactional messaging by additionally providing a transaction manager in the configuration.
The transaction manager is looked up using jndi name `java:jboss/TransactionManager`.

```
<bean id="jtaTransactionManager" class="org.springframework.transaction.jta.JtaTransactionManager">
  <property name="transactionManagerName" value="java:jboss/TransactionManager" />
</bean>
```

```
<bean id="internalXABroker" class="org.apache.activemq.camel.component.ActiveMQComponent">
  <property name="connectionFactory" ref="jndiJmsXAConnectionFactory" />
  <property name="transactionManager" ref="jtaTransactionManager" />
  <property name="cacheLevelName" value="CACHE_NONE" />
  <property name="acknowledgementModeName" value="SESSION_TRANSACTED" />
</bean>
```

Note! The “cacheLevelName” should be set to “CACHE\_NONE”.

##### HTTPS

##### Integrator directory structure

##### Environment variables

##### Custom configuration of integrator

###### Custom Integrator JBoss/Wildfly configuration

###### Custom Integrator environment variables

##### Configuring message brokers

###### Resource adapters configuration

###### Camel JMS component configuration

###### Transactional JMS component

#### Camel Migrations


###### 6.1. Camel 3 migration

The Integrator has been updated to use Camel version 3 instead of Camel version 2. The following files must be updated for being compatible with Camel version 3.

* `$CARMUSR/integrator/routes/camelrestroutes.xml`
* `$CARMUSR/integrator/routes/clusterroutesroutes.xml`
* `$CARMUSR/integrator/routes/common.xml`
* `$CARMUSR/integrator/routes/jms.xml`
* `$CARMUSR/integrator/routes/noderoutes.xml`
* `$CARMUSR/integrator/routes/wsroutes.xml`

The following changes has to be done on existing camel route context configurations:

| Component | Changes |  |
| --- | --- | --- |
| <properties> | Replaced by <globalOptions> and <globalOption> |  |
| quartz2 | Moved to quartz component |  |
| camel-spring.xsd | Updated to a specific version camel-spring-3.4.5.xsd |  |
| <setProperty> propertyName attribute | Changed from propertyName to name |  |
| <setHeader> headerName attribute | Changed form headerName to name |  |
| <method> bean attribute | <setHeader> | Changed from bean to beanType |
| Endpoints with consumer. prefix | Removed consumer. prefix |  |

See [Apache Camel 2.x to 3.0 Migration Guide](https://camel.apache.org/manual/latest/camel-3-migration-guide.html) for further details.

###### 6.2. Camel 3.4.5 migration

WildFly upgraded from 18 to 20, see [WildFly 20 Admin Guide](https://docs.wildfly.org/20/Admin_Guide.html)

Camel upgraded from 3.0.1 to 3.4.5, see relevant sections in [APACHE CAMEL 3.X UPGRADE GUIDE](https://camel.apache.org/manual/latest/camel-3x-upgrade-guide.html)

The following files must be updated for being compatible with Camel version 3.4.5:

* `$CARMUSR/integrator/routes/camelrestroutes.xml`
* `$CARMUSR/integrator/routes/clusterroutesroutes.xml`
* `$CARMUSR/integrator/routes/common.xml`
* `$CARMUSR/integrator/routes/jms.xml`
* `$CARMUSR/integrator/routes/noderoutes.xml`
* `$CARMUSR/integrator/routes/wsroutes.xml`

The following changes have to be done on existing camel route context configurations:

| Component | Changes |
| --- | --- |
| Camel schema location | updated from “camel-spring-3.0.1.xsd” to “camel-spring-3.4.5.xsd”. |
| Out-of-band property placeholders | ie) <multicast prop:stopOnException=”stop”> should be written as <multicast stopOnException=”{{stop}}”> |
| Inflight repository | Disabled by default, turn on with <camelContext inflightRepositoryBrowseEnabled=”true”> |
| Context scope error handling | For some cases like loadBalance() an intermediary route is needed, see [CAMEL 3.2 UPGRADE GUIDE](https://camel.apache.org/manual/latest/camel-3x-upgrade-guide-3_2.html#_error_handling) |

###### 6.3. Camel 3.17 migration

Camel upgraded from 3.4 to 3.17, see relevant sections 3.5 - 3.17 in [APACHE CAMEL 3.X UPGRADE GUIDE](https://camel.apache.org/manual/latest/camel-3x-upgrade-guide.html)

WildFly upgraded from version 20 to 24, see [WildFly 24 Admin Guide](https://docs.wildfly.org/24/Admin_Guide.html).

The following changes have to be done on existing camel route context configurations, in files in $CARMUSR/integrator/routes if not
stated otherwise:

| Component | Changes |
| --- | --- |
| Camel XSD schema namespace | Replace “camel-spring-3.4.5.xsd” with “camel-spring.xsd”. |
| Attribute headerName changed | Replace <removeHeader headerName=”…” /> with <removeHeader name=”…” />, (in Camel 3.11.) |
| wireTap changed | If using <wireTap> then it can no longer contain the <body> element. One way to solve this is by directing wiretap to a direct route and set body in that direct route. |
| Resource adapter pool prefill | If an external broker is configured in cli then the resource-adapter connection-definitions need to have `pool-prefill="true"`. In configuration, e.g. `$CARMUSR/integrator/wildfly/cli/exernalbroker.cli`, replace `pool-prefill="false"` with `pool-prefill="true"` for each occurrence. |

**Other updates**

Removed ExampleDS and h2 support. This shows as an ERROR in log when running configure step but should be ignored.

###### 6.4. Camel 3.19 migration in integrator 9.3

Camel upgraded from 3.17 to 3.19, see relevant sections for 3.18 and 3.19 in [APACHE CAMEL 3.X UPGRADE GUIDE](https://camel.apache.org/manual/latest/camel-3x-upgrade-guide.html)

The following changes have to be done on existing camel route context configurations and where the schema namespace below is referenced:

| Component | Changes |  |
| --- | --- | --- |
| Schema namespace change for CXF WS |  | Updated from “<http://camel.apache.org/schema/cxf>” to “<http://camel.apache.org/schema/cxf/jaxws>”. Also implied: “<http://camel.apache.org/schema/cxf/camel-cxf.xsd>” to “<http://camel.apache.org/schema/cxf/jaxws/camel-cxf.xsd>”. Sample file: `$CARMUSR/integrator/routes/wsroutes.xml` |
| Schema namespace change for CXF RS |  | Updated from “<http://camel.apache.org/schema/cxf>” to “<http://camel.apache.org/schema/cxf/jaxrs>”. Also implied: “<http://camel.apache.org/schema/cxf/camel-cxf.xsd>” to “<http://camel.apache.org/schema/cxf/jaxrs/camel-cxf.xsd>” |

**Other updates**

The default and/or preferred TLS version changed in Camel 3.19 in regards of TLSv1.3 for components such as kafka, ftp and api:
:   * The default TLS protocol is changed from TLSv1.2 to TLSv1.3 in Camel JSSE support in camel api and camel ftp.
    * Camel updated doc regarding default TLS protocol in Kafka Clients running on JDK11+, default is TLSv1.2,TLSv1.3 (prefer v1.3 but can fall back to v1.2).
    * For more changes, see [APACHE CAMEL 3.X UPGRADE GUIDE](https://camel.apache.org/manual/latest/camel-3x-upgrade-guide.html)

###### 6.5. Camel 3.20 migration in integrator 9.6.500

Camel upgraded from 3.19 to 3.20.4, see relevant sections in [APACHE CAMEL 3.X UPGRADE GUIDE](https://camel.apache.org/manual/latest/camel-3x-upgrade-guide.html)

| Component | Changes in camel default settings |
| --- | --- |
| kafka | * enableIdempotence: changed from false to true. * requestRequiredAcks: changed from 1 to all. * retries: changed from 0 to unset. |

###### 6.6. Camel deprecations

EIPs `inOnly` and `inOut` are deprecated in Camel 3 and removed in Camel 4.

E.g. inOnly, `<inOnly uri="activemq:queue:one-way"/>` can be replaced by EIP `to` and setting option pattern:

```
<to pattern="InOnly" uri="activemq:queue:one-way"/>
```

##### Camel 3 migration

##### Camel 3.4.5 migration

##### Camel 3.17 migration

##### Camel 3.19 migration in integrator 9.3

##### Camel 3.20 migration in integrator 9.6.500

##### Camel deprecations

#### Running the integrator


The Integrator is managed by `atriumorc`, installation, configuration, starting and stopping should be done using `atriumorc`.

For development, testing and specific administration tasks, it’s also possible to start/stop and configure integrator using *CMSShell*.
Run following command in *CMSShell* for more information.

```
>>> integrator help
```

###### 7.1. Troubleshooting

The server log is at `$CARMSYS/integrator-site/server/standalone/log/server.log`

The global log level can be changed by setting environment variable *LOG\_LEVEL* variable in `env.source`

##### Troubleshooting

#### Appendix A: Supported Camel components


The following Camel components are available to be used in Camel routes configured for the Integrator:
Please see Camel documentation for more information of each component.

> <https://camel.apache.org/components.html>

* ActiveMQ
* Attachments
* Base64
* Bean
* Browse
* Crypto (JCE)
* Direct
* Exec
* File
* FTP
* Jasypt
* JMS
* JSONPath
* Kafka
* Log
* Mail
* Quartz
* SEDA
* Timer
* XPath
* XSLT
* XSLT Saxon

#### Indices and tables

### Jobrunner Configuration Guide


The purpose of this document is to describe the how to configure the Jobrunner feature in CMS.

* [1. Introduction](jobrunner.html)
* [2. Job definitions](jobrunner.html#job-definitions)
* [3. Configuration](jobrunner.html#configuration)
* [4. Executing jobs](jobrunner.html#executing-jobs)

##### Indices and tables

* [Index](../genindex.html)
* [Search Page](../search.html)

#### Introduction

#### Job definitions


Jobs are statically defined in a Python script in the configuration layer. Each job is defined with a unique name,
a description and an optional set of parameters that influence the outcome when running the job. A job can also have
a schedule pattern that defines when the job is scheduled to run. A job without a schedule pattern can be scheduled
manually from the web UI. Each job is also associated with a specific ActiveMQ queue. The trigger starts a job by sending a message
to the job queue.

A job definition has the following properties:

| Name | Required | Description |
| --- | --- | --- |
| name | Yes | An internal identifier for the job. |
| desc | Yes | A description that is typically used to label the job in user interfaces. |
| queue | Yes | The name of the job queue. The trigger starts a job instance by sending a message to this queue. |
| pattern | No | Cron pattern that defines a fixed schedule for when the job should be executed. |
| max\_history | No | Number of historical instances to keep for this job, defaults to 100. |
| parameters | No | Parameters that controls how the job should be executed. |

Job parameters have the following (required) properties:

| Name | Required | Description |
| --- | --- | --- |
| required | Yes | Whether or not the parameter is required. |
| valueType | Yes | The type of the parameter. |
| default | No | The default value for the parameter (only allowed for required parameters. |
| desc | Yes | A description of the parameter. |

The job definitions should be defined in a implementation-specific subclass of `jobrunner.version_1.api.JobDefinitionsBase`.
The class property `jobs` should contain the job definitions. An example is shown below.

```
jobs = {'import_plansync':
           {'name': 'Import plan',
            'desc': "This job is used for importing released rosters from JCR.",
            'pattern': None,
            'queue': 'to.job.import_plansync',
            'parameters':
                {'filename':
                    {'required': True,
                     'valueType': api.ValueTypes.SELECT,
                     'desc': "Name of the file to import."
                    },
                 'scope_period_start':
                    {'required': False,
                     'valueType': api.ValueTypes.DATETIME,
                     'desc' : 'Defines the period start of data to be imported from message to data model.'
                    },
                 'scope_period_end':
                    {'required': False,
                     'valueType': api.ValueTypes.DATETIME,
                     'desc' : 'Defines the period end of data to be imported from message to data model.'
                    },
                 'scope_homebase':
                    {'required': False,
                     'valueType': api.ValueTypes.SELECT,
                     'desc' : 'Defines the rosters/trips to be imported by homebase.'
                    },
                 'scope_rosters_crewid':
                    {'required': False,
                     'valueType': api.ValueTypes.STRING,
                     'desc' : 'Defines specific rosters to be imported (comma separated list of crew ids).'
                    },
                 'create_flightlegs_operational':
                    {'required': False,
                     'default': 'false',
                     'valueType': api.ValueTypes.BOOL,
                     'desc' : "Whether missing flight legs should be created as operational or not."
                    },
                },
            },

        'export_plansync':
            {'name': 'Export plan',
             'desc': "This job is used for exporting rosters to JCR.",
             'queue': 'to.job.export_plansync',
             'pattern': '0 8 * * * *',
             'parameters':
                {'period_start':
                    {'required': True,
                     'valueType': api.ValueTypes.DATETIME,
                     'desc' : 'Defines the period start of data to be exported.'
                    },
                 'period_end':
                    {'required': True,
                     'valueType': api.ValueTypes.DATETIME,
                     'desc' : 'Defines the period end of data to be exported.'
                    },
                },
            },
         }
```

**Parameter types**

The valueType property of parameters should have a value from the `jobrunner.version_1.api.ValueTypes` list of class members. The following value types are defined:

* SELECT
* STRING
* INT
* FLOAT
* BOOL
* DATE
* TIME
* DATETIME
* TIMEDELTA

**SELECT parameters and callbacks**

The SELECT value type means that the value is picked from a list of possible values, returned from a callback method.
The callback method is a member of the job definitions class and should override `jobrunner.version_1.api.JobDefinitionsBase.get_param_values()`.
There is only one callback method, and it must handle all SELECT parameters for all jobs.

In the example below, the callback is implemented for the filename and scope\_homebase parameters of the import\_plansync job.

The callback for filename is implemented by an external process that communicates via an ActiveMQ queue. The callback for homebase returns a list based on catalog data in the plan.

```
def get_param_values(self, job_id, param_name):
    if job_id == 'import_plansync':

        if param_name == "filename":
            content, _ = api.send_message('to.camelroute.list_job_files', receive=True)
            return json.loads(content)

        if param_name == "homebase":
            return [str(i.getId()) for i in ara_core.Base.getInstances(self.plan)]

    return super(Jobs, self).get_param_values(job_id, param_name)
```

**Default values**

Parameters may have default values. For jobs that are automatically triggered using a cron pattern, default values must be provided for all required parameters. Only required parameters can have default values.

Default values can be provided in two ways:

* List default value explicitly in the job definition
* Provide value in callback method

When the jobrunner trigger requires a default parameter value, it first checks if there is a default value in the job definition. If not, it will call a callback method to get the value.
The callback method is a member of the job definitions class and should override `jobrunner.version_1.api.JobDefinitionsBase.get_default_values()`.

The parameter start\_time represents the scheduled start time for the job. Some parameters (e.g. parameters for start and end time of periods) are likely to depend on the on the start time of the job.

```
def get_default_value(self, job_id, param_name, start_time):
    if job_id == 'export_plansync':
        if param_name == 'period_start':
            val = api.to_abstime(start_time).month_floor()
            return api.to_datetime(val)
        if param_name == 'period_end':
            val = api.to_abstime(start_time).month_ceil()
            return api.to_datetime(val)

    return super(Jobs, self).get_default_value(job_id, param_name, start_time)
```

**Setting the message body**

The body of the outgoing message created by the jobrunner trigger can be set by overriding the method `jobrunner.version_1.api.JobDefinitionsBase.get_default_values()` in the job definitions class.
The method takes a job instance dictionary as input and should return the message body.

A job instance is a dictionary with the following keys:
\* jobId
\* parameters (dictionary with parameter keys and values)

Example:

```
def get_message_body(self, job_instance):
    if job_instance['jobId'] == "export_plansync_jcr":
        request_content = """<?xml version="1.0" encoding="utf-8"?>
            <tns:getJCRCrewDataRequest
            xmlns:tns="http://crewdata_output_jcr.service.jcms.jeppesen.com"
            version="3.1.1" source="jobrunner" created="%s"/>
                """ % dt.any2dt(self.now).replace(tzinfo=tz.tzutc()).isoformat()
        return request_content
    return super(Jobs, self).get_message_body(job_instance)
```

**Setting message headers programmatically**

If there are job parameters that are constant or can be derived from the job definition and other parameters,
they can be set by overriding the method `jobrunner.version_1.api.JobDefinitionsBase.get_derived_headers()`

Example:

```
def get_derived_message_headers(self, job_instance):
    if job_instance['jobId'] == "sap_travel_expenses":
        return {'report_name': 'travel_expenses'}
    return super(Jobs, self).get_derived_message_headers(job_instance)
```

**Customizing scheduled job execution time**

The next scheduled execution time for a job, calculated by the scheduler, can be customized by overriding
the method `jobrunner.version_1.api.JobDefinitionsBase.get_next_schedule_time()`

The method must return a `datetime.datetime` instance in UTC or `None` if the job shouldn’t be automatically scheduled to run.

Example:

```
def get_next_schedule_time(self, job_definition):
    if job_definition.get('id') == 'my_job':
        dt = self._get_custom_schedule_time()
    else:
        dt = super(Jobs, self).get_next_schedule_time(job_definition)
    if dt is None:
        return None
    ap = ara_air.Airport.find('GOT', self.plan)
    utc_abs = ap.toUTCTime(to_abstime(dt))
    return to_datetime(utc_abs)
```

#### Configuration

#### Executing jobs


The scope of the Jobrunner framework is limited to generating a message on a specific job queue whenever a specific job instance should be run.

In order to start a job, the Jobrunner trigger sends a message to the queue specified in the job definition.
The message body is empty unless it has been set in the job definition class and the job id and parameters are sent as message headers. (The name of the job id header is *jcms\_job\_id*.)

The Jobrunner framework is not used for performing the actual tasks of the job. Instead some other component in JCMS must consume the message from the job queue,
perform the actual tasks of the job and use the Jobrunner Service API to report the progress and status of the job instance.
The component that performs the job will typically call the *updateJobInstance* operation and use the job instance id provided
in the jcms\_jobid message header.

Below is an example of a component that perform a job implemented as an Apache Camel route.
The job fetches a file from an external source, import the file to the CMS database and finally renames the file.

![Sequence for an example component performing a job](../_images/jobrunner_example_job.png)

In the example above the Camel Route is active during the full lifetime the job is running and orchestrates the differents tasks that is being performed.
The Camel Route will typically implement some Pokémon try/catch clause for catching all errors while performing the actual tasks of the job.
When an error is raised, the Camel Route uses the Jobrunner Service API for setting the status of the job instance to “failed”.

#### Indices and tables

### Setup of processes and services


* [Grouping and setup of interfaces](classification.html)
  + [IOService grouping](classification.html#ioservice-grouping)
  + [High availability setup of IOServices](classification.html#high-availability-setup-of-ioservices)
  + [Integrator Setup](classification.html#integrator-setup)
* [Inbound Feeds](inbound_subscribe_online.html)
  + [The standard flight operations interface](inbound_subscribe_online.html#the-standard-flight-operations-interface)
  + [The standard flight schedule interface](inbound_subscribe_online.html#the-standard-flight-schedule-interface)
  + [The standard interfaces for crew](inbound_subscribe_online.html#the-standard-interfaces-for-crew)

#### Grouping and setup of interfaces


This chapter aims to provide guidelines for the setup and grouping of interfaces.
It will cover the setup of IOServices on IOServer instances as well as integrator/router components and
some information about the internal broker and queue system.

###### IOService grouping

Generally it is preferable to share each instance of an IOServer as much as possible since that will reduce the overall
resource consumptions of the system. Each IOServer main process maintains a local plan in memory and refreshes it from
the database regularly. The fewer such copies are around the less memory and database resources are used.

In a real system there are some constraints that limit the sharing. The most obvious constraints are connected to the
resource capacity of a single host, they are data scope and CPU load. Other constraints stem from the
worker factory design in combination with service behavior expectations.

An approach to determine a good overall service distribution is to

* group them by criticality, data scope and setup type
  \* create rather small groups in this step
  \* consider batches with non-overlapping batch windows as separate groups
* calculate the capacity of each group and distribute services where needed,
  \* prefer a full and a low-load instance over two equally loaded in this step
  \* several batch-groups with non-overlapping time window can share the same capacity slots
* merge groups if there is exceed capacity and the setup merge is acceptable
* redistribute between several instances of the same (merged) group to even the load more

####### Distribute service workers

Some driving factors to separate services on different IOServer instances with respect to service behavior
are the handling times and refresh cycle requirements. Services with general long handling times or broad variation in
timing require longer worker timeout settings. Running such services together with services that expect a
high refresh rate (e.g. web back-end services that implement session consistency or online inbound interfaces with
strong ordering dependencies) will result in overall higher memory consumption due to the
copy on write semantics of the shared memory holding the plan. There is also a risk of some performance impact
for the online interfaces. This effects need to be balanced with the extra overhead for separating IOServer instances.

Another aspect is the high availability (HA) setup explained in more detail below. Services that require different HA setup should be
separated and services which are less robust should not be placed together with highly critical services to avoid
negative side effects.

####### Distribute Data scope

The size of the loaded data context besides requiring memory also affects load, refresh and handling times.
The data context should therefore be configured not to contain too much data.
Most services will likely deal with data around the current date, so the default IOServer data context is often set to
contain about 3 months of data which should be good enough for those use cases.

If services need to operate on other data it is advisable to not put them on the same server instance as all the
online services because that would require a bigger plan for the sum of them and affect all services performance.
It is better to create one or more separate instances, depending on the variation in data need, to cover the special
cases.

####### Distribute CPU capacity

When thinking about CPU capacity the main driver is a basic load balancing. The limit for one host is reached when the
peak of the sum of expected load leads to unacceptable latencies in at least one service. If services need to be
distributed then its a good idea to put services into different instances that have peak loads at the same time and
keep services with different peaks together. This is specially interesting when looking at batch loads, it is often
possible to influence the timing of some jobs so that peak load conflicts can be avoided. Batch jobs can without
problems be deployed together with other services that have higher loads during the day
but are more or less idling during the night.

A rule of thumb is that the number of workers that are busy in parallel should preferably not exceed the number of
cores to avoid delays. If the number of concurrent busy workers is significantly higher there will be
a performance penalty, so the real total throughput becomes lower than what it would be if there were less workers.
Interfaces that do not have any messages to process at the time do not significantly contribute to this penalty, unless
there are so many that the worker handling itself becomes a significant workload.

A further option for load balancing is to distribute workers for the same service over several IOServer instances.
This can be applied if the service has no strong ordering dependencies (e.g. for web session back-end services) or if
the traffic is routed to divide it by dependency. Generally it is advisable to distribute workers for such service on
different IOServer instances if they are already set-up due to the overall resource limitations.

On the other end of the spectrum it is possible to use a single IOService with a dispatch handler to serve several
interfaces of the same pattern and handling class at runtime, delegating the requests to the separate handlers based on
content or a header attribute set by the inbound route. The main limitation with such a setup is the risk that some
messages are waiting in the queue longer due to errors or peak loads on another interface sharing the dispatcher.

###### High availability setup of IOServices

The availability of an IOService has two parts:

* At what times could events occur that need to be handled?
  Any time without ahead notice or just 2-3AM on first Monday every month?
* What delay is acceptable to get the service ready when an event occurs?
  Would it be ok if the message on the queue waits an hour?
  Or do we need another instance online to take on within seconds?

All interfaces where it is not acceptable to await a (automated or manual) server restart need to be deployed on at
least two nodes. For 24/7 instances the restart used to shift the datacontext need to be timed so that
the first node is up again before the second is restarted.
If the overall service window is not 24/7 then the same hardware slots could be reused during offline
time for other services with defined availability windows.

For services that need several nodes there are again two types, distinguished by the
*exclusive* vs. *parallel* IOService patterns described in the [[DG\_SAD]](../index.html#dg-sad).

Services that fall under any of the *parallel* patterns can have several parallel workers active at any point in time.
The most robust setup for these is to distribute the total number of workers needed to serve the
interface over the available nodes as active-active cluster.
The service will thus be available as long as any of the nodes is working. During restart of the single nodes or when a
node fails the service will have a lower capacity which might affect the latency of single messages, but it is still operating.

Services that fall into any of the “exclusive\* patterns described in the [[DG\_SAD]](../index.html#dg-sad)
must only run active on a single node at any time. There is currently no support to handle
service level active-passive setup or fail-over, therefore these service must be placed on an active-passive pair of
IOServer instances. The main limitation with this is of course that fail-over will only happen automatically if the
active IOServer instance stops (e.g. for restart), not if a single service has problems.

###### Integrator Setup

The Integrator setup for each system consists of one or more JEE applications that are deployed on one or more
HA JBoss clusters. In a typical system there are different kinds of contact points into the system with different
setup considerations.

Interfaces that interact with external message queues or storage (shared disk or FTP server) do not expose a service
endpoint to be contacted “from the outside”. They do not need to be found since they initiate the communication.
They might need to authenticate themselves to the external server,
but don’t require authentication or authorization to accept a message.
These are typically grouped in a *feeds integrator* application containing all the routes
that connect the external message sources/sinks with the internal IOService queues.

Web services do expose an HTTP(S) endpoint that is contacted “from the outside” and thus need to be found and
require authentication/authorization. Normally that is handled by a separate Apache web server instance,
see the Deployment chapter in the [[WPF\_SAD]](../index.html#wpf-sad). Under this category fall
services that are part of web applications used by human users as well as
services which will be called by external applications (potentially on behalf of a human user)
and also services that are accessed from within other JCMS applications.
Services that belong to web applications are deployed together with the application,
standalone services are normally deployed as a *wsrouter* integrator application.
Services with different security requirements, e.g. only internally accessible, should typically be put is different
applications to allow easier configuration of the context inside the JBoss and Apache server(s).

##### IOService grouping

###### Distribute service workers

###### Distribute Data scope

###### Distribute CPU capacity

##### High availability setup of IOServices

##### Integrator Setup

#### Inbound Feeds


This chapter describes some concrete realizations of inbound feeds.
It is work in progress.

###### The standard flight operations interface

The standard interface for [Operational Flight Input](../std_interfaces/flight_input_ops.html#stdif-flight-input-ops) can be used to provide flight data to JCMS during operation.
Short before and during operation there will usually be frequent updates to the flight information,
capturing the estimated or actual movements of the aircraft or any disturbances to the planned flow.
Each message will normally only deal with information about a single leg or flight, but some systems support a
bigger decision scope, so that the same message could capture changes to a group of flights at once. Due to the timing
of events during operation messages affecting the same leg would typically come with a few minutes interval,
but there can be cases where several messages about the same leg arrive within the same minute. This can happen for
example if the decision about delay/rerouting is implemented or communicated in several steps.
The standard interface is designed for a situation where all information about operational state of the flights
is coming from a single logical source that is assumed to be master of the data.
If the data shall be fed from several sources that are
not synchronized with each other then some extra logic is required.

The handling time for a typical flight operation message (one that affects a few legs at most) is well below a second.
The acceptable latency for applying an incoming message is much higher, even if it goes up to about a minute
in a few cases that’s OK. It is important on the other hand to make sure that the information about the status of all
flights is reliably updated and temporary issues must not propagate.
We can conclude therefore that using the analysis matrix from the [[DG\_SAD]](../index.html#dg-sad),
this interface falls under the category subscribe with light to medium handling,
persistent requests and loose latency and using an IOService pattern supporting retry strategies is required.

The interface design uses partial-state messages with a granularity of a planned flight leg which
implies a potential strict dependency between messages affecting the same leg according to the definition in the [[DG\_SAD]](../index.html#dg-sad).
Since each message will result in an update of some data on the leg, using the standard flight key conflict trigger will
reduce this to a strong ordering dependency. It still requires an exclusive consumer. For most customers a single
worker should be able to cope with the workload. If a higher throughput is required the service must be split using
content base routing (e.g. select by flight number).

Since the interface is critical for operation it should be setup with high availability.
The combination of HA and exclusive consumer requires today an active/passive setup.

Normally the messages will be available in a message queue on an external broker. An Apache Camel route in the
integrator will forward those to the in-queue of the IOService. The standard interface supports usage
of an error queue which will be used if a response queue is configured in the IOService.
The error queue can either be forwarded to the external broker
using the integrator or it can be consumed by a monitoring application directly (currently not implemented).

###### The standard flight schedule interface

The standard interface for stdif-flight-input-schedule allows CMS to receive initial and updated information
about the flight schedule *before* day of operation. The initial information is typically sent in a batch manner,
either as a *schedule state* or as a set of single flights. For the *Flight Based Input Service*
the same considerations apply as for the operations interface explained above. The *Flight Schedule State Service* is
a state message without any reasonable conflict detection, so the *strict dependency* between messages cannot be
resolved. It is important to keep in mind that the interface cannot handle two messages with overlapping scope within
the same ordering phase interval and is thus only usable in batch-like setups.

###### The standard interfaces for crew

The standard interfaces for [Crew Data Input](../std_interfaces/crew_input.html#stdif-crew-input) can be used to provide crew data to the JCMS.
The majority of crew data will likely be maintained using scheduled export batches
from the source systems. The standard interfaces are designed for situations where only data that is
actually been modified is sent, not all data for all crew is repeated. If all state is sent the resulting state
will be correct but there might be bigger change-sets visible in the JCMS applications.

On the JCMS side the interface is typically configured as online interface i.e. accepting requests at any time,
that allows a flexible reconfiguration of the source batches and also
enables direct forwarding of changes from e.g. online self-service systems.
If there is no flexibility requirement the IOServices could be placed on an IOServer instance that is only active
during the batch window.

The messages can be very big e.g. if a whole crew group is placed in a single message for initial load.
Normally there are not so many changes in a single batch, but the processing time can vary a lot depending on
the size of the message. It can be several minutes for a full batch. The accepted latency is loose or even irrelevant.
The interface design uses partial-state messages which implies potential strict dependency
between messages affecting the same crew. This is usually not a problem if the batches are scheduled not too tight.
If online updates from some interactive system are used for some data then
a conflict trigger or jcms-state shall be used to reduce the coupling.
There will be a standard conflict trigger that protects the business key of crew.

The batches would normally be implemented using message queues or a file drop. Any online service should probably be
provided via queues or as web service, depending on the error handling requirements.

##### The standard flight operations interface

##### The standard flight schedule interface

##### The standard interfaces for crew

### Troubleshooting

#### IOServer log

###### IOServer log

Ref to Datafeeds Configuration Developer Guide IOServer logs - Log format.

To find the start of a log statement for a specific interface for a message, look for `Calling`,
this is when the IOServer has fetched the message, or is time triggerred, and start processing it. To find the end of the processing,
look for `Committing the message (id:`. The Jcmslog MDC service value will be the IOServer service name.

```
<14>1 <timestamp> <hostname> <process name> 32605 OPER [details@38555 cid="29" flow="ioserver.python.Caller" msgId="293d5414-58ff-4fb6-baf5-c651808676bf" service="<ioservice name>"] <U+FEFF>Calling handler '<handler name>'
```

If the handler is run due to an incoming message, a bit above the `Calling` statement, the `Fetched` statement is logged, like:

```
<14>1 <timestamp> <hostname> <process name> 7357 OPER [details@38555 msgId="ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1" flow="ioserver.qpid.QpidMessageSource.<ioservice name>"] <U+FEFF>Fetched message: [msgId="ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1" correlation-id="b870a12f-9937-4609-9c26-013cf0b30a97" jcms_traceid=<trace id> jcms_state=<CID>]
```

If set, the `jcms_traceid` header is used to identify a request from/to the integrator. If not already set, It is set by the Integrator
to the `breadcumbId` if available, otherwise to the messageId.

The `jcms_state` header is set to the `CID`.

Reference IOServer messaging.

The `Commiting the message (id:` log statement:

```
<14>1 <timestamp> <hostname> <process name> 7357 OPER [details@38555 cid="114" msgId="ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1" service="<service name>" flow="ioserver.requestresponse.df_batch_out"] <U+FEFF>Committing the message (id: ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1) from the queue.
```

####### Dispatch / Map pattern

If the IOServer configuration, is using the dispatch / map functionality, see ref IOServer - Patterns - Dispatch, then the IOServer log statements
will use the service\_name attribute value or the handler attribute value (if service\_name is not defined), as Jcmslog MDC service value.

This is only true, as long as the handler is in action, as soon as the handler has finished, and leave control to the IOServer worker to
take care of sending the response, the service value will be the IOServer ioservice name again.
This means that when looking for `Calling` and `Committing the message (id:` the service value will be the ioservice name.
And the handler in the `Calling handler` statement will be the IOServer dispacth\_handle.handler.

```
<14>1 <timestamp> <hostname> <process name> 7357 OPER [details@38555 cid="114" flow="ioserver.python.Caller" msgId="ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1" service="<ioservice name>"] <U+FEFF>Calling handler 'jcms.ioserver.version10.dispatch_handler.handle'
```

In the subsequent log statements for the handler, the service value, will be the service\_name attribute value, or the handler attribute value, like:

```
<14>1 <timestamp> <hostname> <process name> 7357 OPER [details@38555 cid="114" flow="ioserver.<ioservice name>.service" msgId="ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1" service="<service name>"] <handler log message
```

##### Dispatch / Map pattern

#### Integrator log

###### Integrator log
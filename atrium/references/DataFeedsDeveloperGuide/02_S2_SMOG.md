## SMOG


The purpose of this document is to describe the how to use SMOG (Service Model Object Generator), a tool that can be used to develop services.

* [1. Introduction](smog.html)
  + [1.1. Concepts](smog.html#concepts)
  + [1.2. SMOG for Dummies - a Hello World example](smog.html#smog-for-dummies-a-hello-world-example)
* [2. Service Specification](smog.html#service-specification)
  + [2.1. Struct extensions](smog.html#struct-extensions)
  + [2.2. Service extensions](smog.html#service-extensions)
  + [2.3. Backward compatibility](smog.html#backward-compatibility)
  + [2.4. Deprecation support](smog.html#deprecation-support)
* [3. Protocol Specification](smog.html#protocol-specification)
  + [3.1. Supported protocols](smog.html#supported-protocols)
* [4. Service mapping](smog.html#service-mapping)
  + [4.1. Input mapping](smog.html#input-mapping)
  + [4.2. Output mapping](smog.html#output-mapping)
  + [4.3. Mapping extensions](smog.html#mapping-extensions)
  + [4.4. Order of execution](smog.html#order-of-execution)
  + [4.5. Pre- and post processing](smog.html#pre-and-post-processing)
* [5. Using SMOG](smog.html#using-smog)
  + [5.1. Generated service implementations](smog.html#generated-service-implementations)
* [6. Customizing SMOG](smog.html#customizing-smog)
  + [6.1. Customizing Protocols](smog.html#customizing-protocols)
  + [6.2. Customizing Languages](smog.html#customizing-languages)

#### Indices and tables

* [Index](../genindex.html)
* [Search Page](../search.html)

### Introduction

#### Concepts

#### SMOG for Dummies - a Hello World example

###### 1.2. SMOG for Dummies - a Hello World example

1. Download SMOG from Gitlab:

   ```
   > git clone git@git.got.jeppesensystems.com:TD/smog.git
   > cd smog
   ```
2. Create a service specification and save it as service.xml:

```
<service-spec name="hello" xmlns="http://namespace.jeppesen.com/smog/v2">
   <services>
      <service name="Hello" version="1">
         <operation name="sayHello">
            <input type="EmptyStruct"/>
            <output type="HelloStruct"/>
         </operation>
      </service>
   </services>
   <types>
      <struct name="EmptyStruct"/>

      <struct name="HelloStruct">
         <member name="helloMessage" type="string"/>
      </struct>
   </types>
</service-spec>
```

3. Create a protocol specification and save it as protocol.xml:

```
<protocol-spec xmlns="http://namespace.jeppesen.com/smog/v2" target="hello">
   <protocol name="plainxml"/>
</protocol-spec>
```

4. Create a service mapping and save it as mapping.xml:

```
<service-mapping xmlns="http://namespace.jeppesen.com/smog/v2" language="Python">
   <server-impl service_name="Hello" service_version="1"/>

   <output-mapping struct="hello.HelloStruct">
      <out member_or_variant="helloMessage" expr="'Hello World!'"/>
   </output-mapping>
</service-mapping>
```

5. Run SMOG to build protocol and mapping artifacts:

   ```
   > app/src/main/bin/smog -s service.xml -p protocol.xml -m mapping.xml
   ```
6. Call the generated service implementation with just the shell as “runtime environment”:

   ```
   > python hello/Hello_1_server.py "<sayHelloRequest xmlns='http://service.jcms.jeppesen.com/Hello/v1'/>"
   ```
7. You should get the following output from the service:

   ```
   <?xml version='1.0' encoding='UTF-8'?>
   <sayHelloResponse xmlns="http://service.jcms.jeppesen.com/Hello/v1" helloMessage="Hello World!"/>
   ```

### Service Specification


The service specification declares any number of services. A service is always specified with a name, a version and a set of operations.
A service specification may contain several versions of the same service. Services are typically organized around business capabilities,
for example, a service called “Flight” could have operations “getFlight” and “cancelFlight”.
The service specification can be seen as an API with public methods that the service provides to clients calling the service.
Each operation is further defined, describing the input that should be passed to the operation.
An operation typically has an output, a response, which is provided back to clients invoking the operation.
Operations without output are called “one-way” operations and don’t provide any response back to clients when the operation is invoked.
An operation can also define a fault, a specific return type used when an error occurs. The fault can be seen as an exception that might
be thrown back to the client calling the operation.

Service definitions are described using a SMOG specific xml syntax as shown in the example below.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="flight">
    <services>
        <service name="Flight" version="1">
            <operation name="getFlightStatus" desc="Get status for a given flight.">
                <input type="FlightDesignator" desc="The flight to get status for."/>
                <output type="FlightStatus" desc="Status of the flight."/>
                <fault type="Error" desc="Error that occurred when calling this operation."/>
            </operation>
            <operation name="cancelFlight" desc="Cancels the given flight.">
                <input type="FlightDesignator" desc="The flight to cancel."/>
            </operation>
        </service>
    </services>

    <types>
        <struct name="FlightDesignator" desc="Information required for identifying a flight.">
            <member name="airline" type="string" desc="Airline code"/>
            <member name="number" type="int" desc="Flight number"/>
        </struct>

        <struct name="FlightStatus" desc="Information required for identifying a flight.">
            <member name="flight" type="FlightDesignator" desc="The flight this status applies to."/>
            <member name="departureTime" type="dateTime" desc="The departure time of this flight."/>
            <member name="arrivalTime" type="dateTime" desc="The arrival time of this flight."/>
            <member name="scheduleStatus" type="string" desc="Scheduled status of this flight."/>
        </struct>
        <struct name="Error" desc="Information about an error that occurred.">
            <member name="type" type="string" desc="Type of error."/>
            <member name="detail" type="string" desc="Detailed information about the error."/>
        </struct>
    </types>
</service-spec>
```

The root element <service-spec> must specify the SMOG syntax version to use, this is done by setting the xmlns attribute to a specific SMOG syntax version.

The current version is **2**, version **1** should only be used for migrating services from Interface Builder (ifbuilder) tool.

The root element <service-spec> must also have a module **name**, which specifies a prefix used for avoiding naming conflicts when importing other service specification modules.
The <input> and <output> elements of the operations specifies the type of information that is passed to the operations and what type of information that is provided as return.
The operation cancelFlight is a “one-way” operation and does not have any <output> element.

The types section consists of <struct> elements, providing the details of the types used as input and output by the operations.
A struct can be seen as a complex data type, consisting of named **members** with a type that either is **plain** or **complex**.

The following **plain** types are supported:

* **string**: represents a string value.
* **int**: represents a number without any fractional digits.
* **(integer)**: *Deprecated*, only available in SMOG version 1, used int instead.
* **float**: represents a precision floating-point type (including infinity and not-a-number).
* **boolean**: represents a true or false value.
* **date**: represents a date (without time fraction).
* **time**: represents the time fraction on a day (00:00:00 - 23:59:59)
* **dateTime**: represents a date with time fraction.
* **duration**: represents a time interval.
* **text**: represents a multi line string.
* **(any)**: *Deprecated*, only available in SMOG version 1, represents value of any type.

Members of **complex** types refers to some other struct, for example the member “flight” in struct “FlightStatus”.

A struct can also contain **<variant>** elements, defining mutual exclusive members, which means that only one of the variants can have a value.
Only one “group” of variants can be specified in a struct. If more than one “group” of variants are needed they must be specified in separate structs.

```
<struct name="PersonDetails" desc="Information about a person">
    <variant name="employee" type="EmployeeDetails" desc="Information for an employee."/>
    <variant name="contractor" type=" ContractorDetails" desc="Information for a contractor."/>
    <member name="firstName" type="string" desc="Given name of this person."/>
</struct>
```

The struct for PersonDetails above specifies that either employee or a contractor must be provided for a person, but not both at the same time.

Members and variants can also have a **cardinality**, specifying the allowed multiplicity for each member or variant. The cardinality is specified with brackets after the type, for example:

```
<struct name="PersonDetails" desc="Information about a person">
    <variant name="employee" type="EmployeeDetails" desc="Information for an employee."/>
    <variant name="contractor" type="ContractorDetails" desc="Information for a contractor."/>
    <member name="firstName" type="string" desc="Given name of this person."/>
    <member name="middleName" type="string[0:1]" desc="Middle name of this person."/>
    <member name="address" type="AddressDetails[1:]" desc="An address for this person."/>
    <member name="assignment" type="WorkAssignment[:]" desc="A work assignment for this person."/>
    <member name="lastDayOfService" type="date[0:1]" desc="Last day of employment for this person." nullable="true"/>
</struct>
```

* Types without any specified cardinality means that the member is **required** and must occur exactly once in the struct, for example “firstName” in the example above.
* A cardinality of **[:1]** or **[0:1]** means that the member is **optional** and can occur zero or one time, for example “middleName” in the example above.
* A cardinality of **[]** or **[:]** means that the member is optional and multi-valued and can occur zero or more times, for example “assignment” in the example above.
  Note that the member name is “assignment” and not “assignments” since each member instance describe one assignment.
* A cardinality of **[1:]** means that the member is multi-valued, but is required to occur at least once in the struct, for example “address” in the example above.
  Note that the member name is “address” and not “addresses” since each member instance describe one address.
* For multi-valued members it is also possible to specify min and/or max values explicitly, e.g. **[2:3]** means that the member must occur 2 or 3 times.

Members and variants can also be specified to be **nullable**, as the `lastDayOfService` member in PersonDetails struct above.
Specifying a member or variant as nullable allows the member or variant to be a null-value instead of always being a value of the type specified for the member or variant.

The nullable `lastDayOfService` member can take three states in PersonDetails struct:

1. lastDayOfService is set to a date value.
2. lastDayOfService is not specified (the member is optional).
3. lastDayOfService is set to a null value.

States 2 and 3 might appear similar, but state 2 doesn’t say anything about the value of lastDayOfService whereas state 3 clearly indicates that value of lastDayOfService is null.

The usage of nullable is limited to single valued members and variants and cannot be used for members and variants with a multi-valued cardinality.

##### 2.1. Struct extensions

A struct can inherit members and variants from a parent struct by specifying the **based\_on** attribute.

```
<struct name="Person" desc="Information about a person.">
    <member name="firstName" type="string" desc="Given name of this person."/>
    <member name="lastName" type="string[0:1]" desc="Last name of this person."/>
</struct>
<struct name="Student" based_on="Person" desc="Information about a student.">
    <member name="graduationYear" type="int" desc="Year when this student graduated."/>
</struct>
<struct name="Employee" based_on="Person" desc="Information about an employee.">
    <member name="employmentDate" type="date" desc="When this person was employed."/>
</struct>
```

Inheritance can also be used to redefine members, i.e. to change the type, cardinality or description.

```
<struct name="Person" desc="Information about a person.">
    <member name="firstName" type="string" desc="Given name of this person."/>
    <member name="lastName" type="string[0:1]" desc="Last name of this person."/>
</struct>
<struct name="Student" based_on="Person" desc="Information about a student.">
    <member name="major" type="string" desc="Academic major subject"/>
</struct>
<struct name="GraduateStudent" based_on="Student" desc="Information about a graduate student.">
    <member name="major" type="string[1:]" desc="Academic major subjects"/>
</struct>
```

Using inheritance is a good pattern for avoiding duplications in the service specification. It also helps when implementing the service since same logic often can be applied for handling the base struct.

Structs can be organized in **modules**, where each module is stored as a separate xml file. A module contains services and/or structs.
A complete service specification can thus consist of several modules put together by <include> elements as shown in the example below.
The <include> element specifies the path to the file where a module is stored.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="common">
    <types>
        <struct name="Person" desc="Information about a person.">
            <member name="firstName" type="string" desc="Given name of this person."/>
            <member name="lastName" type="string[0:1]" desc="Last name of this person."/>
        </struct>
    </types>
</service-spec>
```

The service specification module above is named “common” and defines a struct called “Person”. If that module is saved as “common\_structs.xml” it could be included by another service specification module:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="school">
    <include href="common_structs.xml" />
    <types>
        <struct name="Student" based_on="common.Person" desc="Information about a student.">
            <member name="graduationYear" type="int" desc="Year when this student graduated."/>
        </struct>
        <struct name="Employee" based_on="common.Person" desc="Information about an employee.">
            <member name="employmentDate" type="date" desc="When this person was employed."/>
        </struct>
    </types>
</service-spec>
```

As the above example shows, structs defined in the included module are referenced using their fully **qualified name** <module name>.<struct name>.
For example “common.Person” is the qualified name of struct “Person” in module “common”.
The qualified name is needed for uniquely identifying the struct since more structs named “Person” could be included from other modules.

By using the <struct-update> element, it is possible to add members and variants to structs defined in e.g. an included module.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="school">
    <include href="common_structs.xml" />

    <types>
        <struct-update struct="common.Person">
            <add-variant name="personalNumber" type="int" />
            <add-variant name="temporaryPersonalId" type="string"/>
            <add-member name="birthdate" type="date" desc="The birthday of this person."/>
        </struct-update>
        <struct name="Student" based_on="common.Person" desc="Information about a student.">
            <member name="graduationYear" type="int" desc="Year when this student graduated."/>
        </struct>
        <struct name="Employee" based_on="common.Person" desc="Information about an employee.">
            <member name="employmentDate" type="date" desc="When this person was employed."/>
        </struct>
    </types>
</service-spec>
```

By using the <struct-update> element, it is also possible to modify members and variants to existing structs.
In the following example, assume the service specification module “school” is saved as “school\_structs.xml”.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="school">
    <types>
        <struct name="Student" desc="Information about a student.">
            <member name="firstName" type="string" desc="Given name of this student."/>
            <member name="lastName" type="string[0:1]" desc="Last name of this student."/>
            <member name="graduationYear" type="int" desc="Year when this student graduated."/>
        </struct>
        <struct name="GraduateStudent" based_on="Student" desc="Information about a graduate student.">
          <member name="major" type="string[1:]" desc="Academic major subjects"/>
        </struct>
    </types>
</service-spec>
```

Members/variants of these structs can then be modified using the <update-member> and <update-variant> elements:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="myschool">
    <include href="school_structs.xml" />

    <types>
        <struct-update struct="school.GraduateStudent">
            <update-member name="major" type="MajorSubject[1:2]" desc="Academic major subjects, restricted to maximum two."/>
        </struct-update>
        <struct name="MajorSubject" based_on="common.Person" desc="Information about a student.">
            <member name="subject_name" type="string" desc="The name of the major subject."/>
            <member name="credits" type="int" desc="Credits granted for this subject"/>
        </struct>
    </types>
</service-spec>
```

Using <struct-update> or inheritance with “based\_on” provides similar results, with the difference that <struct-update> doesn’t define any new struct in the service specification.
This is a vital difference when it comes to the [Service Mapping](#service-mapping) concept since mappings are defined for the structs.

##### 2.2. Service extensions

Not only structs can be included from other modules and updated, but also services can be included and updated by using the <service-update> element.
Updating existing services provides much flexibility as it makes it easy to reuse a service while adding new operations, adding output or fault messages to existing services.

In the example below, the operation “reschedule” is added to the “Flight” service which is defined in a module stored in file “flight/services.xml”.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="flight_ext">
    <include href="flight/services.xml" />
    <services>
        <service-update name="Flight" version="1" updated_version="1.1">
            <add-operation name="reschedule" desc="Reschedules the given flight.">
                <input type="RescheduleFlight" desc="Information of what flight to reschedule."/>
            </add-operation>
        </service-update>
    </services>
</service-spec>
```

The example below shows how output and fault messages can be added to an operation that was originally defined as “one-way”, i.e. only having an input message.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="flight_ext">
    <include href="flight/services.xml" />
    <services>
        <service-update name="Flight" version="1" updated_version="1.1">
            <add-output operation="cancelFlight" type="TripInfo" desc="Information about affected trips."/>
            <add-fault operation="cancelFlight" type="flight.Error"/>
        </service-update>
    </services>

    <types>
        <struct name="TripInfo">
            <member name="numberOfTrips" type="int"/>
            <member name="numberOfCrew" type="int"/>
        </struct>
    </types>
</service-spec>
```

Another way to change an included service is to redefine it. In the following example, the version 1 of the Flight service is redefined such that
the type of the output message of operation “getFlightStatus” is changed and the operation “cancelFlight” is removed:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="flight_ext">
    <include href="flight/services.xml" />
    <services>
        <service name="Flight" version="1">
            <operation name="getFlightStatus" desc="Get status for a given flight.">
                <input type="flight.FlightDesignator" desc="The flight to get status for."/>
                <output type="MyFlightStatus" desc="Status of the flight."/>
                <fault type="flight.Error" desc="Error that occurred when calling this operation."/>
            </operation>
        </service>
    </services>

    <types>
        <struct name="MyFlightStatus" based_on="flight.FlightStatus">
           <member name="scheduleStatus" type="int" desc="Numeric status code."/>   <!-- redefines the member of the base struct -->
           <member name="returnCounter" type="int" desc="Return to ramp count."/>
       </struct>
    </types>
</service-spec>
```

##### 2.3. Backward compatibility

When a version of a service has been deployed in a production runtime environment, only limited changes are allowed to the service specification in order not to break existing consumers/clients.
Exactly which changes are allowed depend on the protocol but normally the following applies:

* Adding optional members to input messages
* Removing optional members from output messages
* Changing cardinality of members in input messages from required to optional
* Changing cardinality of members in output messages from optional to required
* Adding operations to a service

Please refer to chapter [Protocol Specification](#protocol-specification) for details about specific protocols.
All other changes require a major version change of the service and thus forces consumers/clients to upgrade their protocol artifact versions.

SMOG however allows additional flexibility by introducing the possibility to annotate struct members with attributes **backward\_compatible\_addition**
and **backward\_compatible\_removal**. By using these attributes it is possible to apply additional changes to an interface,
while still maintaining backward compatibility within its current major version. Normally the following additional changes apply, although it may differ for individual protocols:

* Adding and removing optional members of any type to/from input and output messages
* Removing required members from input messages
* Adding required members to output messages

The value of the **backward\_compatible\_addition** and **backward\_compatible\_removal** attributes is a date. All changes with a certain date
represent one minor version of the service specification and date itself typically corresponds to the release date of the minor version.
Hence a particular major version of a service may aggregate backward compatible changes of more than one minor version.

##### 2.4. Deprecation support

In the service specification, elements <service>, <operation>, <struct>, <member> and <variant> can be tagged with attribute **deprecated**.
The value of the attribute is a string that will be included in deprecation warning messages:

If a service or operation is deprecated, the following deprecation warning is issued when calling a deprecated operation or service:

```
Operation is deprecated. <deprecated attribute string value>
```

If a struct is deprecated, the following deprecation warning will be generated into the protocol artifact:

```
WARNING: This type is deprecated. <deprecated attribute string value>
```

If a member or variant is deprecated, the following deprecation warning will be generated into the protocol artifact:

```
WARNING: This field is deprecated. <deprecated attribute string value>
```

#### Struct extensions

#### Service extensions

#### Backward compatibility

#### Deprecation support

### Protocol Specification


The protocol specification provides details to the protocols that services should use for communication,
for example, whether a service should use SOAP, XML, REST or some other protocol.
Protocol specifications are described using a SMOG specific xml syntax.

In its simplest form it only lists the names of the protocols to use as shown in the example below.

```
<?xml version="1.0" encoding="UTF-8"?>
<protocol-spec xmlns="http://namespace.jeppesen.com/smog/v2" target="some_system">
    <protocol name="soap" />
    <protocol name="plainxml" />
</protocol-spec>
```

The protocol specification above could be used for any service specification and would instruct SMOG to generate WSDL files for the “soap” protocol and XSD files for the “plainxml” protocol.
Each protocol can be further specified with more details. Certain details can be provided for different protocols.
The **target** attribute provides a logical name of the target environment the generated protocol artifacts are intended for.
It is used by SMOG to name the sub-directory where it stores the artifacts. The parent directory is determined by the **-o** parameter, see [Using SMOG](#using-smog).

##### 3.1. Supported protocols

SMOG currently supports the following protocols out of the box. It is possible to customize protocol implementations or to add new protocols as plugins.
For this purpose, the SMOG specification allows the <protocol> elements of the protocol specification to contain any attributes and child elements.
This enables flexible configuration of custom protocols.

Protocols for XML messages and SOAP:

* [plainxml](plainxml.html#plainxml)
* [soap](soap.html#soap)

Protocols for JSON messages and REST API’s:

* [plainjson](plainjson.html#plainjson)
* [openapi](openapi.html#openapi)

#### Supported protocols

### Service mapping


Service mapping provides implementation logic for a service in a specific target runtime environment, for example a Java application server or Python web server.
The service mapping can be seen as a mapping between the service specification and the data model of the environment where the service is deployed.

Mapping is made for the structs in the service and the mapping type is either **input** or **output**.
An input mapping for a struct programmatically describes what the service should do when receiving that struct as input.
The output mapping describes what the service should do when producing a specific struct for output or fault.
The picture in section [Order of execution](#order-of-execution) below describes the mapping flow, the order in which input and output mappings are executed for a service.

Service mappings are written using a SMOG xml syntax and are always made for a specific programming language, for example “Java” or “Python”.
Service mappings describe how a server or a client implements the service.

In order for a server to provide mapping for the “Flight” service below, we need to define input-mapping for structs “FlightDesignator” and “FlightSchedule”,
and output-mappings for struct “FlightInfo”. Contrary for a client, we would need to define output-mapping for struct “FlightDesignator” and
“FlightSchedule” and input-mappings for struct “FlightInfo”.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="flight">
    <services>
        <service name="Flight" version="1">
            <operation name="getFlightInfo" desc="Get information for a given flight.">
                <input type="FlightDesignator" desc="The flight to get information for."/>
                <output type="FlightInfo" desc="Information about the flight."/>
            </operation>
            <operation name="rescheduleFlight" desc="Reschedules the given flight.">
                <input type="FlightSchedule" desc="New departure and arrival times for a flight."/>
            </operation>
        </service>
    </services>

    <types>
        <struct name="FlightDesignator" desc="Information required for identifying a flight.">
            <member name="airline" type="string" desc="Airline code"/>
            <member name="number" type="int" desc="Flight number"/>
        </struct>
        <struct name="FlightInfo" desc="Information required for identifying a flight.">
            <member name="flight" type="FlightDesignator" desc="The flight this status applies to."/>
            <member name="departureAirport" type="string" desc="The departure time of this flight."/>
            <member name="arrivalAirport" type="string" desc="The arrival time of this flight."/>
        </struct>
        <struct name="FlightSchedule based_on="FlightDesignator">
            <member name="departureTime" type="dateTime"/>
            <member name="arrivalTime" type="dateTime"/>
        </struct>
    </types>
</service-spec>
```

Assuming that service “Flight ” should be deployed in a Python runtime environment that provides access to a database, we could use the following service mapping.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="flight_info_system">
    <server-impl service_name="Flight" service_version="1">
        <runtime-parameters>
            <parameter name="db_session" desc="A database session provided by the runtime environment."/>
        </runtime-parameters>
    </server-impl>
</service-mapping>
```

Assume that the same runtime environment should also provide a client, the following is needed for the client implementation:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="flight_info_system">
    <client-impl service_name="Flight" service_version="1">
        <runtime-parameters>
            <parameter name="db_session" desc="A database session provided by the runtime environment."/>
        </runtime-parameters>
    </client-impl>
</service-mapping>
```

Now assume that the client should only implement the **rescheduleFlight** operation, thus the getFlightInfo operation is not relevant for the client
and therefore the input mapping for structs “FlightInfo” and “Error” and the output mapping for “FlightDesignator” are not required. In order to hint
SMOG about this, the attribute **operations** can be added as shown below:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="flight_info_system">
    <client-impl service_name="Flight" service_version="1" operations="rescheduleFlight">
        <runtime-parameters>
            <parameter name="db_session" desc="A database session provided by the runtime environment."/>
        </runtime-parameters>
    </client-impl>
</service-mapping>
```

The **operations** attribute is available both on <server-impl> and <client-impl> elements. More than one operation can be specified by providing a
comma separated list. If specified, the service contract and service implementation artifacts produced by SMOG will only be based on the specified
operation(s) and the structs that are associated with them. Hence, SMOG will also suppress validation of any service mapping provided for any other
structs.

The namespace given in the root <service-mapping> element specifies the SMOG syntax version used. The root element also has the following attributes:

* **language**: Specifies the programming language used in the service implementation.
* **target**: Provides a logical name of the target environment the mapping is intended for. It specifies the name of the sub-directory where the generated mapping artifact is stored.
  If ommitted, it defaults to the **target** given in the protocol specification. The parent directory is determined by the **-g** parameter, see [Using SMOG](#using-smog).

The <server-impl> element states that this mapping is a server implementation of the service. The <runtime-parameters> lists the parameters provided by the runtime environment. Such parameters become available to use in mapping.

Just like with service specifications it also possible to import other mapping modules using the <include> element:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python">
    <include href="$CARMSYS/data/config.flight_mapping.xml"/>
    <include href="custom_input_mapping.xml"/>
    <include href="custom_output_mapping.xml"/>
</service-mapping>
```

Included modules may in their turn contain <include> element. Note that the **target** attribute of included mapping modules (if specified) have no effect.
It is only the **target** specified in the “root” mapping that is significant.

##### 4.1. Input mapping

Input mappings are defined using the <input-mapping> element. The struct attribute identifies which struct the mapping applies to, i.e. what should the server do when receiving that struct as input. An <input-mapping> element can contain the following sub elements:

* <import> - import a module for use in subsequent mappings.
* <assign> - assign a value to a variable for use in mapping of this struct and in mappings of child structs.
* <condition> - omit the mapping of this struct if the specified condition is not fulfilled.
* <call> - call a function before iterating child struct mappings.
* <assign-last> - same as <assign> but evaluated after iterating child structs (new in SMOG v2).
* <call-last> - call a function after iterating child struct mappings.

A <condition> applied directly on <input-mapping> or <output-mapping> is also called struct level condition.
Sub elements <assign>, <assign-last>, <call> and <call-last> can also have a <condition> element for omitting the use of that part if the specified condition is not fulfilled.

```
<input-mapping struct="flight.FlightDesignator">
    <import name="flight.service.helper" alias="helper"/>
    <assign name="flight_record" expr="db_session.find_flight(@{struct}.airline, @{struct}.number)"/>
    <call name="flight_not_found" expr="helper.raise_exception('No such flight.')">
        <condition expr="flight_record is None"/>
    </call>
    <call name="cancel_flight" expr="helper.cancel_flight(db_session, flight_record)">
        <condition expr="@{service}.operation_name == 'cancelFlight'"/>
    </call>
</input-mapping>
```

The example input mapping above is for struct “FlightDesignator” and uses <import> for importing a Python module, making that module available
with the name “helper” in subsequent Python expressions. The <assign> element declares a new variable called “flight\_record” which gets a value by
calling a Python expression. The name “db\_session” used in the expression is provided from the runtime environment. Variables defined using <assign>
can be used in expressions within the same mapping and for mappings of child structs (but not the other way around). Variables defined using <assign>
in the <input-mapping> of the operations input struct are also available to use in the <output-mapping> of the operations output struct.
Conversely for <client-impl> mapping, variables defined in <output-mapping> are however not available to use in the <input-mapping>.

The syntax **@{struct}** is used for getting the values for members “airline” and “number” of the “FlightDesignator” struct, i.e. the actual values provided in the service call.
There are two <call> elements, the first one uses the imported “helper” for throwing an exception if no flight record was found.
The other <call> element calls a function that cancels the flight, but only if the operation is “cancelFlight”.
The special token **@{struct}.instance\_name** can be used in the mapping to access the name of the context node, i.e. the currently processed struct instance in the input message.
For example in case of **plainxml** or **soap** protocols that means the element name.
The token **@{struct}.is\_null(name)** can be used in the mapping to check whether a member or variant with specified name is a null value.
The syntax **@{service}** is used for getting or assigning service variables. A service variable can be thought of as an instance variable of the service.
Chapter [Python API](#python-api) lists the predefined service variables provided by SMOG. In addition to these it is possible to define and use any
service variable in the mapping (both <input-mapping> and <output-mapping>).

##### 4.2. Output mapping

Output mappings are defined using the <output-mapping> element. The struct attribute identifies which struct the mapping applies to, i.e. what the application should do when producing this struct for output. An <output-mapping> element can contain the following sub elements:

* <import> - import a module for use in subsequent mappings.
* <assign> - declare a variable for use in mapping of this struct and in mappings of child structs.
* <condition> - omit the mapping of this struct if the specified condition is not fulfilled.
* <call> - call a function before iterating child struct mappings.
* <out> - sets the value of a member or variant of this struct.
* <assign-last> - same as <assign> but evaluated after iterating child structs (new in SMOG v2).
* <call-last> - call a function after iterating child struct mappings.

A <condition> applied directly on <input-mapping> or <output-mapping> is also called struct level condition.
In <output-mapping>, nullable members and variants of complex types are set to null when struct level conditions of structs are not fulfilled.
Sub elements <assign>, <assign-last>, <out>, <call> and <call-last> can also have a <condition> element for omitting the use of that part if the specified condition is not fulfilled.

The example output mapping below is for struct “FlightStatus” and uses <out> for setting the values of the members. Values are received by calling a Python expression using the variable “flight\_record” defined in the <input-mapping>.

```
<output-mapping struct="flight.FlightStatus">
    <out member_or_variant="departureTime" expr="flight_record.get_departure_time()" />
    <out member_or_variant="arrivalTime" expr="flight_record.get_arrival_time()" />
    <out member_or_variant="scheduleStatus" expr="flight_record.get_schedule_status()" />
</output-mapping>
```

If the member or variant is of multi-value type then attribute **iter** is used instead of **expr** in the <out> element. Assume a struct “CreatureDetails” defined as:

```
<struct name="CreatureDetails" desc="Information about a creature">
    <variant name="humanAddress" type="HumanAddressDetails[0:]" />
    <variant name="alienAddress" type="AlienAddressDetails[0:]" />
    <member name="phone" type="string[0:]" />
    <member name="spaceship" type="Spaceship[0:1]"/>
</struct>

<struct name="HumanAddressDetails">
    <member name="street" type="string"/>
    <member name="city" type="string"/>
</struct>

<struct name="AlienAddressDetails">
    <member name="planet" type="string"/>
    <member name="galaxy" type="string"/>
    <member name="universe" type="string"/>
</struct>

<struct name="Spaceship">
    <member name="model" type="string[0:1]"/>
    <member name="regNo" type="string"/>
</struct>
```

Then the <out> elements for the multi-value members and variants need to specify the **iter** attribute:

```
<output-mapping struct="space.CreatureDetails">
    <out member_or_variant="humanAddress" iter="db_result.get_addresses(creature.id, human=True)" variable_name="address_obj"/>
    <out member_or_variant="alienAddress" iter="db_result.get_addresses(creature.id, human=False)" variable_name="address_obj"/>
    <out member_or_variant="phone" iter="db_result.get_phone_numbers(creature.id)" />
</output-mapping>

<output-mapping struct="space.HumanAddressDetails">
    <out member_or_variant="street" expr="address_obj.get_street()"/>
    <out member_or_variant="city" expr="address_obj.get_city()"/>
</output>

<output-mapping struct="space.AlienAddressDetails">
    <out member_or_variant="planet" expr="address_obj.get_planet()"/>
    <out member_or_variant="galaxy" expr="address_obj.get_galaxy()"/>
    <out member_or_variant="universe" expr="'the one and only'"/>
</output>
```

Note that for the members or variants that are of complex (struct) types, the additional **variable\_name** attribute is needed.
The variable\_name defines the variable in which each address instance is available to the child struct mappings.

The variable\_name attribute is also mandatory for a non multi-value complex member or variant if the **expr** attribute is specified:

```
<output-mapping struct="space.CreatureDetails">
    <out member_or_variant="spaceship" expr="spaceships.get_ship_for_creature(creature.id)" variable_name="ship"/>
</output-mapping>

<output-mapping struct="space.Spaceship">
    <out member_or_variant="model" expr="ship.model"/>
    <out member_or_variant="regNo" expr="ship.regno"/>
</output-mapping>
```

Note however that if **expr** is not specified in this case, then variable\_name is not needed:

```
<output-mapping struct="space.CreatureDetails">
    <out member_or_variant="spaceship" />
</output-mapping>

<output-mapping struct="space.Spaceship">
    <assign name="ship" expr="spaceships.get_ship_for_creature(creature.id)" />
    <out member_or_variant="model" expr="ship.model"/>
    <out member_or_variant="regNo" expr="ship.regno"/>
</output-mapping>
```

In fact, for **required** non multi-value complex members or variants the entire <out> element is not needed as illustrated in the following example
in which struct “MobileCreatureDetails” redefines “spaceship” to be a required member (note that the cardinality “[0:1]” has been removed from the type):

```
<struct name="MobileCreatureDetails" based_on="CreatureDetails">
    <member name="spaceship" type="Spaceship"/>
</struct>
```

Output mapping for struct “MobileCreatureDetails” wouldn’t need the <out member\_or\_variant=”spaceship”/>. Only the output mapping for the “Spaceship”
struct itself is needed.

In fact, SMOG does not enforce output mapping to be specified for any structs used in output, leaving the possibility to build output structs
programmatically using the generated service implementation, see [Generated service implementations](#generated-service-implementations).

##### 4.3. Mapping extensions

As we saw in the beginnig of this chapter, a service mapping can combine several mapping modules by means of the <include> element. Several modules
can even contribute to the mapping for one and the same struct as shown in the following examples.

Regard the following extension module for a service specification:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="my_extensions">
    <include href="common_structs.xml" />

    <types>
        <struct-update struct="common.Person">
            <add-member name="birthdate" type="date" desc="The birthday of this person."/>
        </struct-update>
    </types>
</service-spec>
```

The mapping for the “Person” struct could be combined from two different sources such that the mapping for members defined in the “common” module are
separated from the mapping of the extended members. Assume the following mapping module is stored as file “base\_mappings.xml”:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="air2">
    <output-mapping struct="common.Person">
        <out member_or_variant="firstName" expr="crew.FirstName"/>
        <out member_or_variant="lastName" expr="crew.Surname"/>
    </output-mapping>
</service-mapping>
```

Then the resulting mapping for the extended struct could be specified as:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="air2">
    <include href="base_mappings.xml"/>

    <output-mapping struct="common.Person">
        <out member_or_variant="birthdate" expr="crew.birthdate"/>
    </output-mapping>
</service-mapping>
```

The next example shows how multiple mapping contributions can be used when a struct has been extended by means of inheritance.
Regard the following extension module for a service specification:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="my_extensions">
    <include href="common_structs.xml" />

    <types>
        <struct name="Employee" based_on="Person" desc="Information about an employee.">
           <member name="employmentDate" type="date" desc="Date of employment."/>
        </struct>
    </types>
</service-spec>
```

Then, assuming the same “base\_mappings.xml” as above, the resulting mapping for the new struct “Employee” could be specified as follows.
Note that the output mapping for “Employee” not only defines the mapping for the extra member “employmentDate” but also redefines
the mapping for member “firstName”:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="air2">
    <include href="base_mappings.xml"/>

    <output-mapping struct="my_extensions.Employee">
        <out member_or_variant="firstName" expr="crew.FirstName + ' ' + crew.MiddleName"/>
        <out member_or_variant="graduationYear" expr="crew.Birthdate"/>
    </output-mapping>
</service-mapping>
```

The principles for combining mapping contributions as outlined in this section apply not only to <out> but to all other types of mapping elements as well
(<import>, <assign>, <condition> etc.), both for <input-mapping> and <output-mapping>. The resulting mapping is made up by applying each contribution in document order.
In case any of the mappings in such a hierarchy of contributions contains more than one mapping element with the same name,
the elements are matched starting from the lowest index and any overshooting instances (number of child/parent instances differ) are applied last (among elements of the same type), as illustrated below:

```
<output-mapping struct="MyStruct">
    <assign name="myVar" expr="1" />
    <out member_or_variant="outcome" expr="myVar" />
</output-mapping>

<output-mapping struct="MyStruct">
    <assign name="myVar" expr="3" />
    <assign name="myVar" expr="myVar + 1" />
</output-mapping>
```

Hence, “outcome” would yield “4” in the resulting output mapping for “MyStruct” because:

* The two mapping contributions for “MyStruct” are applied in document order, and therefore
* the “<assign name=’myVar’ expr=‘3’ />” will match (and thus redefine/replace) “<assign name=’myVar’ expr=‘1’ />”, and
* the overshooting “<assign name=’myVar’ expr=’myVar + 1’ />” will be applied last of the <assign>’s

For mapping elements where the “name” attribute is optional, elements are only redefined if the “name” attribute is specified.
This applies to mapping element types <call> and <call-last>, and is illustrated in the next example:

```
<output-mapping struct="MyStruct">
    <call name="init" expr="helper.init()" />
    <call expr="helper.do_it()" />
</output-mapping>

<output-mapping struct="MyStruct">
    <call name="init" expr="helper.reset()" />
    <call expr="helper.do_this_too()" />
</output-mapping>
```

Hence, the execution of <call>’s in the resulting output mapping for “MyStruct” would be:

1. helper.reset()
2. helper.do\_it()
3. helper.do\_this\_too()

###### 4.3.1. Extensions and overrides to <server-impl> and <client-impl>

In the same way as described for <input-mapping> and <output-mapping> above, inheritance and overloading can also be applied to
the <server-impl> and <client-impl> sections in the service mapping:

Assume the following mapping module is stored as “base\_mappings.xml” (details left out for clarity):

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="flight_info_system">
    <client-impl service_name="Flight" service_version="1" operations="rescheduleFlight">
        <runtime-parameters>
            <parameter name="db_session" desc="A database session provided by the runtime environment."/>
        </runtime-parameters>
    </client-impl>

    <output-mapping struct="common.FlightSchedule">
        :
    </output-mapping>
</service-mapping>
```

Then, it is possible to customize the client implementation as illustrated below:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="flight_info_system">
    <include href="base_mappings.xml"/>

    <client-impl service_name="Flight" service_version="1" operations="rescheduleFlight, cancelFlight"/>

    <output-mapping struct="common.FlightCancellationData">
        :
    </output-mapping>
</service-mapping>
```

Note that in the custom version of the client, the **operations** attribute is redefined such that the client now also contains
an implementation of the **cancelFlight** operation.

It is also possible to customize the **runtime parameters** of an implementation as illustrated in the next snippet where
a new parameter *logger* has been introduced:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="flight_info_system">
    <include href="base_mappings.xml"/>

    <client-impl service_name="Flight" service_version="1" operations="rescheduleFlight, cancelFlight">
        <runtime-parameters>
            <parameter name="db_session" desc="A database session provided by the runtime environment."/>
            <parameter name="logger" desc="Global logger instance"/>
        </runtime-parameters>
    </client-impl>

    <output-mapping struct="common.FlightCancellationData">
        :
    </output-mapping>
</service-mapping>
```

Note that when overriding runtime parameters in this way, the <runtime-parameters> section must be specified as a whole, i.e. in the
above example both *db\_session* and *logger* must be included (i.e. if the intention is to keep the original *db\_session* parameter).

Within the <server-impl> and <client-impl> sections it is also possible to customize pre- and post-processors in the same fashion
(see [Pre- and post processing](#pre-post-processing)).

##### 4.4. Order of execution

The execution order of struct mappings are based on the service specification.
The execution of the input mapping is driven by the structure and contents of the input message. It starts on the top level with the struct defined as input type of the operation.
Input mappings of child structs are executed based on the order they appear in the service specification, recursing downwards for all struct members.

![../_images/execution_order.png](../_images/execution_order.png)

Operations within each input-mapping are executed in the following order:

1. Import modules for all <import> elements (imports for all <input-mappings> and <output-mappings> happens globally when the execution is initiated)
2. Evaluate all <assign> elements in the order they appear in the <input-mapping>.
3. Evaluate the struct level <condition> element (if any) and abort execution if it returns false.
4. Evaluate all <call> elements in the order they appear in the <input-mapping>.
5. Execute <input-mapping> for the variant of the struct (only one of the variants can have a value). If the variant is a struct, execute the <input-mapping> for that struct.
6. Execute <input-mapping> for each struct member in the order they appear in the <struct>. If the member is a struct, execute the <input-mapping> for that struct.
7. Evaluate all <assign-last> elements in the order they appear in the <input-mapping>.
8. Evaluate all <call-last> elements in the order they appear in the <input-mapping>.

Operations within each output-mapping are executed in the following order:

1. Import modules for all <import> elements (imports for all <input-mappings> and <output-mappings> happens globally when the execution is initiated)
2. Evaluate all <assign> elements in the order they appear in the <output-mapping>.
3. Evaluate the <condition> element (if any) and abort execution if it returns false.
4. Evaluate all <call> elements in the order they appear in the <output-mapping>.
5. Execute <out> for each variant in the order they appear in the <struct>. Stop on the first variant with a <condition> that evaluates to true and skip the other variants. If the variant is a struct, execute the <output-mapping> for that struct.
6. Execute <out> for each members in the order they appear in the <struct>. If the member is a struct, execute the <output-mapping> for that struct.
7. Evaluate all <assign-last> elements in the order they appear in the <output-mapping>.
8. Evaluate all <call-last> elements in the order they appear in the <output-mapping>.

##### 4.5. Pre- and post processing

In SMOG it is possible to plugin code to be executed before input mapping is executed (pre-process) and/or after output mapping is executed (post-process).
Several pre- and post-processing steps can be chained together and will then be executed after eachother such that the output from one step becomes
the input to the next. Pre-process steps are invoked when calling methods “handle” and “fault” on the service class, or “handle\_response” in case of a client.
See [Python API](#python-api) for more information about the public methods.
Pre-processors are also invoked if “operation\_<operation-name>” or “handle\_<operation-name>\_response” are called directly (bypassing the “handle”/”handle\_response” methods).
Post-process steps can specify an optional operation such that it will only be executed after the given operation.

Consider the following service mapping module stored as “hotel\_mapping\_base.xml”:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns="http://namespace.jeppesen.com/smog/v2" language="Python" target="air2">

  <server-impl service_name="TripHotel" service_version="1">
      <runtime-parameters>
          <parameter name="planholder" />
          <parameter name="service_context" />
      </runtime-parameters>
      <pre-process name="api_request" module="std_interfaces.api_hotels" function="HotelHandler.from_pairing_request"/>
      <post-process name="api_export_pairings" module="std_interfaces.api_hotels" function="HotelHandler.to_load_trips" operation="exportTrips"/>
      <post-process name="api_export_rosters" module="std_interfaces.api_hotels" function="HotelHandler.to_update_trips" operation="exportRosters"/>
  </server-impl>

</service-mapping>
```

SMOG calls the pre- and post-processing functions with the service instance as the first parameter.
The rest of the signature is identical to that of the “handle” method of the service class, see [Python API](#python-api) (or, for a client implementation the “make\_<operation>\_request” and handle\_<operation>\_response” methods).
The Python code below shows in principle how the plugin code in python module “std\_interfaces/api\_hotels.py” could be implemented:

```
class HotelHandler(BaseInterfaceHandler):

    @classmethod
    def from_pairing_request(cls, service, request_payload, request_headers, planholder, service_context):
        """
        Pre-processing step to transform "Request-Pairing-Refresh" request messages
        """
        xsl_path = cls.get_path("from_pairing_request.xsl")
        return cls._xslt_transform(xsl_path, request_payload)

    @classmethod
    def to_load_pairings(cls, service, response_payload, request_headers, planholder, service_context):
        """
        Post-processing step to transform messages on format TripHotel_version1.xsd to ACES Load-Pairings.xsd
        """
        xsl_path = cls.get_path("to_api_hotels_pairings.xsl")
        service.response_headers.update({'JMSType': 'Load-Pairings'})
        return cls._xslt_transform(xsl_path, response_payload, transaction="load")

    @classmethod
    def to_update_pairings(cls, service, response_payload, request_headers, planholder, service_context):
        """
        Post-processing step to transform messages on format TripHotel_version1.xsd to ACES Update-Pairings.xsd
        """
        ext_schema_path = cls.get_path("Update-Pairings.xsd")
        xsl_path = cls.get_path("to_api_hotels_pairings.xsl")
        service.response_headers.update({'JMSType': 'Update-Pairings'})
        return cls._xslt_transform(xsl_path, response_payload, transaction="update")
```

Pre- and post-processing steps can be extended/redefined in the same way as other mapping elements, following the same principles as described in [Mapping extensions](#mapping-extensions):
The following mapping shows how e.g. the pre-processing step of the “TripHotel” service could be customized:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns="http://namespace.jeppesen.com/smog/v2" language="Python" target="air2">
  <include href="hotel_mapping_base.xml"/>

  <server-impl service_name="TripHotel" service_version="1">
      <pre-process name="api_request" module="api_hotels_extensions" function="custom_pairing_request"/>
  </server-impl>

</service-mapping>
```

The custom redefined pre-processor named “api\_request” could be implemented e.g. as follows in python module “api\_hotels\_extensions.py”:

```
def custom_pairing_request(cls, service, request_payload, request_headers, planholder, service_context):
    # In the custom version of the pre-processing no transform is needed, just log the request
    logger.info(request_payload)
    return request_payload
```

In the previous example a pre-processor was used for transforming some external format into the protocol configured for the service.
A slightly different use case is for the pre-processor to parse directly from an external format to the protocol independent “internal” SMOG format.
Chapter [Generated service implementations](#id3) explains that the generated service class contains class representations for all structs used by the service.
The following shows an example where the pre-processor passes an internal `SmogStruct` instance to the input mapping. Assume the following service specification:

```
<?xml version="1.0" encoding="UTF-8"?>
<service-spec xmlns="http://namespace.jeppesen.com/smog/v2" name="flight_input">
    <services>
        <service name="FlightInput" version="1">
            <operation name="createFlight">
                <input type="FlightMsg"/>
            </operation>
        </service>
    </services>

    <types>
        <struct name="FlightMsg">
            <member name="source" type="string" desc="Message source" />
            <member name="version" type="string" desc="Message version" />
            <member name="flight" type="Flight" desc="The flight this status applies to."/>
        </struct>
        <struct name="Flight" desc="Information about the flight to create.">
            <member name="airline" type="string" desc="Airline code"/>
            <member name="flightNumber" type="int" desc="Flight number"/>
            <member name="dateOfOrigin" type="date" desc="Flight date"/>
        </struct>
    </types>
</service-spec>
```

and the service mapping would look something like this (<input-mapping> sections excluded for clarity):

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language="Python" target="flight_info_system">
    <server-impl service_name="FlightInput" service_version="1">
        <runtime-parameters>
            <parameter name="db_session" desc="A database session provided by the runtime environment."/>
        </runtime-parameters>
        <pre-process name="from_iata_asm" module="std_interfaces_parsers.iata" function="parse_asm" />
    </server-impl>

</service-mapping>
```

The code below outlines how the pre-processor named “from\_iata\_asm” could be implemented in python module “std\_interfaces\_parsers/iata.py”:

```
def parse_asm(service, request_payload, request_headers, db_session):
    parser = ASMParser()
    asm_msg = parser.parse(request_payload)
    smog_struct = service.create_struct_createFlight({'source': 'ASM', 'version': '1')
    smog_struct.flight = service.Flight({'airline': asm_msg.carrier, 'flightNumber': asm_msg.num, 'dateOfOrigin': asm_msg.dor})

    return smog_struct
```

Notice how `SmogStruct` instances are created using the public interface of the SMOG generated service class.
See chapter [Generated service implementations](#id3) and sub-sections for more info.

The exmple below illustrates how pre- and post-processing can be applied to a **client implementation**. Note that for a “trigger” type of client,
that only produces request messages, only post-processing steps are relevant.

```
<?xml version="1.0" encoding="UTF-8"?>
<service-mapping xmlns="http://namespace.jeppesen.com/smog/v2" language="Python" target="air2">

    <client-impl service_name="TripHotel" service_version="1">
        <runtime-parameters>
            <parameter name="plan" desc="Plan instance from IOServer."/>
            <parameter name="ravesession" desc="Rave session from IOServer."/>
            <parameter name="changeset" desc="Mave changeset from IOServer."/>
            <parameter name="service_logger" desc="Logger instance from IOServer."/>
            <parameter name="now_time" desc="Current time according to the runtime environment."/>
         </runtime-parameters>
         <post-process name="api_transactions" module="std_interfaces.api_hotels_1" function="HotelEventHandler.to_api_transaction" operation="updateTrips"/>
    </client-impl>

</service-mapping>
```

The post-processing step above could be implemented in python module “std\_interfaces/api\_hotels.py” as follows:

```
class HotelEventHandler(BaseInterfaceHandler):

    @classmethod
    def to_api_transaction(cls, client, request_payload, request_headers, plan, ravesession, changeset, service_logger, now_time):
        """
        Post-processing step to transform messages on format TripEventOutput_version1.xsd to ACES formats
        """
        xsl_path = cls.get_path("to_api_hotels_pairings.xsl")
        tree = etree.fromstring(request_payload)
        payload_list = []
        headers_list = []

        # Handle addTrip
        ext_schema_path = cls.get_path("Add-Pairing.xsd")
        for trip_elem in tree.xpath("/jct:updateTripsRequest/jct:addTrip", namespaces=nsmap):
            msg, props = cls._transform_trip_elem(xsl_path, ext_schema_path, trip_elem, request_headers)
            props['JMSType'] = 'Add-Pairing'
            payload_list.append(msg)
            headers_list.append(props)

        # Handle updateTrip
        ext_schema_path = cls.get_path("Revise-Pairing.xsd")
        for trip_elem in tree.xpath("/jct:updateTripsRequest/jct:updateTrip", namespaces=nsmap):
            msg, props = cls._transform_trip_elem(xsl_path, ext_schema_path, trip_elem, request_headers)
            props['JMSType'] = 'Revise-Pairing'
            payload_list.append(msg)
            headers_list.append(props)

        client.request_headers = headers_list
        return payload_list
```

The above example also illustrates that a post-processing step may return a list of payloads i.e. **splitting** the original payload into several messages.
If several post-processing steps are chained together, the multiplicity must of course be taken into account when payload is passed on between steps -
a post-processing step must be able to handle a list of payloads as input in case the preceding step returns a list of payloads.

The attribute `process_struct="true"` can be set on the first `<post-process>` element in `<server-impl>` or `<client-impl>` (only SMOG version 2).
SMOG passes the output SMOG struct instance as `request_payload`/`response_payload` to the post processor, instead of passing the payload formatted on the protocol being used.
This is useful in situations where it’s easier to format the SMOG struct to the target format rather than a formatted payload.

Both pre- and post-processors may return None to indicate that they leave the payload unchanged. This is equivalent to returning the input payload of the processor.

#### Input mapping

#### Output mapping

#### Mapping extensions

##### Extensions and overrides to <server-impl> and <client-impl>

#### Order of execution

#### Pre- and post processing

### Using SMOG


Smog is run from the command line, the usage is:

```
smog [options] -s filename
```

Filename is the name of the required service specification. More options can be specified for providing a protocol specification and optionally a service mapping.

|  |  |
| --- | --- |
| `-h, --help` | Show this help message and exit |
| `-p` | Path to protocol specification file that specifies the protocol artifacts to generate. |
| `-m` | Path to service mapping file that specifies the service implementation artifacts to generate. |
| `-o` | Output directory for service contracts artifacts. Default: “.” |
| `-g` | Output directory for service implementation artifacts. Default: “.” |
| `-c` | Custom protocol package. Python package containing custom protocol implementation. |
| `-d` | Custom language package. Python package containing custom language implementation. |
| `-n` | Optional service name (case sensitive) to filter the services specified in the service specification. If not specified, protocol and mapping artifacts are generated for all services in the given service specification. |
| `-v` | Optional service version to filter the services specified in the service specification. |
| `-e` | Optional comma-separated list of protocols (case sensitive) to override the protocols specified in protocol specification. |
| `-j` | Print service service specification and information about built artifacts on json format on stdout |

##### 5.1. Generated service implementations

SMOG uses the service mapping for generating deployable service mapping artifacts for server and client implementations.
The artifacts are generated as source code for service classes with public methods to use by the calling framework in the runtime environment where the service is deployed.
The source code for the service class is generated for the language specified in the service mapping, e.g. Python, Java etc.
The mapping artifacts contain one service class for each protocol in the protocol specification.

###### 5.1.1. Python

Python service classes are generated in a Python module named `<service-name>_<service-version>_server|client.py` .
One service class is generated for each protocol that the service supports and is named using pattern `Service<service-name>_<protocol>` and `Client<service-name>_<protocol>` for server and client implementations respectively.
The generated Python module also contains class representations for all structs used by the service.
The struct classes inherit from the static `SmogStruct` class and provides a simple way for programmatically working with input and output messages.

**Example deployment**

The example below demonstrates how the “Flight” service is deployed to run in flask web server.

```
"""
Simple web server deploying the "Flight" service for using the SOAP protocol.
"""

from flask import Flask, Response, request

#### import the generated Python module
import flight_info_system.Flight_1_server as service_module

app = Flask(__name__)

db_session = None # A fictive database session provided
                  # by the environment where this application is deployed.

@app.route('/services/Flight', methods=['POST'])
def service_flight():
    # create an instance of the service class for SOAP protocol
    service = service_module.ServiceFlight_soap()
    try:
        # Let the service handle the request and pass the database session as a runtime paramter.
        service.handle(request_payload=request.data, request_headers=request.headers, db_session)
        status = 200
    except Exception as e:
        # Let the service handle the fault for producing a fault response.
        service.fault(request_payload=request.data, request_headers=request.headers, db_session)
        status = 500
    # send response back to the client
    return Response(service.response_payload, mimetype='text/xml', status=status)
```

###### 5.1.2. Python API

####### 5.1.2.1. Service Variables

Generated service classes provides the following service variables (public members):

> `request_payload`: The request payload, unparsed, currently being handled.
>
> > type: `str`
>
> `request_headers`: Dictionary containing message headers of request currently being handled.
>
> > type: `dict`
>
> `response_payload`: The response payload, set when output mapping is complete.
>
> > type: `str or list of str`
>
> `response_headers`: Dictionary containing message headers of response, set when output mapping is complete.
>
> > type: `dict or list of dict`
>
> `parsed_struct`: Instance representation of request being handled.
>
> > type: `SmogStruct`
>
> `operation_name`: Name of the operation currently being handled.
>
> > type: `str`
>
> `result`: A result code set when the operation is complete. A default result code can be specified for an operation by specifying attribute **default\_result** with value “SAVE” or “UNCHANGED” on the <operation> element in the service specification.
>
> > type: `str`
>
> `exception`: The exception that was raised.
>
> > type: `Exception or None`
>
> `traceback`: Traceback of exception that was raised.
>
> > type: `Traceback or None`
>
> `fault_payloads`: Input message payload(s) in case of a fault. This information is collected when the ‘fault’ method of the service/client is called. If pre-processors are used, the intermetiate payload between each processor that changes the payload is also collected, and formatted if in SmogStruct format.
>
> > type: `list of str`

The service variables can be accessed from within the service mapping as e.g. **@{service}.operation\_name**.

####### 5.1.2.2. Methods in server implementation classes

Service classes provide the following public methods to be used by the calling framework when deploying and testing the service implementation.

* `handle(request_payload, request_headers, <runtime-parameters>)`

  Main method for handling an incoming request messages to the service. It first analyzes the given payload and tries to figure out the operation of the payload, and then calls the corresponding handle method for operation currently being handled.

  > `request_payload` `str` or `SmogStruct`: The request message, either the “raw” message body formatted according to the protocol of the service class (e.g. an xml message for the “plainxml” protocol), or an instance of the SmogStruct subclass that represents the input type of the operation.
  >
  > `request_headers` `dict`: Dictionary of headers passed with the incoming request message.
  >
  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <server-impl> element.

  return: `None`

  raises: Any exception raised during handling of the given request payload.
* `fault(request_payload, request_headers, exception, <runtime-parameters>)`

  Main method for handling errors raised outside of this handler. It is called by the runtime environment hosting the service, in order to generate an error message.
  Calls the corresponding fault method for operation currently being handled.

  > `request_payload` `str`: The request body.
  >
  > `request_headers` `dict`: Dictionary of headers passed with the incoming request message.
  >
  > `exception` `Exception`: Exception to generate error message for.
  >
  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <server-impl> element.

  return: `None`
* `operation_<operation-name>(request_payload, request_headers, <runtime-parameters>)`

  Method for handling an incoming request messages for a specific operation.

  > `request_payload` `str` or `SmogStruct`: The request message, either the “raw” message body formatted according to the protocol of the service class, or an instance of the SmogStruct subclass that represents the input type of the operation.
  >
  > `request_headers` `dict`: Dictionary of headers passed with the incoming request message.
  >
  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <server-impl> element.

  return: `None`

  raises: Any exception raised during handling of the given request payload.
* `fault_<operation-name>(request_payload, request_headers, exception, <runtime-parameters>)`

  Method for generating an fault message for a specific operation.

  > `request_payload` `str`: The request body.
  >
  > `request_headers` `dict`: Dictionary of headers passed with the incoming request message.
  >
  > `exception` `Exception`: Exception to generate error message for.
  >
  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <server-impl> element.

  return: `None`
* `pre_process(payload)`

  This is the main method for translating an incoming message. Any pre-processing steps (if specified) are executed first,
  then the resulting payload is parsed into a SmogStruct representation (if not already done by the pre-processing) by calling
  the `parse(payload)` method (see below).
  If called in the context of error handling (i.e. when the `exception` property is set), it collects intermediate results
  from each pre-processor that changes the payload. This can be used when generating error messages (see also service variable
  ‘fault\_payloads’).

  > `payload` `str`: The payload to parse.

  return: tuple of (`SmogStruct`, str or `SmogStruct`)

  raises: `ValueError` If the payload cannot be used for creating a valid struct instance.
* `parse(payload)`

  Parses given payload and returns a struct instance populated with the values of the payload. The payload should be on the protocol associated with this service class.

  > `payload` `str`: The payload to parse.

  return: `SmogStruct`

  raises: `ParseMsgError` If the payload cannot be used for creating a valid struct instance.
* `format(struct, validate=True)`

  Formats the given struct for the protocol used by this service class.

  > `struct` `SmogStruct`: The struct instance to format.
  >
  > `validate` `bool`: Whether the struct should be validated before being formatted.

  return: `str`

  raises: `ValueError` If the given struct cannot be formated on the protocol for this service class.
* `format_fault(struct, validate=True)`

  Formats the given struct as a fault for the protocol used by this service class.

  > `struct` `SmogStruct`: The struct instance to format.
  >
  > `validate` `bool`: Whether the struct should be validated before being formatted.

  return: `str`

  raises: `ValueError` If the given struct cannot be formated on the protocol for this service class.
* `create_struct_<operation-name>(*args, **kwargs)`

  Creates SmogStruct instance that can be used as input for a specific operation.

  return: `SmogStruct`

####### 5.1.2.3. Methods in client implementation classes

Client classes provide the following public methods to be used by the calling framework when deploying and testing the service implementation.

* `make_<operation-name>_request(<runtime-parameters>)`

  Method for producing request messages for a specific operation. The formatted result is stored in service variable request\_payload.

  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <client-impl> element.

  return: `None`

  raises: Any exception raised during execution of the output mapping.
* `handle_response(response_payload, response_headers, <runtime-parameters>)`

  Main method for handling incoming response messages from a server. It first analyzes the given payload and tries to figure out the operation of the payload, and then calls the corresponding handle method for operation currently being handled.

  > `response_payload` `str` or `SmogStruct`: The response message, either the “raw” message body formatted according to the protocol of the client class (e.g. an xml message for the “plainxml” protocol), or an instance of the SmogStruct subclass that represents the input type of the operation.
  >
  > `response_headers` `dict`: Dictionary of headers passed with the incoming response message.
  >
  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <client-impl> element.

  return: `None`

  raises: Any exception raised during handling of the given response payload.
* `handle_<operation-name>_response(response_payload, response_headers, <runtime-parameters>)`

  Method for handling an incoming response messages for a specific operation.

  > `response_payload` `str` or `SmogStruct`: The response message, either the “raw” message body formatted according to the protocol of the client class, or an instance of the SmogStruct subclass that represents the input type of the operation.
  >
  > `response_headers` `dict`: Dictionary of headers passed with the incoming response message.
  >
  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <client-impl> element.

  return: `None`

  raises: Any exception raised during handling of the given response payload.
* `fault(response_payload, response_headers, exception, <runtime-parameters>)`

  Main method for handling errors raised outside of this handler. It is called by the runtime environment hosting the client, in order to generate an error message.
  Calls the corresponding fault method for operation currently being handled.

  > `response_payload` `str`: The response body.
  >
  > `response_headers` `dict`: Dictionary of headers passed with the incoming response message.
  >
  > `exception` `Exception`: Exception to generate error message for.
  >
  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <client-impl> element.

  return: `None`
* `fault_<operation-name>(response_payload, response_headers, exception, <runtime-parameters>)`

  Method for generating an fault message for a specific operation.

  > `response_payload` `str`: The request body.
  >
  > `response_headers` `dict`: Dictionary of headers passed with the incoming response message.
  >
  > `exception` `Exception`: Exception to generate error message for.
  >
  > `<runtime-parameters>`: `*args`: Parameters specified in the <runtime-parameters> in the <client-impl> element.

  return: `None`
* `pre_process(payload)`

  This is the main method for translating an incoming message. Any pre-processing steps (if specified) are executed first,
  then the resulting payload is parsed into a SmogStruct representation (if not already done by the pre-processing) by calling
  the `parse(payload)` method (see below).
  If called in the context of error handling (i.e. when the `exception` property is set), it collects intermediate results
  from each pre-processor that changes the payload. This can be used when generating error messages (see also service variable
  ‘fault\_payloads’).

  > `payload` `str`: The payload to parse.

  return: tuple of (`SmogStruct`, str or `SmogStruct`)

  raises: `ValueError` If the payload cannot be used for creating a valid struct instance.
* `parse(payload)`

  Parses given payload and returns a struct instance populated with the values of the payload. The payload should be on the protocol associated with this client class.

  > `payload` `str`: The payload to parse.

  return: `SmogStruct`

  raises: `ParseMsgError` If the payload cannot be used for creating a valid struct instance.
* `format(struct, validate=True)`

  Formats the given struct for the protocol used by this client class.

  > `struct` `SmogStruct`: The struct instance to format.
  >
  > `validate` `bool`: Whether the struct should be validated before being formatted.

  return: `str`

  raises: `ValueError` If the given struct cannot be formated on the protocol for this client class.
* `format_fault(struct, validate=True)`

  Formats the given struct as a fault for the protocol used by this client class.

  > `struct` `SmogStruct`: The struct instance to format.
  >
  > `validate` `bool`: Whether the struct should be validated before being formatted.

  return: `str`

  raises: `ValueError` If the given struct cannot be formated on the protocol for this client class.
* `create_struct_<operation-name>(*args, **kwargs)`

  Creates SmogStruct instance that can be used as input for a specific operation.

  return: `SmogStruct`
* `exception_context()`

  Returns contextual information from mapping method where self.exception was raised.
  The returned information is formatted as JSON.

  return: `str`

#### Generated service implementations

##### Python

##### Python API

###### Service Variables

###### Methods in server implementation classes

###### Methods in client implementation classes

### Customizing SMOG


By means of parameters `-c` and `-d` (see [Using SMOG](#using-smog)), it is possible to specify custom protocol and language packages in order to
customize protocol implementations or languages supported natively by SMOG, or to add support for other protocols and languages.
The following sections provide examples of how to do this. Note that this kind of customizations is not to be mixed up with extending or customizing
service specifications or service mappings as described in chapters [Struct extensions](#struct-extensions), [Service extensions](#service-extensions) and [Mapping extensions](#mapping-extensions).
Customizing SMOG itself is normlly not needed when working with service configurations and is therefore not considered normal usage.
Hence, the api:s described in this chapter should be seen as internal to SMOG and may change without notice.

##### 6.1. Customizing Protocols

Each protocol natively supported by SMOG is implemented in a python module with the same name as the protocol, in package `smog.<smog version>.protocols`.
As an example, the **soap** protocol is implemented in `$SMOG_HOME/python/smog/v2/protocols/soap.py` for version 2 of SMOG.

In SMOG the class **ProtocolMgr** is responsible for reading the protocol specification, dynamically load the protocol modules needed and govern the generation of protocol artifacts.
By specifying parameter `-c <custom protocol package>` when running SMOG, the ProtocolMgr will first look for protocol implementations
in the <custom protocol package>. If a certain protocol implementation is found there, it will use that implementation instead of the one
in the native protocol package.

All protocol modules must implement a function with the following signature: (no particular return value is required):

```
    generate_protocol_artifacts(protocol_mgr, protocol_node)

,where protocol_mgr:  An instance of the ProtocolMgr
       protocol_node: A python data structure representing the <protocol> node
                      that specifies the protocol in the protocol specification.
                      See configreader module for more information about the
                      python data structure.
```

In order to generate protocol specific parts of the service implementation, the protocol module must also implement a function with the following signature:

```
    get_code_generator(protocol_mgr, protocol_node, language)

,where protocol_mgr:  see above
       protocol_node: see above
       language:      Target language for the generated service implementation
 The function should return an instance of a code generator class that implements the interface prescribed for the specified language (see TODO: add reference).
```

###### 6.1.1. Customizing an existing Protocol implementation

In this example, the implementation of the [plainxml](plainxml.html#plainxml) protocol is changed such that all struct members are represented as xml elements
in the generated XSD.

1. Store the following protocol specification as “protocol.xml”:

```
<?xml version="1.0" encoding="UTF-8"?>
<protocol-spec xmlns="http://namespace.jeppesen.com/smog/v2" target="hello">
   <protocol name="plainxml"/>
</protocol-spec>
```

2. Store the following module as “plainxml.py” in a directory e.g. “my\_protocol\_cust” and make sure the directory contains a “\_\_init\_\_.py” and is included in the PYTHONPATH:

```
import smog.v2.protocols.plainxml

def generate_protocol_artifacts(mgr, protocol):
    """
    Entry point for generation of protocol artifacts.

    @param mgr:           Protocol manager
    @type mgr:            artifactmanager.ProtocolMgr
    @param protocol:      A python data structure representing the <protocol> node that
                          specifies the crap protocol in the protocol specification.
                          See configreader module for more information about the
                          python data structure
    @type protocol:       dict wrapped as configreader.ConfigNode
    """
    xsd = CustomXsdArtifact(mgr, protocol)
    xsd.generate()


class CustomXsdArtifact(smog.v2.protocols.plainxml.XsdArtifact):
    """
    Custom implementation of plainxml that extends the native SMOG implementation.
    """

    @staticmethod
    def is_xml_attribute(member):
        return False
```

3. Specify the custom protocol package with parameter **-c** when running SMOG:

   ```
   > smog -s <service spec> -p protocol.xml -c my_protocol_cust
   ```

###### 6.1.2. Adding a new Protocol implementation

In this example, the implementation of a fictitious protocol **foo** is outlined. Artifacts for protocol foo should be generated alongside with artifacts for [plainxml](plainxml.html#plainxml).

1. Store the following protocol specification as “protocol.xml”:

```
<?xml version="1.0" encoding="UTF-8"?>
<protocol-spec xmlns="http://namespace.jeppesen.com/smog/v2"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" target="my_target_env">
    <protocol name="plainxml" />
    <protocol name="foo" param1="boo" param2="koo">
        <artifact artifact_type="foo_manifest">
            <myconfig1>spam</myconfig1>
            <myconfig2>egg</myconfig2>
        </artifact>
    </protocol>
</protocol-spec>
```

2. Store the following module as “foo.py” in a directory e.g. “my\_protocol\_cust” and make sure the directory contains a “\_\_init\_\_.py” and is included in the PYTHONPATH:

```
def generate_protocol_artifacts(mgr, protocol):
    """
    Entry point for generation of protocol artifacts for the "foo" protocol.

    @param mgr:           Protocol manager
    @type mgr:            artifactmanager.ProtocolMgr
    @param protocol:      A python data structure representing the <protocol> node that
                          specifies the crap protocol in the protocol specification.
                          See configreader module for more information about the
                          python data structure
    @type protocol:       dict wrapped as configreader.ConfigNode
    """

    for artifact in protocol.get_children('artifact'):
        for service in mgr.sspec.get_services():
            output = "#" + mgr.get_docstring(service.getattr('name'), service.getattr('version')) + "\n"
            output += "FOO param1: %s\n" % protocol.getattr('param1')
            # Read artifact configuration
            artifact_type = artifact.getattr('artifact_type')
            for config in artifact.get_children():
                output += "%s=%s " % (config.tag, config.text)
            output += "\n"

        for operation in service.get_children('operation'):
            input_elem = operation.get_child('input')
            input_name = mgr.sspec.get_input_name(operation)
            output_elem = operation.get_child('output')
            output_name = mgr.sspec.get_output_name(operation)
            output += "\tINPUT %s : \t OUTPUT %s\n" % (input_name, output_name)

        # Store generated artifact
        target_fname = os.path.join(mgr.target_root_dir, mgr.target_dir, service.getattr('name') + "_" + service.getattr('version') + ".foo")
        f = open(target_fname, 'w')
        f.write(output)
        f.close()
```

3. Specify the custom protocol package with parameter **-c** when running SMOG:

   ```
   > smog -s <service spec> -p protocol.xml -c my_protocol_cust
   ```

##### 6.2. Customizing Languages

Mapping artifacts are based on the language specified by the **language** attribute in the service mapping, e.g. `<service-mapping language="Python">`.
The only language currently supported by SMOG is **Python** and it is implemented by python modules `smog.<smog version>.languages.<language>_generator` and `smog.<smog version>.languages.<language>_templates`,
where <language> is the name of the language. Hence, the **Python** language is implemented in `$SMOG_HOME/python/smog/v2/language/python_generator.py` and `$SMOG_HOME/python/smog/v2/language/python_templates.py` for version 2 of SMOG.

In SMOG the class **MappingMgr** is responsible for reading the service mapping, dynamically loading the language modules needed and governing the generation of mapping artifacts.
The two modules mentioned above are required in the interface between the MappingMgr and the language implementation.
The native Python implementation also consists of an additional module `smog.<smog version>.languages.python_struct` which is used internally by `smog.<smog version>.languages.<language>_generator` but it is not known or used by the MappingMgr.

By specifying parameter `-d <custom language package>` when running SMOG, the MappingMgr will first look for language implementations in the <custom language package>.
If a certain language implementation is found there, it will use that implementation instead of the one in the native language package.

All `smog.<smog version>.languages.<language>_generator` modules must implement a function with the following signature:

```
    generate_mapping_artifacts(mapping_mgr)

where mapping_mgr: An instance of MappingMgr
```

The MappingMgr calls this function in order to generate mapping artifacts for all services in the given service specification.
The code generation is based on templates available in module `smog.<smog version>.languages.<language>_templates`.
The MappingMgr assigns the template module as member variable “template\_module” and can then be used by the code generation through the MappingMgr instance passed in the call to `generate_mapping_artifacts`.
The MappingMgr itself doesn’t have any api requirements towards the template module.

Note that when it comes to serializing and de-serializing protocol specific messages, that part of the generated mapping artifact is unique to each protocol.
That means there is a part of the mapping that is both language- and protocol specific.
Therefore the protocol implementation must also implement an api for the code generation to use in order to generate those protocol specific parts.

In the Python implementation, the `smog.<smog version>.languages.python_generator` module expects the protocol implementation to contain a function “get\_code\_generator” as described in [Customizing Protocols](#customizing-protocols).
The function should return an instance of a code generator class that is a subclass of `smog.<smog version>.languages.python_generator.CodeGenerator` which has the following public api methods:

```
def get_module_initializations(self, service):
    """
    Returns protocol specific module initializations for the generated service implementation python module

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python code to insert as module level initializations in the generated service module
    @rtype:          list of strings
    """
    raise NotImplementedError("Must be implemented by subclass")

def get_class_initializations(self, service):
    """
    Returns protocol specific service class initializations

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python code to insert as class level initializations in the generated service class for a specific protocol
    @rtype:          string
    """
    raise NotImplementedError("Must be implemented by subclass")

def get_parse_method(self, service):
    """
    Returns python source code for a method that parses a given payload on protocol specific format and returns a SmogStruct instance
    populated with the values of the payload. The generated method is pasted into the service class for a specific protocol and
    should have the following signature:

        def parse(self, payload)

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python source code
    @rtype:          string
    """
    raise NotImplementedError("Must be implemented by subclass")

def get_format_method(self, service):
    """
    Returns python source code for a method that formats a given SmogStruct instance into protocol specific format.
    The generated method is pasted into the service class for a specific protocol and should have the following signature:

        def format(self, struct, validate=True)

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python source code
    @rtype:          string
    """
    raise NotImplementedError("Must be implemented by subclass")

def get_format_fault_method(self, service):
    """
    Returns python source code for a method that formats a given SmogStruct instance into a fault message on protocol specific format.
    The generated method is pasted into the service class for a specific protocol and should have the following signature:

        def format_fault(self, struct, validate=True)

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python source code
    @rtype:          string
    """
    raise NotImplementedError("Must be implemented by subclass")

def get_parse_value_methods(self):
    """
    Returns python source code for a set of methods for parsing string representations of values into internal plain types.
    The generated methods are pasted into the service class for a specific protocol and should have the following signatures:

        def parseString(self, value)        @type value: str               @rtype: str
        def parseInt(self, value)           @type value: str               @rtype: int
        def parseFloat(self, value)         @type value: str               @rtype: float
        def parseBool(self, value)          @type value: str               @rtype: bool
        def parseDate(self, value)          @type value: str               @rtype: datetime.date
        def parseDatetime(self, value)      @type value: ste               @rtype: datetime.datetime
        def parseDuration(self, value)      @type value: str               @rtype: datetime.timedelta
        def parseTime(self, value)          @type value: str               @rtype: datetime.time

    @return:         Python source code
    @rtype:          string
    """
    raise NotImplementedError("Must be implemented by subclass")

def get_format_value_methods(self):
    """
    Returns python source code for a set of methods for formatting values of various internal plain types into protocol specific
    string representation.
    The generated methods are pasted into the service class for a specific protocol and should have the following signatures:

        def formatString(self, value)        @type value: str                   @rtype: str
        def formatInt(self, value)           @type value: int                   @rtype: str
        def formatFloat(self, value)         @type value: float                 @rtype: str
        def formatBool(self, value)          @type value: bool                  @rtype: str
        def formatDate(self, value)          @type value: datetime.date         @rtype: str
        def formatDatetime(self, value)      @type value: datetime.datetime     @rtype: str
        def formatDuration(self, value)      @type value: datetime.timedelta    @rtype: str
        def formatTime(self, value)          @type value: datetime.time         @rtype: str

    @return:         Python source code
    @rtype:          string
    """
    raise NotImplementedError("Must be implemented by subclass")
```

###### 6.2.1. Customizing Python mapping artifacts

In this example, the implementation of mapping artifact generation for the **Python** language is changed such that an additional Copyright notice is added in the beginning of all mapping artifacts.
Note that this kind of customization can be done solely by subclassing the template class, without actually customizing module `smog.<smog version>.languages.python_generator` itself.

1. Make sure the service mapping specifies Python as language: `<service-mapping language="Python">`
2. Store the following module as “python\_templates.py” in a directory e.g. “my\_language\_cust” and make sure the directory contains a “\_\_init\_\_.py” and is included in the PYTHONPATH:

```
from smog.v2.languages.python_templates import PythonTemplate as PythonTemplateBase

class PythonTemplate(PythonTemplateBase):

    def __getattribute__(self, attr):
        prepend = ""
        if attr == "HANDLER_MODULE_TEMPLATE":
            prepend = "# Copyright: Tyrell Corporation 1982 \n"
        return prepend + super(PythonTemplate, self).__getattribute__(attr)
```

3. Specify the custom language package with parameter **-d** when running SMOG:

   ```
   > smog -s <service spec> -p <protocol spec> -m <service mapping> -d my_language_cust
   ```

#### Customizing Protocols

##### Customizing an existing Protocol implementation

##### Adding a new Protocol implementation

#### Customizing Languages

##### Customizing Python mapping artifacts

### Indices and tables
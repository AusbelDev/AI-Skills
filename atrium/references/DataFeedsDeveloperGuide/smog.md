# SMOG

The purpose of this document is to describe the how to use SMOG (Service Model Object Generator), a tool that can be used to develop services.

1. Introduction
1.1. Concepts
1.2. SMOG for Dummies - a Hello World example

2. Service Specification
2.1. Struct extensions
2.2. Service extensions
2.3. Backward compatibility
2.4. Deprecation support

3. Protocol Specification
3.1. Supported protocols

4. Service mapping
4.1. Input mapping
4.2. Output mapping
4.3. Mapping extensions
4.4. Order of execution
4.5. Pre- and post processing

5. Using SMOG
5.1. Generated service implementations

6. Customizing SMOG
6.1. Customizing Protocols
6.2. Customizing Languages

## Indices and tables

- Index
- Search Page



--- SUBPAGE: smog.html ---

# 1. Introduction

SMOG, Service Model Object Generator, is a development tool helping you define, implement and maintain services. Using SMOG you can define services
and generate artifacts required for deploying service applications in a service-oriented architecture. SMOG has been developed with the following goals in mind:

- Make it easy to define services, in the form of data structures and operations.
- Enable separation of service definition from service implementation.
- Make it easy to extend and customize existing services.
- Enable separation of protocol implementation from service business logic.
- One service should support multiple protocols (SOAP, REST, JSON, Protobuf etc.) without duplicating implementation efforts.
- Support for deploying the same service in different runtime environments.

## 1.1. Concepts

The following key concepts are given as input when using SMOG:

- Service specification: Defines services, operations and data types in a neutral format without any implementation specific details.
- Protocol specification: Specifies protocol details, for example, whether a service should use SOAP, REST or some other protocol.
- Service mapping: Provides implementation logic for a service in a specific target runtime environment. Describes how a specific backend server implements the service, how to handle service requests and how to produce service responses in that environment. The service mapping can also specify how clients should produce service requests and handle service responses for different runtime environments.

As a result SMOG generates the following artifacts:

- Service contracts: Protocol specific service contracts for the configured protocols, for example xsd, wsdl, wadl files for services.
- Service implementations: Generated source code for deploying services in different runtime environments. Source code can be generated in different languages (Python, Java, etc.).

## 1.2. SMOG for Dummies - a Hello World example

Download SMOG from Gitlab:

&gt; git clone git@git.got.jeppesensystems.com:TD/smog.git
&gt; cd smog

- Create a service specification and save it as service.xml:

&lt;service-spec name=&quot;hello&quot; xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot;&gt;
   &lt;services&gt;
      &lt;service name=&quot;Hello&quot; version=&quot;1&quot;&gt;
         &lt;operation name=&quot;sayHello&quot;&gt;
            &lt;input type=&quot;EmptyStruct&quot;/&gt;
            &lt;output type=&quot;HelloStruct&quot;/&gt;
         &lt;/operation&gt;
      &lt;/service&gt;
   &lt;/services&gt;
   &lt;types&gt;
      &lt;struct name=&quot;EmptyStruct&quot;/&gt;

      &lt;struct name=&quot;HelloStruct&quot;&gt;
         &lt;member name=&quot;helloMessage&quot; type=&quot;string&quot;/&gt;
      &lt;/struct&gt;
   &lt;/types&gt;
&lt;/service-spec&gt;

- Create a protocol specification and save it as protocol.xml:

&lt;protocol-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; target=&quot;hello&quot;&gt;
   &lt;protocol name=&quot;plainxml&quot;/&gt;
&lt;/protocol-spec&gt;

- Create a service mapping and save it as mapping.xml:

&lt;service-mapping xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; language=&quot;Python&quot;&gt;
   &lt;server-impl service_name=&quot;Hello&quot; service_version=&quot;1&quot;/&gt;

   &lt;output-mapping struct=&quot;hello.HelloStruct&quot;&gt;
      &lt;out member_or_variant=&quot;helloMessage&quot; expr=&quot;&#39;Hello World!&#39;&quot;/&gt;
   &lt;/output-mapping&gt;
&lt;/service-mapping&gt;

Run SMOG to build protocol and mapping artifacts:

&gt; app/src/main/bin/smog -s service.xml -p protocol.xml -m mapping.xml

Call the generated service implementation with just the shell as “runtime environment”:

&gt; python hello/Hello_1_server.py &quot;&lt;sayHelloRequest xmlns=&#39;http://service.jcms.jeppesen.com/Hello/v1&#39;/&gt;&quot;

You should get the following output from the service:

&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt;
&lt;sayHelloResponse xmlns=&quot;http://service.jcms.jeppesen.com/Hello/v1&quot; helloMessage=&quot;Hello World!&quot;/&gt;

# 2. Service Specification

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

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;flight&quot;&gt;
    &lt;services&gt;
        &lt;service name=&quot;Flight&quot; version=&quot;1&quot;&gt;
            &lt;operation name=&quot;getFlightStatus&quot; desc=&quot;Get status for a given flight.&quot;&gt;
                &lt;input type=&quot;FlightDesignator&quot; desc=&quot;The flight to get status for.&quot;/&gt;
                &lt;output type=&quot;FlightStatus&quot; desc=&quot;Status of the flight.&quot;/&gt;
                &lt;fault type=&quot;Error&quot; desc=&quot;Error that occurred when calling this operation.&quot;/&gt;
            &lt;/operation&gt;
            &lt;operation name=&quot;cancelFlight&quot; desc=&quot;Cancels the given flight.&quot;&gt;
                &lt;input type=&quot;FlightDesignator&quot; desc=&quot;The flight to cancel.&quot;/&gt;
            &lt;/operation&gt;
        &lt;/service&gt;
    &lt;/services&gt;

    &lt;types&gt;
        &lt;struct name=&quot;FlightDesignator&quot; desc=&quot;Information required for identifying a flight.&quot;&gt;
            &lt;member name=&quot;airline&quot; type=&quot;string&quot; desc=&quot;Airline code&quot;/&gt;
            &lt;member name=&quot;number&quot; type=&quot;int&quot; desc=&quot;Flight number&quot;/&gt;
        &lt;/struct&gt;

        &lt;struct name=&quot;FlightStatus&quot; desc=&quot;Information required for identifying a flight.&quot;&gt;
            &lt;member name=&quot;flight&quot; type=&quot;FlightDesignator&quot; desc=&quot;The flight this status applies to.&quot;/&gt;
            &lt;member name=&quot;departureTime&quot; type=&quot;dateTime&quot; desc=&quot;The departure time of this flight.&quot;/&gt;
            &lt;member name=&quot;arrivalTime&quot; type=&quot;dateTime&quot; desc=&quot;The arrival time of this flight.&quot;/&gt;
            &lt;member name=&quot;scheduleStatus&quot; type=&quot;string&quot; desc=&quot;Scheduled status of this flight.&quot;/&gt;
        &lt;/struct&gt;
        &lt;struct name=&quot;Error&quot; desc=&quot;Information about an error that occurred.&quot;&gt;
            &lt;member name=&quot;type&quot; type=&quot;string&quot; desc=&quot;Type of error.&quot;/&gt;
            &lt;member name=&quot;detail&quot; type=&quot;string&quot; desc=&quot;Detailed information about the error.&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

The root element &lt;service-spec&gt; must specify the SMOG syntax version to use, this is done by setting the xmlns attribute to a specific SMOG syntax version.

The current version is 2, version 1 should only be used for migrating services from Interface Builder (ifbuilder) tool.

The root element &lt;service-spec&gt; must also have a module name, which specifies a prefix used for avoiding naming conflicts when importing other service specification modules.
The &lt;input&gt; and &lt;output&gt; elements of the operations specifies the type of information that is passed to the operations and what type of information that is provided as return.
The operation cancelFlight is a “one-way” operation and does not have any &lt;output&gt; element.

The types section consists of &lt;struct&gt; elements, providing the details of the types used as input and output by the operations.
A struct can be seen as a complex data type, consisting of named members with a type that either is plain or complex.

The following plain types are supported:

- string: represents a string value.
- int: represents a number without any fractional digits.
- (integer): Deprecated, only available in SMOG version 1, used int instead.
- float: represents a precision floating-point type (including infinity and not-a-number).
- boolean: represents a true or false value.
- date: represents a date (without time fraction).
- time: represents the time fraction on a day (00:00:00 - 23:59:59)
- dateTime: represents a date with time fraction.
- duration: represents a time interval.
- text: represents a multi line string.
- (any): Deprecated, only available in SMOG version 1, represents value of any type.

Members of complex types refers to some other struct, for example the member “flight” in struct “FlightStatus”.

A struct can also contain &lt;variant&gt; elements, defining mutual exclusive members, which means that only one of the variants can have a value.
Only one “group” of variants can be specified in a struct. If more than one “group” of variants are needed they must be specified in separate structs.

&lt;struct name=&quot;PersonDetails&quot; desc=&quot;Information about a person&quot;&gt;
    &lt;variant name=&quot;employee&quot; type=&quot;EmployeeDetails&quot; desc=&quot;Information for an employee.&quot;/&gt;
    &lt;variant name=&quot;contractor&quot; type=&quot; ContractorDetails&quot; desc=&quot;Information for a contractor.&quot;/&gt;
    &lt;member name=&quot;firstName&quot; type=&quot;string&quot; desc=&quot;Given name of this person.&quot;/&gt;
&lt;/struct&gt;

The struct for PersonDetails above specifies that either employee or a contractor must be provided for a person, but not both at the same time.

Members and variants can also have a cardinality, specifying the allowed multiplicity for each member or variant. The cardinality is specified with brackets after the type, for example:

&lt;struct name=&quot;PersonDetails&quot; desc=&quot;Information about a person&quot;&gt;
    &lt;variant name=&quot;employee&quot; type=&quot;EmployeeDetails&quot; desc=&quot;Information for an employee.&quot;/&gt;
    &lt;variant name=&quot;contractor&quot; type=&quot;ContractorDetails&quot; desc=&quot;Information for a contractor.&quot;/&gt;
    &lt;member name=&quot;firstName&quot; type=&quot;string&quot; desc=&quot;Given name of this person.&quot;/&gt;
    &lt;member name=&quot;middleName&quot; type=&quot;string[0:1]&quot; desc=&quot;Middle name of this person.&quot;/&gt;
    &lt;member name=&quot;address&quot; type=&quot;AddressDetails[1:]&quot; desc=&quot;An address for this person.&quot;/&gt;
    &lt;member name=&quot;assignment&quot; type=&quot;WorkAssignment[:]&quot; desc=&quot;A work assignment for this person.&quot;/&gt;
    &lt;member name=&quot;lastDayOfService&quot; type=&quot;date[0:1]&quot; desc=&quot;Last day of employment for this person.&quot; nullable=&quot;true&quot;/&gt;
&lt;/struct&gt;

- Types without any specified cardinality means that the member is required and must occur exactly once in the struct, for example “firstName” in the example above.
- A cardinality of [:1] or [0:1] means that the member is optional and can occur zero or one time, for example “middleName” in the example above.
A cardinality of [] or [:] means that the member is optional and multi-valued and can occur zero or more times, for example “assignment” in the example above.
Note that the member name is “assignment” and not “assignments” since each member instance describe one assignment.

A cardinality of [1:] means that the member is multi-valued, but is required to occur at least once in the struct, for example “address” in the example above.
Note that the member name is “address” and not “addresses” since each member instance describe one address.

- For multi-valued members it is also possible to specify min and/or max values explicitly, e.g. [2:3] means that the member must occur 2 or 3 times.

Members and variants can also be specified to be nullable, as the lastDayOfService member in PersonDetails struct above.
Specifying a member or variant as nullable allows the member or variant to be a null-value instead of always being a value of the type specified for the member or variant.

The nullable lastDayOfService member can take three states in PersonDetails struct:

- lastDayOfService is set to a date value.
- lastDayOfService is not specified (the member is optional).
- lastDayOfService is set to a null value.

States 2 and 3 might appear similar, but state 2 doesn’t say anything about the value of lastDayOfService whereas state 3 clearly indicates that value of lastDayOfService is null.

The usage of nullable is limited to single valued members and variants and cannot be used for members and variants with a multi-valued cardinality.

## 2.1. Struct extensions

A struct can inherit members and variants from a parent struct by specifying the based_on attribute.

&lt;struct name=&quot;Person&quot; desc=&quot;Information about a person.&quot;&gt;
    &lt;member name=&quot;firstName&quot; type=&quot;string&quot; desc=&quot;Given name of this person.&quot;/&gt;
    &lt;member name=&quot;lastName&quot; type=&quot;string[0:1]&quot; desc=&quot;Last name of this person.&quot;/&gt;
&lt;/struct&gt;
&lt;struct name=&quot;Student&quot; based_on=&quot;Person&quot; desc=&quot;Information about a student.&quot;&gt;
    &lt;member name=&quot;graduationYear&quot; type=&quot;int&quot; desc=&quot;Year when this student graduated.&quot;/&gt;
&lt;/struct&gt;
&lt;struct name=&quot;Employee&quot; based_on=&quot;Person&quot; desc=&quot;Information about an employee.&quot;&gt;
    &lt;member name=&quot;employmentDate&quot; type=&quot;date&quot; desc=&quot;When this person was employed.&quot;/&gt;
&lt;/struct&gt;

Inheritance can also be used to redefine members, i.e. to change the type, cardinality or description.

&lt;struct name=&quot;Person&quot; desc=&quot;Information about a person.&quot;&gt;
    &lt;member name=&quot;firstName&quot; type=&quot;string&quot; desc=&quot;Given name of this person.&quot;/&gt;
    &lt;member name=&quot;lastName&quot; type=&quot;string[0:1]&quot; desc=&quot;Last name of this person.&quot;/&gt;
&lt;/struct&gt;
&lt;struct name=&quot;Student&quot; based_on=&quot;Person&quot; desc=&quot;Information about a student.&quot;&gt;
    &lt;member name=&quot;major&quot; type=&quot;string&quot; desc=&quot;Academic major subject&quot;/&gt;
&lt;/struct&gt;
&lt;struct name=&quot;GraduateStudent&quot; based_on=&quot;Student&quot; desc=&quot;Information about a graduate student.&quot;&gt;
    &lt;member name=&quot;major&quot; type=&quot;string[1:]&quot; desc=&quot;Academic major subjects&quot;/&gt;
&lt;/struct&gt;

Using inheritance is a good pattern for avoiding duplications in the service specification. It also helps when implementing the service since same logic often can be applied for handling the base struct.

Structs can be organized in modules, where each module is stored as a separate xml file. A module contains services and/or structs.
A complete service specification can thus consist of several modules put together by &lt;include&gt; elements as shown in the example below.
The &lt;include&gt; element specifies the path to the file where a module is stored.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;common&quot;&gt;
    &lt;types&gt;
        &lt;struct name=&quot;Person&quot; desc=&quot;Information about a person.&quot;&gt;
            &lt;member name=&quot;firstName&quot; type=&quot;string&quot; desc=&quot;Given name of this person.&quot;/&gt;
            &lt;member name=&quot;lastName&quot; type=&quot;string[0:1]&quot; desc=&quot;Last name of this person.&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

The service specification module above is named “common” and defines a struct called “Person”. If that module is saved as “common_structs.xml” it could be included by another service specification module:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;school&quot;&gt;
    &lt;include href=&quot;common_structs.xml&quot; /&gt;
    &lt;types&gt;
        &lt;struct name=&quot;Student&quot; based_on=&quot;common.Person&quot; desc=&quot;Information about a student.&quot;&gt;
            &lt;member name=&quot;graduationYear&quot; type=&quot;int&quot; desc=&quot;Year when this student graduated.&quot;/&gt;
        &lt;/struct&gt;
        &lt;struct name=&quot;Employee&quot; based_on=&quot;common.Person&quot; desc=&quot;Information about an employee.&quot;&gt;
            &lt;member name=&quot;employmentDate&quot; type=&quot;date&quot; desc=&quot;When this person was employed.&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

As the above example shows, structs defined in the included module are referenced using their fully qualified name &lt;module name&gt;.&lt;struct name&gt;.
For example “common.Person” is the qualified name of struct “Person” in module “common”.
The qualified name is needed for uniquely identifying the struct since more structs named “Person” could be included from other modules.

By using the &lt;struct-update&gt; element, it is possible to add members and variants to structs defined in e.g. an included module.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;school&quot;&gt;
    &lt;include href=&quot;common_structs.xml&quot; /&gt;

    &lt;types&gt;
        &lt;struct-update struct=&quot;common.Person&quot;&gt;
            &lt;add-variant name=&quot;personalNumber&quot; type=&quot;int&quot; /&gt;
            &lt;add-variant name=&quot;temporaryPersonalId&quot; type=&quot;string&quot;/&gt;
            &lt;add-member name=&quot;birthdate&quot; type=&quot;date&quot; desc=&quot;The birthday of this person.&quot;/&gt;
        &lt;/struct-update&gt;
        &lt;struct name=&quot;Student&quot; based_on=&quot;common.Person&quot; desc=&quot;Information about a student.&quot;&gt;
            &lt;member name=&quot;graduationYear&quot; type=&quot;int&quot; desc=&quot;Year when this student graduated.&quot;/&gt;
        &lt;/struct&gt;
        &lt;struct name=&quot;Employee&quot; based_on=&quot;common.Person&quot; desc=&quot;Information about an employee.&quot;&gt;
            &lt;member name=&quot;employmentDate&quot; type=&quot;date&quot; desc=&quot;When this person was employed.&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

By using the &lt;struct-update&gt; element, it is also possible to modify members and variants to existing structs.
In the following example, assume the service specification module “school” is saved as “school_structs.xml”.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;school&quot;&gt;
    &lt;types&gt;
        &lt;struct name=&quot;Student&quot; desc=&quot;Information about a student.&quot;&gt;
            &lt;member name=&quot;firstName&quot; type=&quot;string&quot; desc=&quot;Given name of this student.&quot;/&gt;
            &lt;member name=&quot;lastName&quot; type=&quot;string[0:1]&quot; desc=&quot;Last name of this student.&quot;/&gt;
            &lt;member name=&quot;graduationYear&quot; type=&quot;int&quot; desc=&quot;Year when this student graduated.&quot;/&gt;
        &lt;/struct&gt;
        &lt;struct name=&quot;GraduateStudent&quot; based_on=&quot;Student&quot; desc=&quot;Information about a graduate student.&quot;&gt;
          &lt;member name=&quot;major&quot; type=&quot;string[1:]&quot; desc=&quot;Academic major subjects&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

Members/variants of these structs can then be modified using the &lt;update-member&gt; and &lt;update-variant&gt; elements:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;myschool&quot;&gt;
    &lt;include href=&quot;school_structs.xml&quot; /&gt;

    &lt;types&gt;
        &lt;struct-update struct=&quot;school.GraduateStudent&quot;&gt;
            &lt;update-member name=&quot;major&quot; type=&quot;MajorSubject[1:2]&quot; desc=&quot;Academic major subjects, restricted to maximum two.&quot;/&gt;
        &lt;/struct-update&gt;
        &lt;struct name=&quot;MajorSubject&quot; based_on=&quot;common.Person&quot; desc=&quot;Information about a student.&quot;&gt;
            &lt;member name=&quot;subject_name&quot; type=&quot;string&quot; desc=&quot;The name of the major subject.&quot;/&gt;
            &lt;member name=&quot;credits&quot; type=&quot;int&quot; desc=&quot;Credits granted for this subject&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

Using &lt;struct-update&gt; or inheritance with “based_on” provides similar results, with the difference that &lt;struct-update&gt; doesn’t define any new struct in the service specification.
This is a vital difference when it comes to the Service Mapping concept since mappings are defined for the structs.

## 2.2. Service extensions

Not only structs can be included from other modules and updated, but also services can be included and updated by using the &lt;service-update&gt; element.
Updating existing services provides much flexibility as it makes it easy to reuse a service while adding new operations, adding output or fault messages to existing services.

In the example below, the operation “reschedule” is added to the “Flight” service which is defined in a module stored in file “flight/services.xml”.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;flight_ext&quot;&gt;
    &lt;include href=&quot;flight/services.xml&quot; /&gt;
    &lt;services&gt;
        &lt;service-update name=&quot;Flight&quot; version=&quot;1&quot; updated_version=&quot;1.1&quot;&gt;
            &lt;add-operation name=&quot;reschedule&quot; desc=&quot;Reschedules the given flight.&quot;&gt;
                &lt;input type=&quot;RescheduleFlight&quot; desc=&quot;Information of what flight to reschedule.&quot;/&gt;
            &lt;/add-operation&gt;
        &lt;/service-update&gt;
    &lt;/services&gt;
&lt;/service-spec&gt;

The example below shows how output and fault messages can be added to an operation that was originally defined as “one-way”, i.e. only having an input message.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;flight_ext&quot;&gt;
    &lt;include href=&quot;flight/services.xml&quot; /&gt;
    &lt;services&gt;
        &lt;service-update name=&quot;Flight&quot; version=&quot;1&quot; updated_version=&quot;1.1&quot;&gt;
            &lt;add-output operation=&quot;cancelFlight&quot; type=&quot;TripInfo&quot; desc=&quot;Information about affected trips.&quot;/&gt;
            &lt;add-fault operation=&quot;cancelFlight&quot; type=&quot;flight.Error&quot;/&gt;
        &lt;/service-update&gt;
    &lt;/services&gt;

    &lt;types&gt;
        &lt;struct name=&quot;TripInfo&quot;&gt;
            &lt;member name=&quot;numberOfTrips&quot; type=&quot;int&quot;/&gt;
            &lt;member name=&quot;numberOfCrew&quot; type=&quot;int&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

Another way to change an included service is to redefine it. In the following example, the version 1 of the Flight service is redefined such that
the type of the output message of operation “getFlightStatus” is changed and the operation “cancelFlight” is removed:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;flight_ext&quot;&gt;
    &lt;include href=&quot;flight/services.xml&quot; /&gt;
    &lt;services&gt;
        &lt;service name=&quot;Flight&quot; version=&quot;1&quot;&gt;
            &lt;operation name=&quot;getFlightStatus&quot; desc=&quot;Get status for a given flight.&quot;&gt;
                &lt;input type=&quot;flight.FlightDesignator&quot; desc=&quot;The flight to get status for.&quot;/&gt;
                &lt;output type=&quot;MyFlightStatus&quot; desc=&quot;Status of the flight.&quot;/&gt;
                &lt;fault type=&quot;flight.Error&quot; desc=&quot;Error that occurred when calling this operation.&quot;/&gt;
            &lt;/operation&gt;
        &lt;/service&gt;
    &lt;/services&gt;

    &lt;types&gt;
        &lt;struct name=&quot;MyFlightStatus&quot; based_on=&quot;flight.FlightStatus&quot;&gt;
           &lt;member name=&quot;scheduleStatus&quot; type=&quot;int&quot; desc=&quot;Numeric status code.&quot;/&gt;   &lt;!-- redefines the member of the base struct --&gt;
           &lt;member name=&quot;returnCounter&quot; type=&quot;int&quot; desc=&quot;Return to ramp count.&quot;/&gt;
       &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

## 2.3. Backward compatibility

When a version of a service has been deployed in a production runtime environment, only limited changes are allowed to the service specification in order not to break existing consumers/clients.
Exactly which changes are allowed depend on the protocol but normally the following applies:

- Adding optional members to input messages
- Removing optional members from output messages
- Changing cardinality of members in input messages from required to optional
- Changing cardinality of members in output messages from optional to required
- Adding operations to a service

Please refer to chapter Protocol Specification for details about specific protocols.
All other changes require a major version change of the service and thus forces consumers/clients to upgrade their protocol artifact versions.

SMOG however allows additional flexibility by introducing the possibility to annotate struct members with attributes backward_compatible_addition
and backward_compatible_removal. By using these attributes it is possible to apply additional changes to an interface,
while still maintaining backward compatibility within its current major version. Normally the following additional changes apply, although it may differ for individual protocols:

- Adding and removing optional members of any type to/from input and output messages
- Removing required members from input messages
- Adding required members to output messages

The value of the backward_compatible_addition and backward_compatible_removal attributes is a date. All changes with a certain date
represent one minor version of the service specification and date itself typically corresponds to the release date of the minor version.
Hence a particular major version of a service may aggregate backward compatible changes of more than one minor version.

## 2.4. Deprecation support

In the service specification, elements &lt;service&gt;, &lt;operation&gt;, &lt;struct&gt;, &lt;member&gt; and &lt;variant&gt; can be tagged with attribute deprecated.
The value of the attribute is a string that will be included in deprecation warning messages:

If a service or operation is deprecated, the following deprecation warning is issued when calling a deprecated operation or service:

Operation is deprecated. &lt;deprecated attribute string value&gt;

If a struct is deprecated, the following deprecation warning will be generated into the protocol artifact:

WARNING: This type is deprecated. &lt;deprecated attribute string value&gt;

If a member or variant is deprecated, the following deprecation warning will be generated into the protocol artifact:

WARNING: This field is deprecated. &lt;deprecated attribute string value&gt;

# 3. Protocol Specification

The protocol specification provides details to the protocols that services should use for communication,
for example, whether a service should use SOAP, XML, REST or some other protocol.
Protocol specifications are described using a SMOG specific xml syntax.

In its simplest form it only lists the names of the protocols to use as shown in the example below.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;protocol-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; target=&quot;some_system&quot;&gt;
    &lt;protocol name=&quot;soap&quot; /&gt;
    &lt;protocol name=&quot;plainxml&quot; /&gt;
&lt;/protocol-spec&gt;

The protocol specification above could be used for any service specification and would instruct SMOG to generate WSDL files for the “soap” protocol and XSD files for the “plainxml” protocol.
Each protocol can be further specified with more details. Certain details can be provided for different protocols.
The target attribute provides a logical name of the target environment the generated protocol artifacts are intended for.
It is used by SMOG to name the sub-directory where it stores the artifacts. The parent directory is determined by the -o parameter, see Using SMOG.

## 3.1. Supported protocols

SMOG currently supports the following protocols out of the box. It is possible to customize protocol implementations or to add new protocols as plugins.
For this purpose, the SMOG specification allows the &lt;protocol&gt; elements of the protocol specification to contain any attributes and child elements.
This enables flexible configuration of custom protocols.

Protocols for XML messages and SOAP:

- plainxml
- soap

Protocols for JSON messages and REST API’s:

- plainjson
- openapi

# 4. Service mapping

Service mapping provides implementation logic for a service in a specific target runtime environment, for example a Java application server or Python web server.
The service mapping can be seen as a mapping between the service specification and the data model of the environment where the service is deployed.

Mapping is made for the structs in the service and the mapping type is either input or output.
An input mapping for a struct programmatically describes what the service should do when receiving that struct as input.
The output mapping describes what the service should do when producing a specific struct for output or fault.
The picture in section Order of execution below describes the mapping flow, the order in which input and output mappings are executed for a service.

Service mappings are written using a SMOG xml syntax and are always made for a specific programming language, for example “Java” or “Python”.
Service mappings describe how a server or a client implements the service.

In order for a server to provide mapping for the “Flight” service below, we need to define input-mapping for structs “FlightDesignator” and “FlightSchedule”,
and output-mappings for struct “FlightInfo”. Contrary for a client, we would need to define output-mapping for struct “FlightDesignator” and
“FlightSchedule” and input-mappings for struct “FlightInfo”.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;flight&quot;&gt;
    &lt;services&gt;
        &lt;service name=&quot;Flight&quot; version=&quot;1&quot;&gt;
            &lt;operation name=&quot;getFlightInfo&quot; desc=&quot;Get information for a given flight.&quot;&gt;
                &lt;input type=&quot;FlightDesignator&quot; desc=&quot;The flight to get information for.&quot;/&gt;
                &lt;output type=&quot;FlightInfo&quot; desc=&quot;Information about the flight.&quot;/&gt;
            &lt;/operation&gt;
            &lt;operation name=&quot;rescheduleFlight&quot; desc=&quot;Reschedules the given flight.&quot;&gt;
                &lt;input type=&quot;FlightSchedule&quot; desc=&quot;New departure and arrival times for a flight.&quot;/&gt;
            &lt;/operation&gt;
        &lt;/service&gt;
    &lt;/services&gt;

    &lt;types&gt;
        &lt;struct name=&quot;FlightDesignator&quot; desc=&quot;Information required for identifying a flight.&quot;&gt;
            &lt;member name=&quot;airline&quot; type=&quot;string&quot; desc=&quot;Airline code&quot;/&gt;
            &lt;member name=&quot;number&quot; type=&quot;int&quot; desc=&quot;Flight number&quot;/&gt;
        &lt;/struct&gt;
        &lt;struct name=&quot;FlightInfo&quot; desc=&quot;Information required for identifying a flight.&quot;&gt;
            &lt;member name=&quot;flight&quot; type=&quot;FlightDesignator&quot; desc=&quot;The flight this status applies to.&quot;/&gt;
            &lt;member name=&quot;departureAirport&quot; type=&quot;string&quot; desc=&quot;The departure time of this flight.&quot;/&gt;
            &lt;member name=&quot;arrivalAirport&quot; type=&quot;string&quot; desc=&quot;The arrival time of this flight.&quot;/&gt;
        &lt;/struct&gt;
        &lt;struct name=&quot;FlightSchedule&quot; based_on=&quot;FlightDesignator&quot;&gt;
            &lt;member name=&quot;departureTime&quot; type=&quot;dateTime&quot;/&gt;
            &lt;member name=&quot;arrivalTime&quot; type=&quot;dateTime&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

Assuming that service “Flight “ should be deployed in a Python runtime environment that provides access to a database, we could use the following service mapping.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;flight_info_system&quot;&gt;
    &lt;server-impl service_name=&quot;Flight&quot; service_version=&quot;1&quot;&gt;
        &lt;runtime-parameters&gt;
            &lt;parameter name=&quot;db_session&quot; desc=&quot;A database session provided by the runtime environment.&quot;/&gt;
        &lt;/runtime-parameters&gt;
    &lt;/server-impl&gt;
&lt;/service-mapping&gt;

Assume that the same runtime environment should also provide a client, the following is needed for the client implementation:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;flight_info_system&quot;&gt;
    &lt;client-impl service_name=&quot;Flight&quot; service_version=&quot;1&quot;&gt;
        &lt;runtime-parameters&gt;
            &lt;parameter name=&quot;db_session&quot; desc=&quot;A database session provided by the runtime environment.&quot;/&gt;
        &lt;/runtime-parameters&gt;
    &lt;/client-impl&gt;
&lt;/service-mapping&gt;

Now assume that the client should only implement the rescheduleFlight operation, thus the getFlightInfo operation is not relevant for the client
and therefore the input mapping for structs “FlightInfo” and “Error” and the output mapping for “FlightDesignator” are not required. In order to hint
SMOG about this, the attribute operations can be added as shown below:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;flight_info_system&quot;&gt;
    &lt;client-impl service_name=&quot;Flight&quot; service_version=&quot;1&quot; operations=&quot;rescheduleFlight&quot;&gt;
        &lt;runtime-parameters&gt;
            &lt;parameter name=&quot;db_session&quot; desc=&quot;A database session provided by the runtime environment.&quot;/&gt;
        &lt;/runtime-parameters&gt;
    &lt;/client-impl&gt;
&lt;/service-mapping&gt;

The operations attribute is available both on &lt;server-impl&gt; and &lt;client-impl&gt; elements. More than one operation can be specified by providing a
comma separated list. If specified, the service contract and service implementation artifacts produced by SMOG will only be based on the specified
operation(s) and the structs that are associated with them. Hence, SMOG will also suppress validation of any service mapping provided for any other
structs.

The namespace given in the root &lt;service-mapping&gt; element specifies the SMOG syntax version used. The root element also has the following attributes:

- language: Specifies the programming language used in the service implementation.
target: Provides a logical name of the target environment the mapping is intended for. It specifies the name of the sub-directory where the generated mapping artifact is stored.
If ommitted, it defaults to the target given in the protocol specification. The parent directory is determined by the -g parameter, see Using SMOG.

The &lt;server-impl&gt; element states that this mapping is a server implementation of the service. The &lt;runtime-parameters&gt; lists the parameters provided by the runtime environment. Such parameters become available to use in mapping.

Just like with service specifications it also possible to import other mapping modules using the &lt;include&gt; element:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot;&gt;
    &lt;include href=&quot;$CARMSYS/data/config.flight_mapping.xml&quot;/&gt;
    &lt;include href=&quot;custom_input_mapping.xml&quot;/&gt;
    &lt;include href=&quot;custom_output_mapping.xml&quot;/&gt;
&lt;/service-mapping&gt;

Included modules may in their turn contain &lt;include&gt; element. Note that the target attribute of included mapping modules (if specified) have no effect.
It is only the target specified in the “root” mapping that is significant.

## 4.1. Input mapping

Input mappings are defined using the &lt;input-mapping&gt; element. The struct attribute identifies which struct the mapping applies to, i.e. what should the server do when receiving that struct as input. An &lt;input-mapping&gt; element can contain the following sub elements:

- &lt;import&gt; - import a module for use in subsequent mappings.
- &lt;assign&gt; - assign a value to a variable for use in mapping of this struct and in mappings of child structs.
- &lt;condition&gt; - omit the mapping of this struct if the specified condition is not fulfilled.
- &lt;call&gt; - call a function before iterating child struct mappings.
- &lt;assign-last&gt; - same as &lt;assign&gt; but evaluated after iterating child structs (new in SMOG v2).
- &lt;call-last&gt; - call a function after iterating child struct mappings.

A &lt;condition&gt; applied directly on &lt;input-mapping&gt; or &lt;output-mapping&gt; is also called struct level condition.
Sub elements &lt;assign&gt;, &lt;assign-last&gt;, &lt;call&gt; and &lt;call-last&gt; can also have a &lt;condition&gt; element for omitting the use of that part if the specified condition is not fulfilled.

&lt;input-mapping struct=&quot;flight.FlightDesignator&quot;&gt;
    &lt;import name=&quot;flight.service.helper&quot; alias=&quot;helper&quot;/&gt;
    &lt;assign name=&quot;flight_record&quot; expr=&quot;db_session.find_flight(@{struct}.airline, @{struct}.number)&quot;/&gt;
    &lt;call name=&quot;flight_not_found&quot; expr=&quot;helper.raise_exception(&#39;No such flight.&#39;)&quot;&gt;
        &lt;condition expr=&quot;flight_record is None&quot;/&gt;
    &lt;/call&gt;
    &lt;call name=&quot;cancel_flight&quot; expr=&quot;helper.cancel_flight(db_session, flight_record)&quot;&gt;
        &lt;condition expr=&quot;@{service}.operation_name == &#39;cancelFlight&#39;&quot;/&gt;
    &lt;/call&gt;
&lt;/input-mapping&gt;

The example input mapping above is for struct “FlightDesignator” and uses &lt;import&gt; for importing a Python module, making that module available
with the name “helper” in subsequent Python expressions. The &lt;assign&gt; element declares a new variable called “flight_record” which gets a value by
calling a Python expression. The name “db_session” used in the expression is provided from the runtime environment. Variables defined using &lt;assign&gt;
can be used in expressions within the same mapping and for mappings of child structs (but not the other way around). Variables defined using &lt;assign&gt;
in the &lt;input-mapping&gt; of the operations input struct are also available to use in the &lt;output-mapping&gt; of the operations output struct.
Conversely for &lt;client-impl&gt; mapping, variables defined in &lt;output-mapping&gt; are however not available to use in the &lt;input-mapping&gt;.

The syntax &#64;{struct} is used for getting the values for members “airline” and “number” of the “FlightDesignator” struct, i.e. the actual values provided in the service call.
There are two &lt;call&gt; elements, the first one uses the imported “helper” for throwing an exception if no flight record was found.
The other &lt;call&gt; element calls a function that cancels the flight, but only if the operation is “cancelFlight”.
The special token &#64;{struct}.instance_name can be used in the mapping to access the name of the context node, i.e. the currently processed struct instance in the input message.
For example in case of plainxml or soap protocols that means the element name.
The token &#64;{struct}.is_null(name) can be used in the mapping to check whether a member or variant with specified name is a null value.
The syntax &#64;{service} is used for getting or assigning service variables. A service variable can be thought of as an instance variable of the service.
Chapter Python API lists the predefined service variables provided by SMOG. In addition to these it is possible to define and use any
service variable in the mapping (both &lt;input-mapping&gt; and &lt;output-mapping&gt;).

## 4.2. Output mapping

Output mappings are defined using the &lt;output-mapping&gt; element. The struct attribute identifies which struct the mapping applies to, i.e. what the application should do when producing this struct for output. An &lt;output-mapping&gt; element can contain the following sub elements:

- &lt;import&gt; - import a module for use in subsequent mappings.
- &lt;assign&gt; - declare a variable for use in mapping of this struct and in mappings of child structs.
- &lt;condition&gt; - omit the mapping of this struct if the specified condition is not fulfilled.
- &lt;call&gt; - call a function before iterating child struct mappings.
- &lt;out&gt; - sets the value of a member or variant of this struct.
- &lt;assign-last&gt; - same as &lt;assign&gt; but evaluated after iterating child structs (new in SMOG v2).
- &lt;call-last&gt; - call a function after iterating child struct mappings.

A &lt;condition&gt; applied directly on &lt;input-mapping&gt; or &lt;output-mapping&gt; is also called struct level condition.
In &lt;output-mapping&gt;, nullable members and variants of complex types are set to null when struct level conditions of structs are not fulfilled.
Sub elements &lt;assign&gt;, &lt;assign-last&gt;, &lt;out&gt;, &lt;call&gt; and &lt;call-last&gt; can also have a &lt;condition&gt; element for omitting the use of that part if the specified condition is not fulfilled.

The example output mapping below is for struct “FlightStatus” and uses &lt;out&gt; for setting the values of the members. Values are received by calling a Python expression using the variable “flight_record” defined in the &lt;input-mapping&gt;.

&lt;output-mapping struct=&quot;flight.FlightStatus&quot;&gt;
    &lt;out member_or_variant=&quot;departureTime&quot; expr=&quot;flight_record.get_departure_time()&quot; /&gt;
    &lt;out member_or_variant=&quot;arrivalTime&quot; expr=&quot;flight_record.get_arrival_time()&quot; /&gt;
    &lt;out member_or_variant=&quot;scheduleStatus&quot; expr=&quot;flight_record.get_schedule_status()&quot; /&gt;
&lt;/output-mapping&gt;

If the member or variant is of multi-value type then attribute iter is used instead of expr in the &lt;out&gt; element. Assume a struct “CreatureDetails” defined as:

&lt;struct name=&quot;CreatureDetails&quot; desc=&quot;Information about a creature&quot;&gt;
    &lt;variant name=&quot;humanAddress&quot; type=&quot;HumanAddressDetails[0:]&quot; /&gt;
    &lt;variant name=&quot;alienAddress&quot; type=&quot;AlienAddressDetails[0:]&quot; /&gt;
    &lt;member name=&quot;phone&quot; type=&quot;string[0:]&quot; /&gt;
    &lt;member name=&quot;spaceship&quot; type=&quot;Spaceship[0:1]&quot;/&gt;
&lt;/struct&gt;

&lt;struct name=&quot;HumanAddressDetails&quot;&gt;
    &lt;member name=&quot;street&quot; type=&quot;string&quot;/&gt;
    &lt;member name=&quot;city&quot; type=&quot;string&quot;/&gt;
&lt;/struct&gt;

&lt;struct name=&quot;AlienAddressDetails&quot;&gt;
    &lt;member name=&quot;planet&quot; type=&quot;string&quot;/&gt;
    &lt;member name=&quot;galaxy&quot; type=&quot;string&quot;/&gt;
    &lt;member name=&quot;universe&quot; type=&quot;string&quot;/&gt;
&lt;/struct&gt;

&lt;struct name=&quot;Spaceship&quot;&gt;
    &lt;member name=&quot;model&quot; type=&quot;string[0:1]&quot;/&gt;
    &lt;member name=&quot;regNo&quot; type=&quot;string&quot;/&gt;
&lt;/struct&gt;

Then the &lt;out&gt; elements for the multi-value members and variants need to specify the iter attribute:

&lt;output-mapping struct=&quot;space.CreatureDetails&quot;&gt;
    &lt;out member_or_variant=&quot;humanAddress&quot; iter=&quot;db_result.get_addresses(creature.id, human=True)&quot; variable_name=&quot;address_obj&quot;/&gt;
    &lt;out member_or_variant=&quot;alienAddress&quot; iter=&quot;db_result.get_addresses(creature.id, human=False)&quot; variable_name=&quot;address_obj&quot;/&gt;
    &lt;out member_or_variant=&quot;phone&quot; iter=&quot;db_result.get_phone_numbers(creature.id)&quot; /&gt;
&lt;/output-mapping&gt;

&lt;output-mapping struct=&quot;space.HumanAddressDetails&quot;&gt;
    &lt;out member_or_variant=&quot;street&quot; expr=&quot;address_obj.get_street()&quot;/&gt;
    &lt;out member_or_variant=&quot;city&quot; expr=&quot;address_obj.get_city()&quot;/&gt;
&lt;/output&gt;

&lt;output-mapping struct=&quot;space.AlienAddressDetails&quot;&gt;
    &lt;out member_or_variant=&quot;planet&quot; expr=&quot;address_obj.get_planet()&quot;/&gt;
    &lt;out member_or_variant=&quot;galaxy&quot; expr=&quot;address_obj.get_galaxy()&quot;/&gt;
    &lt;out member_or_variant=&quot;universe&quot; expr=&quot;&#39;the one and only&#39;&quot;/&gt;
&lt;/output&gt;

Note that for the members or variants that are of complex (struct) types, the additional variable_name attribute is needed.
The variable_name defines the variable in which each address instance is available to the child struct mappings.

The variable_name attribute is also mandatory for a non multi-value complex member or variant if the expr attribute is specified:

&lt;output-mapping struct=&quot;space.CreatureDetails&quot;&gt;
    &lt;out member_or_variant=&quot;spaceship&quot; expr=&quot;spaceships.get_ship_for_creature(creature.id)&quot; variable_name=&quot;ship&quot;/&gt;
&lt;/output-mapping&gt;

&lt;output-mapping struct=&quot;space.Spaceship&quot;&gt;
    &lt;out member_or_variant=&quot;model&quot; expr=&quot;ship.model&quot;/&gt;
    &lt;out member_or_variant=&quot;regNo&quot; expr=&quot;ship.regno&quot;/&gt;
&lt;/output-mapping&gt;

Note however that if expr is not specified in this case, then variable_name is not needed:

&lt;output-mapping struct=&quot;space.CreatureDetails&quot;&gt;
    &lt;out member_or_variant=&quot;spaceship&quot; /&gt;
&lt;/output-mapping&gt;

&lt;output-mapping struct=&quot;space.Spaceship&quot;&gt;
    &lt;assign name=&quot;ship&quot; expr=&quot;spaceships.get_ship_for_creature(creature.id)&quot; /&gt;
    &lt;out member_or_variant=&quot;model&quot; expr=&quot;ship.model&quot;/&gt;
    &lt;out member_or_variant=&quot;regNo&quot; expr=&quot;ship.regno&quot;/&gt;
&lt;/output-mapping&gt;

In fact, for required non multi-value complex members or variants the entire &lt;out&gt; element is not needed as illustrated in the following example
in which struct “MobileCreatureDetails” redefines “spaceship” to be a required member (note that the cardinality “[0:1]” has been removed from the type):

&lt;struct name=&quot;MobileCreatureDetails&quot; based_on=&quot;CreatureDetails&quot;&gt;
    &lt;member name=&quot;spaceship&quot; type=&quot;Spaceship&quot;/&gt;
&lt;/struct&gt;

Output mapping for struct “MobileCreatureDetails” wouldn’t need the &lt;out member_or_variant=”spaceship”/&gt;. Only the output mapping for the “Spaceship”
struct itself is needed.

In fact, SMOG does not enforce output mapping to be specified for any structs used in output, leaving the possibility to build output structs
programmatically using the generated service implementation, see Generated service implementations.

## 4.3. Mapping extensions

As we saw in the beginnig of this chapter, a service mapping can combine several mapping modules by means of the &lt;include&gt; element. Several modules
can even contribute to the mapping for one and the same struct as shown in the following examples.

Regard the following extension module for a service specification:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;my_extensions&quot;&gt;
    &lt;include href=&quot;common_structs.xml&quot; /&gt;

    &lt;types&gt;
        &lt;struct-update struct=&quot;common.Person&quot;&gt;
            &lt;add-member name=&quot;birthdate&quot; type=&quot;date&quot; desc=&quot;The birthday of this person.&quot;/&gt;
        &lt;/struct-update&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

The mapping for the “Person” struct could be combined from two different sources such that the mapping for members defined in the “common” module are
separated from the mapping of the extended members. Assume the following mapping module is stored as file “base_mappings.xml”:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;air2&quot;&gt;
    &lt;output-mapping struct=&quot;common.Person&quot;&gt;
        &lt;out member_or_variant=&quot;firstName&quot; expr=&quot;crew.FirstName&quot;/&gt;
        &lt;out member_or_variant=&quot;lastName&quot; expr=&quot;crew.Surname&quot;/&gt;
    &lt;/output-mapping&gt;
&lt;/service-mapping&gt;

Then the resulting mapping for the extended struct could be specified as:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;air2&quot;&gt;
    &lt;include href=&quot;base_mappings.xml&quot;/&gt;

    &lt;output-mapping struct=&quot;common.Person&quot;&gt;
        &lt;out member_or_variant=&quot;birthdate&quot; expr=&quot;crew.birthdate&quot;/&gt;
    &lt;/output-mapping&gt;
&lt;/service-mapping&gt;

The next example shows how multiple mapping contributions can be used when a struct has been extended by means of inheritance.
Regard the following extension module for a service specification:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;my_extensions&quot;&gt;
    &lt;include href=&quot;common_structs.xml&quot; /&gt;

    &lt;types&gt;
        &lt;struct name=&quot;Employee&quot; based_on=&quot;Person&quot; desc=&quot;Information about an employee.&quot;&gt;
           &lt;member name=&quot;employmentDate&quot; type=&quot;date&quot; desc=&quot;Date of employment.&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

Then, assuming the same “base_mappings.xml” as above, the resulting mapping for the new struct “Employee” could be specified as follows.
Note that the output mapping for “Employee” not only defines the mapping for the extra member “employmentDate” but also redefines
the mapping for member “firstName”:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;air2&quot;&gt;
    &lt;include href=&quot;base_mappings.xml&quot;/&gt;

    &lt;output-mapping struct=&quot;my_extensions.Employee&quot;&gt;
        &lt;out member_or_variant=&quot;firstName&quot; expr=&quot;crew.FirstName + &#39; &#39; + crew.MiddleName&quot;/&gt;
        &lt;out member_or_variant=&quot;graduationYear&quot; expr=&quot;crew.Birthdate&quot;/&gt;
    &lt;/output-mapping&gt;
&lt;/service-mapping&gt;

The principles for combining mapping contributions as outlined in this section apply not only to &lt;out&gt; but to all other types of mapping elements as well
(&lt;import&gt;, &lt;assign&gt;, &lt;condition&gt; etc.), both for &lt;input-mapping&gt; and &lt;output-mapping&gt;. The resulting mapping is made up by applying each contribution in document order.
In case any of the mappings in such a hierarchy of contributions contains more than one mapping element with the same name,
the elements are matched starting from the lowest index and any overshooting instances (number of child/parent instances  differ) are applied last (among elements of the same type), as illustrated below:

&lt;output-mapping struct=&quot;MyStruct&quot;&gt;
    &lt;assign name=&quot;myVar&quot; expr=&quot;1&quot; /&gt;
    &lt;out member_or_variant=&quot;outcome&quot; expr=&quot;myVar&quot; /&gt;
&lt;/output-mapping&gt;

&lt;output-mapping struct=&quot;MyStruct&quot;&gt;
    &lt;assign name=&quot;myVar&quot; expr=&quot;3&quot; /&gt;
    &lt;assign name=&quot;myVar&quot; expr=&quot;myVar + 1&quot; /&gt;
&lt;/output-mapping&gt;

Hence, “outcome” would yield “4” in the resulting output mapping for “MyStruct” because:

- The two mapping contributions for “MyStruct” are applied in document order, and therefore
- the “&lt;assign name=’myVar’ expr=’3’ /&gt;” will match (and thus redefine/replace) “&lt;assign name=’myVar’ expr=’1’ /&gt;”, and
- the overshooting “&lt;assign name=’myVar’ expr=’myVar + 1’ /&gt;” will be applied last of the &lt;assign&gt;’s

For mapping elements where the “name” attribute is optional, elements are only redefined if the “name” attribute is specified.
This applies to mapping element types &lt;call&gt; and &lt;call-last&gt;, and is illustrated in the next example:

&lt;output-mapping struct=&quot;MyStruct&quot;&gt;
    &lt;call name=&quot;init&quot; expr=&quot;helper.init()&quot; /&gt;
    &lt;call expr=&quot;helper.do_it()&quot; /&gt;
&lt;/output-mapping&gt;

&lt;output-mapping struct=&quot;MyStruct&quot;&gt;
    &lt;call name=&quot;init&quot; expr=&quot;helper.reset()&quot; /&gt;
    &lt;call expr=&quot;helper.do_this_too()&quot; /&gt;
&lt;/output-mapping&gt;

Hence, the execution of &lt;call&gt;’s in the resulting output mapping for “MyStruct” would be:

- helper.reset()
- helper.do_it()
- helper.do_this_too()

### 4.3.1. Extensions and overrides to &lt;server-impl&gt; and &lt;client-impl&gt;

In the same way as described for &lt;input-mapping&gt; and &lt;output-mapping&gt; above, inheritance and overloading can also be applied to
the &lt;server-impl&gt; and &lt;client-impl&gt; sections in the service mapping:

Assume the following mapping module is stored as “base_mappings.xml” (details left out for clarity):

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;flight_info_system&quot;&gt;
    &lt;client-impl service_name=&quot;Flight&quot; service_version=&quot;1&quot; operations=&quot;rescheduleFlight&quot;&gt;
        &lt;runtime-parameters&gt;
            &lt;parameter name=&quot;db_session&quot; desc=&quot;A database session provided by the runtime environment.&quot;/&gt;
        &lt;/runtime-parameters&gt;
    &lt;/client-impl&gt;

    &lt;output-mapping struct=&quot;common.FlightSchedule&quot;&gt;
        :
    &lt;/output-mapping&gt;
&lt;/service-mapping&gt;

Then, it is possible to customize the client implementation as illustrated below:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;flight_info_system&quot;&gt;
    &lt;include href=&quot;base_mappings.xml&quot;/&gt;

    &lt;client-impl service_name=&quot;Flight&quot; service_version=&quot;1&quot; operations=&quot;rescheduleFlight, cancelFlight&quot;/&gt;

    &lt;output-mapping struct=&quot;common.FlightCancellationData&quot;&gt;
        :
    &lt;/output-mapping&gt;
&lt;/service-mapping&gt;

Note that in the custom version of the client, the operations attribute is redefined such that the client now also contains
an implementation of the cancelFlight operation.

It is also possible to customize the runtime parameters of an implementation as illustrated in the next snippet where
a new parameter logger has been introduced:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;flight_info_system&quot;&gt;
    &lt;include href=&quot;base_mappings.xml&quot;/&gt;

    &lt;client-impl service_name=&quot;Flight&quot; service_version=&quot;1&quot; operations=&quot;rescheduleFlight, cancelFlight&quot;&gt;
        &lt;runtime-parameters&gt;
            &lt;parameter name=&quot;db_session&quot; desc=&quot;A database session provided by the runtime environment.&quot;/&gt;
            &lt;parameter name=&quot;logger&quot; desc=&quot;Global logger instance&quot;/&gt;
        &lt;/runtime-parameters&gt;
    &lt;/client-impl&gt;

    &lt;output-mapping struct=&quot;common.FlightCancellationData&quot;&gt;
        :
    &lt;/output-mapping&gt;
&lt;/service-mapping&gt;

Note that when overriding runtime parameters in this way, the &lt;runtime-parameters&gt; section must be specified as a whole, i.e. in the
above example both db_session and logger must be included (i.e. if the intention is to keep the original db_session parameter).

Within the &lt;server-impl&gt; and &lt;client-impl&gt; sections it is also possible to customize pre- and post-processors in the same fashion
(see Pre- and post processing).

## 4.4. Order of execution

The execution order of struct mappings are based on the service specification.
The execution of the input mapping is driven by the structure and contents of the input message. It starts on the top level with the struct defined as input type of the operation.
Input mappings of child structs are executed based on the order they appear in the service specification, recursing downwards for all struct members.

Operations within each input-mapping are executed in the following order:

- Import modules for all &lt;import&gt; elements (imports for all &lt;input-mappings&gt; and &lt;output-mappings&gt; happens globally when the execution is initiated)
- Evaluate all &lt;assign&gt; elements in the order they appear in the &lt;input-mapping&gt;.
- Evaluate the struct level &lt;condition&gt; element (if any) and abort execution if it returns false.
- Evaluate all &lt;call&gt; elements in the order they appear in the &lt;input-mapping&gt;.
- Execute &lt;input-mapping&gt; for the variant of the struct (only one of the variants can have a value). If the variant is a struct, execute the &lt;input-mapping&gt; for that struct.
- Execute &lt;input-mapping&gt; for each struct member in the order they appear in the &lt;struct&gt;. If the member is a struct, execute the &lt;input-mapping&gt; for that struct.
- Evaluate all &lt;assign-last&gt; elements in the order they appear in the &lt;input-mapping&gt;.
- Evaluate all &lt;call-last&gt; elements in the order they appear in the &lt;input-mapping&gt;.

Operations within each output-mapping are executed in the following order:

- Import modules for all &lt;import&gt; elements (imports for all &lt;input-mappings&gt; and &lt;output-mappings&gt; happens globally when the execution is initiated)
- Evaluate all &lt;assign&gt; elements in the order they appear in the &lt;output-mapping&gt;.
- Evaluate the &lt;condition&gt; element (if any) and abort execution if it returns false.
- Evaluate all &lt;call&gt; elements in the order they appear in the &lt;output-mapping&gt;.
- Execute &lt;out&gt; for each variant in the order they appear in the &lt;struct&gt;. Stop on the first variant with a &lt;condition&gt; that evaluates to true and skip the other variants. If the variant is a struct, execute the &lt;output-mapping&gt; for that struct.
- Execute &lt;out&gt; for each members in the order they appear in the &lt;struct&gt;. If the member is a struct, execute the &lt;output-mapping&gt; for that struct.
- Evaluate all &lt;assign-last&gt; elements in the order they appear in the &lt;output-mapping&gt;.
- Evaluate all &lt;call-last&gt; elements in the order they appear in the &lt;output-mapping&gt;.

## 4.5. Pre- and post processing

In SMOG it is possible to plugin code to be executed before input mapping is executed (pre-process) and/or after output mapping is executed (post-process).
Several pre- and post-processing steps can be chained together and will then be executed after eachother such that the output from one step becomes
the input to the next. Pre-process steps are invoked when calling methods “handle” and “fault” on the service class, or “handle_response” in case of a client.
See Python API for more information about the public methods.
Pre-processors are also invoked if “operation_&lt;operation-name&gt;” or “handle_&lt;operation-name&gt;_response” are called directly (bypassing the “handle”/”handle_response” methods).
Post-process steps can specify an optional operation such that it will only be executed after the given operation.

Consider the following service mapping module stored as “hotel_mapping_base.xml”:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; language=&quot;Python&quot; target=&quot;air2&quot;&gt;

  &lt;server-impl service_name=&quot;TripHotel&quot; service_version=&quot;1&quot;&gt;
      &lt;runtime-parameters&gt;
          &lt;parameter name=&quot;planholder&quot; /&gt;
          &lt;parameter name=&quot;service_context&quot; /&gt;
      &lt;/runtime-parameters&gt;
      &lt;pre-process name=&quot;api_request&quot; module=&quot;std_interfaces.api_hotels&quot; function=&quot;HotelHandler.from_pairing_request&quot;/&gt;
      &lt;post-process name=&quot;api_export_pairings&quot; module=&quot;std_interfaces.api_hotels&quot; function=&quot;HotelHandler.to_load_trips&quot; operation=&quot;exportTrips&quot;/&gt;
      &lt;post-process name=&quot;api_export_rosters&quot; module=&quot;std_interfaces.api_hotels&quot; function=&quot;HotelHandler.to_update_trips&quot; operation=&quot;exportRosters&quot;/&gt;
  &lt;/server-impl&gt;

&lt;/service-mapping&gt;

SMOG calls the pre- and post-processing functions with the service instance as the first parameter.
The rest of the signature is identical to that of the “handle” method of the service class, see Python API (or, for a client implementation the “make_&lt;operation&gt;_request” and handle_&lt;operation&gt;_response” methods).
The Python code below shows in principle how the plugin code in python module “std_interfaces/api_hotels.py” could be implemented:

class HotelHandler(BaseInterfaceHandler):

    @classmethod
    def from_pairing_request(cls, service, request_payload, request_headers, planholder, service_context):
        &quot;&quot;&quot;
        Pre-processing step to transform &quot;Request-Pairing-Refresh&quot; request messages
        &quot;&quot;&quot;
        xsl_path = cls.get_path(&quot;from_pairing_request.xsl&quot;)
        return cls._xslt_transform(xsl_path, request_payload)

    @classmethod
    def to_load_pairings(cls, service, response_payload, request_headers, planholder, service_context):
        &quot;&quot;&quot;
        Post-processing step to transform messages on format TripHotel_version1.xsd to ACES Load-Pairings.xsd
        &quot;&quot;&quot;
        xsl_path = cls.get_path(&quot;to_api_hotels_pairings.xsl&quot;)
        service.response_headers.update({&#39;JMSType&#39;: &#39;Load-Pairings&#39;})
        return cls._xslt_transform(xsl_path, response_payload, transaction=&quot;load&quot;)

    @classmethod
    def to_update_pairings(cls, service, response_payload, request_headers, planholder, service_context):
        &quot;&quot;&quot;
        Post-processing step to transform messages on format TripHotel_version1.xsd to ACES Update-Pairings.xsd
        &quot;&quot;&quot;
        ext_schema_path = cls.get_path(&quot;Update-Pairings.xsd&quot;)
        xsl_path = cls.get_path(&quot;to_api_hotels_pairings.xsl&quot;)
        service.response_headers.update({&#39;JMSType&#39;: &#39;Update-Pairings&#39;})
        return cls._xslt_transform(xsl_path, response_payload, transaction=&quot;update&quot;)

Pre- and post-processing steps can be extended/redefined in the same way as other mapping elements, following the same principles as described in Mapping extensions:
The following mapping shows how e.g. the pre-processing step of the “TripHotel” service could be customized:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; language=&quot;Python&quot; target=&quot;air2&quot;&gt;
  &lt;include href=&quot;hotel_mapping_base.xml&quot;/&gt;

  &lt;server-impl service_name=&quot;TripHotel&quot; service_version=&quot;1&quot;&gt;
      &lt;pre-process name=&quot;api_request&quot; module=&quot;api_hotels_extensions&quot; function=&quot;custom_pairing_request&quot;/&gt;
  &lt;/server-impl&gt;

&lt;/service-mapping&gt;

The custom redefined pre-processor named “api_request” could be implemented e.g. as follows in python module “api_hotels_extensions.py”:

def custom_pairing_request(cls, service, request_payload, request_headers, planholder, service_context):
    # In the custom version of the pre-processing no transform is needed, just log the request
    logger.info(request_payload)
    return request_payload

In the previous example a pre-processor was used for transforming some external format into the protocol configured for the service.
A slightly different use case is for the pre-processor to parse directly from an external format to the protocol independent “internal” SMOG format.
Chapter Generated service implementations explains that the generated service class contains class representations for all structs used by the service.
The following shows an example where the pre-processor passes an internal SmogStruct instance to the input mapping. Assume the following service specification:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; name=&quot;flight_input&quot;&gt;
    &lt;services&gt;
        &lt;service name=&quot;FlightInput&quot; version=&quot;1&quot;&gt;
            &lt;operation name=&quot;createFlight&quot;&gt;
                &lt;input type=&quot;FlightMsg&quot;/&gt;
            &lt;/operation&gt;
        &lt;/service&gt;
    &lt;/services&gt;

    &lt;types&gt;
        &lt;struct name=&quot;FlightMsg&quot;&gt;
            &lt;member name=&quot;source&quot; type=&quot;string&quot; desc=&quot;Message source&quot; /&gt;
            &lt;member name=&quot;version&quot; type=&quot;string&quot; desc=&quot;Message version&quot; /&gt;
            &lt;member name=&quot;flight&quot; type=&quot;Flight&quot; desc=&quot;The flight this status applies to.&quot;/&gt;
        &lt;/struct&gt;
        &lt;struct name=&quot;Flight&quot; desc=&quot;Information about the flight to create.&quot;&gt;
            &lt;member name=&quot;airline&quot; type=&quot;string&quot; desc=&quot;Airline code&quot;/&gt;
            &lt;member name=&quot;flightNumber&quot; type=&quot;int&quot; desc=&quot;Flight number&quot;/&gt;
            &lt;member name=&quot;dateOfOrigin&quot; type=&quot;date&quot; desc=&quot;Flight date&quot;/&gt;
        &lt;/struct&gt;
    &lt;/types&gt;
&lt;/service-spec&gt;

and the service mapping would look something like this (&lt;input-mapping&gt; sections excluded for clarity):

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=http://namespace.jeppesen.com/smog/v2 language=&quot;Python&quot; target=&quot;flight_info_system&quot;&gt;
    &lt;server-impl service_name=&quot;FlightInput&quot; service_version=&quot;1&quot;&gt;
        &lt;runtime-parameters&gt;
            &lt;parameter name=&quot;db_session&quot; desc=&quot;A database session provided by the runtime environment.&quot;/&gt;
        &lt;/runtime-parameters&gt;
        &lt;pre-process name=&quot;from_iata_asm&quot; module=&quot;std_interfaces_parsers.iata&quot; function=&quot;parse_asm&quot; /&gt;
    &lt;/server-impl&gt;

&lt;/service-mapping&gt;

The code below outlines how the pre-processor named “from_iata_asm” could be implemented in python module “std_interfaces_parsers/iata.py”:

def parse_asm(service, request_payload, request_headers, db_session):
    parser = ASMParser()
    asm_msg = parser.parse(request_payload)
    smog_struct = service.create_struct_createFlight({&#39;source&#39;: &#39;ASM&#39;, &#39;version&#39;: &#39;1&#39;)
    smog_struct.flight = service.Flight({&#39;airline&#39;: asm_msg.carrier, &#39;flightNumber&#39;: asm_msg.num, &#39;dateOfOrigin&#39;: asm_msg.dor})

    return smog_struct

Notice how SmogStruct instances are created using the public interface of the SMOG generated service class.
See chapter Generated service implementations and sub-sections for more info.

The exmple below illustrates how pre- and post-processing can be applied to a client implementation. Note that for a “trigger” type of client,
that only produces request messages, only post-processing steps are relevant.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;service-mapping xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; language=&quot;Python&quot; target=&quot;air2&quot;&gt;

    &lt;client-impl service_name=&quot;TripHotel&quot; service_version=&quot;1&quot;&gt;
        &lt;runtime-parameters&gt;
            &lt;parameter name=&quot;plan&quot; desc=&quot;Plan instance from IOServer.&quot;/&gt;
            &lt;parameter name=&quot;ravesession&quot; desc=&quot;Rave session from IOServer.&quot;/&gt;
            &lt;parameter name=&quot;changeset&quot; desc=&quot;Mave changeset from IOServer.&quot;/&gt;
            &lt;parameter name=&quot;service_logger&quot; desc=&quot;Logger instance from IOServer.&quot;/&gt;
            &lt;parameter name=&quot;now_time&quot; desc=&quot;Current time according to the runtime environment.&quot;/&gt;
         &lt;/runtime-parameters&gt;
         &lt;post-process name=&quot;api_transactions&quot; module=&quot;std_interfaces.api_hotels_1&quot; function=&quot;HotelEventHandler.to_api_transaction&quot; operation=&quot;updateTrips&quot;/&gt;
    &lt;/client-impl&gt;

&lt;/service-mapping&gt;

The post-processing step above could be implemented in python module “std_interfaces/api_hotels.py” as follows:

class HotelEventHandler(BaseInterfaceHandler):

    @classmethod
    def to_api_transaction(cls, client, request_payload, request_headers, plan, ravesession, changeset, service_logger, now_time):
        &quot;&quot;&quot;
        Post-processing step to transform messages on format TripEventOutput_version1.xsd to ACES formats
        &quot;&quot;&quot;
        xsl_path = cls.get_path(&quot;to_api_hotels_pairings.xsl&quot;)
        tree = etree.fromstring(request_payload)
        payload_list = []
        headers_list = []

        # Handle addTrip
        ext_schema_path = cls.get_path(&quot;Add-Pairing.xsd&quot;)
        for trip_elem in tree.xpath(&quot;/jct:updateTripsRequest/jct:addTrip&quot;, namespaces=nsmap):
            msg, props = cls._transform_trip_elem(xsl_path, ext_schema_path, trip_elem, request_headers)
            props[&#39;JMSType&#39;] = &#39;Add-Pairing&#39;
            payload_list.append(msg)
            headers_list.append(props)

        # Handle updateTrip
        ext_schema_path = cls.get_path(&quot;Revise-Pairing.xsd&quot;)
        for trip_elem in tree.xpath(&quot;/jct:updateTripsRequest/jct:updateTrip&quot;, namespaces=nsmap):
            msg, props = cls._transform_trip_elem(xsl_path, ext_schema_path, trip_elem, request_headers)
            props[&#39;JMSType&#39;] = &#39;Revise-Pairing&#39;
            payload_list.append(msg)
            headers_list.append(props)

        client.request_headers = headers_list
        return payload_list

The above example also illustrates that a post-processing step may return a list of payloads i.e. splitting the original payload into several messages.
If several post-processing steps are chained together, the multiplicity must of course be taken into account when payload is passed on between steps -
a post-processing step must be able to handle a list of payloads as input in case the preceding step returns a list of payloads.

The attribute process_struct=&quot;true&quot; can be set on the first &lt;post-process&gt; element in &lt;server-impl&gt; or &lt;client-impl&gt; (only SMOG version 2).
SMOG passes the output SMOG struct instance as request_payload/response_payload to the post processor, instead of passing the payload formatted on the protocol being used.
This is useful in situations where it’s easier to format the SMOG struct to the target format rather than a formatted payload.

Both pre- and post-processors may return None to indicate that they leave the payload unchanged. This is equivalent to returning the input payload of the processor.

# 5. Using SMOG

Smog is run from the command line, the usage is:

smog [options] -s filename

Filename is the name of the required service specification. More options can be specified for providing a protocol specification and optionally a service mapping.

-h, --help
Show this help message and exit

-p
Path to protocol specification file that specifies the protocol artifacts to generate.

-m
Path to service mapping file that specifies the service implementation artifacts to generate.

-o
Output directory for service contracts artifacts. Default: “.”

-g
Output directory for service implementation artifacts. Default: “.”

-c
Custom protocol package. Python package containing custom protocol implementation.

-d
Custom language package. Python package containing custom language implementation.

-n
Optional service name (case sensitive) to filter the services specified in the service specification. If not specified, protocol and mapping artifacts are generated for all services in the given service specification.

-v
Optional service version to filter the services specified in the service specification.

-e
Optional comma-separated list of protocols (case sensitive) to override the protocols specified in protocol specification.

-j
Print service service specification and information about built artifacts on json format on stdout

## 5.1. Generated service implementations

SMOG uses the service mapping for generating deployable service mapping artifacts for server and client implementations.
The artifacts are generated as source code for service classes with public methods to use by the calling framework in the runtime environment where the service is deployed.
The source code for the service class is generated for the language specified in the service mapping, e.g. Python, Java etc.
The mapping artifacts contain one service class for each protocol in the protocol specification.

### 5.1.1. Python

Python service classes are generated in a Python module named &lt;service-name&gt;_&lt;service-version&gt;_server|client.py .
One service class is generated for each protocol that the service supports and is named using pattern Service&lt;service-name&gt;_&lt;protocol&gt; and Client&lt;service-name&gt;_&lt;protocol&gt; for server and client implementations respectively.
The generated Python module also contains class representations for all structs used by the service.
The struct classes inherit from the static SmogStruct class and provides a simple way for programmatically working with input and output messages.

Example deployment

The example below demonstrates how the “Flight” service is deployed to run in flask web server.

&quot;&quot;&quot;
Simple web server deploying the &quot;Flight&quot; service for using the SOAP protocol.
&quot;&quot;&quot;

from flask import Flask, Response, request

# import the generated Python module
import flight_info_system.Flight_1_server as service_module

app = Flask(__name__)

db_session = None # A fictive database session provided
                  # by the environment where this application is deployed.

@app.route(&#39;/services/Flight&#39;, methods=[&#39;POST&#39;])
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
    return Response(service.response_payload, mimetype=&#39;text/xml&#39;, status=status)

### 5.1.2. Python API

5.1.2.1. Service Variables
Generated service classes provides the following service variables (public members):

request_payload: The request payload, unparsed, currently being handled.

type: str

request_headers: Dictionary containing message headers of request currently being handled.

type: dict

response_payload:  The response payload, set when output mapping is complete.

type: str or list of str

response_headers:  Dictionary containing message headers of response, set when output mapping is complete.

type: dict or list of dict

parsed_struct:  Instance representation of request being handled.

type: SmogStruct

operation_name:  Name of the operation currently being handled.

type: str

result:  A result code set when the operation is complete. A default result code can be specified for an operation by specifying attribute default_result with value “SAVE” or “UNCHANGED” on the &lt;operation&gt; element in the service specification.

type: str

exception:  The exception that was raised.

type: Exception or None

traceback:  Traceback of exception that was raised.

type: Traceback or None

fault_payloads:  Input message payload(s) in case of a fault. This information is collected when the ‘fault’ method of the service/client is called. If pre-processors are used, the intermetiate payload between each processor that changes the payload is also collected, and formatted if in SmogStruct format.

type: list of str

The service variables can be accessed from within the service mapping as e.g. &#64;{service}.operation_name.

5.1.2.2. Methods in server implementation classes
Service classes provide the following public methods to be used by the calling framework when deploying and testing the service implementation.

handle(request_payload, request_headers, &lt;runtime-parameters&gt;)

Main method for handling an incoming request messages to the service. It first analyzes the given payload and tries to figure out the operation of the payload, and then calls the corresponding handle method for operation currently being handled.

request_payload str or SmogStruct: The request message, either the “raw” message body formatted according to the protocol of the service class (e.g. an xml message for the “plainxml” protocol), or an instance of the SmogStruct subclass that represents the input type of the operation.

request_headers dict: Dictionary of headers passed with the incoming request message.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;server-impl&gt; element.

return: None

raises: Any exception raised during handling of the given request payload.

fault(request_payload, request_headers, exception, &lt;runtime-parameters&gt;)

Main method for handling errors raised outside of this handler. It is called by the runtime environment hosting the service, in order to generate an error message.
Calls the corresponding fault method for operation currently being handled.

request_payload str: The request body.

request_headers dict: Dictionary of headers passed with the incoming request message.

exception Exception: Exception to generate error message for.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;server-impl&gt; element.

return: None

operation_&lt;operation-name&gt;(request_payload, request_headers, &lt;runtime-parameters&gt;)

Method for handling an incoming request messages for a specific operation.

request_payload str or SmogStruct: The request message, either the “raw” message body formatted according to the protocol of the service class, or an instance of the SmogStruct subclass that represents the input type of the operation.

request_headers dict: Dictionary of headers passed with the incoming request message.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;server-impl&gt; element.

return: None

raises: Any exception raised during handling of the given request payload.

fault_&lt;operation-name&gt;(request_payload, request_headers, exception, &lt;runtime-parameters&gt;)

Method for generating an fault message for a specific operation.

request_payload str: The request body.

request_headers dict: Dictionary of headers passed with the incoming request message.

exception Exception: Exception to generate error message for.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;server-impl&gt; element.

return: None

pre_process(payload)

This is the main method for translating an incoming message. Any pre-processing steps (if specified) are executed first,
then the resulting payload is parsed into a SmogStruct representation (if not already done by the pre-processing) by calling
the parse(payload) method (see below).
If called in the context of error handling (i.e. when the exception property is set), it collects intermediate results
from each pre-processor that changes the payload. This can be used when generating error messages (see also service variable
‘fault_payloads’).

payload str: The payload to parse.

return: tuple of (SmogStruct, str or SmogStruct)

raises: ValueError If the payload cannot be used for creating a valid struct instance.

parse(payload)

Parses given payload and returns a struct instance populated with the values of the payload. The payload should be on the protocol associated with this service class.

payload str: The payload to parse.

return: SmogStruct

raises: ParseMsgError If the payload cannot be used for creating a valid struct instance.

format(struct, validate=True)

Formats the given struct for the protocol used by this service class.

struct SmogStruct: The struct instance to format.

validate bool: Whether the struct should be validated before being formatted.

return: str

raises: ValueError If the given struct cannot be formated on the protocol for this service class.

format_fault(struct, validate=True)

Formats the given struct as a fault for the protocol used by this service class.

struct SmogStruct: The struct instance to format.

validate bool: Whether the struct should be validated before being formatted.

return: str

raises: ValueError If the given struct cannot be formated on the protocol for this service class.

create_struct_&lt;operation-name&gt;(*args, **kwargs)

Creates SmogStruct instance that can be used as input for a specific operation.

return: SmogStruct

5.1.2.3. Methods in client implementation classes
Client classes provide the following public methods to be used by the calling framework when deploying and testing the service implementation.

make_&lt;operation-name&gt;_request(&lt;runtime-parameters&gt;)

Method for producing request messages for a specific operation. The formatted result is stored in service variable request_payload.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;client-impl&gt; element.

return: None

raises: Any exception raised during execution of the output mapping.

handle_response(response_payload, response_headers, &lt;runtime-parameters&gt;)

Main method for handling incoming response messages from a server. It first analyzes the given payload and tries to figure out the operation of the payload, and then calls the corresponding handle method for operation currently being handled.

response_payload str or SmogStruct: The response message, either the “raw” message body formatted according to the protocol of the client class (e.g. an xml message for the “plainxml” protocol), or an instance of the SmogStruct subclass that represents the input type of the operation.

response_headers dict: Dictionary of headers passed with the incoming response message.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;client-impl&gt; element.

return: None

raises: Any exception raised during handling of the given response payload.

handle_&lt;operation-name&gt;_response(response_payload, response_headers, &lt;runtime-parameters&gt;)

Method for handling an incoming response messages for a specific operation.

response_payload str or SmogStruct: The response message, either the “raw” message body formatted according to the protocol of the client class, or an instance of the SmogStruct subclass that represents the input type of the operation.

response_headers dict: Dictionary of headers passed with the incoming response message.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;client-impl&gt; element.

return: None

raises: Any exception raised during handling of the given response payload.

fault(response_payload, response_headers, exception, &lt;runtime-parameters&gt;)

Main method for handling errors raised outside of this handler. It is called by the runtime environment hosting the client, in order to generate an error message.
Calls the corresponding fault method for operation currently being handled.

response_payload str: The response body.

response_headers dict: Dictionary of headers passed with the incoming response message.

exception Exception: Exception to generate error message for.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;client-impl&gt; element.

return: None

fault_&lt;operation-name&gt;(response_payload, response_headers, exception, &lt;runtime-parameters&gt;)

Method for generating an fault message for a specific operation.

response_payload str: The request body.

response_headers dict: Dictionary of headers passed with the incoming response message.

exception Exception: Exception to generate error message for.

&lt;runtime-parameters&gt;: *args: Parameters specified in the &lt;runtime-parameters&gt; in the &lt;client-impl&gt; element.

return: None

pre_process(payload)

This is the main method for translating an incoming message. Any pre-processing steps (if specified) are executed first,
then the resulting payload is parsed into a SmogStruct representation (if not already done by the pre-processing) by calling
the parse(payload) method (see below).
If called in the context of error handling (i.e. when the exception property is set), it collects intermediate results
from each pre-processor that changes the payload. This can be used when generating error messages (see also service variable
‘fault_payloads’).

payload str: The payload to parse.

return: tuple of (SmogStruct, str or SmogStruct)

raises: ValueError If the payload cannot be used for creating a valid struct instance.

parse(payload)

Parses given payload and returns a struct instance populated with the values of the payload. The payload should be on the protocol associated with this client class.

payload str: The payload to parse.

return: SmogStruct

raises: ParseMsgError If the payload cannot be used for creating a valid struct instance.

format(struct, validate=True)

Formats the given struct for the protocol used by this client class.

struct SmogStruct: The struct instance to format.

validate bool: Whether the struct should be validated before being formatted.

return: str

raises: ValueError If the given struct cannot be formated on the protocol for this client class.

format_fault(struct, validate=True)

Formats the given struct as a fault for the protocol used by this client class.

struct SmogStruct: The struct instance to format.

validate bool: Whether the struct should be validated before being formatted.

return: str

raises: ValueError If the given struct cannot be formated on the protocol for this client class.

create_struct_&lt;operation-name&gt;(*args, **kwargs)

Creates SmogStruct instance that can be used as input for a specific operation.

return: SmogStruct

exception_context()

Returns contextual information from mapping method where self.exception was raised.
The returned information is formatted as JSON.

return: str

# 6. Customizing SMOG

By means of parameters -c and -d (see Using SMOG), it is possible to specify custom protocol and language packages in order to
customize protocol implementations or languages supported natively by SMOG, or to add support for other protocols and languages.
The following sections provide examples of how to do this. Note that this kind of customizations is not to be mixed up with extending or customizing
service specifications or service mappings as described in chapters Struct extensions, Service extensions and Mapping extensions.
Customizing SMOG itself is normlly not needed when working with service configurations and is therefore not considered normal usage.
Hence, the api:s described in this chapter should be seen as internal to SMOG and may change without notice.

## 6.1. Customizing Protocols

Each protocol natively supported by SMOG is implemented in a python module with the same name as the protocol, in package smog.&lt;smog version&gt;.protocols.
As an example, the soap protocol is implemented in $SMOG_HOME/python/smog/v2/protocols/soap.py for version 2 of SMOG.

In SMOG the class ProtocolMgr is responsible for reading the protocol specification, dynamically load the protocol modules needed and govern the generation of protocol artifacts.
By specifying parameter -c &lt;custom protocol package&gt; when running SMOG, the ProtocolMgr will first look for protocol implementations
in the &lt;custom protocol package&gt;. If a certain protocol implementation is found there, it will use that implementation instead of the one
in the native protocol package.

All protocol modules must implement a function with the following signature: (no particular return value is required):

    generate_protocol_artifacts(protocol_mgr, protocol_node)

,where protocol_mgr:  An instance of the ProtocolMgr
       protocol_node: A python data structure representing the &lt;protocol&gt; node
                      that specifies the protocol in the protocol specification.
                      See configreader module for more information about the
                      python data structure.

In order to generate protocol specific parts of the service implementation, the protocol module must also implement a function with the following signature:

    get_code_generator(protocol_mgr, protocol_node, language)

,where protocol_mgr:  see above
       protocol_node: see above
       language:      Target language for the generated service implementation
 The function should return an instance of a code generator class that implements the interface prescribed for the specified language (see TODO: add reference).

### 6.1.1. Customizing an existing Protocol implementation

In this example, the implementation of the plainxml protocol is changed such that all struct members are represented as xml elements
in the generated XSD.

- Store the following protocol specification as “protocol.xml”:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;protocol-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot; target=&quot;hello&quot;&gt;
   &lt;protocol name=&quot;plainxml&quot;/&gt;
&lt;/protocol-spec&gt;

- Store the following module as “plainxml.py” in a directory e.g. “my_protocol_cust” and make sure the directory contains a “__init__.py” and is included in the PYTHONPATH:

import smog.v2.protocols.plainxml

def generate_protocol_artifacts(mgr, protocol):
    &quot;&quot;&quot;
    Entry point for generation of protocol artifacts.

    @param mgr:           Protocol manager
    @type mgr:            artifactmanager.ProtocolMgr
    @param protocol:      A python data structure representing the &lt;protocol&gt; node that
                          specifies the crap protocol in the protocol specification.
                          See configreader module for more information about the
                          python data structure
    @type protocol:       dict wrapped as configreader.ConfigNode
    &quot;&quot;&quot;
    xsd = CustomXsdArtifact(mgr, protocol)
    xsd.generate()

class CustomXsdArtifact(smog.v2.protocols.plainxml.XsdArtifact):
    &quot;&quot;&quot;
    Custom implementation of plainxml that extends the native SMOG implementation.
    &quot;&quot;&quot;

    @staticmethod
    def is_xml_attribute(member):
        return False

Specify the custom protocol package with parameter -c when running SMOG:

&gt; smog -s &lt;service spec&gt; -p protocol.xml -c my_protocol_cust

### 6.1.2. Adding a new Protocol implementation

In this example, the implementation of a fictitious protocol foo is outlined. Artifacts for protocol foo should be generated alongside with artifacts for plainxml.

- Store the following protocol specification as “protocol.xml”:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;protocol-spec xmlns=&quot;http://namespace.jeppesen.com/smog/v2&quot;
               xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; target=&quot;my_target_env&quot;&gt;
    &lt;protocol name=&quot;plainxml&quot; /&gt;
    &lt;protocol name=&quot;foo&quot; param1=&quot;boo&quot; param2=&quot;koo&quot;&gt;
        &lt;artifact artifact_type=&quot;foo_manifest&quot;&gt;
            &lt;myconfig1&gt;spam&lt;/myconfig1&gt;
            &lt;myconfig2&gt;egg&lt;/myconfig2&gt;
        &lt;/artifact&gt;
    &lt;/protocol&gt;
&lt;/protocol-spec&gt;

- Store the following module as “foo.py” in a directory e.g. “my_protocol_cust” and make sure the directory contains a “__init__.py” and is included in the PYTHONPATH:

def generate_protocol_artifacts(mgr, protocol):
    &quot;&quot;&quot;
    Entry point for generation of protocol artifacts for the &quot;foo&quot; protocol.

    @param mgr:           Protocol manager
    @type mgr:            artifactmanager.ProtocolMgr
    @param protocol:      A python data structure representing the &lt;protocol&gt; node that
                          specifies the crap protocol in the protocol specification.
                          See configreader module for more information about the
                          python data structure
    @type protocol:       dict wrapped as configreader.ConfigNode
    &quot;&quot;&quot;

    for artifact in protocol.get_children(&#39;artifact&#39;):
        for service in mgr.sspec.get_services():
            output = &quot;#&quot; + mgr.get_docstring(service.getattr(&#39;name&#39;), service.getattr(&#39;version&#39;)) + &quot;\n&quot;
            output += &quot;FOO param1: %s\n&quot; % protocol.getattr(&#39;param1&#39;)
            # Read artifact configuration
            artifact_type = artifact.getattr(&#39;artifact_type&#39;)
            for config in artifact.get_children():
                output += &quot;%s=%s &quot; % (config.tag, config.text)
            output += &quot;\n&quot;

        for operation in service.get_children(&#39;operation&#39;):
            input_elem = operation.get_child(&#39;input&#39;)
            input_name = mgr.sspec.get_input_name(operation)
            output_elem = operation.get_child(&#39;output&#39;)
            output_name = mgr.sspec.get_output_name(operation)
            output += &quot;\tINPUT %s : \t OUTPUT %s\n&quot; % (input_name, output_name)

        # Store generated artifact
        target_fname = os.path.join(mgr.target_root_dir, mgr.target_dir, service.getattr(&#39;name&#39;) + &quot;_&quot; + service.getattr(&#39;version&#39;) + &quot;.foo&quot;)
        f = open(target_fname, &#39;w&#39;)
        f.write(output)
        f.close()

Specify the custom protocol package with parameter -c when running SMOG:

&gt; smog -s &lt;service spec&gt; -p protocol.xml -c my_protocol_cust

## 6.2. Customizing Languages

Mapping artifacts are based on the language specified by the language attribute in the service mapping, e.g. &lt;service-mapping language=&quot;Python&quot;&gt;.
The only language currently supported by SMOG is Python and it is implemented by python modules smog.&lt;smog version&gt;.languages.&lt;language&gt;_generator and smog.&lt;smog version&gt;.languages.&lt;language&gt;_templates,
where &lt;language&gt; is the name of the language. Hence, the Python language is implemented in $SMOG_HOME/python/smog/v2/language/python_generator.py and  $SMOG_HOME/python/smog/v2/language/python_templates.py for version 2 of SMOG.

In SMOG the class MappingMgr is responsible for reading the service mapping, dynamically loading the language modules needed and governing the generation of mapping artifacts.
The two modules mentioned above are required in the interface between the MappingMgr and the language implementation.
The native Python implementation also consists of an additional module smog.&lt;smog version&gt;.languages.python_struct which is used internally by smog.&lt;smog version&gt;.languages.&lt;language&gt;_generator but it is not known or used by the MappingMgr.

By specifying parameter -d &lt;custom language package&gt; when running SMOG, the MappingMgr will first look for language implementations in the &lt;custom language package&gt;.
If a certain language implementation is found there, it will use that implementation instead of the one in the native language package.

All smog.&lt;smog version&gt;.languages.&lt;language&gt;_generator modules must implement a function with the following signature:

    generate_mapping_artifacts(mapping_mgr)

where mapping_mgr: An instance of MappingMgr

The MappingMgr calls this function in order to generate mapping artifacts for all services in the given service specification.
The code generation is based on templates available in module smog.&lt;smog version&gt;.languages.&lt;language&gt;_templates.
The MappingMgr assigns the template module as member variable “template_module” and can then be used by the code generation through the MappingMgr instance passed in the call to generate_mapping_artifacts.
The MappingMgr itself doesn’t have any api requirements towards the template module.

Note that when it comes to serializing and de-serializing protocol specific messages, that part of the generated mapping artifact is unique to each protocol.
That means there is a part of the mapping that is both language- and protocol specific.
Therefore the protocol implementation must also implement an api for the code generation to use in order to generate those protocol specific parts.

In the Python implementation, the smog.&lt;smog version&gt;.languages.python_generator module expects the protocol implementation to contain a function “get_code_generator” as described in Customizing Protocols.
The function should return an instance of a code generator class that is a subclass of smog.&lt;smog version&gt;.languages.python_generator.CodeGenerator which has the following public api methods:

def get_module_initializations(self, service):
    &quot;&quot;&quot;
    Returns protocol specific module initializations for the generated service implementation python module

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python code to insert as module level initializations in the generated service module
    @rtype:          list of strings
    &quot;&quot;&quot;
    raise NotImplementedError(&quot;Must be implemented by subclass&quot;)

def get_class_initializations(self, service):
    &quot;&quot;&quot;
    Returns protocol specific service class initializations

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python code to insert as class level initializations in the generated service class for a specific protocol
    @rtype:          string
    &quot;&quot;&quot;
    raise NotImplementedError(&quot;Must be implemented by subclass&quot;)

def get_parse_method(self, service):
    &quot;&quot;&quot;
    Returns python source code for a method that parses a given payload on protocol specific format and returns a SmogStruct instance
    populated with the values of the payload. The generated method is pasted into the service class for a specific protocol and
    should have the following signature:

        def parse(self, payload)

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python source code
    @rtype:          string
    &quot;&quot;&quot;
    raise NotImplementedError(&quot;Must be implemented by subclass&quot;)

def get_format_method(self, service):
    &quot;&quot;&quot;
    Returns python source code for a method that formats a given SmogStruct instance into protocol specific format.
    The generated method is pasted into the service class for a specific protocol and should have the following signature:

        def format(self, struct, validate=True)

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python source code
    @rtype:          string
    &quot;&quot;&quot;
    raise NotImplementedError(&quot;Must be implemented by subclass&quot;)

def get_format_fault_method(self, service):
    &quot;&quot;&quot;
    Returns python source code for a method that formats a given SmogStruct instance into a fault message on protocol specific format.
    The generated method is pasted into the service class for a specific protocol and should have the following signature:

        def format_fault(self, struct, validate=True)

    @param service:  The service to generate implementation for
    @type service:   dict wrapped as configreader.ConfigNode
    @return:         Python source code
    @rtype:          string
    &quot;&quot;&quot;
    raise NotImplementedError(&quot;Must be implemented by subclass&quot;)

def get_parse_value_methods(self):
    &quot;&quot;&quot;
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
    &quot;&quot;&quot;
    raise NotImplementedError(&quot;Must be implemented by subclass&quot;)

def get_format_value_methods(self):
    &quot;&quot;&quot;
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
    &quot;&quot;&quot;
    raise NotImplementedError(&quot;Must be implemented by subclass&quot;)

### 6.2.1. Customizing Python mapping artifacts

In this example, the implementation of mapping artifact generation for the Python language is changed such that an additional Copyright notice is added in the beginning of all mapping artifacts.
Note that this kind of customization can be done solely by subclassing the template class, without actually customizing module smog.&lt;smog version&gt;.languages.python_generator itself.

- Make sure the service mapping specifies Python as language: &lt;service-mapping language=&quot;Python&quot;&gt;
- Store the following module as “python_templates.py” in a directory e.g. “my_language_cust” and make sure the directory contains a “__init__.py” and is included in the PYTHONPATH:

from smog.v2.languages.python_templates import PythonTemplate as PythonTemplateBase

class PythonTemplate(PythonTemplateBase):

    def __getattribute__(self, attr):
        prepend = &quot;&quot;
        if attr == &quot;HANDLER_MODULE_TEMPLATE&quot;:
            prepend = &quot;# Copyright: Tyrell Corporation 1982 \n&quot;
        return prepend + super(PythonTemplate, self).__getattribute__(attr)

Specify the custom language package with parameter -d when running SMOG:

&gt; smog -s &lt;service spec&gt; -p &lt;protocol spec&gt; -m &lt;service mapping&gt; -d my_language_cust
## Synchronize Data between Atrium systems


The purpose of this document is to describe the how to configure the syncadata feature in CMS.

* [1. Introduction](syncadata.html)
* [2. System overview](syncadata.html#system-overview)
* [3. Synchronization of ARA DomainObjects](syncadata.html#synchronization-of-ara-domainobjects)
* [4. Scope of synchronized data](syncadata.html#scope-of-synchronized-data)
* [5. Scenarios](syncadata.html#scenarios)
* [6. Jobrunner](syncadata.html#jobrunner)
  + [6.1. API for getting request messages](syncadata.html#api-for-getting-request-messages)
* [7. Configuration](syncadata.html#configuration)
  + [7.1. Data specification](syncadata.html#data-specification)
  + [7.2. Producer](syncadata.html#producer)
  + [7.3. Consumer](syncadata.html#consumer)
  + [7.4. Trigger](syncadata.html#trigger)
  + [7.5. Database tables](syncadata.html#database-tables)

#### Indices and tables

* [Index](../genindex.html)
* [Search Page](../search.html)

### Introduction

### System overview


The syncadata component provides two IOServices, `syncadata trigger` and `syncadata service`, that can be deployed
in Atrium systems. The `trigger` is responsible for identifying and acting when data changes in the
database and produce data messages for updated business objects. The `service` is responsible for consuming data
messages coming from other Atrium systems and update database accordingly.
The service can also be requested to produce and distribute data messages on demand.

![Components used by syncadata framework](../_images/syncadata_overview.png)

Data synchronization is automatically triggered from the Atrium system that owns (masters) the data
whenever the data is updated in the database. The `syncadata trigger` generates data messages for
the updated ARA objects and the generated data messages are distributed to other Atrium systems. The received data messages
are consumed by the `syncadata service` and updated in the database. Synchronization can also be initiated on
demand using Jobrunner, requesting the `syncadata service` to produce specific data messages,
for example all flight data for a certain date or period. The `syncadata service` can also be requested to produce
data messages for a specific scenario (instead from live plan).
Currently, the `syncadata trigger` should not be deployed in JCT since the current syncadata
version is limited to trigger synchronization from JOC to JCT.

The Atrium systems must be integrated in such way that messages produced on internal queues in one Atrium system
can be consumed from internal queues of other Atrium systems. This integration typically involves configuration
of Camel routes in the Integrator, but the actual details are airline specific and varies between deployment sites.

### Synchronization of ARA DomainObjects


Data messages used in synchronization contains json objects representing ARA DomainObject instances to synchronize.
The receiving system must match the received json objects with ARA DomainObject instances available in the data model
in order to find correct instance to update. Most DomainObjects can be identified through an id or a code for
the primary key. This applies to airports, carriers, delay codes and other DomainObjects with a natural primary key.

Matching of FlightLeg instances is primarily done using the external key (RowID) of the FlightLeg from the
sending system, as stored in UDM entity `flight_leg_ext_key` of the receiving system. In case the FlightLeg object
key is unknown (not in UDM entity `flight_leg_ext_key`), matching is done using the IATA flight leg key
(IdentifierDate, Carrier, FlightNumber, Suffix, StartStation).

Matched DomainObject instances are updated in the receiving systems to match the values of the received data.
New DomainObject instances are created if no existing instance could be matched. Single value attributes are
simply set to same value as the received data. Multi value attributes are set to contain the
same values as the received data, i.e. lists are applied as a complete state. Creation of new DomainObject
instances applies to all attribute values. This means that syncadata automatically creates e.g. airports
and other referenced DomainObjects whenever needed. It should be pointed out that if such object is
not covered by the synchronization of catalog data, syncadata merely populates the code that identifies the object
by its primary key to secure the referential integrity of the referencing (e.g. FlightLeg) object. In the example
of airports it means that other related information such as geographical or timezone data is not synchronized.

### Scope of synchronized data


A configuration file specifies what data to be synchronized. The configuration file, known as the *data specification*,
lists data types and attributes owned (mastered) per Atrium system.
The default data specification is available in `$CARMSYS/data/config/syncadata/version_1/dataspec.yml` and comprises
flight legs and associated return events as well as the following set of catalog data types:

* Aircraft

> * aircraft\_incidentlock - only the records associated with selected Aircraft(s)
> * aircraft\_period - always a full replacement for selected Aircraft(s)

* AircraftType
* aircraft\_body\_type
* aircraft\_engine\_type
* aircraft\_group
* Airline
* cancel\_code
* Country
* delay\_code
* diversion\_code
* pax\_category
* pax\_grouping
* seat\_configuration

> * seat\_config\_seat - only the records associated with selected seat\_configuration(s)
> * seat\_type - only the records associated with selected seat\_configuration(s)

* ServiceType

Note that since *aircraft\_period* records are updated as a state, i.e. any existing periods and their values are replaced,
any *aircraft\_period* custom extension attributes defined in JCT but not in JOC will be cleared when periods are synchronized.
It is therefore recommended that such attributes are defined in a separate database table.

The *data specification* lists the names of the involved Atrium systems (atrium-joc, atrium-joc) and denotes
the primitive data types of each attribute. The cardinality token `[]` denotes attributes as multi-valued.
The following primitive types exist:

* `String`
* `Integer`
* `Boolean`
* `AbsDate`
* `AbsTime`
* `RelTime`

Dot “.” notation is used to specify attributes further down in the model hierarchy e.g. `String AircraftAssignment.Resource.RegistrationNumber`
or `Integer delays[].seqno`. The leftmost part refer to an ARA attribute or reverse reference on the top level domain object,
e.g. `FlightLeg`.

See the current [default data specification](resources/version_1/dataspec.yml) for the exact scope of synchronized data.

### Scenarios


The `syncadata service` can be requested to produce data messages for a scenario or solution by sending the following
type of message to the service:

```
{
  "get_scenario": {
    "scenario_id": "<required-scenario-id>",
    "job_id": "<optional-job-id>",
    "option_id": "<optional-solution-id>",
    "name": "<optional-scenario-name>",
    "author": "<optional-scenario-author>",
    "description": "<optional-scenario-description>"
  }
}
```

The properties `job_id` and `option_id` are optional, but both should be specified if provided.

### Jobrunner

#### API for getting request messages

###### 6.1. API for getting request messages

The job definitions use an API provided by syncadata that contains convenience functions for creating synchronization request
messages. The API is available in module `jcms.syncadata.version_1.functions`:

```
def make_get_catalog_data_request():
```

Produces a request message to synchronize catalog data (see [Scope of synchronized data](#scope-of-synchronized-data) for details).

```
def make_get_FlightLeg_request(period_start=None, period_end=None, flights=None):
```

Produces a request message for synchronizing flight legs and associated return events, optionally specifying
a period and/or flight filters to restrict the selection of data to be synchronized.

> `period_start`: Restricts the selection of flight legs such that udor must be greater than or equal to period\_start.
> :   Type is AbsDate or string in AbsDate or ISO compatible format e.g. ‘8JUN2022’
>
> `period_end`: Restricts the selection of flight legs such that udor must be less than or equal to period\_end.
> :   Type is AbsDate or string in AbsDate or ISO compatible format e.g. ‘2022-06-08’
>
> `flights`: List of flight (leg) identifiers (see description below). Type is list of strings.

The flight filters is a list of flight or leg identifiers in the following format:

> `<carrier><number><suffix> <udor> <adep> <ades>` e.g. SK201 8JUN2022 GOT CPH

Note that udor, adep (departure airport) and ades (destination airport) are optional. If only one of adep/ades
is specified it is assumed to be adep. Udor is only used as filtering criterion if neither period\_start nor period\_end
is specified.

### Configuration

#### Data specification

###### 7.1. Data specification

A custom data specification is needed when synchronization should include additional information that might be
airline specific. The best approach is to use a copy of the default data specification `$CARMSYS/data/config/syncadata/version_1/dataspec.yml`
as starting point and add changes to it.

The custom data specification can be added in the configuration layer by either:

* Adding file `$CARMUSR/data/config/syncadata/dataspec.yml`
* Setting environment variable `SYNCADATA_CONFIG` to custom file location.

The updated custom data specification must be added to the configuration layer of both producing and consuming systems.
The syncadata component can automatically produce and consume the specified data types and attributes as long as
the data specifications correspond with the ARA attributes in the respective data models.
Hence it’s a good idea striving for having a one-to-one mapping between the data specification and the ARA data model.
However, it is possible to configure the [Producer](#producer) and [Consumer](#consumer) if data specification doesn’t correspond with the ARA data model.

The system is designed to be tolerant towards differences in data models between the producing and consuming systems, with the objective
to always synchronize as much as possible of a domain object and report any problems encountered. The consumer matches an incoming
synchronization message with the data specification and tries to synchronize all attributes provided in the message, for which there
exists a corresponding entry in the data specification.

Both the producer and consumer are fully configurable to handle both extensions to the data model and custom mapping logic. They are
based on a design where the handler falls back to a generic behavior in case no explicit override exists. For data model extensions
it means that in many cases it is enough to include the extensions in a custom data specification and rely on the generic mapping logic.
The following two sections describe how to configure custom overrides of the mapping logic, applied to attributes that exist in the
standard data model. However the principle is the same for defining custom mapping logic for model extensions.

#### Producer

###### 7.2. Producer

It’s possible to override and extend the default behavior when producing (sending) data messages.
This is done by implementing the Python class `Producer` in `$CARMUSR/lib/python/syncadata_ext/producer.py`.

The class should implement methods named:

```
def produce_<datatype>_<attribute>(self, obj, attr):
```

Where `<datatype>` and `<attribute>` matches the datatype and attribute names in the data specification, for example:

```
import jcms.syncadata.version_1.producer as producer_core
from RelTime import RelTime

class Producer(producer_core.Producer):

    def produce_FlightLeg_ScheduledOffblockTime(self, obj, attr):
        """
        Custom method for getting value for a primitive attribute of a DataType.

        @param obj: The DomainObject instance to get value for.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Full name of the attribute to get value from, for example "FlightLeg.ScheduledOffblockTime"
        @type attr: str
        @rtype: Type as specified for primitive attribute in data-spec.yml or None
        """
        self.logger.info(f"Producing custom {attr}.")
        return obj.ScheduledOffblockTime + RelTime("00:10")

    def produce_FlightLeg_DiversionStation(self, obj, attr):
        """
        Custom method for getting a complex attribute of a DataType.

        @param obj: The DomainObject to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Full name of the attribute to get value from, for example "FlightLeg.DiversionStation"
        @type attr: str
        @return: DomainObject instance as specified in data-spec.yml
        @rtype: jcms.ara.core.DomainObject or None
        """
        self.logger.info(f"Producing custom {attr}.")
        if obj.DiversionStation and obj.DiversionStation != obj.ScheduledEndStation:
            return obj.DiversionStation
        return None

    def produce_FlightLeg_delays(self, obj, attr):
        """
        Custom method for getting values for a complex list attribute of a DataType.

        @param obj: The DomainObject to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Full name of the attribute to get value from, for example "FlightLeg.delays[]"
        @type attr: str
        @return: DomainObject instances as specified in data-spec.yml
        @rtype: list of jcms.ara.core.DomainObject
        """
        self.logger.info(f"Producing custom {attr}.")
        return [d for d in obj.delays if d.duration >= RelTime("00:10")]
```

#### Consumer

###### 7.3. Consumer

It’s possible to override and extend the default behavior when consuming (receiving) data messages.
This is done by implementing the Python class `Consumer` in `$CARMUSR/lib/python/syncadata_ext/consumer.py`.

The class should implement methods named:

```
def consume_<datatype>_<attribute>(self, obj, attr, data):
```

Where `<datatype>` and `<attribute>` matches the datatype name attribute name in the data specification, for example:

```
import jcms.syncadata.version_1.consumer as consumer_core
import jcms.ara.air as ara_air


class Consumer(consumer_core.Consumer):

    def consume_FlightLeg_ScheduledOffblockTime(self, obj, attr, data):
        """
        Custom method for setting/updating a primitive attribute.

        @param obj: The DomainObject instance to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Name of the primitive attribute to set/update.
        @type attr: str
        @param data: The new value to set/update.
        @type data: str or None
        @rtype: None
        """
        sobt = consumer_core.abstime(data)
        if obj.getScheduledOffblockTime() != sobt:
            self.logger.info(f"{self.context} rescheduled with new STD {sobt}")
            obj.sobt = sobt
        else:
            self.logger.info(f"{self.context} STD not updated.")

    def consume_FlightLeg_DiversionStation(self, obj, attr, data):
        """
        Custom method for setting/updating a complex attribute.

        @param obj: The DomainObject instance to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Name of the complex attribute to set/update.
        @type attr: str
        @param data: Structure representing the DomainObject instance to to set/update.
        @type data: dict or None
        @rtype: None or jcms.ara.core.DomainObject
        """
        if data is None:
            return
        ap = ara_air.Airport.find(data['id'], self.plan) or ara_air.Airport.create(data['id'], self.plan)
        if obj.getDiversionStation() is None:
            self.logger.info(f"{self.context} diverted to {ap.getId()}.")
        else:
            self.logger.info(f"{self.context} diversion changed from {obj.getDiversionStation().getId()} to {ap.getId()}.")
        obj.setDiversionStation(ap)

    def consume_FlightLeg_delays(self, obj, attr, data_list):
        """
        Custom method for setting/updating a complex list attribute.

        @param obj: The DomainObject instance to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Full name of the list attribute to set/update, for example "FlightLeg.delays[]"
        @type attr: str
        @param data_list: List containing the structures representing the DomainObject instances to to set/update.
        @type data_list: list of dict
        """
        self.logger.info(f"Received {len(data_list)} delays for {self.context} from {self.data_source}.")
        if self.data_source == "atrium-joc":
            self.logger.info(f"Ignoring to update delays from atrium-joc.")
            return
        return super(Consumer, self).consume_child_objects(obj, attr, data_list)
```

#### Trigger

#### Database tables

###### 7.5. Database tables

UDM entity `flight_leg_ext_key` is used by the consumer to map the external keys (ROWID) of flight\_leg records with the corresponding
local flight\_leg record.

UDM entity `aircraft_ext_key` is used by the consumer to map the external keys (ROWID) of aircraft records with the corresponding
local aircraft record.

UDM entity `syncadata_parameter` is used on the producing side to coordinate between jobrunner sync jobs and the syncadata trigger, e.g.
to suppress trigger updates within an imported SSIM period while the synchronization job is active.

### Indices and tables
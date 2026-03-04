# Synchronize Data between Atrium systems

The purpose of this document is to describe the how to configure the syncadata feature in CMS.

1. Introduction
2. System overview
3. Synchronization of ARA DomainObjects
4. Scope of synchronized data
4.1. Sent from JOC
4.2. Sent from JCT

5. Scenarios
6. Jobrunner
6.1. API for getting request messages

7. Configuration
7.1. Data specification
7.2. Producer
7.3. Consumer
7.4. Trigger
7.5. Rave definitions
7.6. Database tables

## Indices and tables

- Index
- Search Page



--- SUBPAGE: syncadata.html ---

# 1. Introduction

Multiple Atrium systems cannot operate on information stored in the same database.
Instead each Atrium system is isolated using separate database. The syncadata component is
responsible for keeping data synchronized across Atrium systems deployed at the same site,
typically in airline operation centers where both Jeppesen OpsControl (JOC) and
Jeppesen Crew Tracking (JCT) are being used.

Not all data is synchronized across involved Atrium systems, only a subset of the information that
is owned (mastered) by one Atrium system is synchronized with other Atrium systems. For example,
JOC owns the flight and tail assignment information, while JCT owns the trip/paring and crew related
information.

The current version of syncadata is limited to synchronizing flight information and catalog data from JOC to JCT
and crew assignment data from JCT to JOC, see Scope of synchronized data for more details.

Data cannot be synchronized, or replicated, directly on database level since the involved Atrium systems
might have incompatible database schemas. Information is instead synchronized using data messages,
representing higher level ARA business objects, which can be mapped from/to the data model in respective Atrium system.

# 2. System overview

The syncadata component provides two IOServices, syncadata trigger and syncadata service, that can be deployed
in Atrium systems. The trigger is responsible for identifying and acting when data changes in the
database and produce data messages for updated business objects. The syncadata service is responsible for consuming data
messages coming from other Atrium systems and update database accordingly.
The service can also be requested to produce and distribute data messages on demand.

Data synchronization is automatically triggered from the Atrium system that owns (masters) the data
whenever the data is updated in the database. The syncadata trigger generates data messages for
the updated ARA objects and the generated data messages are distributed to other Atrium systems. The received data messages
are consumed by the syncadata service and updated in the database. Synchronization can also be initiated on
demand using Jobrunner, requesting the syncadata service to produce specific data messages,
for example all flight data for a certain date or period. The syncadata service can also be requested to produce
data messages for a specific scenario (instead from live plan).
Both the syncadata trigger and the syncadata service should be deployed in both JOC and JCT since data is
synchronized in both directions.

The Atrium systems must be integrated in such way that messages produced on internal queues in one Atrium system
can be consumed from internal queues of other Atrium systems. This integration typically involves configuration
of Camel routes in the Integrator, but the actual details are airline specific and varies between deployment sites.

# 3. Synchronization of ARA DomainObjects

Data messages used in synchronization contains json objects representing ARA DomainObject instances to synchronize.
The receiving system must match the received json objects with ARA DomainObject instances available in the data model
in order to find correct instance to update. Most DomainObjects can be identified through an id or a code for
the primary key. This applies to airports, carriers, delay codes and other DomainObjects with a natural primary key.

Matching of more complex business objects like flight legs, crew members and aircrafts is primarily done using the
external key (RowId) of the object from the source system that is master of the data. On the receiving system this
RowId is stored in a dedicated cross-reference table along with a reference to the corresponding business object in
the receiving system. This way, objects may change their business key in the source system but still being synchronized
correctly. UDM entities flight_leg_ext_key, aircraft_ext_key and crewmember_ext_key are examples of such
cross-reference tables. When an external RowId is unknown on the receiving side, e.g. due to a new FlightLeg object was
created in the source system, matching is done using the business key (i.e. in the case of flight leg the IATA leg key
consisting of IdentifierDate, Carrier, FlightNumber, Suffix and StartStation). If no match was found based on the
business key then a new object is created. Finally a new cross reference entry is created , e.g. in entity
flight_leg_ext_key. Note that the matching of FlightLegs using business key may be disabled in JCT by adding an
entry in table syncadata_parameter with typ=’allow_duplicate_keys_FlightLeg’ (case sensitive) and val=’true’.
This may be useful in cases where the IATA leg key is not unique in the JOC source system. In this case a new FlightLeg
object is created without attempting to match an existing leg by IATA leg key, if the existing leg has an associated ext_key.

Matched DomainObject instances are updated in the receiving systems to match the values of the received data.
New DomainObject instances are created based on the provided business keys and other properties if no existing instance
could be matched. Single value attributes are
simply set to same value as the received data. Multi value attributes are set to contain the
same values as the received data, i.e. lists are applied as a complete state. Creation of new DomainObject
instances applies to all attribute values. This means that syncadata automatically creates e.g. airports
and other referenced DomainObjects whenever needed. It should be pointed out that if such object is
not covered by the synchronization of catalog or resource data, syncadata merely populates the code that identifies the object
by its primary key to secure the referential integrity of the referencing (e.g. FlightLeg) object. In the example
of airports it means that other related information such as geographical or timezone data is not synchronized.

# 4. Scope of synchronized data

A configuration file specifies what data to be synchronized. The configuration file, known as the data specification,
lists data types and attributes owned (mastered) per Atrium system.
The default data specification is available in $CARMSYS/data/config/syncadata/version_1/dataspec.yml and comprises
flight legs, their associated return events and crew assignments as well as the following set of catalog and resource data
types:

## 4.1. Sent from JOC

- Aircraft
- aircraft_incidentlock - only the records associated with selected Aircraft(s)
- aircraft_period - always a full replacement for selected Aircraft(s)
- AircraftType
- aircraft_body_type
- aircraft_engine_type
- aircraft_group
- Airline
- cancel_code
- Country
- delay_code
- diversion_code
- pax_category
- pax_grouping
- seat_configuration
- seat_config_seat - only the records associated with selected seat_configuration(s)
- seat_type - only the records associated with selected seat_configuration(s)
- ServiceType

## 4.2. Sent from JCT

- Crewmember
- non_crew

Note that since aircraft_period records are updated as a state, i.e. any existing periods and their values are replaced,
any aircraft_period custom extension attributes defined in JCT but not in JOC will be cleared when periods are synchronized.
It is therefore recommended that such attributes are defined in a separate database table.

The data specification root level lists the names of the involved Atrium systems (atrium-joc, atrium-jct) and under each
one all data types to be sent from that system are specified. On the lowest level of this hierarchy are
the primitive attributes and their data types. The cardinality token [] denotes attributes as multi-valued.
The following primitive types exist:

- String
- Integer
- Boolean
- AbsDate
- AbsTime
- RelTime

Dot “.” notation is used to specify attributes further down in the model hierarchy e.g. String AircraftAssignment.Resource.RegistrationNumber
or Integer delays[].seqno. The leftmost part refer to an ARA attribute or reverse reference on the top level domain object,
e.g. FlightLeg.

There must be a clear ownership for all synchronized data. It is the sending (producing) system that is regarded as the master of the
top level data type. In the core setup of JCT and JOC for instance JOC is the master of FlightLeg and Aircraft whereas JCT is the
master of Crewmember and non_crew. Still it may be feasible to specify bi-directional synchronization of a data type if e.g. a certain
aspect of the business object is owned by the opposite system. A prime example of this is the FlightLeg data type under both ‘atrium-joc’
and ‘atrium-jct’ sections in the core data specification. In this case JOC is master of the FlightLeg object itself but JCT is setup
as master of the FlightLeg’s crew assignments. This is reflected by the way the FlightLeg data type is specified under the respective
system’s section in the data specification, and the diffence in how FlightLeg objects are handled by the Consumer in each system.

See the current default data specification for the exact scope of synchronized data.

# 5. Scenarios

The syncadata service can be requested to produce data messages for a scenario or solution by sending the following
type of message to the service:

{
  &quot;get_scenario&quot;: {
    &quot;scenario_id&quot;: &quot;&lt;required-scenario-id&gt;&quot;,
    &quot;job_id&quot;: &quot;&lt;optional-job-id&gt;&quot;,
    &quot;option_id&quot;: &quot;&lt;optional-solution-id&gt;&quot;,
    &quot;name&quot;: &quot;&lt;optional-scenario-name&gt;&quot;,
    &quot;author&quot;: &quot;&lt;optional-scenario-author&gt;&quot;,
    &quot;description&quot;: &quot;&lt;optional-scenario-description&gt;&quot;
  }
}

The properties job_id and option_id are optional, but both should be specified if provided.

The scenario server URL can be set by environment variable SCENARIO_SERVER_URL.

# 6. Jobrunner

Syncadata is designed to work together with the Jobrunner component. This allows for scheduling and running synchronization
jobs on demand. The syncadata service automatically reports progress/status of jobs to the local Jobrunner when messages
contain the specific message header jcms_job_id.

The Jobrunner job definition must be configured for each synchronization job, see the Jobrunner documentation
for more information.

The sequence diagram below illustrates a configuration setup to provide synchronization feedback when initiating a
synchronization job through TIC.

## 6.1. API for getting request messages

The job definitions use an API provided by syncadata that contains convenience functions for creating synchronization request
messages. The API is available in module jcms.syncadata.version_1.functions:

def make_get_catalog_data_request():

Produces a request message to synchronize catalog data (see Scope of synchronized data for details).

def make_get_FlightLeg_request(period_start=None, period_end=None, flights=None):

Produces a request message for synchronizing flight legs and associated return events, optionally specifying
a period and/or flight filters to restrict the selection of data to be synchronized.

period_start:Restricts the selection of flight legs such that udor must be greater than or equal to period_start.
Type is AbsDate or string in AbsDate or ISO compatible format e.g. ‘8JUN2022’

period_end:Restricts the selection of flight legs such that udor must be less than or equal to period_end.
Type is AbsDate or string in AbsDate or ISO compatible format e.g. ‘2022-06-08’

flights:List of flight (leg) identifiers (see description below). Type is list of strings.

The flight filters is a list of flight or leg identifiers in the following format:

&lt;carrier&gt;&lt;number&gt;&lt;suffix&gt; &lt;udor&gt; &lt;adep&gt; &lt;ades&gt;  e.g. SK201 8JUN2022 GOT CPH

Note that udor, adep (departure airport) and ades (destination airport) are optional. If only one of adep/ades
is specified it is assumed to be adep. Udor is only used as filtering criterion if neither period_start nor period_end
is specified.

def make_block_updates_FlightLeg_request(start_date, end_date):

Produces a request message for blocking sync updates for flight legs within a given period. Flight legs with
Identifier Date (udor) within the period (including the start and end dates) are blocked for update.

start_date: Start of period for blocking updates..Type is AbsDate or string in AbsDate or ISO compatible format e.g. ‘8JUN2022’

end_date:   End of period for blocking updates.Type is AbsDate or string in AbsDate or ISO compatible format e.g. ‘2022-06-08’

def make_unblock_updates_FlightLeg_request():

Produces a request message for unblocking sync updates for flight legs.

# 7. Configuration

The syncadata IOServices must be configured to be activated in the configuration layer of each Atrium
system where they should be deployed.

Queues used by syncadata IOServices are configured by adding following to file $CARMUSR/etc/ccf.xml.

&lt;include href=&quot;${CARMSYS}/etc/ccf/syncadata.xml&quot;&gt;

The syncadata service is activated by adding following to file $CARMUSR/etc/programs/ioserver_batch.xml.

&lt;include href=&quot;${CARMSYS}/etc/service_template/syncadata/version_1/syncadata.xml&quot;&gt;

The syncadata trigger is activated by adding following to file $CARMUSR/etc/programs/ioserver_single1.xml.

&lt;include href=&quot;${CARMSYS}/etc/service_template/syncadata/version_1/syncadata_trigger.xml&quot; /&gt;

As indicated by the paths above, the version of the imported IOService configuration controls which version of syncadata is used.
It is important that both producing and consuming systems run the same version of syncadata.

## 7.1. Data specification

A custom data specification is needed when synchronization should include additional information that might be
airline specific. The best approach is to use a copy of the default data specification $CARMSYS/data/config/syncadata/version_1/dataspec.yml
as starting point and add changes to it.

The custom data specification can be added in the configuration layer by either:

- Adding file $CARMUSR/data/config/syncadata/dataspec.yml
- Setting environment variable SYNCADATA_CONFIG to custom file location.

The updated custom data specification must be added to the configuration layer of both producing and consuming systems.
The syncadata component can automatically produce and consume the specified data types and attributes as long as
the data specifications correspond with the ARA attributes in the respective data models.
Hence it’s a good idea striving for having a one-to-one mapping between the data specification and the ARA data model.
However, it is possible to configure the Producer and Consumer if data specification doesn’t correspond with the ARA data model.

The system is designed to be tolerant towards differences in data models between the producing and consuming systems, with the objective
to always synchronize as much as possible of a domain object and report any problems encountered. The consumer matches an incoming
synchronization message with the data specification and tries to synchronize all attributes provided in the message, for which there
exists a corresponding entry in the data specification.

Both the producer and consumer are fully configurable to handle both extensions to the data model and custom mapping logic. They are
based on a design where the handler falls back to a generic behavior in case no explicit override exists. For data model extensions
it means that in many cases it is enough to include the extensions in a custom data specification and rely on the generic mapping logic.
The following two sections describe how to configure custom overrides of the mapping logic, applied to attributes that exist in the
standard data model. However the principle is the same for defining custom mapping logic for model extensions.

## 7.2. Producer

It’s possible to override and extend the default behavior when producing (sending) data messages.
This is done by implementing the Python class Producer in $CARMUSR/lib/python/syncadata_ext/producer.py.

The class should implement methods named:

def produce_&lt;datatype&gt;_&lt;attribute&gt;(self, obj, attr):

Where &lt;datatype&gt; and &lt;attribute&gt; matches the datatype and attribute names in the data specification, for example:

import jcms.syncadata.version_1.producer as producer_core
from RelTime import RelTime

class Producer(producer_core.Producer):

    def produce_FlightLeg_ScheduledOffblockTime(self, obj, attr):
        &quot;&quot;&quot;
        Custom method for getting value for a primitive attribute of a DataType.

        @param obj: The DomainObject instance to get value for.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Full name of the attribute to get value from, for example &quot;FlightLeg.ScheduledOffblockTime&quot;
        @type attr: str
        @rtype: Type as specified for primitive attribute in data-spec.yml or None
        &quot;&quot;&quot;
        self.logger.info(f&quot;Producing custom {attr}.&quot;)
        return obj.ScheduledOffblockTime + RelTime(&quot;00:10&quot;)

    def produce_FlightLeg_DiversionStation(self, obj, attr):
        &quot;&quot;&quot;
        Custom method for getting a complex attribute of a DataType.

        @param obj: The DomainObject to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Full name of the attribute to get value from, for example &quot;FlightLeg.DiversionStation&quot;
        @type attr: str
        @return: DomainObject instance as specified in data-spec.yml
        @rtype: jcms.ara.core.DomainObject or None
        &quot;&quot;&quot;
        self.logger.info(f&quot;Producing custom {attr}.&quot;)
        if obj.DiversionStation and obj.DiversionStation != obj.ScheduledEndStation:
            return obj.DiversionStation
        return None

    def produce_FlightLeg_delays(self, obj, attr):
        &quot;&quot;&quot;
        Custom method for getting values for a complex list attribute of a DataType.

        @param obj: The DomainObject to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Full name of the attribute to get value from, for example &quot;FlightLeg.delays[]&quot;
        @type attr: str
        @return: DomainObject instances as specified in data-spec.yml
        @rtype: list of jcms.ara.core.DomainObject
        &quot;&quot;&quot;
        self.logger.info(f&quot;Producing custom {attr}.&quot;)
        return [d for d in obj.delays if d.duration &gt;= RelTime(&quot;00:10&quot;)]

## 7.3. Consumer

It’s possible to override and extend the default behavior when consuming (receiving) data messages.
This is done by implementing the Python class Consumer in $CARMUSR/lib/python/syncadata_ext/consumer.py.

The class should implement methods named:

def consume_&lt;datatype&gt;_&lt;attribute&gt;(self, obj, attr, data):

Where &lt;datatype&gt; and &lt;attribute&gt; matches the datatype name attribute name in the data specification, for example:

import jcms.syncadata.version_1.consumer as consumer_core
import jcms.ara.core as ara_core

class Consumer(consumer_core.Consumer):

    def consume_FlightLeg_ScheduledOffblockTime(self, obj, attr, data):
        &quot;&quot;&quot;
        Custom method for setting/updating a primitive attribute.

        @param obj: The DomainObject instance to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Name of the primitive attribute to set/update.
        @type attr: str
        @param data: The new value to set/update.
        @type data: str or None
        @rtype: None
        &quot;&quot;&quot;
        sobt = consumer_core.abstime(data)
        if obj.getScheduledOffblockTime() != sobt:
            self.logger.info(f&quot;{self.context} rescheduled with new STD {sobt}&quot;)
            obj.sobt = sobt
        else:
            self.logger.info(f&quot;{self.context} STD not updated.&quot;)

    def consume_FlightLeg_DiversionStation(self, obj, attr, data):
        &quot;&quot;&quot;
        Custom method for setting/updating a complex attribute.

        @param obj: The DomainObject instance to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Name of the complex attribute to set/update.
        @type attr: str
        @param data: Structure representing the DomainObject instance to to set/update.
        @type data: dict or None
        @rtype: None or jcms.ara.core.DomainObject
        &quot;&quot;&quot;
        if data is None:
            return
        ap = ara_core.Airport.find(data[&#39;id&#39;], self.plan) or ara_core.Airport.create(data[&#39;id&#39;], self.plan)
        if obj.getDiversionStation() is None:
            self.logger.info(f&quot;{self.context} diverted to {ap.getId()}.&quot;)
        else:
            self.logger.info(f&quot;{self.context} diversion changed from {obj.getDiversionStation().getId()} to {ap.getId()}.&quot;)
        obj.setDiversionStation(ap)

    def consume_FlightLeg_delays(self, obj, attr, data_list):
        &quot;&quot;&quot;
        Custom method for setting/updating a complex list attribute.

        @param obj: The DomainObject instance to update.
        @type obj: jcms.ara.core.DomainObject
        @param attr: Full name of the list attribute to set/update, for example &quot;FlightLeg.delays[]&quot;
        @type attr: str
        @param data_list: List containing the structures representing the DomainObject instances to to set/update.
        @type data_list: list of dict
        &quot;&quot;&quot;
        self.logger.info(f&quot;Received {len(data_list)} delays for {self.context} from {self.data_source}.&quot;)
        if self.data_source == &quot;atrium-joc&quot;:
            self.logger.info(f&quot;Ignoring to update delays from atrium-joc.&quot;)
            return
        return super(Consumer, self).consume_child_objects(obj, attr, data_list)

If the consumption of a data type should differ between systems, it is possible to implement system-specific
override methods using the following syntax:

def consume_&lt;datatype&gt;_&lt;attribute&gt;_from_&lt;system&gt;(self, obj, attr, data):

, where &lt;system&gt; is the last part of the system name e.g. “JOC” for “atrium-joc” or “JCT” for “atrium-jct”:

def consume_FlightLeg_from_JCT(self, obj, datatype, data):
       leg = self.lookup_FlightLeg_JOC(data)
       self.consume_FlightLeg_CrewAssignments(leg, &quot;FlightLeg.CrewAssignments[]&quot;, data.get(&#39;CrewAssignments&#39;, []))
       self.consume_child_objects(leg, &quot;FlightLeg.non_crew_flight_asmts[]&quot;, data.get(&#39;non_crew_flight_asmts&#39;, []))
       self.consume_child_objects(leg, &quot;FlightLeg.nextleg_crew_conns[]&quot;, data.get(&#39;nextleg_crew_conns&#39;, []))

System-specific overrides take precedence over ordinary overrides.

## 7.4. Trigger

It’s possible to override and extend the default syncadata trigger to detect additional changes in the data model.
This might be needed if a custom data specification is used since the core trigger doesn’t know that it must also look
for changes to custom tables.

Using a custom trigger by implementing the Python class Trigger in $CARMUSR/lib/python/syncadata_ext/trigger.py.

The class should override the method named:

def find_changed_objects(self, changeset):

The method typically calls same method of the super class for getting changed objects from core trigger
and then call additional custom methods for finding additional objects that should be synchronized, for example:

import jcms.syncadata.version_1.trigger as trigger_core
import carmensystems.mave2.core as mave

class Trigger(trigger_core.Trigger):

    def find_changed_objects(self, changeset):
        &quot;&quot;&quot;
        Custom extension of trigger.
        &quot;&quot;&quot;
        # get changed objects from core trigger
        objs = super(Trigger, self).find_changed_objects(changeset)
        # extend changed objects in custom tables
        objs = objs.union(self.find_legs_changed_delay_lock(changeset))
        return objs

    def find_legs_changed_delay_lock(self, changeset):
        &quot;&quot;&quot;
        Find flight legs where table flight_delay_lock was changed.
        &quot;&quot;&quot;
        self.logger.info(f&quot;Triggering on custom table flight_delay_lock.&quot;)
        legs = set()
        for change in changeset.getCollectionChangeSet(&quot;flight_delay_lock&quot;):
            try:
                if change.isErased():
                    leg = self.plan.fromTuple(change.getPrevious().getTuple(&quot;leg&quot;))
                else:
                    leg = self.plan.fromTuple(change.getCurrent().getTuple(&quot;leg&quot;))
                if leg is None or leg.TaskNumber != 0:
                    continue
                legs.add(leg)
            except mave.DanglingReference as dr:
                self.logger.error(&quot;Dangling reference found, skipping processing change: %s&quot; % dr)
        return legs

## 7.5. Rave definitions

On JCT, the Producer uses the following Rave variables defined in the CARMSYS:

- syncadata_core.%from_jct_crew_min_connection_time%: Defines the minimum crew connection time for aircraft change following a leg
- syncadata_core.%from_jct_flight_crew_competences%: Defines a comma separated list of crew competence identities associated with a leg

## 7.6. Database tables

UDM entity flight_leg_ext_key is used by the consumer to map the external keys (RowId) of flight_leg records with the corresponding
local flight_leg record.

UDM entity aircraft_ext_key is used by the consumer to map the external keys (RowId) of aircraft records with the corresponding
local aircraft record.

UDM entity crewmember_ext_key is used by the consumer to map the external keys (RowId) of crewmember records with the corresponding
local crewmember record.

UDM entity non_crew_ext_key is used by the consumer to map the external keys (RowId) of non_crew records with the corresponding
local non_crew record.

UDM entity syncadata_parameter is used for controlling the behavior of the syncadata application. The following keys are recognized by the core syncadata application:

allow_duplicate_keys_FlightLeg - The presence of such an entry with val equal to true will cause syncadata to only match FlightLeg objects in JCT by their ext_key. However existing legs without any associated ext_key may also be matched by IATA leg key, if any.
block_updates_FlightLeg - used by the application to keep track of periods of blocking consumption of FlightLeg updates
block_trigger_FlightLeg - used by the application to keep track of periods of blocking trigger from producing FlightLeg updates
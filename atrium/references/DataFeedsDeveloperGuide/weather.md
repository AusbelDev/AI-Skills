# Jeppesen Weather Service

The purpose of this document is to describe the JCMS service for retrieving weather data from Jeppesen Weather Service.

1. Introduction
2. Design overview
3. Configuration
3.1. Sysmond
3.2. Environment
3.3. Customization

4. Admin API

## Indices and tables

- Index
- Search Page



--- SUBPAGE: pohlman.html ---

# 1. Introduction

Accurate and up-to-date weather observations and forecasts are needed in order to alert JOC operators about upcoming
issues with e.g. low visibility or strong crosswinds. There exists widely spread and commonly known standard formats
within the airline industry for weather observations (METAR) and weather forecasts (TAF).
The Jeppesen Weather Service (HWS) provides observations and forecasts on a request/response basis on the standard
formats as well as a structured JSON representation of the same data.

The pohlman component runs as a service in JCMS, responsible for retrieving relevant weather data from HWS and
store it in the UDM data model. The pohlman service runs autonomously in the background and needs no interaction
with a user. It determines relevant airports of interest for which it retrieves weather data, based on which flights
are currently in the operating time window. In addition to departure, arrival and any diversion airports, it also
takes alternate airports as defined by the flight plan into consideration (if available).

# 2. Design overview

Pohlman is a component of its own and does not belong to the Standard Interfaces component. The process runs
stand-alone on an SPS (or INFRA) node in a JCMS system, not in the context of an IOServer. It reaches out to the HWS
with http requests directly, bypassing the Integrator component which normally acts as endpoint to interfaces
communicating with external systems. Because of this design there are no Camel routes nor any internal ActiveMQ
queues needed by the component.
Pohlman only operates on a portion of the UDM data model limited by flight legs, airports, flight plans and the
weather related entities themselves. Furthermore it is the only source of weather data in JCMS, the other parts of
the data model (flight legs, flight plans etc.) is only used for reading. In order to make efficient use of system
resources, rather than defining a limited data context to load an ARA plan, it uses Dave directly to access the UDM
data model.

The interval pohlman requests latest weather data from HWS is by default each minute for observations and
each five minutes for forecasts. The pohlman
process is however resident once started (i.e. it is not cyclically activated by sysmond or any other scheduling
mechanism), making it all the time available from the cmsshell based admin API (see Admin API).

Each time the process activates for a new request to HWS, it evaluates the airports of interest based on all
operating flight legs with a scheduled off-block time within the current operating time window (from 24h before
until 48h after now time by default). Simulated time is used if a time server is running in the JCMS system. Before
each processing cycle, the airport data is also retrieved fresh from the data model in order to account for any new
airports being introduced in JCMS. Since the HWS service is based on ICAO airport codes it is essential that
airports in the UDM data model have the ‘icao’ column specified, regardless if the airport key scheme is based on
IATA or ICAO codes.

In addition to the production HWS service, there exists a mock HWS service which pohlman normally uses when
running in a test environment such as Confbox. Which HWS instance to use is part of the system configuration
(see Configuration). The mock HWS service is not part of the pohlman component itself but is
hosted by a separate component hws-mock.

# 3. Configuration

The pohlman service must be configured to be activated in the configuration layer of each Atrium
system where it should be deployed.

## 3.1. Sysmond

Sysmond is used to start, stop and supervise the pohlman process.
Add the following element to CARMUSR/etc/programs/sysmond/*.xml (either SPS or INFRA node):

&lt;start&gt;pohlman&lt;/start&gt;

The process should only start on one of the available nodes.

## 3.2. Environment

Add the following variables to Atrium system environment.yml:

- fedproxy_auth_url: FedProxy client authentication endpoint for requesting Authorization Code (AC).
- fedproxy_token_url: FedProxy client authentication endpoint for getting Access Token (AT).
- hws_api_url: Base url to the HWS web API.
- hws_client_cert_path: Client’s X.509 certificate (.pem file) for HWS as registered in FedProxy authentication.
- hws_client_id: OAuth Client ID for HWS as registered in FedProxy authentication.

For the mock HWS and the live HWS service instances respectively, the following values apply:

Parameter

Mock HWS

HWS UAT (Use Acceptance Test)

HWS Production

fedproxy_auth_url

[https://hws-mock-auth.service.cloud.jeppesensystems.com/auth](https://hws-mock-auth.service.cloud.jeppesensystems.com/auth)

[https://proxy-mtls.uat.boeingservices.com/as/authorization.oauth2](https://proxy-mtls.uat.boeingservices.com/as/authorization.oauth2)

[https://proxy-mtls.boeingservices.com/as/authorization.oauth2](https://proxy-mtls.boeingservices.com/as/authorization.oauth2)

fedproxy_token_url

[https://hws-mock.service.cloud.jeppesensystems.com/token](https://hws-mock.service.cloud.jeppesensystems.com/token)

[https://proxy-mtls.uat.boeingservices.com/as/token.oauth2](https://proxy-mtls.uat.boeingservices.com/as/token.oauth2)

[https://proxy-mtls.boeingservices.com/as/token.oauth2](https://proxy-mtls.boeingservices.com/as/token.oauth2)

hws_api_url

[https://hws-mock.service.cloud.jeppesensystems.com](https://hws-mock.service.cloud.jeppesensystems.com)

[https://hws.uat.jhwc.boeingservices.com:443](https://hws.uat.jhwc.boeingservices.com:443)

[https://hws.jhwc.boeingservices.com:443](https://hws.jhwc.boeingservices.com:443)

hws_client_cert_path

/etc/jeppesen/files/hws-mock-client.pem

/etc/jeppesen/files/hws-uat-client.pem

/etc/jeppesen/files/weather-&lt;name&gt;-client-prod.pem

hws_client_id

mock-test

Wx-JOC-Client-Uat

Wx-&lt;name&gt;-Client-Prod

The client certificate for mock HWS can be downloaded [here](https://git.got.jeppesensystems.com/TD/IO/hws-mock/-/raw/main/hws-mock-client.pem?inline=false).

For other production and test instances please refer to [FedProxy Endpoint Configurations](https://confluence.digitalaviationservices.com/display/CES/FedProxy+Endpoint+Configurations).

For information on acquiring a client certificate please refer to [https://confluence.digitalaviationservices.com/display/CES/FedProxy+Endpoint+Configurations](https://confluence.digitalaviationservices.com/display/CES/FedProxy+Endpoint+Configurations).

## 3.3. Customization

The following parameters can be provided when starting the pohlman service:

Param

Name

Description

Default value

-i

interval_secs_metar

Interval in seconds between calls to HWS for getting
latest METAR information.

60

-k

interval_secs_taf

Interval in seconds between calls to HWS for getting
latest TAF information.

300

-l

long_taf_threshold

Long TAF threshold in hours to classify if TAF is long or short.

16

-f

hours_before

Number of hours before now time, defining the start of the current
time window relevant for retrieving weather data

24

-e

hours_after

Number of hours after now time, defining the end of the current
time window relevant for retrieving weather data

48

-a

extra_airports

Optional comma-separated list of ICAO airport codes to complement
the airports derived from flight data

-c

dbconn_str

Database connection string

provided by xmlconfig

-d

client_id

OAuth Client ID for HWS as registered in FedProxy authentication

passed from environment.yml

-r

cert_path

Client’s X.509 certificate (.pem file) for HWS as registered
in FedProxy authentication

passed from environment.yml

-o

auth_url

FedProxy client authentication endpoint for requesting
Authorization Code (AC)

passed from environment.yml

-t

token_url

FedProxy client authentication endpoint for getting
Access Token (AT)

passed from environment.yml

-u

api_url

Base url to the HWS web API

passed from environment.yml

-p

port

port to use for http admin api, uses any available port number if
not specified

allocated by Sysmond

-v

verify_server_cert

Disable verification of server certificate (trust any).
Should only be specified for testing.

True (= verify)

In order to override any of the parameters, add a file CARMUSR/etc/programs/pohlman.xml and copy and adapt the content from
CARMSYS/etc/config.d/programs.d/pohlman.xml.

Then add the following element to CARMUSR/etc/programs/programs.xml:

&lt;include href=&quot;${CARMUSR}/etc/programs/pohlman.xml&quot; /&gt;

# 4. Admin API

An admin API for pohlman is available in cmsshell. It is only accessible on the node where the pohlman process is running.
The communication between cmsshell and pohlman takes place over http on a port that is by default dynamically allocated by Sysmond.

The following commands are available:

- url - Prints the url to the admin api.
- info - Prints metrics and other information about the running pohlman service.
- selftest - Verifies that pohlman can communicate with the HWS service and that it can access the database.
- airports - Lists the current airports of interest (ICAO codes and names) for which weather data is retrieved.
- extra_airports [&lt;airports&gt;] - Set extra airports to request weather data from (in addition to those derived from flight data). Parameter &lt;airports&gt; is a comma-separated list of airport ICAO codes. If omitted, the extra airports currently in effect are printed.
- metar &lt;airport&gt; - Requests weather observation for an airport and prints the result. Parameter &lt;airport&gt; is an ICAO airport code.
- taf &lt;airport&gt; - Requests weather forecast for an airport and prints the result. Parameter &lt;airport&gt; is an ICAO airport code.
- force_run - Retrieves and stores weather observations and forecasts based on current airports of interest, and prints immediate feedback.
- stop - Stop the service. Note that if pohlman is started by sysmond, sysmond will start the process again.
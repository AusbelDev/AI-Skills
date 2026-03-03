## Jeppesen Weather Service


The purpose of this document is to describe the JCMS service for retrieving weather data from Jeppesen Weather Service.

* [1. Introduction](pohlman.html)
* [2. Design overview](pohlman.html#design-overview)
* [3. Configuration](pohlman.html#configuration)
  + [3.1. Sysmond](pohlman.html#sysmond)
  + [3.2. Environment](pohlman.html#environment)
  + [3.3. Customization](pohlman.html#customization)
* [4. Admin API](pohlman.html#admin-api)

#### Indices and tables

* [Index](../genindex.html)
* [Search Page](../search.html)

### Introduction

### Design overview

### Configuration

#### Sysmond

###### 3.1. Sysmond

Sysmond is used to start, stop and supervise the `pohlman` process.
Add the following element to `CARMUSR/etc/programs/sysmond/*.xml` (either SPS or INFRA node):

```
<start>pohlman</start>
```

The process should only start on one of the available nodes.

#### Environment

###### 3.2. Environment

Add the following variables to Atrium system `environment.yml`:

* `fedproxy_auth_url`: FedProxy client authentication endpoint for requesting Authorization Code (AC).
* `fedproxy_token_url`: FedProxy client authentication endpoint for getting Access Token (AT).
* `hws_api_url`: Base url to the HWS web API.
* `hws_client_cert_path`: Client’s X.509 certificate (.pem file) for HWS as registered in FedProxy authentication.
* `hws_client_id`: OAuth Client ID for HWS as registered in FedProxy authentication.

For the mock HWS and the live HWS service instances respectively, the following values apply:

| Parameter | Mock HWS | HWS UAT (Use Acceptance Test) | HWS Production |
| --- | --- | --- | --- |
| fedproxy\_auth\_url | <https://hws-mock-auth.service.cloud.jeppesensystems.com/auth> | <https://proxy-mtls.uat.boeingservices.com/as/authorization.oauth2> | <https://proxy-mtls.boeingservices.com/as/authorization.oauth2> |
| fedproxy\_token\_url | <https://hws-mock.service.cloud.jeppesensystems.com/token> | <https://proxy-mtls.uat.boeingservices.com/as/token.oauth2> | <https://proxy-mtls.boeingservices.com/as/token.oauth2> |
| hws\_api\_url | <https://hws-mock.service.cloud.jeppesensystems.com> | <https://hws.uat.jhwc.boeingservices.com:443> | <https://hws.jhwc.boeingservices.com:443> |
| hws\_client\_cert\_path | /etc/jeppesen/files/hws-mock-client.pem | /etc/jeppesen/files/hws-uat-client.pem | /etc/jeppesen/files/weather-<name>-client-prod.pem |
| hws\_client\_id | mock-test | Wx-JOC-Client-Uat | Wx-<name>-Client-Prod |

The client certificate for mock HWS can be downloaded [here](https://git.got.jeppesensystems.com/TD/IO/hws-mock/-/raw/main/hws-mock-client.pem?inline=false).

For other production and test instances please refer to [FedProxy Endpoint Configurations](https://confluence.digitalaviationservices.com/display/CES/FedProxy+Endpoint+Configurations).

For information on acquiring a client certificate please refer to <https://confluence.digitalaviationservices.com/display/CES/FedProxy+Endpoint+Configurations>.

#### Customization

###### 3.3. Customization

The following parameters can be provided when starting the `pohlman` service:

| Param | Name | Description | Default value |
| --- | --- | --- | --- |
| -i | interval\_secs\_metar | Interval in seconds between calls to HWS for getting latest METAR information. | 60 |
| -k | interval\_secs\_taf | Interval in seconds between calls to HWS for getting latest TAF information. | 300 |
| -l | long\_taf\_threshold | Long TAF threshold in hours to classify if TAF is long or short. | 16 |
| -f | hours\_before | Number of hours before now time, defining the start of the current time window relevant for retrieving weather data | 24 |
| -e | hours\_after | Number of hours after now time, defining the end of the current time window relevant for retrieving weather data | 48 |
| -a | extra\_airports | Optional comma-separated list of ICAO airport codes to complement the airports derived from flight data |  |
| -c | dbconn\_str | Database connection string | provided by xmlconfig |
| -d | client\_id | OAuth Client ID for HWS as registered in FedProxy authentication | passed from environment.yml |
| -r | cert\_path | Client’s X.509 certificate (.pem file) for HWS as registered in FedProxy authentication | passed from environment.yml |
| -o | auth\_url | FedProxy client authentication endpoint for requesting Authorization Code (AC) | passed from environment.yml |
| -t | token\_url | FedProxy client authentication endpoint for getting Access Token (AT) | passed from environment.yml |
| -u | api\_url | Base url to the HWS web API | passed from environment.yml |
| -p | port | port to use for http admin api, uses any available port number if not specified | allocated by Sysmond |
| -v | verify\_server\_cert | Disable verification of server certificate (trust any). Should only be specified for testing. | True (= verify) |

In order to override any of the parameters, add a file `CARMUSR/etc/programs/pohlman.xml` and copy and adapt the content from
`CARMSYS/etc/config.d/programs.d/pohlman.xml`.

Then add the following element to `CARMUSR/etc/programs/programs.xml`:

```
<include href="${CARMUSR}/etc/programs/pohlman.xml" />
```

### Admin API


An admin API for `pohlman` is available in cmsshell. It is only accessible on the node where the `pohlman` process is running.
The communication between cmsshell and `pohlman` takes place over http on a port that is by default dynamically allocated by Sysmond.

The following commands are available:

* **url** - Prints the url to the admin api.
* **info** - Prints metrics and other information about the running pohlman service.
* **selftest** - Verifies that pohlman can communicate with the HWS service and that it can access the database.
* **airports** - Lists the current airports of interest (ICAO codes and names) for which weather data is retrieved.
* **extra\_airports [<airports>]** - Set extra airports to request weather data from (in addition to those derived from flight data). Parameter <airports> is a comma-separated list of airport ICAO codes. If omitted, the extra airports currently in effect are printed.
* **metar <airport>** - Requests weather observation for an airport and prints the result. Parameter <airport> is an ICAO airport code.
* **taf <airport>** - Requests weather forecast for an airport and prints the result. Parameter <airport> is an ICAO airport code.
* **force\_run** - Retrieves and stores weather observations and forecasts based on current airports of interest, and prints immediate feedback.
* **stop** - Stop the service. Note that if pohlman is started by sysmond, sysmond will start the process again.

### Indices and tables
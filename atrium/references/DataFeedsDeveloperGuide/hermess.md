# Hermess ACARS API

The purpose of this document is to describe the JCMS service for sending ACARS free text messages

1. Introduction
2. Design overview
3. Configuration
3.1. systemd
3.2. Environment

4. Examples

## Indices and tables

- Index
- Search Page



--- SUBPAGE: hermess.html ---

# 1. Introduction

This component implements a REST API for sending ACARS free text messages. These
are arbitrary messages, at most 200 characters long, that are sent directly to a
specific aircraft via an external relay.

# 2. Design overview

Hermess is a free standing component, and is not a part of Standard
Interfaces. The intended usage is to run it on an SPS node where it is started
by systemd as a stand-alone application. The component provides an http
server with a REST API, and the only system dependencies is access to the
ActiveMQ message broker where outgoing messages are placed. These outgoing
messages are then intended to be processed by Message Recipient Management (MRM)
which can be setup to forward them to a suitable ACARS service.

A call to the free-text API with a message, generates up to two messages
(depending on configuration) in the message broker; one message formatted for
Message Retention (MR) and one message formatted for MRM. Since MRM also stores
messages for posterity, the intention is that the user should disable the MR
messages once that component is deprecated.

# 3. Configuration

The server accepts the following command line parameters:
- --api-specification: Path to OpenAPI specification of the API
- --mr-queue: Queue to use for MR messages (an empty queue name disables these messages)
- --mrm-queue: Queue to use for MRM messages (an empty queue name disables these messages)
- --broker-host: ActiveMQ broker host name
- --broker-port: ActiveMQ broker port (AMQP protocol)
- --broker-username: ActiveMQ broker user name
- --broker-password: ActiveMQ broker password
- --server-listen-address: Server bind address (“0.0.0.0” to accept all incoming connections)
- --server-listen-port: Server listen port
- --dont-rewrite-regno: Disable adding a dash in the correct place in aircraft registration numbers

## 3.1. systemd

hermess is started and stopped via systemd. The command line parameters
above can be changed in the systemd script
(/etc/systemd/system/hermess.service) created when running atriumctl
configure.

## 3.2. Environment

The following parameters are configurable via environment.yml:

- feature_hermess: Whether the Hermess ACARS API should be enabled on this system or not,
- hermess_mrm_queue: Queue used for sending outbound ACARS messages to Recipient Management (MRM),
- hermess_mr_queue: Queue used for sending outbound ACARS messages to Message Retention (MongoDB),
- feature_service_mesh: Set to ‘compatible’ or ‘enabled’ to enable Consul Connect sevice mesh for Atrium internal communication,

# 4. Examples

To check that the service is operating, issue a GET request to health

curl [http://$HOST/hermess/v1/health](http://$HOST/hermess/v1/health)

To send a message:

curl -X POST -H “Content-Type: text/plain” –data “Message to be sent” [http://$HOST/hermess/v1/free-text?car=6E&amp;num=1023&amp;udor=2022-02-02&amp;adep=HYD&amp;ades=DEL&amp;regno=A-BCDE&amp;suf=Q](http://$HOST/hermess/v1/free-text?car=6E&amp;num=1023&amp;udor=2022-02-02&amp;adep=HYD&amp;ades=DEL&amp;regno=A-BCDE&amp;suf=Q)
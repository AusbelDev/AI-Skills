## Hermess ACARS API


The purpose of this document is to describe the JCMS service for sending ACARS free text messages

* [1. Introduction](hermess.html)
* [2. Design overview](hermess.html#design-overview)
* [3. Configuration](hermess.html#configuration)
  + [3.1. systemd](hermess.html#systemd)
  + [3.2. Environment](hermess.html#environment)
* [4. Examples](hermess.html#examples)

#### Indices and tables

* [Index](../genindex.html)
* [Search Page](../search.html)

### Introduction

### Design overview

### Configuration

#### systemd

###### 3.1. systemd

`hermess` is started and stopped via systemd. The command line parameters
above can be changed in the systemd script
(`/etc/systemd/system/hermess.service`) created when running atriumctl
configure.

#### Environment

### Examples

### Indices and tables
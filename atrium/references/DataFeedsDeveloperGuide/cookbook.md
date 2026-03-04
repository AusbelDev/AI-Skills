# Data Feeds Developer Cookbook

This section provides step-by-step guides and instructions for data feeds developers.

Creating a standalone custom interface describes how to develop a custom request/response data feed without the Interface Builder

Creating a trigger service describes how to develop a trigger.

The Integrator chapter describes how to make services inside JCMS available to external systems using the Integrator component.

The Jobrunner Configuration Guide describes how to configure the Jobrunner framework, for scheduling and triggering of e.g. datafeeds imports and exports.

Setup of processes and services describes concrete realizations of typical interfaces and the
reasoning behind the design decisions. This includes cases that utilize the standard interfaces as well as
custom feeds and services.

## Contents

Overview
Creating a standalone custom interface
Creating a trigger service
IOService builder
Integrator
Jobrunner Configuration Guide
Setup of processes and services
Troubleshooting



--- SUBPAGE: genindex.html ---

Index

 _
 | A
 | B
 | C
 | D
 | E
 | F
 | G
 | H
 | I
 | J
 | M
 | N
 | O
 | P
 | R
 | S
 | T
 | U
 

_

  
      __init__() (jcms.ioserver.testutils.version10.main.IMemoryHAStore method)

      
        (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

        (jcms.ioserver.testutils.version10.main.ITestConfig method)

        (jcms.ioserver.testutils.version10.main.TestMain method)

        (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

        (jcms.ioserver.testutils.version9.main.IMemoryHAStore method)

        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

        (jcms.ioserver.testutils.version9.main.ITestConfig method)

        (jcms.ioserver.testutils.version9.main.TestMain method)

        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

        (jcms.ioserver.version10.config.IConfig method)

        (jcms.ioserver.version10.context.OnLoadServiceContext method)

        (jcms.ioserver.version10.context.ServiceContext method)

        (jcms.ioserver.version10.message.PlainIOMessage method)

        (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

        (jcms.ioserver.version9.config.IConfig method)

        (jcms.ioserver.version9.context.ServiceContext method)

        (jcms.ioserver.version9.message.PlainIOMessage method)

        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
  

A

  
      addInputIOMessage() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
  

B

  
      begin() (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

      
        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

      
  
  
      bookmarkCurrentVersion() (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

      
        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

      
  

C

  
      clear() (jcms.ioserver.testutils.version10.main.IMemoryHAStore method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryHAStore method)

      
      config (jcms.ioserver.version10.context.OnLoadServiceContext property)

      
        (jcms.ioserver.version10.context.ServiceContext property)

        (jcms.ioserver.version9.context.ServiceContext property)

      
      ConflictDetectionDisabled (built-in variable)

      ConflictDetectionMessage (built-in variable)

      ConflictDetectionPlan (built-in variable)

      content (jcms.ioserver.version10.message.PlainIOMessage property)

      
        (jcms.ioserver.version9.message.PlainIOMessage property)

      
  
  
      content_type (jcms.ioserver.version10.message.PlainIOMessage property)

      
        (jcms.ioserver.version9.message.PlainIOMessage property)

      
      convertToMemoryQueues() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      create_io_message() (jcms.ioserver.version10.context.ServiceContext method)

      
        (jcms.ioserver.version10.message.PlainIOMessage class method)

        (jcms.ioserver.version9.context.ServiceContext method)

        (jcms.ioserver.version9.message.PlainIOMessage class method)

      
      create_io_message_from_content() (jcms.ioserver.version10.context.ServiceContext method)

      
        (jcms.ioserver.version9.context.ServiceContext method)

      
  

D

  
      debugPrint() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
  
  
      DEFAULT_RESPONSE (jcms.ioserver.version10.actions.FaultAction attribute)

      
        (jcms.ioserver.version9.actions.FaultAction attribute)

      
  

E

  
      enableMessageRetention() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      encoding (jcms.ioserver.version10.message.PlainIOMessage property)

      
        (jcms.ioserver.version9.message.PlainIOMessage property)

      
  
  
      end() (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

      
        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

      
  

F

  
      FaultAction (class in jcms.ioserver.version10.actions)

      
        (class in jcms.ioserver.version9.actions)

      
  
  
      full_message_text (jcms.ioserver.version10.message.PlainIOMessage property)

      
        (jcms.ioserver.version9.message.PlainIOMessage property)

      
  

G

  
      get_available_sinks() (jcms.ioserver.version10.context.ServiceContext method)

      
        (jcms.ioserver.version9.context.ServiceContext method)

      
      get_default_content_type() (jcms.ioserver.version10.message.PlainIOMessage class method)

      
        (jcms.ioserver.version9.message.PlainIOMessage class method)

      
      get_default_sink_name() (jcms.ioserver.version10.context.ServiceContext method)

      get_meta() (jcms.ioserver.version10.message.PlainIOMessage method)

      get_properties() (jcms.ioserver.version10.message.PlainIOMessage method)

      
        (jcms.ioserver.version9.message.PlainIOMessage method)

      
      get_property() (jcms.ioserver.version10.message.PlainIOMessage method)

      
        (jcms.ioserver.version9.message.PlainIOMessage method)

      
      get_system_encoding() (jcms.ioserver.version10.message.PlainIOMessage class method)

      
        (jcms.ioserver.version9.message.PlainIOMessage class method)

      
      get_user_attributes() (jcms.ioserver.version10.message.PlainIOMessage method)

      
        (jcms.ioserver.version9.message.PlainIOMessage method)

      
      getChangeSet() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getConfig() (jcms.ioserver.testutils.version10.main.TestMain method)

      
        (jcms.ioserver.testutils.version9.main.TestMain method)

      
      getConfigAttribute() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getConfigAttributes() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getConfigBool() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getConfigInt() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getConfigSubGroup() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getConfigValue() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getContextParameter() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getDefaultInputContentType() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getDefaultInputEncoding() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getDomainGeneration() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

        (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getenv() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getGlobalConfigGroup() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getGlobalGroupNames() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getInputIOMessage() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getInputIOMessages() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getInputSize() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getMave2ChangeSet() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getMave2Plan() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getMave2PlanWithViewpoint() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getMave2PreviousVersion() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getMaveGeneration() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getMemoryHAStore() (jcms.ioserver.testutils.version10.main.TestMain method)

      
        (jcms.ioserver.testutils.version9.main.TestMain method)

      
      getMemoryQueue() (jcms.ioserver.testutils.version10.main.TestMain method)

      
        (jcms.ioserver.testutils.version9.main.TestMain method)

      
  
  
      getNowTime() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getOutputIOMessage() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getOutputIOMessageByName() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getOutputIOMessages() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getOutputIOMessagesByName() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getOutputSize() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getOutputSizeByName() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getPlan() (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

      
        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

        (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getPlanBuilderName() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      getPlanPeriodEnd() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getPlanPeriodStart() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getPortBase() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getPreviousVersion() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getProcessName() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

        (jcms.ioserver.version10.config.IConfig method)

        (jcms.ioserver.version9.config.IConfig method)

      
      getProcessServicePort() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

        (jcms.ioserver.version10.config.IConfig method)

        (jcms.ioserver.version9.config.IConfig method)

      
      getProcessServiceUrl() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getRaveSession() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getRaveSessionWithViewpoint() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      getRulesetType() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      getRunner() (jcms.ioserver.testutils.version10.main.TestMain method)

      
        (jcms.ioserver.testutils.version9.main.TestMain method)

      
      getServiceConfigGroup() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getServiceGroupNames() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getServiceNames() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

        (jcms.ioserver.version10.config.IConfig method)

        (jcms.ioserver.version9.config.IConfig method)

      
      getStartId() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      getSubGroupNames() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getSubGroups() (jcms.ioserver.version10.config.IConfig method)

      
        (jcms.ioserver.version9.config.IConfig method)

      
      getThePlan() (jcms.ioserver.version10.planholder_militaris.IPlanHolder static method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder static method)

      
      getValue() (jcms.ioserver.testutils.version10.main.IMemoryHAStore method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryHAStore method)

      
  

H

  
      has_request (jcms.ioserver.version10.context.ServiceContext property)

      
        (jcms.ioserver.version9.context.ServiceContext property)

      
      has_response (jcms.ioserver.version10.context.ServiceContext property)

      
        (jcms.ioserver.version9.context.ServiceContext property)

      
  
  
      hasValue() (jcms.ioserver.testutils.version10.main.IMemoryHAStore method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryHAStore method)

      
  

I

  
      IConfig (class in jcms.ioserver.version10.config)

      
        (class in jcms.ioserver.version9.config)

      
      id (jcms.ioserver.version10.message.PlainIOMessage property)

      
        (jcms.ioserver.version9.message.PlainIOMessage property)

      
      IMemoryHAStore (class in jcms.ioserver.testutils.version10.main)

      
        (class in jcms.ioserver.testutils.version9.main)

      
      IMemoryQueue (class in jcms.ioserver.testutils.version10.main)

      
        (class in jcms.ioserver.testutils.version9.main)

      
      importProcessConfig() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
  
  
      IPlanHolder (class in jcms.ioserver.version10.planholder_militaris)

      
        (class in jcms.ioserver.version9.planholder_militaris)

      
      isPlanLoaded() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      isRulesetLoaded() (jcms.ioserver.version10.planholder_militaris.IPlanHolder method)

      
        (jcms.ioserver.version9.planholder_militaris.IPlanHolder method)

      
      ITestConfig (class in jcms.ioserver.testutils.version10.main)

      
        (class in jcms.ioserver.testutils.version9.main)

      
  

J

  
      
    jcms.ioserver.testutils.version10.main

      
        module

      
      
    jcms.ioserver.testutils.version9.main

      
        module

      
      
    jcms.ioserver.version10.actions

      
        module

      
      
    jcms.ioserver.version10.config

      
        module

      
      
    jcms.ioserver.version10.context

      
        module

      
  
  
      
    jcms.ioserver.version10.message

      
        module

      
      
    jcms.ioserver.version9.actions

      
        module

      
      
    jcms.ioserver.version9.config

      
        module

      
      
    jcms.ioserver.version9.context

      
        module

      
      
    jcms.ioserver.version9.message

      
        module

      
  

M

  
      meta_enabled (jcms.ioserver.version10.message.PlainIOMessage property)

      
    module

      
        jcms.ioserver.testutils.version10.main

        jcms.ioserver.testutils.version9.main

        jcms.ioserver.version10.actions

        jcms.ioserver.version10.config

        jcms.ioserver.version10.context

        jcms.ioserver.version10.message

        jcms.ioserver.version9.actions

        jcms.ioserver.version9.config

        jcms.ioserver.version9.context

        jcms.ioserver.version9.message

      
  

N

  
      NO_RESPONSE (jcms.ioserver.version10.actions.FaultAction attribute)

      
        (jcms.ioserver.version9.actions.FaultAction attribute)

      
  

O

  
      OnLoadServiceContext (class in jcms.ioserver.version10.context)

  

P

  
      PlainIOMessage (class in jcms.ioserver.version10.message)

      
        (class in jcms.ioserver.version9.message)

      
      PlanAction (class in jcms.ioserver.version10.actions)

      
        (class in jcms.ioserver.version9.actions)

      
  
  
      process() (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

      
        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

      
      pyxb_encoding (jcms.ioserver.version10.message.PlainIOMessage attribute)

      
        (jcms.ioserver.version9.message.PlainIOMessage attribute)

      
  

R

  
      refresh() (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

      
        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

      
      report_progress() (jcms.ioserver.version10.context.ServiceContext method)

      
        (jcms.ioserver.version9.context.ServiceContext method)

      
      request_message (jcms.ioserver.version10.context.ServiceContext property)

      
        (jcms.ioserver.version9.context.ServiceContext property)

      
      reset() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

      
  
  
      response_message (jcms.ioserver.version10.context.ServiceContext property)

      
        (jcms.ioserver.version9.context.ServiceContext property)

      
      ROLLBACK (jcms.ioserver.version10.actions.PlanAction attribute)

      
        (jcms.ioserver.version9.actions.PlanAction attribute)

      
      rollbackToBookmark() (jcms.ioserver.testutils.version10.runner_militaris.TestRunner method)

      
        (jcms.ioserver.testutils.version9.runner_militaris.TestRunner method)

      
  

S

  
      SAVE (jcms.ioserver.version10.actions.PlanAction attribute)

      
        (jcms.ioserver.version9.actions.PlanAction attribute)

      
      send() (jcms.ioserver.version10.context.ServiceContext method)

      
        (jcms.ioserver.version9.context.ServiceContext method)

      
      SEND_RESPONSE (jcms.ioserver.version10.actions.FaultAction attribute)

      
        (jcms.ioserver.version9.actions.FaultAction attribute)

      
      send_to_sink() (jcms.ioserver.version10.context.ServiceContext method)

      
        (jcms.ioserver.version9.context.ServiceContext method)

      
      service_logger (jcms.ioserver.version10.context.OnLoadServiceContext property)

      
        (jcms.ioserver.version10.context.ServiceContext property)

        (jcms.ioserver.version9.context.ServiceContext property)

      
      service_name (jcms.ioserver.version10.context.OnLoadServiceContext property)

      
        (jcms.ioserver.version10.context.ServiceContext property)

        (jcms.ioserver.version9.context.ServiceContext property)

      
      ServiceContext (class in jcms.ioserver.version10.context)

      
        (class in jcms.ioserver.version9.context)

      
      set_meta() (jcms.ioserver.version10.message.PlainIOMessage method)

      set_property() (jcms.ioserver.version10.message.PlainIOMessage method)

      
        (jcms.ioserver.version9.message.PlainIOMessage method)

      
      set_response_sink() (jcms.ioserver.version10.context.ServiceContext method)

      
        (jcms.ioserver.version9.context.ServiceContext method)

      
      setChangeReason() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setConfigValue() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setConflictDetectionStrategy() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setCppBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setCppHandlerBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setCppTriggerBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setDatabase() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setDefaultInputContentType() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      setDefaultInputEncoding() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      setDomainGeneration() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setErrorRetryCount() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setEventTriggerPattern() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setInputIOMessages() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      setMemoryQueue() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setMemorySource() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setMsgErrorStrategy() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
  
  
      setNamedMemorySink() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setNow() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setPersistCid() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setPlan() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setPortBase() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setPythonBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setPythonHandlerPlainBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setPythonHandlerSoapBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setPythonTriggerPlainBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setPythonTriggerSoapBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setQpid() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setQpidMessageSink() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setQpidMessageSource() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setRequestResponsePattern() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setRuleset() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setRulesetType() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setServiceValue() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setStartId() (jcms.ioserver.testutils.version10.main.IMemoryQueue method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryQueue method)

      
      setSubscriberPattern() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setSubscriberPatternChunkSize() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setSubscriberPatternSaving() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setTestBinding() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setTimeServicePort() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setTriggerPattern() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
      setValue() (jcms.ioserver.testutils.version10.main.IMemoryHAStore method)

      
        (jcms.ioserver.testutils.version9.main.IMemoryHAStore method)

      
      skipPlan() (jcms.ioserver.testutils.version10.main.ITestConfig method)

      
        (jcms.ioserver.testutils.version9.main.ITestConfig method)

      
  

T

  
      TestMain (class in jcms.ioserver.testutils.version10.main)

      
        (class in jcms.ioserver.testutils.version9.main)

      
  
  
      TestRunner (class in jcms.ioserver.testutils.version10.runner_militaris)

      
        (class in jcms.ioserver.testutils.version9.runner_militaris)

      
  

U

  
      UNCHANGED (jcms.ioserver.version10.actions.PlanAction attribute)

      
        (jcms.ioserver.version9.actions.PlanAction attribute)

--- SUBPAGE: search.html ---

Search
  
  
  
  
    Please activate JavaScript to enable the search
    functionality.
  

  
  
  
  
  
    Searching for multiple words only shows matches that contain
    all words.

--- SUBPAGE: devbook/interfaces_overview.html ---

# Overview

- IO server
- Interface Builder
- Standard and Custom Interfaces
- Integrator
- Jobrunner
- Summary

A crew tracking system will always have a number of interfaces to external systems for different purposes, for example:

- Receive flight schedule information from flight planning and operations systems
- Receive flight movement information from aircraft and airports
- Send crew data to and from HR and payroll systems
- Send trip and roster information between JCT and the rostering system
- Create and send ticket reservations and hotel bookings

## IO server

Interfaces in JCT are realized within the IO server framework.

A number of IO server processes are running in the system. An IO server process runs a number of services, where each service is configured to handle an interface. A service always uses ActiveMQ message queues for input and output. Processes, services and message queues are configured using XML in the JCT XML configuration.

The IO server main process loads the plan from the JCT database and repeatedly does a refresh from the database. After each refresh, main process forks subprocesses for each service. A service may have one or more parallel worker processes depending on the expected usage pattern.

There are a number of IO server processes in a JCT system. An example setup is:

- ioserver_batch - services that do not need high availability support since they are only used for batch processing
- ioserver_singleton - services that can only run in one instance at a time
- ioserver_web - services used by Crew Access and TIC
- ioserver_datafeeds - services used by external services (none batch interfaces)
- ioserver_historical - used by Report Manager to generate reports containing historical data.

When implementing a service, there are a number of different patterns to choose from:

SubscriberA subscriber service reads from an input queue, processes the message and writes to the JCT database. The client of the service does not expect any response. Flight schedule and movement messages are examples of interfaces that are implemented with the subscriber pattern.

Request/responseA request/response service reads from an input queue, processes the message, optionally saves data in the JCT database and sends a response on an output queue. Most interfaces are implemented using the this pattern, for example roster, trip and crew input and output interfaces.

TriggerA trigger service examines the changes in the JCT database since last refresh and writes messages on an output queue or saves data in the database, based on what changes there are. Triggers are used for sending out information to e.g. ticket and hotel reservation systems and crew facing applications when rosters change.

Repeating triggerA repeating trigger service runs at specified time intervals and writes messages on an output queue or saves data in the database, depending on the contents of the database. Repeating triggers are typically used for generating scheduled reports to e.g. HR and payroll systems.

Patterns can also be combined. For example, a common usage scenario is to have a trigger service that creates a request for a request/response service. The output queue for the trigger is the input queue for the request/response service.

## Interface Builder

The interface builder is a tool for building interfaces where the message payload is based on XML. The message syntax can be based on either pure XML or SOAP. Both the interface specification and implementation is defined using an XML based domain specific lanuage - CSDL. The CSDL language allows interface and implementation to be separated from each other. It also has constructs for defining customized extensions to both interface and implementation.

Based on the CSDL specification, the Interface Builder will generate interface definitions in the form of WSDL or XSD files, to be used by clients, as well as an IO server service handler script. The configuration of the IO service will point out the handler script.

## Standard and Custom Interfaces

There are a number of predefined standard interfaces in the JCT core product, for example for:

- Airport Data import
- Flight schedule import
- Flight movements import
- Flight export
- Trip import and export
- Crew data import and export
- Roster import and export
- Plan synchronization
- Crew messages
- Crew check-in

The standard interfaces are described in detail in Standard Interfaces

When defining the interfaces in a customization project, there are a number of options:

Use a standard interfaceUsing a standard interface requires a very minor configuration effort in the customization layer. The interface need to be defined, but no CSDL code or other form of adaptation is needed.

Extend a standard interfaceIt is also possible to define a new interface that is based on a standard interface. This requires that some customization CSDL code is written. The customized interface inherits the standard interface.

Write a CSDL based interface from scratchThe Interface Builder can also be used to write a customer specific interface from scratch. This requires that all CSDL code is written in the customization layer.

Write a non-CSDL based interfaceFor non-CSDL based interfaces, service handler needs to be handcrafted. The handler should implement a service handler API defined by the IO server. Handlers for triggers and repreating triggers always need to be implemented using this method, since trigger patterns are not supported by the Interface Builder. For request/response and subscriber interfaces, there are often requirements that input or output should follow non-XML legacy formats. This is another example of a case when a non-CSDL based interface handler needs to be implemented.

## Integrator

The IO server always uses message queues for communication. In most cases there are requirements that input/output is handled using other endpoint types, for example importing/exporting files, SOAP or plain HTTP requests/responses, outgoing HTTP requests for outbound interfaces or FTP transfers.

The main purpose with the Integrator component is to route input and output between the IO server message queues and the preferred endpoints. The Integrator is also used to transform messages between external message formats and Jeppesen standard interface formats.

The Integrator is a WildFly application server with Apache Camel - a Java framework for implementing enterprise integration patterns - installed. Using the concept of routes and contexts in Camel, messages can be routed to any type of endpoint. Routes in the Integrator are defined with XML.

## Jobrunner

Jobrunner is a framework for scheduling and manually running interface jobs, for example file exports and imports. Jobs are started and monitored from a web user interface. Jobrunner is implemented as two IO server services - one SOAP web service for reading configuration and starting jobs and a trigger service that starts jobs based on the schedule in the configuration. Static configuration is defined in python code and Apach Camel routes. Information about running jobs is stored in a simple presistent key-value store.

Each type of job needs to be defined in the customization implementation. Job configuration consists of two parts:

Static job definitionsJob name, job parameters, default values and lists of permissible parameter values is defined in python code.

Job implementationThe implementation of the job, i.e. what actions to take, consists of a Camel route. The route will call the appropriate IO service and also call the Jobrunner SOAP web service to update the status of running jobs.

## Summary

The Standard Interfaces, IO server, Integrator, and Jobrunner are the core components that enables customized interface development in an implementation project.

The customer implementation layer will need the following:

Interfaces
- CSDL specification/implementation or hand-written interface handlers.

IO server configuration
- Configuration of IO services, defining services, mapping services to interface handlers
- Configuration of message queues

Integrator
- Defining Camel routes and endpoints for services
- Defining Camel routes for Jobrunner jobs

Jobrunner
- Defining jobs, custom handling of e.g. parameter values and default values.

--- SUBPAGE: py-modindex.html ---

# Python Module Index

   
   j
   

   
     &#160;
     
       j
     
       <img src="_static/minus.png" class="toggler"
              id="toggle-1" style="display: none" alt="-" />
       
       jcms
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.testutils.version10.main
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.testutils.version9.main
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.version10.actions
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.version10.config
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.version10.context
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.version10.message
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.version9.actions
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.version9.config
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.version9.context
       
     
       
       &#160;&#160;&#160;
       jcms.ioserver.version9.message

--- SUBPAGE: devbook/interfaces_custom.html ---

# Creating a standalone custom interface

This chapter describes the steps needed to write a pure request/response or subscriber custom interface (not built by the SMOG/IOService Builder or the IFBuilder tools) to be run by the IOServer.

See the IOServer documentation for reference information.

- Defining a handler
- Configuration
- Testing the interface

## Defining a handler

The main difference between writing an interface using the IFBuilder and writing  standalone interface is that in the latter case, a handler script needs to be written - it will not be generated automatically.

A python module should to be defined in $CARMUSR/lib/python/datafeeds/&lt;interface name&gt;/, e.g. request_handler.py.

The module need to implement handler_interface_version and a handler method, which are called from the IOServer.
The module may optionally implement an on_fault method.

See Handler interface.

The handler method name is given by:

- For a SOAP-XML handler, the name is read from the SOAPAction message header. (Having standalone SOAP XML handlers will not be very common.)
- For a plain text handler, the name is read from the handler configuration, binding/operation. The default name is handle.

### Implementing the handler

Example of a handler implementation using the plain data format:

from jcms.ioserver.versions import InterfaceVersion
from jcms.ioserver.version10.actions import PlanAction, FaultAction

def handler_interface_version():
    &quot;&quot;&quot;
    Define the ioserver interfaces version
    &quot;&quot;&quot;
    return InterfaceVersion.TEN

def on_fault(planholder, service_context, excp):
    error_response = &quot;Failed to handle request with error: %s&quot; % excp
    io_message = service_context.create_io_message(error_response, encoding=&#39;utf-8&#39;)
    service_context.response_message = io_message
    return FaultAction.SEND_RESPONSE

def handle(planholder, service_context):
    try:
        request_body = service_context.request_message.content
        response_body = handle_request(request_body)
        io_message = service_context.create_io_message(response_body, encoding=&#39;utf-8&#39;)
        service_context.response_message = io_message

        return PlanAction.UNCHANGED
    except Exception as e:
        service_context.service_logger.exception(&quot;Failed to handle request: %s&quot;, str(e))
        raise ios_exceptions.SkipMsgError(e)

The handle method is called whenever a request message is available and it receives two arguments:

- The planholder provides access to the ARA plan and Rave session.

The service context contains e.g.
Member variables for the request and response message, making it possible for the handler to read the request and write the response.
To return a message, the handler should set the response_message of the service_context argument.

- Methods for creating messages
- A logger object, making it possible to log from the service handler.

To return a message, the handler sets the response_message of the service_context argument.

The handler should return one of these constants, indicating how the IO server should handle any possible changes to the plan that the handler has done:

PlanAction.UNCHANGEDno changes in the plan, nothing needs to be saved

PlanAction.SAVEchanges in the plan need to be saved

PlanAction.ROLLBACKchanges in the plan must be rolled back.

When the plan action has been executed successfully, any provided response message is sent out
and the request is removed from the source (input) queue.

The IOServer Python API reference is used to get access to the IOServer version, public constants, exceptions, the IOServer configuration, return actions, the message and the ARA plan.

## Configuration

See Configuration.

To configure an interface to be run by the IOServer, an service needs to be defined by a configuration xml file in $CARMUSR/usr/etc/programs/ioservices/datafeeds/. The file and the IO service should have the same name and they should be named with an interface name, prefixed by df_ (as in datafeeds) and suffixed by the direction of the interface, either _in or _out, for example df_crew_data_in.xml or df_layover_out.xml.

The service configuration file needs to be included by a specific IOServer process xml file, for example ioserver_datafeeds.xml in
$CARMUSR/usr/etc/programs/. New IOServer processes can also be defined if there is a need for it.

Example:

&lt;include href=&quot;${CARMUSR}/etc/programs/ioservices/datafeeds/df_preassignments_out.xml&quot; /&gt;

An example of a service configuration file is shown below.

&lt;ioservice name=&quot;df_preassignments_out&quot;&gt;
  &lt;pattern&gt;
    &lt;class&gt;requestresponse&lt;/class&gt;
    &lt;cacs_role&gt;interface&lt;/cacs_role&gt;
    &lt;changereason&gt;Other&lt;/changereason&gt;
  &lt;/pattern&gt;
  &lt;binding&gt;
    &lt;language&gt;python&lt;/language&gt;
    &lt;handler&gt;datafeeds.df_preassignments_out.request_handler&lt;/handler&gt;
    &lt;protocol&gt;plain&lt;/protocol&gt;
  &lt;/binding&gt;
  &lt;source&gt;
    &lt;class&gt;qpid&lt;/class&gt;
    &lt;queue_reference&gt;to.ioservice.df_preassignments_out&lt;/queue_reference&gt;
  &lt;/source&gt;
  &lt;sink&gt;
    &lt;class&gt;qpid&lt;/class&gt;
    &lt;queue_reference&gt;to.camelroute.export_preassignments&lt;/queue_reference&gt;
  &lt;/sink&gt;
&lt;/ioservice&gt;

The pattern class element indicates that this is a request/response interface.

The binding element points out the implementation code that handles the requests. The handler represents the python module that contains the implementation of the service handler. It is possible to write handlers in C++, but all customer specific handlers should be written in python. The handler should implement an interface defined by the IO server component. The interface is different for different service patterns.

The protocol can be either plain or soap.

For each service, a source message queue and a sink message queue should be defined. For request/response services, responses are sent to the sink. For subscriber services, only error messages are sent to the sink.

## Testing the interface

The IOService builder provides a test class IOServiceTestBase that makes it easy to test standalone custom IOServices. The framework is based on Python unit tests and the following example shows how to test the service once it has been added to a service configuration as shown above.

from ioservice_builder.testsupport import IOServiceTestBase

class TestPreassignmentsService(IOServiceTestBase):

    ioserver_name = &quot;ioserver_datafeeds&quot; # name of the IOServer process that provides the IOServer to test.
    ioservice_name = &quot;df_preassignments_out&quot; # name of the IOService to test
    schema_name = &quot;tiny&quot; # Name of Firebird schema to use, must exist as $CARMTMP/firebird/unit_test/&lt;schema_name&gt;.fdb

    def test_something(self):
        # Create a request message on a format that the custom handler understands
        request = &quot;CREWID: 12345, MONTH: MAR2020&quot;

        # Put the message on the IOService source queue
        self.put_msg(request)

        # Let the IOService process messages on the source queue
        self.testrunner.process()

        # Get content and headers for the response message from the IOService sink queue
        content, headers = self.get_msg()

        # Assert response message
        self.assertEquals(content, ...)
        self.assertHeaders(headers, ...)

--- SUBPAGE: devbook/interfaces_triggers.html ---

# Creating a trigger service

This chapter describes the steps needed to write a trigger service to be run by the IOServer. Triggers cannot be implemented using IFBuilder.

See the IOServer documentation for reference information.

- Defining a handler
- Configuration

## Defining a handler

A python module should to be defined in $CARMUSR/lib/python/datafeeds/triggers/&lt;trigger name&gt;/, e.g. handler.py.
The module need to implement handler_interface_version, an on_event method and optionally an on_load method, which are called from the IOServer.

See Trigger interface.

### Implementing the trigger handler

Example of a handler implementation using the plain data format:

from jcms.ioserver.versions import InterfaceVersion
from jcms.ioserver.version9.actions import PlanAction

def handler_interface_version():
    &quot;&quot;&quot;
    Define the ioserver interfaces version
    &quot;&quot;&quot;
    return InterfaceVersion.TEN

def on_load(planholder, context):
    pass

def on_event(planholder, service_context):

    finder = BookingOperationFinder(planholder.getMave2ChangeSet(), planholder.getPlan())
    booking_ops = finder.find_booking_operations()

    # Generate messages and send requests
    if len(booking_ops) &gt; 0:
        generator = MessageGenerator(planholder.getMave2Plan(), service_context)
        for booking_op in booking_ops:
            message  = generator.generate_message(planholder, booking_op)
            generator.send_message(message)
            booking_op.set_sent_status(planholder.getMave2Plan())

        return PlanAction.SAVE

      return PlanAction.UNCHANGED

The on_load method is called after the IO server main process has finished the initial load of data from the database.

The on_event method is called by the IO server after each refresh, or in the case of repreating triggers, with the specified time interval.

The on_event method receives two arguments:

- The planholder provides access to the ARA plan and Rave session. For triggers, the plan holder also provides the changeset, i.e. a table-by-table difference between the current state of the data and the state after the previous call to on_event.

The service context contains e.g.
Member variable for the response message, making it possible for the handler to write the response.
To return a message, the handler should set the response_message of the service_context argument.

- Methods for creating messages
- A logger object, making it possible to log from the service handler.

The purpose of the on_event method is to deduce what messages to send to the sink queue, from the changeset provided by the planholder (for triggers) or from the current state of the plan (for repeating triggers).

The handler should return one of these constants, indicating how the IO server should handle any possible changes to the plan that the handler has done:

PlanAction.UNCHANGEDno changes in the plan, nothing needs to be saved

PlanAction.SAVEchanges in the plan need to be saved

PlanAction.ROLLBACKchanges in the plan must be rolled back.

In the example above, records of sent messages is maintained in the database, and the trigger will instruct the IO server to save the changes it has made if the on_event method has processed any data. However, most triggers will be “read-only” and return PlanAction.UNCHANGED.

When the plan action has been executed successfully, any provided response message is sent to the sink queue.

The IOServer Python API reference is used to get access to the IOServer version, public constants, exceptions, the IOServer configuration, return actions, the message and the ARA plan.

### Creating the response

The response message can have any format - the format is entirely defines by the requirements of the receiver of the sink message.

In the simple example below, the content of the message is a plain text string. The outgoing message also has a property example_header.

def on_event(planholder, service_context):

    content = &quot;12345&quot;
    io_message = service_context.create_io_message(content, contentType=&quot;text/plain&quot;, encoding=&#39;US-ASCII&#39;)
    io_message.set_property(&quot;example_header&quot;, &quot;ABC&quot;)
    service_context.send(io_message)
    return PlanAction.UNCHANGED

The IO server API also has support for creating XML messages. It is not uncommon that the output of the trigger is input to a request/response service.

In the following example, the message created by the trigger is sent to the source of a request/response service created with the IFBuilder. The service handler of the request/response service holds the XSD as a member variable. An XML content factory is created by the trigger handler and used to build a request message for the request/response service.

import jcms.ioserver.version9.LxmlContent as ContentModel
import ioservice_impl.ticket_reservation_output_1_0_ext.ticketreservationoutput_handler as handler_module

def generate_message(self, planholder):

    content_factory = ContentModel.LxmlContentFactory(handler_module.xsd, tnsname=&quot;tns&quot;)
    request_node = content_factory.makeNode(&quot;TicketReservationRequestMsg&quot;, &quot;ticketReservationRequest&quot;)
    request_node.setValue(&quot;version&quot;, &quot;1.0&quot;)
    request_node.setValue(&quot;source&quot;, &quot;df_ticket_res_out_trigger&quot;)
    request_node.setValue(&quot;created&quot;, self.now)

    #
    # ...more content filled in here...
    #

## Configuration

See Configuration.

To configure a trigger to be run by the IOServer, a service needs to be defined by a configuration xml file in
$CARMUSR/usr/etc/programs/ioservices/datafeeds/. A good convention is to let the file and the IO service should have the same name and name them with df_ followed by a name of the trigger ,and suffixed with _trigger, for example df_roster_state_out_trigger.xml.

The service configuration file needs to be included by a specific IOServer process xml file, for example ioserver_singleton.xml in
$CARMUSR/usr/etc/programs/. New IOServer processes can also be defined if there is a need for it.

Example:

&lt;include href=&quot;${CARMUSR}/etc/programs/ioservices/datafeeds/df_ticket_res_out_trigger.xml&quot; /&gt;

Note that triggers must never run in multiple workers or processes at the same time. Typically there will be an IOServer process (e.g. ioserver_singleton.xml) that runs services that must always have exactly one worker.

An example of a service configuration file is shown below.

&lt;?xml version=&quot;1.0&quot; encoding=&quot;ISO-8859-1&quot; ?&gt;
&lt;!-- IOService definition for crew seat booking trigger --&gt;
&lt;ioservice name=&quot;df_ticket_res_out_trigger&quot;&gt;

  &lt;pattern&gt;
    &lt;class&gt;trigger&lt;/class&gt;
    &lt;cacs_role&gt;interface&lt;/cacs_role&gt;
    &lt;changereason&gt;Other&lt;/changereason&gt;
  &lt;/pattern&gt;

  &lt;binding&gt;
    &lt;language&gt;python&lt;/language&gt;
    &lt;trigger&gt;datafeeds.triggers.ticket_res_out_trigger.handler&lt;/trigger&gt;
    &lt;protocol&gt;plain&lt;/protocol&gt;
  &lt;/binding&gt;

  &lt;sink&gt;
    &lt;class&gt;qpid&lt;/class&gt;
    &lt;queue_reference&gt;to.camelroute.export_ticket_reservation&lt;/queue_reference&gt;
    &lt;capacity&gt;0&lt;/capacity&gt;
  &lt;/sink&gt;

  &lt;persist_cid&gt;true&lt;/persist_cid&gt;
  &lt;hastore&gt;
    &lt;class&gt;consul&lt;/class&gt;
  &lt;/hastore&gt;

  &lt;worker_time_out&gt;360&lt;/worker_time_out&gt;
  &lt;worker_pool_size&gt;1&lt;/worker_pool_size&gt;

&lt;/ioservice&gt;

The pattern class element indicates that this is a trigger.

The binding element points out the implementation code that handles the requests. The handler represents the python module that contains the implementation of the trigger. It is possible to write handlers in C++, but all customer specific handlers sshould be written in python. The handler should implement an interface defined by the IO server component. The interface is different for different service patterns.

The protocol can be either plain or soap.

For each service, a sink message queue should be defined. Triggers do not need a source message queue, since they react on changes in the database and not on input messages.

The persist_cid and hastore elements specify that he service should maintain the commit id from the database, to make sure that no changes will be skipped. The commit id will be stored in Consul, which is a distributed key-value and service discovery store.

--- SUBPAGE: ioservice_builder/index.html ---

# IOService builder

The purpose of this document is to describe the how to use IOService builder, a tool that can be used for developing IOServices.

1. Introduction
2. Building IOServices
2.1. Subscriber and request/response patterns
2.2. Trigger and repeatingtrigger pattern
2.3. Managed subscription pattern

3. Configuration templates
4. Type conversions in service mapping
5. Testing IOServices
5.1. Request/Response and Subscriber pattern
5.2. Trigger pattern
5.3. Running tests

## Indices and tables

- Index
- Search Page

--- SUBPAGE: integrator-site/index.html ---

# Integrator

Document Information
Doc Version: DevGuide 1.0.126-SNAPSHOT, Date: 2026-03-03,
Security Class: External

Welcome to the documentation of Integrator-core.

1. Purpose
2. Overview
3. Integrator features
3.1. Camel routes
3.2. Exposing SOAP web services
3.3. Exposing REST web services
3.4. REST Gateway web service
3.5. Web services security
3.6. JMS REST API for Test Purposes
3.7. Large Message Handling
3.8. MQ-router

4. Message Retention
5. Configuration
5.1. HTTPS
5.2. Integrator directory structure
5.3. Environment variables
5.4. Custom configuration of integrator

6. Kubernetes specific aspects of integrator
6.1. JWT scopes configuration of integrator in k8s

7. Camel JMS component configuration
7.1. Transactions and JMS components
7.2. Configuring message brokers

8. Camel Migrations
8.1. Camel 3 migration
8.2. Camel 3.4.5 migration
8.3. Camel 3.17 migration
8.4. Camel 3.19 migration in integrator 9.3
8.5. Camel 3.20 migration in integrator 9.6.500
8.6. Camel deprecations
8.7. Camel 4.4 migration to 4.7 in integrator 11+
8.8. Camel 4.9 migration to 4.10 in integrator 11.9.0

9. Migration from integrator 10.x to 11.0
9.1. Camel migration
9.2. JMS configuration
9.3. Failover strategy
9.4. Variables removed from environment.yml
9.5. Informational

10. Running the integrator
10.1. Troubleshooting

11. Appendix A: Supported Camel components

## Indices and tables

- Index
- Search Page

--- SUBPAGE: jobrunner/index.html ---

# Jobrunner Configuration Guide

The purpose of this document is to describe the how to configure the Jobrunner feature in CMS.

1. Introduction
2. Job definitions
3. Configuration
4. Executing jobs

## Indices and tables

- Index
- Search Page

--- SUBPAGE: setup_interfaces/index.html ---

# Setup of processes and services

Grouping and setup of interfaces
IOService grouping
High availability setup of IOServices
Integrator Setup

Inbound Feeds
The standard flight operations interface
The standard flight schedule interface
The standard interfaces for crew

--- SUBPAGE: devbook/interfaces_troubleshooting.html ---

# Troubleshooting

To troubleshoot interfaces, there are basically 2 different types of logfiles and 3 web-pages of interrest.
The logfiles are the IOServer logfile and the Integrator logfile.

The web pages:

- http://&lt;web-node&gt;:20100/hawtio/ shows the status of all the Camel Contexts, and the routes.
- https://&lt;infra-node&gt;:8162/admin shows all ActiveMQ queues and their status.
- http://&lt;mon-node&gt;:5601 Kibana shows various status information and the logfiles.

IOServer

The IOServer produces logfiles, where the output from an interface, run in the IOServer will be logged. They are placed in
$CARMTMP/logfiles and are named as the ioserver process name from the XML configuration.

See IOServer logs.

They will reside on the monitor node, if no monitor node is defined, they will reside on the infra node.

This is the first place to look.

Integrator

If the interface seems to have run ok, or have not run at all, the problem could also be in the integrator.
The integrator produces logfiles on the web-node(s), in
$CARMUSR/integrator-site/server/standalone/log/ called server.log.

The integrator is the integration layer from the IOServer to an external system, ie. web-services, producing files,
receive/send messages on external queueing system etc.

## IOServer log

Ref to Datafeeds Configuration Developer Guide IOServer logs - Log format.

To find the start of a log statement for a specific interface for a message, look for Calling,
this is when the IOServer has fetched the message, or is time triggerred, and start processing it. To find the end of the processing,
look for Committing the message (id:. The Jcmslog MDC service value will be the IOServer service name.

&lt;14&gt;1 &lt;timestamp&gt; &lt;hostname&gt; &lt;process name&gt; 32605 OPER [details@38555 cid=&quot;29&quot; flow=&quot;ioserver.python.Caller&quot; msgId=&quot;293d5414-58ff-4fb6-baf5-c651808676bf&quot; service=&quot;&lt;ioservice name&gt;&quot;] &lt;U+FEFF&gt;Calling handler &#39;&lt;handler name&gt;&#39;

If the handler is run due to an incoming message, a bit above the Calling statement, the Fetched statement is logged, like:

&lt;14&gt;1 &lt;timestamp&gt; &lt;hostname&gt; &lt;process name&gt; 7357 OPER [details@38555 msgId=&quot;ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1&quot; flow=&quot;ioserver.qpid.QpidMessageSource.&lt;ioservice name&gt;&quot;] &lt;U+FEFF&gt;Fetched message: [msgId=&quot;ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1&quot; correlation-id=&quot;b870a12f-9937-4609-9c26-013cf0b30a97&quot; jcms_traceid=&lt;trace id&gt; jcms_state=&lt;CID&gt;]

If set, the jcms_traceid header is used to identify a request from/to the integrator. If not already set, It is set by the Integrator
to the breadcumbId if available, otherwise to the messageId.

The jcms_state header is set to the CID.

Reference IOServer messaging.

The Commiting the message (id: log statement:

&lt;14&gt;1 &lt;timestamp&gt; &lt;hostname&gt; &lt;process name&gt; 7357 OPER [details@38555 cid=&quot;114&quot; msgId=&quot;ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1&quot; service=&quot;&lt;service name&gt;&quot; flow=&quot;ioserver.requestresponse.df_batch_out&quot;] &lt;U+FEFF&gt;Committing the message (id: ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1) from the queue.

### Dispatch / Map pattern

If the IOServer configuration, is using the dispatch / map functionality, see ref IOServer - Patterns - Dispatch, then the IOServer log statements
will use the service_name attribute value or the handler attribute value (if service_name is not defined), as Jcmslog MDC service value.

This is only true, as long as the handler is in action, as soon as the handler has finished, and leave control to the IOServer worker to
take care of sending the response, the service value will be the IOServer ioservice name again.
This means that when looking for Calling and Committing the message (id: the service value will be the ioservice name.
And the handler in the Calling handler statement will be the IOServer dispacth_handle.handler.

&lt;14&gt;1 &lt;timestamp&gt; &lt;hostname&gt; &lt;process name&gt; 7357 OPER [details@38555 cid=&quot;114&quot; flow=&quot;ioserver.python.Caller&quot; msgId=&quot;ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1&quot; service=&quot;&lt;ioservice name&gt;&quot;] &lt;U+FEFF&gt;Calling handler &#39;jcms.ioserver.version10.dispatch_handler.handle&#39;

In the subsequent log statements for the handler, the service value, will be the service_name attribute value, or the handler attribute value, like:

&lt;14&gt;1 &lt;timestamp&gt; &lt;hostname&gt; &lt;process name&gt; 7357 OPER [details@38555 cid=&quot;114&quot; flow=&quot;ioserver.&lt;ioservice name&gt;.service&quot; msgId=&quot;ID:direct-10-67-113-191-44063-1524037189415-3:834:0:0:1&quot; service=&quot;&lt;service name&gt;&quot;] &lt;handler log message

## Integrator log
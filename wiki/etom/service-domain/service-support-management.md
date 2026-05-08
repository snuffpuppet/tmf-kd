---
type: etom-l2
spec_id: GB921
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx
source_extract_paths:
  - raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md
authority: primary
l1_parent: "1.4 Service Domain"
l2_id: "1.4.4"
l2_name: "Service Support Management"
---

# Service Support Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

## Overview

Service Support Management processes manage service infrastructure, ensuring that the appropriate service capacity is available and ready to support the SM&O Fulfillment, Assurance and Billing processes in instantiating and managing service instances, and for monitoring and reporting on the capabilities and costs of the individual SM&O FAB processes. 
The responsibilities of these processes include, but are not limited to:
• Supporting the operational introduction of new and/or modified service infrastructure;
• Managing and ensuring the ongoing quality of the Service Inventory;
• Applying service capacity rules from Infrastructure Lifecycle Management processes;
• Analyzing availability and quality over time on service infrastructure and service instances, including trend analysis and forecasting;
• Ensuring the operational capability of the SM&O processes
• Maintaining rating and tariff information for service infrastructure and service instances.
. Conducting Vulnerability Management;     
. Conducting Threat Assessments;        
. Conducting Risk Assessments;        
. Conducting Risk Mitigation;             
. Conducting Secure Configuration Activities
This process was renamed in 23.5. old name was Service Readiness & Support
This process was renamed in 24.0  old name was Service Support Readiness

— GB921 v25.5 Excel master, process ID `1.4.4`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.4.4.1 Manage Service Inventory

**Extended Description.**

The responsibilities of the Manage Service Inventory processes are twofold - establish, manage and administer the enterprise's service inventory, as embodied in the Service Inventory Database, and monitor and report on the usage and access to the service inventory, and the quality of the data maintained in it.

The service inventory maintains records of all service infrastructure and service instance configuration, version, and status details. It also records test and performance results and any other service related- information, required to support SM&O and other processes.

The service inventory is also responsible for maintaining the association between customer purchased product offering instances and service instances, created as a result of the Service Configuration & Activation processes.

Responsibilities of these processes include, but are not limited to:

• Identifying the inventory-relevant information requirements to be captured for service infrastructure and service instances ;

• Identifying, establishing and maintaining service inventory repository facilities;

• Establishing and managing the service inventory management and information capture processes;

• Managing the registration and access control processes that enable processes to create, modify, update, delete and/or download service data to and from the service inventory;

• Ensuring the service inventory repository accurately captures and records all identified service infrastructure and service instance details, through use of automated or manual audits;

• Tracking and monitoring of the usage of, and access to, the service inventory repository and associated costs, and reporting on the findings

• Identifying any technical driven shortcomings of the service inventory repository, and providing input to Resource Development & Management processes to rectify these issues.

**L4 sub-processes:**

- **1.4.4.1.1** Manage Service Inventory Database and Processes — Establishing, managing and administering the enterprise's service inventory,
- **1.4.4.1.2** Perform Service Inventory Audit Tests — Performing audit if inventory repository accurately captures and records all identified service infrastructure and service instance details
- **1.4.4.1.3** Track and Monitor Service Inventory Capabilities — Monitoring and reporting on the usage and access to the service inventory, and the quality of the data maintained in it.
- **1.4.4.1.4** Identify Service Inventory Issues and Provide Reports and Warnings — Managing and Identifying any service Inventory Repository issues and providing warnings.

### 1.4.4.2 Enable Service Configuration & Activation

**Extended Description.**

The Enable Service Configuration & Activation processes are responsible for planning and deployment of service infrastructure, and for ensuring availability of sufficient service infrastructure to support the Service Configuration & Activation processes.

The responsibilities of these processes include, but are not limited to:

• forecasting at an operational level service infrastructure volume requirements and run-out timeframes;

• the capacity planning associated with the deployment of new and/or modified service infrastructure;

• establishment and monitoring of organizational arrangements to support deployment and operation of new and/or modified service infrastructure;

• creation, deployment, modification and/or upgrading of service infrastructure deployment support tools (including Service Inventory) and processes for new and/or modified service infrastructure;

• development and promulgation of service infrastructure capacity deployment rules and controls;

• authoring, reviewing and approving operational procedures developed by Service Development & Management processes prior to service infrastructure deployment;

• the testing and acceptance of new and/or modified service infrastructure as part of the handover procedure from the Service Development & Management processes to Operations;

• detecting service infrastructure operational limitations and/or deployment incompatibilities and providing requirements to address these aspects to Service Development & Management processes;

• co-ordination and roll-out, in accordance with approved plans, of the approved new and/or modified service infrastructure;

• monitoring capacity utilization of deployed service infrastructure to provide early detection of potential service infrastructure shortfalls;

• reconfiguration and re-arrangement of under-utilized deployed service infrastructure;

• managing recovery and/or removal of obsolete or unviable service infrastructure;

• reporting on deployed service infrastructure capacity;

• Tracking and monitoring of the service infrastructure deployment processes and costs (including where service infrastructure is deployed and managed by third parties), and reporting on the capability of the service infrastructure deployment processes;

• establishing and managing service provisioning notification facilities and lists to support the Service Configuration & Activation notification and reporting processes

• updating the Service Inventory of any changes to the available service infrastructure capacity.

**L4 sub-processes:**

- **1.4.4.2.1** Plan & Forecast Service Infrastructure Requirements and Manage Capacity Planning — Planning, managing, deploying, monitoring and reporting of new and/or modified service infrastructure
- **1.4.4.2.2** Establish, Manage, and Develop Service Infrastructure Organization, Tools and Processes — Establishing, Creating, Managing, and developing organization, Tools and processes for operations of new/or modified service infrastructure.
- **1.4.4.2.3** Develop and Implement Service Infrastructure Capacity and Operational Rules and Procedures — Developing and implementing the capacity deployment rules and administrating the infrastructure operational procedures.
- **1.4.4.2.4** Perform Service Infrastructure Acceptance Test and Address & Monitor the Change — Performing acceptance test during the hand over process of new and/or modified service infrastructure. Also monitoring the new and/or modified infrastructure and addressing the operational limitations.
- **1.4.4.2.5** Monitor, Report and Release Mgmt. of Service Infrastructure and Capacity Utilization — Monitoring and reporting the capacity utilization of existing infrastructure.
- **1.4.4.2.6** Optimize Existing Service Infrastructure Utilization — Optimizing the infrastructure capacity utilization.
- **1.4.4.2.7** Update Service Inventory Record — Updating the inventory record.

### 1.4.4.3 Support Service Problem Management

**Extended Description.**

The responsibilities of the Support Service Problem Management processes are twofold - assist Service Problem Management processes by proactively undertaking statistically driven preventative and scheduled service infrastructure maintenance activities and monitoring, managing and reporting on the capability of the Service Problem Management processes.

These processes are responsible for ensuring that the service infrastructure is working effectively and efficiently.

Responsibilities of these processes include, but are not limited to:

• Extracting and analyzing, including undertaking trend analysis, historical and current service instance problem reports and performance reports to identify potential service infrastructure or service instances requiring proactive maintenance and/or replacement;

• Requesting scheduling of additional service instance data collection to assist in the analysis activity;

• Requesting scheduling of service instance performance testing to assist in analysis activity;

• Developing and managing service infrastructure and service instance proactive maintenance programs;

• Requesting service provisioning activity to prevent anticipated service problems associated with capacity limitations identified in the analysis activities;

• Reporting outcomes of trend analysis to Service Development & Management processes to influence new and/or modified service infrastructure development;

• Tracking and monitoring of the Service Problem Management processes and associated costs (including where service infrastructure is deployed and managed by third parties), and reporting on the capability of the Service Problem Management processes;

• Establishing and managing service problem notification facilities and lists to support the Service Problem Management notification and reporting processes;

**L4 sub-processes:**

- **1.4.4.3.1** Manage Service Problem & Performance Data Collection — Reviewing the trend analysis and undertaking the analysis of trouble and performance report to identify the necessary preventative activities.
- **1.4.4.3.2** Manage Service Infrastructure, Provisioning and Preventive Maintenance Schedules — Proactively undertaking statistically driven preventative and scheduled service infrastructure maintenance activities, and repair activities, and monitoring, managing and reporting on the capability of the Service Problem Management processes.
- **1.4.4.3.3** Report Service Problem Trends — Proactively generating reports based on the trend analysis.
- **1.4.4.3.4** Track, Monitor and Manage Service Problem Processes — Track, monitor and assess the service performance management processes and associated costs and report.
- **1.4.4.3.5** Provide Support for Service Problem Processes — Establishing, managing and maintaining the supporting facilities and quality management support for Service Problem management processes.

### 1.4.4.4 Enable Service Quality Management

**Extended Description.**

The responsibilities of the Enable Service Quality Management processes are twofold -support Service Quality Management processes by proactively monitoring and assessing service infrastructure performance, and monitoring, managing and reporting on the capability of the Service Quality Management processes.

Proactive management is undertaken using a range of performance parameters, whether technical, time, economic or process related.

The responsibilities of the processes include, but are not limited to:

• Undertaking proactive monitoring regimes of service infrastructure as required to ensure ongoing performance within agreed parameters over time;

• Developing and maintaining a repository of acceptable performance threshold standards for service instances to support the Service Quality Management processes;

• Undertaking trend analysis, and producing reports, of the performance of service infrastructure to identify any longer term deterioration;

• Monitoring and analyzing the service instance analyses produced by the Service Quality Management processes to identify problems that may be applicable to the service infrastructure as a whole;

• Sourcing details relating to service instance performance and analysis from the service inventory to assist in the development of trend analyses;

• Logging the results of the analysis into the service inventory repository;

• Establishing and managing service quality data collection schedules, including managing the collection of the necessary information from the Resource Data Collection & Distribution processes, to support proactive monitoring and analysis activity, and requests from Service Quality Management processes for additional data to support service instance performance analysis;

• Establishing and managing facilities to support management of planned service infrastructure and service instance outages;

• Establishing, maintaining and managing the testing of Service Quality control plans to cater for anticipated service quality disruptions;

• Proactively triggering the instantiation of control plans to manage performance through programmed and/or foreseen potentially disruptive events, i.e. anticipated traffic loads on Xmas day, planned outages, etc.;

• Tracking and monitoring of the Service Quality Management processes and associated costs (including where service infrastructure is deployed and managed by third parties), and reporting on the capability of the Service Quality Management processes;

• Establishing and managing service quality notification facilities and lists to support the Service Quality Management notification and reporting processes

• Supporting the Support Customer QoS/SLA Management process.

**L4 sub-processes:**

- **1.4.4.4.1** Establish and Maintain Service Performance Threshold Standards — Establishing and maintaining the rules and standards for performance threshold
- **1.4.4.4.2** Monitor and Analyze Service Performance Reports, and Identify Issues — Review the service performance management operational report prepared by resource performance management processes.
- **1.4.4.4.3** Correlate the Service Performance Problem Reports & Manage Inventory Repository — Correlating the Performance issues identified based on the performance report review and logging the results in inventory repository.
- **1.4.4.4.4** Manage Service Performance Data Collection — Developing and managing the service performance data collection schedules and supporting the monitoring activities to gather the resource performance data.
- **1.4.4.4.5** Assess and Report Service Quality Management Processes — Track, monitor and assess the service performance management processes and associated costs and report.

### 1.4.4.5 Support Service & Specific Instance Rating

**Extended Description.**

The purpose of the Support Service & Specific Instance Rating processes ensure that rating and tariff information is maintained for each service class, for use by Service & Specific Instance Rating. They are also responsible for the processing of this information related to administration of the services

### 1.4.4.6 Manage Service Test

**Extended Description.**

Manage Service Test process manages the end-to-end execution of a test or test scenario for services not specific to a customer. Tests can be manual or automated.

Service Test Management processes rely on Product and Resource Test Management processes due to dependencies between product tests and resource tests.

Service Test Management includes:

- Identification of service tests needed according to fulfillment and assurance issues

- triggering of service tests in manual or automated mode

- Execution of service tests

- Verification of test authorization (role and context) and quota management

- Identification and prioritization of tests

- Setting up the test context and configuration

- Triggering appropriate product and resource Tests

- Tests can be on-demand or planned according to specific needs

- Enrichment with product and resource tests results based on applicable service test rules

- Reporting of test results

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.4.4.1** Manage Service Inventory — Establish, manage and administer the enterprise's service inventory, as embodied in the Service Inventory Database, and monitor and report on the usage and access to the service inventory, and the quality of the data maintained in it.
- **1.4.4.2** Enable Service Configuration & Activation — Planning and deployment of service infrastructure, and for ensuring availability of sufficient service infrastructure to support the Service Configuration & Activation processes.
- **1.4.4.3** Support Service Problem Management — Assist Service Problem Management processes by proactively undertaking statistically driven preventative and scheduled service infrastructure maintenance activities and monitoring, managing and reporting on the capability of the Service Problem Management processes.
- **1.4.4.4** Enable Service Quality Management — Support Service Quality Management processes by proactively monitoring and assessing service infrastructure performance, and monitoring, managing and reporting on the capability of the Service Quality Management processes.
- **1.4.4.5** Support Service & Specific Instance Rating — Ensure that rating and tariff information is maintained for each service class, for use by Service & Specific Instance Rating
- **1.4.4.6** Manage Service Test — Manage Service Test process manages the end-to-end execution of a test or test scenario for services not specific to a customer. Tests can be manual or automated.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/production]]
- [[wiki/oda/functional-blocks/intelligence-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Service Process Decompositions PDF (GB921_Service_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

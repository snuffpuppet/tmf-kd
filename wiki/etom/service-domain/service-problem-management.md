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
l2_id: "1.4.6"
l2_name: "Service Problem Management"
---

# Service Problem Management

> **Vertical context:** Assurance ([[wiki/foundations/lifecycle]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

## Overview

Service Problem Management processes are responsible for the management of problems associated with specific services.  The objective of these processes is to respond immediately to reported service problems or failures in order to minimize their effects on customers, and to invoke the restoration of the service, or provide an alternate service as soon as possible.
Responsibilities of the Service Problem Management processes include, but are not limited to:
• Detecting, analyzing, managing and reporting on service alarm event notifications; 
• Initiating and managing service trouble reports;
• Performing service problem localization analysis; 
• Correcting and resolving service problems;
• Reporting progress on service trouble reports to other processes;
• Assigning & tracking service problem testing and recovery activities 
• Managing service problem jeopardy conditions
Service Problem Management processes perform analysis, decide on the appropriate actions/responses and carry them out with the intent of restoring normal operation on specific services. 
However these activities need to interact with the Problem Handling processes, as the latter have a view on customer impact.  Service Problem Management processes are responsible for informing Problem Handling processes of any potential customer problems.  Where the original report arose as a result of customer problems, the Service Problem Management processes may be coordinated by Problem Handling processes.

— GB921 v25.5 Excel master, process ID `1.4.6`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.4.6.1 Create Service Trouble Report

**Extended Description.**

The objective of the Create Service Trouble Report process is to create a new service trouble report.

A new service trouble report may be created as a result of service alarm event notification analysis, and subsequent creation of new service alarm event records, undertaken by the Survey & Analyze Service Problem processes, or at the request of analysis undertaken by other processes in the Customer ( in particular a Customer Problem Report can generate one or more Service Trouble Reports), Service or Resource Domains which detect that some form of failure has occurred for which service restoration activity is required to restore normal operation.

If the service trouble report is created as a result of a notification or request from processes other than the Survey & Analyze Service Problem processes, the Create Service Trouble Report processes are responsible for converting the received information into a form suitable for the Service Problem Management processes, and for requested additional information if required.

These processes will make estimates of the time to restore service which will be included in the new service trouble report so that other processes can gain access to this information.

**L4 sub-processes:**

- **1.4.6.1.1** Generate Service Problem — This process creates a new Service Trouble report.
- **1.4.6.1.2** Convert Report To Service Problem Format — Not used for this process element.
- **1.4.6.1.3** Estimate Time For Restoring Service — This process estimates the time to restore service which is included in the new Service Trouble report so that other processes can gain access to this information.

### 1.4.6.2 Diagnose Service Problem

**Extended Description.**

The objective of the Diagnose Service Problem processes is to identify the root cause of the specific service problem. These processes are invoked by the Track & Manage Service Problem processes.

The responsibilities of these processes include, but are not limited to:

• Verifying whether the service configuration matches the appropriate product features;

• Performing diagnostics against the specific services;

• Running tests against the specific services;

• Starting and stopping audits against specific services

• Scheduling routine testing of the specific services.

The Diagnose Service Problem processes will make the results of the root cause analysis available to other processes. The Diagnose Service Problem processes will update the open service trouble report, as required during the assessment, and when the root cause has been identified.

When the process is complete the Diagnose Service Problem processes will notify the Track & Manage Service Problem processes.

**L4 sub-processes:**

- **1.4.6.2.1** Verify Service Configuration — This process verifies whether the service configuration matches the appropriate product features.
- **1.4.6.2.2** Perform Specific Service Problem Diagnostics — This process performs diagnostics against the specific services.
- **1.4.6.2.3** Perform Specific Service Problem Tests — This process runs tests against the specific services.
- **1.4.6.2.5** Stop And Start Audit On Services — This process starts and stops audits against specific services.
- **1.4.6.2.6** Notify T&M Root Cause Service Problem — Not used for this process element.
- **1.4.6.2.7** Categorize Service Problem — This process is responsible for categorizing the service problem according to the type of the problem, impact, and standardized criteria at SM&O level. Moreover, this activity will be carried out with appropriate diligence, in order to provide inputs to the "Track & Manage Service Problem" process.

### 1.4.6.3 Correct & Resolve Service Problem

**Extended Description.**

The objective of the Correct & Resolve Service Problem processes is to restore the service to a normal operational state as efficiently as possible.

Based on the nature of the service failure leading to the associated service alarm event notification, automatic restoration procedures might be triggered. Manual restoration activity is assigned to the Correct & Resolve Service Problem processes from the Track & Manage Service Problem processes.

Depending on the nature of the specific service failure, these processes may possibly re-assign services or re-configure service parameters.

For large service failures requiring extensive re-assignment and/or re-configuration activity to restore normal operation, these processes will attempt to implement work-arounds to recover the specific service operation. In these circumstances, recovery of normal operation may require invocation of the Support Service Problem Management processes.

They will also report successful restoration of normal service operation, restoration through temporary work-arounds or an unsuccessful attempt at service restoration to Track & Manage Service Problem through updates to the associated service trouble report.

**L4 sub-processes:**

- **1.4.6.3.1** Reassign / Reconfigure Failed Service — Not used for this process element.
- **1.4.6.3.2** Manage Service Restoration — Not used for this process element.
- **1.4.6.3.3** Implement Service Problem Work Arounds — Not used for this process element.
- **1.4.6.3.4** Invoke Support Service Problem Management Processes — Not used for this process element.
- **1.4.6.3.5** Review Major Service Problem — To review the resolution of service problems that have been categorized as major impact, in order to prevent recurrence and learn lessons for the future.

### 1.4.6.4 Track & Manage Service Problem

**Extended Description.**

The purpose of the Track & Manage Service Problem processes is to ensure that testing, repair and restoration activities are assigned, coordinated and tracked efficiently, and that escalation is invoked as required for any open service trouble reports in jeopardy.

Responsibilities of these processes include, but are not limited to:

• Initiating first-in testing using automated remote testing capabilities;

• Adding additional information to an open service trouble report based on the first-in testing;

• Scheduling, assigning and coordinating repair and restoration activities;

• Generating the respective resource trouble report creation request(s) to Create Resource Trouble Report based on specific service trouble reports;

• Initiate any final testing to confirm clearance of the service problem;

• Undertake necessary tracking of the execution progress;

• Modifying information in an existing service trouble report based on assignments;

• Modifying the service trouble report status;

• Canceling a service trouble report when the specific problem was related to a false service alarm event

• Monitoring the jeopardy status of open service trouble reports, and escalating service trouble reports as necessary.

Note that some specific resource components may be owned and managed by other parties. In these cases the Track & Manage Service Problem process is responsible for initiating requests, through Party Problem Handling processes for restoration and recovery by the party related to the specific resource components.

These processes will co-ordinate all the actions necessary in order to guarantee that all tasks are finished at the appropriate time and in the appropriate sequence.

The Track & Manage Service Problem processes are responsible for engaging external parties in correction and recovery activities when:

• higher level expertise and/or higher level support is required to resolve the service problem, (which may be automatic in the case of highest priority service problems);

• the specific service has been purchased from an external party (as in an interconnect service).

• the specific service is delivered by an external party.

Where the engagement with an external party is for purchased or delivered services, as the case may be, the tracking and management of the party problem resolution activity is actually performed by the Party Problem Handling processes, with the Track & Manage Service Problem processes relegated to an overall coordination role. The Track & Manage Service Problem processes will also inform the Close Service Problem processes by modifying the service trouble report status to cleared when the service problem has been resolved.

**L4 sub-processes:**

- **1.4.6.4.1** Coordinate Service Problem — Not used for this process element.
- **1.4.6.4.2** Perform First in Service Testing — This process initiates first-in testing using automated remote testing capabilities, and adds additional information to an open Service Trouble report based on the first-in testing.
- **1.4.6.4.3** Cancel Service Problem — This process cancels a Service Trouble report when the specific trouble was related to a false alarm event.
- **1.4.6.4.4** Escalate/End Service Problem — Not used for this process element.
- **1.4.6.4.5** Perform Final Service Test — This process initiates any final testing to confirm clearance of the Service Problem.
- **1.4.6.4.6** Prioritize Service Problem — This process is responsible for assigning the prioritization to service problem in order to establish an order for managing it. The prioritization is assigned (usually automatically) according to criteria, such as, categorization, services affected and SL

### 1.4.6.5 Report Service Problem

**Extended Description.**

The objective of the Report Service Problem processes is to monitor the status of service trouble reports, provide notifications of any changes and provide management reports.

These processes are responsible for continuously monitoring the status of service trouble reports and managing notifications to processes and other parties registered to receive notifications of any status changes, for example, Service Quality Management and Customer QoS/SLA Management processes. Notification lists are managed and maintained by the Support Service Problem Management processes.

These processes record, analyze and assess the service trouble report status changes to provide management reports and any specialized summaries of the efficiency and effectiveness of the overall Service Problem Management process. These specialized summaries could be specific reports required by specific audiences.

These processes will make the necessary reports about the problem that occurred, the root cause and the activities carried out for restoration.

**L4 sub-processes:**

- **1.4.6.5.1** Monitor Service Problem — Not used for this process element.
- **1.4.6.5.2** Distribute Service Problem Notifications — This process makes the necessary reports about the Service Problem that occurred, the root cause and the activities carried out for restoration.
- **1.4.6.5.3** Distribute Service Problem Management Reports & Summaries — Not used for this process element.

### 1.4.6.6 Close Service Trouble Report

**Extended Description.**

The objective of the Close Service Trouble Report processes is to close a service trouble report when the service problem has been resolved.

These processes monitor the status of all open service trouble reports, and recognize that a service trouble report is ready to be closed when the status is changed to cleared.

### 1.4.6.7 Survey & Analyze Service Problem

**Extended Description.**

The objective of the Survey & Analyze Service Problem processes is to monitor service alarm event notifications and manage service alarm event records in real-time.

Responsibilities of the Survey & Analyze Service Problem processes include, but are not limited to:

• Detecting and collecting service alarm event notifications;

• Initiating and managing service alarm event records;

• Performing service alarm event notification localization analysis;

• Correlating and filtering service alarm event records;

• Reporting service alarm event record status changes to other processes;

• Managing service alarm event record jeopardy conditions.

Service alarm event notification analysis encompasses the identification of the service alarm event in terms of reporting entity and nature of the service alarm event. It will then analyze the service alarm events based on a number of criteria and then suppress redundant, transient or implied service alarm events by means of filtering and correlation. It includes the notification of new service alarm event records, or status changes of previously reported service alarm event records, as well as abatement messages when service alarm event records have been cleared.

The analysis will correlate service alarm event notifications to planned outage notifications to remove false service alarm event notifications arising as a result of the planned outage activity.

These processes may determine that a service alarm event notification may represent a customer impacting condition. In these circumstances this process is responsible for indicating a potential customer problem to the Problem Handling processes. As a part of this indication this process is responsible for identifying the impacted deployed product instances associated with the service instances presenting alarm event notifications and passing this information to the Problem Handling processes.

Service alarm event record correlation and filtering encompasses the correlation of redundant, transient or implied service alarm event notifications with a specific “root cause” service alarm event notification and associated service alarm event record.

The Survey & Analyze Service Problem processes might trigger a well-defined action based on specific service alarm event notification information as well as the non-arrival of service alarm event notification information after a specific time interval has elapsed.

These processes are also responsible for monitoring and triggering the appropriate action when a service alarm event record is not cleared within a pre-defined period of time.

**L4 sub-processes:**

- **1.4.6.7.1** Manage Service Alarm Event Notifications — Not used for this process element.
- **1.4.6.7.2** Filter Service Alarm Event Notifications — This process encompasses the correlation of redundant, transient or implied service alarm event notifications with a specific “root cause” service alarm event notification and associated service alarm event record.
- **1.4.6.7.3** Correlate Service Alarm Event Notifications — Not used for this process element.
- **1.4.6.7.4** Abate Service Alarm Event Records — This process includes the notification of new service alarm event records, or status changes of previously reported service alarm event records, as well as abatement messages when service alarm event records have been cleared.
- **1.4.6.7.5** Trigger Defined Service Alarm Action — Not used for this process element.
- **1.4.6.7.6** Monitor Service Alarms Events — This process is responsible for collecting and monitoring events and alarms provided by services though systems and monitoring tools.
- **1.4.6.7.7** Categorize Service Alarm Event — This process is responsible for categorizing the service alarm events in order to support the management, filtering and correlation of events at SM&O level.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.4.6.1** Create Service Trouble Report — Create a new service trouble report.
- **1.4.6.2** Diagnose Service Problem — Identify the root cause of the specific service problem, including those service problems related to security events.
- **1.4.6.3** Correct & Resolve Service Problem — Restore the service to a normal operational state as efficiently as possible
- **1.4.6.4** Track & Manage Service Problem — Ensure that testing, repair and restoration activities are assigned, coordinated and tracked efficiently, and that escalation is invoked as required for any open service trouble reports in jeopardy
- **1.4.6.5** Report Service Problem — Monitor the status of service trouble reports, provide notifications of any changes and provide management reports.  This includes service trouble caused by security events.
- **1.4.6.6** Close Service Trouble Report — Close a service trouble report when the service problem has been resolved
- **1.4.6.7** Survey & Analyze Service Problem — Monitor service alarm event notifications and manage service alarm event records in real-time.  Service alarm events include security event alarms.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Service Process Decompositions PDF (GB921_Service_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

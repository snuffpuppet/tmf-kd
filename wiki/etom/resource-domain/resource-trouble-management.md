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
l1_parent: "1.5 Resource Domain"
l2_id: "1.5.8"
l2_name: "Resource Trouble Management"
---

# Resource Trouble Management

> **Vertical context:** Assurance ([[wiki/foundations/lifecycle]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Trouble Management processes are responsible for the management of troubles, including security events, associated with specific resources. The objectives of these processes are to efficiently and effectively manage reported resource trouble, isolate the root cause and act to resolve the resource trouble. 

Responsibilities of the Resource Trouble Management processes include, but are not limited to:

• Detecting, analyzing, managing and reporting on resource alarm event notifications; 
• Initiating and managing resource trouble reports;
• Performing resource trouble localization analysis; 
• Correcting and resolving resource trouble;
• Reporting progress on resource trouble reports to other processes;
• Assigning & tracking resource trouble testing and repair activities 
• Managing resource trouble jeopardy conditions.

On one hand, resource troubles may relate to Problems in the Service domain and therefore also potentially in the customer domain. On the other hand, they may relate to specific resource failures or performance degradations, which are caused by resource faults.
As such, the Resource Trouble Management processes work with specific resource alarm event notifications received from Resource Data Collection & Distribution, specific resource performance notifications from Resource Performance Management, and potential specific resource trouble notifications from Service Problem Management processes.

Resource Trouble Management processes perform analysis, decide on the appropriate actions/responses and carry them out with the intent of restoring normal operation on specific resources. 
However these activities need to interact with the Service Problem Management processes, as the latter have a view on service impact.  Resource Trouble Management processes are responsible for informing Service Problem Management of any potential service problems.  Where the original report arose as a result of service problems, the Resource Trouble Management processes may be coordinated by Service Problem Management processes.

— GB921 v25.5 Excel master, process ID `1.5.8`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.5.8.1 Survey & Analyze Resource Trouble

**Extended Description.**

The objective of the Survey & Analyze Resource Trouble processes is to monitor resource alarm event notifications and manage resource alarm event records in real-time.

Responsibilities of the Survey & Analyze Resource Trouble processes include, but are not limited to:

• Detecting and collecting resource alarm event notifications;

• Initiating and managing resource alarm event records;

• Performing resource alarm event notification localization analysis;

• Correlating and filtering resource alarm event records;

• Reporting resource alarm event record status changes to other processes

• Managing resource alarm event record jeopardy conditions.

Resource alarm event notification analysis encompasses the identification of the resource alarm event in terms of reporting entity and nature of the resource alarm event. It will then analyze the resource alarm events based on a number of criteria and then suppress redundant, transient or implied resource alarm events by means of filtering and correlation. It includes the notification of new resource alarm event records, or status changes of previously reported resource alarm event records, as well as abatement messages when resource alarm event records have been cleared.

The analysis will correlate resource alarm event notifications to planned outage notifications to remove false resource alarm event notifications arising as a result of the planned outage activity.

These processes may determine that a resource alarm event notification may represent a service impacting condition. In these circumstances this process is responsible for indicating a potential service problem to the Service Problem Management processes. As a part of this indication this process is responsible for identifying the impacted service instances associated with the resource instances presenting alarm event notifications and passing this information to the Service Problem Management processes.

Resource alarm event record correlation and filtering encompasses the correlation of redundant, transient or implied resource alarm event notifications with a specific “root cause” resource alarm event notification and associated resource alarm event record.

The Survey & Analyze Resource Trouble processes might trigger a well-defined action based on specific resource alarm event notification information as well as the non-arrival of resource alarm event notification information after a specific time interval has elapsed.

These processes are also responsible for monitoring and triggering the appropriate action when a resource alarm event record is not cleared within a pre-defined period of time.

**L4 sub-processes:**

- **1.5.8.1.1** Manage Resource Alarm Event Notifications — Not used for this process element.
- **1.5.8.1.2** Filter Resource Alarm Event Notifications — Not used for this process element.
- **1.5.8.1.3** Correlate Resource Alarm Event Notifications — Not used for this process element.
- **1.5.8.1.4** Abate Alarm Event Records — This process includes the notification of new resource alarm event records, or status changes of previously reported resource alarm event records, as well as abatement messages when resource alarm event records have been cleared.
- **1.5.8.1.5** Trigger Defined Action — Not used for this process element.
- **1.5.8.1.6** Monitor Resource Alarms Events — This process is responsible for collecting and monitoring events and alarms provided by resources though systems and monitoring tools.
- **1.5.8.1.7** Categorize Resource Alarm Event — This process is responsible for categorizing the resource alarm events in order to support the management, filtering and correlation of events at Resource-Ops level.

### 1.5.8.2 Localize Resource Trouble

**Extended Description.**

The objective of the Localize Resource Trouble processes is to identify the root cause of the specific resource trouble. These processes are invoked by the Track & Manage Resource Trouble processes.

The responsibilities of these processes include, but are not limited to:

•Verifying whether the resource configuration matches the appropriate service features;

•Performing diagnostics against the specific resources;•

•Running tests against the specific resources;

•Starting and stopping audits against specific resources

•Scheduling routine testing of the specific resources.

The Localize Resource Trouble processes will make the results of the root cause analysis available to other processes. The Localize Resource Trouble processes will update the open resource trouble report, as required during the assessment, and when the root cause has been identified.

When the process is complete the Localize Resource Trouble processes will notify the Track & Manage Resource Trouble processes.

**L4 sub-processes:**

- **1.5.8.2.1** Verify Resource Configuration — This process verifies whether the resource configuration matches the appropriate service features.
- **1.5.8.2.2** Perform Specific Resource Trouble Diagnostics — This process performs diagnostics against the specific resources. This includes application of signatures and other methods to capture anomalous events or malware.
- **1.5.8.2.3** Perform Specific Resource Trouble Tests — This process runs tests against the specific resources. This can include penetration tests to check for vulnerabilities.
- **1.5.8.2.4** Stop And Start Audit On Resources — This process starts and stops audits against specific resources.
- **1.5.8.2.6** Notify T&M Root Cause Resource Trouble — Not used for this process element.
- **1.5.8.2.7** Categorize Resource Trouble — This process is responsible for categorizing the resource trouble according to the type of the trouble, impact, and standardized criteria at Resource-Ops level. Moreover, this activity will be carried out with appropriate diligence, in order to provide inputs to the "Track & Manage Resource Trouble" process.

### 1.5.8.3 Correct & Resolve Resource Trouble

**Extended Description.**

The objective of the Correct & Resolve Resource Trouble processes is to restore or replace resources that have failed as efficiently as possible.

Based on the nature of the resource failure leading to the associated resource alarm event notification, automatic restoration procedures might be triggered. Manual restoration activity is assigned to the Correct & Resolve Resource Trouble processes from the Track & Manage Resource Trouble processes.

Depending on the nature of the specific resource failure, these processes may possibly repair or replace the failed unit or specific resource. These processes are also responsible for

- to isolate a unit with a fault

- to manage the redundant resource units (e.g. hot standby)

- to (auto) heal a resource

- to identify the root cause of failure

- to repair failed specific resource (including hardware failure and software failure)

For large resource failures requiring extensive repair and/or replacement activity to restore normal operation, these processes will attempt to implement work-arounds to recover the specific resource operation. In these circumstances, recover of normal operation may require invocation of the Support Resource Trouble Management processes.

They will also report successful restoration of normal operation, restoration through temporary work-arounds or an unsuccessful attempt at restoration to Track & Manage Resource Trouble through updates to the associated resource trouble report.

**L4 sub-processes:**

- **1.5.8.3.1** Repair / Replace Failed Resource — This process may possibly repair, reconfigure, or replace the failed unit or specific resource (including hardware failure and software failure).
- **1.5.8.3.2** Isolate Unit with Fault — This process is responsible for isolating a unit with a fault.
- **1.5.8.3.3** Manage Standby Resource Units — This process is responsible for managing the redundant resource units (e.g. hot standby).
- **1.5.8.3.4** Implement Resource Trouble Work Arounds — Not used for this process element.
- **1.5.8.3.5** Invoke Support Resource Trouble Management Processes — Not used for this process element.
- **1.5.8.3.6** Review Major Resource Trouble — To review the resolution of resource troubles that have been categorized as major impact, in order to prevent recurrence and learn lessons for the future.
- **1.5.8.3.7** Probe Root Cause Of Failure — Probe the root cause of failure to identify repair point and prevention of recurrence.
- **1.5.8.3.8** Self Heal Resource Trouble — Self Heal failed resource before identification of root cause of failure.

### 1.5.8.4 Track & Manage Resource Trouble

**Extended Description.**

The objective of the Track & Manage Resource Trouble is to ensure testing, repair and restoration activities are assigned, coordinated and tracked efficiently, and that escalation is invoked as required for any open resource trouble reports in jeopardy. Responsibilities of these processes include, but are not limited to:

•Initiating first-in testing using automated remote testing capabilities;

•Adding additional information to an open resource trouble report based on the first-in testing;

•Scheduling, assigning and coordinating repair and restoration activities;

•Initiate any final testing to confirm clearance of the service problem;

•Undertake necessary tracking of the execution progress;

•Modifying information in an existing resource trouble report based on assignments;

•Modifying the resource trouble report status;

•Canceling a resource trouble report when the specific trouble was related to a false alarm event

•Monitoring the jeopardy status of open resource trouble reports, and escalating resource trouble reports as necessary.

These processes will co-ordinate all the actions necessary in order to guarantee that all tasks are finished at the appropriate time and in the appropriate sequence.

The Track & Manage Resource Trouble processes are responsible for engaging external suppliers in correction and recovery activities when higher level expertise and/or higher level support is required to resolve the resource trouble. This engagement can be linked to the priority of the resource trouble report, and could occur automatically for highest priority resource trouble reports.

The Track & Manage Resource Trouble processes will also inform the Close Resource Trouble processes by modifying the resource trouble report status to cleared when the resource trouble has been resolved.

**L4 sub-processes:**

- **1.5.8.4.1** Coordinate Resource Trouble — Not used for this process element.
- **1.5.8.4.2** Perform First in Testing — This process initiates first-in testing using automated remote testing capabilities, and adds additional information to an open resource trouble report based on the first-in testing.
- **1.5.8.4.3** Cancel Resource Trouble — This process cancels a resource trouble report when the specific trouble was related to a false alarm event.
- **1.5.8.4.4** Escalate/End Resource Trouble — Not used for this process element.
- **1.5.8.4.5** Perform Final Test — This process initiates any final testing to confirm clearance of the service problem.
- **1.5.8.4.6** Engaging External Suppliers — Not used for this process element.
- **1.5.8.4.7** Prioritize Resource Trouble — This process is responsible for assigning the prioritization to resource trouble in order to establish an order for managing it. The prioritization is assigned (usually automatically) according to criteria, such as, categorization and resources affected.

### 1.5.8.5 Report Resource Trouble

**Extended Description.**

The objective of the Report Resource Trouble processes is to monitor the status of resource trouble reports, provide notifications of any changes and provide management reports.

These processes are responsible for continuously monitoring the status of resource trouble reports and managing notifications to processes and other parties registered to receive notifications of any status changes, for example, Resource Performance Management and Service Quality Management. Notification lists are managed and maintained by the Support Resource Trouble Management processes.

These processes record, analyze and assess the resource trouble report status changes to provide management reports and any specialized summaries of the efficiency and effectiveness of the overall Resource Trouble Management process. These specialized summaries could be specific reports required by specific audiences.

These processes will make the necessary reports about the resource trouble that occurred, the root cause and the activities carried out for restoration.

**L4 sub-processes:**

- **1.5.8.5.1** Monitor Resource Trouble — Not used for this process element.
- **1.5.8.5.2** Distribute Notifications — This process makes the necessary reports about the Service Problem that occurred, the root cause and the activities carried out for restoration.
- **1.5.8.5.3** Distribute Management Reports & Summaries — Not used for this process element.

### 1.5.8.6 Close Resource Trouble Report

**Extended Description.**

The objective of the Close Service Trouble Report processes is to close a service trouble report when the service problem has been resolved.

These processes monitor the status of all open service trouble reports, and recognize that a service trouble report is ready to be closed when the status is changed to cleared.

### 1.5.8.7 Create Resource Trouble Report

**Extended Description.**

The objective of the Create Resource Trouble Report process is to create a new resource trouble report.

A new resource trouble report may be created as a result of resource alarm event notification analysis, and subsequent creation of new resource alarm event records, undertaken by the Survey & Analyze Resource Trouble processes, or at the request of analysis undertaken by other processes in the Service-Ops or Resource-Ops (in particular a Service Trouble Report can generate one or more Resource Trouble Reports) or Engaged Party-Ops and Resource-Ops layers which detect that some form of failure has occurred for which resource restoration activity is required to restore normal operation.

If the resource trouble report is created as a result of a notification or request from processes other than the Survey & Analyze Resource Trouble processes, the Create Resource Trouble Report processes are responsible for converting the received information into a form suitable for the Resource Trouble Management processes, and for requesting additional information if required.

These processes will make estimates of the time to restore resource which will be included in the new resource trouble report so that other processes can gain access to this information.

**L4 sub-processes:**

- **1.5.8.7.1** Generate Resource Trouble — This process creates a new resource trouble report.
- **1.5.8.7.2** Convert Report To Resource Trouble Format — Not used for this process element.
- **1.5.8.7.3** Estimate Time For Restoring Resource — This process estimates the time to restore service which is included in the new Service Trouble report so that other processes can gain access to this information.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.5.8.1** Survey & Analyze Resource Trouble — Monitor resource alarm event notifications and manage resource alarm event records in real-time.  Resource alarm event notifications include those alarms related to security events.
- **1.5.8.2** Localize Resource Trouble — Perform analysis to identify the root cause of the specific resource trouble including those resource troubles related to security events.
- **1.5.8.3** Correct & Resolve Resource Trouble — Restore or replace resources that have failed as efficiently as possible
- **1.5.8.4** Track & Manage Resource Trouble — Ensure testing, repair and restoration activities are assigned, coordinated and tracked efficiently, and that escalation is invoked as required for any open resource trouble reports in jeopardy
- **1.5.8.5** Report Resource Trouble — Monitor the status of resource trouble reports provide notifications of any changes and provide management reports. This includes resource trouble caused by security events.
- **1.5.8.6** Close Resource Trouble Report — Close a resource trouble report when the resource problem has been resolved
- **1.5.8.7** Create Resource Trouble Report — Create a new resource trouble report

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
  Resource Process Decompositions PDF (GB921_Resource_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

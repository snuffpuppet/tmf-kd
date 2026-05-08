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
l2_id: "1.5.9"
l2_name: "Resource Performance Management"
---

# Resource Performance Management

> **Vertical context:** Assurance ([[wiki/foundations/lifecycle]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Performance Management processes encompass managing, tracking, monitoring, analyzing, controlling and reporting on the performance of specific resources. They work with basic information received from the Resource Data Collection & Distribution processes.

If the analysis identifies a resource performance violation or a potential service performance violation, information will be passed to Resource Trouble Management and/or Service Quality Management as appropriate. The latter processes are responsible for deciding on and carrying out the appropriate action/response. This may include requests to the Resource Performance Management processes to install controls to optimize the specific resource performance.
The Resource Performance Management processes will continue to track the resource performance problem, ensuring that resource performance is restored to a level required to support services.

— GB921 v25.5 Excel master, process ID `1.5.9`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.5.9.1 Monitor Resource Performance

**Extended Description.**

The objective of the Monitor Resource Performance processes is to monitor received resource performance information and undertake first-in detection.

The responsibilities of the processes include, but are not limited to:

•Undertaking the role of first in detection by monitoring the received specific resource performance data;

•Comparing the received specific resource performance data to performance standards set for each specific resource (available from the Resource Inventory);

•Assessing and recording received specific resource performance data which is within tolerance limits for performance standards, and for which continuous monitoring and measuring of specific resource performance is required;

•Recording the results of the continuous monitoring for reporting through the Report Resource Performance processes;

•Detecting performance threshold violations which represent specific resource failures due to abnormal performance;

•Passing information about resource failures due to performance threshold violations to Resource Trouble Management to manage any necessary restoration activity as determined by that process;

•Passing information about potential specific service performance degradations arising from specific resource degradations to Service Quality Management to manage any necessary restoration activity as determined by that process;

•Detecting performance degradation for specific resources which provide early warning of potential issues;

•Forwarding resource performance degradation notifications to other Resource Performance Management processes, which manage activities to restore normal specific resource performance

•Logging specific resource performance degradation and violation details within the repository in the Manage Resource Inventory processes to ensure historical records are available to support the needs of other processes.

**L4 sub-processes:**

- **1.5.9.1.1** Manage Resource Performance Data — Not used for this process element.
- **1.5.9.1.2** Record Resource Performance Data — Not used for this process element.
- **1.5.9.1.3** Correlate Resource Performance Event Notifications — Not used for this process element.

### 1.5.9.2 Analyze Resource Performance

**Extended Description.**

The objective of the Analyze Resource Performance processes is to analyze the information received from the Monitor Resource Performance process to evaluate the performance of a specific resource.

The responsibilities of the processes include, but are not limited to:

•Undertaking analysis as required on specific resource performance information received from the Monitor Resource Performance processes;

•Initiating, modifying and cancelling continuous performance data collection schedules for specific resources required to analyze specific resource performance. These schedules are established through requests sent to the Enable Resource Data Collection & Distribution processes;

•Determining the root causes of specific resource performance degradations and violations;

•Recording the results of the analysis and intermediate updates in the Resource Inventory for historical analysis and for use as required by other processes

•Undertaking specific detailed analysis (if the original requested came from Service Quality Management processes) to discover the root cause of service performance degradations that may be arising due to interactions between resource instances, without any specific resource instance having an unacceptable performance in its own right.

**L4 sub-processes:**

- **1.5.9.2.1** Perform Specific Resource Performance Diagnostics — Not used for this process element.
- **1.5.9.2.2** Manage Resource Performance Data Collection Schedules — Not used for this process element.

### 1.5.9.3 Control Resource Performance

**Extended Description.**

The objective of the Control Resource Performance processes is to apply controls to resource instances in order to optimize the resource performance.

The responsibilities of the processes include, but are not limited to:

•Instantiating controls to attempt to restore resource instances to normal operation, at the request of Analyze Resource Performance processes. These controls may be based on established control plans, or the controls may be developed within the Control Resource Performance processes depending on circumstances.

•Instantiating controls to attempt to restore failed resource instances to normal operation, at the request of Resource Trouble Management or Service Quality Management processes. These controls may be based on established control plans, or the controls may be developed within the Control Resource Performance process depending on circumstances.

**L4 sub-processes:**

- **1.5.9.3.1** Instantiate Resource Performance Controls — Not used for this process element.
- **1.5.9.3.2** Instantiate Resource Trouble Controls — Not used for this process element.

### 1.5.9.4 Report Resource Performance

**Extended Description.**

The objective of the Report Resource Performance processes is to monitor the status of resource performance degradation reports, provide notifications of any changes and provide management reports.

These processes are responsible for continuously monitoring the status of resource performance degradation reports and managing notifications to other processes in the Resource-Ops and other layers, and to other parties registered to receive notifications of any status changes. Notification lists are managed and maintained by the Enable Resource Performance Management processes.

These processes record, analyze and assess the resource performance degradation report status changes to provide management reports and any specialized summaries of the efficiency and effectiveness of the overall Resource Performance Management process. These specialized summaries could be specific reports required by specific audiences.

**L4 sub-processes:**

- **1.5.9.4.1** Monitor Resource Performance Degradation Report — Not used for this process element.
- **1.5.9.4.2** Distribute Resource Quality Management Reports & Summaries — Not used for this process element.

### 1.5.9.5 Create Resource Performance Degradation Report

**Extended Description.**

The objective of the Create Resource Performance Degradation Report process is to create a new resource performance degradation report, modify existing resource performance degradation reports, and request cancellation of existing resource performance degradation reports.

A new resource performance degradation report may be created as a result of specific resource performance notifications undertaken by the Monitor Resource Performance processes, or at the request of analysis undertaken by other Service-Ops or Resource-Ops or party management processes which detect that some form of deterioration or failure has occurred requires an assessment of the specific resource performance.

If the resource performance degradation report is created as a result of a notification or request from processes other than Monitor Resource Performance processes, the Create Resource Performance Degradation Report processes are responsible for converting the received information into a form suitable for the Resource Performance Management processes, and for requesting additional information if required.

**L4 sub-processes:**

- **1.5.9.5.1** Generate Resource Performance Degradation Problem — Not used for this process element.
- **1.5.9.5.2** Convert Report To Resource Performance Degradation Report Format — Not used for this process element.

### 1.5.9.6 Track & Manage Resource Performance Resolution

**Extended Description.**

The objective of the Track & Manage Resource Performance Resolution processes is to efficiently assign, coordinate and track specific resource performance analysis and control activities, and escalate any open resource performance degradation reports in jeopardy.

Responsibilities of these processes include, but are not limited to:

• Adding additional information to an open resource performance degradation report based on the first-in and on-going analysis;

• Scheduling, assigning and coordinating analysis and specific resource performance restoration activities and/or repair activities delegated to other processes;

• Generating the respective other parties problem report creation request(s) to Initiate other parties Problem Report processes based on specific resource performance degradation reports where analysis the root cause is related to other parties products;

• Modifying information in an existing resource performance degradation report based on assignments;

• Modifying the resource performance degradation report status;

• Canceling a resource performance degradation report when the specific request was related to a false resource failure event

• Monitoring the jeopardy status of open resource performance degradation reports, and escalating resource performance degradation reports as necessary.

These processes will co-ordinate all the actions necessary in order to guarantee that all tasks are finished at the appropriate time and in the appropriate sequence.

The Track & Manage Resource Performance Resolution processes will also inform the Close Resource Performance Degradation Report processes by modifying the resource performance degradation report status to cleared when the specific resource performance issues have been resolved.

**L4 sub-processes:**

- **1.5.9.6.1** Coordinate Resource Performance — Not used for this process element.
- **1.5.9.6.2** Request Other Parties Performance Degradation Report Creation and Update — Not used for this process element.
- **1.5.9.6.3** Update First in Resource Testing Results — This process adds additional information to an open Resource Performance Degradation Report based on the first-in testing.
- **1.5.9.6.4** Cancel Resource Performance Degradation Report — This process cancels a resource Performance Degradation Report when the specific trouble was related to a false resource failure event.
- **1.5.9.6.5** Escalate/End Resource Performance Degradation Report — This process monitors the jeopardy status of open Resource Performance Degradation Reports, and escalates Resource Performance Degradation Reports as necessary.
- **1.5.9.6.6** Clear Resource Performance Degradation Report Status — This process informs the Close Resource Performance Degradation Report process by modifying the Resource Performance Degradation Report status to cleared when the specific resource performance quality issues have been resolved.
- **1.5.9.6.7** Engage External Party Resource — Not used for this process element.

### 1.5.9.7 Close Resource Performance Degradation Report

**Extended Description.**

The objective of the Close Resource Performance Degradation Report processes is to close a resource performance degradation report when the resource performance has been resolved.

These processes monitor the status of all open resource performance degradation reports, and recognize that a resource performance degradation report is ready to be closed when the status is changed to cleared.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.5.9.1** Monitor Resource Performance — Monitor received resource performance information and undertake first-in detection.
- **1.5.9.2** Analyze Resource Performance — Analyze and evaluate the performance of specific resources
- **1.5.9.3** Control Resource Performance — Apply controls to resources in order to optimize the resource performance
- **1.5.9.4** Report Resource Performance — Monitor the status of resource performance degradation reports, provide notifications of any changes and provide management reports
- **1.5.9.5** Create Resource Performance Degradation Report — Create a new resource performance degradation report
- **1.5.9.6** Track & Manage Resource Performance Resolution — Ensure testing, repair and restoration activities are assigned, coordinated and tracked efficiently, and that escalation is invoked as required for any open resource performance degradation reports in jeopardy
- **1.5.9.7** Close Resource Performance Degradation Report — Close a resource performance degradation report when the resource performance has been resolved

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/intelligence-management]]

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Resource Process Decompositions PDF (GB921_Resource_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

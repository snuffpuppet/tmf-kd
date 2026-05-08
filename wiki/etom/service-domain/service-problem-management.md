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

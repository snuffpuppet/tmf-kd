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

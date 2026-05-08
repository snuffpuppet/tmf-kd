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

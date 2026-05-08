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
l2_id: "1.4.8"
l2_name: "Service Guiding & Mediation"
---

# Service Guiding & Mediation

> **Vertical context:** Billing ([[wiki/foundations/lifecycle]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

## Overview

Service Guiding & Mediation processes manage usage events by correlating and formatting them into a useful format.   These processes include guiding resource events to an appropriate service, mediation of these usage records, as well as de-duplication of usage records already processed.  These processes provide information on customer-related and Service-related events to other process areas across assurance and billing. This includes reports on non-chargeable events and overcharged events and analysis of event records to identify fraud and prevent further occurrences.

In many cases, this process is performed by a resource such as a network element.

— GB921 v25.5 Excel master, process ID `1.4.8`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.4.8.1** Mediate Service Usage Records — Validate, normalize, convert and correlate usage records collected from the resource layer
- **1.4.8.2** Report Service Usage Records — Generate reports on usage records based on requests from other processes
- **1.4.8.3** Guide Resource Usage Records — Relates the usage record to the appropriate service.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Service Process Decompositions PDF (GB921_Service_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

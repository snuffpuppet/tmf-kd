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
l2_id: "1.5.10"
l2_name: "Resource Mediation & Reporting"
---

# Resource Mediation & Reporting

> **Vertical context:** Billing ([[wiki/foundations/lifecycle]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Mediation & Reporting processes manage resource events by correlating and formatting them into a useful format.  These processes include the mediation and reporting of resource records.  Investigation of resource related billing event problems is also part of these processes.

These processes are often handled by appropriate network elements.

— GB921 v25.5 Excel master, process ID `1.5.10`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.5.10.1 Mediate Resource Usage Records

**Extended Description.**

The purpose of the Mediate Usage Records processes is to validate, normalize, convert and correlate usage records collected from various pieces of equipment in the network. It also removes any duplicate usage records that have already been processed.

**L4 sub-processes:**

- **1.5.10.1.1** Validate Resource Usage Records — Validate resource usage record collected from the network.
- **1.5.10.1.2** Normalize Resource Usage Records — Normalize resource usage records to specific expression format.
- **1.5.10.1.3** Convert Resource Usage Records — Convert resource usage records to specific data format.
- **1.5.10.1.4** Correlate Resource Usage Records — Correlate collected resource usage records.
- **1.5.10.1.5** Remove Duplicate Resource Usage Records — Remove duplicate resource usage records.

### 1.5.10.2 Report Resource Usage Records

**Extended Description.**

The purpose of the Report Resource Usage Records is to generate reports on usage records based on requests from other processes. These processes produce reports that may identify abnormalities, which may be caused by fraudulent activity or related to customer complaints or network problems.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.5.10.1** Mediate Resource Usage Records — Validate, normalize, convert and correlate usage records collected from the network.
- **1.5.10.2** Report Resource Usage Records — Generate reports on resource usage records based on requests from other processes.

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

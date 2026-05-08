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
l2_id: "1.5.16"
l2_name: "Resource Catalog Operational Readiness Management"
---

# Resource Catalog Operational Readiness Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Catalog Operational Readiness Management business process establishes and administers the support needed to operationalize Resource catalogs for ongoing day-to-day business needs.
These business activities implement the Resource Catalog through Release and Deploy business activities.

— GB921 v25.5 Excel master, process ID `1.5.16`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.5.16.1 Release Resource Catalog

**Extended Description.**

Release Resource Catalog business activity ensure all cross-functional activities needed to support catalog maintenance and operations, such as training and updating the support of the catalog are in place.

Release Resource Catalog business activity includes identifying stakeholders, catalog integration, catalog federation etc. for any scenario in support of the organizations business goals, including Release conditions that support users, customers and business partners.

**L4 sub-processes:**

- **1.5.16.1.1** Plan & Schedule Resource Catalog Release — Plan & Schedule Resource Catalog Release business activity is used to handle the release plan for the Resource Catalog.
- **1.5.16.1.2** Control Resource Catalog Release — Control Resource Catalog Release business activity is used to support the various catalog release tasks.
- **1.5.16.1.3** Test Resource Catalog — Test Resource Catalog business activity is used to establish the quality, reliability and performance requirement of the catalog according to the Resource management needs.

### 1.5.16.2 Deploy Resource Catalog

**Extended Description.**

Deploy Resource Catalog business activity manage the availability and use of the Resource catalog in operations.

Deploy Resource Catalog business activity includes identifying stakeholders, creating catalog category hierarchies, catalog integration, and catalog federation for any scenario, such as with business partners and between business functions.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.5.16.1** Release Resource Catalog — Release Resource Catalog business activity ensure all cross-functional activities needed to support catalog maintenance and operations, such as training and updating the support of the catalog are in place.
- **1.5.16.2** Deploy Resource Catalog — Deploy Resource Catalog business activity manage the availability and use of the Resource catalog in operations.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Resource Process Decompositions PDF (GB921_Resource_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

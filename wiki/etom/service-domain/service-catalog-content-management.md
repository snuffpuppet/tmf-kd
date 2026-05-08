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
l2_id: "1.4.15"
l2_name: "Service Catalog Content Management"
---

# Service Catalog Content Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

## Overview

Service Catalog Content Management business process define and provide the business activities that support the day-to-day operations of Service Catalogs in order to realize the business operations goals.
Service Catalog Content Management business processes include administering the Service Catalog instance in production, maintaining catalog entries, assuring catalogs, managing catalog access, managing entry lifecycle through versioning, handling catalog entity entry and changes, supporting distribution of catalogs as needed, and supporting user-facing activities.

— GB921 v25.5 Excel master, process ID `1.4.15`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.4.15.1** Maintain Service Catalog Content — Maintain Service Catalog Content business activity handles catalog content entry for adding or updating the operational Catalog by following the established Catalog Content Management operations standards and policies.
- **1.4.15.2** Manage Service Catalog Access — Manage Service Catalog Access business activity handles access to the catalog according to the Catalog Content Management standards and policies.
- **1.4.15.3** Manage Service Catalog Content Lifecycle — Manage Service Catalog Content Lifecycle business activity handles changes to catalog content according to the Catalog Content Management standards and policies.
- **1.4.15.4** Distribute Service Catalog — Distribute Service Catalog business activity handles exchange and distribution of catalogs according to the Catalog Content Management standards and policies.

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

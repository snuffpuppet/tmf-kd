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
l2_id: "1.5.17"
l2_name: "Resource Catalog Content Management"
---

# Resource Catalog Content Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Catalog Content Management business process define and provide the business activities that support the day-to-day operations of Resource Catalogs in order to realize the business operations goals.
Resource Catalog Content Management business processes include administering the Resource Catalog instance in production, maintaining catalog entries, assuring catalogs, managing catalog access, managing entry lifecycle through versioning, handling catalog entity entry and changes, supporting distribution of catalogs as needed, and supporting user-facing activities.

— GB921 v25.5 Excel master, process ID `1.5.17`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.5.17.1 Maintain Resource Catalog Content

**Extended Description.**

Maintain Resource Catalog Content business activity handles catalog content entry through adding or updating the Catalog by following the established Catalog Content Management standards and policies.

Manage Catalog Entry support the following activities and sub-activities:

Maintaining Catalog Content Versions

Maintain Catalog Content Relationship

Maintain Catalog Content taxonomy

Organize Catalog Entry

Classify Catalog Entry

**L4 sub-processes:**

- **1.5.17.1.1** Maintain Resource Catalog Content Version — Maintain Resource Catalog Content Version business activity handles tracking and controlling changes for Resource catalog entries.
- **1.5.17.1.2** Maintain Resource Catalog Content Relationship — Maintain Resource Catalog Content Relationship business activity handles associating Resource catalog entries.
- **1.5.17.1.3** Maintain Resource Catalog Content Entry — Maintain Resource Catalog Content Entry business activity handles content entry, content organization, content classification in the Resource Catalog according to the Resource Catalog model.

### 1.5.17.2 Manage Resource Catalog Access

**Extended Description.**

Manage Resource Catalog Access business activity handles access to the catalog according to the Catalog Content Management standards and policies.

Manage Resource Catalog Access will handle assigning catalog managers and granting privileges.

### 1.5.17.3 Manage Resource Catalog Content Lifecycle

**Extended Description.**

Manage Resource Catalog Content Lifecycle business activity handles changes to catalog content according to the Catalog Content Management standards and policies.

### 1.5.17.4 Distribute Resource Catalog

**Extended Description.**

Distribute Resource Catalog business activity handles exchange and distribution of catalogs according to the Catalog Content Management standards and policies.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.5.17.1** Maintain Resource Catalog Content — Maintain Resource Catalog Content business activity handles catalog content entry for adding or updating the operational Catalog by following the established Catalog Content Management operations standards and policies.
- **1.5.17.2** Manage Resource Catalog Access — Manage Resource Catalog Access business activity handles access to the catalog according to the Catalog Content Management standards and policies.
- **1.5.17.3** Manage Resource Catalog Content Lifecycle — Manage Resource Catalog Content Lifecycle business activity handles changes to catalog content according to the Catalog Content Management standards and policies.
- **1.5.17.4** Distribute Resource Catalog — Distribute Resource Catalog business activity handles exchange and distribution of catalogs according to the Catalog Content Management standards and policies.

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

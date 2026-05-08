---
type: sid-abe
spec_id: GB922
spec_version: "23.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Common_v23.0.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Common_v23.0.md
authority: primary
abe_category: common
entity_name: "Calendar ABE"
---

# Calendar ABE

## Overview

Represents Entities used to provide time related functions. This includes scheduling,
time conflicts and time based presentation support. — GB922 Common §4.9, p. 195

This document covers non base type entities that are time related (Entities like Time
Period are covered by the Base Types SID document).

This facet of the SID deals with Time based entities, which answer the question "when".
In this initial version of the document, we will only cover entities related to
Calendar functionality. — GB922 Common §4.9, p. 195

## Business Entities

§4.9 spans pp. 195–217 (22 pages) and covers Calendar functionality including:

- Calendar entities for scheduling
- Time conflict detection
- Time-based presentation

For full BE listings, attributes, and figures see source GB922 Common §4.9.
Detailed Calendar entity content not extracted in v1 ingest.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- TimePeriod (the simpler "valid for" type) is in Base Types ABE
  ([[wiki/sid/common/base-types-abe]]) — Calendar covers richer scheduling above that.
- Used by Capacity ([[wiki/sid/common/capacity-abe]]) and Project
  ([[wiki/sid/common/project-abe]]) for scheduling and time-bounded operations.
— GB922 Common §4.9, pp. 195–216

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-016: Calendar ABE content thin in v1 ingest; deepen on follow-up

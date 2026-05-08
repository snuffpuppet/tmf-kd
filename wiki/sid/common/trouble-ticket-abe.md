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
entity_name: "Trouble Ticket ABE"
release_status: draft
---

# Trouble Ticket ABE

> **Diagram-only ABE, source-flagged "not fully developed".** GB922 Common v23.0
> lists Trouble Ticket ABE as a top-level Common ABE in the §4.1 [ComD-01] Common
> ABEs Level 1 diagram with a brief one-paragraph description, but provides **no
> dedicated chapter**. The §4.1 description explicitly notes "This ABE is not fully
> developed." `release_status: draft` set in frontmatter to reflect that.

## Overview

Represents a record used for reporting and managing the resolution of Trouble or
Problem. This ABE is not fully developed. — GB922 Common §4.1, p. 43

## Key Attributes

No dedicated §4.x chapter exists in GB922 Common v23.0; key attributes not
published at this revision. The source explicitly flags Trouble Ticket ABE as
"not fully developed".

## Relationships

- Records the resolution of [[wiki/sid/common/trouble-or-problem-abe]] (per the
  §4.1 brief)
- Production-side fault management at the SID layer is partial: see also
  [[wiki/sid/service/service-problem-abe]] («NotFullyDeveloped») and
  [[wiki/sid/resource/resource-trouble-abe]] («notFullyDeveloped») — combined gap
  flagged by OQ-024 + OQ-031

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Trouble Ticket ABE not directly mapped in any
ODA Functional Block table to date.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Trouble Ticket pending.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-024: Service Problem ABE «NotFullyDeveloped» — paired production-side fault
  modelling gap
- OQ-031: Resource Trouble ABE «notFullyDeveloped» — paired production-side fault
  modelling gap
- OQ-041: Trouble Ticket ABE ingested as part of v1 Common gap fill; diagram-only
  and source-flagged "not fully developed"

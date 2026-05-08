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
entity_name: "Event ABE"
release_status: draft
---

# Event ABE

> **Diagram-only ABE, source-flagged "not fully developed".** GB922 Common v23.0
> lists Event ABE as a top-level Common ABE in the §4.1 [ComD-01] Common ABEs Level 1
> diagram with a brief one-paragraph description, but provides **no dedicated
> chapter**. The §4.1 description explicitly notes "This ABE is not fully developed."
> `release_status: draft` set in frontmatter to reflect that.

## Overview

The Event ABE contains entities that are used to represent events, their occurrence
and their recording within systems. This ABE is not fully developed.
— GB922 Common §4.1, p. 44

## Key Attributes

No dedicated §4.x chapter exists in GB922 Common v23.0; key attributes not
published at this revision. The source explicitly flags Event ABE as
"not fully developed".

## Relationships

Not specified in source at the Common ABE level beyond the §4.1 brief. Event
modelling appears across other ABEs (e.g. Usage events in
[[wiki/sid/common/usage-abe]]) but the Common Event ABE itself has no published
relationship model in v23.0.

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Event ABE not directly mapped in any ODA
Functional Block table to date.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Event pending.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Event ABE ingested as part of v1 Common gap fill; diagram-only and
  source-flagged "not fully developed"

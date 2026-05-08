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
entity_name: "Segmentation ABE"
---

# Segmentation ABE

## Overview

The Segmentation ABE contains all entities used for specifying rules to divide a
large set of Entities instances into subsets according to criteria. These subsets
are called segments. — GB922 Common §4.25, p. 846

## Key Attributes

Source §4.25.1 (Figure Sgt.01 — Criterion overview) defines:

- **Criterion** — the definition of information classifying an Entity from the
  model (represented by an instance of RootEntityType). A Criterion classifies
  only one RootEntityType.
- **CriterionCalculationRule** — for criteria whose information has to be
  calculated rather than read directly from an existing attribute.
- **AssociationSpecification:** `description: String`, `ID: String`,
  `lifecycleStatus: String`, `name: String`, `validFor: TimePeriod` — used when
  the Entity carrying the Criterion attribute is related to the Entity classified
  by the Criterion via an indirect relationship.
- **RootEntityTypeCharSpec** / **RootEntityTypeCharUse** — locate the attribute
  carrying the Criterion information.

Examples of Criteria from source: "Age" classifies Party; "Installation city"
classifies Resource.

Detailed attribute tables not extracted in v1 ingest; consult source.
— GB922 Common §4.25.1, pp. 846–848

## Relationships

- Criteria classify instances of **RootEntityType** entities — see
  [[wiki/sid/common/root-business-entities-abe]] for the RootEntity / RootEntityType
  pattern (referenced in source §4.25.1: "For more information about RootEntity /
  RootEntityType pattern, refer to the Common guide book").
- **AssociationSpecification** governs relationships between the classified Entity
  and the Entity carrying the Criterion's attribute.
— GB922 Common §4.25, pp. 846–848

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Segmentation ABE not directly mapped in any
ODA Functional Block table to date.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Segmentation pending.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Segmentation ABE ingested as part of v1 Common gap fill

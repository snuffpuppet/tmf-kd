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
entity_name: "Topology ABE"
---

# Topology ABE

> **Diagram-only ABE.** GB922 Common v23.0 lists Topology ABE as a top-level Common
> ABE in the §4.1 [ComD-01] Common ABEs Level 1 diagram with a brief one-paragraph
> description, but provides **no dedicated chapter**. The page below captures
> everything the source publishes about this ABE at the Common level. For specialised
> topological modelling content, see Resource Topology ABE
> ([[wiki/sid/resource/resource-topology-abe]]) which provides physical, logical,
> and network topological information for the Resource domain.

## Overview

The Topology ABE contains entities that are used to represent topological concepts
that can be used to model a large variety of topological relations between entities
ranging from dependencies to connectivity. — GB922 Common §4.1, p. 44

## Key Attributes

No dedicated §4.x chapter exists in GB922 Common v23.0; key attributes not
published at the Common ABE level. Topological pattern usage in Common is restricted
to references from §4.10 Location ABE (Binary Topological Relationships, Figures
L.02a/L.02b — see [[wiki/sid/common/location-abe]]). Specialised attributes appear
in Resource Topology ABE — see [[wiki/sid/resource/resource-topology-abe]].

## Relationships

- Specialised by Resource Topology ABE
  ([[wiki/sid/resource/resource-topology-abe]]) — physical, logical, network
  topological information for the Resource domain
- Topological relationship pattern referenced by Location ABE
  ([[wiki/sid/common/location-abe]]) §4.10.3–§4.10.4 (Binary Topological
  Relationship Examples)
— GB922 Common §4.1 brief and cross-references

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]] (GB1022 §4.5.2 Table 4-10 #01 — listed
  as a SID ABE in the Common Domain owned by the Production block, sourced from
  GB922 R20.5)

See [[wiki/open-questions#OQ-008]] — further ODA components pending trilateral
sweep.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Topology pending.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Topology ABE ingested as part of v1 Common gap fill; diagram-only in
  source (no §4.x chapter content available)

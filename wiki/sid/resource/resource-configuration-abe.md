---
type: sid-abe
spec_id: GB922
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Resource_v25.5.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Resource_v25.5.md
authority: primary
release_status: pre-production
abe_category: resource
entity_name: "Resource Configuration ABE"
---

# Resource Configuration ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].

## Overview

The Resource Configuration ABE represents the specification of the different possible
Resource configurations as well as the Resource Configurations instantiated for a
Resource. — GB922 Resource §4.4, p. 326

The Configuration model is shared with Service and Product Configurations — Figure
CP.01 in Resource is explicitly "copy from Common". The canonical model lives in
[[wiki/sid/common/configuration-and-profiling-abe]].

## Business Entities

This ABE applies the canonical Configuration pattern from
[[wiki/sid/common/configuration-and-profiling-abe]] to Resource entities:

- **ResourceConfiguration** — Configuration applied to a Resource instance
- **ResourceConfigurationSpec** — EntitySpec side
- Common pattern entities (`ConfigurationRelationship`, `ConfigSpecRelationship`)
  inherited from the Common ABE

For full detail consult source GB922 Resource §4.4.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Specialises canonical [[wiki/sid/common/configuration-and-profiling-abe]].
- Parallel to [[wiki/sid/product/product-configuration-abe]] and
  [[wiki/sid/service/service-configuration-abe]].
- Configuration applied to Resource instances ([[wiki/sid/resource/resource-abe]]).
- ConfigurationSpec relates to ResourceSpecification
  ([[wiki/sid/resource/resource-specification-abe]]) via the EntitySpec/Entity
  pattern.

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-027: Pre-production source release status

---
type: sid-abe
spec_id: GB922
spec_version: "25.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Service_v25.0.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Service_v25.0.md
authority: primary
abe_category: service
entity_name: "Service Configuration ABE"
---

# Service Configuration ABE

## Overview

The Service Configuration ABE represents the specification of the different possible
Service configurations as well as the Service Configurations instantiated for a
Service. — GB922 Service §4.5, p. 109

The Configuration model is shared with Resource and Product Configurations — Figure
CP.01 in Service is explicitly noted as "copy from Common". The canonical model lives
in [[wiki/sid/common/configuration-and-profiling-abe]]. — GB922 Service §4.5, p. 109

## Business Entities

This ABE applies the canonical Configuration pattern (from
[[wiki/sid/common/configuration-and-profiling-abe]]) to Service entities:

- **ServiceConfiguration** — Configuration applied to a Service instance
- **ServiceConfigurationSpec** — EntitySpec side
- Common pattern entities (`ConfigurationRelationship`, `ConfigSpecRelationship`)
  inherited from the Common ABE

For full detail consult source GB922 Service §4.5, pp. 109–112.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Specialises the canonical
  [[wiki/sid/common/configuration-and-profiling-abe]].
- Parallel to [[wiki/sid/product/product-configuration-abe]] and the Resource
  Configuration ABE (Resource Domain — not yet ingested).
- Configuration applied to Service instances
  ([[wiki/sid/service/service-abe]]).
- ConfigurationSpec relates to ServiceSpecification
  ([[wiki/sid/service/service-specification-abe]]) via the EntitySpec/Entity pattern.
— GB922 Service §4.5, pp. 109–112

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest

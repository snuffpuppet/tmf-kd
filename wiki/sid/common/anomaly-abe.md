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
entity_name: "Anomaly ABE"
---

# Anomaly ABE

## Overview

Anomaly ABE represents any unusual or unexpected event, observation, pattern, or
item that is significantly different from the norm that an enterprise wishes to
detect, analyze, assess and mitigate within an autonomous environment. In order for
the autonomous operations environment to behave within the calibrated operational
level, anomalies may require administrative and operational guidance. Anomaly ABE
entities provide a means of defining boundary conditions and lifecycle behavior for
Anomalies, as well as providing control over the end-to-end management process for
Anomalies. — GB922 Common §4.30, p. 893

## Key Attributes

Source §4.30.1 (Figure An.01 — Anomaly Management Basic Entities) defines:

- **Anomaly** — derived from `RootEntity → Entity`. The abstract Anomaly Class
  represents the generic anomaly.
- **AnomalySpecification** — derived from `RootEntity → EntitySpecification`;
  defines AnomalyClosedLoop scope and lifecycle.

Source §4.30.2 (Figure An.02) shows domain specialisations:

- **ProductAnomaly / ProductAnomalySpecification** — anomaly management for
  ProductSpecification / Product instances
- **ServiceAnomaly / ServiceAnomalySpecification** — anomaly management for
  ServiceSpecification / Service instances
- (Resource and other domain-specific anomaly specialisations follow the same
  pattern.) Anomaly can be associated with any SID Entity, not limited to Service
  or Resource.

Detailed attribute tables not extracted in v1 ingest; consult source.
— GB922 Common §4.30.1–§4.30.2, pp. 893–895

## Relationships

- **Anomaly ↔ AnomalySpecification** via `SpecificesAnomaly` (verbatim spelling
  from source) — `AnomalySpecificationReferredBy` documents references
- **Anomaly ↔ ClosedLoop** — Anomaly is managed using a ClosedLoop defined by
  ClosedLoopSpecification; see [[wiki/sid/common/closed-loop-abe]]
- **AnomalySpecification ↔ EntitySpecification** — domain specialisations
  (ProductAnomalySpecification etc.) extend EntitySpecification and reference
  domain specifications:
    - ProductAnomalySpecification ↔ ProductSpecification (see
      [[wiki/sid/product/product-specification-abe]])
    - ServiceAnomalySpecification ↔ ServiceSpecification (see
      [[wiki/sid/service/service-specification-abe]])
    - Resource Domain analogues exist — see
      [[wiki/sid/resource/resource-specification-abe]]
- Anomaly / AnomalySpecification derive from RootEntity / Entity /
  EntitySpecification in [[wiki/sid/common/root-business-entities-abe]]
— GB922 Common §4.30, pp. 893–897

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Anomaly ABE not directly mapped in any ODA
Functional Block table to date.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Anomaly pending. Likely
v25.5 candidates by name are the three Anomaly Management L2s (Product 1.2.25,
Service 1.4.18, Resource 1.5.21) but no source mapping table establishes the link;
the wikilinks will be added when a trilateral sweep against those L2s is run with
source backing (e.g. an updated GB1022 or per-domain decomposition PDF).

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Anomaly ABE ingested as part of v1 Common gap fill

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
entity_name: "Resource Performance ABE"
---

# Resource Performance ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].

## Overview

The Resource Performance ABE collects information used to correlate, consolidate, and
validate various performance statistics and other operational characteristics of
Resources. Each of these entities also enables network performance assessment against
planned goals, performs various aspects of trend analysis, including error rate and
cause analysis and Resource degradation. — GB922 Resource §4.8, p. 348

Entities in this ABE also include statistics defining Resource loading, and traffic
trend analysis. — GB922 Resource §4.8, p. 348

## Business Entities

### ResourcePerformance

Resource-side specialisation of Performance ([[wiki/sid/common/performance-abe]]).
Carries performance measurement instances for Resources.

### ResourcePerformanceSpec

EntitySpec side. Defines performance measurement specifications.

For full BE inventory and figures (e.g. PF.02 — Service, Resource, and Performance) see
source GB922 Resource §4.8.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Specialises canonical [[wiki/sid/common/performance-abe]].
- Parallel to [[wiki/sid/service/service-performance-abe]] (ServicePerformance) and
  Product Performance ([[wiki/sid/product/product-performance-abe]] —
  «notFullyDeveloped»).
- ResourcePerformance relates to Resource instances
  ([[wiki/sid/resource/resource-abe]]).
- Cross-domain associations: Figure PF.02 shows performance entities' associations
  with existing service and resource entities, plus Customer (so ResourcePerformance
  can correlate to customer-experienced metrics).
— GB922 Resource §4.8

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/intelligence-management]]

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-027: Pre-production source release status

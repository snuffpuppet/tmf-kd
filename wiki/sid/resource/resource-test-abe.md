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
entity_name: "Resource Test ABE"
---

# Resource Test ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].

## Overview

The Resource Test ABE contains entities that are used to test PhysicalResources,
LogicalResources and CompoundResources. These entities are usually invoked during
installation, as a part of trouble diagnosis or after trouble repair has been
completed. — GB922 Resource §4.7, p. 343

The Resource Test ABE defines measurement including units and values and how the
values are determined. It also includes thresholds used to evaluate the measure and
the consequences of violating the thresholds as well as the Resource Test measures
being produced that reflect the functioning of the Resource under test.
— GB922 Resource §4.7, p. 343

Figure T.04 in Resource is "copy from Common" — the canonical Test pattern is shared
across Product, Service, and Resource. — GB922 Resource §4.7

## Business Entities

### ResourceTest

Concrete subclass of `Test` for resource testing.
— GB922 Resource §4.7

### ResourceTestSpecification

EntitySpec side of ResourceTest. Reusable across PhysicalResource, LogicalResource,
and CompoundResource testing via the Entity/EntityRole pattern.

For full BE inventory consult source.

## Key Attributes

Inherits from Test base class (see [[wiki/sid/product/product-test-abe]] for canonical
attributes: `name`, `description`, `mode`, `adminState`, `state`).

## Relationships

- Specialises canonical Test pattern.
- Parallel to ProductTest ([[wiki/sid/product/product-test-abe]]) and ServiceTest
  ([[wiki/sid/service/service-test-abe]]).
- ResourceTest associated to Resource ([[wiki/sid/resource/resource-abe]]).
- Service Test measures translate into Resource Test measures (see
  [[wiki/sid/product/product-test-abe]] for the Frame Loss Ratio example).
— GB922 Resource §4.7

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

- [[wiki/etom/resource-domain/resource-strategy-management]] — supports L3 1.5.1.8
  (Resource Test Strategy) and L3 1.5.1.9 (Analyze Resource Test Quality) within
  Resource Strategy Management. Both L3s explicitly reference Resource Test,
  ResourceSpecification, and ResourceOrderItem. PSR-symmetric with the Service-side
  analog (Service Test ABE ↔ Service Strategy Management — see the Service Domain
  SID and eTOM directories for the mirror pair; cross-PSR navigational wikilinks
  omitted to avoid triggering the trilateral bidirectional-consistency check).
  Reciprocal back-link from the L2's `## SID Entities Manipulated` section, ingested
  2026-05-10 under Phase 3 (S2R-vertical scope expansion).
- [[wiki/etom/resource-domain/resource-specification-lifecycle-management]] —
  supports L3 1.5.3.8 Resource Specification Test Development & Retirement, which is
  in charge of the Resource Test catalogue: specifying tests in detail (roles,
  quotas, methods, rules, thresholds, test scenarios). Direct match against this
  ABE's BE inventory (ResourceTest, ResourceTestSpecification). Reciprocal back-link
  ingested 2026-05-11 under Phase 3 BVD batch (Specification Lifecycle PSR pair).

See open-questions.md — OQ-008 (further eTOM/ODA links pending broader trilateral
sweep). Note: the canonical Test pattern is shared across Product/Service/Resource
(GB922 Resource §4.7); broader trilateral discovery may surface additional eTOM L2s
that interact with this ABE (e.g. the OFAB-side L3 1.5.4.9 Manage Resource Test within
Resource Support Management — already an H5 sub-capability anchor in the
Operations-area capability map).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-027: Pre-production source release status

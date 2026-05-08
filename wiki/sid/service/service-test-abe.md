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
entity_name: "Service Test ABE"
---

# Service Test ABE

## Overview

The Service Test ABE defines measurement including units and values and how the values
are determined. It also includes thresholds used to evaluate the measure and the
consequences of violating the thresholds as well as the Service Test measures that
reflect the functioning of the Service under test. — GB922 Service §4.8, p. 126

> The following Figure shows one way to support tests for Product, Services, and
> Resources by applying the Entity/EntityRole pattern. This allows the same "Test
> Specification" to be used for many "Product TestSpecifications",
> "ServiceTestSpecifications", and "Resource TestSpecifications".
>
> Product, Service, and Resource Tests are defined to be generalizations of the
> abstract "Test" class. — GB922 Service §4.8, p. 126

Figure T.04 in Service is "copy from Common" — the canonical Test pattern is shared
across all three layers.

## Business Entities

### ServiceTest

Concrete subclass of `Test` (in [[wiki/sid/product/product-test-abe]] or canonical
Common Test pattern) for service testing.

### ServiceTestSpecification

EntitySpec side of ServiceTest.

For full BE inventory and figures see source GB922 Service §4.8, pp. 126–127.

## Key Attributes

Inherits from Test base class (see
[[wiki/sid/product/product-test-abe]] for canonical attribute list: name, description,
mode, adminState, state). Detailed Service-specific attributes not extracted in v1
ingest.

## Relationships

- Specialises the canonical Test pattern (Common Domain).
- Parallel to ProductTest ([[wiki/sid/product/product-test-abe]]) and ResourceTest
  (Resource Domain — not yet ingested).
- ServiceTest associated to Service ([[wiki/sid/service/service-abe]]).
- Service test measures (e.g. "Frame Loss Ratio") relate to Resource test measures
  via the cross-domain Test pattern.
— GB922 Service §4.8, pp. 126–127

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest

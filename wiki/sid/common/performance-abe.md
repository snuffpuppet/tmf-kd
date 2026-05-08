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
entity_name: "Performance ABE"
---

# Performance ABE

## Overview

Represents a measure of the manner in which a Product and/or Service and/or Resource is
functioning. — GB922 Common §4.20, p. 630

This paragraph describes the SID Service and Resource Performance ABEs. This
performance model could be extended to also support the SID Product Performance ABE.
These ABEs were developed to support the SID principle of inherent extensibility by
employing SID modeling patterns. — GB922 Common §4.20, p. 630

The ABEs concerned by this paragraph are:

- in Product Domain: Product Performance ([[wiki/sid/product/product-performance-abe]])
- in Service Domain: Service Performance (not yet ingested)
- in Resource Domain: Resource Performance (not yet ingested)

— GB922 Common §4.20, p. 630

## Business Entities

§4.20 spans pp. 630–669 (40 pages). Core entities include:

- **Performance** — abstract base measure
- **PerformanceSpec** — EntitySpec side
- **ProductPerformance**, **ServicePerformance**, **ResourcePerformance** —
  domain specialisations

For full BE inventory and figures see source.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Specialises Metric ([[wiki/sid/common/metric-abe]]) for performance-specific use.
- Domain-specific Performance ABEs sit in their respective documents:
  Product Performance ([[wiki/sid/product/product-performance-abe]] —
  «notFullyDeveloped» in source); Service and Resource Performance not yet ingested.
- Operational relevance to eTOM Assurance lifecycle stage
  ([[wiki/foundations/lifecycle#Assurance]]).
— GB922 Common §4.20, pp. 630–669

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/intelligence-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest

---
type: sid-abe
spec_id: GB922
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Product_v25.5.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Product_v25.5.md
authority: primary
abe_category: product
entity_name: "Strategic Product Portfolio Plan ABE"
---

# Strategic Product Portfolio Plan ABE «notFullyDeveloped»

> **Status flag.** GB922 Product v25.5 §4.12 explicitly marks this ABE as
> «notFullyDeveloped». Content is minimal in the source. See
> [[wiki/open-questions#OQ-012]].
>
> Additionally, this ABE relates to the *Strategy-to-Readiness* lifecycle area, which
> is partially out of scope for the operational mapping focus of this corpus. See
> [[wiki/open-questions#OQ-013]].

## Overview

A strategy employed to promote a ProductOfferingSpecification. Strategic Product
Portfolio Plan ABE is concerned with the plans of the product portfolio, which product
offerings to make available to each market segment and the plans to development and
deploy product offerings, as well as retirement of products.

This ABE is not fully developed.

— GB922 Product §4.12, p. 253

## Business Entities

No specific entities are enumerated in §4.12 of GB922 Product v25.5. The ABE is in
development.

## Key Attributes

Not specified in source.

## Relationships

- Strategic plans target ProductOfferingSpecifications
  ([[wiki/sid/product/product-offering-specification-abe]]).
- Implied relationship to MarketSegments (Customer/Common Domain, not yet ingested).

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-012: GB922 Product §4.12 marked «notFullyDeveloped»; content minimal
- OQ-013: §4.12 sits in Strategy-to-Readiness lifecycle area; in-corpus scope
  primarily targets Operations lifecycle. Confirm whether this ABE should remain in
  the corpus or be deferred.

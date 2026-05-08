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
entity_name: "Location ABE"
---

# Location ABE

## Overview

The Location ABE represents the site or position of something, such as a customer's
address, the site of equipment where there is a fault and where is the nearest person
who could repair the equipment, and so forth. Locations can take the form of
coordinates and/or addresses and/or physical representations.
— GB922 Common §4.10, p. 217

> **Disclaimer (verbatim from source).** This Location model is complex and has a
> number of subtleties. It provides a high level framework, explains broad concepts
> and gives illustrative examples. Actual solutions for particular requirements will
> be dependent factors such as country address standards, state/country/province map
> standards, Service Provider addressing standards, Equipment vendor equipment naming
> & addressing conventions, whether textual only or graphical representations will be
> provided. — GB922 Common §4.10, p. 217

## Business Entities

§4.10 spans pp. 217–296 (79 pages). The Location model includes:

- **Location** — abstract base entity
- **GeographicAddress** — address-based locations (street, city, postal code, country)
- **GeographicLocation** — coordinate-based locations
- **GeographicArea** — bounded geographic regions
- **AdministrativeArea** — political/administrative subdivisions (used by
  TaxJurisdiction in [[wiki/sid/product/product-party-roles-abe]])
- **Place** — physical representation (used by ProductOfferingSpecification in
  [[wiki/sid/product/product-offering-specification-abe]])

Detailed entity hierarchy, address standards integration, and figures (a substantial
collection covering coordinates, addresses, areas, and references) are in the source.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source GB922 Common
§4.10, pp. 217–296.

## Relationships

- Used pervasively across SID — by Party (residential addresses), Resource (equipment
  sites), Service (point-of-presence), Product (delivery locations), Capacity
  (geographic capacity demands).
- Provides AdministrativeArea reference for tax jurisdictions
  ([[wiki/sid/product/product-party-roles-abe]] — TaxJurisdiction).
- Provides GeographicPlace reference for capacity geographic constraints
  ([[wiki/sid/product/product-capacity-abe]]).
— GB922 Common §4.10, pp. 217–296

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-017: Location ABE is large and complex; full BE inventory deferred — this page
  covers conceptual structure only

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
entity_name: "Product Test ABE"
---

# Product Test ABE

## Overview

Product Test ABE represents all information to specify tests that will be performed on
Products as well as the results in measures being produced that reflect the
functioning of the product under test. — GB922 Product §4.9, p. 246

> Product, Service, and Resource Tests are defined to be generalizations of the
> abstract "Test" class. In this way, the "Test" model may be used for the
> specification of all three types of tests. Each test, such as "ServiceTest" is
> associated to its relative entity under test, which in this case is "Service". The
> relationships therefore between products, services, and resources, are maintained to
> the associated tests. — GB922 Product §4.9, p. 246

> As an example, a service test measure such as "Frame Loss Ratio" may translate to
> resource test measures "Number of frames sent" and "Number of frames received". The
> metric "Number of Frames Lost" is derived from the resource test measures, and the
> "Frame Loss Ratio" is further calculated by dividing the number of frames lost by
> the number of frames sent. — GB922 Product §4.9, p. 246

> Refer to Common Domain guidebook for more details.
> — GB922 Product §4.9, p. 246

## Business Entities

### Test (abstract)

The abstract base class generalising ProductTest, ServiceTest, ResourceTest.
— GB922 Product §4.9, p. 246

Attributes (Figure PT.01, p. 246):
- `name: String`
- `description: String`
- `mode: TestMode`
- `adminState: AdministrativeState`
- `state: TestState`

### ProductTest

Concrete subclass of `Test` associated to a Product
([[wiki/sid/product/product-and-offering-instance-abe]]) under test.
— GB922 Product §4.9, p. 246

### TestSpecification

The EntitySpecification side of the Entity/EntitySpec pattern for Test.
— GB922 Product §4.9, p. 246

Attributes (Figure PT.01):
- `name: String`
- `description: String`
- `validFor: TimePeriod`

### TestMeasure / TestMeasureDefinition

TestMeasure represents an actual measurement produced by a Test;
TestMeasureDefinition specifies a measure type. — GB922 Product §4.9, p. 246

### TestSpecificationRole

Role classification applied via the Entity/EntityRole pattern, allowing the same Test
Specification to be reused across Product, Service, Resource Test Specifications.
— GB922 Product §4.9, p. 246

## Key Attributes

See Test attributes above. Detailed attribute tables for other entities not extracted
in v1 ingest; consult source.

## Relationships

- ProductTest relates to Product entities in
  [[wiki/sid/product/product-and-offering-instance-abe]].
- The Test model also generalises ServiceTest and ResourceTest — Service and Resource
  Domains, not yet ingested.
- TestSpecificationRole pattern enables sharing TestSpecifications across
  Product/Service/Resource testing.
- Test produces TestMeasure(s) which match TestMeasureDefinition(s).
— GB922 Product §4.9, p. 246

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest

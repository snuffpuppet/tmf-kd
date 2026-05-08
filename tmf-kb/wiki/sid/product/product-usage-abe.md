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
entity_name: "Product Usage ABE"
---

# Product Usage ABE

## Overview

Product Usage ABE represents specification of usages enabled by Products and usages of
products tracked. — GB922 Product §4.6, p. 207

> Put simply, usage is how much service is used, by whom is it used, where and when is
> it used and circumstances under which it is used. Normally, when a usage event
> occurs, it is stored in a network element, for instance in a switch, router, gateway
> or in an application system. Resources (applications, network and computing
> capabilities) usually store usage data in proprietary formats that are not understood
> by the billing system. Depending on the polling strategy, a mediation engine connects
> to resources, collects usage data and formats them into a format that is understood
> by the billing system. Output of a mediation engine are Usage Detail Records (UDRs).
> Examples of UDRs are Call Detail Records (CDRs – used to describe usage details of
> voice call services) and Internet Protocol Detail Records (IPDRs – used to describe
> usage details of Internet Protocol based services). — GB922 Product §4.6, p. 207

## Business Entities

### Usage (abstract)

The abstract business entity used to describe any resource-, service- or product-based
usage that the billing system can read, update and process.
— GB922 Product §4.6, p. 207

### UsageSpecification

Describes a type of usage. In order to achieve a flexible structure of the
UsageSpecification all its attributes are stored as characteristics. The
UsageSpecification is comprised of UsageSpecCharacteristics that define all
characteristics (attributes) known by a particular type of usage. Each characteristic
is described by its name, category, presence and a set of allowed values.
— GB922 Product §4.6, p. 207

UsageSpecification has the following subclasses:

- **ServiceUsageSpec** (represents a service usage)
- **ResourceUsageSpec** (represents a resource usage)
— GB922 Product §4.6, p. 207

### ProductUsage

Concrete subclass of `Usage` for product-based usage.
— GB922 Product §4.6, p. 207

### ServiceUsage

Concrete subclass of `Usage` for service-based usage. — GB922 Product §4.6, p. 207

### ResourceUsage

Concrete subclass of `Usage` for resource-based usage. — GB922 Product §4.6, p. 207

### UsageSpecCharacteristic

Defines all characteristics (attributes) known by a particular type of usage. Each
characteristic is described by its name, category, presence and a set of allowed
values. Categories include the high-level "Who, When, What, Where, and Why" of usage
information. — GB922 Product §4.6, p. 207

### UsageSpecCharacteristicValue

Class describing all allowed values or value ranges for a UsageSpecCharacteristic.
— GB922 Product §4.6, p. 207

## Key Attributes

UsageSpecCharacteristic attributes:
- `name: String` — unique name identifying the characteristic
- `category: String` — high-level aspect (Who, When, What, Where, Why)
- `presence: enum` — required or optional

Detailed attribute tables for other entities not extracted in v1 ingest; consult source.

## Relationships

- Usage and its subclasses (ProductUsage, ServiceUsage, ResourceUsage) follow the
  CharacteristicSpecification/CharacteristicValue pattern (see Common Domain — not yet
  ingested).
- ProductUsage relates to Products instantiated from
  [[wiki/sid/product/product-and-offering-instance-abe]].
- ServiceUsage and ResourceUsage relate to Service/Resource entities (Service Domain,
  Resource Domain — not yet ingested).
— GB922 Product §4.6, pp. 207–216

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest

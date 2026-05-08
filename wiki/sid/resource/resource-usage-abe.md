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
entity_name: "Resource Usage ABE"
---

# Resource Usage ABE

> **Pre-production source.** GB922 Resource v25.5 — see
> [[wiki/open-questions#OQ-027]].

## Overview

The Resource Usage ABE represents the specification of Resource Usage types and
collects Resource Usage records with their characteristics (a.k.a. consumption data).
— GB922 Resource §4.6, p. 340

The entities in this ABE provide physical, logical, and network usage information.

> A resource usage represents any usage of resources in its broadest meaning, for
> example a usage of a product realized by a resource.
>
> A service usage represents any usage of service in its broadest meaning, for example
> or a usage of a service that realizes a product.
>
> A Product is realized as one or more Service(s) and/or Resource(s).
> — GB922 Resource §4.6, p. 340

## Business Entities

### ResourceUsage

Concrete subclass of `Usage` for resource-based usage. Sister to ProductUsage
([[wiki/sid/product/product-usage-abe]]) and ServiceUsage
([[wiki/sid/service/service-usage-abe]]).
— GB922 Resource §4.6 (Figure U.07)

### ResourceUsageSpec

Specification side of the EntitySpec/Entity pattern for ResourceUsage.

The Usage class hierarchy is shared across Product/Service/Resource — figures U.07
referenced in Resource are explicitly drawn from the canonical Usage model.

## Key Attributes

UsageSpecCharacteristics include name, category (Who/When/What/Where/Why), presence,
allowed values — the canonical pattern is in
[[wiki/sid/product/product-usage-abe]] and shared across all three Usage variants.

## Relationships

- ResourceUsage parallels [[wiki/sid/product/product-usage-abe]] (ProductUsage) and
  [[wiki/sid/service/service-usage-abe]] (ServiceUsage).
- ResourceUsage relates to Resource instances ([[wiki/sid/resource/resource-abe]]).
- Mediation engines convert Resource usage data (UDRs, CDRs, IPDRs) into Service-
  and Product-level Usage Detail Records.
— GB922 Resource §4.6, pp. 340–342

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-027: Pre-production source release status

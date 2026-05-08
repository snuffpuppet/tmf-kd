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
entity_name: "Service Usage ABE"
---

# Service Usage ABE

## Overview

The Service Usage ABE represents the specification of Service Usage types and collects
Service Usage records with their characteristics (a.k.a. consumption data).
— GB922 Service §4.7, p. 117

The Usage model is shared with Product and Resource Usage — Figures U.02, U.04, U.06
in Service are explicitly "copy from Common". The canonical Usage model lives in
[[wiki/sid/product/product-usage-abe]] (which itself is the Product specialisation of
the abstract Usage model — the cross-domain Usage abstraction is referenced from
multiple SID documents).

## Business Entities

### ServiceUsage

Concrete subclass of `Usage` for service-based usage. Sister to ProductUsage
([[wiki/sid/product/product-usage-abe]]) and ResourceUsage (Resource Domain).
— GB922 Service §4.7, p. 117

### ServiceUsageSpec

Specification side of the EntitySpec/Entity pattern for ServiceUsage.
— GB922 Service §4.7 (Figure U.02 copy)

## Sub-ABEs

§4.7 contains nested sub-ABEs:

- §4.7.1 **Service Usage Specification ABE** (p. 124, Figure SUS.01)
- §4.7.2 **Service Usage Entity ABE** (p. 125, Figure SUE.01)

## Key Attributes

UsageSpecCharacteristics include name, category (Who/When/What/Where/Why), presence,
and allowed values — the canonical pattern is in [[wiki/sid/product/product-usage-abe]].

## Relationships

- ServiceUsage parallels ProductUsage
  ([[wiki/sid/product/product-usage-abe]]) and ResourceUsage (Resource Domain — not
  yet ingested).
- ServiceUsage relates to Service instances ([[wiki/sid/service/service-abe]]).
- Mediation engines convert Resource usage data (UDRs, CDRs, IPDRs) into
  Service-level Usage Detail Records.
— GB922 Service §4.7, pp. 117–125

## ODA Components That Own This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest

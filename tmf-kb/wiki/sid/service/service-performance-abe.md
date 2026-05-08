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
entity_name: "Service Performance ABE"
---

# Service Performance ABE

## Overview

The Service Performance ABE collects information used to correlate, consolidate, and
validate various performance statistics and other operational characteristics of
Know-Hows (a.k.a. CFS) and Technical Solutions (a.k.a. RFS). It provides a set of
entities that enables performance monitoring and reporting. Each of these entities
also enables network performance assessment against planned goals, performs various
aspects of trend analysis, including error rate and cause analysis and Service
degradation. Entities in this ABE also enable the traffic trend analysis.
— GB922 Service §4.9, p. 128

> It should be noted that this section is still a work in progress, and is subject to
> change. — GB922 Service §4.9, p. 128

## Business Entities

### ServiceLevelSpecification (SLS)

A ServiceLevelSpecification expresses commitments associated with Services. Customers
expect a certain level of Service. — GB922 Service §4.9, p. 128 (Figure SO.37)

### ServiceLevelAgreement (SLA)

Specialised Agreement (from [[wiki/sid/common/agreement-abe]]) carrying SLS
commitments. — GB922 Service §4.9 (Figure SO.38)

### ServiceLevelSpecParameter / ServiceLevelSpecObjective

Parameter and objective entities defining what the SLS measures and at what level.
— GB922 Service §4.9 (Figure SO.40)

### KPI / KQI

Key Performance Indicators and Key Quality Indicators relating Products and Services.
— GB922 Service §4.9 (Figure SO.41)

### ServiceLevelSpecConsequence

Consequences of SLS violation. — GB922 Service §4.9 (Figure SO.42)

### ServiceLevelSpecApplicability / ServiceLevelSpecificationExpression

Applicability conditions and expression syntax for SLS.
— GB922 Service §4.9 (Figures SO.43, SO.43a)

## Sub-ABEs

§4.9 contains nested sub-ABEs:

- §4.9.1 **Service Level Spec ABE** (p. 140, Figure SLS.01)
- §4.9.2 **Service Performance Specification ABE** (p. 142, Figure SPS.01)

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Specialises the canonical Performance ABE
  ([[wiki/sid/common/performance-abe]]).
- ServiceLevelAgreement is a specialisation of Agreement
  ([[wiki/sid/common/agreement-abe]]).
- SLS relates to Products ([[wiki/sid/product/product-and-offering-instance-abe]])
  and Services ([[wiki/sid/service/service-abe]]).
- KPIs/KQIs link to ProductSpecification
  ([[wiki/sid/product/product-specification-abe]]) and ServiceSpecification
  ([[wiki/sid/service/service-specification-abe]]).
— GB922 Service §4.9, pp. 128–143

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/intelligence-management]]

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## eTOM Processes That Manipulate This Entity

See open-questions.md — OQ-008 (eTOM and ODA layers not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-023: GB922 Service §4.9 source notes "this section is still a work in progress,
  and is subject to change" — content may evolve

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
entity_name: "Metric ABE"
---

# Metric ABE

## Overview

The Metric ABE defines standards of measurement including units and values and how the
values are determined. It also includes thresholds used to evaluate the metric and the
consequences of violating the thresholds. — GB922 Common §4.19, p. 520

It's in vision that other projects use and specialize the Metric ABE in some way
(creating sub-classes and adding new entities) such as PM (Performance Management), RA
(Revenue Assurance), SLA (Service Level Agreement), etc. — GB922 Common §4.19, p. 520

One business dictionary defines metrics in terms of standards of measurement. They go
on to define measurement in terms of values and units. Since there is a fundamental
need to measure all aspects of enterprises based on Frameworx, the need for a Common
Business Entity standardizing what a Metric is in Frameworx has been deemed as
essential. — GB922 Common §4.19, p. 520

This addendum is organized in two parts — 1) the standardized definition of the SID
Metric ABE itself, including elaboration on the critical details of the definition,
and 2) Best Practices for design and application of specific metrics, both generically
and in specific application uses. — GB922 Common §4.19, p. 520

## Business Entities

§4.19 spans pp. 520–629 (110 pages — second-largest single ABE in this document after
Root Business Entities). Core entities include:

- **Metric** — abstract base
- **MetricSpec** — EntitySpec side
- **MetricMeasurement** / measurement value entities
- **Threshold** — evaluation conditions
- **MetricCalculation** / determination logic
- Specialisations referenced in source: PM (Performance Management), RA (Revenue
  Assurance), SLA — these are conceptual sub-class areas, fully realised in
  domain-specific documents

For full BE inventory, attribute tables, and figures see source.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Specialised by Performance ([[wiki/sid/common/performance-abe]]).
- Specialised in domain-specific Performance and Quality ABEs in Service and Resource
  domains (not yet ingested).
- Used by SLA / Agreement ([[wiki/sid/common/agreement-abe]]) for measurable
  conditions.
- Threshold entities relate to monitoring activities (operational eTOM Assurance —
  see [[wiki/foundations/lifecycle#Assurance]]).
— GB922 Common §4.19, pp. 520–629

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/intelligence-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-019: Metric ABE is the second-largest chapter (110 pages); v1 ingest covers
  conceptual content only — deeper ingest needed for design-and-application detail

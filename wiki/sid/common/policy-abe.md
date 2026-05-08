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
entity_name: "Policy ABE"
---

# Policy ABE

## Overview

The Policy Domain consists of a set of layered ABEs that define specifications (e.g.,
templates) and definitions of Policy entities that can be used in managing the behavior
and definition of entities in other Domains. Policy takes three primary forms. The
first is the definition of how policy is used to manage the definition, change, and
configuration of other entities. The second is the definition of how policy itself is
managed. The third is how applications use policies to manage entities.
— GB922 Common §4.21, p. 670

Policy management has been portrayed as an effective mechanism to orchestrate the
behavior of distributed systems. Different versions of policy management have
concentrated on different aspects of this problem, ranging from defining business goals
to specifying low-level configuration changes in a device. Unfortunately, such efforts
have been scattered and uncoordinated. — GB922 Common §4.21, p. 670

## Business Entities

§4.21 spans pp. 670–760 (91 pages). Core entities include:

- **Policy** (abstract)
- **PolicySpec** — EntitySpec side
- **PolicyRule** — rule definitions (used by ProductOfferingPrice in
  [[wiki/sid/product/product-offering-specification-abe]])
- **PolicyStatement**, **PolicyCondition**, **PolicyAction** — the
  condition-action structure
- **PolicySet** — groupings (referenced from Product offering pricing)
- **PolicyRepository** — Collection of policies
- **PolicyEventBase** — event-driven policy triggering

For full BE inventory and figures see source.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- Used pervasively to govern other domain entities — e.g.
  ProductOfferingPrice governance via PolicyRule
  ([[wiki/sid/product/product-offering-specification-abe]] §4.3, Figures Pr.14–Pr.21).
- Inherits from RootEntity / EntitySpec / Entity patterns in
  [[wiki/sid/common/root-business-entities-abe]]. Source explicitly notes: "Policy
  entities in the Common Business Entities domain" inherit RootEntity attributes.
- PolicyRepository uses Collection (also from Root Business Entities ABE).
- Privacy-specific policies layer atop Policy via
  [[wiki/sid/common/party-privacy-abe]] indirectly.
— GB922 Common §4.21, pp. 670–760

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest

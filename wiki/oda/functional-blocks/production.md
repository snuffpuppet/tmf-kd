---
type: oda-component
spec_id: GB1022
spec_version: "1.1.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf
source_extract_paths:
  - raw/extracted/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.md
authority: primary
oda_domain: "Functional Blocks"
component_id: "GB1022 §4.5"
component_name: "Production"
psr_layer: "service-and-resource"
---

# Production

> **Architectural role.** Per GB1022 §3 Systems of Separation: Production is one of
> three blocks in the **Systems of Records** group — the technical/network layer.
>
> **Production/commercial relevance.** This is the **production-side** block — the
> direct ODA realisation of the production half of the production/commercial split
> the corpus's PSR mapping goal targets. It handles CFS/RFS lifecycle (see
> [[wiki/sid/service/service-abe]] — CFS/RFS instances) and pairs with both Service
> and Resource SID domains and with the operational Service and Resource eTOM L2s
> ([[wiki/etom/service-domain/_index]] and [[wiki/etom/resource-domain/_index]]).

## Overview

The Production Block is responsible for the delivery and lifecycle management of
**Customer Facing Services (CFS)** and **Resource Facing Services (RFS)** regardless
of the technology type (e.g., physical, virtual, connectivity, end point, etc.) or
the operational domain or factory where it originates, including third parties.

The Production Block exposes its service capabilities in a way that is commonly
known as Network as a Service (NaaS) for consumption by other ODA function blocks.
For example, the Core Commerce Management Block uses them to create products and
offers, while the Engagement Management Block uses them to allow customers to
recharge their balance or order a new video on demand. The Production block may also
expose devices (e.g., smartphone) and application capabilities (e.g., email).

The scope of the Production block includes the exposure of its service capability
definitions and the dynamic run-time decision of how the service(s) supporting
Products and Customer will be created, delivered, used, maintained, assured, and
repaired. It provides end-to-end management of operational functions for services
and resources to support the commercial success of the ecosystem - including
activities that span multiple enterprises such as the management of installation,
deployment, and operations of technologies, performance and quality.

The Production Block does not need to know the details of a product nor the
customer, contract owner, or payer requesting its exposed service capabilities. It
assumes responsibility for the delivery of the CFS/RFS, as well as for operating the
usage functions up to a committed quality of service - including applying policy
control and balance management and supplying the Core Commerce Management Block with
usage data records to perform rating on offers. — GB1022 §4.5.1, pp. 37

Production can be characterized as follows:

- Production deals with **"HOW"**
- Production is in charge of Services and Resources oriented processes, functions
  and repositories such as:
    - Definition and lifecycle of the telco capabilities that can be exposed as
      Services (CFS) to define Products and Offers to commercialize (in Core
      Commerce Management)
    - Definition and lifecycle of the technical solutions available for these
      services (RFS), based on all type of technology (physical, virtual, …) or all
      network, service platforms, IT systems, … capabilities, directly managed by
      the telco operator or available by means of a Business Partner
    - Infrastructure Deployment and Operations management
    - Delivery of services and resources
    - Usage of services, including usage control and real-time balance management
    - Problem and Performance Management
    - Service & Resource Strategy activities

— GB1022 §4.5, p. 37

## Responsibilities

The business processes are derived from eTOM level 2 business process elements.
Source Table 4-9 (Production Standardized Business Process descriptions, source
GB921 R20.5) covers Service Development and Management, Service Management and
Operations, Resource Development and Management, and Resource Management and
Operations groupings. — GB1022 §4.5, p. 38

## SID Entities Owned

GB1022 §4.5.2 Table 4-10 enumerates the SID ABEs owned by the Production block,
sourced from GB922 R20.5. The table covers Service, Resource, Enterprise (Workforce),
and Common (Topology, Location) domains. Cross-walk to our v25.0 / v23.0 / v25.5
corpus and the resulting links are recorded in [[wiki/open-questions#OQ-040]].

**Service Domain ABEs** (Table 4-10 entries 01–08) — resolved to GB922 Service v25.0:

- [[wiki/sid/service/service-abe]] (Table 4-10 #01 Service ABE)
- [[wiki/sid/service/service-order-abe]] (#02 Service Order ABE)
- [[wiki/sid/service/service-specification-abe]] (#03 Service Specification ABE)
- [[wiki/sid/service/service-strategy-and-plan-abe]] (#04 Service Strategy & Plan ABE)
- [[wiki/sid/service/service-configuration-abe]] (#05 Service Configuration ABE)
- [[wiki/sid/service/service-usage-abe]] (#06 Service Usage ABE)
- [[wiki/sid/service/service-problem-abe]] (#07 Service Problem ABE)
- [[wiki/sid/service/service-test-abe]] (#08 Service Test ABE)

**Resource Domain ABEs** (Table 4-10 entries 01–09) — resolved to GB922 Resource v25.5:

- [[wiki/sid/resource/resource-abe]] (#01 Resource ABE)
- [[wiki/sid/resource/resource-order-abe]] (#02 Resource Order ABE)
- [[wiki/sid/resource/resource-specification-abe]] (#03 Resource Specification ABE)
- [[wiki/sid/resource/resource-topology-abe]] (#04 Resource Topology ABE)
- [[wiki/sid/resource/resource-configuration-abe]] (#05 Resource Configuration ABE)
- [[wiki/sid/resource/resource-usage-abe]] (#06 Resource Usage ABE)
- [[wiki/sid/resource/resource-strategy-and-plan-abe]] (#07 Resource Strategy & Plan ABE)
- [[wiki/sid/resource/resource-trouble-abe]] (#08 Resource Trouble ABE)
- [[wiki/sid/resource/resource-test-abe]] (#09 Resource Test ABE)

**Common Domain ABEs** (Table 4-10 entries 01–02) — resolved to GB922 Common v23.0:

- [[wiki/sid/common/topology-abe]] (#01 Common Topology ABE — diagram-only ABE in
  v23.0; resolved during the v1 Common ingest gap fill, see
  [[wiki/open-questions#OQ-041]])
- [[wiki/sid/common/location-abe]] (#02 Location ABE)

**Enterprise Domain Workforce ABE** (Table 4-10 #01) — out of corpus scope per
CLAUDE.md §3 (Enterprise Domain not in v1).

— GB1022 §4.5.2, Table 4-10, pp. 41–45.

## eTOM Processes Realised

GB1022 §4.5 Table 4-9 enumerates the eTOM L2 processes carried by the Production
block, sourced from GB921 R20.5. Cross-walk to our GB921 v25.5 corpus and the
resulting links are recorded in [[wiki/open-questions#OQ-040]].

**Service Domain L2s** — resolved to v25.5:

- [[wiki/etom/service-domain/service-support-management]] (Table 4-9 R20.5 1.4.4
  "SM&O Support & Readiness"; same ID, renamed in v25.5; v25.5 1.4.4 also absorbs
  R20.5 1.4.10 Service Test Management as L3 1.4.4.6 — see OQ-040)
- [[wiki/etom/service-domain/service-activation-management]] (R20.5 1.4.5 "Service
  Configuration & Activation"; same ID, renamed; v25.5 Extended Description still
  references the legacy name)
- [[wiki/etom/service-domain/service-problem-management]] (R20.5 1.4.6; same ID,
  same name)
- [[wiki/etom/service-domain/service-guiding-and-mediation]] (R20.5 1.4.8; same ID,
  same name)

**Resource Domain L2s** — resolved to v25.5:

- [[wiki/etom/resource-domain/resource-support-management]] (R20.5 1.5.4 "RM&O
  Support & Readiness"; same ID, renamed; v25.5 1.5.4 also absorbs R20.5 1.5.12
  Resource Test Management as L3 1.5.4.9, and parts of R20.5 1.5.5 Workforce
  Management and R20.5 1.5.6 Resource Provisioning — see OQ-040)
- [[wiki/etom/resource-domain/resource-data-management]] (R20.5 1.5.7 "Resource Data
  Collection & Distribution"; same ID, renamed)
- [[wiki/etom/resource-domain/resource-trouble-management]] (R20.5 1.5.8; same ID,
  same name)
- [[wiki/etom/resource-domain/resource-mediation-and-reporting]] (R20.5 1.5.10; same
  ID, same name)

**R20.5 entries deferred or out of scope:**

- R20.5 1.4.1, 1.4.2, 1.4.3, 1.5.2, 1.5.3 (Strategy / Capability / Specification
  L2s) — out of corpus scope per CLAUDE.md §3 (SIP vertical excluded)
- R20.5 1.X.Y Service Balance Management — source itself flags as "to be discussed
  for next versions"; no v25.5 target
- R20.5 1.4.10, 1.5.5, 1.5.6, 1.5.12 — restructured in v25.5; absorbing L2s already
  linked above; full reasoning in [[wiki/open-questions#OQ-040]]

— GB1022 §4.5, Table 4-9, pp. 38–40.

## Component Dependencies

- [[wiki/oda/functional-blocks/core-commerce-management]] — exposes Service
  capabilities consumed by CCM for product/offer construction; supplies usage data
  for CCM rating
- [[wiki/oda/functional-blocks/party-management]] — uses Party data for Service
  configuration (e.g. assigned phone numbers, internet addresses)
- [[wiki/oda/functional-blocks/engagement-management]] — surfaces Service status
  via user journeys
- [[wiki/oda/functional-blocks/intelligence-management]] — analyses Service/Resource
  performance data
- [[wiki/oda/functional-blocks/decoupling-and-integration]]

## Open Questions

- OQ-037: GB1022 mapping tables reference GB921/GB922 R20.5; corpus uses v25.x
- OQ-040: Production block trilateral sweep — R20.5→v25.x cross-walk decisions
  (resolved mappings, restructured L2s, Common Topology ABE gap)

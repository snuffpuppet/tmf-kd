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

GB1022 §4.5.2 (Standard Business Information Objects) provides verbatim mapping
tables from Frameworx SID ABEs to the Production block (source GB922 R20.5). Primary
domains covered: Service, Resource, and supporting Common ABEs.

In v25.x corpus terms, Production owns or directly references:

- Service Domain ABEs: Service Specification, Service, Service Configuration,
  Service Order, Service Usage, Service Test, Service Performance, Service Capacity,
  Service Problem (NotFullyDeveloped) — see
  [[wiki/sid/service-abe]]
- Resource Domain ABEs: Resource Specification, Resource, Resource Configuration,
  Resource Order, Resource Usage, Resource Test, Resource Performance, Resource
  Capacity, Resource Trouble (NotFullyDeveloped) — see
  [[wiki/sid/resource-abe]]
- Common Domain ABEs: Capacity, Configuration, Test, Performance (canonical patterns
  specialised by Service/Resource) — see [[wiki/sid/common-abe]]

See [[wiki/open-questions#OQ-008]] and [[wiki/open-questions#OQ-037]]. The full
mapping table is in source pp. 41–45.

## eTOM Processes Realised

GB1022 §4.5 maps Production to the Service and Resource Domain operational L2s. In
v25.5 corpus terms (with renaming caveats per OQ-036), Production realises:

- Service Domain operational L2s ([[wiki/etom/service-domain/_index]]) — all 8
  in-scope L2s
- Resource Domain operational L2s ([[wiki/etom/resource-domain/_index]]) — all 9
  in-scope L2s

See [[wiki/open-questions#OQ-008]] and [[wiki/open-questions#OQ-037]].

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

- OQ-008: ODA↔eTOM↔SID trilateral linking sweep deferred
- OQ-037: GB1022 mapping tables reference GB921/GB922 R20.5; corpus uses v25.x

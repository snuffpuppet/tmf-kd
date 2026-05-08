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
component_id: "GB1022 §4.2"
component_name: "Engagement Management"
psr_layer: "cross-cutting"
---

# Engagement Management

> **Architectural role.** Per GB1022 §3 Systems of Separation: Engagement Management
> is the front-end, fast-evolving block — handling user interactions powered by
> fast-moving technologies (customer experience, ergonomics, social networking) that
> service providers must adapt to quickly.
>
> **Non-business block.** §4.2.2 explicitly states that Engagement Management
> "Holds no business process (eTOM), no functions (functional Framework) and no
> operational data (SID)". Trilateral sections below note this structural exemption.

## Overview

The Engagement Management (EGM) Block represents the interaction point between the
enterprise and its ecosystem, which can be through different channels for different
experiences. EGM provides the capabilities to assure a digital, secure and accurate
interaction of all these stakeholders, providing digital and omnichannel capabilities
through the configuration of the different journeys reusing the processes and
functionalities provided by the platform.

Its scope includes interactions between users and processes handled by other
functions such as from the Intelligence Management, Party Management, Core Commerce
Management or Production Blocks. "Users" from the perspective of EGM, may be machines
and things (IoT context), humans (prospects, customers, users, employees, of people
working on behalf of partners and suppliers - 3rd parties) that collaborate and
integrate their own solutions to the ecosystem, providers of different services
(retailers, salespeople, technical providers). — GB1022 §4.2.1, p. 15

## Responsibilities

Engagement Management is characterized as (verbatim from §4.2.2, p. 16):

- Handling relationship between external and internal actors (including 3rd party
  systems, connected objects, …) and other ODA blocks.
- Managing the presentation layer according to the channel, the device to allow
  multi and cross-channel user journeys over multiple types of devices.
- Tailoring interactions using contextual information from back ends (360°view,
  process states).
- Relying on Processes, Functions and Data stored in the other ODA blocks (this is
  what enables reuse, cross channel and multi device).
- "Powering" customer / user journeys (what users see of the ongoing back end
  processes).
- **Holding no business process (eTOM), no functions (functional Framework) and no
  operational data (SID)**
- Holding technical functions – and data related to these functions and to their
  execution (context)
- Interacting with other ODA blocks only through Event or Process APIs (new APIs -
  definition ongoing), or read data through current standard TMF Open API

Standardised functionalities (Table 4-2) include: Front-ends (UIs), Journey
Management, Access to content, Content Aggregation, Content Organization,
Personalization of content, Filtering of content, Information Services, User
Interface Orchestration, plus additional entries in source.

## SID Entities Owned

Engagement Management holds no operational data per GB1022 §4.2.2. See
[[wiki/open-questions#OQ-038]].

## eTOM Processes Realised

Engagement Management holds no business processes per GB1022 §4.2.2. See
[[wiki/open-questions#OQ-038]].

## Component Dependencies

Engagement Management interacts with all other functional blocks (it surfaces their
processes/data through user journeys):

- [[wiki/oda/functional-blocks/decoupling-and-integration]] — for API mediation
- [[wiki/oda/functional-blocks/party-management]]
- [[wiki/oda/functional-blocks/core-commerce-management]]
- [[wiki/oda/functional-blocks/production]]
- [[wiki/oda/functional-blocks/intelligence-management]]

## Open Questions

- OQ-008: ODA↔eTOM↔SID trilateral linking sweep deferred
- OQ-038: Non-business ODA block trilateral exemption
- OQ-037: GB1022 mapping tables reference GB921/GB922 R20.5; corpus uses v25.x

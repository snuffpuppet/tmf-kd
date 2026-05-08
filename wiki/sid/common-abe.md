# Common Business Entities

Category landing page. Lists Common Business Entity ABEs ingested from GB922 Common.
This page is not normative for individual ABEs — entity-level content lives in the
per-ABE pages linked below.

> **Sub-domain note.** GB922 Common spans three sub-domains per the source's own
> Level 1 figures: Common, Pattern, and Shared (per [[wiki/foundations/domains]]
> §1.1.1.9–§1.1.1.11). The v1 wiki uses a single `abe_category: common` for all 19
> ABEs in this document; some (e.g. Communication Interaction) are explicitly placed
> in the Shared sub-domain by the source. See [[wiki/open-questions#OQ-014]] for the
> deferred decision on whether to formalise the split into separate categories.

## ABEs in this category

GB922 Common v23.0 organises the Common Domain into 27 per-chapter ABEs (§4.4–§4.30
of the source) plus four diagram-only ABEs declared in §4.1 [ComD-01] Common ABEs
Level 1 with brief definitions but no dedicated chapter. v1 ingest covered §4.4–§4.22
(2026-05-08T15:00Z); the remaining 12 ABEs were added in the gap-fill ingest of
2026-05-08T19:00Z (see [[wiki/open-questions#OQ-041]]).

**Per-chapter ABEs (§4.4–§4.30):**

- [[wiki/sid/common/party-abe]] — Party, PartyRole, and 11 nested sub-ABEs
- [[wiki/sid/common/party-privacy-abe]] — Privacy profiles, types, agreements
- [[wiki/sid/common/party-payment-abe]] — PartyPayment, PaymentMethod, PaymentPlan, Bank
- [[wiki/sid/common/communication-interaction-abe]] — CommunicationInteraction (Shared sub-domain per source)
- [[wiki/sid/common/digital-identity-abe]] — Digital identity for Party and Resource
- [[wiki/sid/common/calendar-abe]] — Time-related entities for scheduling
- [[wiki/sid/common/location-abe]] — GeographicAddress, Place, AdministrativeArea
- [[wiki/sid/common/base-types-abe]] — TimePeriod, value-object base types
- [[wiki/sid/common/root-business-entities-abe]] — RootEntity, EntitySpec/Entity, Characteristic patterns (foundational)
- [[wiki/sid/common/account-abe]] — Account, BusinessPartnerAccount, CustomerBillingAccount
- [[wiki/sid/common/business-interaction-abe]] — BusinessInteraction (parent of ProductOrder, Agreement)
- [[wiki/sid/common/agreement-abe]] — Agreement, SLA, CustomerPriceAgreement
- [[wiki/sid/common/capacity-abe]] — Canonical Capacity model (specialised by Product/Service/Resource)
- [[wiki/sid/common/catalog-abe]] — Catalog generalisation (Product/Service/Resource Catalog all derive)
- [[wiki/sid/common/configuration-and-profiling-abe]] — Canonical Configuration (specialised by Product/Service/Resource)
- [[wiki/sid/common/metric-abe]] — Standards of measurement, thresholds
- [[wiki/sid/common/performance-abe]] — Performance measure (specialised across domains)
- [[wiki/sid/common/policy-abe]] — Policy, PolicyRule, PolicyAction, PolicySet
- [[wiki/sid/common/project-abe]] — Generic project management model
- [[wiki/sid/common/test-abe]] — Canonical Test (Product/Service/Resource Test specialise)
- [[wiki/sid/common/usage-abe]] — Canonical Usage (Product/Service/Resource Usage specialise)
- [[wiki/sid/common/segmentation-abe]] — Criterion, segments
- [[wiki/sid/common/intent-abe]] — Intent, IntentReport
- [[wiki/sid/common/closed-loop-abe]] — «Preliminary» — closedloop management framework
- [[wiki/sid/common/goal-abe]] — «Preliminary» — Goal, GoalSpecification
- [[wiki/sid/common/workflow-abe]] — «Preliminary» — Workflow, Activity
- [[wiki/sid/common/anomaly-abe]] — Anomaly, AnomalySpecification

**Diagram-only ABEs (§4.1 brief; no dedicated chapter):**

- [[wiki/sid/common/topology-abe]] — Topological concepts (specialised by Resource Topology)
- [[wiki/sid/common/event-abe]] — Event modelling («not fully developed»)
- [[wiki/sid/common/trouble-ticket-abe]] — Trouble Ticket records («not fully developed»)
- [[wiki/sid/common/trouble-or-problem-abe]] — Trouble or Problem (parent of Service Problem and Resource Trouble)

For browsable listing see [[wiki/sid/common/_index]].

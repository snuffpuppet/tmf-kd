---
type: etom-l2
spec_id: GB921
spec_version: "25.5"
retrieval_date: 2026-05-11
source_paths:
  - raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx
source_extract_paths:
  - raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md
authority: primary
l1_parent: "1.4 Service Domain"
l2_id: "1.4.3"
l2_name: "Service Specification Lifecycle Management"
---

# Service Specification Lifecycle Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Business Value Development ([[wiki/foundations/lifecycle#Business Value Development]]) — _first BVD-vertical L2 ingested under Phase 3._
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

_Renamed in v24.0 — old name "Service Specification Development & Retirement"._

> **R20.5 lineage — distinguishing feature.** This L2 carries Original Process Identifier `1.2.2.3` (R20.5 numbering). **First S2R-vertical L2 in Phase 3 with R20.5 lineage** — the Strategy + Capability Management L2s ingested earlier in Phase 3 were uniformly v25.5-net-new (Original PID = None). BVD has pre-v25 history: GB921 R20.5 carried "Specification Development & Retirement" as the SIP-vertical L2, v24.0 renamed to "Specification Lifecycle Management", v25.5 re-grouped under the Business Value Development vertical. The R20.5 PID may appear in GB1022 §4.x ODA mapping tables — softer ODA gap than for v25.5-net-new L2s; see [[wiki/open-questions#OQ-046]].

## Overview

Service Specification Lifecycle Management processes are project oriented in that they develop and deliver new or enhanced service types. These processes include process and procedure implementation, systems changes and customer documentation. They also undertake rollout and testing of the service type, capacity management and costing of the service type. It ensures the ability of the enterprise to deliver service types according to requirements.

This process was renamed in 24.0. old name was- Service Specification Development &; Retirement

— GB921 v25.5 Excel master, process ID `1.4.3` (Original PID `1.2.2.3`), sheet `eTOM25,5`. Source text contains `&;` Excel-encoding artefacts (rendered verbatim above).

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master.

### 1.4.3.1 Gather & Analyze New Service Ideas

**Extended Description.**

The Gather & Analyze New Service Ideas processes combine specific product requirements with demographic, customer, technology and marketing information to identify specific new service classes/components or enhancements to existing service classes/components. These processes undertake the necessary analysis to identify potential service classes, compare current service classes with the identified required service classes, and as a result of the analysis develop new service class ideas. The new service class ideas include an analysis of the customer value proposition.

> **PSR-cascade observation.** Service-side input is *"specific product requirements"* — Product-domain upstream only. The Resource-side analog [[wiki/etom/resource-domain/resource-specification-lifecycle-management#1.5.3.1 Gather & Analyze New Resource Ideas|1.5.3.1]] takes input from *"specific product & service class requirements"* — Product **and** Service. Reflects the canonical PSR cascade: Product → Service → Resource at the requirements layer.

**L4 sub-processes:**

- **1.4.3.1.1** Analyze Service Classes — Undertake necessary analysis to identify potential service classes; compare current service classes with identified required service classes. _(source ED: "Not used for this process element")_
- **1.4.3.1.2** Develop Service Classes — Develop new service class ideas including analysis of customer value proposition. _(source ED: "Not used for this process element")_

### 1.4.3.2 Assess Performance of Existing Services

**Extended Description.**

The Assess Performance of Existing Services processes analyze the performance of existing services to identify inadequacies and required improvements. These processes use information from customers and from operational activities to identify required improvements.

_No L4 sub-processes in source._

### 1.4.3.3 Develop New Service Business Proposal

**Extended Description.**

The Develop New Service Business Proposal processes develop and document business proposals for the identified new or enhanced Service ideas (including if necessary a business case). The business proposal (or business case) identifies the new service requirements, including the specific resource components which underpin the service. The business proposal also identifies the service development, management and operations costs and anticipated benefits, including forecast demand, performance gains, productivity gains and/or operational cost improvements. The business proposal also includes an assessment of the risks and the competitive positioning of the service proposal. As a part of the business proposal development a feasibility assessment can be produced. Potential external parties who can assist in the development of the service classes are also identified (note that commercial arrangements may already be in place with these potential parties). As a part of the process, the business proposal is appropriately approved, and as a result of the approval, necessary staff and other resources are made available.

**L4 sub-processes:**

- **1.4.3.3.1** Develop Service Business Proposal — Develop and document business proposals; identify new service requirements + specific resource components; service development / management / operations costs and benefits; risks and competitive positioning; feasibility assessment; identification of potential parties.
- **1.4.3.3.2** Gain Service Business Proposal Approval — Manage approval of business proposal; on approval, necessary staff and other resources are made available. _(source ED: "Not used for this process element")_

### 1.4.3.4 Develop Detailed Service Specifications

**Extended Description.**

The Develop Detailed Service Specifications processes develop and document the detailed service-related technical and operational specifications, and customer manuals. These processes develop and document the required service features, the specific underpinning resource requirements and selections, the specific operational, and quality requirements and support activities, any service specific data required for the systems and network infrastructure as agreed through the Develop New Service Business Proposal processes.  The Develop Detailed Product Specifications processes provide input to these specifications. The processes ensure that all detailed specifications are produced and appropriately documented. Additionally the processes ensure that the documentation is captured in an appropriate enterprise repository.

**L4 sub-processes:**

- **1.4.3.4.1** Develop Detailed Service Technical Specifications — Required service features for systems and network infrastructure; documentation captured in enterprise repository.
- **1.4.3.4.2** Develop Detailed Service Support Specifications — Specific underpinning resource requirements and selections; captured in enterprise repository.
- **1.4.3.4.3** Develop Detailed Service Operational Specifications — Specific operational and quality requirements + support activities + service-specific data for systems / network infrastructure.
- **1.4.3.4.4** Develop Detailed Service Customer Manuals — Customer manuals as agreed through Develop New Service Business Proposal; documentation captured in enterprise repository.

### 1.4.3.5 Manage Service Development

**Extended Description.**

The Manage Service Development processes ensure the co-coordinated development in line with the approved business case of all required new or enhanced service classes/components for that business case across the enterprise. These processes ensure that all operational processes and procedures, IT systems changes, network changes, channel changes, operational procedures, testing tools and procedures, etc. required to support the new service class/component are identified and developed. These processes ensure that the necessary documentation and training packages are produced to support the operation of the new service class. These processes also ensure that the required service level agreements and operational level agreements to support the detailed service specifications are developed and agreed for each service class deployed, and that any party operational support has been identified and agreed. These processes have both program/project management aspects and technical/operational specification aspects, with the detailed management of individual service class deployment managed by the Manage Service Deployment processes.

As well as developing new service classes these processes manage upgrades or enhancements to existing service classes, as the need to review operational and other support is also relevant for upgrading existing classes/components.

Note that management of major new or enhanced infrastructure delivery to support service development is managed within the Service Capability Delivery process.

> **Cross-L2 boundary — Service Capability Delivery handoff.** The closing sentence above documents the Spec Lifecycle ↔ Capability Delivery boundary: this L2 (Spec Lifecycle) develops the *spec content* + project-managed class deployment; Capability Delivery (1.4.2 → [[wiki/etom/service-domain/service-capability-delivery|`service-capability-delivery`]]) does the *major infrastructure delivery* underneath. Distinct concerns, related work.
>
> **Implicit Service-side version management.** *"As well as developing new service classes these processes manage upgrades or enhancements to existing service classes…"* — confirms that the Service-side version-management treatment is implicit / folded into this L3, in contrast to the Resource-side which carries an explicit `1.5.19.4 Update and Version Resource Specifications` L3 in [[wiki/etom/resource-domain/resource-specification-management|Resource Specification Management]]. **Definitive PSR asymmetry on version management** — Service-side has no dedicated version-management L3 anywhere across Spec Mgmt (1.4.19) + Spec Lifecycle (1.4.3); Resource-side has one in Spec Mgmt (1.5.19.4).

**L4 sub-processes:**

- **1.4.3.5.1** Identify Required Processes & Procedures for Services — All operational processes / procedures, IT systems changes, network changes, channel changes, operational procedures, testing tools and procedures required to support the new service class/component are identified. _(source ED: "Not used for this process element")_
- **1.4.3.5.2** Develop Required Processes & Procedures for Services — Same scope as `.1` but developed. _(source ED: "Not used for this process element")_
- **1.4.3.5.3** Develop Service & Operational Agreements for Services — Required SLAs and OLAs are developed and agreed; party operational support identified. _(source ED: "Not used for this process element"; **brief contains "resource class deployed" rather than "service class deployed" — source-text bug; verbatim preserved per CLAUDE.md §1, §10.3, OQ-045-family handling.**)_
- **1.4.3.5.4** Gain Service & Operational Agreements Approval for Services — SLAs and OLAs agreed for each service class deployed; party operational support has been agreed. _(source ED: "Not used for this process element")_
- **1.4.3.5.5** Produce Supporting Documentation & Training Packages for Services — Necessary documentation and training packages produced to support operation of the new service class. _(source ED: "Not used for this process element")_

### 1.4.3.6 Manage Service Deployment

**Extended Description.**

The Manage Service Deployment processes ensure the co-coordinated deployment in line with the approved business case of all required service classes/components for that business case across the enterprise. These processes ensure that all operational processes and procedures, IT systems changes, network changes, channel changes, operational procedures, testing tools and procedures, etc. required to support the new service class/component have been implemented. These processes ensure that appropriate operational staff are identified and have received the necessary training. These processes ensure that the agreed party operational support has been implemented. These processes also ensure that acceptance testing is successfully performed to assure that the new or enhanced services comply with the specifications. These processes have both program/project and management aspects.

**L4 sub-processes:**

- **1.4.3.6.1** Manage Service Process & Procedure Implementation — All processes/procedures required to support new service class/component have been implemented. _(source ED: "Not used for this process element")_
- **1.4.3.6.2** Manage Service Operational Staff Training — Operational staff identified and received necessary training. _(source ED: "Not used for this process element")_
- **1.4.3.6.3** Develop Service Party Operational Support — Agreed party operational support has been implemented. _(source ED: "Not used for this process element"; **uses "Party" terminology — vs the Resource-side analog 1.5.3.6.3 which uses "Supplier/Partner" terminology — naming-asymmetry convention applies; preserved verbatim.**)_
- **1.4.3.6.4** Manage Service Acceptance Testing — Acceptance testing successfully performed; new or enhanced services comply with specifications. _(source ED: "Not used for this process element")_

### 1.4.3.7 Manage Service Exit

**Extended Description.**

The Manage Service Exit processes identify existing service classes which are unviable and manage the process to exit the Service from the products they support. The processes analyze existing service classes to identify economically or strategically unviable classes, identify products & customers impacted by any exit, develop product & customer specific exit or migration strategies, develop service infrastructure transition and/or replacement strategies, and manage the operational aspects of the exit process. A business proposal identifying the competitive threats, risks and costs may be required as a part of developing the exit strategy. These processes include any interaction with cross-enterprise co-ordination and management functions to ensure that the needs of all stakeholders are identified and managed.

> **PSR-asymmetric Exit decomposition.** This L3 has **no L4 decomposition in source**. The Resource-side analog [[wiki/etom/resource-domain/resource-specification-lifecycle-management#1.5.3.7 Manage Resource Exit|1.5.3.7]] has **4 L4s** breaking out the exit-process steps (Identify Unviable Resources, Identify Impacted Resource Customers, Develop Resource Transition Strategies, Manage Resource Exit Process). Strong PSR asymmetry — Resource side has explicit exit-step breakdown; Service side keeps the exit process at L3-narrative level only.

_No L4 sub-processes in source._

### 1.4.3.8 Service Specification Test Development & Retirement

> **New in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). PSR-symmetric with [[wiki/etom/resource-domain/resource-specification-lifecycle-management#1.5.3.8 Resource Specification Test Development & Retirement|Resource-side 1.5.3.8]]. Third instance in Phase 3 of v25.5 introducing test-related L3s into pre-existing process groups (after 1.4.1.8/9 + 1.5.1.8/9 Service/Resource Test Strategy and Analyze Service/Resource Test Quality).

**Extended Description.**

Service Test Development & Retirement is in charge of the Service Test catalogue.

A type of Service Test aims at measuring proper functioning and capacities of a Service.

Service Test Development & Retirement includes:

- Specifying in detail each Service Test according to the different context. It includes specifying:
    - the roles authorized to use the Test and quotas for each type of role
    - the method to conduct the Test
    - the rules that define the strategies for conducting the test (including  the test plan)
    - the thresholds and related actions
    - the relationships with lower level tests (Resource Test)
    - the report of test results with rules for enrichment of Resource Tests results according to role asking for it
- Specifying test scenarios defining sequence of Tests with rules about context and planning to trigger it. It includes roles allowed for asking test scenario and corresponding quotas.

> **Cross-PSR-test composition.** The fifth bullet *"the relationships with lower level tests (Resource Test)"* explicitly documents the PSR-test-cascade — Service Test is positioned as a *higher-level* test that consumes Resource Test results. The sixth bullet documents the enrichment direction: Service Test result reports enrich Resource Test results. PSR-test cascade is explicit at the test-catalogue level here.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.4.3.1** Gather & Analyze New Service Ideas — Combine product requirements with demographic, customer, technology and marketing information to identify specific new service classes/components or enhancements to existing service classes/components.
- **1.4.3.2** Assess Performance of Existing Services — Analyze the performance of existing services to identify inadequacies and required improvements.
- **1.4.3.3** Develop New Service Business Proposal — Develop and document business proposals for the identified new or enhanced Service ideas.
- **1.4.3.4** Develop Detailed Service Specifications — Develop and document the detailed service-related technical and operational specifications, and customer manuals.
- **1.4.3.5** Manage Service Development — Ensure the co-coordinated development in line with the approved business case of all required new or enhanced service classes/components.
- **1.4.3.6** Manage Service Deployment — Ensure the co-coordinated deployment in line with the approved business case.
- **1.4.3.7** Manage Service Exit — Identify existing service classes which are unviable and manage the processes to exit the Service from the market.
- **1.4.3.8** Service Specification Test Development & Retirement — In charge of the Service Test catalogue. _(New in v25.5; no R20.5 PID.)_

## SID Entities Manipulated

- [[wiki/sid/service/service-specification-abe]] — **lifecycle-driven manipulator**. This L2 manages the introduction-to-retirement lifecycle of service classes (L3 .4 develops detailed specifications; L3 .5 manages development incl. upgrades; L3 .7 manages exit/retirement). The Service Specification ABE is the data model. After this ingest, the ABE carries **four eTOM back-links** ordered by manipulator role: primary specifications-management (1.4.19) + capability-delivery upstream-input (1.4.2) + catalog-planning scope-specific (1.4.16) + **this L2's lifecycle-driven scope (1.4.3)**. The four manipulator roles distinguish temporal scope of the activity on the same ABE: ongoing-maintenance / project-driven-design / catalog-system-design / class-introduction-to-retirement. Densest trilateral pattern in the corpus.
- [[wiki/sid/service/service-test-abe]] — L3 1.4.3.8 Service Specification Test Development & Retirement explicitly manages the Service Test catalogue: specifying tests, roles, quotas, methods, rules, thresholds, scenarios. Direct match against the Test ABE's BE inventory (ServiceTest, ServiceTestSpecification per GB922 §4.8). Adds a second eTOM back-link to service-test-abe (alongside existing 1.4.1 from Strategy Management's Test-strategy L3s 1.4.1.8/9).

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). **Note: softer gap than for v25.5-net-new L2s** — this L2 carries R20.5 lineage (Original PID `1.2.2.3`). The R20.5 PID may appear in GB1022 §4.x mapping tables; the ODA cross-walk sweep when it happens has a real chance of resolving for this L2.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Service Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — R20.5-lineage status of this L2 softens the gap vs v25.5-net-new L2s)_

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
l1_parent: "1.5 Resource Domain"
l2_id: "1.5.3"
l2_name: "Resource Specification Lifecycle Management"
---

# Resource Specification Lifecycle Management

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Business Value Development ([[wiki/foundations/lifecycle#Business Value Development]]) — _first BVD-vertical L2 PSR pair ingested under Phase 3, paired with Service-side 1.4.3._
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

_Renamed in v24.0 — old name "Resource Specification Development & Retirement"._

> **R20.5 lineage.** Original Process Identifier `1.2.3.3` (R20.5 numbering). PSR-symmetric with the Service-side analog [[wiki/etom/service-domain/service-specification-lifecycle-management|1.4.3]] in this respect; BVD batch carries pre-v25 history that Capability Management batch did not. The R20.5 PID may appear in GB1022 §4.x ODA mapping tables — softer ODA gap than for v25.5-net-new L2s; see [[wiki/open-questions#OQ-046]].

## Overview

Resource Specification Lifecycle Management processes develop new, or enhance existing technologies and associated resource types, so that new Products are available to be sold to customers. They use the capability definition or requirements defined by Resource Strategy &; Planning They also decide whether to acquire resources from outside, taking into account the overall business policy in that respect. These processes also retire or remove technology and associated resource types, which are no longer required by the enterprise.

Resource types may be built, or in some cases leased from other parties. To ensure the most efficient and effective solution can be used, negotiations on network level agreements with other parties are paramount for both building and leasing.

These processes interact strongly with Product and  Engaged Party Development processes.

This process was renamed in 24.0 old name was Resource Specification Development &; Retirement

— GB921 v25.5 Excel master, process ID `1.5.3` (Original PID `1.2.3.3`), sheet `eTOM25,5`. Source text contains `&;` Excel-encoding artefacts (rendered verbatim above).

> **Cross-version naming reference.** The L2 ED references *"Resource Strategy &; Planning"* — this is the **pre-v24.0 name** for what is now [[wiki/etom/resource-domain/resource-strategy-management|1.5.1 Resource Strategy Management]] (renamed v24.0). Preserve verbatim per CLAUDE.md §1, §10.3; a reader seeking "Resource Strategy & Planning" won't find a current page by that name — the current resource-strategy L2 is 1.5.1.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master.

### 1.5.3.1 Gather & Analyze New Resource Ideas

**Extended Description.**

The Gather & Analyze New Resource Ideas processes combine specific product & service class requirements with demographic, customer, technology and marketing information to identify specific new resource classes/components, or enhancements to existing resource classes/components. These processes undertake the necessary analysis to identify potential resource classes, compare current resource classes with the identified required resource classes, and as a result of the analysis develop new resource class ideas.

> **PSR-cascade observation.** Input is *"specific product & service class requirements"* — Product **and** Service upstream. The Service-side analog [[wiki/etom/service-domain/service-specification-lifecycle-management#1.4.3.1 Gather & Analyze New Service Ideas|1.4.3.1]] takes input from Product only. Reflects the canonical PSR cascade: Product → Service → Resource at the requirements layer.

**L4 sub-processes:**

- **1.5.3.1.1** Analyze Resource Classes — Undertake necessary analysis to identify potential resource classes; compare current resource classes with identified required service classes. _(source ED: "Not used for this process element"; **brief reads "required service classes" not "required resource classes" — source-text artefact, verbatim preserved.**)_
- **1.5.3.1.2** Develop Resource Classes — Develop new resource class ideas including customer value proposition analysis. _(source ED: "Not used for this process element")_

### 1.5.3.2 Assess Performance of Existing Resources

**Extended Description.**

The Assess Performance of Existing Resources processes analyze the performance of existing resources to identify inadequacies and required improvements. These processes use information from customers and from operational activities to identify required improvements.

_No L4 sub-processes in source._

### 1.5.3.3 Develop New Resource Business Proposal

**Extended Description.**

The Develop New Resource Business Proposal processes develop and document business proposals for the identified new or enhanced Resource ideas (including if necessary a business case). The business proposal (or business case) identifies the resource development (e.g.. network and/or IT resources), management and operations costs and anticipated benefits, including forecast demand, performance gains, productivity gains and/or operational cost improvements specifically associated with the resource business proposal. The business proposal also includes an assessment of the risks and the competitive positioning of the proposal. As a part of the business proposal development a feasibility assessment can be produced. Potential other parties who can assist in the development of the resource classes are also identified (note that commercial arrangements may already be in place with these potential related parties. As a part of the process, the business proposal is appropriately approved, and as a result of the approval, necessary staff and other resources are made available.

**L4 sub-processes:**

- **1.5.3.3.1** Develop Resource Business Proposal — Develop and document business proposals; identifies resource development (network/IT resources), management and operations costs, forecast demand, performance/productivity gains, risks, competitive positioning, feasibility assessment, identification of potential parties.
- **1.5.3.3.2** Gain Resource Business Proposal Approval — Manage approval of business proposal; on approval, necessary staff and resources are made available. _(source ED: "Not used for this process element")_

### 1.5.3.4 Develop Detailed Resource Specifications

**Extended Description.**

The Develop Detailed Resource Specifications processes develop and document the detailed resource-related technical, performance and operational specifications, and manuals. These processes develop and document the required resource features, the specific technology requirements and selections, the specific operational, performance and quality requirements and support activities, any resource specific data required for the systems and network infrastructure. The Develop Detailed Resource Specifications processes provide input to these specifications. The processes ensure that all detailed specifications are produced and appropriately documented. Additionally the processes ensure that the documentation is captured in an appropriate enterprise repository.

**L4 sub-processes:**

- **1.5.3.4.1** Develop Detailed Resource Technical Specifications — Required resource features for systems and network infrastructure; documentation captured in enterprise repository.
- **1.5.3.4.2** Develop Detailed Resource Support Specifications — Specific technology requirements and selections for systems and network infrastructure.
- **1.5.3.4.3** Develop Detailed Resource Operational Specifications — Specific operational and quality requirements + support activities + resource-specific data for systems / network infrastructure.
- **1.5.3.4.4** Develop Detailed Resource Manuals — Documentation manuals; captured in enterprise repository.

### 1.5.3.5 Manage Resource Development

**Extended Description.**

The Manage Resource Development processes ensure the co-coordinated development in line with the approved business case of all required resource classes/components for that business case across the enterprise. These processes ensure that all operational processes and procedures, resource changes (e.g. network and/or IT resources), operational procedures, testing tools and procedures, etc. required to support the new resource class/component are identified and developed. These processes ensure that the necessary documentation and training packages are produced to support the operation of the new resource class. These processes also ensure that the required service level agreements and operational level agreements are developed and agreed for each resource class deployed, and that any other parties operational support has been identified and agreed. These processes have both program/project management aspects and technical/operational specification aspects, with the detailed management of individual resource class deployment managed by the Manage Resource Deployment processes.

Note that management of major new or enhanced infrastructure delivery to support product and offer development is managed within the Resource Capability Delivery process.

Note that delivery of resource classes/components within the context of existing commercial arrangements is managed through the  Party Offering Development & Retirement process. If new related parties are required, the Party Tender Management and Party Agreement Management processes are used to deliver the necessary commercial arrangements

> **Cross-L2 boundary — Resource Capability Delivery handoff.** First "Note that" — documents the Spec Lifecycle ↔ Capability Delivery boundary on the Resource side: this L2 develops the *spec content* + project-managed class deployment; Capability Delivery (1.5.2 → [[wiki/etom/resource-domain/resource-capability-delivery|`resource-capability-delivery`]]) does the *major infrastructure delivery* underneath. PSR-symmetric with Service-side 1.4.3.5.
>
> **Forward references to out-of-scope Party processes.** Second "Note that" — references Party Offering Development & Retirement, Party Tender Management, Party Agreement Management. All Engaged Party / Business Partner domain processes — out of L1 scope per CLAUDE.md §3. Pattern matches previous Phase 3 forward references to "Engaged Party domains" (1.4.1.6 / 1.4.2.4 / 1.4.2.6) and "Party Offering Development & Retirement" (1.5.1.2 / 1.5.1.6 / 1.5.2.6).

**L4 sub-processes:**

- **1.5.3.5.1** Identify Required Processes & Procedures for Resources — All operational processes / procedures, resource changes (network/IT), operational procedures, testing tools required to support new resource class/component are identified. _(source ED: "Not used for this process element")_
- **1.5.3.5.2** Develop Required Processes & Procedures for Resources — Same scope as `.1` but developed. _(source ED: "Not used for this process element")_
- **1.5.3.5.3** Develop Service & Operational Agreements for Resources — SLAs and OLAs developed for each resource class deployed; party operational support identified. _(source ED: "Not used for this process element")_
- **1.5.3.5.4** Gain Service & Operational Agreements Approval for Resources — SLAs and OLAs agreed for each resource class deployed; party operational support has been agreed. _(source ED: "Not used for this process element")_
- **1.5.3.5.5** Produce Supporting Documentation & Training Packages for Resources — Necessary documentation and training packages produced to support operation of the new resource class. _(source ED: "Not used for this process element")_

### 1.5.3.6 Manage Resource Deployment

**Extended Description.**

The Manage Resource Deployment processes ensure the co-coordinated deployment in line with the approved business case of all required resource classes/components for that business case across the enterprise. These processes ensure that all operational processes and procedures, resource changes (e.g. network and/or IT resources), operational procedures, testing tools and procedures, etc. required to support the new resource class/component have been implemented. These processes ensure that appropriate operational staff are identified and have received the necessary training. These processes ensure that the agreed other parties operational support has been implemented. These processes also ensure that acceptance testing is successfully performed to assure that the new or enhanced resources comply with the specifications. These processes have both program/project and management aspects.

**L4 sub-processes:**

- **1.5.3.6.1** Manage Resource Process & Procedure Implementation — All processes/procedures required to support new resource class/component have been implemented. _(source ED: "Not used for this process element")_
- **1.5.3.6.2** Manage Resource Operational Staff Training — Operational staff identified and received necessary training. _(source ED: "Not used for this process element")_
- **1.5.3.6.3** Develop Resource Supplier/Partner Operational Support — Agreed other parties operational support has been implemented. _(source ED: "Not used for this process element"; **uses "Supplier/Partner" terminology — vs Service-side analog 1.4.3.6.3 which uses "Party" terminology — naming-asymmetry convention applies; preserved verbatim.**)_
- **1.5.3.6.4** Manage Resource Acceptance Testing — Acceptance testing successfully performed; new or enhanced resources comply with specifications. _(source ED: "Not used for this process element")_

### 1.5.3.7 Manage Resource Exit

**Extended Description.**

The Manage Resource Exit processes identify existing resource classes which are unviable and manage the process to exit the Resource from the services they support. The processes analyze existing resource classes to identify economically or strategically unviable classes, identify products, services classes & customers impacted by any exit, develop specific exit or migration strategies, develop resource infrastructure transition and/or replacement strategies, and manage the operational aspects of the exit process. A business proposal identifying the competitive threats, risks and costs may be required as a part of developing the exit strategy. These processes include any interaction with cross-enterprise co-ordination and management functions to ensure that the needs of all stakeholders are identified and managed.

> **PSR-asymmetric Exit decomposition.** This L3 carries **4 L4s** breaking out the exit-process steps. The Service-side analog [[wiki/etom/service-domain/service-specification-lifecycle-management#1.4.3.7 Manage Service Exit|1.4.3.7]] carries **0 L4s** — Service side keeps Exit at L3-narrative level only. Resource side has explicit exit-step breakdown. Strong PSR asymmetry on retirement-process granularity.

**L4 sub-processes:**

- **1.5.3.7.1** Identify Unviable Resources — Analyze existing resource classes to identify economically or strategically unviable classes. _(source ED: "Not used for this process element")_
- **1.5.3.7.2** Identify Impacted Resource Customers — Identify products, services classes & customers impacted by any exit. _(source ED: "Not used for this process element")_
- **1.5.3.7.3** Develop Resource Transition Strategies — Develop specific exit or migration strategies; develop resource infrastructure transition and/or replacement strategies. _(source ED: "Not used for this process element")_
- **1.5.3.7.4** Manage Resource Exit Process — Manage the operational aspects of the exit process. _(source ED: "Not used for this process element")_

### 1.5.3.8 Resource Specification Test Development & Retirement

> **New in v25.5.** Original Process Identifier = `None` (no R20.5 / pre-v25 equivalent). PSR-symmetric with [[wiki/etom/service-domain/service-specification-lifecycle-management#1.4.3.8 Service Specification Test Development & Retirement|Service-side 1.4.3.8]]. Third instance in Phase 3 of v25.5 introducing test-related L3s into pre-existing process groups.

**Extended Description.**

Resource Test Development & Retirement is in charge of the Resource Test catalogue.

A type of Resource Test aims at measuring proper functioning and capacities of a Resource.

Resource Test Development & Retirement includes:

- Specifying in detail each Resource Test according to the different context. It includes specifying:
    - the roles authorized to use the Test and quotas for each type of role
   - the method to conduct the Test
   - the rules that define the strategies for conducting the test (including  the test plan)
   - the thresholds and related actions
   - the report of test results with rules for enrichment of Resource Tests results according to role asking for it
- Specifying test scenarios defining sequence of Tests with rules about context and planning to trigger it. It includes roles allowed for asking test scenario and corresponding quotas.

> **Source-text observation — possible copy-paste artefact.** The fifth bullet *"the report of test results with rules for enrichment of **Resource** Tests results according to role asking for it"* references Resource Tests enriching Resource Test results — either (a) recursive Resource-test composition, or (b) parallel structure mirroring the Service-side analog's "enrichment of Resource Tests results" phrasing without changing it. The Service-side analog [[wiki/etom/service-domain/service-specification-lifecycle-management#1.4.3.8 Service Specification Test Development & Retirement|1.4.3.8]] has both this enrichment line AND an additional line *"the relationships with lower level tests (Resource Test)"* — this Resource-side L3 lacks the second line (because Resource Test has no lower-level tests in the PSR hierarchy). Preserved verbatim per CLAUDE.md §1, §10.3, OQ-045-family handling. No separate OQ filed.

_No L4 sub-processes in source._

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.5.3.1** Gather & Analyze New Resource Ideas — Combine product & service class requirements with demographic, customer, technology and marketing information to identify specific new resource classes/components, or enhancements to existing resource classes/components.
- **1.5.3.2** Assess Performance of Existing Resources — Analyze the performance of existing resources to identify inadequacies and required improvements.
- **1.5.3.3** Develop New Resource Business Proposal — Develop and document business proposals for the identified new or enhanced Resource ideas.
- **1.5.3.4** Develop Detailed Resource Specifications — Develop and document the detailed resource-related technical, performance and operational specifications, and manuals.
- **1.5.3.5** Manage Resource Development — Ensure the co-coordinated delivery in line with the approved business case of all required resource classes/components capabilities for that business case across the enterprise.
- **1.5.3.6** Manage Resource Deployment — Ensure the co-coordinated deployment in line with the approved business proposal of all required resource classes/components for that business proposal across the enterprise.
- **1.5.3.7** Manage Resource Exit — Identify existing resource classes which are unviable and manage the processes to exit the Resource from the market.
- **1.5.3.8** Resource Specification Test Development & Retirement — In charge of the Resource Test catalogue. _(New in v25.5; no R20.5 PID.)_

## SID Entities Manipulated

- [[wiki/sid/resource/resource-specification-abe]] — **lifecycle-driven manipulator**. This L2 manages the introduction-to-retirement lifecycle of resource classes (L3 .4 develops detailed specifications; L3 .5 manages development incl. upgrades; L3 .7 manages exit/retirement with 4 explicit L4 steps). The Resource Specification ABE is the data model. After this ingest, the ABE carries **four eTOM back-links** ordered by manipulator role: primary specifications-management (1.5.19) + capability-delivery upstream-input (1.5.2) + catalog-planning scope-specific (1.5.18) + **this L2's lifecycle-driven scope (1.5.3)**. The four manipulator roles distinguish temporal scope on the same ABE: ongoing-maintenance / project-driven-design / catalog-system-design / class-introduction-to-retirement. Densest trilateral pattern in the corpus, paralleling the Service-side. Target ABE is `release_status: pre-production` per [[wiki/open-questions#OQ-027]].
- [[wiki/sid/resource/resource-test-abe]] — L3 1.5.3.8 Resource Specification Test Development & Retirement explicitly manages the Resource Test catalogue: specifying tests, roles, quotas, methods, rules, thresholds, scenarios. Direct match against the Test ABE's BE inventory (ResourceTest, ResourceTestSpecification per GB922 §4.7). Adds a second eTOM back-link to resource-test-abe (alongside existing 1.5.1 from Strategy Management's Test-strategy L3s 1.5.1.8/9). Pre-production source.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables). **Note: softer gap than for v25.5-net-new L2s** — this L2 carries R20.5 lineage (Original PID `1.2.3.3`). The R20.5 PID may appear in GB1022 §4.x mapping tables; the ODA cross-walk sweep when it happens has a real chance of resolving for this L2.

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Resource Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — R20.5-lineage status of this L2 softens the gap)_

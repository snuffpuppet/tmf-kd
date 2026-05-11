---
type: etom-l2
spec_id: GB921
spec_version: "25.5"
retrieval_date: 2026-05-10
source_paths:
  - raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx
source_extract_paths:
  - raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md
authority: primary
l1_parent: "1.5 Resource Domain"
l2_id: "1.5.2"
l2_name: "Resource Capability Delivery"
---

# Resource Capability Delivery

> **Lifecycle area:** Strategy-to-Readiness ([[wiki/foundations/lifecycle#Strategy-to-Readiness]]).
> **Vertical context:** Capability Management ([[wiki/foundations/lifecycle#Capability Management]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Capability Delivery processes use the capability definition or requirements to deploy new and/or enhanced technologies and associated resources.

The objectives of these processes is to ensure that network, application and computing resources are deployed, according to the plans set by Resource Development. They deliver the physical resource capabilities necessary for the ongoing operations, and long term well-being of the enterprise, and ensure the basis on which all resources and services will be built. Using automation may enhance resource capability delivery.

Responsibilities of the Resource Capability Delivery processes include, but are not limited to:

•  Planning resource supply logistics (warehousing, transport, etc.)
•  Planning the Resource Installation
•  Contracting and Directing the Resource Construction where needed
•  Verifying the Resource Installation
•  Handover the Resource Capability to Operations through interactions with the Manage Resource Class Configuration

Logical network configurations (such as resource elements integration) are as important to the network resources as the physical aspects. All aspects must be planned and considered in the design and implementation of the network, including infrastructure owned by the enterprise, and by supplier/partners, other physical resources and logical elements. Logical network configuration may be designed digitally in order to make sure all the resources are aligned and planned proactively.

— GB921 v25.5 Excel master, process ID `1.5.2` (Original PID `1.2.3.2` — R20.5 SIP-vertical Resource-side numbering), sheet `eTOM25,5`.

> **Source-text observation — "Manage Resource Class Configuration" forward reference.** The fifth Responsibilities bullet refers to "interactions with the Manage Resource Class Configuration." No L2 by that name exists in v25.5; possible R20.5 legacy reference. Verbatim preserved; pattern matches OQ-045-family handling (intent recognisable; not blocking; no separate OQ filed).

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master.

> **Source-text observation — AI / automation / digital references.** GB921 v25.5's Resource Capability Delivery L3 EDs (1.5.2.1, 1.5.2.2, 1.5.2.3, plus four L4 EDs in 1.5.2.2) carry repeated explicit references to *"AI forecasting techniques"*, *"automated process … using advanced technologies such as AI"*, *"automated processes to improve efficiency and shorten TTM"*, *"console or visual platform"* visualisation. The Service-side analog L2 (1.4.2) carries no such references in its L3 EDs. This is the same v25.5 PSR-asymmetry pattern observed in the 1.4.1 ↔ 1.5.1 Strategy Management pair. Preserved verbatim below; surfaced here so the asymmetry is visible to readers comparing PSR pairs.

### 1.5.2.1 Map & Analyze Resource Requirements

**Extended Description.**

The Map & Analyze Resource Requirements processes define the detailed resource infrastructure requirements to guide the definition of service capabilities required by the enterprise. The processes provide detailed analysis of new resource requirements linked to relevant geographic distributions which for example in mobile networks may be as small as a cell level. These processes also establish the detailed performance requirements. These processes take the forecast information available from the Produce Resource Business Plans and requirements information from the Map & Analyze Service Requirements processes, as well as resource infrastructure requirements developed by the Develop Detailed Resource Specifications processes, to establish detailed views of anticipated resource demand and performance requirements. These views may be displayed on a console or visual platform and shared by relevant resource owners.

These processes manage the capacity planning for the resource infrastructure, and identify capacity requirements based on service forecasts and appropriate resource related metrics, i.e., transaction volumes, storage requirements, traffic volumes, port availabilities, etc. These forecasts may be based on near real-time information and use AI forecasting techniques.

The processes include any interaction with cross-enterprise and cross-domain coordination and management functions to ensure that the demand distributions capture the needs of relevant stakeholders. Coordination and management function may use automated processes to improve efficiency and shorten TTM.

> **Cross-domain handoff (back-reference):** the input from "Map & Analyze Service Requirements" referenced above is L3 [[wiki/etom/service-domain/service-capability-delivery#1.4.2.1 Map & Analyze Service Requirements|1.4.2.1]] on the Service-side. This L3 is the documented receiving end of the Service-to-Resource Capability-Management cross-domain integration chain.

**L4 sub-processes:**

- **1.5.2.1.1** Capture Resource Demand & Performance Requirements — Detailed analysis of new resource requirements linked to geographic distributions (cell-level granularity in mobile networks); establish detailed performance requirements; manage capacity planning with concrete metrics (transaction volumes, storage requirements, traffic volumes, port availabilities); forecasts may use near-real-time information + AI forecasting. Visualisation via console or visual platform shared by resource owners.
- **1.5.2.1.2** Agree Resource Infrastructure Requirements — Obtain agreement to detailed resource infrastructure requirements; cross-enterprise + cross-domain coordination; coordination/management may use automated processes for efficiency and TTM.

### 1.5.2.2 Capture Resource Capability Shortfalls

**Extended Description.**

The Capture Resource Capability Shortfalls processes identify specific or imminent resource capacity, resource performance and/or resource operational support shortfalls. These processes take information available from the Resource Management & Operations processes to establish detailed views of anticipated resource and shortfalls and support process issues. These views may be displayed on a console or visual platform and shared by relevant resource owners.

Resource capability shortfalls may be captured via an automated process. It may process information using advanced technologies such as AI.

**L4 sub-processes:**

- **1.5.2.2.1** Capture Resource Capacity Shortfalls — Identify specific or imminent resource capacity shortfalls; visualisation on console/visual platform; AI / automated capture available.
- **1.5.2.2.2** Capture Resource Performance Shortfalls — Identify specific or imminent resource performance shortfalls; same visualisation + AI / automation pattern.
- **1.5.2.2.3** Capture Resource Operational Support Shortfalls — Identify specific or imminent resource operational support shortfalls; same visualisation + AI / automation pattern.

### 1.5.2.3 Gain Resource Capability Investment Approval

**Extended Description.**

The Gain Resource Capability Investment Approval processes capture all activities required to develop and gain necessary approval for investment proposals to develop and deliver the required resource capabilities, including identification of potential other parties. These processes take the input from the Map & Analyze Resource Requirements, the Capture Resource Capability Shortfalls and the Map & Analyze Service Requirements processes to develop and gain approval for any business proposals arising. In some cases the business proposal may require the creation and approval of a formal business case, in other cases the business proposal approval may be delegated to local management. In any event the cost estimates for delivering the resource infrastructure, including costs for materials (equipment and tools), labor and training are part of the investment proposal.

The rules and procedures outlining the necessary approval process to be used are also part of these processes.

The processes include any interaction with cross-enterprise and cross-domain coordination and management functions to ensure that the demand distributions capture the needs of relevant stakeholders. Coordination and management function may use automated processes to improve efficiency and shorten TTM.

**L4 sub-processes:**

- **1.5.2.3.1** Develop Resource Capability Investment Proposals — Capture all activities required to develop business proposals for required resource capabilities; identification of potential other parties; cost estimates for resource infrastructure incl. materials, labor, training; rules/procedures for the approval process.
- **1.5.2.3.2** Approve Resource Capability Investment — Capture all activities required to gain necessary approval for resource business proposals; cross-enterprise + cross-domain coordination; automated coordination for efficiency.

### 1.5.2.4 Design Resource Capabilities

**Extended Description.**

The Design Resource Capabilities processes manage the design of the resource infrastructure to meet the requirements in any approved investment proposals. These processes ensure the collation and coordination of requirements from all approved investment proposals, assess the most appropriate resource infrastructure, develop the tactical/solution architecture and design specifications to be used to build or source the necessary resource infrastructure components, and select the most appropriate resource infrastructure other parties to support the resource requirements. A key element of the overall design is the integration approach between the existing legacy resource infrastructure and any proposed new resource infrastructure. This integration design is managed within the architecture and specification processes.

Note that the actual management of the sourcing process is handled within the Party Offering Development & Retirement processes.

**L4 sub-processes:**

- **1.5.2.4.1** Define Resource Capability Requirements — Ensure the collation and coordination of requirements from all approved investment proposals. _(source ED: "Not used for this process element")_
- **1.5.2.4.2** Specify Resource Capability Infrastructure — Assess the most appropriate resource infrastructure; develop tactical/solution architecture and design specifications for building or sourcing the necessary resource infrastructure components. Key element: integration approach between existing legacy and proposed new resource infrastructure. _Source ED references "Supply Chain Development & Management processes" for sourcing process management — asymmetric to the L2 ED's "Party Offering Development & Retirement" reference; preserved verbatim._
- **1.5.2.4.3** Select Resource Capability at Other Parties — Select the most appropriate resource infrastructure at other parties to support the identified resource capability requirements. _(source ED: "Not used for this process element")_

### 1.5.2.5 Enable Resource Support & Operations

**Extended Description.**

The Enable Resource Support & Operations processes manage the design of any improvements or changes required to the resource operational support processes to support the investment proposals and new resource capabilities and infrastructure. The processes ensure the identification of operational support groups, required skill sets, and availability of appropriate training programs. These processes ensure the identification, collation and coordination of support requirements from all approved investment proposals, and from any operational support shortfalls identified in the Capture Resource Capability Shortfalls processes.

**L4 sub-processes:**

- **1.5.2.5.1** Design Resource Operational Support Process Improvements — Manage the design of any improvements or changes required to resource operational support processes. _(source ED: "Not used for this process element")_
- **1.5.2.5.2** Identify Resource Support Groups, Skills & Training — Ensure the identification of operational support groups, required skill sets, and availability of appropriate training programs. _(source ED: "Not used for this process element")_
- **1.5.2.5.3** Identify Resource Support Requirements — Ensure identification, collation and coordination of support requirements from all approved investment proposals and any operational support shortfalls.

### 1.5.2.6 Manage Resource Capability Delivery

**Extended Description.**

The Manage Resource Capability Delivery processes manage the provision, implementation, commissioning and roll-out of the new or enhanced resource capability and associated operational support processes. These processes are predominantly program/project management process functions, and require the detailed management and co-ordination of the delivery of individual resource infrastructure components to achieve the delivery of the overall resource capability. Within the Manage Resource Capability Delivery processes separate other parties may be responsible for the delivery of the resource capability, and other  parties for the installation and construction. The Manage Resource Capability Delivery processes ensure that the roles and responsibilities of all parties are identified, managed and coordinated.

These processes are responsible to ensure that the quality of the implemented resource capability meets the design specifications. These processes manage the commissioning of the new resource infrastructure by ensuring the availability of test programs and specifications against which to test the new resource infrastructure meets the design requirements.

These processes leverage the Party Offering Development & Retirement processes as necessary to establish any new sourcing arrangements for the delivery of resource components.

**L4 sub-processes:**

- **1.5.2.6.1** Co-ordinate Resource Capability Delivery — Ensure provision, implementation and roll-out of new/enhanced resource capability and associated operational support; predominantly program/project management; multi-party (delivery vs installation/construction) coordination.
- **1.5.2.6.2** Ensure Resource Capability Quality — Ensure the quality of the implemented resource capability meets the design specifications. _(source ED: "Not used for this process element")_
- **1.5.2.6.3** Manage Commissioning of New Resource Infrastructure — Manage the commissioning of new resource infrastructure by ensuring the availability of test programs and specifications against which to test that new resource infrastructure meets design requirements. _(source ED: "Not used for this process element"; **PSR-asymmetric — no analog L4 on Service-side L3 1.4.2.6**.)_
- **1.5.2.6.4** Establish Resource Capability Sourcing — Leverage the Supply Chain Development & Management processes as necessary to establish any new sourcing arrangements for the delivery of resource components. _(source ED: "Not used for this process element"; brief references "Supply Chain Development & Management" — asymmetric to the L3 ED's "Party Offering Development & Retirement" reference.)_

> **Asymmetry vs Service-side 1.4.2.6.** Service-side 1.4.2.6 has 6 L4s — co-ordinate, ensure quality, establish sourcing, develop timetables, track and report, ensure costs. Resource-side 1.5.2.6 has 4 L4s — co-ordinate, ensure quality, **manage commissioning of new resource infrastructure** (Resource-only — physical-hardware concern), establish sourcing. The commissioning step + the dropped Timetables/Reporting/Costs L4s reflect that Resource Capability Delivery has a physical-infrastructure dimension (test programs, design-requirements verification on installed hardware) that Service Capability Delivery does not, while Service Capability Delivery breaks out the program-management bookkeeping more granularly. Preserved verbatim per CLAUDE.md §1, §10.3.

### 1.5.2.7 Manage Handover to Resource Operations

**Extended Description.**

The Manage Handover to Resource Operations processes manage the processes involved in handover of deployed resource infrastructure to operational control. These processes ensure that all operational and performance design requirements have been met by the installed resource infrastructure, and that all tools, test equipment, operational procedures, support groups, and training is in place to allow for successful operation. These processes include the management and coordination of all stakeholders required to gain approval and acceptance of the handover to operational control.

**L4 sub-processes:**

- **1.5.2.7.1** Co-ordinate Resource Operational Handover — Co-ordinate the handover processes; manage stakeholder approval and acceptance of handover to operational control.
- **1.5.2.7.2** Validate Resource Infrastructure Design — Ensure that all operational and process performance design requirements have been met by the installed resource infrastructure. _(source ED: "Not used for this process element")_
- **1.5.2.7.3** Ensure Resource Handover Support — Ensure that all tools, test equipment, operational procedures, support groups, and training is in place to allow for successful operation. _(source ED: "Not used for this process element")_

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5 Excel master `Brief description` column:

- **1.5.2.1** Map & Analyze Resource Requirements — Define the detailed resource infrastructure requirements to support the service capabilities required by the enterprise
- **1.5.2.2** Capture Resource Capability Shortfalls — Identify specific or imminent resource capacity, resource performance and/or resource operational support shortfalls
- **1.5.2.3** Gain Resource Capability Investment Approval — Capture all activities required to develop and gain necessary approval for investment proposals to develop and deliver the required resource capabilities
- **1.5.2.4** Design Resource Capabilities — Manage the design of the resource infrastructure to meet the requirements in any approved investment proposals.
- **1.5.2.5** Enable Resource Support & Operations — Manage the design of any improvements or changes required to the resource operational support processes to support the investment proposals and new resource capabilities and infrastructure
- **1.5.2.6** Manage Resource Capability Delivery — Manage the provision, implementation, commissioning and roll-out of the new or enhanced resource capability, and associated operational support processes.
- **1.5.2.7** Manage Handover to Resource Operations — Manage the processes involved in handover of deployed resource infrastructure to operational control

## SID Entities Manipulated

- [[wiki/sid/resource/resource-specification-abe]] — direct match for L3 1.5.2.4 Design Resource Capabilities, which produces resource design specifications used to build or source resource infrastructure components. The Resource Specification ABE (carrying Physical / Logical / Compound resource specs) is the data side of the capability-design output. Target ABE is `release_status: pre-production` per [[wiki/open-questions#OQ-027]].
- [[wiki/sid/resource/resource-capacity-abe]] — L3 1.5.2.1 explicitly addresses resource capacity planning with concrete capacity metrics (transaction volumes, storage requirements, traffic volumes, port availabilities); L3 1.5.2.2 captures resource capacity shortfalls. Target ABE is `release_status: pre-production` per OQ-027.

## ODA Components That Realise This Process

See open-questions.md — OQ-046 (S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables; the v25.5 Original Process Identifier `1.2.3.2` references the R20.5 SIP-vertical Resource-side numbering scheme).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep _(open — applies as a class)_
- OQ-035: Source verbatim extracted from the Excel master; no Resource Process Decompositions PDF analog exists for the S2R-vertical L2s at v24.0, so no narrative-PDF supplementation pass is anticipated for this L2 _(open)_
- OQ-046: S2R-vertical eTOM L2s — ODA component cross-walk against GB1022 mapping tables _(open — filed 2026-05-10 with the 1.4.1 ingest; applies forward to all 16 S2R L2s)_

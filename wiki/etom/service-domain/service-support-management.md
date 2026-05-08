---
type: etom-l2
spec_id: GB921
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx
source_extract_paths:
  - raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md
authority: primary
l1_parent: "1.4 Service Domain"
l2_id: "1.4.4"
l2_name: "Service Support Management"
---

# Service Support Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

## Overview

Service Support Management processes manage service infrastructure, ensuring that the appropriate service capacity is available and ready to support the SM&O Fulfillment, Assurance and Billing processes in instantiating and managing service instances, and for monitoring and reporting on the capabilities and costs of the individual SM&O FAB processes. 
The responsibilities of these processes include, but are not limited to:
• Supporting the operational introduction of new and/or modified service infrastructure;
• Managing and ensuring the ongoing quality of the Service Inventory;
• Applying service capacity rules from Infrastructure Lifecycle Management processes;
• Analyzing availability and quality over time on service infrastructure and service instances, including trend analysis and forecasting;
• Ensuring the operational capability of the SM&O processes
• Maintaining rating and tariff information for service infrastructure and service instances.
. Conducting Vulnerability Management;     
. Conducting Threat Assessments;        
. Conducting Risk Assessments;        
. Conducting Risk Mitigation;             
. Conducting Secure Configuration Activities
This process was renamed in 23.5. old name was Service Readiness & Support
This process was renamed in 24.0  old name was Service Support Readiness

— GB921 v25.5 Excel master, process ID `1.4.4`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.4.4.1** Manage Service Inventory — Establish, manage and administer the enterprise's service inventory, as embodied in the Service Inventory Database, and monitor and report on the usage and access to the service inventory, and the quality of the data maintained in it.
- **1.4.4.2** Enable Service Configuration & Activation — Planning and deployment of service infrastructure, and for ensuring availability of sufficient service infrastructure to support the Service Configuration & Activation processes.
- **1.4.4.3** Support Service Problem Management — Assist Service Problem Management processes by proactively undertaking statistically driven preventative and scheduled service infrastructure maintenance activities and monitoring, managing and reporting on the capability of the Service Problem Management processes.
- **1.4.4.4** Enable Service Quality Management — Support Service Quality Management processes by proactively monitoring and assessing service infrastructure performance, and monitoring, managing and reporting on the capability of the Service Quality Management processes.
- **1.4.4.5** Support Service & Specific Instance Rating — Ensure that rating and tariff information is maintained for each service class, for use by Service & Specific Instance Rating
- **1.4.4.6** Manage Service Test — Manage Service Test process manages the end-to-end execution of a test or test scenario for services not specific to a customer. Tests can be manual or automated.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/production]]
- [[wiki/oda/functional-blocks/intelligence-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Service Process Decompositions PDF (GB921_Service_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

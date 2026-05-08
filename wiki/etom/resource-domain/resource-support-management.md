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
l1_parent: "1.5 Resource Domain"
l2_id: "1.5.4"
l2_name: "Resource Support Management"
---

# Resource Support Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Support Management processes are responsible for managing resource infrastructure to ensure that appropriate application, computing and network resources are available and ready to support the Fulfillment, Assurance and Billing processes in instantiating and managing resource instances, and for monitoring and reporting on the capabilities and costs of the individual FAB processes. 
Responsibilities of these processes include but are not limited to:
• Supporting the operational introduction of new and/or modified resource infrastructure and conducting operations readiness testing and acceptance;
• Managing planned outages;
• Managing and ensuring the ongoing quality of the Resource Inventory;
• Analyzing availability and performance over time on resources or groups of resources, including trend analysis and forecasting;
• Demand balancing in order to maintain resource capacity and performance
• Performing pro-active maintenance and repair activities;
• Establishing and managing the workforce to support the eTOM processes
• Managing spares, repairs, warehousing, transport and distribution of resources and consumable goods.
• Conducting Vulnerability Management;     
• Conducting Threat Assessments;        
• Conducting Risk Assessments;        
• Conducting Risk Mitigation;             
• Conducting Secure Configuration Activities
This process was renamed in 23.5. old name was Resource Readiness & Support
This process was renamed in 24.0. old name was Resource Support Readiness

— GB921 v25.5 Excel master, process ID `1.5.4`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.5.4.1** Enable Resource Provisioning — Planning and deployment of new and/or modified resource infrastructure to ensure availability of sufficient resource infrastructure to support the Resource Provisioning processes, and monitoring, managing and reporting on the capability of the Resource Provisioning processes.
- **1.5.4.2** Enable Resource Performance Management — Proactively monitoring and maintaining resource infrastructure, and monitoring, managing and reporting on the capability of the Resource Performance Management processes.
- **1.5.4.3** Support Resource Trouble Management — Proactively undertaking statistically driven preventative and scheduled resource infrastructure maintenance activities, and repair activities, and monitoring, managing and reporting on the capability of the Resource Trouble Management processes.
- **1.5.4.4** Enable Resource Data Collection & Distribution — Administering and management of the processes which enable the effective operation of the resource data collection and data distribution network, and monitoring, managing and reporting on the capability of the Resource Data Collection & Distribution processes
- **1.5.4.5** Manage Resource Inventory — Establish, manage and administer the enterprise's resource inventory, as embodied in the Resource Inventory Database, and monitor and report on the usage and access to the resource inventory, and the quality of the data maintained in it
- **1.5.4.7** Manage Number Portability — The Manage Number Portability process is responsible for receiving, managing and tracking number portability requests issued by customer orders or a third CSP.
- **1.5.4.8** Manage Field Workforce — "Managing the staff performing manual activities along with managing the actual activity being performed.
- Note: The current focus of the Manage Field Workforce processes is field Staff and others managed through work orders, etc.
- **1.5.4.9** Manage Resource Test — Manage Resource Test Resource processes manage the end-to-end execution of a test or test scenario for resources not specific to a customer's subscribed product(s).

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
  Resource Process Decompositions PDF (GB921_Resource_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

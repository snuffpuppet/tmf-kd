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
l2_id: "1.4.5"
l2_name: "Service Activation Management"
---

# Service Activation Management

> **Vertical context:** Fulfillment ([[wiki/foundations/lifecycle]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

## Overview

Service Activation Management processes encompass allocation, implementation, configuration, activation and testing of specific services to meet customer requirements, or in response to requests from other processes to alleviate specific service capacity shortfalls, availability concerns or failure conditions.  Where included in the service provider offering, these processes extend to cover customer premises equipment.
Responsibilities of the Service Configuration & Activation processes include, but are not limited to:
• Verifying whether specific service designs sought by customers are feasible as part of pre-order feasibility checks;
• Allocating the appropriate specific service parameters to support service orders or requests from other processes;
• Reserving specific service parameters (if required by the business rules) for a given period of time until the initiating customer order is confirmed, or until the reservation period expires (if applicable);
• Implementing, configuring and activating specific services, as appropriate;
• Testing the specific services to ensure the service is working correctly;
• Recovery of specific services;
• Updating of the Service Inventory Database to reflect that the specific service has been allocated, modified or recovered;
• Assigning and tracking service provisioning activities; 
• Managing service provisioning jeopardy conditions
• Reporting progress on service orders to other processes.
This process was renamed in 24.0 Old name was Service Configuration & Activation

— GB921 v25.5 Excel master, process ID `1.4.5`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.4.5.1** Design Solution — Develop an end-end specific service design which complies with a particular customer's requirement
- **1.4.5.2** Allocate Specific Service Parameters to Services — Issue service identifiers for new services.
- **1.4.5.3** Track & Manage Service Provisioning — Ensure service provisioning activities are assigned, managed and tracked efficiently.
- **1.4.5.4** Implement, Configure & Activate Service — Implement, configure and activate the specific services allocated against an issued service order.
- **1.4.5.5** Test Service End-to-End — Test specific services to ensure all components are operating within normal parameters, and that the service is working to agreed performance levels
- **1.4.5.6** Issue Service Orders — Issue correct and complete service orders
- **1.4.5.7** Report Service Provisioning — Monitor the status of service orders, provide notifications of any changes and provide management reports.
- **1.4.5.8** Close Service Order — Close a service order when the service provisioning activities have been completed
- **1.4.5.9** Recover Service — Recover specific services that are no longer required by customers.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Service Process Decompositions PDF (GB921_Service_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

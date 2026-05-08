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
l1_parent: "1.2 Product Domain"
l2_id: "1.2.4"
l2_name: "Product Support Management"
---

# Product Support Management

> **Vertical context:** Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Product Domain ([[wiki/foundations/domains#Product Domain]]).

## Overview

Product Support Management processes ensure the support capability is in place to allow the  Product Fulfillment, Assurance and Billing processes to operate effectively.  
The responsibilities of these processes include, but are not limited to:
• Provision of product Inventory process infrastructure 
• Policy support and decision support knowledge for product
• Monitoring and reporting on the capabilities and costs of the individual Product FAB processes
• Longer-term trend analysis on product FAB processes in order to establish the extent to which enterprise targets for these processes are being achieved and/or the need for the processes to be modified.

This Process was renamed in 24.0 Old name was: Product Readiness Support

— GB921 v25.5 Excel master, process ID `1.2.4`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.2.4.3** Support Product Configuration Management — Support Product Configuration Management ensures that all information, materials, systems and resources are available so that the Product Configuration Management processes can operate effectively.
- **1.2.4.4** Support Product Offering Purchasing — Support Product Offering Purchasing ensures that all information, materials, systems and resources are available so that the Product Offering Purchasing processes can operate effectively.
- **1.2.4.5** Enable Product Performance Management — Enable Product Performance Management ensures that all information, materials, systems and resources are available so that the Product Performance Management processes can operate effectively.
- **1.2.4.6** Support Product Rating & Rate Assignment — Ensure that all information and systems are available so that the Product Rating & Rate Assignment processes can be completed without delay.
- **1.2.4.7** Support Product Usage Mgt — Ensure that all information and systems are available so that the Product Usage Mgt process can be completed without delay.
- **1.2.4.8** Support Product Balance Management — Ensure that all information and systems are available so that the Product Balance Management processes can be completed without delay.
- **1.2.4.9** Manage Product Test — Manage Product Test processes manage the end-to-end execution of a test or test scenario for products not specific to a customer.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/core-commerce-management]]
- [[wiki/oda/functional-blocks/intelligence-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Product Process Decompositions PDF (GB921_Product_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

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
l2_id: "1.5.5"
l2_name: "Resource Order Management"
---

# Resource Order Management

> **Vertical context:** Business Value Development, Fulfillment, Operations Readiness & Support ([[wiki/foundations/lifecycle]]).
> **Domain:** Resource Domain ([[wiki/foundations/domains#Resource Domain]]).

## Overview

Resource Order Management business process directs and controls ordering, scheduling, and allocation of resources (such as materials, equipment, and personnel) within the business. 

Resource Order Management includes managing the capture of resource orders, scheduling works to support the resource order, managing the fulfillment of resource orders, picking/packing, shipping, tracking and closing orders.

— GB921 v25.5 Excel master, process ID `1.5.5`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.5.5.6** Manage Resource Order Capture — Manage Resource Order Capture is responsible for directing and controlling the capture and collection of resource orders from internal and external customers.
- **1.5.5.7** Manage Resource Work Order — Manage Resource Order Work business activity directs and controls all work that are required to fulfill an approved resource order by ensuring the work related to the order is planned, executed and closed in a timely and efficient manner.
- **1.5.5.8** Manage Resource Order Fulfillment — Manage Resource Order Fulfillment business activity directs and controls activities that ensure that resource orders are described, internally satisfied and delivered accordingly.
- **1.5.5.9** Manage Resource Order Picking/Packing — Manage Resource Order Picking/Packing business activity directs and controls the preparation of resources for delivery to the customer.
- **1.5.5.10** Manage Resource Order Shipment — Manage Resource Order Shipment business activity directs and controls the arrangements for delivery of resources.
- **1.5.5.11** Manage Resource Order Returns — Manage Resource Order Returns business activity directs and controls returns of ordered resources.
- **1.5.5.12** Manage Resource Order Tracking — Manage Resource Order Tracking business activity directs and controls the monitoring of resource order status from the time the order is placed to the time is confirmed delivered.
- **1.5.5.13** Manage Resource Order Closure — Manage Resource Order Closure business activity directs and controls the closure of an order and finalizing all supporting business activities.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Resource Process Decompositions PDF (GB921_Resource_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

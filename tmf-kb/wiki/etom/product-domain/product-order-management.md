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
l2_id: "1.2.27"
l2_name: "Product Order Management"
---

# Product Order Management

> **Vertical context:** Fulfillment ([[wiki/foundations/lifecycle]]).
> **Domain:** Product Domain ([[wiki/foundations/domains#Product Domain]]).

## Overview

Product Order Management business direct and control processes that capture, track, fulfil, deliver and close product order requests. 

Product Order Management begins with the capture of a product order request based on a party (Customer, Business Partner, Employee etc.), and processes, tracks and reports the products from order capture to  fulfilment, shipping the order, and managing cancellation and returns.

— GB921 v25.5 Excel master, process ID `1.2.27`, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.2.27.1** Manage Product Order Capture — Manage Product Order Capture business activity direct and control the creation of product orders, validate product orders against feasibility and/or availability checks, and ensure product orders are complete for onward business processing.
- **1.2.27.2** Manage Product Order Fulfillment — Manage Product Order Fulfillment business activity is responsible of directing and controlling for product orders, the configuration of product order fulfilment steps, managing the product order fulfilment profile, managing the product order picking and packing, managing product order shipment, managing product order returns, tracking product order fulfilment, and closing fulfilment of product orders.
- **1.2.27.3** Manage Product Order Delivery — Manage Product Order Delivery business activity directs and controls the activities to validate products in the product order.
- **1.2.27.4** Manage Product Order Cancellation — Manage Product Order Cancellation business activity directs and controls the product order cancellation requests.
- **1.2.27.5** Manage Product Order Management Reports — Manage Product Order Management Reports business activity directs and controls monitoring of product order management activities, notify product order management status and reporting product order management activities.
- **1.2.27.6** Manage Product Order Search — Manage Product Order Search business activity directs and controls product order browsing and discovery.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

See open-questions.md — OQ-008 (ODA layer not yet ingested).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Product Process Decompositions PDF (GB921_Product_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

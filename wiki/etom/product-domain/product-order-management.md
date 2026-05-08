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

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.2.27.1 Manage Product Order Capture

**Extended Description.**

Manage Product Order Capture business activity direct and control the creation of product orders, validate product orders against feasibility and/or availability checks, and ensure product orders are complete for onward business processing.

Manage Product Order Capture assures for completeness, the Product Order requirements needed for successfully processing, delivering and managing returns of orders.

**L4 sub-processes:**

- **1.2.27.1.1** Manage Product Order Selection — Manage Product Order Selection business activity directs and controls the addition and change to product orders.
- **1.2.27.1.2** Approve Product Order — Approve Product Order business activity is responsible for certifying that a product order, based on defined product order management business rules and policies, can be endorsed for further processing.

### 1.2.27.2 Manage Product Order Fulfillment

**Extended Description.**

Manage Product Order Fulfillment business activity is responsible of directing and controlling for product orders, the configuration of product order fulfillment steps, managing the product order fulfillment profile, managing the product order picking and packing, managing product order shipment, managing product order returns, tracking product order fulfillment, and closing fulfillment of product orders.

Manage Product Order Fulfillment support "Product Order Management" by ensuring all associated products, and/or services and/or resources are organized to meet the required promise of the product order.

**L4 sub-processes:**

- **1.2.27.2.1** Configure Product Order fulfilment — Configure Product Order fulfilment business activity is responsible for processing the activities to receive products for a product order , processing product orders, and arranging all supporting requirements of a product order to meet the expectations of the product order.
- **1.2.27.2.2** Manage Product Order Fulfilment Profile — Manage Product Order Fulfilment Profile business activity direct and control product order fulfilment steps that take a product from order to delivery.
- **1.2.27.2.3** Manage Product Order Picking/Packing — Manage Product Order Picking/Packing directs and controls all activities that enable product order picking and product order packing.
- **1.2.27.2.4** Manage Product Order Shipment — Manage Product Order Shipment business activity directs and controls the activities to prepare the product order for shipment using the packing information, generating product order manifest and managing the shipping activities of the products in the product order.
- **1.2.27.2.5** Manage Product Order Returns — Manage Product Order Returns business activity directs and controls activities that process or reject a return of a product order.
- **1.2.27.2.6** Track Product Order Fulfilment — Track Product Order Fulfilment business activity records all the product order fulfilment processing status.
- **1.2.27.2.7** Close Product Order Fulfilment — Close Product Order Fulfilment business activity finalizes a product order fulfillment to be complete.

### 1.2.27.3 Manage Product Order Delivery

**Extended Description.**

Manage Product Order Delivery business activity directs and controls the activities to validate products in the product order.

Manage Product Order Delivery business activity ensures product can be successfully be supplied to consignee of the product order to enable complete the product order process.

**L4 sub-processes:**

- **1.2.27.3.1** Validate Product Order Delivery Requirement — Validate Product Order Delivery Requirement business activity proves validity of the delivery requirements in the product order.
- **1.2.27.3.2** Deliver Product Order — Deliver Product Order business activity is responsible for the actual delivery activity of the product order fulfilled by the business to the consignee. It includes ensuring the product order can be activated/is activated, tracking the product order delivery and notifying product order delivery.
- **1.2.27.3.3** Close Product Order Delivery — Close Product Order Delivery business activity is responsible for ensuring communication and confirmation of product order delivery.

### 1.2.27.4 Manage Product Order Cancellation

**Extended Description.**

Manage Product Order Cancellation business activity directs and controls the product order cancellation requests.

Manage Product Order Cancellation ensures that product order requests are processed in accordance to the organizations business rules and policies. It includes managing request of product order cancellation, processing product order cancellation, and tracking product order cancellation.

**L4 sub-processes:**

- **1.2.27.4.1** Request Product Order Cancellation — Request Product Order Cancellation business activity enables product orders to be dropped or removed from product order processing.
- **1.2.27.4.2** Handle Product Order Cancellation — Manage Product Order Cancellation business activity is responsible for directing and controlling the product order cancellation approval, rejection or completion of the cancellation.
- **1.2.27.4.3** Track Product Order Cancellation — Track Product Order Cancellation business activity is responsible for following up product order cancellation stages and states within the stages.
- **1.2.27.4.5** Close Product Order Cancellation — Close Product Order Cancellation business activity is responsible for ensuring communication and confirmation of product order cancellations.

### 1.2.27.5 Manage Product Order Management Reports

**Extended Description.**

Manage Product Order Management Reports business activity directs and controls monitoring of product order management activities, notify product order management status and reporting product order management activities.

Manage Product Order Management Reports ensures that there is visibility of product order management altogether in order to ensure product order management meet the organization's business requirements.

**L4 sub-processes:**

- **1.2.27.5.1** Monitor Product Order Management Activity — Monitor Product Order Management Activity is responsible for observing and recording every activity in the product order management process.
- **1.2.27.5.2** Notify Product Order Management Status — Notify Product Order Management Status business activity is responsible for sending information about product order management activities.
- **1.2.27.5.3** Report Product Order Management Activity — Report Product Order Management business activity is responsible for formally accounting for product order management.

### 1.2.27.6 Manage Product Order Search

**Extended Description.**

Manage Product Order Search business activity directs and controls product order browsing and discovery.

**L4 sub-processes:**

- **1.2.27.6.1** Browse Product Orders — Browse Product Orders business activity is responsible for making product order available based on general or multiple information.
- **1.2.27.6.2** Find Product Orders — Find Product Orders business activity is responsible for specifically locating and accessing product orders based on specific information.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

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

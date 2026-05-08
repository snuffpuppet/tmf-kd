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

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.5.5.6 Manage Resource Order Capture

**Extended Description.**

Manage Resource Order Capture is responsible for directing and controlling the capture and collection of resource orders from internal and external customers.

The business activity begins with the receipt of an order for resource(s), checks orders for completeness and accuracy, and ensures missing or incorrect information is requested from the customer.

**L4 sub-processes:**

- **1.5.5.6.1** Initiate Resource Order Capture — Initiate Resource Order Capture business activity is responsible for the initial activity of capturing and collecting resource orders from internal and external customers.
- **1.5.5.6.2** Change Resource Order Capture — Change Resource Order Capture business activity manages changes to resource orders that have been previously captured and processed to ensure that any changes to resource orders are approved and modified in a timely and accurate manner, and that the necessary resources are available.
- **1.5.5.6.3** Review Resource Order Capture — Review Resource Order Capture business activity ensures that resource orders captured can be approved for further processing, or rejected in a timely manner to enable any changes to be done.

### 1.5.5.7 Manage Resource Work Order

**Extended Description.**

Manage Resource Order Work business activity directs and controls all work that are required to fulfill an approved resource order by ensuring the work related to the order is planned, executed and closed in a timely and efficient manner.

Manage Resource Order Work business activity includes activities to "Initiate Resource Work Order", "Create Resource Work Order", "Review Resource Work Order", "Plan Resource Work Order", "Close Resource Work Order", "Analyze Resource Work Order" and "Report Resource Work Order".

**L4 sub-processes:**

- **1.5.5.7.1** Initiate Resource Work Order — Initiate Resource Work Order business activity starts a new work order for a specific resource along with all work orders tasks, roles and supporting resources that are need.
- **1.5.5.7.2** Review Resource Work Order — Review Resource Work Order business activity is responsible for ensuring that the work order meets the organization's standards and policies, and that all the necessary information is included.
- **1.5.5.7.3** Plan Resource Work Order — Plan Resource Work Order business activity is responsible for planning and managing the scheduling of appointments for the work order and associated tasks that need to be done to fulfill the resource work order.
- **1.5.5.7.4** Close Resource Work Order — Close Resource Work Order business activity is responsible for closing out the work order when all information on the work order has been documented with an end state.
- **1.5.5.7.5** Analyze Resource Work Order — Analyze Resource Work Order business activity is responsible for examining work orders in a way to improve efficiency and identify any issues or problems that occurred.
- **1.5.5.7.6** Report Resource Work Order — Report Resource Work Order business activity gives an account of resource work order activities.

### 1.5.5.8 Manage Resource Order Fulfillment

**Extended Description.**

Manage Resource Order Fulfillment business activity directs and controls activities that ensure that resource orders are described, internally satisfied and delivered accordingly.

Manage Resource Order Fulfillment business activity will coordinate with various business processes, such as inventory management, purchasing and logistics to ensure that resources are readily available and can be shipped to the customer in a timely manner.

**L4 sub-processes:**

- **1.5.5.8.1** Manage Resource Order Fulfilment Profile — Manage Resource Order Fulfillment Profile business activity directs and controls the fulfillment information (e.g. set of predefined rules and procedures) that dictate how resource orders are processed.
- **1.5.5.8.2** Manage Resource Order Provisioning — Manage Resource Order Provisioning business activity directs and controls the arrangements/composition/organization and setup of underlying resources that enable the organization to fulfill a resource order.
- **1.5.5.8.3** Manage Resource Order Activation — Manage Resource Order Activation business activity directs and controls the validation of the provisioned resources, the completion of all underlying work orders. and communication of the resource order activation status.

### 1.5.5.9 Manage Resource Order Picking/Packing

**Extended Description.**

Manage Resource Order Picking/Packing business activity directs and controls the preparation of resources for delivery to the customer.

Manage Resource Order Picking/Packing business activity will select the resources from inventory, package them accordingly for delivery (based on the shipment method of the resource order), applying the right mark/label/designation.

**L4 sub-processes:**

- **1.5.5.9.1** Apply Resource Order Picking & Packing Rules — Apply Resource Order Picking & Packing Rules business activity matches established guidelines and regulations for picking and packing resource order items.
- **1.5.5.9.2** Pick Resource Order Items — Pick Resource Order Items gathers the appropriate item/s from inventory to fulfill the resource order.
- **1.5.5.9.3** Package Resource Order Items — Package Resource Order Items business activity packs resource order items appropriately and properly.

### 1.5.5.10 Manage Resource Order Shipment

**Extended Description.**

Manage Resource Order Shipment business activity directs and controls the arrangements for delivery of resources.

Manage Resource Order Shipment business activity includes planning, coordinating with logistics, delivery functions to schedule the actual delivery, tracking the delivery and providing the resource order consignee with related information (e.g. tracking number).

**L4 sub-processes:**

- **1.5.5.10.1** Plan Resource Order Shipment — Plan Resource Order Shipment business activity determines the shipping method, carrier and route for the resource order.
- **1.5.5.10.2** Coordinate Resource Order Shipping — Coordinate Resource Order Shipping liaises and communicates with inter-linked processes and resources to ensure timely and correct shipping.
- **1.5.5.10.3** Track Resource Order Shipping — Track Resource Order Shipping business activity monitors the shipment over the shipment lifecycle.
- **1.5.5.10.4** Verify Resource Order Shipping — Verify Resource Order Shipping business activity reviews and validates delivery information.
- **1.5.5.10.5** Closed Resource Order Shipping — Close Resource Order Shipping business activity finalizes shipment with an update to all relevant information.

### 1.5.5.11 Manage Resource Order Returns

**Extended Description.**

Manage Resource Order Returns business activity directs and controls returns of ordered resources.

Manage Resource Order Returns business activity coordinates with requesting parties all returns, inspection of returned resources, processing refunds or replacements.

**L4 sub-processes:**

- **1.5.5.11.1** Create Resource Order Return — Create Resource Order Return business activity initiates the return of a resource order that was previously fulfilled.
- **1.5.5.11.2** Authorize Resource Order Return — Authorize Resource Order Return business activity reviews and approves/rejects a resource order return according to the organizations return policy.
- **1.5.5.11.3** Receive Resource Order Returns — Receive Resource Order Return business activity accepts returns of resource order and associated resource order items and verify they meet the conditions for return acceptance and processing.
- **1.5.5.11.4** Create Reverse Resource Order Return — Create Reverse Resource Order Return business activity handle tasks to act on returned resource order and resource order items.
- **1.5.5.11.5** Monitor Resource Order Returns — Monitor Resource Order Returns business activity tracks and accounts for resource order returns and return items.
- **1.5.5.11.6** Close Resource Order Return — Close Resource Order Return business activity finalizes and updates the resource order return for no further action.

### 1.5.5.12 Manage Resource Order Tracking

**Extended Description.**

Manage Resource Order Tracking business activity directs and controls the monitoring of resource order status from the time the order is placed to the time is confirmed delivered.

Manage Resource Order Tracking business activity tracks the status of the resource order, provides updates to all related parties, and ensures that issues are escalated and managed promptly.

### 1.5.5.13 Manage Resource Order Closure

**Extended Description.**

Manage Resource Order Closure business activity directs and controls the closure of an order and finalizing all supporting business activities.

Manage Resource Order Closure business activity will support order invoicing, order payment processing, and updating the resource order status based on completion status of the order.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

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

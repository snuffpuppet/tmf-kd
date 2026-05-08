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
l2_id: "1.2.18"
l2_name: "Product Balance Management"
---

# Product Balance Management

> **Vertical context:** Billing ([[wiki/foundations/lifecycle]]).
> **Domain:** Product Domain ([[wiki/foundations/domains#Product Domain]]).

## Overview

This process is responsible for holding, calculating, applying policies and managing functionality/interfaces for the Product balances 

Here the values resulting from rating and the application of discounts are applied to a Product balance. The balance affected by the value may be monetary or other balances such as minutes, points, or tokens. Authorizing service requests based on available balance is optional.

— GB921 v25.5 Excel master, process ID `1.2.18`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.2.18.1 Manage Product Balance Containers

**Extended Description.**

This process manages the balance containers assigned to a Product and is used to keep track of usage events, providing input for decision making processes (such as product usage authorization) by means of the balance policies.

The containers include monetary and non-monetary balances (or shared) and are used as prepaid balances (enabling real-time product usage authorization), postpaid balances (in conjunction with an Account-Receivables [AR] application). Examples of non-monetary balances and allowances are: free minutes, WAP-only quota, etc.

### 1.2.18.2 Manage Product Balance Policies

**Extended Description.**

Product Balance policies are rules that describe how balance affecting usages are to be handled. This is done by comparing the value of each usage against criteria such as the following:

- a minimum allowable balance limit (e.g. balance must remain above zero),

- balance expiration dates,

- balance thresholds actions and notifications and

- roll-over & cyclic policies.

### 1.2.18.3 Product Balance Operations Management

**Extended Description.**

Product Balance operations processes the charged events, using balance policies and then guides the results towards the relevant balance containers. Operations include :

- Reserving amounts from any balance for any session, and crediting unused reservations back into the balance, when a session is released.

- Updating balances by applying charges to the balance and credit/debit adjustments.

- Balance queries.

- Transferring amounts from one balance to another.

### 1.2.18.4 Authorize Transaction Based on Product Balance

**Extended Description.**

This process may include Product balance reservation and must be performed online.

Subsequent balance updates are not required to be done in real-time. In this context a usage is provided by the network, e.g. voice call. Product might be a digital content delivered via the network, e.g. content such as music, games, etc.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.2.18.1** Manage Product Balance Containers — Hold and maintain the different Product balances that a customer and/or a subscriber may have.
- **1.2.18.2** Manage Product Balance Policies — Executing policies per balance or balance type.
- **1.2.18.3** Product Balance Operations Management — Allow different operations to be performed on the managed balance.
- **1.2.18.4** Authorize Transaction Based on Product Balance — Manages authorization of product usage requests based on available balances (monetary or non-monetary) and policies.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/core-commerce-management]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Product Process Decompositions PDF (GB921_Product_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

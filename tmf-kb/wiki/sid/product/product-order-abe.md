---
type: sid-abe
spec_id: GB922
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Product_v25.5.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Product_v25.5.md
authority: primary
abe_category: product
entity_name: "Product Order ABE"
---

# Product Order ABE

## Overview

The Product Order ABE contains all entities required to specify a communication used to
procure or update one or many Products and ProductOfferingInstances in the context of
ProductSpecifications and ProductOfferingSpecifications. — GB922 Product §4.5, p. 200

A ProductOrder represents a request used to procure, update or remove one or many
Products and ProductOfferingInstances in the context of ProductSpecifications and
ProductOfferingSpecifications through all its ProductOfferingOrderItems and
ProductOrderItems. — GB922 Product §4.5, p. 200

> Some but not all enterprises consider an Order to be a type of an Agreement. From a
> SID model perspective, an Order can be formalized by an Agreement and the
> Agreements relationship between the Agreement and the ProductOrder. This philosophy
> has the advantage of clearly separating two different concepts: the order from the
> legal formalisms associated with the order. — GB922 Product §4.5, p. 200

## Business Entities

### ProductOrder

Sub-class of `RootEntity` and therefore inherits from all its attributes and
relationships. — GB922 Product §4.5, p. 200

### ProductOfferingOrderItem

Order item at the offering level. May depend on other ProductOfferingOrderItems via
`ProductOfferingOrderItemRelationship`. — GB922 Product §4.5, p. 200

### ProductOrderItem

Order item at the product level. May depend on other ProductOrderItems via
`ProductOrderItemRelationship`. — GB922 Product §4.5, p. 201

### CustomerProductOrder

Sub-class of ProductOrder used to procure, update or remove ProductOfferingInstances
for Customers — corresponds to ProductOfferingInstances ordered by a Customer from the
Service Provider. — GB922 Product §4.5, pp. 200–201

### BusinessPartnerProductOrder

Sub-class of ProductOrder used to procure, update or remove ProductOfferingInstances
for the Service Provider — corresponds to ProductOfferingInstances ordered by the
Service Provider from a Business Partner. — GB922 Product §4.5, pp. 200–201

### ProductOrderItemRelationship / ProductOfferingOrderItemRelationship

Express dependencies between order items at each level.
— GB922 Product §4.5, p. 200

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- At least one CommunicationInteraction is the source of a ProductOrder
  (Customer/Common Domain entities, not yet ingested).
- A ProductOrder may refer to an Agreement specifying all what has been approved by the
  PartyRoles ([[wiki/sid/product/product-party-roles-abe]]) involved in the
  ProductOrder.
- ProductOrder, ProductOfferingOrderItems and ProductOrderItems may be further
  described by Attachments (Common Domain, not yet ingested).
- Each ProductOrderItem references Products and ProductOfferingInstances
  ([[wiki/sid/product/product-and-offering-instance-abe]]) within
  ProductSpecifications ([[wiki/sid/product/product-specification-abe]]) and
  ProductOfferingSpecifications ([[wiki/sid/product/product-offering-specification-abe]]).
— GB922 Product §4.5, pp. 200–206

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest

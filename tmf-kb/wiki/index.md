# TMF Knowledge Base — Index

Top-level catalog of the TMF wiki. Updated after every ingest. For governance see
[[CLAUDE]]. For ambiguities see [[wiki/open-questions]]. For event history see [[wiki/log]].

The corpus represents the **PSR (Product, Service, Resource)** modelling principle at three
architectural layers: process (eTOM), data (SID), and component (ODA), with foundational
cross-framework concepts above.

## Foundations
- [[wiki/foundations/_index|Browse foundations]]
- [[wiki/foundations/domains]] — 11 horizontal domains (Market, Sales, Product, Customer,
  Service, Resource, Business Partner, Enterprise, Shared, Patterns, Integration)
- [[wiki/foundations/lifecycle]] — vertical context (Strategy-to-Readiness vs Operations
  Lifecycle Areas; 7 Lifecycle Stages)
- [[wiki/foundations/business-process-framework]] — Business Process Framework (eTOM)
  conceptual definition; Core/Enabling/Supporting Process classification
- [[wiki/foundations/information-framework]] — Information Framework (SID) conceptual
  definition; ABE, Business Entity, Attribute, Relationship
- [[wiki/foundations/functional-framework]] — Functional Framework conceptual definition
- [[wiki/foundations/principles]] — Shared, BPF, Information Framework, and Functional
  Framework principles (23 in total)

## eTOM Service Domain
- [[wiki/etom/service-domain/_index|Browse Service Domain L2s]]
- 8 L2s in scope (OFAB verticals from GB921 v25.5):
  Service Support Management (1.4.4), Service Activation Management (1.4.5), Service
  Problem Management (1.4.6), Service Performance Management (1.4.7), Service
  Guiding & Mediation (1.4.8), Service Catalog Operational Readiness Management
  (1.4.14), Service Catalog Content Management (1.4.15), Service Anomaly Management
  (1.4.18)

## eTOM Resource Domain
- [[wiki/etom/resource-domain/_index|Browse Resource Domain L2s]]
- 9 L2s in scope (OFAB verticals from GB921 v25.5):
  Resource Support Management (1.5.4), Resource Order Management (1.5.5), Resource
  Data Management (1.5.7), Resource Trouble Management (1.5.8), Resource Performance
  Management (1.5.9), Resource Mediation & Reporting (1.5.10), Resource Catalog
  Operational Readiness Management (1.5.16), Resource Catalog Content Management
  (1.5.17), Resource Anomaly Management (1.5.21)

## eTOM Product Domain (operational)
- [[wiki/etom/product-domain/_index|Browse Product Domain L2s]]
- 12 L2s in scope (OFAB verticals from GB921 v25.5):
  Product Support Management (1.2.4), Product Configuration Management (1.2.5),
  Product Performance Management (1.2.6), Product Inventory Management (1.2.11),
  Product Usage Management (1.2.16), Product Rating & Rate Assignment (1.2.17),
  Product Balance Management (1.2.18), Product Catalog Operational Readiness
  Management (1.2.21), Product Catalog Content Management (1.2.22), Product Anomaly
  Management (1.2.25), Product Problem Management (1.2.26), Product Order Management
  (1.2.27)

## SID — Product
- [[wiki/sid/product-abe|Browse Product ABE category]]
- 12 ABEs (§4.1–§4.12 of GB922 Product v25.5):
  Product Party Roles, Product Specification, Product Offering Specification, Product
  and Offering Instance, Product Order, Product Usage, Loyalty, Product Configuration,
  Product Test, Product Capacity, plus two «notFullyDeveloped» (Product Performance,
  Strategic Product Portfolio Plan)

## SID — Service
- [[wiki/sid/service-abe|Browse Service category]]
- 12 ABEs (§4.2–§4.13 of GB922 Service v25.0):
  Service Party Roles, Service Specification (CFSSpec/RFSSpec), Service (CFS/RFS),
  Service Configuration, Service Order, Service Usage, Service Test, Service
  Performance (SLS/SLA), Service Capacity, plus three flagged ABEs:
  Service Problem («NotFullyDeveloped»), Service Strategy & Plan
  («notFullyDeveloped»), TIP Service Management («likelyToBeDepreciated»)
- The CFS/RFS distinction in §4.4 is directly relevant to the corpus's PSR
  production/commercial mapping goal

## SID — Resource
- [[wiki/sid/resource-abe|Browse Resource category]]
- 13 ABEs (§4.1–§4.13 of GB922 Resource v25.5 — **pre-production source**):
  Resource Party Roles, Resource Specification (Logical/Physical/Compound), Resource
  (LR/PR/CR), Resource Configuration, Resource Order, Resource Usage, Resource Test,
  Resource Performance, Stock Item, Resource Capacity, plus three «notFullyDeveloped»
  (Resource Trouble, Resource Topology, Resource Strategy & Plan)
- All pages carry `release_status: pre-production` per OQ-027.

## SID — Common Business Entities
- [[wiki/sid/common-abe|Browse Common category]]
- 19 ABEs (§4.4–§4.22 of GB922 Common v23.0):
  Party, Party Privacy, Party Payment, Communication Interaction (Shared sub-domain),
  Digital Identity, Calendar, Location, Base Types, Root Business Entities, Account,
  Business Interaction, Agreement, Capacity (canonical), Catalog (canonical),
  Configuration and Profiling (canonical), Metric, Performance, Policy, Project

## ODA
_(none yet)_

## Views
_(none yet)_

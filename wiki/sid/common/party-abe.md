---
type: sid-abe
spec_id: GB922
spec_version: "23.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/sid/GB922_Common_v23.0.pdf
source_extract_paths:
  - raw/extracted/tmf/sid/GB922_Common_v23.0.md
authority: primary
abe_category: common
entity_name: "Party ABE"
---

# Party ABE

> **Sub-domain note.** GB922 Common spans Common, Pattern, and Shared sub-domains
> (per [[wiki/foundations/domains#Shared Domain]] and §4.1–§4.3 of the source).
> Party ABE sits in the Common Business Entities portion. See
> [[wiki/open-questions#OQ-014]].

## Overview

A Party represents an individual, an organization, or an organization unit that are of
interest, involved or that provide value directly or indirectly from an enterprise
perspective (Enterprise is to be understood here as provider, service provider or
operator). — GB922 Common §4.4, p. 54

Hence the Party plays one or more roles with the enterprise or with another Party
playing a role with the enterprise (indirectly). This is introduced to specify that the
only party an enterprise would be interested in and will consider in its systems is a
party playing a role (directly or indirectly). Roles would be represented by the
PartyRole concept. — GB922 Common §4.4, p. 54

This Party ABE defines information about companies and people. Implementations of this
model are responsible for ensuring that the relevant privacy legislation standards are
adhered to in the countries that will use the implementation. — GB922 Common §4.4, p. 54

## Business Entities

§4.4 contains a substantial collection of entities and nested sub-ABEs. Top-level core
entities include:

- **Party** — the abstract base for individuals and organizations
- **Individual** — a human party
- **Organization** — an organizational party
- **PartyRole** — the role a Party plays in interactions; specialised across all
  business domains (MarketSales Roles, Customer Roles, Product Roles, Service Roles,
  Resource Roles, Business Partner Roles, Enterprise Roles)
- **PartyRoleSpecification** — the EntitySpec side of PartyRole
- **PartyRoleGroup** — groupings of related party roles
- **Permission** / **PermissionSpec** — rights granted via PartyRoles

Nested sub-ABEs (each with its own related-entities figure) include:

- Contact Medium ABE (§4.4.44, Figure CMd.01)
- Currency ABE (§4.4.45, Figure Cur.01)
- Identification ABE (§4.4.46, Figure Id.01)
- Party Community ABE (§4.4.47, Figure PyC.01)
- Party Demographic ABE (§4.4.48, Figure PD.01)
- Party Organization ABE (§4.4.49, Figure PO.01)
- Party Profile ABE (§4.4.50, Figure PyP.01)
- Party Role Examples ABE (§4.4.51, Figure PRE.01)
- Party Role Group ABE (§4.4.52, Figure PRG.01)
- Permission ABE (§4.4.53, Figure Perm.01)
- Skill ABE (§4.4.54, Figure Sk.01)

For full BE listings, attribute tables, and figures (P.00–P.20 plus 30+ illustrations),
see source GB922 Common v23.0 §4.4, pp. 54–142.

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- PartyRole specialises across every business domain. Domain-specific PartyRoles are
  defined in their own SID documents (e.g. ProductManager in
  [[wiki/sid/product/product-party-roles-abe]]).
- Party Profile, Demographics, Skills, Privacy (separate ABE — see
  [[wiki/sid/common/party-privacy-abe]]) extend Party.
- Permission entities establish rights granted via PartyRoles.
- Contact Medium connects Parties for inbound/outbound communication
  (used by [[wiki/sid/common/communication-interaction-abe]]).
— GB922 Common §4.4, pp. 54–142

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/party-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-014: GB922 Common spans Common/Pattern/Shared sub-domains; v1 wiki uses single
  `abe_category: common` — schema may need split

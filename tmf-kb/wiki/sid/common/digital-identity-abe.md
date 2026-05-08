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
entity_name: "Digital Identity ABE"
---

# Digital Identity ABE

## Overview

A Digital Identity ABE contains all Business Entities used for enabling
identification / authentification of Party or Resource in order to allow Party or
Resource to use their permission carried by their roles. — GB922 Common §4.8, p. 188

A DigitalIdentity enables identification / authentification of Party or Resource in
order to allow Party or Resource to use their permission. The DigitalIdentity needs an
ID, a status and a valid period during which the DigitalIdentity can be used.
— GB922 Common §4.8, p. 188

## Business Entities

### DigitalIdentity (abstract)

Base entity for identification/authentication. Has `ID`, `status`, and a valid period.
— GB922 Common §4.8, p. 188

### PartyDigitalIdentity

Enables identification/authentication of a unique Party or many PartyRoles. May
identify a Party for a subset of the PartyRoles he plays — e.g. one
PartyDigitalIdentity for professional roles delegated by an employer, another for
personal PartyRoles. — GB922 Common §4.8, p. 188

### ResourceDigitalIdentity

Enables identification/authentication of a unique Resource. Used for controlling
Machine-to-Machine activities. — GB922 Common §4.8, p. 188

### Credential

At least one Credential is needed for a DigitalIdentity. Enables
identification/authentification. One or many ContactMediums might be defined for each
Credential to be used for reset. — GB922 Common §4.8, p. 188

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source.

## Relationships

- PartyDigitalIdentity relates to Parties and PartyRoles
  ([[wiki/sid/common/party-abe]]).
- ResourceDigitalIdentity relates to Resources (Resource Domain, not yet ingested).
- Permissions carried via PartyRole/ResourceRole (Permission ABE within
  [[wiki/sid/common/party-abe]]).
- Credentials may use ContactMedium for reset (Contact Medium sub-ABE in Party ABE).
— GB922 Common §4.8, pp. 188–194

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-015: GB922 Common §4.8 source spelling "authentification" (vs "authentication")
  preserved verbatim

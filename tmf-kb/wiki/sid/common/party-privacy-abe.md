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
entity_name: "Party Privacy ABE"
---

# Party Privacy ABE

## Overview

The Party Privacy Profile ABE contains all entities used by the Party Privacy
Management process for specifying:

- the information concerned by Privacy rules,
- the Privacy rules themselves,
- and the choices made by Parties for their own Privacy.

— GB922 Common §4.5, p. 143

The Party Privacy Management process manages privacy information and agreement with
party. Therefore, it needs to specify the information concerned by Privacy rules and
the Privacy rules themselves.

Each SID Entity corresponds to an instance of RootEntityType and each attribute of an
Entity corresponds to the use (RootEntityTypeCharUse) of a CharacteristicSpecification.
— GB922 Common §4.5, pp. 143–145

## Business Entities

Nested sub-ABEs:

- **Party Privacy Profile ABE** (§4.5.14, Figure PPP.01) — the profile carrying privacy
  choices for a Party
- **Party Privacy Profile Type ABE** (§4.5.15, Figure PPPT.01) — the EntitySpec side

Key entities (full list and figures Ppr.01–Ppr.05 in source):

- **PartyPrivacyProfile**
- **PartyPrivacyProfileType**
- **PrivacyAgreement**
- Use of `RootEntityType`, `RootEntityTypeCharUse`,
  `RootEntityTypeCharValueUse` from [[wiki/sid/common/root-business-entities-abe]] to
  reference SID-wide privacy targets

## Key Attributes

Detailed attribute tables not extracted in v1 ingest; consult source GB922 Common
§4.5, pp. 143–165.

## Relationships

- Party Privacy Profile attaches to a Party ([[wiki/sid/common/party-abe]]).
- Privacy targets are described via the RootEntityType pattern from
  [[wiki/sid/common/root-business-entities-abe]].
- PrivacyAgreement is a specialisation of Agreement
  ([[wiki/sid/common/agreement-abe]]).
— GB922 Common §4.5, pp. 143–165

## ODA Components That Own This Entity

- [[wiki/oda/functional-blocks/party-management]]

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM and ODA layers not yet ingested.

## Open Questions

- OQ-008: Trilateral linking pending eTOM and ODA layer ingestion
- OQ-009: BE-level attribute detail deferred to future ingest
- OQ-014: Common/Pattern/Shared sub-domain schema split deferred

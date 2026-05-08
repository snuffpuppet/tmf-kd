---
type: oda-component
spec_id: GB1022
spec_version: "1.1.0"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.pdf
source_extract_paths:
  - raw/extracted/tmf/oda/GB1022_ODA_Functional_Architecture_Guidebook_v1.1.0.md
authority: primary
oda_domain: "Functional Blocks"
component_id: "GB1022 §4.1"
component_name: "Decoupling & Integration"
psr_layer: "cross-cutting"
---

# Decoupling & Integration

> **Architectural role.** Per GB1022 §3 Systems of Separation: Decoupling &
> Integration is the transversal/integration layer that borders all adjacent
> functional blocks. It does not sit within Engagement, Systems of Records, or
> Systems of Insight — it sits *between* them.
>
> **Non-business block.** D&I gathers non-business functions; it has no business
> process (eTOM) or operational data (SID) mappings of its own. Trilateral sections
> below note this structural exemption.

## Overview

The Decoupling & Integration (D&I) Block is about governing and managing separation
of functional borders based on well-established "families" of closely interrelated
services as well as the integration between them. D&I gathers non-business functions
that are needed at design and runtime to enable the combinations of services that
the business requires.

The Decoupling & Integration Block ensures that services provided by ODA can be
combined in a flexible way, without restriction imposed by a process pattern derived
from a given stack of blocks. — GB1022 §4.1.1, p. 15

> Where in traditional architectures functional layers are supposed to communicate
> only with adjacent ones (e.g., BSS with OSS, OSS with Network but not BSS directly
> with Network). "Decoupling" within ODA emphasizes that ODA Function Blocks are
> not behaving like layers and tightly coupled together. This ensures that the
> functional architecture by itself doesn't preclude any combination of services.
> — GB1022 §4.1.1, p. 15

## Responsibilities

Core functionalities (verbatim from GB1022 §4.1.2 Table 4-1):

- **DI.001 Normalized APIs** — Catalog of APIs; Management of API catalog and
  documentations, including links to catalogs of partners
- **DI.002 Message Routing** — API Routing; Route API calls to endpoint, API Mediation

Additional functionalities are listed in source Table 4-1.

## SID Entities Owned

The Decoupling & Integration Block is a non-business block per GB1022 §4.1.1 — it
holds no operational data (SID) of its own. See [[wiki/open-questions#OQ-038]] for
the structural exemption.

## eTOM Processes Realised

The Decoupling & Integration Block is a non-business block per GB1022 §4.1.1 — it
holds no business processes (eTOM) of its own. See [[wiki/open-questions#OQ-038]].

## Component Dependencies

D&I borders all other ODA Functional Blocks as the integration layer:

- [[wiki/oda/functional-blocks/engagement-management]]
- [[wiki/oda/functional-blocks/party-management]]
- [[wiki/oda/functional-blocks/core-commerce-management]]
- [[wiki/oda/functional-blocks/production]]
- [[wiki/oda/functional-blocks/intelligence-management]]

## Open Questions

- OQ-008: ODA↔eTOM↔SID trilateral linking sweep deferred
- OQ-038: Non-business ODA block (D&I, Engagement Management) trilateral exemption
- OQ-037: GB1022 mapping tables reference GB921/GB922 R20.5; corpus uses v25.x

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

The Decoupling & Integration Block holds no operational data per GB1022 §4.1.1
(non-business functions). The trilateral sweep performed 2026-05-08T21:30Z
confirmed: GB1022 §4.1 contains no SID ABE mapping table for this block (unlike
§4.3.3 / §4.4.3 / §4.5.2 / §4.6.2 which carry Tables 4-4 / 4-7 / 4-10 / 4-13 for
the business blocks). §4.1.2 Table 4-1 lists only integration functionalities
(Normalized APIs, Message Routing). Source-supported absence, not a gap. See
[[wiki/open-questions#OQ-038]].

## eTOM Processes Realised

The Decoupling & Integration Block holds no business processes per GB1022 §4.1.1
(non-business functions). The trilateral sweep performed 2026-05-08T21:30Z
confirmed: GB1022 §4.1 contains no eTOM L2 mapping table for this block (unlike
§4.3.2 / §4.4.2 / §4.5 / §4.6.1 which carry Tables 4-3 / 4-6 / 4-9 / 4-12 for
the business blocks). Source-supported absence, not a gap. See
[[wiki/open-questions#OQ-038]].

## Component Dependencies

D&I borders all other ODA Functional Blocks as the integration layer:

- [[wiki/oda/functional-blocks/engagement-management]]
- [[wiki/oda/functional-blocks/party-management]]
- [[wiki/oda/functional-blocks/core-commerce-management]]
- [[wiki/oda/functional-blocks/production]]
- [[wiki/oda/functional-blocks/intelligence-management]]

## Open Questions

- OQ-038: Non-business ODA block trilateral exemption — source-supported absence
  of eTOM/SID mappings for Decoupling & Integration (§4.1.1)

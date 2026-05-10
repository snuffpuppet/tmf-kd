# S2R-Vertical Scope Expansion — Planning Document

**Status:** Scoping in progress (Phase 3 of capability map work).
**Initiated:** 2026-05-10 per user direction *"promote it then scope the S2R work."*
**Trigger:** User Phase 1 review question — *"Why is there no 'strategy' and 'capability' verticals?"*
**Source-grounded answer:** They're excluded today by CLAUDE.md §3 ("Strategy / Infrastructure / Product Lifecycle Management (SIP) vertical — strategic, not operational"). v25.5 calls this the **Strategy-to-Readiness (S2R)** Lifecycle Area per GB991 §1.1.2.

This document scopes what it would take to expand the corpus and the capability map to include S2R-area verticals. **Scoping only — no ingest happens until the user reviews and approves.**

---

## 1. Goal

Add the **Strategy Management** and **Capability Management** verticals (and optionally **Business Value Development** — see Decision 1 below) to the Service and Resource Domain coverage in the corpus and capability map, enabling heat-map / roadmap analysis of strategic-planning and capability-delivery maturity alongside the current operational-only view.

The user's stated goal remains operational OSS-mapping, but Phase 1 surfaced practitioner curiosity about strategic / capability layers — this scope expansion serves stakeholders who need a fuller process-maturity view (e.g. roadmap planning, capability-investment decisions) rather than just the operational gap analysis.

---

## 2. L2 inventory — source-grounded

Direct read from `raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx` (2026-05-10 survey). Service Domain (1.4.x) and Resource Domain (1.5.x) only.

### Strategy Management vertical — 2 L2s

| ID | Name | Domain |
|---|---|---|
| 1.4.1 | Service Strategy Management | Service |
| 1.5.1 | Resource Strategy Management | Resource |

### Capability Management vertical — 8 L2s

| ID | Name | Domain |
|---|---|---|
| 1.4.2 | Service Capability Delivery | Service |
| 1.4.12 | Service Capacity Management | Service |
| 1.4.16 | Service Catalog Planning Management | Service |
| 1.4.19 | Service Specification Management | Service |
| 1.5.2 | Resource Capability Delivery | Resource |
| 1.5.14 | Resource Capacity Management | Resource |
| 1.5.18 | Resource Catalog Planning Management | Resource |
| 1.5.19 | Resource Specification Management | Resource |

### Business Value Development vertical — 6 unique L2s

GB991 §1.1.2 groups Business Value Development under the same S2R Lifecycle Area as Strategy and Capability Management. Decision 1 below: include or defer.

| ID | Name | Domain |
|---|---|---|
| 1.4.3 | Service Specification Lifecycle Management | Service |
| 1.4.13 | Service Catalog Lifecycle Management | Service |
| 1.4.17 | Service Anomaly Lifecycle Management | Service |
| 1.5.3 | Resource Specification Lifecycle Management | Resource |
| 1.5.15 | Resource Catalog Lifecycle Management | Resource |
| 1.5.20 | Resource Anomaly Lifecycle Management | Resource |

(Note: 1.5.5 Resource Order is also flagged BVD by GB921 v25.5 alongside Fulfillment + ORS — already in corpus scope.)

### Totals

| Scope option | Verticals | New L2 pages |
|---|---|---|
| Minimal (Strategy + Capability) | 2 | 10 |
| Full S2R (Strategy + Capability + BVD) | 3 | 16 |

---

## 3. SID ABE situation — already largely in corpus

Survey (2026-05-10) of existing `wiki/sid/{service,resource,product,common}/` ABE pages against keywords *Strategy*, *Capability*, *Specification*, *Capacity*, *Plan*:

| ABE | Status | Path |
|---|---|---|
| Service Strategy and Plan | **Already ingested** | `wiki/sid/service/service-strategy-and-plan-abe.md` |
| Resource Strategy and Plan | **Already ingested** | `wiki/sid/resource/resource-strategy-and-plan-abe.md` |
| Service Specification | **Already ingested** | `wiki/sid/service/service-specification-abe.md` |
| Resource Specification | **Already ingested** | `wiki/sid/resource/resource-specification-abe.md` |
| Product Specification | **Already ingested** | `wiki/sid/product/product-specification-abe.md` |
| Product Offering Specification | **Already ingested** | `wiki/sid/product/product-offering-specification-abe.md` |
| Service Capacity | **Already ingested** | `wiki/sid/service/service-capacity-abe.md` |
| Resource Capacity | **Already ingested** | `wiki/sid/resource/resource-capacity-abe.md` |
| Product Capacity | **Already ingested** | `wiki/sid/product/product-capacity-abe.md` |
| Common Capacity | **Already ingested** | `wiki/sid/common/capacity-abe.md` |
| Strategic Product Portfolio Plan | **Already ingested** | `wiki/sid/common/strategic-product-portfolio-plan-abe.md` |

**Reason:** SID coverage in CLAUDE.md §3 is by ABE category (Product / Service / Resource / Common), not by vertical alignment. The Strategy/Capability ABEs were ingested at v1 because they're Service/Resource Domain ABEs.

**Likely missing:** Capability-specific ABEs (e.g. *Service Capability Plan*, *Resource Capability Plan* — these may exist in GB922 v25.5 but may not have been called out in the v1 ingest). Verification needed; estimated 0–4 new ABE pages.

**Net SID ingest burden: low** — most of the data-layer support already exists.

---

## 4. CLAUDE.md amendments needed

### §3 — In Scope / Out of Scope

Current text (eTOM section):
> Out of scope:
> - The **Strategy / Infrastructure / Product Lifecycle Management (SIP) vertical** — this is strategic, not operational. The goal is mapping operational processes.

Proposed amendment options:

**Option A — Scoped expansion (recommended for Strategy + Capability):**
> In scope (Phase 3 expansion 2026-05-10):
> - **Strategy Management** lifecycle stage of S2R: provides strategic planning view aligned with operational mapping.
> - **Capability Management** lifecycle stage of S2R: bridges strategic planning to operational readiness via capability delivery, capacity management, and specification management.
>
> Out of scope (still excluded):
> - **Business Value Development** lifecycle stage of S2R — lifecycle/version-management of catalog and specification artifacts; defer pending stakeholder need.

**Option B — Full S2R inclusion (if BVD included):**
> In scope (Phase 3 expansion 2026-05-10):
> - **Strategy-to-Readiness (S2R) Lifecycle Area** — Strategy Management, Capability Management, and Business Value Development lifecycle stages.
>
> Out of scope: _(no remaining S2R-area exclusions for Service and Resource Domains.)_

### §3 — Vertical naming nomenclature

Current text references "OFAB verticals." After expansion this becomes ambiguous (OFAB is Operations area; new verticals are S2R area). Add a clarifying note:
> **OFAB** = Operations Readiness & Support, Fulfillment, Assurance, Billing — the four lifecycle stages of the **Operations** area (per GB991 §1.1.2). The Phase 3 expansion adds lifecycle stages from the **Strategy-to-Readiness (S2R)** area. "Vertical" is the GB991 term for a lifecycle stage; "Lifecycle Area" is the higher-level grouping (S2R or Operations).

### §1.1.2 reference

Update §3 to reference the GB991 §1.1.2 lifecycle structure (already documented in `wiki/foundations/lifecycle.md`) so the scope decision is anchored in the source's own framework.

---

## 5. Capability map integration — structural choices

### Decision 2 — How to organize the capability map after expansion

The current capability map structure:
```
## Service Domain — L2 Capabilities (in scope)
### Operations Readiness & Support
### Fulfillment
### Assurance
### Billing

## Resource Domain — L2 Capabilities (in scope)
### Operations Readiness & Support
### Fulfillment
### Assurance
### Billing
```

Three options for the expanded structure:

**Option 2A — Flat verticals (preserve current pattern):**
Add new H3 sections under each L1 Domain. Service Domain gets 6–7 H3s (Strategy Management, Capability Management, optional BVD, ORS, Fulfillment, Assurance, Billing). Resource same.
- Pros: minimal restructure; consistent with current organization.
- Cons: visual clutter; no Lifecycle-Area distinction; reader doesn't see the S2R/Operations split that GB991 establishes.

**Option 2B — Lifecycle-Area subgrouping (recommended):**
Introduce H2-level Lifecycle-Area split or H3 lifecycle headers.
```
## Service Domain — L2 Capabilities (in scope)

### Strategy-to-Readiness Lifecycle Area
#### Strategy Management
[L2s as H4 capabilities]
#### Capability Management
[...]
#### Business Value Development (if Decision 1 = include)
[...]

### Operations Lifecycle Area
#### Operations Readiness & Support
[...]
#### Fulfillment
[...]
#### Assurance
[...]
#### Billing
[...]
```
But this pushes capabilities to **H5**, sub-capabilities (security, workforce, inventory, test) to **H6**. Obsidian outline gets deep; may break heat-map readability.

**Option 2C — Two view pages (capability map split):**
Keep `capability-map.md` as Operations-only (current state). Create new `capability-map-s2r.md` for the Strategy + Capability + (BVD) verticals. Cross-link both. Heat map can be built on each independently or combined externally.
- Pros: keeps current capability map clean for the operational-OSS use case; isolates the new content; simpler structure per page.
- Cons: practitioner has two pages to navigate; cross-PSR comparisons within Capability Management require cross-page reading; Mermaid diagram doesn't show full picture in one place.

### Decision 3 — Mermaid diagram strategy

Current diagram: 3 top-level subgraphs (Out of scope greyed; Service Domain in scope; Resource Domain in scope), each containing OFAB-vertical sub-subgraphs.

For Option 2A or 2B: subgraphs grow significantly. With 16 added L2s + the 17 existing, Mermaid `flowchart TB` may render unmanageably wide or tall. Consider:
- **3a:** Add new subgraphs but accept visual size growth.
- **3b:** Two diagrams (Operations + S2R), one per Lifecycle Area.
- **3c:** Replace flowchart with a more compact representation (e.g. Mermaid `gantt`-style swim lanes, or table-based).

---

## 6. Capability sub-capability (H5) review

The L3-derived sub-capability convention (settled at capability-map Phase 2) requires fresh L3 review for the new L2s. Likely candidates worth surveying:

- **Capability Delivery (1.4.2 / 1.5.2)** L3s — may carry sub-processes worth heat-map separation (e.g. capability planning vs capability deployment).
- **Capacity Management (1.4.12 / 1.5.14)** L3s — capacity planning is a distinct practitioner concern.
- **Specification Management (1.4.19 / 1.5.19)** L3s — specification design vs specification publishing may merit separate cells.

Effort: similar to Phase 2 — survey all L3s in the new L2s, apply the L3-derived sub-capability criteria (named L3, substantive scope, recognised practitioner concern, cross-PSR symmetry).

---

## 7. Trilateral linking — ODA Functional Block ownership

The existing capability map deliberately omits trilateral inline (framing decision #5). But the new L2 ingest still needs trilateral linking on each L2 page (eTOM-l2 type carries required `## SID Entities Manipulated` and `## ODA Components That Realise This Process` sections).

Likely ODA-block ownership for the new L2s (verification needed against GB1022):
- **Engagement Management** — likely owns Strategy Management L2s (engagement is upstream of strategy).
- **Core Commerce Management** — possibly owns some Capability Management L2s related to product/service portfolio.
- **Production** — possibly owns Capability Delivery / Capacity Management given operational-readiness adjacency.
- **Intelligence Management** — possibly owns Strategy Management's analytics / forecasting functions.

OQ-038 / OQ-040 / OQ-042 / OQ-043 / OQ-044 cross-walk decisions from the v1 trilateral sweep apply: GB1022 may reference R20.5 IDs that need translation to v25.5. Expect 5–10 new OQs filed during ingest.

---

## 8. Effort estimate

Broken down by sub-task. Conservative estimates assuming careful verbatim source extraction and bidirectional trilateral linking.

| Sub-task | Strategy + Capability (10 L2s) | Full S2R (16 L2s) |
|---|---|---|
| **CLAUDE.md amendment** | 1–2 hr | 1–2 hr |
| **L2 page ingest** (verbatim source extraction, full anatomy) | 6–8 hr | 9–12 hr |
| **L3 detail / Extended Description deepening** (per TODO #2 pattern) | 3–4 hr | 5–6 hr |
| **SID ABE verification + any missing ingest** | 1–3 hr | 1–3 hr |
| **Trilateral sweep** (forward links from new L2s + reciprocal ODA back-links) | 2–4 hr | 3–6 hr |
| **Capability map integration** (10–16 new H4 entries, structural decisions, Mermaid update) | 2–3 hr | 3–5 hr |
| **L3-derived sub-capability review** (Phase 2 pattern) | 1–2 hr | 2–3 hr |
| **Lint cleanup throughout** | 1 hr | 1–2 hr |
| **Total** | **17–27 hr** | **25–39 hr** |

For comparison: capability-map Phases 1–2 (Batches 1–6 + L3 review) took ~6 conversation iterations of ~2–3 hours each = ~12–18 hours of iterative collaboration.

---

## 9. Phasing options

### Option P1 — Pilot first (recommended)

Start with the 2 Strategy Management L2s (1.4.1 + 1.5.1) only:
- Smallest scope to validate the workflow.
- Surfaces L1 frame and Mermaid restructure decisions early.
- Produces a small but complete artifact for stakeholder review.
- ~6–8 hours of work.
- If pilot lands cleanly, expand to Capability Management (8 L2s); then optionally BVD.

### Option P2 — Full Strategy + Capability in one pass

10 L2s, 17–27 hours. Produces a complete S2R-pair view (excluding BVD). Recommended if the user has stakeholder pressure for the full picture.

### Option P3 — Full S2R in one pass (Strategy + Capability + BVD)

16 L2s, 25–39 hours. Most comprehensive. Recommended if BVD is genuinely needed for stakeholder use cases.

---

## 10. Decisions needed from user

1. **Include Business Value Development (BVD) vertical?**
   - Yes → 16 L2s, full S2R coverage.
   - No → 10 L2s, Strategy + Capability only.
   - Defer (scope BVD as Phase 4 later) → 10 L2s now, BVD a future TODO.

2. **Capability map structural choice (see §5):**
   - 2A flat verticals (simple, may be cluttered).
   - 2B Lifecycle-Area subgrouping (clean structure, deeper heading levels — capabilities at H5).
   - 2C two view pages (clean separation, two artifacts to navigate).

3. **Mermaid diagram strategy (see §5):**
   - 3a single growing diagram.
   - 3b two diagrams per Lifecycle Area.
   - 3c restructure to compact representation.

4. **Phasing (see §9):**
   - P1 pilot (2 L2s) → expand on success.
   - P2 full Strategy + Capability in one pass (10 L2s).
   - P3 full S2R (16 L2s).

5. **ODA trilateral verification approach.** Expect 5–10 new OQs from R20.5→v25.5 cross-walk. OK with that, or want a clean trilateral sweep first to baseline?

---

## 11. Recommendation

**Decision 1: Include BVD** (full S2R coverage). Reasoning: GB991 §1.1.2 groups all three under S2R Lifecycle Area; partial inclusion creates an awkward gap in the lifecycle view; BVD's scope (Specification Lifecycle, Catalog Lifecycle, Anomaly Lifecycle) is conceptually paired with Capability Management's specification/catalog work — splitting them feels artificial.

**Decision 2: Option 2C — two view pages.** Reasoning: keeps the current `capability-map.md` clean for the user's primary OSS-operational use case (heat-map overlay against the Operations area). New `capability-map-s2r.md` carries the Strategy-to-Readiness content with its own frame, anchors, and (likely simpler) Mermaid diagram. Cross-link the two via top-of-page navigation. Avoids deepening heading levels in the existing capability map; avoids visual diagram bloat.

**Decision 3: Option 3b — two Mermaid diagrams.** Reasoning: matches the two-page split. Each page's diagram stays compact and focused.

**Decision 4: Option P1 — pilot first.** Reasoning: 16 L2s in one pass is a long-running effort; pilot validates the structural choices (Decisions 2 & 3) early. Pilot scope: 2 Strategy Management L2s (1.4.1 Service Strategy Management + 1.5.1 Resource Strategy Management). 6–8 hours. After pilot lands and is reviewed, expand to Capability Management, then BVD.

**Decision 5: Trilateral verification incremental.** File OQs as they arise during ingest; treat the trilateral sweep as part of the ingest (per the v1 pattern), not a precondition.

---

## 12. Next step (after user review of this document)

If the user approves the recommendations above:
1. Amend CLAUDE.md §3 per Option A.
2. Begin the pilot — ingest 1.4.1 Service Strategy Management as the first new L2 page. This single ingest exercises the full workflow (verbatim source extraction → L2 page → frontmatter → Source Pages → trilateral sections → SID/ODA back-references → lint).
3. Pause for user review.
4. If pilot lands clean, ingest 1.5.1 Resource Strategy Management.
5. Pause again.
6. Begin capability-map-s2r.md skeleton with the 2 Strategy Management capabilities.
7. Pause again — review the structural choices in practice, refine if needed.
8. Then expand to Capability Management (8 more L2 ingests).
9. Then BVD (6 more).
10. Throughout: capability-map-s2r.md fills in batch by batch like the original capability map; final L3-derived sub-capability review at the end.

---

## Document state

Prepared 2026-05-10 during capability-map Phase 3 scoping. Status: awaiting user review of decisions in §10. No corpus content modified yet — scoping only.

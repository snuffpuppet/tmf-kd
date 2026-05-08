# Resource ABE

Category landing page. Lists Resource ABE entities ingested from GB922 Resource
v25.5. This page is not normative for individual ABEs — entity-level content lives
in the per-ABE pages linked below.

> **Pre-production source.** GB922 Resource v25.5 PDF reports "Release Status:
> Pre-production" and "Approval Status: Team Approved" — not the standard
> "Production / TM Forum Approved" of other v25.x SID documents. All Resource ABE
> pages carry `release_status: pre-production` in frontmatter. See
> [[wiki/open-questions#OQ-027]] for the open question recording this status.

> **Production-side relevance.** Resources are the production/network-facing entities
> that ResourceFacingService (RFS in [[wiki/sid/service/service-abe]]) binds to. The
> Logical/Physical/Compound trichotomy (§4.2, §4.3) is the structural decomposition
> the corpus's PSR mapping goal uses for the production layer.

## ABEs in this category

GB922 Resource v25.5 organises the Resource Domain into 13 top-level ABEs (§4.1–§4.13
of the source):

- [[wiki/sid/resource/resource-party-roles-abe]] — Technician, ResourceInstaller, ResourceManager
- [[wiki/sid/resource/resource-specification-abe]] — Logical/Physical/Compound Spec; AI Model, Software, Address sub-ABEs (110 pages)
- [[wiki/sid/resource/resource-abe]] — Logical/Physical/Compound Resource instances; Computing & Software addendum (100 pages)
- [[wiki/sid/resource/resource-configuration-abe]] — specialises canonical Configuration
- [[wiki/sid/resource/resource-order-abe]] — Resource ordering
- [[wiki/sid/resource/resource-usage-abe]] — Resource Usage
- [[wiki/sid/resource/resource-test-abe]] — specialises canonical Test
- [[wiki/sid/resource/resource-performance-abe]] — Resource Performance
- [[wiki/sid/resource/stock-item-abe]] — Supply chain modelling (148 pages)
- [[wiki/sid/resource/resource-capacity-abe]] — specialises canonical Capacity
- [[wiki/sid/resource/resource-trouble-abe]] — *«notFullyDeveloped»* — pairs with Service Problem ABE
- [[wiki/sid/resource/resource-topology-abe]] — *«notFullyDeveloped»*
- [[wiki/sid/resource/resource-strategy-and-plan-abe]] — *«notFullyDeveloped»*

For browsable listing see [[wiki/sid/resource/_index]].

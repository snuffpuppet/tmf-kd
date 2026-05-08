# ODA — Functional Blocks

The 6 ODA Functional Blocks defined in GB1022 §4. Source: GB1022 ODA Functional
Architecture Guidebook v1.1.0.

## Architectural grouping (GB1022 §3 Systems of Separation)

GB1022 distinguishes three system groups, plus a transversal integration layer:

- **Engagement** (fast-evolving, customer-facing): [[wiki/oda/functional-blocks/engagement-management]]
- **Systems of Records** (stable, operational):
  [[wiki/oda/functional-blocks/party-management]],
  [[wiki/oda/functional-blocks/core-commerce-management]],
  [[wiki/oda/functional-blocks/production]]
- **Systems of Insight** (knowledge-defined automation):
  [[wiki/oda/functional-blocks/intelligence-management]]
- **Decoupling & Integration** (transversal): [[wiki/oda/functional-blocks/decoupling-and-integration]]

## Functional Block pages

| § | Block | Group | PSR Layer |
|---|-------|-------|-----------|
| 4.1 | [[wiki/oda/functional-blocks/decoupling-and-integration]]    | Transversal       | cross-cutting |
| 4.2 | [[wiki/oda/functional-blocks/engagement-management]]         | Engagement        | cross-cutting (front-end) |
| 4.3 | [[wiki/oda/functional-blocks/party-management]]              | Systems of Records| cross-cutting |
| 4.4 | [[wiki/oda/functional-blocks/core-commerce-management]]      | Systems of Records| product (commercial) |
| 4.5 | [[wiki/oda/functional-blocks/production]]                    | Systems of Records| service-and-resource (production) |
| 4.6 | [[wiki/oda/functional-blocks/intelligence-management]]       | Systems of Insight| cross-cutting |

## Production/commercial separation mapping

For the corpus's PSR mapping goal:

- **Commercial layer:** [[wiki/oda/functional-blocks/core-commerce-management]]
  (Product/Offering catalog, Order Capture, Billing) plus
  [[wiki/oda/functional-blocks/party-management]] (Customer/Partner data)
- **Production layer:** [[wiki/oda/functional-blocks/production]] (CFS/RFS
  lifecycle, network/resource operations)
- **Front-end:** [[wiki/oda/functional-blocks/engagement-management]] (UI/UX,
  cross-channel)
- **Cross-cutting:** [[wiki/oda/functional-blocks/intelligence-management]]
  (analytics) and [[wiki/oda/functional-blocks/decoupling-and-integration]]
  (integration)

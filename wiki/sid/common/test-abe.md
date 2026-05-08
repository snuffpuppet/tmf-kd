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
entity_name: "Test ABE"
---

# Test ABE

## Overview

A test is a procedure intended to establish the quality, performance, or reliability
of an entity, especially before it is taken into widespread use. A test may also be
executed upon the entity after it is in use to diagnose problems related to the
correct functioning of the entity. As such, a test may be executed against a product,
a service, or a resource.

The tests are divided into three categories:

- **Pro-active/Controlled.** Tests that are established during the fulfillment
  process on an entity, and are generally run continuously throughout the lifetime
  of the entity. These tests are often used to establish correct functioning of the
  entity under test before providing the entity to a consumer. The results of these
  tests may be queried at any given time.
- **On-demand/Controlled.** Tests that are requested at a specific point in time,
  but that may also be scheduled to actually execute at a future point in time.
  These tests are normally run as part of assurance processes; they are used to
  either detect problems, or to guarantee quality, performance, or reliability
  commitments made to the consumer of the function provided by the entity under
  test. These tests are controlled in the sense that they are "managed" and can be
  suspended, resumed, and for which results may be requested.
- **On-demand/Uncontrolled.** Tests that are requested to execute immediately, and
  for which the request is blocking until the test completes and returns results in
  real time. These tests are uncontrolled in that they may not be "managed".

Test ABE is specialised for Product Test ABE, Service Test ABE and Resource Test ABE.
— GB922 Common §4.23, p. 810

## Key Attributes

Source §4.23.2 (Figure T.01 — Basic Test Entities) defines core entities:

- **Test:** `adminState: AdministrativeState`, `description: String`,
  `mode: TestMode`, `name: String`, `state: TestState`
- **TestSpecification:** `description: String`, `name: String`,
  `validFor: TimePeriod`
- **TestMeasure** / **TestMeasureDefinition** — specific measures captured during
  test execution
- **TestSpecificationRole** — abstract base for product/service/resource test
  specification roles
- **MetricMeasurementJob** — the actual execution of Test(s) producing
  TestMeasures

Detailed attribute tables not extracted in v1 ingest; consult source.
— GB922 Common §4.23.1–§4.23.2, pp. 810–812

## Relationships

- **Specialisations:** ProductTest, ServiceTest, ResourceTest (each living in its
  domain ABE: [[wiki/sid/service/service-test-abe]],
  [[wiki/sid/resource/resource-test-abe]]; Product Test ABE not separately ingested
  in v1 — see [[wiki/sid/product/product-test-abe]])
- **TestSpecification ↔ EntitySpecification** (Product/Service/Resource
  Specification): TestSpecification describes how a test against that entity is
  configured
- **TestMeasureDefinition** inherits from `MetricDefMeasure` in
  [[wiki/sid/common/metric-abe]]
— GB922 Common §4.23, pp. 810–812

## ODA Components That Own This Entity

See [[wiki/open-questions#OQ-008]] — Common Test ABE not directly mapped in any
ODA Functional Block table; specialised Test ABEs (Product/Service/Resource Test)
are mapped via their specialisation parent's ODA owner.

## eTOM Processes That Manipulate This Entity

See [[wiki/open-questions#OQ-008]] — eTOM mappings for Test ABE pending trilateral
sweeps. The v25.5 L3 "Manage Service Test" (1.4.4.6) and L3 "Manage Resource Test"
(1.5.4.9) likely manipulate specialisations rather than the Common parent.

## Open Questions

- OQ-008: Trilateral linking pending further ODA component sweeps
- OQ-009: BE-level attribute detail deferred
- OQ-041: Test ABE ingested as part of v1 Common gap fill

---
type: foundation
spec_id: GB991
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/foundations/GB991_TMForum_Core_Frameworks_Concepts_and_Principles_v25.5.pdf
source_extract_paths:
  - raw/extracted/tmf/foundations/GB991_TMForum_Core_Frameworks_Concepts_and_Principles_v25.5.md
authority: primary
concept_category: principle
title: "Core Frameworks Principles"
---

# Core Frameworks Principles

## Overview

GB991 §2 catalogues principles for the Core Frameworks, organised into Shared
principles (apply across all frameworks) and framework-specific principles for the
Business Process Framework, Information Framework, and Functional Framework.

Two principle areas are marked "FUTURE WORK" in v25.5 and are not represented here:
§2.2.1 Business Capability and §2.2.5 Metrics. See [[wiki/open-questions#OQ-005]] and
[[wiki/open-questions#OQ-006]].

The Functional Framework principles in §2.2.4 carry an explicit caveat from the
source: "We are currently in the process of redefining the principles of the Functional
Framework. This is an iterative process and we plan to remove the current principles
and add new one as they are identified discussed and approved to be included." The
"previous list of principles" is reproduced here verbatim with that caveat noted. See
[[wiki/open-questions#OQ-004]].

## Shared Principles

### S-01 — One framework organizes all ODA Core objects

**Statement.** A shared framework is a common language and structure that enables
different parts of the Open Digital Architecture to organize concepts that work
together effectively towards same goals, by improving communication and collaboration,
and by reducing confusion and misunderstandings.

**Rationale.**

- Improve communication and collaboration between different parts of the enterprise.
- Better decision-making with context based on bounded zones / blocks.
- Provide a common language and structure for different foundations of ODA to work
  together effectively.
- Ensure producers and consumers are working towards the same goals with reduced
  confusion and misunderstandings.

**Implications.**

- Provide a common language and structure for Open Digital Architecture foundation
  assets that serve as primitives for enterprises to plan, transform and operate.
- Reduce confusion and misunderstandings between different departments or teams and
  help to ensure that business objects grouped are altogether supporting same goals.
- Improve communication and collaboration between different parts of an enterprise,
  which can lead to better decision-making and more effective problem-solving.

— GB991 §2.1, pp. 21

### S-02 — Release and Publication Status

**Statement.** The shared release and publication status for all ODA Core assets shall
be one of:

- Released
- Preliminary
- Draft
- Not Fully Developed

**Rationale.** Applying the same lifecycle statuses across all elements promotes
consistency, predictability, and transparency. It allows for better tracking,
management, and understanding of the state of each element at any given time.

**Implications.**

- Ensures that all stakeholders have a clear understanding of the status of each
  element.
- Facilitates better planning and resource allocation based on the lifecycle status.
- Promotes accountability as each status requires specific actions and
  responsibilities.
- Enhances efficiency by standardizing the process of updates and releases.

— GB991 §2.1, pp. 21–22

### S-03 — Business-first understanding

**Statement.** All business processes, information models, and software functions
shall be designed with simplicity and a business-first approach. They should be easily
understandable and directly contribute to the achievement of business goals.

**Rationale.** Simplicity leads to better understanding, efficient execution, and
easier maintenance. A business-first approach ensures that all processes, models, and
functions are aligned with the enterprises objectives and contribute to its success.

**Implications.** Keep models simple and understandable by Business first, and then
technology personas. This will:

- Facilitate clear communication across all levels of the enterprise.
- Enhance efficiency by reducing complexity in processes, models, and functions.
- Ensure alignment of all operations with the enterprises' business goals.
- Promotes a culture of simplicity and clarity in the enterprise.

— GB991 §2.1, p. 22

## Business Process Framework Principles

### BPF-01 — Nature of the Business Process Framework

**Statement.** The Business Process Framework consists of a decomposition structure
and taxonomy of process abstractions representing business process elements (i.e.
groups of processes, activities and tasks) that a Service Provider needs to manage.

**Rationale.** The Business Process Framework is intended to be comprehensive — all of
a service provider's processes, activities and tasks should fit within the Business
Process Framework.

**Implications.** The process abstractions of the business process framework are
categorizations of the context-specific processes that exist within service providers.
The Business Process Framework provides a comprehensive catalog of such process
abstractions relevant for a Service Provider. It provides an industry agreed standard
consisting of process decomposition structure, terminology, and classification scheme
of process elements across multiple levels of decomposition.

The process elements of the Business Process Framework can be used to create
consistent process flows (however, they are not business process flows themselves)

The business drivers for adopting and using the framework can be summarized according
to the following:

- The need to standardize the language for describing business processes
- The need to standardize tasks on which business process flows will be based
- The need to understand the elements that make up each business process.
- The need to understand the objectives associated with each business processes

— GB991 §2.2.2, pp. 22–23

### BPF-02 — Standards for Organizing Business Processes — Naming, Decomposition and Traceability

**Statement.** A business process element shall be named and decomposed according to
the following pattern or structure.

Naming:

- Noun verb (for a business process grouping)
- Verb noun (for underlying activities and tasks that support the business process)

Decomposition:

- The Business Process Framework is decomposed from notional Level 0 to more granular
  levels
- The Levels 1, 2, 3 and 4 (and some of levels 5 and 6) are addressed so far.

**Rationale.** This prevents any confusion and establishes a unified level setting for
business processes. Because the Business Process Framework is a decomposition model,
the lower levels of the decomposition can be traced back to the higher levels.

As a classification or taxonomy of Process Elements, at Level 0 the elements are
classified into S2R (Strategy to Operations) and Operations. Lower Levels are formed
by decomposition with each Process Element occurring once only.

**Implications.**

- Achieve consistency in naming and decomposition following a consistent pattern
- Ensure the goal is implied in the name of the business process with relevance
  primary stakeholders.
- Ensure the name resonates with industry use or advances industry consensus about the
  primary role the business process plays.

— GB991 §2.2.2, pp. 23–24

### BPF-03 — Classification of Business Processes

**Statement.** All business processes shall be classified as one of the following
types:

- Core Process
- Enabling Process
- Supporting Process

**Rationale.** Enable organizations to identify important business actions that impact
their core business, enabling the management of resources and the efficiency of
support. This includes cost reduction and resource allocation.

**Implications.**

- Enable enterprises to understand and manage business processes more effectively.
- Identify levels of importance of business processes and allocate associated
  resources accordingly.
- Help to improve efficiency and reduce costs of operationalizing business processes,
  while also ensuring that the enterprise is focused on its core business goals.

— GB991 §2.2.2, p. 24

### BPF-04 — Definition of Business Processes

**Statement.** All business processes should be clearly defined in terms of their
structure, constituents, roles and purpose.

**Rationale.** Enable organizations to ensure their business processes are consistent
and complete.

**Implications.**

- A business process has characteristics that include goals, inputs, outputs and
  business outcome.
- A well identified, scoped and articulated business process must provide clarity on
  the resources underpinning its activities.
- Organizations should be able to realize goals linked to business processes by
  formalizing them in specific sequence to realize value.

— GB991 §2.2.2, pp. 24–25

### BPF-05 — Information Ownership By Business Processes

**Statement.** Each Business Process element should be associated with one (or more)
Information Framework ABE(s).

**Rationale.** To be consistent, processes must be related to specific information
elements.

**Implications.**

- Business processes do not exist in isolation. Processes require information from
  other processes, and they in turn provide information to other processes.
- Dependencies (or associations) between processes occur when an activity requires
  information from another activity. Process dependencies are related to the entities
  and attributes required by the business area.

— GB991 §2.2.2, p. 25

### BPF-06 — Business Process Ownership

**Statement.** A business process shall always have a "Process Owner" who acts as the
person or instance that has the highest level of responsibility and decision-making
with respect to the process; such person or instance is designated as being
accountable for the outcome that results from the execution of the process.

**Rationale.** Responsibility can be shared amongst individuals involved in the
execution of a particular process, however, accountability — which designates ultimate
responsibility and ownership of the process — refers to the unique instance or person
who is in charge of the entire process, and therefore accountable for the outcome
resulting from the execution of such process, this instance or person is designated as
the "accountable" party and it is in general referred to as "the Owner" of the
process.

**Implications.**

- "Shared responsibility is no accountability";
- a business process is always overseen and "groomed" by its owner who is the person
  or instance ultimately responsible for the outcome of the execution of the process;
- failure to designate or have implicitly a process owner or accountable party would
  result in lack of commitment or accountability in the event that the process is not
  delivering the expected outcome; likewise, if the process is delivering excellent
  results, it is most often the process owner (or accountable instance) that gets
  glorified.

— GB991 §2.2.2, pp. 25–26

### BPF-07 — Continuously Optimize Business Processes

**Statement.** New information systems will be implemented after business processes
have been analyzed, simplified or otherwise redesigned as appropriate.

**Rationale.**

- There is no real "value" in applying technology to old, inefficient business
  processes.
- Core processes will be more streamlined, efficient and cost-effective.
- Core processes, activities, tasks and associated business rules will be well
  understood and documented.
- Reduces the total cost of ownership.

**Implications.**

- Need to have an agreed upon continuous business process improvement activity.
- New technology will be applied in conjunction with business process review.
- Business processes must be optimized to align with business drivers.
- Additional time and resources will have to be invested in analysis early in the
  systems' lifecycle.
- Organizational change will be required to implement reengineered work processes.
- May require regulatory or legislative change.

— GB991 §2.2.2, p. 26

### BPF-08 — A core process has a unique position in the process framework

**Statement.** All Level-2 (L2) business processes have a specific, unique position in
the process framework, their position depends on the purpose, nature, and role of the
process within the enterprise. As a general rule, each position is determined by the
intersection between the vertical grouping and the horizontal domain to which the
process belongs in the process framework. In general, L2 process belong to one unique
vertical and one unique horizontal domain; however, there are some exceptions in which
some L2 processes can span more than one vertical, these are commonly referred to as
cross-functional or transversal core processes.

**Rationale.** The Business Process Framework was created and evolved from two
different but complementary models: 1) An Enterprise Architecture layering model
(based on a construct of hierarchical architecture layers) which originated with the
early concepts underpinning the TMN model; and 2) An enterprise lifecycle structure
consisting of vertical groupings (aka lifecycle stages) which originated in the early
concepts associated with the FCAPS model. Such design resulted in a matrix of X and Y
positions, each position characterized by a specific couple 'vertical/horizontal',
representing a unique stage in the enterprise lifecycle and a unique horizontal
architecture domain; as a general rule, each position hosts several L2 processes,
therefore, each L2 process belongs to one unique vertical and one unique horizontal
domain; however, some L2 processes span more than one vertical, these are referred to
as cross-functional or transversal processes, they are considered exceptions to the
previous rule, and therefore they are prone to change in the future as the framework
continues to evolve.

**Implications.** Level-2 (L2) processes play a vital role in the lifecycle of the
enterprise, each L2 process represents a grouping of activities and tasks that deliver
the intended business outcomes for each part of the enterprise process framework, as
such, L2 processes are designed based on the role they perform and outcome they
deliver, both of which are determined by the position of the process in the framework
i.e. vertical grouping(s) and horizontal domain to which the process belongs. In the
past, common process models were designed contextless — that is — core processes were
monolithic elements decomposed into smaller granularity elements, but without being
directly related or mapped to any specific context i.e., didn't belong to any
particular enterprise lifecycle or architecture domain e.g., Product, Service,
Resource, etc. The Business Process Framework (eTOM) brought along an innovative
classification and modelling of the business processes across the enterprise, by
adding horizontal domains and vertical Lifecycle stages which provided a meaningful
architectural context.

— GB991 §2.2.2, pp. 26–27

### BPF-09 — Business Processes lead on architecture requirements

**Statement.** Business processes represent an implementation of the business
requirements sourced from the organization's strategy and business intent, as such,
business processes embody the required support and full alignment with the business to
ensure business operations and their goals are achieved.

**Rationale.** Business processes embody the activities and tasks that need to be in
place, to enable and support successfully the operation of the enterprise, business
processes are in alignment with the goals of the business, as such, they translate
business intent and required business capabilities into "implied" functional
requirements that are further communicated to the functional, application and
technology architectures — as subordinates of the Business Architecture — for
implementation and execution through either manual or automated support, or a
combination of both.

**Implications.** Business processes play a central role in the business architecture,
as they define altogether the fabric of activities and tasks that are needed to
effectively support and run the business. It is a vital principle to always ensure an
optimal alignment between the enterprise business goals, and the capabilities
available to support and achieve those goals.

— GB991 §2.2.2, pp. 27–28

## Information Framework Principles

> **Verbatim note on numbering.** The GB991 v25.5 source presents INF principles as
> #INF-01, #INF-05, #INF-06, #INF-07, #INF-08, #INF-09, #INF-10. Numbers 02, 03, 04 do
> not appear. See [[wiki/open-questions#OQ-003]].

### #INF-01 — Coupling of ABEs to Business Processes

**Statement.** An ABE shall be created by one business process (denoted primary
process). If a one-to-one coupling is not achievable, an ABE shall be coupled to
associated

**Rationale.** A single primary process should manage the complete life cycle of an
ABE, creating, updating, and deleting entity instances contained within the ABE.

**Implications.** If there is more than one process creating an ABE, this suggests
these are overlapping processes, or the scope of the ABE is too broad.

— GB991 §2.2.3, p. 28

### #INF-05 — ABEs, Core Entities and Dependent Entities

**Statement.** There should be one single core business entity in an ABE in general
(there are some exceptions however), in most cases the core entity has the same name
as its parent ABE.

**Rationale.** A well-defined Aggregate Business Entity (ABE) consists of a set of
information that characterizes a highly cohesive, loosely coupled set of business
entities, which have loose relationships with items outside the ABE.

**Implications.** A core business entity is an entity that is not dependent upon any
other entity within the ABE. Likewise, generally, non-core business entities are
dependent on the core business entity. And do not need to have an 'ID' attribute,
given they can be reached by navigation from the core business entity.

— GB991 §2.2.3, p. 28

### #INF-06 — Principles for ABE Placement in Shared Domain versus Patterns Domain

**Statement.** ABEs and related BEs will be placed in Shared when:

1. One or more "Core" Business Entities are "Concrete", AND
2. Business Entities must be used in more than one domain without modification or
   subclassing (e.g. - Party)

A core entity is a main entity (not a subclass)

ABEs and related BEs will be placed in the Patterns Domain when:

1. All "core" business entities are abstract.

Business entities, attributes, and/or relationships are inherited by concrete business
entities within other ABEs.

**Rationale.** To be completed

**Implications.** To be completed

— GB991 §2.2.3, p. 28

### #INF-07 — Principles for ABE Placement in Patterns Domain

**Statement.** ABEs and related BEs will be placed in the Patterns Domain when

1. All "core" business entities are abstract.
2. Business entities, attributes, and/or relationships are inherited by concrete
   business entities within other ABEs.

**Rationale.** To be completed

**Implications.** To be completed

— GB991 §2.2.3, p. 29

### #INF-08 — Inheritance

**Statement.** The Information Model is built on the principle of "single
inheritance". Not all business entities need to be "rooted", but a given class/business
entity can only inherit from one entity.

Notes:

- Must verify that this is true
- One reason for not doing multi-inheritance is because it can be a challenge to
  'implement'

**Rationale.** To be completed

**Implications.** To be completed

— GB991 §2.2.3, p. 29

### #INF-09 — Association Directionality

**Statement.** Within the SID model, an association is assumed to be bi-directional.

**Rationale.** To be completed

**Implications.** To be completed

— GB991 §2.2.3, p. 29

### #INF-10 — Ennumerations

> **Verbatim note.** The source heading reads "Ennumerations" (double n), preserved
> verbatim.

**Statement.** Generally, the Information model does not use enumerations. Attributes
with some number of given values is handled as follows:

**Rationale.** To be completed

**Implications.** To be completed

— GB991 §2.2.3, p. 29

## Functional Framework Principles

> **Verbatim source caveat.** GB991 §2.2.4 prefaces this list with: "Please note! We
> are currently in the process of redefining the principles of the Functional
> Framework. This is an iterative process and we plan to remove the current principles
> and add new one as they are identified discussed and approved to be included.
> Previous List of Principles, will be curated in next version." See
> [[wiki/open-questions#OQ-004]].

### #FUF-01 — Nature of the Functional Framework

**Statement.** The Functional Framework is a taxonomy of systems\* capabilities that
are relevant to the ecosystem of communications service providers. Systems
capabilities are what systems are able to provide, defined independent of the context
of specific processes, organizations, applications and implementations.

\*Software and/or hardware

**Rationale.** It is the intent that all functions of the Service Provider can be
supported by (i.e. are able to fit within) the Functional Framework functions. Each
function has a detailed description that reflects its purpose.

**Implications.** The Functional Framework is a catalog of functions/functionalities
that are relevant for a Service Provider.

The Functional Framework specifies functions along with their descriptions and are
grouped in alignment with the Business Process Framework process structure.

The functions Process Elements are activity-based, and the Business Process Framework
is thus an activity-based process decomposition model.

— GB991 §2.2.4, p. 30

### #FUF-02 — Definition of Functional Framework Functions

> **Verbatim note.** The source heading carries the editorial annotation
> "[TO BE EDITED BY KAJ / DONE]". Preserved verbatim from the source. See
> [[wiki/open-questions#OQ-004]].

**Statement.** A function is defined to produce one specified result.

Functions are defined at such granularity level that the principle of separation of
concerns is considered and when activated the function's result will be accepted
without exceptions.

Each Functional Framework functions should be unique for each described functionality.

**Rationale.** The functions of the Functional Framework shall be trusted to be
unique. The function shall specify a functionality without exceptions.

**Implications.** A function specifies the action it will perform. A list of functions
can be used to specify a collective functionality of e.g. a component or application,
without the risk of conflicting functions or overlapping functionality.

— GB991 §2.2.4, p. 30

### #FUF-03 — Information Ownership Functions

**Statement.** In Domains that are business context specific, (Market_Sales, Customer,
Product, Service, Resource and Business Partner) the functions belonging to these
domains have a direct responsibility type of relationship (Create, Update and Delete)
with Information Framework elements.

Functions in the Shared Domain can be used in different contexts, which means that
mapping to Information Framework elements will differ depending on where the functions
are used.

**Rationale.** A fundamental role of functions is to manage information. Based on the
function's purpose it is related to specific information elements.

**Implications.** Functions are the primary way to manage information and acts on
behalf of processes and other functions to manage the information of their ownership.

Functions require information from other functions, and they in turn provide
information to other functions, but each function should have unique impact on its
related information.

— GB991 §2.2.4, pp. 30–31

### #FUF-04 — Function Ownership

**Statement.** A function shall always have a "Function Owner" that acts as the entity
or instance that, from an implementation point of view, is responsible for the direct
outcome that results from the execution of the function.

**Rationale.** Responsibility can be shared amongst entities or instances of parties
involved in the specification and execution of a particular function, however,
accountability — which designates utmost responsibility and ownership of the parent
process — refers to the unique instance or person who is ultimately liable for the
outcome of the process, the process in turn delegates responsibility to the function
in charge for the execution of the task(s) involved. Depending on the implementation
scenario, the function can be owned by the delegating process itself, or by a different
entity or party (e.g., outsourcing scenario).

**Implications.** "Shared responsibility is no accountability."

A function is always overseen and "groomed" by its owner who is the person or entity
ultimately responsible for the outcome of the execution of the function. If a function
owner or accountable party has not been formally specified or designated, the result
could be a lack of commitment or accountability in the event that the function is not
delivering the expected outcome; likewise, if the function is delivering the expected
result, it is the function owner, or the accountable process owner, or both who get
credit for the successful outcome.

— GB991 §2.2.4, p. 31

### #FUF-05 — Continuously Optimize Functions

**Statement.** New functions will be designed and implemented continuously as
information systems and technology develop.

Functional Framework functions will continuously be analyzed, simplified, or otherwise
redesigned as appropriate to follow the development.

**Rationale.** For the management of the functionality of a corporate's system
infrastructure the functions must be continuously improved, and the number of
functions expanded.

Functions will be used or referred to in many systems architectures.

To have access to up-to-date function specifications is of great value.

For systems architectures with high flexibility to improve individual functions (e.g.,
ODA Components) the functional framework and the functions are expected to be updated
in a dialog with the industry.

For more stable systems the Functional Framework function and the functions are
expected to be a source of reference and inspiration.

**Implications.** There is a need to have an agreed governance of continuous function
improvement activity.

New technologies will influence the Functional Framework and its functions.

Functions must be optimized to align with business development, architecture
development and technology development.

Additional time and resources will have to be invested in analysis early in the
systems lifecycle.

Organizational change will be required to implement reengineered systems with
optimized functions.

— GB991 §2.2.4, p. 32

## Cross-Framework Application

_(populated as eTOM, SID, and ODA pages reference specific principles; e.g. an ODA
component page may invoke FUF-03 when establishing information ownership; a SID entity
page may invoke INF-08 for inheritance behaviour)_

-

## Open Questions

- OQ-003: GB991 INF principle numbering gap (INF-02/03/04 absent) — see
  [[wiki/open-questions#OQ-003]]
- OQ-004: §2.2.4 Functional Framework principles flagged "previous list, will be
  curated" by source — see [[wiki/open-questions#OQ-004]]
- OQ-005: §2.2.1 Business Capability principles marked "FUTURE WORK" — see
  [[wiki/open-questions#OQ-005]]
- OQ-006: §2.2.5 Metrics principles marked "FUTURE WORK" — see
  [[wiki/open-questions#OQ-006]]

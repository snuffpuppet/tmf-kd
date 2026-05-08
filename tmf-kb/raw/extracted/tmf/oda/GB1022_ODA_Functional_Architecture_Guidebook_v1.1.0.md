TM Forum Guidebook



GB1022 ODA Functional
Architecture Guidebook




GB1022
Team Approved Date: 29-Jan-2021



 Release Status: Production            Approval Status: TM Forum Approved
 Version 1.1.0                         IPR Mode: RAND


TM Forum 2021. All Rights Reserved.
GB1022 ODA Functional Architecture Guidebook v2.0.0




Notice
Copyright © TM Forum 2021. All Rights Reserved.

This document and translations of it may be copied and furnished to others, and derivative
works that comment on or otherwise explain it or assist in its implementation may be
prepared, copied, published, and distributed, in whole or in part, without restriction of any
kind, provided that the above copyright notice and this section are included on all such copies
and derivative works. However, this document itself may not be modified in any way, including
by removing the copyright notice or references to TM FORUM, except as needed for the
purpose of developing any document or deliverable produced by a TM FORUM Collaboration
Project Team (in which case the rules applicable to copyrights, as set forth in the TM FORUM
IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by TM FORUM or
its successors or assigns.

This document and the information contained herein is provided on an “AS IS” basis and TM
FORUM DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY
OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A
PARTICULAR PURPOSE.

TM FORUM invites any TM FORUM Member or any other party that believes it has patent
claims that would necessarily be infringed by implementations of this TM Forum Standards
Final Deliverable, to notify the TM FORUM Team Administrator and provide an indication of its
willingness to grant patent licenses to such patent claims in a manner consistent with the IPR
Mode of the TM FORUM Collaboration Project Team that produced this deliverable.

The TM FORUM invites any party to contact the TM FORUM Team Administrator if it is aware
of a claim of ownership of any patent claims that would necessarily be infringed by
implementations of this TM FORUM Standards Final Deliverable by a patent holder that is not
willing to provide a license to such patent claims in a manner consistent with the IPR Mode of
the TM FORUM Collaboration Project Team that produced this TM FORUM Standards Final
Deliverable. TM FORUM may include such claims on its website but disclaims any obligation to
do so.

TM FORUM takes no position regarding the validity or scope of any intellectual property or
other rights that might be claimed to pertain to the implementation or use of the technology
described in this TM FORUM Standards Final Deliverable or the extent to which any license
under such rights might or might not be available; neither does it represent that it has made
any effort to identify any such rights. Information on TM FORUM's procedures with respect to
rights in any document or deliverable produced by a TM FORUM Collaboration Project Team
can be found on the TM FORUM website. Copies of claims of rights made available for
publication and any assurances of licenses to be made available, or the result of an attempt
made to obtain a general license or permission for the use of such proprietary rights by
implementers or users of this TM FORUM Standards Final Deliverable, can be obtained from
the TM FORUM Team Administrator. TM FORUM makes no representation that any
information or list of intellectual property rights will at any time be complete, or that any
claims in such list are, in fact, Essential Claims.




© TM Forum 2021. All Rights Reserved.                                  Page 2 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Direct inquiries to the TM Forum office:

181 New Road, Suite 304
Parsippany, NJ 07054, USA
Tel No. +1 973 944 5100
Fax No. +1 973 998 7916
TM Forum Web Page: www.tmforum.org




© TM Forum 2021. All Rights Reserved.                 Page 3 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Table of Contents

     Notice .................................................................................................................................... 2
     Table of Contents................................................................................................................ 4
     List of Tables.......................................................................................................................... 6
     List of Tables.......................................................................................................................... 7
     Executive Summary ............................................................................................................... 8
     1. Introduction ....................................................................................................................... 9
             1.1.         Benefits of ODA .............................................................................................. 9
             1.2.         Scope of ODA Functional Architecture ........................................................... 9
     2. The Functional Architecture of ODA ................................................................................ 11
     3. ODA Systems of Separation ............................................................................................. 13
     4. The Functional Blocks ...................................................................................................... 15
             4.1.         Decoupling & Integration ............................................................................. 15
                 4.1.1.       Definition & Scope .................................................................................... 15
                 4.1.2.       Functions of Decoupling & Integration .................................................... 15
             4.2.         Engagement Management ........................................................................... 15
                 4.2.1.       Definition & Scope .................................................................................... 15
                 4.2.2.       Engagement Management is characterized as: ....................................... 16
                 4.2.3.       Engagement Management Block functionalities ..................................... 16
                 4.2.4.       Open API's Mapping ................................................................................. 17
             4.3.         Party Management ....................................................................................... 18
                 4.3.1.       Definition & Scope .................................................................................... 18
                 4.3.2.       Business Processes in the Party Management Block ............................... 18
                 4.3.3.       Standard Business Information Entities ................................................... 24
                 4.3.4.       Standard Interfaces .................................................................................. 27
             4.4.         Core Commerce Management ..................................................................... 28
                 4.4.1.       Definition & Scope .................................................................................... 28
                 4.4.2.       Business Processes in the Core Commerce Management Block .............. 29
                 4.4.3.       Standard Business Information Objects ................................................... 33
                 4.4.4.       Standard Interfaces .................................................................................. 36
             4.5.         Production .................................................................................................... 37
                 4.5.1.       Definition & Scope .................................................................................... 37
                 4.5.2.       Standard Business Information Objects ................................................... 41


© TM Forum 2021. All Rights Reserved.                                                                        Page 4 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



                 4.5.3.       Standardized Interfaces............................................................................ 45
            4.6.          Intelligence Management ............................................................................. 47
                 4.6.1.       Business Processes in the Intelligence Management Block ..................... 48
                 4.6.2.       Standard Business Information Objects ................................................... 50
                 4.6.3.       Intelligence Management Block functionalities ....................................... 52
                 4.6.4.       Standardized Interfaces............................................................................ 54
     5. Using the Functional Architecture ................................................................................... 55
            5.1.          Reference User Stories ................................................................................. 55
                 5.1.1.       IG1197 ODA User Stories and Use Cases.................................................. 55
                 5.1.2.       IG1228 ODA/APIs Call Flow Use Cases ..................................................... 55
            5.2.          Function level mappings ............................................................................... 55
            5.3.          Creating an ODA Component ....................................................................... 55
                 5.3.1.       IG1171 ODA Component Definition ......................................................... 55
            5.4.          Implementation Scenarios ............................................................................ 55
                 5.4.1.       IG1167 ODA Functional Architecture ....................................................... 55
     6. Evolution .......................................................................................................................... 56
     7. Administrative Appendix ................................................................................................. 57
            7.1.          Terminology, Abbreviations and Definitions ................................................ 57
            7.2.          References .................................................................................................... 57
                 7.2.1.       Core References ....................................................................................... 57
                 7.2.2.       Other Related References ........................................................................ 57
     8. Document History ............................................................................................................ 58
            8.1.          Version History ............................................................................................. 58
            8.2.          Release History ............................................................................................. 58
     9. Acknowledgements ......................................................................................................... 59




© TM Forum 2021. All Rights Reserved.                                                                     Page 5 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




List of Tables

Figure 2.1. ODA Functional Architecture - High Level view (Level 0).......................................... 11
Figure 2.2. ODA Functional Architecture - alternate view (Level 0) ........................................... 12
Figure 3.1. Grouping of systems based on the Functional Architecture .................................... 13




© TM Forum 2021. All Rights Reserved.                                                Page 6 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




List of Tables

Table 4-1. Decoupling & Integration key functionalities ............................................................ 15
Table 4-2. Functionalities provided by the Engagement Management Block include: .............. 16
Table 4-3. Party Management eTOM Process Descriptions ....................................................... 19
Table 4-4. SID ABEs and their description (Source GB922 R20.5 ) .............................................. 24
Table 4-5. Proposed Standard Interfaces for Party Management block .................................... 28
Table 4-6. Core Commerce Management eTOM Process Descriptions (Source reference GB921
R20.5) .......................................................................................................................................... 30
Table 4-7. SID ABEs and their description (Source GB922 R20.5)............................................... 34
Table 4-8. Standard Interfaces in the Core Commerce block ..................................................... 36
Table 4-9. Production Standardized Business Process descriptions (Source reference GB921
R20.5) .......................................................................................................................................... 38
Table 4-10. SID ABEs and their description (extract from GB922 20.5) ..................................... 42
Table 4-11. Standard Interfaces in the Production block ........................................................... 46
Table 4-12. Intelligence Management eTOM Process descriptions ........................................... 48
Table 4-13. SID ABEs and their description (extract from GB922 20.5) ..................................... 51
Table 4-14. Functionalities covered by the Intelligence Management block ............................ 52
Table 4-15. Standard Interfaces in the Intelligence Management block ................................... 54




© TM Forum 2021. All Rights Reserved.                                                                          Page 7 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Executive Summary
The fifth generation of mobile technology and onward, seize growth opportunities that drives
continuous management and operations transformation. This demands a “fifth generation”
business that is primarily digital-first. The result is addressing business transformation in a
holistic way, a way encompassing strategy transformation and continuous innovation;
customer centricity; digital business operations, responsiveness and agility; and the ability to
engage in multi-sided and platform-based business models.
Supporting systems that have in the past helped service provides in technology business
management and operations, typically referred to as Business and Operations Support
Systems (BSS/OSS) hold the key to manage and monetize new opportunities at scale. The
ability to align and transformation these systems has mandated refactoring of the typical two-
view monolithic view, into a flat, non-layered management and operations supporting
systems.
This guidebook presents the standards for refactoring typical BSS/OSS into a digital-native
architecture that facilitates simplification of business operations. As service providers evolve
and refactor technology systems, CTIOs must address Customer Experience needs, Revenue
Management needs, Total Cost of Ownership (TCO) and effective Operational Efficiency. These
are the agility and responsiveness goals that mark the success of businesses in a digital-native
world. The new generation of systems needed, embrace advancement in prior architectural
models, like Service Oriented Architectures (SOA), event-based Microservice with new
development and operations models that rely on Open source, Virtualization and Software-
enabled management. The result is the ability to scale technologies to meet business needs,
and to ultimately achieve business goals.
The business potential leading to defining a new management and operations software stack
has been explored in many TM Forum research reports, and member collaboration projects.
These initiatives have altogether explored the opportunities a service-oriented operation,
solving the problems of a communications service provider, and attaining utilizing the best of
technologies and capabilities from both the IT and CT worlds. This combination is refining
existing and new business and addressing new growth opportunities.
The Open Digital Architecture developed based on member's common vision, and shared
understanding of the future of service delivery, has defined the standards of separating
management and operating concerns for organization objects, mapped them to business
processes, implemented functional grouping void of any organization implementation
specifics, and defined principles for decoupling and integration of architecture components.
The evolution of the standards will be based on requirements that guides its continuity into
the future systems.
This document represents the key artifacts that frames the Information Systems Architecture.




© TM Forum 2021. All Rights Reserved.                                    Page 8 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




1. Introduction
This document outlines the normative aspects of Open Digital Architecture Functional
framework. It presents the Operations Map and the Technology Integration mapping along
with descriptions and high level specifications for a digital platform and digital service
provider. IT represents an agreed view of a majority of the industry key stakeholders strategic
and operating plan.
The document targets CTIOs, Enterprise Architects, Platform Owners, Supply Chain Managers
and Business Transformation officers. It can be used to define RFPs, refactor legacy BSS/OSS
systems, as well as their management and operations. It defines standards for mapping
business and information objects in a way that addresses concerns about vendor lock-in,
product innovation, multi-vendor operating environment, etc.
As the Functional Architecture for the Open Digital Architecture, it enforces the principles
established in GB998 Open Digital Architecture (ODA) Concepts & Principles and set out clarity
for decoupling of functions, componentization of applications, and inclusion of systems of
intelligence. Mapping to the Frameworx Business Process Framework (eTOM GB921)
and Information Framework (SID GB922) are standards that capture business concerns of
today, as well as new requirements that fulfill the changing dynamics of business,
management and operations in a digital world.



                    1.1. Benefits of ODA
•   Decouples Technical and Commercial evolution of the Business (It achieves this through a
    new Functional grouping which provides flexible composition and interaction)
•   Provides direct and real-time cross-functional capability interaction between Systems of
    Engagement (SoE), Systems of Record (SoR) and Systems of Insights(SoI).
•   Removes data replication between functions that work on the same data
•   Allows playing different roles (Retailer, Biller, …)
•   Exposes standardized APIs (TMF Open APIs, 3GPP SBIs, MEG APIs) at the border of each
    Functional block.
•   Enforces event based microservice architecture
•   Eliminates unnecessary bundling and functionality integration
•   Ensure reusability



                    1.2. Scope of ODA Functional Architecture
•   Normative Taxonomy of Business and Technology Functions
•   Standard Functionality of a Digital Enterprise business Functions
•   Standardized Core Business Processes for Functions (which can be extended by industry)
•   Structured use of Frameworx.
•   Technology neutral Features and Feature Grouping (using SID information
    Framework Definitions)


© TM Forum 2021. All Rights Reserved.                                   Page 9 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



That enables:
•   Business to define requirements using an unambiguous set of Functions (Leverage same
    language as Frameworx for consistency in expressing requirements and reuse of function
    specifications).
•   Creation of reusable Software component and specifications based on groupings of
    Functions
•   Simplified Management and Operations through well-defined decoupling and integration
    principles




© TM Forum 2021. All Rights Reserved.                                Page 10 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




2. The Functional Architecture of ODA
The ODA Function Blocks (below) define the key functional grouping that logically establish
related family of information systems objects. Through functional decomposition of the key
capabilities of a digital business/digital enterprise, the Functional Architecture establishes a
Level 0 Functional grouping that enables achieves business and operational agility.
The Functional Architecture is modeled to represent digital enterprise business operation,
using functions that correspond to the interactions that go beyond the traditional pipe-line
business model. Each of the ODA Function Blocks is an enterprise level group of functions with
a collection of coherent processes continuously performed to enable digital business.




Figure 2.1. ODA Functional Architecture - High Level view (Level 0)


As a Level-0 Functional Architecture, the Function Blocks can be used to quickly develop
various information systems operating models of a specific enterprise based on its mission -
while maintaining alignment integration to the overall vision of a digital enterprise.
Alternate View 1
An alternate view is provided in order to de-constrain the representation. The choice of view is
not mandatory. Members can choose to change the view to fit any specific use, but the core
standards must always remain consistent with the overarching principle - non-layered, the
existence of a decoupling and integration function bordering all adjacent functions.




© TM Forum 2021. All Rights Reserved.                                     Page 11 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Figure 2.2. ODA Functional Architecture - alternate view (Level 0)




© TM Forum 2021. All Rights Reserved.                                Page 12 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




3. ODA Systems of Separation
The functional view of ODA can be summarized in a system view based on the architectural
elements that deliver the system’s functionality. The view in Figure 3-1 below groups the ODA
function blocks into a system’s structure-including the key functional elements (Party
Management, Core Commerce Management, and Production), their responsibilities, which can
be used to summarize their roles, interfaces they expose, and the interactions between them.
Taken together, this shows how the responsibility of the systems and the functions required of
them.




Figure 3.1. Grouping of systems based on the Functional Architecture


Rationale of systems separation
Each of above defined system types has its own lifecycle :
•   Engagement Management:
    Responsible for user interactions that are powered by fast moving technologies, it is
    committed to evolve (e.g., in a quick & agile mode) in order to catch the trends on the
    fields of customer experience, ergonomics, social networking. These trends apply to all
    industries not only telecommunications, therefore, Service Providers have no control over
    them and must adapt quickly.




© TM Forum 2021. All Rights Reserved.                                  Page 13 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




•   Systems of Records
    Responsible for operational processes, it consists of assets (processes, objects and data)
    that are core to the stability of an enterprise.
•   Systems of Insight
    Responsible for knowledge-defined automation. It makes use of Big & Fast Data to enable
    cross-functional Intelligence functions and cognitive workflows.




© TM Forum 2021. All Rights Reserved.                                    Page 14 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




4. The Functional Blocks

                    4.1. Decoupling & Integration
                  4.1.1. Definition & Scope
The Decoupling & Integration (D&I) Block is about governing and managing separation of
functional borders based on well-established "families" of closely interrelated services as well
as the integration between them. D&I gathers non-business functions that are needed at
design and runtime to enable the combinations of services that the business requires.
The Decoupling & Integration Block ensures that services provided by ODA can be combined in
a flexible way, without restriction imposed by a process pattern derived from a given stack of
blocks.
Note: Where in traditional architectures functional layers are supposed to communicate only
with adjacent ones (e.g., BSS with OSS, OSS with Network but not BSS directly with Network).
"Decoupling" within ODA emphasizes that ODA Function Blocks are not behaving like layers
and tightly coupled together. This ensures that the functional architecture by itself doesn't
preclude any combination of services.

                  4.1.2. Functions of Decoupling & Integration
Core functionalities covered by the "Decoupling and Integration" aspect of the functional
architecture are outline in the table below.
Table 4-1. Decoupling & Integration key functionalities

#        Functionality       Description / Purpose
DI.001 Normalized            Catalog of API's - Management of API catalog and
       APIs                  documentations, including links to catalogs of partners
DI.002 Message               API Routing - Route API calls to endpoint, API Mediation
       Routing
         ...



                    4.2. Engagement Management
                  4.2.1. Definition & Scope
The Engagement Management (EGM) Block represents the interaction point between the
enterprise and its ecosystem, which can be through different channels for different
experiences. EGM provides the capabilities to assure a digital, secure and accurate interaction
of all these stakeholders, providing digital and omnichannel capabilities through the
configuration of the different journeys reusing the processes and functionalities provided by
the platform.
Its scope includes interactions between users and processes handled by other functions such
as from the Intelligence Management, Party Management, Core Commerce Management or
Production Blocks. “Users” from the perspective of EGM, may be machines and things (IoT



© TM Forum 2021. All Rights Reserved.                                    Page 15 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



context), humans (prospects, customers, users, employees, of people working on behalf of
partners and suppliers - 3rd parties) that collaborate and integrate their own solutions to the
ecosystem, providers of different services (retailers, salespeople, technical providers).

                  4.2.2. Engagement Management is characterized as:
•   Handling relationship between external and internal actors (including 3rd party systems,
    connected objects, …) and other ODA blocks.
•   Managing the presentation layer according to the channel, the device to allow multi and
    cross-channel user journeys over multiple types of devices.
•   Tailoring interactions using contextual information from back ends (360°view, process
    states).
•   Relying on Processes, Functions and Data stored in the other ODA blocks (this is what
    enables reuse, cross channel and multi device).
•   "Powering" customer / user journeys (what users see of the ongoing back end processes).
•   Holding no business process (eTOM), no functions (functional Framework) and no
    operational data (SID)
•   Holding technical functions – and data related to these functions and to their execution
    (context)
•   Interacting with other ODA blocks only through Event or Process APIs (new APIs -
    definition ongoing), or read data through current standard TMF Open API

                  4.2.3. Engagement Management Block functionalities
This is the list of standardized Engagement Management functionalities. As new standards
emerge, they will be updated into the table below.
Table 4-2. Functionalities provided by the Engagement Management Block include:

#         Functionality             Description / Purpose
EM.001 Front-ends (UIs)             Portals and application interfaces that are rendered for
                                    interactions.
EM.002 Journey                      Configure and adapt interactions to different types of
       Management                   Parties, Channels etc.
EM.003 Access to content            Access in read only to data contained in different
                                    repositories, according to Party rights. It can include
                                    access through Front-Ends or via APIs.
EM.004 Content                      Collects information from multiple internal and / or
       Aggregation                  external sources, including digital body language, and
                                    transcodes them for a single presentation format, storing
                                    document references.
EM.005 Content                      Classifies or categorizes data according to predefined
       Organization                 ranking plans




© TM Forum 2021. All Rights Reserved.                                     Page 16 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



#         Functionality             Description / Purpose
EM.006 Personalization of           Collects user’s preferences and personalization criteria.
       content                      Adapt contents and renders them based on context,
                                    user, interfaces, and according to user’s preferences and
                                    personalization criteria.
EM.007 Filtering of content Provides select capabilities for content based on
                            engagement context and criteria.
EM.008 Information                  Selective notification of information or alerts based on
       Services                     events (including social listening) towards the
                                    appropriate Actors, channel and device.
EM.009 User Interface               Defines, formats and structures the sequence of user
       Orchestration                interfaces (UIs) needed by a process.
EM.010 Integration                  Integrating internal systems/software/devices with
                                    external systems/software/devices - this includes social
                                    network platforms etc.
EM.011 API HUB                      Exposes standardized API to Partners and external
                                    systems. Manages security and checks Access right
                                    policies.
EM.012 Authentication and Correctly authenticates and authorizes a Party, including
       Authorization*     role management.
EM.013 User-interaction             Manage Party interactions with the different services
       lifecycle                    (provide consent, configure services, etc.) as well as their
       management*                  relationship with other users (create groups and share
                                    services)
*These functionalities are still under review for confirmation.

                  4.2.4. Open API's Mapping

#        Interface          Description/Purpose                                           Specification /
         Name                                                                             Reference
1        Process flow       Engagement management doesn’t have the right to Open API
                            Create, Delete, Update data. So, it cannot use the TMF701
                            current TMF Open APIs, which are CRUD operations
                            on data.
                            The Process flow API is defined to enable Systems of
                            Records and Intelligence to invoke kinematics in the
                            Engagement Management function.
2        Event                                                                            Open API
         Management                                                                       TMF688




© TM Forum 2021. All Rights Reserved.                                     Page 17 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



                    4.3. Party Management
                  4.3.1. Definition & Scope
The Party Management (PM) Block handles all interactions and data associated with entities or
actors that are involved or likely to get involved with the enterprise. Party roles and behaviors
are not dependent on industry specifics. This block includes support for identification
processes which are required to validate parties and management of Party relationships.
Party Management can be characterized as follows:
•   Party Management deals with "WHO" & "WHY"
•   It handles Persons and Organizations (called Party) involved in business processes. These
    Parties can be Customers, Business Partners or Employees.
•   In charge of Party oriented processes, functions and repositories such as:
             o    Party, Party Information and Privacy Management, Party Roles and Rights
                  Management
             o    Party Interaction Management
             o    Billing Account Management and Bill Production
             o    Party Financial Management activities : payment, bill inquiry, dunning, …
             o    Market and Party Strategy activities
             o    etc.
•   Party Management is not Telco specific, as any type of digital industry has now this kind of
    needs.

                  4.3.2. Business Processes in the Party Management Block
Party Management mapping is based on a tactical operating model with no categoric business
architecture underpinning it. This mapping is provided for informative purposes only, where
different Business Architecture shall have an influence on eventual mapping.




© TM Forum 2021. All Rights Reserved.                                       Page 18 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Business Process entities and their descriptions (Source GB921 R20.5)

Table 4-3. Party Management eTOM Process Descriptions

Process eTOM Process                         Category Brief Description
Identifier
1.1.1        Market Strategy & Policy (2) eTOM Enable the development of a strategic
                                      Process view of an enterprise’s existing and
                                      Type     desired market-place
1.1.2        Sales Strategy & Planning (2) eTOM Develop an appropriate sales strategy
                                       Process to complement the market strategy.
                                       Type
1.1.3        Sales Forecasting               (2) eTOM Sales Forecasting involves gathering
                                             Process current and historic order
                                             Type     information, analyzing sales trends
                                                      and patterns generating sales forecast
                                                      and analyzing historical and planned
                                                      promotions and events.
1.1.5        Sales Development               (2) eTOM Develop the Sales support and
                                             Process response for new and existing
                                             Type     products, as well as existing and
                                                      potential customers.
1.1.8        Sales Channel                   (2) eTOM This process element represents part
             Management                      Process of the overall enterprise, modeled in
                                             Type     business process terms, and can be
                                                      applied (i.e., “instantiated”) with
                                                      other similar process elements for
                                                      application within a specific
                                                      organization or domain.
1.1.9        Selling                         (2) eTOM Responsible for managing prospective
                                             Process customers, for qualifying and
                                             Type     educating customers, and matching
                                                      customer expectations
                                                       Managing prospective parties with
                                                       whom an enterprise may do business,
                                                       such as potential existing or new
                                                       customers and partners, for qualifying
                                                       and educating them, and ensuring
                                                       their expectations are met.
1.1.11       Contact/Lead/Prospect           (2) eTOM Develop the appropriate relationships
             Management                      Process with contacts, leads, and prospects
                                             Type     with the intent to convert them to
                                                      consumers, such as customers, or


© TM Forum 2021. All Rights Reserved.                                     Page 19 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                         Category Brief Description
Identifier
                                                       providers, such as partners, of an
                                                       enterprise's offerings.
1.1.14       Marketing                       (2) eTOM Develop and manage communications
             Communications and              Process to the market, prospective and
             Advertising                     Type     existing customers. Communications
                                                      involve both the message and the
                                                      media. Develop a message and
                                                      manage its delivery. Also develop and
                                                      manage interfaces with press/news
                                                      and manage an editorial calendar to
                                                      plan placements.
1.1.16       Brand Management                (2) eTOM Create a name, symbol or design that
                                             Process identifies and differentiates an
                                             Type     enterprise’s product offering and/or
                                                      offerings from its others product
                                                      offering(s) and similar offerings
                                                      available from other enterprises,
                                                      including competitors.
1.1.17       Market Research                 (2) eTOM Gathers, analyze and interpret
                                             Process information about a market, about
                                             Type     product offerings that will be made to
                                                      the market, and about the past,
                                                      present and potential customers for
                                                      the offering; Research the
                                                      characteristics, such as spending
                                                      habits and a target market’s
                                                      requirements, the industry as a whole,
                                                      and competitors.
1.3.2        Customer Experience             (2) eTOM Perform customer lifecycle mapping,
             Management                      Process assess customer experience maturity,
                                             Type     as well as analyze customer
                                                      experience metrics.
1.3.4        Customer Management             (2) eTOM Manage the relationship of the
                                             Process Customer and the enterprise.
                                             Type
1.3.5        Customer Interaction            (2) eTOM Manage interactions between the
             Management                      Process customer and the enterprise.
                                             Type     Interactions can be triggered by the
                                                      customer or by the enterprise




© TM Forum 2021. All Rights Reserved.                                     Page 20 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                         Category Brief Description
Identifier
1.3.6        Customer Information            (2) eTOM Manage customer information after
             Management                      Process customer contracts or associated
                                             Type     service orders have been finalized and
                                                      during the order completion phase.
                                                      Ensure that any customer information
                                                      required by other CRM processes is
                                                      updated as part of the customer order
                                                      completion.
1.3.9        Customer Bill Invoice           (2) eTOM Ensure the bill invoice is created,
             Management                      Process physically and/or electronically
                                             Type     produced and distributed to
                                                      customers, and that the appropriate
                                                      taxes, discounts, adjustments, rebates
                                                      and credits for the products and
                                                      services delivered to customers have
                                                      been applied.
1.3.10       Customer Bill Payments          (2) eTOM Ensure that enterprise revenue is
             & Receivables                   Process collected through pre-established
             Management                      Type     collection channels and put in place
                                                      procedures to recover past due
                                                      payments.
1.3.11       Customer Bill Inquiry           (2) eTOM Ensure the timely and effective
             Handling                        Process fulfillment of all customer bill inquiries
                                             Type     and complaints.
1.3.15       Customer Experience             (2) eTOM This set of processes will enable the
             Management Strategy             Process development
             and Planning                    Type     of a strategy and plan for how
                                                       customer experience management
                                                       would be incorporated into the who
                                                       organization.
1.3.16       Customer Inventory              (2) eTOM Establish, manage and administer the
             Management                      Process enterprise's customer inventory, as
                                             Type     embodied in the Customer Inventory
                                                      Database, and monitor and report on
                                                      the usage and access to the customer
                                                      inventory, and the quality of the data
                                                      maintained in it.
1.6.1        Party Strategy & Planning (2) eTOM Develop the strategies and policies of
                                       Process the enterprise for engagement with
                                       Type     other parties



© TM Forum 2021. All Rights Reserved.                                     Page 21 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                         Category Brief Description
Identifier
1.6.2        Party Tender                    (2) eTOM Party Tender Management processes
             Management                      Process manage the activities associated with
                                             Type     developing tender documents,
                                                      running tender processes, gaining
                                                      enterprise agreement to tender
                                                      decisions.
1.6.3        Party Relationship              (2) eTOM Manage the lifecycles of parties with
             Development &                   Process whom the enterprise has a
             Retirement                      Type     relationship. Relationship with new
                                                      parties may be required to broaden
                                                      the services an enterprise offers, to
                                                      improve performance, for outsourcing
                                                      and out-tasking requirements, and so
                                                      forth.
1.6.5        Party Agreement                 (2) eTOM Manage the evaluation of agreements
             Management                      Process with parties, including customers.
                                             Type     Initiate and complete business
                                                      agreements when one or more other
                                                      parties are involved.
1.6.7        Party Privacy                   (2) eTOM Manage the Privacy of Data Subject
             Management                      Process Party Information in accordance with
                                             Type     privacy regulations and the Data
                                                      Subject’s explicit wishes. Create and
                                                      define the Privacy Profile Type,
                                                      manage the definition of the Privacy
                                                      Profile with the Data Subject Party as
                                                      well as the evolution of this profile if
                                                      required, and ensure that the Data
                                                      Controller Party can demonstrate
                                                      compliance by itself and any other
                                                      Party.
1.6.9        Party Interaction               (2) eTOM Manage interactions between parties
             Management                      Process and the enterprise. Interactions can
                                             Type     be triggered by the enterprise (as a
                                                      result of a query or complaint) or by a
                                                      party (for example sending bills or
                                                      other notifications.)
1.6.13       Party Training and              (2) eTOM Assess an enterprise's training needs,
             Education                       Process design training plans, develop
                                             Type     training, conduct and evaluate
                                                      training and results.



© TM Forum 2021. All Rights Reserved.                                     Page 22 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                         Category Brief Description
Identifier
1.6.14       Party Special Event             (2) eTOM Plans, prepare, and produce a special
             Management                      Process event which targets one or more
                                             Type     types of parties. It includes the
                                                      assessment, definition, acquisition,
                                                      allocation, direction, control, and
                                                      analysis of time, finances, people,
                                                      products, services, and other
                                                      resources to achieve an event's
                                                      objectives.
1.6.15       Business Partner        (2) eTOM Manage the party bill/invoice process,
             Bill/Invoice Management Process control bills/invoices, manage the
                                     Type     lifecycle of bills/invoices, and perform
                                              bill/invoice trend analysis. A bill is a
                                              notice for payment which is supposed
                                              to be preceded by an invoice in most
                                              cases. An invoice typically does not
                                              summarize to total outstanding
                                              payment or payments due. A bill
                                              typically contains the payment due
                                              date and balance.
1.6.16       Business Partner Bill  (2) eTOM Party Bill Payments & Receivables
             Payments & Receivables Process Management is responsible for
             Management             Type     management of methods used by
                                             parties to make payments,
                                             administers payment plans, handles
                                             payments, and collects debt.
1.6.20       Business Partner Bill           (2) eTOM Ensure the timely and effective
             Inquiry Handling                Process resolution of all party bill inquiries and
                                             Type     complaints initiated by an enterprise
                                                      or initiated by another party, such as
                                                      partner.
1.6.21       Party Inventory                 (2) eTOM Manage the administration of the
             Management                      Process enterprise's party inventory.
                                             Type
1.X.Y        Party Identification &          (2) eTOM to be discussed for next versions
             Authentication                  Process
                                             Type




© TM Forum 2021. All Rights Reserved.                                     Page 23 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




                    4.3.3. Standard Business Information Entities
Below is a mapping of Frameworx SID ABEs to the Party Management functional block




Table 4-4. SID ABEs and their description (Source GB922 R20.5 )

SID            #       ABE                  ABE Definition
Domain
Market /       01      Market & Sales       Supports the business plans and strategies on how to
Sales                  Strategy and         address the market with appropriate products and
                       Plan                 channels.
               02      Market Segment Supports market segments, market statistics, and
                                      forecasts
               03      Competitor           Identifies other providers who compete in the same
                                            market segments, accumulates intelligence about the
                                            competitors, including products (price, Key
                                            Performance Indicators and so forth).
               04      Contact / Lead / Provides the ability to track sales leads through their
                       Prospect         life cycle up until the time the leads become
                                        customers, including lead and contact information,
                                        sales prospects, proposals made to potential
                                        customers, and the amount of potential revenue the
                                        leads represent in the form of a sales pipeline.
               05      Sales Channel        Keeps track of distribution channels and sales
                                            activities, sales quotas, sales, contests,
                                            commission/bonus plans, commissions/bonuses, and
                                            maintain groups of individuals that make up the sales
                                            force.



© TM Forum 2021. All Rights Reserved.                                    Page 24 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID            #      ABE                   ABE Definition
Domain
               06     Market Sales          Maintains market and sales forecasts, new service
                      Forecast              requirements, customer needs, and customer
                                            education.
               07     Market Sales          Market Sales Party Roles ABE contains all PartyRoles
                      Party Roles           related to the Market Sales Domain such as
                                            MarketingManager, SalesAgent...
Customer 01           Customer Party        The Customer Party Roles ABE is the focus on all the
                      Roles                 roles related to Customer.
               02     Customer              Represents communications with customers, and the
                      Interaction           translation of customer requests and inquiries into
                                            appropriate “events” such as the creation of a
                                            customer order, the creation of a customer bill
                                            inquiry, or the creation of a customer problem.
               03     Customer Bill         Handles real-time and non-real-time Call Detail
                                            Records (CDRs) and other sources of data that result
                                            in invoice items. The Customer Bill ABE also
                                            represents the format of a bill, schedule the
                                            production of bills, customer invoicing profiles, all
                                            the financial calculations necessary to determine the
                                            total of the bill (except for rating and rating
                                            discounts), and credits and adjustments to bills.
               04     Customer Bill         Handles credit violations, actions for overdue debts,
                      Collection            and facility billing audits.
               05     Customer Bill         Represents invoice inquiries associated with invoices
                      Inquiry               sent to customers and handles disputes and
                                            adjustments on individual charges, invoices, and
                                            accounts.
Business       01     Party Strategy & The strategies and the planning of the business
Partner               Plan             relation with the other parties with input from other
                                       ABEs, such as MarketSales, Party Performance and
                                       Competitor Analysis.
               02     Party                 A Party represents an individual or an organization,
                                            or an organization unit that are of interest, involved
                                            or that provide value directly or indirectly from an
                                            enterprise perspective (Enterprise is to be
                                            understood here as provider, service provider or
                                            operator). Hence, the Party plays one or more roles
                                            with the enterprise or with another Party playing a
                                            role with the enterprise (indirectly). This is



© TM Forum 2021. All Rights Reserved.                                     Page 25 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID            #      ABE                   ABE Definition
Domain
                                            introduced to specify that the only party an
                                            enterprise would be interested in and will consider in
                                            its systems is a party playing a role (directly or
                                            indirectly). Roles would be represented by the Party
                                            Role concept. Additional roles will be defined to
                                            cover the needs of the new digital ecosystem."
                                            Examples of roles played by Parties include those: •
                                            Of interest, such as competitors, sales prospects •
                                            Involved, such as customers, users, employees • That
                                            provides value directly or indirectly, such as service
                                            providers, operators, cloud brokers, infrastructure
                                            providers, application developers.
               03     Business Partner Additional Party Entities ABE represents entities that
                      Account          are similar to those in the Customer ABE, such as
                                       PartyAccount and Party Account Contact.
               04     Party Bill            (preliminary)
               05     Party Bill            The Party Bill Collection ABE handles credit
                      Collection            violations, actions for overdue debts (Dunning), and
                                            all what is related to PartyPayment.
               06     Business Partner Manages Partner roles and related information.
                      Party Roles
               07     Party Interaction Represents communications with parties, and the
                                        translation of requests and inquiries into appropriate
                                        "events" such as the creation of an order, the
                                        creation of a bill inquiry, or the creation of a
                                        problem.
               08     Party Privacy         Contains all entities used by the Party Privacy
                                            Management process for specifying the information
                                            concerned by Privacy rules, the Privacy rules
                                            themselves, and the choices made by Parties for
                                            their own Privacy.
Common 01             Communication The Communication Interaction ABE contains all
                      Interaction   entities needed for specifying a
                                    CommunicationInteraction describing an exchange of
                                    information during a communication between two or
                                    more human(s) and/or machine(s) during a period of
                                    time.




© TM Forum 2021. All Rights Reserved.                                    Page 26 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID            #       ABE                  ABE Definition
Domain
               02      Users and Roles Represents types of users and roles and their
                                       involvement in the usage of products, services and
                                       resources.
Enterprise 01          Enterprise Party Enterprise Party Roles ABE contains all PartyRoles
                       Roles            related to the Enterprise such as Employee,
                                        Employer, Regulator...
Product        01      Product Party        Product Party Roles ABE contains all PartyRoles
                       Roles                related to the Product Domain such as
                                            ProductManager
Service        01      Service Party        Service Party Roles ABE contains all PartyRoles
                       Roles                related to the Service Domain such as
                                            ServiceManager.
Resource 01            Resource Party       Resource Party Roles ABE contains all PartyRoles
                       Roles                related to the Resource Domain such as Technician,
                                            ResourceManager.

                    4.3.4. Standard Interfaces
List of Open APIs proposed to be provided by Party Management functional bloc.




© TM Forum 2021. All Rights Reserved.                                    Page 27 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Table 4-5. Proposed Standard Interfaces for Party Management block

#        Interface Name                               Purpose/Description Specification /
                                                                          Reference
1        Party Management API                                                  Open API TMF632
2        Customer Management API                                               Open API TMF629
3        Privacy Management API                                                Open API TMF644
4        Party Role Management API                                             Open API TMF669
5        Account Management API                                                Open API TMF666
6        Document Management API                                               Open API TMF667
7        Partnership Type Management API                                       Open API TMF668
8        Payment Method API                                                    Open API TMF670
9        Users Role & Permissions API                                          Open API TMF672
10       Payment Management API                                                Open API TMF676
11       Customer Bill Management API                                          Open API TMF678
12       Communication API                                                     Open API TMF681
13       Party Interaction Management API                                      Open API TMF683
14       Federated Identity API                                                Open API TMF691
15       Sales Management API                                                  Open API TMF699
16       Process Flow API                                                      Open API TMF701
17       Self-Care API Component Suite (Party                                  Open API TMF910
         information level)



                    4.4. Core Commerce Management
                  4.4.1. Definition & Scope
The Core Commerce Management (CCM) Block represents the part of the enterprise that is
concerned with enabling profitable exchange of goods and services. It includes all those
activities which directly or indirectly facilitate that exchange such as marketing & sales,
sourcing and procurement, strategic (buying & selling) portfolio plans (commercial rules), life-
cycle product management, offer management, new business development - for all types of
business engagements - B2B, B2C, C2C, B2B2X etc. It is responsible for formalizing business
models, revenue generation and business assurance processes.




© TM Forum 2021. All Rights Reserved.                                    Page 28 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Core Commerce Management can be characterized as follows:
•   Core Commerce Management deals with "WHAT"
•   It handles the catalogue of Product Offerings and Products marketed by the telco operator
    for all types of business (B2C, B2B, B2B2X, …)
•   Core Commerce Management is in charge of Product Offerings and Products Catalogue
    oriented processes, functions and repositories such as :
             o    Product Offerings and Products Catalogue Management
             o    Order Handling, from Order Capture & Configuration to the global
                  orchestration of the Customer Order Delivery
             o    Rating of any types of charges and Bill items Calculation
             o    Business Partners Revenue Sharing & Settlement
             o    Product Assurance
             o    Product Strategy activities
             o    Etc.
•   Core Commerce Management is independent from technical concerns - managed by
    Production – to be able to decouple commercial and technical evolution
Core Commerce Management Block functionalities

                  4.4.2. Business Processes in the Core Commerce Management Block
The Core Commerce Management Block mapping is based on a tactical operating model with
no categoric business architecture underpinning it. This mapping is provided for informative
purposes only, where different Business Architecture shall have an influence on eventual
mapping. This mapping is based on eTOM level 2 business processes.




© TM Forum 2021. All Rights Reserved.                                     Page 29 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Table 4-6. Core Commerce Management eTOM Process Descriptions (Source reference GB921 R20.5)

Process eTOM Process                    Category Brief Description
Identifier
1.1.5         Sales                     (2) eTOM Develop the Sales support and response for
              Development               Process new and existing products, as well as existing
                                        Type     and potential customers.
1.1.9         Selling                   (2) eTOM Responsible for managing prospective
                                        Process customers, for qualifying and educating
                                        Type     customers, and matching customer
                                                 expectations
                                                  Managing prospective parties with whom an
                                                  enterprise may do business, such as potential
                                                  existing or new customers and partners, for
                                                  qualifying and educating them, and ensuring
                                                  their expectations are met.
1.1.19        Loyalty Program (2) eTOM Define all aspects of a loyalty program, such
              Management      Process as requirements and objectives of a loyalty
                              Type     program, determine the benefits to
                                       participants. Develop a program, prototype it,
                                       test it, roll out/launch it, amend and evaluate
                                       it, and terminate it when it is no longer viable
                                       for an enterprise.
                                                  Manage all operational aspects of running a
                                                  loyalty program. Enable parties to become
                                                  members of a program, earn currency and
                                                  rewards, and redeem currency. Manage a
                                                  loyalty program account, leave a program,
                                                  and provide operational reports.
1.2.1         Product & Offer           (2) eTOM Develop strategies for products at the
              Portfolio                 Process portfolio level.
              Planning                  Type
1.2.2         Product & Offer           (2) eTOM Manage the delivery and build of new or
              Capability                Process changed Product & Offer and delivery
              Delivery                  Type     capabilities within an enterprise.
1.2.5         Product                   (2) eTOM Product Configuration involves specifying
              Configuration             Process how a Product operates or functions in terms
              Management                Type     of a product’s configurable properties and
                                                 features, collectively called characteristics,
                                                 and related products, services, and resources
                                                 that are used in its configuration.



© TM Forum 2021. All Rights Reserved.                                      Page 30 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                    Category Brief Description
Identifier
                                                   Specify how a product operates or functions
                                                   in terms of a product’s configurable
                                                   parameters, collectively called characteristics,
                                                   and related configurations of products,
                                                   services, and resources that are part of its
                                                   overall configuration. The configuration for a
                                                   product, which is also managed by this
                                                   process, is governed by a selected product
                                                   configuration specification.
1.2.7         Product                   (2) eTOM Develop and deliver new product
              Specification &           Process specifications as well as enhancements and
              Offering                  Type     new features, ready for use by other
              Development &                      processes, including Product Offering
              Retirement                         Development & Retirement.
                                                   Develop and deliver new product offerings,
                                                   their pricing, as well as catalogs that contain
                                                   both.
1.2.8         Product Capacity (2) eTOM Specify available product capacity and
              Management       Process capture product capacity demand for defined
                               Type     time periods. The consumption of available
                                        capacity by demand is captured for a given
                                        time period.
1.2.9         Product Offering (2) eTOM Make an inbound/outbound purchase of one
              Purchasing       Process or more product offerings, change an offering
                               Type     being purchased, review an entire purchase,
                                        and other processes that manage the lifecycle
                                        of a purchase of one or more product
                                        offerings.
1.2.11        Product                   (2) eTOM Establish, manage and administer the
              Inventory                 Process enterprise's product inventory, as embodied
              Management                Type     in the Product Inventory repository, and
                                                 monitor and report on the usage and access
                                                 to the product inventory, and the quality of
                                                 the information maintained in it.
1.2.15        Product Test              (2) eTOM Product Test Management provides the
              Management                Process manages the end-to-end execution of a test
                                        Type     or test scenario for products not specific to a
                                                 customer.




© TM Forum 2021. All Rights Reserved.                                        Page 31 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                    Category Brief Description
Identifier
1.2.16        Product Usage             (2) eTOM Encompasses the functions required to guide,
              Management                Process distribute, mediate, summarize, accumulate,
                                        Type     and analyze Product Usage records.
1.2.17        Product Rating & (2) eTOM Rate a value (monetary or other) to a Product
              Rate Assignment Process Usage or a set of Product Usages and assign
                               Type     the result to a Product and a Billing Account.
1.2.18        Product Balance (2) eTOM Management of Product balances.
              Management      Process
                              Type
1.3.3         Customer Order (2) eTOM Responsible for accepting and issuing orders.
              Handling       Process
                             Type
1.3.7         Customer                  (2) eTOM Responsible for receiving trouble reports
              Problem                   Process from customers, resolving them to the
              Handling                  Type     customer’s satisfaction and providing
                                                 meaningful status on repair and/or
                                                 restoration activity to the customer.
1.3.8         Customer                  (2) eTOM Monitoring, managing and reporting of
              QoS/SLA                   Process delivered vs. contractual Quality of Service
              Management                Type     (QoS), as defined in the enterprise’s service
                                                 descriptions, customer contracts or product
                                                 catalogue.
1.6.4         Party Offering            (2) eTOM Manage on-boarding and off-boarding
              Development &             Process another party's product specifications and
              Retirement                Type     product offerings that a required to facilitate
                                                 the business model of the enterprise.
1.6.5         Party Agreement (2) eTOM Manage the evaluation of agreements with
              Management      Process parties, including customers. Initiate and
                              Type     complete business agreements when one or
                                       more other parties are involved.
1.6.8         Party Order               (2) eTOM Track, monitor and report on an order to
              Handling                  Process another party to ensure that the interactions
                                        Type     are in accordance with the agreed
                                                 commercial agreements with the other party.
1.6.10        Party Problem             (2) eTOM Ensure the timely and effective resolution of
              Handling                  Process all party problems initiated by an enterprise
                                        Type     or initiated by another party, such as a
                                                 partner.



© TM Forum 2021. All Rights Reserved.                                      Page 32 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                    Category Brief Description
Identifier
1.6.14        Party Special             (2) eTOM Plans, prepare, and produce a special event
              Event                     Process which targets one or more types of parties. It
              Management                Type     includes the assessment, definition,
                                                 acquisition, allocation, direction, control, and
                                                 analysis of time, finances, people, products,
                                                 services, and other resources to achieve an
                                                 event's objectives.
1.6.18        Party Revenue             (2) eTOM Develops party revenue sharing models,
              Sharing and               Process prepare party revenue sharing agreements,
              Settlements               Type     determine party revenue shares, and
                                                 reconcile party revenue shares.


                  4.4.3. Standard Business Information Objects
Below is a mapping of Frameworx SID ABEs to the Core Commerce Management functional
block




© TM Forum 2021. All Rights Reserved.                                       Page 33 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Table 4-7. SID ABEs and their description (Source GB922 R20.5)

SID           #       SID ABE             ABE Definition
Domain
Customer 01           Customer            Handles single customer orders and the various types
                      Product Order       thereof, such as regulated and non-regulated orders.
                      ABE
              02      Customer            Focuses on technical assistance and problem handling
                      Problem ABE         for customers.
              03      Customer SLA        Is a special case of the Service Level Agreement ABE
                      ABE                 where an involved party in the agreement is a
                                          Customer. See the Agreement ABE in the Engaged
                                          Party Domain for details.
              04      Applied          Deals with the correlation of related usage for
                      Customer         subsequent rating, rates applied to the usage (both
                      Billing Rate ABE regulated and non-regulated), discounts to usage, and
                                       any taxes due on the rated usage.
Product       01      Product ABE         Represents an instance of a product offering
                                          subscribed to by a party, such as a customer, the place
                                          where the product is in use, as well as configuration
                                          characteristics, such as assigned telephone numbers
                                          and internet addresses. The Product ABE also tracks
                                          the services and/or resources through which the
                                          product is realized.
              02      Product             Contains all what represent a product specification as
                      Specification       perceived by the business user and specifies what the
                      ABE                 marketing operator wants to sell at a functional level
                                          (i.e., what are the capacities, which usages are
                                          available…).
              03      Strategic           Is concerned with the plans of the product portfolio,
                      Product             which product offerings to make available to each
                      Portfolio Plan      market segment and the plans to develop and deploy
                      ABE                 product offerings, as well as retirement of products
              04      Product             Describes tangible and intangible goods made available
                      Offering ABE        for a certain price to the market in the form of product
                                          catalogs. This ABE is also responsible for targeting
                                          market segments based on the appropriate market
                                          strategy.
              05      Product Usage Represents usage of products associated with
                      ABE           Customers used for charging that may appear on a
                                    Customer Bill.




© TM Forum 2021. All Rights Reserved.                                    Page 34 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID           #       SID ABE             ABE Definition
Domain
              06      Product             The definition of how a Product operates or functions
                      Configuration       in terms of CharacteristicSpecification(s) and related
                      ABE                 ResourceSpec(s), ProductSpec(s), ServiceSpec(s) as
                                          well as a representation of how a Product operates or
                                          functions in terms of characteristics and related
                                          Resource(s), Product(s), Service(s).
              07      Loyalty ABE          A loyalty program is one of the tools used by the
                                          loyalty process to retain customers. The Loyalty ABE
                                          contains all entities useful to specify and instantiate
                                          loyalty programs. A LoyaltyProgramProdSpec defines
                                          the LoyaltyRules that have to be checked in order to
                                          identify the actions to apply. Depending on the type of
                                          LoyaltyRules a LoyaltyAccount might be needed to
                                          collect gains or not. A LoyaltyProgramProduct is a type
                                          of ProductComponent and described by a
                                          LoyaltyProgramProdSpec.
              08      Product Test        A product test is a function performed on a product
                      ABE                 that results in measures being produced that reflect
                                          the functioning of the entity under test.
Business 01           Party Problem       Focuses on technical assistance and problem handling
Partner               ABE                 reported to and by other parties.
              02      Business        Contains all entities required to specify a
                      Partner Product communication used to procure or update one or
                      Order ABE       many Products in the context of a ProductOffering.
              03      Party Product Represents the involvement parties playing roles have
                      Specification & with ProductSpecifications and Product Offerings, such
                      Offering ABE    as ordered from and billed by.
              04      Party Revenue Party Revenue ABE is composed of revenue sharing
                      Settlement    and settlements.
              05      Party Service       Party Service Level Agreement ABE represents an SLA
                      Level               with one or more other parties. See the Agreement
                      Agreement           ABE for additional details.
              06      Applied Party       (Preliminary - Ongoing study)
                      Billing Rate
Common 01             Agreement ABE Represents a contract or arrangement, either written
                                    or verbal and sometimes enforceable by law, such as a
                                    service level agreement or a customer price
                                    agreement. An agreement involves a number of other



© TM Forum 2021. All Rights Reserved.                                     Page 35 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID           #       SID ABE             ABE Definition
Domain
                                          business entities, such as products, services, and
                                          resources and/or their specifications.
              02      Capacity ABE        A generalized ABE and specializations that provide
                                          capacity and capacity demand for products, services
                                          and resources

                   4.4.4. Standard Interfaces




Table 4-8. Standard Interfaces in the Core Commerce block

# Interface Name                                Purpose/Description Specification / Reference
1 Product Catalog Management API                                    Open API TMF620
2 Trouble Ticket API                                                Open API TMF621
3 Product Ordering API                                              Open API TMF622
4 SLA Management API                                                Open API TMF623
5 Product Inventory Management                                      Open API TMF637
  API
6 Quote Management API                                              Open API TMF648
7 Agreement Management API                                          Open API TMF651
8 Loyalty Management API                                            Open API TMF658
9 Shopping Cart API                                                 Open API TMF663
10 Promotion API                                                    Open API TMF671



© TM Forum 2021. All Rights Reserved.                                    Page 36 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



# Interface Name                              Purpose/Description Specification / Reference
11 Product Offering Qualification API                                Open API TMF679
12 Process Flow API                                                  Open API TMF701
13 Self-Care API Component Suite                                     Open API TMF910
   (Core Commerce information
   level)
14 Test API Component Suite                                          Open API TMF913
   (Product level)                                                   (includes TMF704 to
                                                                     TMF710)



                    4.5. Production
                  4.5.1. Definition & Scope
The Production Block is responsible for the delivery and lifecycle management of Customer
Facing Services (CFS) and Resource Facing Services (RFS) regardless of the technology type
(e.g., physical, virtual, connectivity, end point, etc.) or the operational domain or factory
where it originates, including third parties.
The Production Block exposes its service capabilities in a way that is commonly known as
Network as a Service (NaaS) for consumption by other ODA function blocks. For example, the
Core Commerce Management Block uses them to create products and offers, while the
Engagement Management Block uses them to allow customers to recharge their balance or
order a new video on demand. The Production block may also expose devices (e.g.,
smartphone) and application capabilities (e.g., email).
The scope of the Production block includes the exposure of its service capability definitions
and the dynamic run-time decision of how the service(s) supporting Products and Customer
will be created, delivered, used, maintained, assured, and repaired. It provides end-to-end
management of operational functions for services and resources to support the commercial
success of the ecosystem - including activities that span multiple enterprises such as the
management of installation, deployment, and operations of technologies, performance and
quality.
The Production Block does not need to know the details of a product nor the customer,
contract owner, or payer requesting its exposed service capabilities. It assumes responsibility
for the delivery of the CFS/RFS, as well as for operating the usage functions up to a committed
quality of service - including applying policy control and balance management and supplying
the Core Commerce Management Block with usage data records to perform rating on offers.
Production can be characterized as follows:
•   Production deals with "HOW "
•   Production is in charge of Services and Resources oriented processes, functions and
    repositories such as:
             o    Definition and lifecycle of the telco capabilities that can be exposed as Services
                  (CFS) to define Products and Offers to commercialize (in Core Commerce
                  Management)



© TM Forum 2021. All Rights Reserved.                                      Page 37 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



             o    Definition and lifecycle of the technical solutions available for these services
                  (RFS), based on all type of technology (physical, virtual, …) or all network,
                  service platforms, IT systems, … capabilities, directly managed by the telco
                  operator or available by means of a Business Partner
             o    Infrastructure Deployment and Operations management
             o    Delivery of services and resources
             o    Usage of services, including usage control and real-time balance management
             o    Problem and Performance Management
             o    Service & Resource Strategy activities
             o    etc.
Business Processes in the Production Function
The Production Block's business processes are based on a tactical operating model with no
business architecture lock-in.
The business processes are derived from eTOM level 2 business process elements. The
processes descriptions are derived from the following eTOM Groupings: Service Development
and Management, Service Management and Operations, Resource Development and
Management and Resource Management and Operations




Table 4-9. Production Standardized Business Process descriptions (Source reference GB921 R20.5)

Process eTOM Process                            Category Brief Description
Identifier
1.4.1        Service Strategy & Planning (2) eTOM Enable the development of a
                                         Process strategic view and a multi-year
                                         Type     business plan for the enterprise’s
                                                  services and service directions, and




© TM Forum 2021. All Rights Reserved.                                       Page 38 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                            Category Brief Description
Identifier
                                                          the parties who will supply the
                                                          required services.
1.4.2        Service Capability Delivery (2) eTOM Plan and deliver the total capabilities
                                         Process required to deliver changes to
                                         Type     service.
1.4.3        Service                  (2) eTOM Develop and deliver new or
             SpecificationDevelopment Process enhanced service types.
             & Retirement             Type
1.4.4        SM&O Support &                     (2) eTOM Manage service infrastructure,
             Readiness                          Process ensuring that the appropriate
                                                Type     service capacity is available and
                                                         ready to support the SM&O
                                                         Fulfillment, Assurance and Billing
                                                         processes
1.4.5        Service Configuration &            (2) eTOM Allocation, implementation,
             Activation                         Process configuration, activation and testing
                                                Type     of specific services to meet
                                                         customer requirements.
1.4.6        Service Problem                    (2) eTOM Respond immediately to customer-
             Management                         Process affecting service problems or failures
                                                Type     in order to minimize their effects on
                                                         customers, and to invoke the
                                                         restoration of the service, or provide
                                                         an alternate service as soon as
                                                         possible.
1.4.8        Service Guiding &                  (2) eTOM Manage usage events by correlating
             Mediation                          Process and formatting them into a useful
                                                Type     format as well as guiding them to an
                                                         appropriate service.
1.4.10       Service Test Management (2) eTOM Service Test Management provides
                                     Process the manages the end-to-end
                                     Type     execution of a test or test scenario
                                              for Services not related to a specific
                                              customer’s product.
1.5.2        Resource Capability                (2) eTOM Use the capability definition or
             Delivery                           Process requirements to deploy new and/or
                                                Type     enhanced technologies and
                                                         associated resources.




© TM Forum 2021. All Rights Reserved.                                    Page 39 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                            Category Brief Description
Identifier
1.5.3        Resource                 (2) eTOM Develop new, or enhance existing
             SpecificationDevelopment Process technologies and associated
             & Retirement             Type     resource types, so that new Services
                                               can be developed.
1.5.4        RM&O Support &                     (2) eTOM Manage resource infrastructure to
             Readiness                          Process ensure that appropriate application,
                                                Type     computing and network resources
                                                         are available and ready to support
                                                         the Fulfillment, Assurance and Billing
                                                         processes in instantiating and
                                                         managing resource instances, and
                                                         for monitoring and reporting on the
                                                         capabilities and costs of the
                                                         individual FAB processes.
1.5.5        Workforce Management               (2) eTOM Managing the staff performing
                                                Process manual activities along with
                                                Type     managing the actual activity being
                                                         performed.
                                                          "Note: The current focus of the
                                                          Manage Workforce processes is field
                                                          Staff and others managed through
                                                          work orders, etc. There is
                                                          opportunity for further study in
                                                          subsequent releases of eTOM,
                                                          including:
                                                          •   types and positioning of
                                                              workforce (field technicians,
                                                              services representatives, etc.),
                                                          •   other enterprise activities and
                                                              other management of staff,
                                                          •   decomposition and
                                                              normalization considering
                                                              information being acted on.
1.5.6        Resource Provisioning              (2) eTOM Allocation, installation,
                                                Process configuration, activation and testing
                                                Type     of specific resources to meet the
                                                         service requirements, or in response
                                                         to requests from other processes to
                                                         alleviate specific resource capacity




© TM Forum 2021. All Rights Reserved.                                     Page 40 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process                            Category Brief Description
Identifier
                                                          shortfalls, availability concerns or
                                                          failure conditions.
1.5.7        Resource Data Collection & (2) eTOM Collect and/or distribute
             Distribution               Process management information and data
                                        Type     records between resource and
                                                 service instances and other
                                                 enterprise processes.
1.5.8        Resource Trouble                   (2) eTOM Responsible for the management of
             Management                         Process troubles with specific resources.
                                                Type
1.5.10       Resource Mediation &               (2) eTOM Manage resource events by
             Reporting                          Process correlating and formatting them into
                                                Type     a useful format.
1.5.12       Resource Test                      (2) eTOM Resource Test Management
             Management                         Process provides the manages the end-to-
                                                Type     end execution of a test or test
                                                         scenario for Resources not specific
                                                         to a customer’s product.
1.X.Y        Service Balance                    (2) eTOM to be discussed for next versions
             Management                         Process
                                                Type


                  4.5.2. Standard Business Information Objects
Below is SID ABEs for core Production function block




© TM Forum 2021. All Rights Reserved.                                     Page 41 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Table 4-10. SID ABEs and their description (extract from GB922 20.5)

SID           #       SID ABE            ABE Definition
Domain
Service       01      Service ABE        Contains entities that are used to represent both customer-
                                         facing and resource-facing types of services. Entities in this
                                         ABE provide different views to examine, analyze, configure,
                                         monitor and repair Services of all types. Entities in this ABE
                                         are derived from Service Specification entities.
              02      Service Order Contains entities that represent a type of Request that
                      ABE           decomposes a Customer Order's products into the services
                                    associated with a ServiceOrder through which the products
                                    are realized.
              03      Service            Contains entities that define the shared characteristics of
                      Specification      both types of Service entities. This enables multiple
                      ABE                instances to be derived from a single specification entity. In
                                         this derivation, each instance will use the characteristics
                                         defined in its associated specification. Entities in this ABE
                                         focus on adherence to standards, distinguishing features of a
                                         Service, dependencies (both physical and logical, as well as
                                         on other services), quality, and cost. In general, entities in
                                         this ABE enable Services to be bound to Products and run
                                         using Resources. Network services are one example of
                                         Services that can be built. Additional examples include
                                         installation, maintenance, monitoring, and content
                                         authentication, authorization, accounting, and auditing
                                         functions.
              04      Service            Contains entities that are used to address the need for
                      Strategy &         enhanced or new Services, as well as the retirement of
                      Plan ABE           existing Services, by the enterprise. These entities have a
                                         strong dependency to both entities in the Resource and
                                         Product domains. Resulting efforts, such as deciding what
                                         Resources to use to host a Service, or what Services are used
                                         to support new Product Specifications, are also supported,
                                         as are service demand forecasts.
              05      Service       The definition of how a Service operates or functions in
                      Configuration terms of CharacteristicSpecification(s) and related
                      ABE           ResourceSpec(s) and ServiceSpec(s) as well as a
                                    representation of how a Service operates or functions in
                                    terms of characteristics and related Resource(s) and
                                    Service(s).




© TM Forum 2021. All Rights Reserved.                                     Page 42 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID           #       SID ABE            ABE Definition
Domain
              06      Service Usage Collects Service consumption data, and generates Service
                      ABE           usage records, for use by other business entities. The
                                    entities in this ABE provide physical, logical, and network
                                    usage information.
              07      Service            Manages faults, alarms, and outages from a Service point-of-
                      Problem ABE        view. This is then correlated to trouble tickets, regardless of
                                         whether the cause is physical or logical. Other entities in this
                                         ABE are used to direct the recovery from each of these three
                                         types of problems. They provide the ability to associate
                                         Resource faults and alarms to degradation and outages of
                                         Services that run on those Resources. These functions are
                                         independent of the Resources and technologies used to
                                         build the Service. A third set of entities in this ABE is used to
                                         differentiate between customer-reported problems and
                                         network-induced problems.
              08      Service Test       A function performed on a service that results in measures
                      ABE                being produced that reflect the functioning of the entity
                                         under test.
Resource 01           Resource ABE Contains entities that are used to represent the various
                                   aspects of a Resource. This includes four sets of entities that
                                   represent: the physical and logical aspects of a Resource;
                                   show how to aggregate such resources into aggregate
                                   entities that have physical and logical characteristics and
                                   behavior; and show how to represent networks, sub-
                                   networks, network components, and other related aspects
                                   of a network.
              02      Resource           Contains entities related to the business interaction orders.
                      Order ABE
              03      Resource           Contains entities that define the shared characteristics and
                      Specification      behavior of each of the four types of Resource entities. This
                      ABE                enables multiple instances to be derived from a single
                                         specification entity. In this derivation, each instance will use
                                         the shared characteristics and behavior defined in its
                                         associated template.
              04      Resource     Contains entities that define physical, logical, and network
                      Topology ABE topological information. This information is critical for
                                   assessing the current state of the network, as well as
                                   providing information on how to fix problems, tune
                                   performance, and in general work with the network (both as
                                   a whole and with its components). Each of these topological
                                   views provides its own physical, logical, or network related


© TM Forum 2021. All Rights Reserved.                                      Page 43 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID           #       SID ABE            ABE Definition
Domain
                                         information that can be used to manage one or more layers
                                         in a layered network.
              05      Resource      The definition of how a Resource operates or functions in
                      Configuration terms of CharacteristicSpecification(s) and related
                      ABE           ResourceSpec(s), as well as a representation of how a
                                    Resource operates or functions in terms of characteristics
                                    and related Resource(s).
              06      Resource           Collects Resource consumption data, and generates
                      Usage ABE          Resource usage records, for use by other business entities.
                                         The entities in this ABE provide physical, logical, and network
                                         usage information.
              07      Resource           Is used to plan networks and resource elements both initially
                      Strategy &         and for growth. It will coordinate both logical and physical
                      Plan ABE           resource growth. Inputs are budgets from business sources,
                                         service forecasts, current and projected network utilization,
                                         new technologies, and retiring technologies. It handles the
                                         lifecycle (installation, modification, removal, and retirement)
                                         for both logical and physical resources.
              08      Resource           Manages problems found in allocated resource instances,
                      Trouble ABE        regardless of whether the problem is physical or logical.
                                         Entities in this ABE detect these problems, act to determine
                                         their root cause, resolve these problems and maintain a
                                         history of the activities involved in diagnosing and solving
                                         the problem. Detecting problems can be done via software
                                         (e.g., responding to an alarm) and/or by hardware (e.g., a
                                         measurement or probe) and/or manually (e.g., visual
                                         inspection). This includes tracking, reporting, assigning
                                         people to fix the problem, testing and verification, and
                                         overall administration of repair activities.
              09      Resource Test Contains entities that are used to test PhysicalResources,
                      ABE           LogicalResources and CompoundResources. These entities
                                    are usually invoked during installation, as a part of trouble
                                    diagnosis or after trouble repair has been completed.
Enterprise 01         Workforce ABE Represents dispatched Field Force Management - human
                                    and other field resource with their roles, skills, calendars and
                                    other characteristics. Also, models work orders, catalog of
                                    work descriptions, various schedules, as well as reservation
                                    and assignment of a technician to a task
Common 01             Topology ABE The Topology ABE contains entities that are used to
                                   represent topological concepts that can be used to model a


© TM Forum 2021. All Rights Reserved.                                    Page 44 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID           #       SID ABE            ABE Definition
Domain
                                         large variety of topological relations between entities
                                         ranging from dependencies to connectivity.
              02      Location ABE       The Location ABE represents the site or position of
                                         something, such as a customer’s address, the site of
                                         equipment where there is a fault and where is the nearest
                                         person who could repair the equipment, and so
                                         forth. Locations can take the form of coordinates and/or
                                         addresses and/or physical representations


                   4.5.3. Standardized Interfaces




© TM Forum 2021. All Rights Reserved.                                    Page 45 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Table 4-11. Standard Interfaces in the Production block

#        Interface Name                                   Purpose /           Specification /
                                                          Descriptions        Reference
                                              Service related:
01       Service Catalog API                                                  Open API TMF633
02       Service Inventory Management API                                     Open API TMF638
03       Activation and configuration API                                     Open API TMF640
04       Service Ordering Management API                                      Open API TMF641
05       Service Qualification API                                            Open API TMF645
06       Service Test Management API                                          Open API TMF653
07       Service Problem Management API                                       Open API TMF656
08       Service Quality Management API                                       Open API TMF657
                                             Resource related:
01       Resource Catalog Management API                                      Open API TMF634
02       Resource Inventory Management API                                    Open API TMF639
03       Resource Ordering Management API                                     Open API TMF652
04       Resource Function Activation and                                     Open API TMF664
         Configuration API
05       Resource Pool Management API                                         Open API TMF685
06       Resource Activation and Configuration                                Open API TMF702
         API
                               Common API's for Service and Resource:
01       Trouble Ticket API                                                   Open API TMF621
02       SLA Management API                                                   Open API TMF623
03       Usage Management API                                                 Open API TMF635
04       Alarm Management API                                                 Open API TMF642
05       Appointment API                                                      Open API TMF646
06       Prepay Balance Management API                                        Open API TMF654
07       Change Management API                                                Open API TMF655
08       Geographic Address Management API                                    Open API TMF673


© TM Forum 2021. All Rights Reserved.                                    Page 46 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



#        Interface Name                                Purpose /             Specification /
                                                       Descriptions          Reference
09       Geographic Site Management API                                      Open API TMF674
10       Geographic Location Management API                                  Open API TMF675
11       Usage Consumption Management API                                    Open API TMF677
12       Shipment Tracking API                                               Open API TMF684
13       Stock Management                                                    Open API TMF687
14       Process Flow API                                                    Open API TMF701
15       IOT Device Management API Component                                 Open API Suite
         Suite                                                               TMF908
16       NaaS API Component Suite                                            Open API Suite
                                                                             TMF909
17       Test API Component Suite                                            Open API Suite
                                                                             TMF913
18       IOT Service Management API Component                                Open API Suite
         Suite                                                               TMF914



                    4.6. Intelligence Management
Definition and Scope
Analytical processes use operational data (reference data) and events produced by operational
processes or captured from the environment during an interaction with the enterprise (for
instance, events related to the activity of a user on a portal, events generated by operating
connected object or devices).
Analytical processes use operational data along with events received from operational
processes to produce analyses, correlations and aggregations that yield a representation of
operational reality. Analytical processes encompass activity or budget follow-up, as well as
revenue assurance or fraud detection, based on traffic analysis.
Analytical processes can use very large amounts of data and in turn produce their own data
(e.g., all kinds of KPI) for which they are entirely responsible and which they may make
available to other systems (either for display, or as input data for further processing).
Therefore, analytical processes are distinct from operational processes but interact with them
through event exchanges and data sharing. Big and Fast data capabilities are expected to
further develop such interactions and enhance operational processes.




© TM Forum 2021. All Rights Reserved.                                   Page 47 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




                  4.6.1. Business Processes in the Intelligence Management Block
Based on the figure below, eTOM level 2 are identified as "split into 2" when they manage SID
ABEs that are mapped to different ODA functional blocks.




The Intelligence Management process descriptions (Source GB921 R20.5)


Table 4-12. Intelligence Management eTOM Process descriptions

Process eTOM Process Category Brief Description
Identifier
1.1.7        Market Sales        (2) eTOM Market Sales Support & Readiness processes ensure
             Support &           Process the support capability is in place to allow the CRM
             Readiness           Type     Fulfillment, Assurance and Billing processes to
                                          operate effectively.
1.1.12       Market              (2) eTOM Market Performance Involves managing, tracking,
             Performance         Process monitoring, analyzing, improving and reporting on
             Management          Type     the performance of market key performance
                                          indicators
1.1.13       Sales               (2) eTOM Sales Performance Management managing, tracking,
             Performance         Process monitoring, analyzing, improving and reporting on
             Management          Type     the performance of specific sales key performance
                                          indicators that can be defined for certain levels, such
                                          as sales channels, organizations, and so forth.
1.1.15       Marketing           (2) eTOM Develop a marketing campaign through a
             Campaign            Process coordinated series of steps that can include
             Management          Type     promotion of a product through different mediums
                                          (television, radio, print, online) using a variety of


© TM Forum 2021. All Rights Reserved.                                       Page 48 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process Category Brief Description
Identifier
                                              different types of advertisements to reach the
                                              market, customers and channels.
1.2.4        Product             (2) eTOM Product Support processes ensure the support
             Support             Process capability is in place to allow the CRM Fulfillment,
                                 Type     Assurance and Billing processes to operate
                                          effectively.
1.2.6        Product             (2) eTOM Manage, track, monitor, analyze, improve, and
             Performance         Process report on the performance of specific products.
             Management          Type
1.2.13       Product Test        (2) eTOM Product Test Quality Analysis manages a quality
             Quality             Process Analysis on Tests to continually tweak and improve
             Analysis            Type     it.
1.3.1        Customer            (2) eTOM Customer Support processes ensure the support
             Support             Process capability is in place to allow the CRM Fulfillment,
                                 Type     Assurance and Billing processes to operate
                                          effectively.
1.3.2        Customer            (2) eTOM Perform customer lifecycle mapping, assess
             Experience          Process customer experience maturity, as well as analyze
             Management          Type     customer experience metrics.
1.4.4        SM&O Support (2) eTOM Manage service infrastructure, ensuring that the
             and Readiness Process appropriate service capacity is available and ready to
                           Type    support the SM&O Fulfillment, Assurance and Billing
                                   processes
1.4.7        Service Quality (2) eTOM Managing, tracking, monitoring, analyzing,
             Management Process improving and reporting on the performance of
                             Type     specific services
1.4.11       Service Test        (2) eTOM Service Test Quality Analysis manages a quality
             Quality             Process Analysis on Tests to continually tweak and improve
             Analysis            Type     it.
1.5.4        RM & O              (2) eTOM Manage resource infrastructure to ensure that
             Support and         Process appropriate application, computing and network
             Readiness           Type     resources are available and ready to support the
                                          Fulfillment, Assurance and Billing processes in
                                          instantiating and managing resource instances, and
                                          for monitoring and reporting on the capabilities and
                                          costs of the individual FAB processes. (Ongoing
                                          Study)




© TM Forum 2021. All Rights Reserved.                                    Page 49 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



Process eTOM Process Category Brief Description
Identifier
1.5.9        Resource            (2) eTOM Managing, tracking, monitoring, analyzing,
             Performance         Process controlling and reporting on the performance of
             Management          Type     specific resources
1.5.13       Resource Test (2) eTOM Resource Test Quality Analysis manages a quality
             Quality       Process Analysis on Tests to continually tweak and improve
             Analysis      Type     it.
1.6.6        Party Support (2) eTOM Party Support processes are responsible for ensuring
                           Process that all necessary facilities related to the interaction
                           Type     with other parties are ready and functioning.
                                    Moreover, these processes are responsible for the
                                    resolution of problems related to these facilities.
                                    (Ongoing Study)
1.6.11       Party               (2) eTOM Track, monitor and report on performance to ensure
             Performance         Process that the interactions are in accordance with the
             Management          Type     agreed commercial arrangements between the
                                          service provider and another party.


                  4.6.2. Standard Business Information Objects




© TM Forum 2021. All Rights Reserved.                               Page 50 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




Table 4-13. SID ABEs and their description (extract from GB922 20.5)

SID                    #        ABE               ABE Definition
Domain
Market /               01       Marketing         Supports marketing new or existing product offerings to
Sales                           Campaign          identified target markets. For example, the launch of a
                                ABE               pre-paid product with multiple promotions across
                                                  distribution channels, market segments and so forth; a
                                                  new campaign for an existing product; a re-launch of a
                                                  campaign for an existing product.
                       02       Market Sales Maintains sales forecasts, new service requirements,
                                Statistics ABE customer needs, and customer education, as well as
                                               calculating key performance indicators about Sales &
                                               Marketing revenue and sales channel performance.
Customer               01       Customer          Represents the analysis of customer usage patterns,
                                Statistic ABE     customer profitability statistics and churn and retention
                                                  statistics.
Product                01       Product     Handles product performance goals, the results of end-
                                Performance to-end product performance assessments, and the
                                ABE         comparison of assessments against goals. The results
                                            may include the identification of potential capacity
                                            issues.
Service                01       Service     Collects, correlates, consolidates, and validates various
                                Performance performance statistics and other operational
                                ABE         characteristics of customer and resource facing service
                                            entities. It provides a set of entities that can monitor and
                                            report on performance. Each of these entities also
                                            conducts network performance assessment against
                                            planned goals, performs various aspects of trend
                                            analysis, including error rate and cause analysis and
                                            Service degradation. Entities in this ABE also manage the
                                            traffic generated by a Service, as well as traffic trend
                                            analysis. This is important for newer technologies that
                                            separate data, control and management functions for a
                                            given Service.
Resource               01       Resource    Collects, correlates, consolidates, and validates various
                                Performance performance statistics and other operational
                                ABE         characteristics of Resource entities. It provides a set of
                                            entities that can monitor and report on performance.
                                            The entities in this ABE provide physical, logical, and
                                            performance information. Each of these entities also
                                            conducts network performance assessment against
                                            planned goals, performs various aspects of trend


© TM Forum 2021. All Rights Reserved.                                     Page 51 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



SID                    #        ABE               ABE Definition
Domain
                                                  analysis, including error rate and cause analysis and
                                                  Resource degradation. Entities in this ABE also manage
                                                  traffic in a Resource. This includes statistics defining
                                                  Resource loading, and traffic trend analysis.
Common                 01       Party / Party The characteristics used to group Parties that typify
                                Profile (L2)  MarketSegments and for the formulation and targeting
                                              of MarketingCampaigns. A Party ProfileType is used to
                                              categorize one or more PartyRoleSpecifications. A
                                              PartyProfileType can be defined for one or more
                                              GeographicAreas. The profile can target one or more
                                              ProductOfferings and one or more MarketSegments.
                                              PartyProfileTypes can be based on (or defined by)
                                              DemographicCharacteristics.
Business               01       Party Statistic Represents the analysis of party usage patterns,
Partner                         ABE             profitability statistics


                  4.6.3. Intelligence Management Block functionalities
A list of Intelligence Management functionalities identified as part of the ongoing study. The
functionalities currently found to be provided by Intelligence Management are captured
below.
Table 4-14. Functionalities covered by the Intelligence Management block

#      Functionality Description / Purpose
01     Insight    Insight Management integrates data in the Engagement Management
       Management Block, Party Management Block, Core Commerce Management Block and
                  Production Block, to find new relationships and patterns by analyzing
                  historical data, assessing current situation, applying business rules,
                  predicting outcomes, and proposing the next best action.
02     Autonomic            The Autonomic Manager Element's function or Decision Making Element
       Manager              (DE) is to drive control-loops meant to configure and adapt (i.e., regulate)
       Elements             the behavior or state of an ODA resource. Autonomic Management can be
                            implemented to run as an “engine”. (Reference - Generic Autonomic
                            Network Architecture
                            "GANA".http://www.etsi.org/deliver/etsi_ts/103100_103199/10319502/01.
                            01.01_60/ts_10319502v010101p.pdf).
03     Algorithm Ma This function provides the environment to develop and deploy patterns or
       nagement     rules or outcome based "recipes" for business and operational actions
                    performed by Parties or the Autonomic Manager. It gives developers the
                    ability to edit, compose, integrate, package, train and deploy AI-based
                    microservices. (Reference - https://docs.acumos.org/en/latest/)


© TM Forum 2021. All Rights Reserved.                                      Page 52 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



#      Functionality Description / Purpose
04     Analytic           Analytics models provide input for Insight Management, functions based on
       Models             analytic processes (Reference GB979D Big Data Analytics Big Data
                          Repository). Analytic models do not change any operational data but
                          provide functionality to discover, acquire, translate and communicate data
                          and knowledge (synthesized from raw data), relevant to making decisions,
                          feeding decisions or for autonomics. A Cognitive Autonomic Manager (in
                          ETSI GANA Model terms, a Cognitive Decision Element (DE)) as a Deployable
                          AI Model, employs in its operations.
05     Data Lake          The Data Lake function, acquires, manages or prepares data for use by ODA
                          and the enterprise. It includes a data collector function and can translate
                          data from multiple sources in order to create federated information or data
                          models (Data processing and Data storage shall be separated).
06     Knowledge          Knowledge Plane references include ETSI GANA (Generic Autonomic
       Plane              Network Architecture) Knowledge Plane specified in ETSI TS 103 195-2 but
                          not limited to it.
07     Governance         It is an instrument that allows the CSP defining Business Policies, Objective
       Function           /Goal and Intent specifications to be enforced and executed to ensure an
       (Dashboard )       optimal operation and achievement of desired objectives and services while
                          keeping control of activation / deactivation of deployed DEs (AI Models),
                          conflicts resolution that may happen and all associated accountability and
                          responsibility aspects
08     Training Data Various Datasets (e.g., Data extracted from an ODA Data Lake) must be
       Repository    considered in populating the Data Training Repository in order to produce
                     clean and accurate Data and also synthesize knowledge from the data and
                     make the data/knowledge available for AI Model (e.g., Cognitive Autonomic
                     Manager Element/ Cognitive Decision Element (DE)) training and testing
                     processes
09     Testing and        Testing and Evaluation System/Component for Testing and Evaluation of the
       Evaluation         Performance and Quality of “Decision-Making capability” of Cognitive
                          Autonomic Manager Element (DE) as an AI Model, against the expected
                          /predicted targets (prescribed by the CSP) in the CSP’s Testing Environment
                          before declaring and certifying the AI Model (DE) as “operation ready” and
                          “deployable Al Model (DE)” for injection into a Network Element/Function
                          (NE/NF) in the ODA Production or any other ODA Functional Bock or for
                          operationalizing it in the ODA Knowledge Plane (KP) if it is a Knowledge
                          Plane Level DE.




© TM Forum 2021. All Rights Reserved.                                 Page 53 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0



                  4.6.4. Standardized Interfaces




Table 4-15. Standard Interfaces in the Intelligence Management block

#          Interface Name                             Purpose/Description           Specification /
                                                                                    Reference
1          Performance Management API                 A TMF Defined Open API        Open API TMF628
2          Performance Management                     A TMF Defined Open API        Open API TMF649
           Threshold API
3          Recommendation API                         A TMF Defined Open API        Open API TMF680
4          Risk Management                            A TMF Defined Open API        Open API TMF696
5          Process Flow API                           A TMF Defined Open API        Open API TMF701
6          AI Management Suite                        A TMF Defined Open API        Open API Suite
                                                      Suite                         TMF915




© TM Forum 2021. All Rights Reserved.                                       Page 54 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




5. Using the Functional Architecture

                    5.1. Reference User Stories
2 types of user stories and use cases are available :
•   set of simple business use cases to illustrate how ODA can easily solve current issues
•   dynamic illustration of ODA/Open APIs call flow use cases to illustrate the Order to Cash
    global process

                  5.1.1. IG1197 ODA User Stories and Use Cases

                  5.1.2. IG1228 ODA/APIs Call Flow Use Cases



                    5.2. Function level mappings
As the Functional Framework does not yet permit to easily identify functions supporting a
business activity (eTOM level 2 or 3) and SID ABEs or BEs produced, we only have an example
of functions mapping in IG1167 ODA Functional Architecture Exploratory report - Section 2.



                    5.3. Creating an ODA Component
                  5.3.1. IG1171 ODA Component Definition



                    5.4. Implementation Scenarios
                  5.4.1. IG1167 ODA Functional Architecture




© TM Forum 2021. All Rights Reserved.                                   Page 55 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




6. Evolution
New opportunities, new concepts and new technology will continue to impact on the
capability of service provider technology management and operational systems. The fast pace
of Open source innovation, cross-industry collaboration and inside-out innovation by members
will help advance the granularity of ODA specifications.
The ODA Functional Architecture working group will evaluate, on a continuing basis, impact of
new technologies, concepts and technology and identify enhancements through the
Introductory Guide IG1167. Following active member collaboration and contributions, ongoing
reviews and joint approvals will drive the evolution of this standard.




© TM Forum 2021. All Rights Reserved.                                 Page 56 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




7. Administrative Appendix

                    7.1. Terminology, Abbreviations and Definitions
Reference TMF071 ODA Terminology R19.0.1



                    7.2. References
                  7.2.1. Core References
•   Open Digital Architecture Whitepaper
    - https://www.tmforum.org/resources/whitepapers/open-digital-architecture/
•   Open Digital Architecture Vision - IG1166 Open Digital Architecture Vision R18.0.0
•   Open Digital Architecture Concepts & Principles - GB998 Open Digital Architecture (ODA)
    Concepts & Principles R18.0.0
•   Open Digital Architecture Introductory Guide - IG1167
•   OSS of the Future - https://www.tmforum.org/resources/whitepapers/oss-of-the-future/

                  7.2.2. Other Related References
•   IG1186 ODA Governance and Security Vision R19.0.1
•   IG1187 ODA Enterprise Risk Assessment R19.0.1
•   IG1176 TOSCA Guide for Model-Driven Automation R19.0.0
•   GB999 ODA Production Implementation Guidelines R19.0.0
•   IG1171 ODA Component Definition R19.0.0
•   IG1130F SDN/NFV impacts on TAM Knowledge Management R19.0
•   IG1157 Digital Platform Reference Architecture Concepts and Principles R19.0.1




© TM Forum 2021. All Rights Reserved.                                  Page 57 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




8. Document History

                    8.1. Version History

Version           Date           Modified by:                        Description of changes
Number            Modified
1.0.0             02-Oct-        Emmanuel A. Otchere Sylvie          Final edits prior to
                  2020           Demarest Alan Pope                  publication
1.1.0             29-Jan-        Alan Pope                           Final edits prior to
                  2021                                               publication
Production        26-Mar-2021 Adrienne Walcott                       Updated to reflect TM Forum
                                                                     Approved Status



                    8.2. Release History

Release            Date                 Modified by:   Description of changes
Status             Modified
Pre-               02-Oct-2020 Alan Pope               Initial version
production
Production         24-Nov-2020 Adrienne                Updated to reflect TM Forum Approved
                               Walcott                 Status
Pre-               29-Jan-2021 Alan Pope               Updated to version 1.1.0
production
Production         26-Mar-2021          Adrienne       Updated to reflect TM Forum Approved
                                        Walcott        Status




© TM Forum 2021. All Rights Reserved.                                      Page 58 of 59
GB1022 ODA Functional Architecture Guidebook v2.0.0




9. Acknowledgements
This document was prepared by the members of the TM Forum ODA project:
•   Emmanuel A. Otchere, Huawei Technologies Co. Ltd
•   Alexis de Peufeilhoux, Deutsche Telekom AG
•   Brice Petitfrère, Orange
•   Daniela Galigniana, Telefónica
•   Eric Troup, Microsoft Corporation
•   Johan Vandenberghe, Bell Labs Consulting (Nokia)
•   Johanne Mayer, Telstra
•   Sylvie Demarest, Orange
•   Tayeb Ben Meriem, Orange
•   Naotaka Morita, NTT
•   Cecile Ludwichowski, Orange
•   Kamal Maghsoudlou, Ericsson
•   Vance Shipley, Sigscale
•   Alan Pope, TM Forum
•   Dave Milham, TM Forum




© TM Forum 2021. All Rights Reserved.                            Page 59 of 59

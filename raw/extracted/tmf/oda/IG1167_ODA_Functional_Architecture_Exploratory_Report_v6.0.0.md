TM Forum Exploratory Report

ODA Functional Architecture
Exploratory Report




IG1167
Team Approved Date: 02-Apr-2021



 Release Status: Production            Approval Status: TM Forum Approved
 Version 6.0.0                         IPR Mode: RAND

TM Forum 2021. All Rights Reserved.
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




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




© TM Forum 2021. All Rights Reserved.                                              Page 2 of 3
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Direct inquiries to the TM Forum office:

181 New Road, Suite 304
Parsippany, NJ 07054, USA
Tel No. +1 973 944 5100
Fax No. +1 973 998 7916
TM Forum Web Page: www.tmforum.org




© TM Forum 2021. All Rights Reserved.                          Page 3 of 4
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Table of Contents

     Notice .................................................................................................................................... 2
     Table of Contents................................................................................................................ 4
     List of Figures ........................................................................................................................ 7
     List of Tables.......................................................................................................................... 9
     1. SCOPE OF THIS DOCUMENT............................................................................................. 10
             1.1.         Purpose ......................................................................................................... 10
             1.2.         Scope............................................................................................................. 10
             1.3.         Benefits of ODA - Functional Architecture ................................................... 11
     2. CONVENTIONS AND TERMINOLOGY................................................................................ 12
             2.1.         Conventions .................................................................................................. 12
             2.2.         Concepts ....................................................................................................... 12
             2.3.         Terminology .................................................................................................. 12
             2.4.         Definitions ..................................................................................................... 12
             2.5.         Abbreviations ................................................................................................ 12
     3. INTRODUCTION TO ODA .................................................................................................. 13
             3.1.         The Functional Architecture ......................................................................... 13
             3.2.         Systems of Separation .................................................................................. 13
     4. BUSINESS USE CASES ....................................................................................................... 15
             4.1.         Multi-Channel / Omni-Channel User Story ................................................... 15
                 4.1.1.       Multi-channel Catalogue Management Use Case .................................... 15
                 4.1.2.       Multi-channel seamless ordering Use Case ............................................. 17
                 4.1.3.       Multi-channel Customer Interaction management Use Case .................. 19
             4.2.         Multi-Services Identity Management User Story ......................................... 21
                 4.2.1.       Seamless Customer Journey Use Case ..................................................... 21
             4.3.         Seamless Customer Move User Story ........................................................... 24
                 4.3.1.       Fixed Access Use Case .............................................................................. 24
     5. OPEN APIS REQUIREMENTS ............................................................................................. 27
             5.1.         GUI and Business Process Decoupling .......................................................... 27
             5.2.         Process Delegation and Decoupling ............................................................. 28
     6. APPROACH TO MAP BUSINESS INFORMATION OBJECTS TO ODA................................... 29
             6.1.         Illustration - Using 'Order Handling' Business Process ................................. 29
                 6.1.1.       Step 1 - Identify all the functions needed by the process ........................ 29


© TM Forum 2021. All Rights Reserved.                                                                                           Page 4 of 5
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



               6.1.2.       Step 2: Analyze information used & produced by the functions ............. 30
               6.1.3.       Map the functions to ODA functional blocks ........................................... 31
     7. NEW BUSINESS INFORMATION OBJECTS ......................................................................... 32
           7.1.         Decoupling & Integration ............................................................................. 32
               7.1.1.       New Functionalities .................................................................................. 32
           7.2.         Engagement Management ........................................................................... 32
               7.2.1.       New Engagement Management Block functionalities ............................. 32
           7.3.         Party Management ....................................................................................... 33
               7.3.1.       Party Management Block functionalities ................................................. 33
               7.3.2.       New Mapping and CRs to eTOM .............................................................. 33
               7.3.3.       New Mappings and CRs to SID ................................................................. 35
               7.3.4.       New Mapping to Functional Framework.................................................. 36
               7.3.5.       New Reference Interfaces ........................................................................ 36
           7.4.         Core Commerce Management ..................................................................... 37
               7.4.1.       New Core Commerce Management Block functionalities ....................... 37
               7.4.2.       New Mapping and CRs to eTOM .............................................................. 37
               7.4.3.       New Mapping and CRs to SID ................................................................... 39
               7.4.4.       New Reference Interfaces ........................................................................ 39
           7.5.         Production .................................................................................................... 40
               7.5.1.       New Mapping and CRs to eTOM .............................................................. 40
               7.5.2.       New Mapping and CRs to SID ................................................................... 41
               7.5.3.       New Reference Interfaces ........................................................................ 42
           7.6.         Intelligence Management ............................................................................. 42
               7.6.1.       New Mappings and CRs to eTOM ............................................................. 42
               7.6.2.       New Mapping & CRs to SID ...................................................................... 44
               7.6.3.       New Functionalities .................................................................................. 45
               7.6.4.       Capabilities of the Intelligence Management block ................................. 45
               7.6.5.       New Reference Interfaces ........................................................................ 48
     8. DEPLOYMENT SCENARIOS ............................................................................................... 49
           8.1.         Engagement Management ........................................................................... 49
           8.2.         Party Management ....................................................................................... 49
           8.3.         Core Commerce Management ..................................................................... 49
           8.4.         Production .................................................................................................... 49
               8.4.1.       Factory Model - Orange............................................................................ 50




© TM Forum 2021. All Rights Reserved.                                                                                    Page 5 of 6
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



               8.4.2.       E2E Service Model – Telefonica................................................................ 52
               8.4.3.       NaaS Model – Telstra with Operational Domain Management (ODMs).. 52
               8.4.4.       Microsoft Model - Azure .......................................................................... 53
               8.4.5.       Platform-based Model - Reference to TR262........................................... 55
               8.4.6.       Benefits of this proposed deployment approach..................................... 55
               8.4.7.       Using ETSI ZSM Model .............................................................................. 55
           8.5.         Intelligence Management ............................................................................. 56
               8.5.1.       Deployment Scenario 1 - Building AI / Autonomics / Cognitive capabilities
               are built-in per Design in the Intelligence Management Function ........................ 56
               8.5.2.       Deployment Scenario 2 - Instantiation of ETSI GANA Framework unto
               ODA Intelligence Management .............................................................................. 59
     9. ADMINISTRATIVE APPENDIX ............................................................................................ 61
           9.1.         References .................................................................................................... 61
               9.1.1.       Core References ....................................................................................... 61
               9.1.2.       Other Related References ........................................................................ 61
               9.1.3.       Terminology.............................................................................................. 61
           9.2.         Document History ......................................................................................... 61
               9.2.1.       Version History ......................................................................................... 61
               9.2.2.       Release History ......................................................................................... 62
            9.3.        Acknowledgements ...................................................................................... 63
     10.       Appendix A: Detailed Intelligence Management Implementation Scenarios ........ 64
            10.1.       INTRODUCTION............................................................................................. 64
               10.1.1. Deployment Flavors / Features / Scenarios / Options | or How to use .. 64
               10.1.2. Implementation flavors of ODA Knowledge Plane.................................. 68
     11.       BUSINESS SCENARIOS / USE CASE .......................................................................... 75
               11.1.1. ODA and legacy BSS/OSS (INFORMATIVE) .............................................. 75
               11.1.2. Managing Federation of ODA.................................................................. 76




© TM Forum 2021. All Rights Reserved.                                                                                    Page 6 of 7
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




List of Figures
Figure 3.1. ODA Functional Architecture - High Level view (Level 0).......................................... 13
Figure 3.2. Grouping of systems based on the Functional Architecture ..................................... 14
Figure 5.1. API Requirements - GUI and Process layers decoupling ........................................... 27
Figure 5.2. API Requirements - Process decoupling ................................................................... 28
Figure 6.1. eTOM / Functional Framework mapping example - Order Handling ....................... 29
Figure 6.2. eTOM business activities delegation example - Order Handling and Payment....... 30
Figure 6.3. Functional Framework / SID / ODA mapping - Order Handling and Payment ......... 30
Figure 6.4. Functional Framework / ODA mapping - Order Handling and Payment .................. 31
Figure 8-1. Figure 7.1. New eTOM Business process mapping proposed for Party Management
..................................................................................................................................................... 34
Figure 7.2. New Mappings for proposed SID ABEs to the Party Management Function block .. 36
Figure 7.3. New eTOM Business process mapping proposed for Core Commerce Management
..................................................................................................................................................... 37
Figure 7.4. New Mapping for proposed changes to SID ABEs to Core Commerce Management
..................................................................................................................................................... 39
Figure 7.5. New eTOM Business process mapping proposed for Production............................. 40
Figure 7.6. New Production Mapping and CRs to SID ABEs ....................................................... 41
Figure 7.7. New eTOM Business process mapping proposed for Intelligence Management ..... 43
Figure 7.8. Mapping SID 19.5 ABE to Intelligence Management .............................................. 44
Figure 8.1. Orange Production Factory Example ........................................................................ 50
Figure 8.2. Telefonica Production Example ................................................................................ 52
Figure 8.3. Telstra Production Example...................................................................................... 52
Figure 8.4. Microsoft Production Example ................................................................................ 53
Figure 8.5. TR262 Management Platform example ................................................................... 55
Figure 8.6. ETSI ZSM Production example .................................................................................. 56
Figure 8.7. ODA Intelligence Management Deployment option 1 ............................................. 57
Figure 8.8. Intelligence Management Deployment option 2: Instantiation of ETSI GANA
Framework onto ODA Intelligence Management ....................................................................... 59
Figure 10.1. Hierarchy of ODAs ................................................................................................. 65
Figure 10.2. Federation of two ODAs (Peering / Sibling model) ................................................ 66
Figure 10.3. External Autonomic Manager interacting directly with Home Managed Entity that
it does not own ........................................................................................................................... 67
Figure 10.4. External Autonomic Manager communicates with non-owned Home Managed
Entities via owning Home Autonomic Manager ......................................................................... 68
Figure 10.5. ODA Deployment option 1 (ODA-native) ............................................................... 69
Figure 10.6. ODA Knowledge Plane ............................................................................................ 70


© TM Forum 2021. All Rights Reserved.                                                                                                 Page 7 of 8
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Figure 10.7. ODA Master Knowledge Plane (Hierarchy of Knowledge Planes) .......................... 71
Figure 10.8. How to introduce AI / Autonomic / Cognitive capabilities in ODA Production
Function Block: case study .......................................................................................................... 73
Figure 11.1. ODA Deployment option 2: Legacy to ODA............................................................ 76
Figure 11.2. ODA Intelligence Management Federated Framework (multiple ODA Knowledge
Planes scenario) .......................................................................................................................... 77
Figure 11.3. ODA Intelligence Management Federated Framework (Single / Unique ODA
Knowledge Plane scenario) ......................................................................................................... 78




© TM Forum 2021. All Rights Reserved.                                                                                        Page 8 of 9
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




List of Tables
Table 1. Decoupling & Integration key functionalities ............................................................... 32
Table 2. New Functionalities provided by the Engagement Management Block under review for
confirmation include: .................................................................................................................. 32
Table 3. Process Descriptions (Ref to eTOM for additional details) ........................................... 34
Table 4. Descriptions of newly proposed changes to SID ABEs (Ref to SID for additional details)
..................................................................................................................................................... 36
Table 5. Proposed Standard Interfaces for Party Management block ....................................... 36
Table 6. New Core Commerce Management eTOM Process Descriptions and Change Reasons.
..................................................................................................................................................... 37
Table 7. New SID ABEs and their description and Change Reasons ........................................... 39
Table 8. Proposed new Standard Interfaces for Core Commerce Management block............... 39
Table 9. Production eTOM Process descriptions........................................................................ 40
Table 10. SID ABEs and their description (extract from GB922 19.5) ......................................... 42
Table 11. Proposal for new Interfaces to Standard in the Production block ............................. 42
Table 12. Intelligence Management eTOM Process descriptions.............................................. 43
Table 13. Newly proposed SID ABEs and their description ......................................................... 44
Table 14. Functionalities covered by the Intelligence Management block ................................ 45
Table 15. Definition and scope of diagrams ............................................................................... 46
Table 16. New Reference interfaces ........................................................................................... 48
Table 17. Illustrates Mapping / Instantiation ............................................................................. 59




© TM Forum 2021. All Rights Reserved.                                                                                                 Page 9 of 10
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




1. SCOPE OF THIS DOCUMENT

                    1.1. Purpose
The Purpose of this document is to explore and introduce structured concepts which are
implementation-neutral using simplified views of business information objects interacting in
an Information Systems environment.
The document is intended for technical stakeholders that explore new functions, new
capabilities, end-to-end business information objects, and related technologies to realize the
concepts and principles defined in the Open Digital Architecture best practices and standard.
System architects, solution architects, product designers, systems integration specialists et al.
who are exploring or advancing the functional requirements of Digital Organizations can firstly
use this document to landscape their insights and approach.
The functional architecture, TMF GB1022, enforces the concepts and principles established in
GB998 Open Digital Architecture (ODA) Concepts & Principles, which outline characteristics
that are universal to leading digital businesses. These characteristics include decoupling,
componentization and exposure of capabilities. This document is used to share concepts that
advance use cases of ODA and to propose new best practices and standards that can be
adopted into the Standard - GB1022 ODA Functional Architecture Guidebook.
By continuing to capture and rationalize ODA best practices, the business requirements from
service providers and concerns of suppliers and integrators are altogether addressed. Through
this document, the industry is able to identify and propose new best practices as the dynamics
of business and operations change.



                    1.2. Scope
The scope of the Introductory Guide for ODA Functional Architecture is to:
•   Advance taxonomy of Business and Infrastructure Functions
•   Specify the functionality of those Functions, advance their incorporation or mapping to
    Frameworx.
•   Explore scenarios for using the Functions based on implementation that is technology
    neutral aka Features/ Feature Groups (SID information Framework Definition)
This will enable:
•   Digital Enterprises/Organizations to define new business requirements based on an
    unambiguous set of Functions - linked to Frameworx - For consistency in expressing
    requirements through reuse of function specifications.
•   Technology ecosystems to interpret business requirements based on one language.
•   The creation of reusable ODA Component specifications from groupings of these functions
•   Facilitate iterative and incremental design and implementation by developers.




© TM Forum 2021. All Rights Reserved.                                                 Page 10 of 11
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



                    1.3. Benefits of ODA - Functional Architecture
•   Enforces separation of concerns to enable technical and commercial evolution.
•   Easy to realize cross channel capabilities by reusing Systems of Record (SoR) for any and all
    Systems of Engagement (SoE).
•   Eliminates data replication between Functions that process the same data.
•   Enabled Business model innovation (Supports different Actor/Roles such as Retailer, Biller,
    … beyond the pipeline/linear business model)
•   Enables platformization of Functions through standardized definition of API (TMF) at the
    border of Function blocks in order to expose functionalities and services in a unified and
    harmonized way.




© TM Forum 2021. All Rights Reserved.                                                Page 11 of 12
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




2. CONVENTIONS AND TERMINOLOGY

                    2.1. Conventions
All conventions follow industry standards. Where a convention is unique, it will be adequately
described based on the topic and domain.



                    2.2. Concepts
Reference GB998 Open Digital Architecture (ODA) Concepts & Principles v3.0.0 (ODA-645)



                    2.3. Terminology
Reference TMF071 ODA Terminology R19.0.1



                    2.4. Definitions
Reference TMF071 ODA Terminology R19.0.1



                    2.5. Abbreviations
Reference TMF071 ODA Terminology R19.0.1




© TM Forum 2021. All Rights Reserved.                                              Page 12 of 13
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




3. INTRODUCTION TO ODA
Reference GB1022 ODA Functional Architecture Guidebook



                    3.1. The Functional Architecture
The Functional Architecture has been modeled to represent enterprise functions and
corresponding interactions that go beyond the traditional pipe-line business models. Each of
the ODA Function Blocks is an enterprise level group of functions with a collection of coherent
processes continuously performed within the enterprise to support its mission.




Figure 3.1. ODA Functional Architecture - High Level view (Level 0)



                    3.2. Systems of Separation
The functional view of ODA can be summarized in a system view based on the architectural
elements that deliver the system’s functionality. The view in Figure 3-2 below groups the ODA
function blocks into a system’s structure-including the key functional elements (Party
Management, Core Commerce Management, and Production), their responsibilities, which can
be used to summarize their roles, interfaces they expose, and the interactions between them.
Taken together, this shows how the responsibility of the systems and the functions required of
them.




© TM Forum 2021. All Rights Reserved.                                               Page 13 of 14
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 3.2. Grouping of systems based on the Functional Architecture
Rationale of systems separation
Each of above defined system types has its own lifecycle :
•   Engagement Management deals with user interactions that are powered by fast moving
    technologies, it is committed to evolve (e.g., in a quick & agile mode) in order to catch the
    trends on the fields of customer experience, ergonomics, social networking. These trends
    apply to all industries not only telecommunications, therefore Service Providers have no
    control over them and must adapt quickly.
•   Conversely, Systems of Records hold assets (processes, objects and data) that need
    stability over time, while maintaining a strong ability to interwork with fast moving
    Engagement systems. Records is therefore responsible for in variants, stability over time,
    and integrity of data. Hence, Records goes through a slower lifecycle.
•   Intelligence Management, although it is Back-end systems by nature, is as fast-evolving as
    Engagement Management, due in particular to technology leaps such as Big & Fast Data
    that enables functionality previously out of reach of companies (too expensive or needing
    extreme processing capabilities). Therefore, it makes sense to segregate them from the
    other two.




© TM Forum 2021. All Rights Reserved.                                                 Page 14 of 15
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




4. BUSINESS USE CASES
This set of Business oriented use cases illustrates how ODA can solve current business issues
shared by many CSPs.



                    4.1. Multi-Channel / Omni-Channel User Story
Multi and omni channel capabilities and presentation consistency is one of the major issues of
digitalization for CSPs. Historically each channel has been managed by dedicated applications
that generally do not permit to address the issue. We will see through these use cases how
ODA decoupling between Engagement Management, in charge of GUI kinematics, and process
layers will help to solve it.

                  4.1.1. Multi-channel Catalogue Management Use Case
Usually, with CSPs, when queries are performed on one channel interface, the results differ,
most often, with other channels. This can, and most often poses a challenge to customers,
partners and service delivery personnel (like call center agents, and back office customer
support staff).
While presentation of content from, say catalogs, can be optimized per channel, device and/or
customer type/segments, the need to maintain consistency across all these channels for
objects like Offer names, and/or attributes are key to drive unified experience and customer
engagement consistency. Below is a reference of some of the issues.




The reason of these differences, or even inconsistencies, between the information provided on
each channel is that CSPs often have implemented applications or components dedicated to
one channel and covering GUI but also process layer and information. So, E-shop and Mobile




© TM Forum 2021. All Rights Reserved.                                               Page 15 of 16
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



App often have their own catalogue, and global consistency between these catalogues is not
always easy to manage.




With ODA, we propose to manage in Core Commerce a global Product Offerings and Product
Catalogue component, able to serve all the channels, including their specificities. For example,
offers or operations can be allowed only for a subset of channels. E-shop and Mobile App
components will query this catalogue and manage its presentation as they want to.




© TM Forum 2021. All Rights Reserved.                                                Page 16 of 17
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




                  4.1.2. Multi-channel seamless ordering Use Case
A person starts to order offers and products on a channel, using for example the Mobile App
provided by a CSP, and needs to stop before the validation of his basket. Back home he wants
to continue his order using the CSP Website. Often he is not able to recover his basket and
needs to restart his order.
CSPs want to be easily able to provide their customers with a multi-channel seamless ordering.




The reason why this multi-channel seamless ordering is difficult to provide is that CSPs often
have implemented applications or components dedicated to one channel and covering GUI but



© TM Forum 2021. All Rights Reserved.                                              Page 17 of 18
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



also process layer and information. So, E-shop and Mobile App often have not only their own
Catalogue but also their own implementation of the Order Capture process. This prevents the
sharing of Customer Order information and Order Capture progress and status between the
channels.




With ODA, we propose to manage in Core Commerce a global Order Capture process and
component, able to serve all the channels, including their specificities, and driven by the
Product Offering and Product Catalogue. So, E-shop and Mobile App components will address
this Order Capture process, answer its questions, and manage presentation of the basket
content. With this decoupling the customer will be able to change channel without losing
information, and moreover CSPs will be able to manage easily the support of a CSR if needed :
the CSR will directly share the basket initiated by the customer.




© TM Forum 2021. All Rights Reserved.                                             Page 18 of 19
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




                  4.1.3. Multi-channel Customer Interaction management Use Case
A person starts to interact with a CSP bot on a channel, for example using the Mobile App
provided by the CSP. The bot is able to answer his first questions but at one point a human
handover is needed, and a CSR is identified to continue the discussion. This CSR needs to have
the context and history of the discussion with the bot to give efficient answers.
CSPs want to be easily able to provide their customers with a multi-channel seamless
interaction management.




© TM Forum 2021. All Rights Reserved.                                              Page 19 of 20
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



The reason why this multi-channel seamless interaction management is difficult to provide is
that CSPs often have implemented applications or components dedicated to one channel and
covering GUI but also process layer and information. So, Bots and Call Center often have their
own implementation of the Interaction Management process and information. This
prevents the sharing of Customer Interaction information and Interaction Management
progress and status between the channels.




With ODA, we propose to manage in Party Management a global Interaction Management
process and component, able to serve all the channels and to interacts with Bots Knowledge
Center in Intelligence Management. So, Bots and Call Center components will address this
Interaction Management process, transmit the customer questions, and manage presentation
of the answers. With this decoupling the customer will be able to change channel without
losing information, and the CSR will directly share the previous questions and answers
managed by the bot.




© TM Forum 2021. All Rights Reserved.                                               Page 20 of 21
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




                    4.2. Multi-Services Identity Management User Story
                  4.2.1. Seamless Customer Journey Use Case
CSPs are commercializing new lines of business and introducing new products and services,
such as Media and Entertainment (e.g., TV, On-demand Streaming Services like Podcasts,
Radio etc.), Banking (e.g., Payments, CICO* etc.), Healthcare (e.g., Consultation, Monitoring
etc.)
To manage these new lines of business and their services, they require ways to engage with
customers and partners which usually leads to implementing dedicated applications with their
front-ends. This leads to disconnected experiences that often impact on customer engagement
(acquisition, ordering etc.), service abandonment and back office operating efficiencies among
others.
Customers and Partners prefer to have single interfaces, that leverage single sign-on for
frictionless application use. They also require the ability to from a single engagement
interaction, the means to manage their contracts, offers and services without having to switch
applications altogether. This can improve customer acquisition, reduce cart abandonment, and
reduce customer service and back office support overheads.
* CICO: Cash-in Cash-out




© TM Forum 2021. All Rights Reserved.                                                Page 21 of 22
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




The reason why CSPs often propose dedicated applications and identification / authentication
means is that their IT is organized by lines of business, even at the customer level. So, for each
contract subscription they register a new customer and give him a new identification /
authentication mean to manage this contract.
In this context, it can be even difficult for the CSP to identify all the contracts the same person
has subscribed. It can also be difficult to respect some commercial rules, such as Bank
regulation. For example, the same person may not be allowed to have 2 Orange Money
services, but if he gives 2 different phone numbers to identify himself during the subscriptions
the CSP may not be able to stop it the second time. Another example is that in some countries
the same person is not allowed to have more than 3 SIM cards. So, if the CSP has an IT for
prepaid mobile contracts and another IT for postpaid mobile contracts it is not easily possible
to check this rule.




© TM Forum 2021. All Rights Reserved.                                                   Page 22 of 23
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




With ODA, we propose to manage a global Party Management process and component, able to
serve all the lines of business, as long as they stay separated in the CSP IT. Associated to Party
Roles and Rights management this component will permit to identify a person once, to
recognize him during each new contract subscription, and to manage the whole set of the
person's roles and rights. An identification / authentication mean will be associated to the
person, so the person can exercise all granted rights. Other identification / authentication
means this can still be associated to the same person if we want to manage a higher level of
security for specific rights for example.




© TM Forum 2021. All Rights Reserved.                                                 Page 23 of 24
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




                    4.3. Seamless Customer Move User Story
                  4.3.1. Fixed Access Use Case
One of the worst experiences a customer can have with his CSP is to lose his contents
(contacts, mails, VOD, ...) when he moves and has to order the installation of a new fix access.




The reason why it can happen is that CSPs not always clearly separate access and services in
their Order and Delivery IT. So, when a customer moves, his previous access is deleted, and as
many services are managed has linked to this access, they can also be deleted. And when the




© TM Forum 2021. All Rights Reserved.                                                Page 24 of 25
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



new access is created, new services are too, such as mail or TV/VOD service, loosing existing
contents such has contacts or previously purchased VOD.




With ODA, we propose to manage in Core Commerce a global and convergent Offer and
Product catalogue, able to describe any type of product and operations. So, we can create a
new contract with a new access product corresponding to the new address of the customer
and move existing products (or even offers if allowed) to this new contract without any impact
at delivery level (pure commercial operation). At production level we also propose to clearly
separate systems in charge of access delivery and usage and systems in charge of OTT services.




© TM Forum 2021. All Rights Reserved.                                               Page 25 of 26
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




© TM Forum 2021. All Rights Reserved.                          Page 26 of 27
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




5. OPEN APIS REQUIREMENTS
In ODA, operational processes are described in the three horizontal blocks (i.e., Party
Management, Core Commerce Management and Production). The vertical Engagement
Management is in charge of managing interactions with users through the appropriate channel
or device with the proper ergonomics.
To allow interactions and decoupling between Engagement Management, in charge of GUI
layer, and the other ODA blocs in charge of process layers, Engagement Management is only
able to query data, using GET operation provided by standard Open APIs (or POST operation
when used for complex queries). And only Party Management, Core Commerce Management
and Production are allowed to create/update/delete business information they are in charge,
using POST and PATCH operations, because these operations require knowledge of the
processes and business rules.
So, 2 new APIs have been defined to permit decoupling, and they can be used to manage
articulation between process layers and GUI kinematics, especially for manual tasks:
•   TMF701 - Process Flow API,
•   TMF688 - Event Management API



                    5.1. GUI and Business Process Decoupling
The figure below illustrates the location of the current TM Forum Open APIs and the new APIs
that permit to decouple GUI and process layers.




Figure 5.1. API Requirements - GUI and Process layers decoupling


© TM Forum 2021. All Rights Reserved.                                             Page 27 of 28
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



                    5.2. Process Delegation and Decoupling
These 2 new APIs can also be used to allow decoupling between processes managed by
different ODA blocs and manage an end-to-end business process without duplication /
replication of processes, business rules or information.
For example, during an end-to-end Order Capture and Validation process we often need to
create or update Party or Billing Account information, to manage payment, ... The Order
Capture and Validation process will be globally managed by Core Commerce Management and
it will delegate to Party Management the sub-processes related to Party, Billing Account,
Payment, ... management.




Figure 5.2. API Requirements - Process decoupling


Please refer to IG1228 and its concrete use cases showing through sequence diagrams how TMF Open
APIs, including TMF701 and TMF688 can be used.




© TM Forum 2021. All Rights Reserved.                                                Page 28 of 29
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




6. APPROACH TO MAP BUSINESS
   INFORMATION OBJECTS TO ODA
The section provides a step-by-step approach to identify Functions covered by an ODA
functional block and related business information assets eTOM, SID ABEs.
The approach uses:
•   well-defined and relevant eTOM and SID mappings described for each ODA functional
    block (refer to GB1022 ODA Functional Architecture Guidebook);


•   the Functional Framework as source of Function names and definitions; and
•   links between eTOM business activities, SID ABEs and Functions of the Functional
    Framework (as these links are not yet fully available, this document helps to initiate or
    validate them)



                    6.1. Illustration - Using 'Order Handling' Business Process
                  6.1.1. Step 1 - Identify all the functions needed by the process
To identify the functions covered by an ODA functional block, we start, for each eTOM level 2
covered, by using the eTOM / Functional Framework mapping (produced by
the Frameworks team - ongoing work) and that represents for each eTOM Level 3 business
activity which are the functions of the Functional Framework that support this business
activity.




    Legend: function names in green represent proposed updates of current content of the
                                  Functional Framework.
Figure 6.1. eTOM / Functional Framework mapping example - Order Handling
In this example we see that:
•   a business activity can be supported by one or several functions
•   a function can support one or several business activities



© TM Forum 2021. All Rights Reserved.                                                 Page 29 of 30
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Then we can identify related business activities, that may be covered by other functional
blocks, needed by the end-to-end process. For example, during an order capture process we
often need to trigger a payment process. So, the functions that support this payment process
will also be identified in the scope.




Figure 6.2. eTOM business activities delegation example - Order Handling and Payment

                  6.1.2. Step 2: Analyze information used & produced by the functions
As a second step, for each function identified, we use the Functional Framework / SID mapping
(produced by the Frameworks team - ongoing work) to show which are the SID aggregate
business entities (ABE) produced or consumed. And we use the ODA / SID mapping to show
which ODA functional block is responsible for each of these ABEs.




Figure 6.3. Functional Framework / SID / ODA mapping - Order Handling and Payment




© TM Forum 2021. All Rights Reserved.                                                   Page 30 of 31
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Most of the time, a function consumes and produces information (SID ABEs) positioned in the
same functional block as the function itself. But sometimes, a function might consume
information in another functional block.

                  6.1.3. Map the functions to ODA functional blocks
Each function is mapped to the same ODA functional block as the information it produces.




Figure 6.4. Functional Framework / ODA mapping - Order Handling and Payment


From a Business Process such as Order Handling positioned in Core Commerce
Management, most of the functions that support it are also managed by Core Commerce. But
it can also need Functions (e.g.,: Service Availability Validation), or even complementary
processes (e.g., Manage Customer Payments) that are managed by other Functional blocks.




© TM Forum 2021. All Rights Reserved.                                            Page 31 of 32
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




7. NEW BUSINESS INFORMATION OBJECTS
The section captures the proposals to extend or advance the Functions. Each section captures
the new proposals.



                    7.1. Decoupling & Integration
                  7.1.1. New Functionalities
This section introduces new changes and proposals that are relevant to extend or advance the
'Decoupling & Integration' function. For the currently adopted standards for 'Decoupling &
Integration' functionalities, please refer to GB1022 ODA Functional Architecture Guidebook
v2.0.0.
Table 1. Decoupling & Integration key functionalities

Functionality                Description / Purpose                        Change Reason
TBD                          ...


...




                    7.2. Engagement Management
                  7.2.1. New Engagement Management Block functionalities
This section introduces new proposals and changes that are relevant to extend or advance the
'Engagement Management' function. For the currently adopted standards for 'Engagement
Management' functionalities, please refer to GB1022 ODA Functional Architecture Guidebook
v2.0.0
A list of Engagement Management functionalities identified as part of the ongoing study are
listed below:


 Table 2. New Functionalities provided by the Engagement Management Block under review for
confirmation include:

Functionality*         Description / Purpose                   Change Reason
Authentication         Correctly authenticates and             Separate these functionalities and
and                    authorizes a Party, including           allocate them to the right function
Authorization          role management.                        boxes.
                                                               Current proposals are to split across
                                                               Engagement Management and Part
                                                               Management.




© TM Forum 2021. All Rights Reserved.                                                     Page 32 of 33
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Functionality*         Description / Purpose                   Change Reason
                                                               These functionalities correctly
                                                               authenticate and authorize a Party,
                                                               including the kinematics and
                                                               protocols to verify the identity of a
                                                               user or process (authentication) and
                                                               specify access rights/privileges to
                                                               resources.
User-interaction Manage Party interactions
lifecycle        with the different services
management       (provide consent, configure
                 services, etc.) as well as their
                 relationship with other users
                 (create groups and share
                 services)
TBD                    TBD
...                    ...
*These functionalities are still under review for confirmation.
Remark : Addition of these functionalities to the Functional Framework has to be discussed
with the Frameworks team for alignment as part of standardizing them.



                    7.3. Party Management
                  7.3.1. Party Management Block functionalities
This section introduces new proposals and changes that are relevant to extend or advance the
'Party Management' function. For the currently adopted standards for 'Party Management'
functionalities, please refer to GB1022 ODA Functional Architecture Guidebook v2.0.0

                  7.3.2. New Mapping and CRs to eTOM
Since the Party Management mapping is based on a tactical operating model with no categoric
business architecture underpinning it, ongoing analysis and review of the currently mapped
businesses processes and new ones are provided here for informative purposes only.
This figure below provides a reference for mapping of new eTOM level business processes, or
structural changes that apply to the Party Management function block.




© TM Forum 2021. All Rights Reserved.                                                     Page 33 of 34
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 8-1. Figure 7.1. New eTOM Business process mapping proposed for Party Management




Table 3. Process Descriptions (Ref to eTOM for additional details)

eTOM Process Category Process Brief Description                           Change Reason
                      Identifier
Sales                (2) eTOM 1.1.5              Develop the Sales        The current Business
Development          Process                     support and response     Process has activities
                     Type                        for new and existing     spanning two
                                                 products, as well as     Functional
                                                 existing and potential   Architecture blocks.
                                                 customers.               Separation of
                                                                          concerns requires
                                                                          splitting the business
                                                                          processes to follow
                                                                          the principles of ODA.
Selling              (2) eTOM 1.1.9              Responsible for          The current Business
                     Process                     managing prospective Process has activities
                     Type                        customers, for           spanning two
                                                 qualifying and educating Functional
                                                 customers, and           Architecture blocks.
                                                 matching customer        Separation of
                                                 expectations             concerns requires
                                                  Managing prospective splitting the business
                                                 parties with whom an processes to follow
                                                 enterprise may do        the principles of ODA.
                                                 business, such as
                                                 potential existing or
                                                 new customers and
                                                 partners, for qualifying


© TM Forum 2021. All Rights Reserved.                                                  Page 34 of 35
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



eTOM Process Category Process Brief Description                            Change Reason
                      Identifier
                                                 and educating them,
                                                 and ensuring their
                                                 expectations are met.
Customer             (2) eTOM 1.3.2              Perform customer          The current Business
Experience           Process                     lifecycle mapping,        Process has activities
Management           Type                        assess customer           spanning two
                                                 experience maturity, as   Functional
                                                 well as analyze           Architecture blocks.
                                                 customer experience       Separation of
                                                 metrics.                  concerns requires
                                                                           splitting the business
                                                                           processes to follow
                                                                           the principles of ODA.
Party                (2) eTOM 1.6.5              Manage the evaluation     The current Business
Agreement            Process                     of agreements with        Process has activities
Management           Type                        parties, including        spanning two
                                                 customers. Initiate and   Functional
                                                 complete business         Architecture blocks.
                                                 agreements when one       Separation of
                                                 or more other parties     concerns requires
                                                 are involved.             splitting the business
                                                                           processes to follow
                                                                           the principles of ODA.
Party            (2) eTOM 1.6.16                 (TBD)                     The current Business
Identification & Process                                                   Process has activities
Authentication Type                                                        spanning two
                                                                           Functional
                                                                           Architecture blocks.
                                                                           Separation of
                                                                           concerns requires
                                                                           splitting the business
                                                                           processes to follow
                                                                           the principles of ODA.
TBD                  ...


                  7.3.3. New Mappings and CRs to SID
This section identifies new mapping or proposed Frameworx SID ABEs to the Party
Management function block. For the currently adopted standards for SID mappings, please
refer to GB1022 ODA Functional Architecture Guidebook v2.0.0.




© TM Forum 2021. All Rights Reserved.                                                   Page 35 of 36
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 7.2. New Mappings for proposed SID ABEs to the Party Management Function block




Table 4. Descriptions of newly proposed changes to SID ABEs (Ref to SID for additional details)

SID Domain                  ABE         ABE Definition               Change Reason
Budget                      ...
Document                    ...
TBD                         ...


                  7.3.4. New Mapping to Functional Framework
Ongoing Study.

                  7.3.5. New Reference Interfaces
Ongoing Study
Table 5. Proposed Standard Interfaces for Party Management block

Interface Name                    Specification / Reference                Change Reason
TBD                               TBD
...                               ...




© TM Forum 2021. All Rights Reserved.                                                     Page 36 of 37
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



                    7.4. Core Commerce Management
                  7.4.1. New Core Commerce Management Block functionalities
This section introduces new proposals and changes that are relevant to extend or advance the
'Core Commerce Management' function. For the currently adopted standards for 'Party
Management' functionalities, please refer to GB1022 ODA Functional Architecture Guidebook
v2.0.0.

                  7.4.2. New Mapping and CRs to eTOM
The Core Commerce Management Block mapping is based on a tactical operating model with
no categoric business architecture underpinning it. This mapping is provided for informative
purposes only, where different Business Architecture shall have an influence on eventual
mapping.
This figure below provides a mapping of newly proposed eTOM level 2 business processes to
the Core Commerce Management function block.




Figure 7.3. New eTOM Business process mapping proposed for Core Commerce Management
Table 6. New Core Commerce Management eTOM Process Descriptions and Change Reasons.

eTOM Process Category Process Brief Description                            Change Reason
                      Identifier
Sales       (2) eTOM 1.1.5                    Develop the Sales support    The current Business
Development Process                           and response for new and     Process has activities
            Type                              existing products, as well   spanning two
                                              as existing and potential    Functional
                                              customers.                   Architecture blocks.
                                                                           Separation of
                                                                           concerns requires
                                                                           splitting the business




© TM Forum 2021. All Rights Reserved.                                                  Page 37 of 38
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



eTOM Process Category Process Brief Description                            Change Reason
                      Identifier
                                                                           processes to follow
                                                                           the principles of ODA.
Selling            (2) eTOM 1.1.9             Responsible for managing The current Business
                   Process                    prospective customers, for Process has activities
                   Type                       qualifying and educating spanning two
                                              customers, and matching Functional
                                              customer expectations        Architecture blocks.
                                              Managing prospective         Separation of
                                              parties with whom an         concerns requires
                                              enterprise may do            splitting the business
                                              business, such as potential processes to follow
                                              existing or new customers the principles of ODA.
                                              and partners, for qualifying
                                              and educating them, and
                                              ensuring their expectations
                                              are met.
Party      (2) eTOM 1.6.5                     Manage the evaluation of The current Business
Agreement  Process                            agreements with parties, Process has activities
Management Type                               including customers.      spanning two
                                              Initiate and complete     Functional
                                              business agreements when Architecture blocks.
                                              one or more other parties Separation of
                                              are involved.             concerns requires
                                                                        splitting the business
                                                                        processes to follow
                                                                        the principles of ODA.
Party Special (2) eTOM 1.6.14                 Plans, prepare, and           The current Business
Event         Process                         produce a special event       Process has activities
Management Type                               which targets one or more spanning two
                                              types of parties. It includes Functional
                                              the assessment, definition, Architecture blocks.
                                              acquisition, allocation,      Separation of
                                              direction, control, and       concerns requires
                                              analysis of time, finances, splitting the business
                                              people, products, services, processes to follow
                                              and other resources to        the principles of ODA.
                                              achieve an event's
                                              objectives.
...




© TM Forum 2021. All Rights Reserved.                                                  Page 38 of 39
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



                  7.4.3. New Mapping and CRs to SID
This section identifies new mapping or proposed Frameworx SID ABEs to the Core Commerce
function block. For the currently adopted standards for SID mappings to the 'Core Commerce
Management', please refer to GB1022 ODA Functional Architecture Guidebook v2.0.0.

Below is the mapping for newly proposed changes to Frameworx SID ABEs to the Core
Commerce Management function block.




Figure 7.4. New Mapping for proposed changes to SID ABEs to Core Commerce Management


Table 7. New SID ABEs and their description and Change Reasons

SID Domain                 SID ABE           ABE Definition      Change Reason
Opportunity                TBD
...


                  7.4.4. New Reference Interfaces
Ongoing Study
Table 8. Proposed new Standard Interfaces for Core Commerce Management block

Interface Name                       Specification / Reference        Change Reason
Proposals requested                  TBD
...                                  ...




© TM Forum 2021. All Rights Reserved.                                            Page 39 of 40
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



                    7.5. Production
                  7.5.1. New Mapping and CRs to eTOM
This section introduces new proposals and changes that are relevant to extend or advance the
'Production' function. For the currently adopted standards for 'Production' functionalities,
please refer to GB1022 ODA Functional Architecture Guidebook v2.0.0.
The Production Block's mapping is based on a tactical operating model with no categoric
business architecture underpinning it. This mapping is provided for informative purposes only,
where different Business Architecture shall have an influence on eventual mapping.
Below is a mapping of new eTOM level 2 business process elements to the Production function
block.




Figure 7.5. New eTOM Business process mapping proposed for Production.


Table 9. Production eTOM Process descriptions

eTOM           Category Process Brief Description                        Change Reason
Process                 Identifier
SM&O      (2) eTOM 1.4.4                  Manage service infrastructure, The current Business
Support & Process                         ensuring that the appropriate Process has activities
Readiness Type                            service capacity is available  spanning two
                                          and ready to support the       Functional
                                          SM&O Fulfillment, Assurance Architecture blocks.
                                          and Billing processes          Separation of
                                                                         concerns requires
                                                                         splitting the business
                                                                         processes to follow
                                                                         the principles of




© TM Forum 2021. All Rights Reserved.                                                Page 40 of 41
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



eTOM           Category Process Brief Description                         Change Reason
Process                 Identifier
                                                                          ODA.


RM&O      (2) eTOM 1.5.4                  Manage resource                 The current Business
Support & Process                         infrastructure to ensure that   Process has activities
Readiness Type                            appropriate application,        spanning two
                                          computing and network           Functional
                                          resources are available and     Architecture blocks.
                                          ready to support the            Separation of
                                          Fulfillment, Assurance and      concerns requires
                                          Billing processes in            splitting the business
                                          instantiating and managing      processes to follow
                                          resource instances, and for     the principles of
                                          monitoring and reporting on     ODA.
                                          the capabilities and costs of
                                          the individual FAB processes.



                  7.5.2. New Mapping and CRs to SID
Below is a mapping of Frameworx SID ABEs to the Production function block.




Figure 7.6. New Production Mapping and CRs to SID ABEs




© TM Forum 2021. All Rights Reserved.                                                 Page 41 of 42
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Table 10. SID ABEs and their description (extract from GB922 19.5)

SID Domain                SID ABE           ABE Definition            Change Reason
Service                   ...
Resource                  ...
Enterprise                ...
Common                    ...

                  7.5.3. New Reference Interfaces
Table 11. Proposal for new Interfaces to Standard in the Production block

Interface Name                  Specification / Reference                   Change Reason
Service related:
XXXXXX API                      Open API TMFXXX


Resource related:
XXXXXX API                      Open API TMFXXX


Others:
XXXXXX API                      Open API TMFXXX



                    7.6. Intelligence Management
                  7.6.1. New Mappings and CRs to eTOM
This section introduces new proposals and changes that are relevant to extend or advance the
'Intelligence Management' function. For the currently adopted standards for 'Intelligence
Management' functionalities, please refer to GB1022 ODA Functional Architecture Guidebook
v2.0.0.




© TM Forum 2021. All Rights Reserved.                                                  Page 42 of 43
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 7.7. New eTOM Business process mapping proposed for Intelligence Management
Note: eTOM level 2 are identified as "split into 2" when they manage SID ABEs that are mapped
to different ODA functional blocks.


Table 12. Intelligence Management eTOM Process descriptions

eTOM               Category Process Brief Description                      Change Reason
Process                     Identifier
SM&O               (2) eTOM 1.4.4             Manage service                The current
Support and        Process                    infrastructure, ensuring that Business Process
Readiness          Type                       the appropriate service       has activities
                                              capacity is available and     spanning two
                                              ready to support the SM&O Functional
                                              Fulfillment, Assurance and Architecture blocks.
                                              Billing processes             Separation of
                                                                            concerns requires
                                                                            splitting the
                                                                            business processes
                                                                            to follow the
                                                                            principles of ODA.
RM & O             (2) eTOM 1.5.4             Manage resource               The current
Support and        Process                    infrastructure to ensure that Business Process
Readiness          Type                       appropriate application,      has activities
                                              computing and network         spanning two
                                              resources are available and Functional
                                              ready to support the          Architecture blocks.
                                              Fulfillment, Assurance and Separation of
                                              Billing processes in          concerns requires
                                              instantiating and managing splitting the
                                              resource instances, and for business processes
                                              monitoring and reporting on


© TM Forum 2021. All Rights Reserved.                                                 Page 43 of 44
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



eTOM               Category Process Brief Description                      Change Reason
Process                     Identifier
                                              the capabilities and costs of to follow the
                                              the individual FAB processes. principles of ODA.
                                              (Ongoing Study)
Customer   (2) eTOM 1.6.11
Experience Process
Management Type

                  7.6.2. New Mapping & CRs to SID
Below is a mapping of Frameworx SID ABEs to the Intelligence Management function block.




Figure 7.8. Mapping SID 19.5 ABE to Intelligence Management


Table 13. Newly proposed SID ABEs and their description

SID    ABE                      ABE Definition                                          Change
Domain                                                                                  Reason
Common Party / Party The characteristics used to group Parties that typify
       Profile (L2)  MarketSegments and for the formulation and
                     targeting of MarketingCampaigns. A Party
                     ProfileType is used to categorize one or more
                     PartyRoleSpecifications. A PartyProflieType can be
                     defined for one or more GeographicAreas. The
                     profile can target one or more ProductOfferings and
                     one or more MarketSegments. PartyProfileTypes
                     can be based on (or defined by)
                     DemographicCharacteristics.



© TM Forum 2021. All Rights Reserved.                                                 Page 44 of 45
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



SID    ABE                      ABE Definition                                            Change
Domain                                                                                    Reason
TBD         Market and Ongoing Study
            Sales
            Performance
TBD         Party       Ongoing Study
            Performance
TBD         Customer            Ongoing Study
            Experience
TBD         Budget              Ongoing Study
...


                  7.6.3. New Functionalities
This section captured a list of Intelligence Management functionalities through various
ongoing implementations. For the currently adopted standards for 'Intelligence Management'
functionalities, please refer to GB1022 ODA Functional Architecture Guidebook v2.0.0.


Table 14. Functionalities covered by the Intelligence Management block

Functionality                Description / Purpose                      Change Reason
RFC
...

                  7.6.4. Capabilities of the Intelligence Management block
The Intelligence Management (IM) Function Block provides “closed-loop” capabilities to
package and consume data. It relies on analytical data (reference Analytics Big Data
Repository) to develop Insights for decision support, or intent-based actions or advice.
The scope of the Intelligence Management Function Block is considered to be equivalent to
that described in ETSI Generic Autonomic Network Architecture (GANA) model specified in
ETSI TS 103 195-2. ODA uses GANA for the ODA blueprint model that defines and prescribes
the design and operational principles of Decision-Making-Elements (DMEs) called Decision
Elements (DEs) in short, as Autonomic Manager Elements.
Modeling for Intelligence Management
Intelligence Management is about Autonomic & Control paradigm that involves Management
& Control of Networks and Services.
Most of the time people mix up "Autonomic Management" and "Automated Management".
Therefore, within ODA in which a Function Block called "Intelligence Management" Function
Block is a key function, a clear definition and scope needs to be settled from the beginning to
avoid potential confusion. ETSI GANA (Generic Autonomic Network Architecture) model
compared and contrasted both paradigms (Automated Management vs Autonomic
Management) and provided a diagram showing responsibility demarcation of each of them


© TM Forum 2021. All Rights Reserved.                                                   Page 45 of 46
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



and how they complement each other as described in ETSI White Paper
N0.16 (http://www.etsi.org/images/files/ETSIWhitePapers/etsi_wp16_gana_Ed1_20161011.p
df ).
Scope of Automated Management and Autonomic Management & Control
In the table below are the definitions and scopes of both paradigms according to the ETSI
GANA model.


Table 15. Definition and scope of diagrams

Automated Management
Automated Management is about workflow reduction and automation i.e.,
automation of the processes involved in the creation of network configuration input
using specialized task automation tools (e.g., scripts, network planning tools, policy
generators for conflict-free policies).
 Autonomic Management & Control
Citing ETSI White Paper N0.16, is about Decision making Elements (DMEs) or (DEs in
short), as Autonomic Functions (meaning Autonomic Manager components that
implement the logic that drive the operation of various kinds of control-loops) with
cognition capabilities and are introduced in the Management Plane as well as in the
Control Plane (whether these Planes are distributed or centralized). "Control" is about
control-logic as the kernel of a particular DE that realizes a control-loop in order to
dynamically adapt its specifically assigned network resources and parameters or
services in response to changes in network goals/policies, context changes and
challenges in the network environment that affect service availability and quality.
 Autonomic Management & Control vs Automated Management
Automated Management provides input to the Autonomic Management & Control.
Indeed, Autonomic Management must exhibit a network governance interface
through which the input that governs the configuration of an Autonomic Network
should be provided. Thanks to automation tools and mechanisms (Automated
Management), by using a high-level language the operator can define the features of
the network services that should be provided by the underlying network
infrastructure. Such a business language that can help the operator express high level
business goals required of the network may be modeled by the use of ontology to add
semantics and enable machine reasoning on the goals. The human operator defined
features relate to business goals, technical goals and some input configuration data
that an Autonomic Network is supposed to use for network resources and parameter
configuration.


ODA Intelligence Management organizational model
a. Governance and Management concept outside of the Telecom's sector
Governance related aspect is key issue in all organizations at Government level (e.g., Country
Government) as well as at Enterprise level.




© TM Forum 2021. All Rights Reserved.                                               Page 46 of 47
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




The three most adopted options are:
•   Centralized Model
•   Distributed Model
•   Hybrid Model - combination of both Centralized and Distributed
But the most efficient one is the Hybrid one.
Even the "Autonomic Nervous System" of a human body operates at a "Hybrid structure" that
consists of brain in head and the spinal cord with certain "fast reaction" (reflexes) on muscle
contractions close to certain lower regions of the human being coordinated in response to
stimuli, without necessarily need the need for the central brain's direct involvement during the
reflex action.
b. Which option should be adopted by ODA Intelligence Management
Within Digital Service Providers’ space there are various processes and life cycles nested and
interworking at various time-scales (Fast time scale and Slow time-scale). ODA Intelligence
Management has the purpose of managing design and operational processes associated with
Autonomic and Cognitive capabilities (Closed Control-loops for management and control of
Network and Services) and behaviors. As such, ODA Intelligence Management shall adopt
design principles that accommodate and combine both time-scales ("Fast time-scale" and
"Slow time-scale") in an interworking manner in a "Hybrid" Model. Hence, this design principle
defines time-scaling for such capabilities at various levels of abstraction of self-management
functionality.
c. Which available standard can accommodate this ODA Intelligence Management "Hybrid"
option
From standardization ecosystem perspective, ETSI GANA (Generic Autonomic Network
Architecture) Framework (ETSI TS 103 195-2) is a Hybrid model for Autonomic Management &
Control of Network and Services. It is two-level Intelligence Management/Autonomic &
Control architecture:
•   “macro” Autonomic Managers (responsible for Centralized Closed Control-loops) that
    drive logically centralized network-wide control-loops but operate at "Slower time-scale".
•   "micro" Autonomic Managers that drive similar control-loops that can be implemented in
    a distributed fashion in Network Elements (NEs) and collaborating with network
    infrastructure. Within NEs, "micro" Autonomic Managers are for local reactions that
    operate at "Faster time-scale".
Besides, NGMN and 3GPP SON (Self Organizing Network) architecture standard is based on a
Hybrid architecture so called “Hybrid-SON” in the same design architecture principle as the
ETSI GANA one. In this regard, we can say the NGMN and 3GPP Hybrid-SON architecture is
compliant with the ETSI GANA model as this latter is an agnostic model.




© TM Forum 2021. All Rights Reserved.                                               Page 47 of 48
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




                  7.6.5. New Reference Interfaces
The table below lists needed interfaces with the Intelligence Management Function Block
(internal interfaces). Each Interface is described and categorized as internal or external.
Table 16. New Reference interfaces

Interface Name Interface Description Specification / Reference               Change Reason
RFC
....




© TM Forum 2021. All Rights Reserved.                                                Page 48 of 49
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




8. DEPLOYMENT SCENARIOS

                    8.1. Engagement Management
(Ongoing Study)



                    8.2. Party Management
(Ongoing Study)




                    8.3. Core Commerce Management
(Ongoing Study)




                    8.4. Production
Production Block Scenarios (with Ecosystem Participants)
While the Production Block is responsible for sourcing and delivering the customer order,
outside of handling and shipping physical goods, scheduling workforce for installations, the
majority of products will be services exposed, delivered and managed by factories and
Operational Domain Management (ODM).
An Operational Domain is typically a scope of management inside an operator (e.g., network
operator, service operator) that is delineated by an administrative and/or technological
boundary. The technology boundary must be clearly defined as to what services the domain
exposes and what resources the domain has exclusive control over.
Types of factories/ODM include:
•   OTT Services Management/ Partner Services
•   Network services: Physical, virtualized, Hybrid Management
•   Cloud SaaS/PaaS/IaaS Management
•   Application Management
•   Supply Chain Management
•   Device Management
•   Field Intervention Management




© TM Forum 2021. All Rights Reserved.                                               Page 49 of 50
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




In addition, an operational domain can also come from external partners (e.g., application
provider and network service providers) where clear technological boundaries exist for the
external partner. Inside an operational domain, services delivered, and associated
infrastructure resources, are managed including exposure and complete lifecycle management
of the services delivered from that domain. The lifecycle management includes the life of the
service (creation, delivery, removal) and service assurance, usage and related service
management.
In some cases, Operational Domains can be classified whether they create services:
•   From infrastructure resources, and possibly other operational domain services
•   only from other operational domain services (i.e., no direct control over resources or
    infrastructure)
The former can be considered “technology” operational domains and the latter “composite”
operational domains.
An example implementation of these concepts is an Operational Domain Manager (ODM)
publishes all information required for the run-time of a network service (NaaS) from the
ODM's service catalogue to the CCM product catalog e.g., Optical Transmission service
available from 1Meg until 10Gb in increment of 1 Meg. The service provider Product
Manager decides to generate 5 products: 1 Meg, 50 Meg, 100 Meg, 1Gb and 10Gb. The
flexibility now exists that introducing, say a 7Gb product in the product catalogue would no
more involve any changes in the Network factory or ordering system other than passing new
attributes. Similarly, introducing a new optical resource from a vendor would not impact the
exposed service or OSS as the resource layer is hidden and handled within the ODM.

                  8.4.1. Factory Model - Orange
This scenario represents the way Orange is setting up their Production area with their factory
concepts. Most Factories are autonomous and have their own operational domain(s) that
exposes "capabilities" as Customer Facing Services (CFS).




Figure 8.1. Orange Production Factory Example




© TM Forum 2021. All Rights Reserved.                                                Page 50 of 51
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



In this example, most factories are exposing CFS. Exception is for devices and physical goods,
where products cannot be restriction of CFS, so these factories do not expose CFS. Therefore,
Service Management is not required for "Supply Chain" and "Device" factories. Also, note
the "Access Network" factory is separate from the "SoftService" factory to have the capability
to deliver Softservices without any dependency on Access.
Benefits of this proposed deployment approach
The functional architecture is agnostic of any organizational structure, implementation and
technical solution, not constrained by existing legacy or technical characteristics. It describes
only invariant that can be understood and used by any company telco or not.
Each Factory (SoftService, SaaS ….) provides a type of CFS and have the responsibility of all the
processes and data to manage them: Soft Service Factory delivers services like OTT (mail, TV,
VoIP), Access factory delivers Access (Fiber, Copper …), Supply Chain delivers goods, FIM
delivers human services like installation or training, etc. Moreover, if needed, a factory can
request the other factories. e.g., the Soft Service factory needs to instantiate a SaaS, it
requests it from the SaaS factory. The access factory may request the FIM to build the access
and the FIM can request the supply chain to have the equipment.
With this deployment model:
•   There is no need of a transversal orchestration between Factories, because Products are
    derived from CFS and each CFS is provided by a single Factory. The composition of
    resources to deliver a CFS is only know by the factory (that may decide to change it)
•   There is a real decoupling between Commercial (managed in Commercial Core) and
    Technical implementation (managed in the Production), with no commercial composition
    in Production. That is the only way to really reduce TTM.
•   Each level (Product, CFS, Technical solution) can have its own lifecycle and evolve at its
    own speed.
•   Each factory can be instantiated or not depending on the needs. e.g., non-incumbent
    operators do not need an Access Factory, OTT service providers do not know most of the
    factories and pure retailers even need no factory.
•   And it is extendable to any new type of know-how (telco or not) like banking or Health.
    You just have to add a factory and plug-it to Commerce layer through APIs!
To be understood and used by any company, telco or not, and become a standard, the ODA
framework must only describe invariant that are common to everybody. That is what this
Functional architecture provides.




© TM Forum 2021. All Rights Reserved.                                                  Page 51 of 52
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



                  8.4.2. E2E Service Model – Telefonica




Figure 8.2. Telefonica Production Example
In this example, Telefonica continues to have a “Service Management” layer to handle the
technical order through the different domains, proving an end to end control of the different
processes (Fulfillment, Assurance and Planning)
Benefits of this proposed deployment approach
• A single E2E view across all resource domains is maintained.
•   Reduces Service Management activity duplication
•   Implements a single point of Service design irrespective of the Resource domain.
•   Service is agnostic of the underlying Resources

                  8.4.3. NaaS Model – Telstra with Operational Domain Management (ODMs)




Figure 8.3. Telstra Production Example




© TM Forum 2021. All Rights Reserved.                                               Page 52 of 53
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



In this example Telstra Networks expose Network as Services (NaaS) grouped by similar
functions and/or by organizational level. Every Operational Domain Management (ODM)
would be responsible for the entire lifecycle of the services it exposes including the
management of resources. Some ODM may be responsible for services that are coordinated
across other ODMs and hence would not manage the resources directly. NaaS API component
suite (TMF909) is used as the contract of operational functions supported between the Core
Commerce Management Block and ODMs as well as between ODM to ODM.
Benefits of this proposed deployment approach
• Expose the network as a service.
•   Reduce network management complexity

                  8.4.4. Microsoft Model - Azure




Figure 8.4. Microsoft Production Example
In this example the Microsoft Azure Resource Manager (ARM) is used to model all aspects of
application architecture, the relationships, dependencies between service components and all
aspects of Operations including Security. The ARM template provides the Azure internal
management systems everything needed to deploy and operate any given service or
application according to specified policies and specifications. ARM deals with representations
of service capabilities and how they are task organized. Hardware resource issues are
abstracted and handled separately below the Resource Provider layer by systems not
represented here.
Azure is consumed as a Service; a domain of services. The Azure Resource Manager APIs, along
with the Azure Marketplace / Store APIs, are organic to Azure and exposed via the Azure
Portal, Azure Command Line Interface, and plugins provided to various DevOps tools like Visual
Studio or various software orchestrators like Cloudify. Therefore, from a Microsoft point of
view, the Azure Resource Manager APIs are as depicted, but they could be said to interact at
the Decoupling and Integration layer.
Separately, Azure API Management enables one to publish, map and maintain relationships
between native Microsoft APIs and external systems such as ONAP or any particular TM Forum
API.
All service levels are set decoratively as developers define application internal architecture,
dependencies, and policies via the Resource Group definition. A Resource could be a virtual



© TM Forum 2021. All Rights Reserved.                                                  Page 53 of 54
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Hard Drive, a Virtual Machine, a VPN, a blob data store, or practically any resource - any SaaS,
PaaS, IaaS service. For instance, Azure Kubernetes Service is a Resource. Another example: one
could create a Virtual Network Function called PCF modeling its entire architecture including
all Resources, their relationships, dependencies and security all within one or more Resource
Group(s). A VES agent could be defined as a resource and added to the PCF Resource Group by
the Dev to enable automatic reporting to ONAP DCAE upon Operational deployment.
Service Level Metrics / SLAs are collected and exposed via Azure Operations Management
Suite (OMS). The VES agent is another option of course.
It is the responsibility of the Resource Manager to maintain adequate capacity for its offerings.
A 3rd party can also develop Azure Resource Managers in which case there is more
involvement with underlying resource management processes.
Azure Resource Manager definition of terms:
•   Resource - A manageable item that is available through Azure. Some common resources
    are a virtual machine, storage account, web app, database, and virtual network, but there
    are many more.
•   Resource Group - A container that holds related resources for an Azure solution. The
    resource group can include all the resources for the solution, or only those resources that
    you want to manage as a group. You decide how you want to allocate resources to
    resource groups based on what makes the most sense for your organization. See Resource
    groups.
•   Resource Provider - A service that supplies the resources you can deploy and manage
    through Resource Manager. Each resource provider offers operations for working with the
    resources that are deployed. Some common resource providers are Microsoft.Compute,
    which supplies the virtual machine resource, Microsoft.Storage, which supplies the storage
    account resource, and Microsoft.Web, which supplies resources related to web apps. See
    Resource providers.
•   Resource Manager Template aka ARM Template - A JavaScript Object Notation (JSON) file
    that defines one or more resources to deploy to a resource group. It also defines the
    dependencies between the deployed resources. The template can be used to deploy the
    resources consistently and repeatedly. See Template deployment.
•   declarative syntax - Syntax that lets you state "Here is what I intend to create" without
    having to write the sequence of programming commands to create it. The Resource
    Manager template is an example of declarative syntax. In the file, you define the properties
    for the infrastructure to deploy to Azure.
Resource Manager provides several benefits:
•   You can deploy, manage, and monitor all the resources for your solution as a group
    (Resource Groups), rather than handling these resources individually.
•   You can repeatedly deploy your solution throughout the development lifecycle and have
    confidence your resources are deployed in a consistent state.
•   You can manage your infrastructure through declarative templates rather than scripts.
•   You can define the dependencies between resources, so they are deployed in the correct
    order.
•   You can apply access control to all services in your resource group because Role-Based
    Access Control (RBAC) is natively integrated into the management platform. Management
    Groups add flexibility.


© TM Forum 2021. All Rights Reserved.                                                Page 54 of 55
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



•   You can apply tags to resources to logically organize all the resources in your subscription.
•   You can clarify your organization's billing by viewing costs for a group of resources sharing
    the same tag.
See also: Understanding Resource Manager deployment and classic deployment.

                  8.4.5. Platform-based Model - Reference to TR262
Prior ZOOM work on management platform for Hybrid Infrastructure management identified
as set of deployment principles which is to realize ODA Functions as platform that exposed
group of APIs that address three groups of stakeholders: Customer / Product Manager,
Operations Managers, Enterprise Security/Risk Managers.




Figure 8.5. TR262 Management Platform example
In this example, a network service is implemented using the Management platform concept
described in TR262 Management Platform Blueprint that support the three stakeholder
groups: Customer / Product Manager, Operations Managers, Enterprise Security/Risk
Managers.

                  8.4.6. Benefits of this proposed deployment approach
•   Support agile evolution of the Management Platform
•   Realizes NaaS APIs
•   ...

                  8.4.7. Using ETSI ZSM Model
ETSI ZSM is working on enabling zero-touch automation within the Production Block.




© TM Forum 2021. All Rights Reserved.                                                 Page 55 of 56
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 8.6. ETSI ZSM Production example
In this example the ETSI ZSM “Integration Fabric” is an equivalent to "Decoupling and
Integration" Block of the TM Forum ODA Functional Architecture, linking the Core Commerce
Management Block with the Production Block. As per this reference,
http://www.etsi.org/blog-subscription-information/entry/great-strides-made-by-technical-
brainstorming-at-zsm-3 the diagram is work in progress and subject to change. Refer to
https://docbox.etsi.org/ISG/ZSM/Open for latest work.



                    8.5. Intelligence Management
                  8.5.1. Deployment Scenario 1 - Building AI / Autonomics / Cognitive capabilities are
                       built-in per Design in the Intelligence Management Function
Figure 7-7 depicts the ODA Intelligence Management Framework. In this Framework, AI /
Autonomics / Cognitive capabilities are built-in per Design in the Intelligence Management
Function Block and in each of the three horizontal ODA Function Blocks. Each having its own
“Decision-Making Logic”, its own “local Data Lake” so called Knowledge Base (KB) for the
purpose of fast / Distributed / Local decision-making element (d_DE), realized by fast control
loops complemented by “centralized” Decision-Making logics for the purpose of a
holistic decision-making view (at each ODA horizontal Function Block as a whole) at slow time
scale. This can be achieved through slow / centralized control loops and "centralized" Data
lake or centralized Knowledge Base that can be located in the Intelligence Management
Function Block. The Intelligence Management Function Block is the place where Data Lake /
centralized Knowledge Base (cKB) as a "Shared Data repository" used by the three Closed
Control loops should be located. It is also the place where “Centralized” decision-making
element (Centralized_DE) are located.
Both types of Decision-Making-Elements or Decision Elements (DEs) are either Logically
Centralized or Distributed Control Software Logics (DEs) that operate in different time-scales
but interworking harmoniously in realizing autonomic behaviors:
•   Self-configuration,
•   Self-optimization,
•   Self- Healing



© TM Forum 2021. All Rights Reserved.                                                       Page 56 of 57
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



•   Self-* of Managed Entities




Figure 8.7. ODA Intelligence Management Deployment option 1


Distributed / Local / Fast decision-making element or “d_DE” (per ODA Function Block) design
principle

This distributed decision-making logic with less complex Analytics for Autonomics / AI
(Cognitive) Algorithms is realized by fast control loops located in each of the three ODA
Function Blocks. This is reflected at the left-hand-side of Figure 7-7.
In order to distinguish distributed / local / fast Decision-Making-Elements associated with the
three horizontal ODA Function Blocks, we gave them a specific name and color:
•   Yellow fast Closed Control loop) or AI / ML / Cognitive Business (CRM): “Party
    Management Closed Control Loop” with its “Business & Marketing” CRM Knowledge Base
    and its “Decision-Making Logics” (AI Algorithms e.g., those provided by the industry, …)
•   Orange fast Closed Control loop or AI / ML / Cognitive Business (Flexible Offer & Business
    Assurance) : “Core Commerce Management Closed Control Loop” with its “Business &
    Marketing” Knowledge Base and its “Decision-Making Logics” (AI Algorithms e.g., those
    provided by the industry,…)
•   Green fast Closed Control loop or AI / ML / Autonomics / Cognitive Service Assurance:
    “Production Closed Control Loop” with its "Resource & Service” and its “Decision-Making
    Logics” (AI Algorithms e.g., ETSI GANA Decision-Making-Elements (DMEs) Algorithms)
•   Purple fast Closed Control loop or AI / ML / Autonomics / Cognitive (Dynamic Front-End-
    Interaction): “Engagement Closed Control Loop” with its “Front-End” Knowledge Base and
    its “Decision-Making Logics” (AI Algorithms e.g., those provided by the industry…)




© TM Forum 2021. All Rights Reserved.                                                Page 57 of 58
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Interworking between Closed Control loops and concept of Delegations-Escalation-
Synchronization design principle
Those four Closed Control loops (their associated Decision-Making-Elements) may interact to
fulfill business and operations objective. Therefore, they can be configured hierarchically
(nested) and each control-loop’s operation is characterized by a specific life cycle.
•   Those four Closed Control loops shall interact in a coordinated manner per design to
    prevent any conflicts that may happen. Therefore, Delegations-Escalation-Synchronization
    rules along with mapping tables (relationships between Decision-Making-Elements and
    associated policy-controlled Managed Entities) shall be specified to ensure a
    stable interworking of the control-loops for achieving a common efficient decision-making
    objective (conflict-free). Both Top-Down nesting & interworking and Button-up can be
    considered.
•   There is a need for specifying Reference Points /APIs to reflect on those vertical
    interactions between the four Closed Control Loops categories as depicted in Figure 4-19.
    The specification of those Reference Points are implementation-specific (see IG1177)
Logically Centralized / Outer / Slow decision-making design principle
This logically centralized / slow decision-making logic with complex Analytics for Autonomics /
AI (Cognitive) Algorithms is realized by slow control loops located in the ODA Management
Plane or Control Plane associated within each of the three ODA Function Blocks (Party
Management, Core Commerce Management, Production Block) respectively.
In order to distinguish logically centralized / outer / Slow closed Control loops associated with
the four ODA Function Blocks coloring has been synchronized with ODA FA.
Key Implementation requirements associated with Decision-Making-Elements (DMEs) (for
Centralized DMEs and Distributed DMEs) are defined in IG1177.
Synchronization between local Knowledge Bases and Centralized Knowledge Base (cKB)
architecture requirements
ODA shall specify an interface at the Intelligence Management Function Block with
the purpose to updating and synchronizing Local Knowledge Bases and Centralized Knowledge
Bases. It is noted that the Intelligence Management Function Block should be the place where
Data Lake / centralized Knowledge Base (cKB) as a "Shared Data repository" used by the three
Closed Control loops) is located and managed and made available to be consumed by any
authorized "Entity" and audited and verified by the Regulator. Those three Reference Points
/ Interfaces as shown in Figure 4-19 are subject to specification and IG1177.
•   ODA Knowledge Base (Shared Data Repository) shall manage the storage of the content
    (Data / Knowledge) only and make it available to any authorized consumer through Publish
    / Subscribe, Query & Find process.
•   The processing of Knowledge / Data shall be handled elsewhere in Analytical Modules or in
    DMEs or both


ODA Knowledge Base and Regulation architecture requirements
ODA shall specify a reference point then make it available to Regulator to allow this
Body verifying and auditing Data Governance, Provenance and Placement including GDPR
enforcement at each of the three ODA Function Blocks by interacting with their respective
Knowledge Bases as well as with "centralized" Knowledge Base (cKB as shown in Figure 4-19).




© TM Forum 2021. All Rights Reserved.                                                 Page 58 of 59
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



                  8.5.2. Deployment Scenario 2 - Instantiation of ETSI GANA Framework unto ODA
                       Intelligence Management
The scope of the Intelligence Management Function Block is considered to be equivalent to
that described in ETSI Generic Autonomic Network Architecture (GANA) specified in ETSI
103 195-2. Figure 7-8 depicts the mapping of ETSI Generic Autonomic Network Architecture
(GANA) with ODA Intelligence Management and Production Function Block. This Mapping can
involve the other ODA Function Blocks as illustrated in the deployment scenario below.




Figure 8.8. Intelligence Management Deployment option 2: Instantiation of ETSI GANA Framework
onto ODA Intelligence Management


Table 17. Illustrates Mapping / Instantiation

ETSI GANA Knowledge Plane                     ODA Knowledge
•    GANA Centralized Closed-                 •    ODA Centralized Closed-Control Loops (cDEs)
     Control Loops (cDEs) with                     with Analytics
     Analytics
•    ONIX (Overlay Network         •               ODA Knowledge Base / Shared Data
     Information exchange Servers)                 Repository
•    MBTS (Model Based Translation •               Translator of data from multiple sources in
     Service)                                      order to create federated information or data
                                                   models
GANA Network Element /                        ODA Production Element / Managed Entities
Managed Entities (MEs)                        (MEs)
•    GANA Nodes                               •    ODA Nodes


© TM Forum 2021. All Rights Reserved.                                                  Page 59 of 60
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



ETSI GANA Knowledge Plane                     ODA Knowledge
•    Function (Network Function)              •    ODA Network Functions
•    Protocols / Mechanisms                   •    ODA Services (Microservices)
•    Managed Entity Components                •    ODA Components
GANA Network Elements                         ODA Production Elements' distributed Closed-
distributed Closed-Control Loops              Control Loops (dDEs)
(dDEs)
•    Network Element-level d_DE               •    Network Element-level d_DE
•    Node-level d_DE                          •    Node-level d_DE
•    Function (Network Function)-             •    Function (Network Function)-level d_DE
     level d_DE
•    Protocol / Mechanism-level               •    Service (Microservice)-level d_DE
     d_DE


For detailed implementation scenarios, please refer to Appendix A.




© TM Forum 2021. All Rights Reserved.                                                  Page 60 of 61
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




9. ADMINISTRATIVE APPENDIX

                    9.1. References
                  9.1.1. Core References
•     Open Digital Architecture Whitepaper -
      https://www.tmforum.org/resources/whitepapers/open-digital-architecture/
•     OSS of the Future - https://www.tmforum.org/resources/whitepapers/oss-of-the-future/
•     Open Digital Architecture Vision - IG1166 Open Digital Architecture Vision R18.0.0
•     Open Digital Architecture Concepts & Principles - GB998 Open Digital Architecture (ODA)
      Concepts & Principles R18.0.0

                  9.1.2. Other Related References
•     GB1022 ODA Functional Architecture Guidebook v2.0.0.
•     IG1176 TOSCA Guide for Model-Driven Automation R19.0.0
•     GB999 ODA Production Implementation Guidelines R19.0.0
•     IG1130F SDN/NFV impacts on TAM Knowledge Management R19.0
•     IG1157 Digital Platform Reference Architecture Concepts and Principles R19.0.1

                  9.1.3. Terminology
•     Open Digital Architecture Terminology - TMF071 ODA Terminology R18.0.0)



                    9.2. Document History
                  9.2.1. Version History

Version        Date           Modified by: Description of changes
Number         Modified
0.1            31-May-        Emmanuel A. Initial Version
               2018           Otchere
1.0.0          26-Jun-        Alan Pope           Minor edits prior to publication
               2018
1.0.1          16-Jul-        Adrienne            Formatting/style edits prior to R18 publishing
               2018           Walcott
1.0.2          30-Nov-        Brice               Update of Reference Interface Description, for
               2018           Petitfrère          each ODA block
1.0.3          04-Dec-        Sylvie              Update of eTOM and SID mappings, for each
               2018           Demarest            ODA block. Add of SID ABEs definitions, for
                                                  each ODA block


© TM Forum 2021. All Rights Reserved.                                                  Page 61 of 62
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Version        Date           Modified by: Description of changes
Number         Modified
2.0.0          28-Dec-        Alan Pope           Final edits prior to release.
               2018
3.0.0          25-Jun-        Alan Pope           Final edits prior to release.
               2019
3.0.1          17-Oct-        Adrienne            Updated to reflect TM Forum Approved Status
               2019           Walcott
4.0.0          02-Dec-        Alan Pope           Final edits prior to release.
               2019
4.0.1          24-Feb-        Adrienne            Updated to reflect TM Forum Approved Status
               2020           Walcott
5.0.0          30-Jan-        Alan Pope           Final edits prior to publication
               2020
5.0.1          24-Mar-        Adrienne            Updated to reflect TM Forum Approved Status
               2020           Walcott
5.1.0          28-Jan-        Emmanuel A. Restructured as an exploratory document for
               2021           Otchere     ODA-FA advancement
5.1.0          26-Mar-        Adrienne            Updated to reflect TM Forum Approved Status
               2021           Walcott
6.0.0          02-Apr-        Alan Pope           Final edits prior to publication
               2021

                  9.2.2. Release History

Release            Date                 Modified by:       Description of changes
Status             Modified
18.0.0             12-July-2018 Alan Pope                  Initial Release
18.5.0             28-Dec-2018 Alan Pope                   New Release
19.0.0             25-Jun-2019 Alan Pope                   New Release
19.0.1             17-Oct-2019 Adrienne                    Updated to reflect TM Forum Approved
                               Walcott                     Status
Pre-               02-Dec-2019 Alan Pope                   New Release
production
Production         24-Feb-2020 Adrienne                    Updated to reflect TM Forum Approved
                               Walcott                     Status




© TM Forum 2021. All Rights Reserved.                                                 Page 62 of 63
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Release            Date                 Modified by:       Description of changes
Status             Modified
Pre-               31-Jan-2020 Alan Pope                   New Version
production
Production         24-Mar-2020 Adrienne                    Updated to reflect TM Forum Approved
                               Walcott                     Status
Pre-               29-Jan-2021 Alan Pope                   Updated to version 5.1.0
production
Production         26-Mar-2021 Adrienne                    Updated to reflect TM Forum Approved
                               Walcott                     Status
Pre-               02-Apr-2021 Alan Pope                   Updated to version 6.0.0
production
Production         24-May-2021 Adrienne                    Updated to reflect TM Forum Approved
                               Walcott                     Status



                    9.3. Acknowledgements
This document was prepared by the members of the TM Forum ODA project:
•   Sylvie Demarest, Orange
•   Emmanuel A. Otchere, Huawei Technologies Co. Ltd
•   Alexis de Peufeilhoux, Deutsche Telekom AG
•   Brice Petitfrère, Orange
•   Daniela Galigniana, Telefónica
•   Dave Milham, TM Forum
•   Eric Troup, Microsoft Corporation
•   Johanne Mayer, Telstra
•   Tayeb Ben Meriem, Orange
•   Cecile Ludwichowski, Orange




© TM Forum 2021. All Rights Reserved.                                                   Page 63 of 64
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




10. Appendix A: Detailed Intelligence
    Management Implementation Scenarios

                    10.1. INTRODUCTION
                  10.1.1.    Deployment Flavors / Features / Scenarios / Options | or How to use
ODA Intelligence Management categories
For the four use cases described in this section, we are considering two categories of ODA:
1. Home ODA. It is controlled by a Digital Service Provider (DSP)
2. External ODA. It is controlled by a DSP's Partner


This categorization refers to the concept of ownership defined earlier which sets the
responsibility demarcation from an autonomic perspective. It defines how embedded
Autonomic / AI / Cognitive capabilities are arranged within the ODA (relationships between
DEs and MEs inside a given ODA category).
All Managed Entities considered in this section belong to the Production Function Block of the
ODA Functional Architecture. But this principle could apply to the two other horizontal ODA
Function Blocks as well.
Use Case 1: Hierarchy of ODAs
This use case illustrates the situation where two ODAs (Home ODA and External ODA) are
collaborating from decision-making perspective under hierarchical relationship. This model is
built when there is a need for "Delegation - Escalation-Synchronization" operations to prevent
conflicts that may happen in such a model.
Figure 10-1 depicts this use case. It is made of two "ODAs":
•   External ODA. It contains an "External Autonomic Manager" positioned at Upper / Higher
    level in the hierarchical model. Its policy-controls the Home Autonomic Manager belonging
    to the Home Domain.
•   Home ODA. It contains a " Home Autonomic Manager" positioned at Lower level in the
    hierarchical model. It is policy-controlled by the External Autonomic Manager
•   This interaction is shown by the yellow arrow.




© TM Forum 2021. All Rights Reserved.                                                      Page 64 of 65
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 10.1. Hierarchy of ODAs


Use Case 2: Federation of ODAs (Peering / Sibling model)
This use case illustrates the situation where two ODAs (Home ODA and External ODA) are
collaborating from decision-making perspective under federation relationships. This model is
built when there is a need for federating ODAs to deliver E2E service, for instance E2E Network
Slice crossing two ODAs. Cognitive Fulfillment & Service Assurance of the E2E Network Slice
necessitate E2E decision-making cross those two ODAs.
Figure 10-2 depicts this use case. It is made of two "ODAs"
•   External ODA. It contains an "External Autonomic Manager" positioned as the same level
    w.r.t. a Home Autonomic Manager.
•   Home ODA. It contains a " Home Autonomic Manager" positioned at the same level as an
    External Autonomic Manager
•   This interaction is shown by the yellow arrow
External Autonomic Manager is seen as a Peer from Home Autonomic Manager perspective.




© TM Forum 2021. All Rights Reserved.                                              Page 65 of 66
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 10.2. Federation of two ODAs (Peering / Sibling model)


Use Case 3: An Autonomic Manager belonging to an ODA is allowed to interact directly with a
Managed Entity that is not its own

This use case illustrates the situation where two ODAs are collaborating from decision-making
perspective when an External ODA needs to consume services exposed by some Home
Managed Entities by policy-controlling them directly without the need to rely on the Home
Autonomic Manager. There are some real use cases where such a service consumption model
is relevant. This use case respects and enforces the Ownership rules because External
Autonomic Manager cannot change the configuration of the Home Managed Entities (it is not
allowed to do so).
Figure 10-3 depicts this use case. It is made of two "ODAs".
1. External ODA. It contains an "External Autonomic Manager". Its policy-controls the
   targeted Home Managed Entity. It is not allowed to change the configuration of the Home
   Managed Entity.
2. Home ODA. It contains a " Home Autonomic Manager" and the Home Managed Entity
   exposing services. Home Autonomic Manager has the right to change the configuration of
   this Home Managed Entity.
3. This interaction is shown by the yellow arrow.




© TM Forum 2021. All Rights Reserved.                                             Page 66 of 67
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 10.3. External Autonomic Manager interacting directly with Home Managed Entity that it does
not own
Use case 4: An Autonomic Manager belonging to an ODA needs to communicate with a
Managed Entity that is not its own via an Autonomic Manager that owns and manages this
Managed Entity

This use case is a variant of use case 3. The only difference is that External Autonomic Manager
is not allowed to interact directly with Home Managed Entities. For consuming service exposed
by Home Managed Entities, External Autonomic Manager has to rely on the Home Autonomic
Manager.




© TM Forum 2021. All Rights Reserved.                                                   Page 67 of 68
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




This interaction is shown by the yellow arrow
Figure 9-4 depicts this use case




Figure 10.4. External Autonomic Manager communicates with non-owned Home Managed Entities via
owning Home Autonomic Manager

                  10.1.2.    Implementation flavors of ODA Knowledge Plane
ODA Knowledge Plane
The scope of the ODA Knowledge Plane is considered to be equivalent to that described in ETSI
GANA (Generic Autonomic Network Architecture) Knowledge Plane specified in ETSI TS 103
195-2. As explained and depicted in Figure 9-5 ( left-hand side) and in Figure 9-6, ODA
Knowledge Plane is placed in the Intelligence Management Function Block. It is the Brain for
Implementers to design and Implement Advanced Cognitive Management & Control DE
Algorithms (not subject to standardization) to allow them to differentiate each other and make
those Algorithms available to Digital Service Providers to select / choose / purchase the Best-in
Class solutions.
This ODA Knowledge Plane is made of the following entities:
•   Data Lake / Centralized / Shared Knowledge Base (cKB) populated by data from all the ODA
    Function Block and other sources (e.g., Events and KPIs) from PNFs/VNFs, Probes, Data
    Collectors. Raw Data collected are processed and translated onto Knowledge with
    common semantic and made available under Publish / Subscribe, Query & Find
    paradigm to be consumed by the centralized Decision-Making-Elements (DMEs) or
    Decision Elements (DEs).




© TM Forum 2021. All Rights Reserved.                                                Page 68 of 69
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



•   Three categories of Knowledge Planes compose ODA Knowledge Plane:
     1. PM_KP: Party Management Knowledge Plane. It contains its Decision
        Elements (PM_DEs) with complex Analytics for Autonomics / AI (Cognitive)
        Algorithms
     2. CC_KP: Core Commerce Management Knowledge Plane. It contains its Decision
        Elements (CC_DEs) with complex Analytics for Autonomics / AI (Cognitive) Algorithms.
     3. P_KP: Production Knowledge Plane. It contains Decision Elements (CC_DEs) with
        complex Analytics for Autonomics / AI (Cognitive) Algorithm.




Figure 10.5. ODA Deployment option 1 (ODA-native)




© TM Forum 2021. All Rights Reserved.                                              Page 69 of 70
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 10.6. ODA Knowledge Plane


ODA Knowledge Plane interworking models
Figure A-7 depicts two models for the articulation and interworking between the three ODA
Knowledge Planes:
•   Hierarchical model
In this model, there is a need for building a top-level Knowledge Plane we named "ODA Master
Knowledge Plane". This ODA Master Knowledge Plane is setting on the top and policy-controls
the three other Knowledge Planes. To achieve this model, there is a need for defining
reference points / Interfaces to exchange information / KPIs between ODA Master Knowledge
Plane and the three ODA Knowledge Planes to perform a holistic decision-making across the
three Knowledge Planes.
•   Federated model
In this model, the three ODA Knowledge Planes are at the same level. The federation needs
defining "East-West" Reference points / Interfaces between those ODA Knowledge Planes.




© TM Forum 2021. All Rights Reserved.                                            Page 70 of 71
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 10.7. ODA Master Knowledge Plane (Hierarchy of Knowledge Planes)


•   Unique Knowledge Plane model
It is to be noted that ETSI GANA TS 103194 specified a "unique Knowledge Plane" so called
"GANA Knowledge / Dissemination Plane" who interacts with three layers (Business, Service,
Infrastructure), http://www.etsi.org/deliver/etsi_ts/103100_103199/103194/01.01.01_60/ts_
103194v010101p.pdf
Recommendation
ODA Functional Architecture Intelligence Management proposes these ODA Knowledge Plane
models but does not prescribe any implementation solution. This is left to the Knowledge
Planes and Algorithms designers / Implementers.




© TM Forum 2021. All Rights Reserved.                                          Page 71 of 72
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



Componentization view of Production Knowledge Plane (P_KP) (Centralized / Slow Control-
loops) Autonomic Managers (DEs) and distributed /Fast Control-loops (DEs)
The concept of Knowledge Plane was introduced in ODA deployment option1 from design
perspective and from a holistic view at each of the three horizontal ODA Function Blocks. The
focus in this deployment option 2 is on componentization related aspect of the Decision-
Making-Element (DME) or Autonomic Manager and its interfaces and associated primitives
within the scope of Production Function Block.
The componentization of the ODA Autonomic Manager Elements (DMEs) either Knowledge
Plane DMEs or distributed DMEs embedded in ODA Nodes is considered to be equivalent to
that described in ETSI Generic Autonomic Network Architecture (GANA) Knowledge
Plane specified in ETSI TS 103 195-2
•   ODA Autonomic Manager (DME) component view (Macro / Centralized -control loop or
    micro / distributed control loop)
An Autonomic Manager Element (DME or DE) as a component is equipped with 3 categories of
interfaces:
1. S_I: Sensory interface (the same interface is also embedded in the Managed Entity to allow
   the Autonomic Manager Element to policy-control Managed Entities)
2. Ef_I: Effector interface (the same interface is also embedded in the Managed Entity to
   allow the Autonomic Manager Element to policy-control Managed Entities)
3. DE to DE_I: Autonomic Manager Element to Autonomic Manager Element interface to
   allow an Autonomic Manager Element to federate with another one


•   ODA Node (embedding Distributed / Fast Control-loops or micro -Autonomic Manager
    Elements) component view
This ODA Node is the counterpart of a Network Element (NE) in the Non-ODA platform, but it
is made of Managed Entities (MEs) embedding micro Autonomic Managers Element(s). The
ODA Managed Entity (ME) as a component is equipped with 4 categories of interfaces:
1. Ss_I: Sensory interface
2. Ef_I: Effector interface
3. SR_I: Service Requesting interface (it allows this Managed Entity to consume services
   provided by others)
4. SP_I: Service Providing interface (it is about the purpose of the Managed Entity it is
   designed for e.g., the service it provides)
Implementation flavors of ODA Autonomic Managers (DEs) as components
• ODA by design will follow principle of Cloud-Native which includes microservice -style
   implementation.
•   ODA DMEs (DEs) will follow ETSI GANA implementation guide (TS 103 295-2) which
    considers DE as "overlay software" inserted to run on top of the resources layer (ODA
    Production Function Block) and recommends the two implementation flavors described
    below which are compliant with Cloud native and microservice principles:
•   Implementation flavor 1 - Individual Autonomic Managers (DEs) can be implemented as a
    singly merged run-time entity (e.g., a process)
•   Implementation flavor 2 - Individual Autonomic Managers (DEs) can be implemented to
    run as standalone processes (or threads for example) at run-time.



© TM Forum 2021. All Rights Reserved.                                                Page 72 of 73
IG1167 ODA Functional Architecture Exploratory Report v6.0.0



How to introduce AI / Autonomic / Cognitive capabilities in ODA Production Function Block:
case study
While the deployment option 2 depicted in Figure 10-9 is already covering Autonomic and
Cognitive related aspects within Production Function Block, the main focus is at the fine grain
of decomposition in the Production Function Block from an autonomic perspective. Autonomic
Managers Centralized DME and Distributed DMEs) as well as Managed Entities (MEs) are
considered as components, all interacting via their sensory interfaces and Effector interfaces
and associated Operations / Primitives. In contrast, in the case study described here and
depicted in Figure 10-8, we are looking at Autonomic and Cognitive capabilities in Production
Function Block at "systems" level abstracting component view. In this regard, we consider
Production Function Block following SDN / NFV deployment. The exercise consists in
empowering this Production Function Block with Autonomic and Cognitive capabilities to make
it "Autonomic & Cognitive-Aware". As described in Figures 10-5 and 10-10 we will consider the
two levels of Autonomic Manager Elements (DMEs or DEs), centralized one and distributed
one.
Step 1
•   Embedding distributed DEs in the ODA Managed Entities of the Production Function
    Block, either Physical ones, we named "ODA PhyME" (ODA Production Physical Managed
    Entity) or virtualized ones we named "ODA_vME" (ODA Production virtualized Managed
    Entity),
Step 2
•   Empowering "ODA Managers": ODA Service Orchestrator, ODA Network Orchestrator,
    ODA VNF Manager, ODA VIM, ODA SDN Controller (SDN-C), EMS by Production Knowledge
    Plane Decision Elements (P_DEs) logic. In this model, P_DEs software logic is considered as
    an application interacting with each ODA Manager via their Northbound interface / API.




Figure 10.8. How to introduce AI / Autonomic / Cognitive capabilities in ODA Production Function Block:
case study




© TM Forum 2021. All Rights Reserved.                                                     Page 73 of 74
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Relevance of this case study to Service Providers
This case study is of high interest to Service Providers who are facing various paradigms
SDN / NFV, Service Orchestration, Big Data Analytics, Autonomic, Self- Management &
Cognitive networking. Those paradigms all are sharing a common roadmap and targeting the
same objective. Therefore, combining them constitutes a key enabler to 5G Network Slice
Service Assurance. Extensive work in this space has been carried out by ETSI GANA, in one
hand (see Note 1 below) and by a Multi-SDO joint activity, in the other hand (See Note 2
below)
Note 1: This use case is a high level adaptation from ETSI GANA case study (instantiation of
ETSI GANA onto SDN, NFV, Service Orchestration) depicted in Figure 9-6 of
http://www.etsi.org/images/files/ETSIWhitePapers/etsi_wp16_gana_Ed1_20161011.pdf
Note 2: This detailed architecture can be found in the Workshop Report from the Initiative:
Joint SDOs/Fora Industry Harmonization for Unified Standards on AMC, SDN, NFV, E2E
Orchestration, Software-oriented enablers for 5G: Joint SDOs/Fora Workshop Report from the
workshop held on 4th June 2015 at the TM Forum Live 2015 http://projects.sigma-
orionis.com/eciao/wp-content/uploads/2015/07/Report-on-Joint-SDOs-Industry-
Harmonization-for-Unified-Standards-on-AMC_SDN_NFV_E2E-
Orchestration_ver3.01.compressed.pdf




© TM Forum 2021. All Rights Reserved.                                               Page 74 of 75
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




11. BUSINESS SCENARIOS / USE CASE
                  11.1.1.    ODA and legacy BSS/OSS (INFORMATIVE)
Legacy to ODA-native deployment option in a Transition phase

Figure 11-1 depicts this deployment option. In this case we consider the ODA Intelligence
Management (Autonomic / AI / Cognitive) capabilities are embedded in the Production
Function Block only which is the Function Block of the ODA Functional Architecture that is
relevant from migration path perspective when it comes to introduce ODA at an early stage, it
shows the interaction with a Non-ODA Platform. The main characteristics and requirements
associated with this deployment option are:
•   From the ODA Knowledge Plane perspective, as depicted in Figures 9-5 and 9-6, we
    consider only P_KP (Knowledge Plane of the Production Function Block). P_KP shall
    interwork with Legacy OSS. To this end, there is a need for specifying:
    - a reference point / API between the Legacy OSS and the Production Knowledge Plane
    (P_KP) we named “OSS_(P_KP)
    - a reference point / API between the Non-ODA Nodes (Legacy Managed Entities, in this
    case it is about Managed Elements in traditional management-style sense) and the
    Production Knowledge Plane (P_KP). We named this reference point “L_(P_KP)” (Legacy to
    P_Knowledge Plane)
•   The Production Knowledge Plane (P_KP) shall embed capabilities to manage Non-ODA
    Managed Entities (MEs) or Network Elements (NEs) for the purpose of the transition
    phase. This is the reason why there is a need for specifying this “L_(P_KP)” reference point.
•   There is no need to evolve (upgrade) the Legacy OSS not only for cost saving reasons
    (upgrading the legacy OSS is time and cost consuming) but mainly for moving away from
    the Legacy OSS to the ODA-native-style which embeds advanced Management & Control
    capabilities (it is “Intelligent and Cognitive i.e., Autonomic per design”). Those Autonomic
    & Cognitive capabilities are enablers for new value stream creation mainly in the 5G
    Network Slice space for verticals.
•   Well-Known traditional management interfaces associated with Non-ODA
    Platforms are indicated:
             o    SBI (South Bound Interface: between Legacy Managed Entities (MEs) and
                  EMS (Element Management System)
             o    NBI (North Bound Interface) between EMS and NMS (Network Management
                  System)




© TM Forum 2021. All Rights Reserved.                                                 Page 75 of 76
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 11.1. ODA Deployment option 2: Legacy to ODA

                  11.1.2.    Managing Federation of ODA
ODA Intelligence Management Federated Framework

a) Federation under Multiple ODA Knowledge Planes scenario
Figure 11-2 depicts this deployment option 3. In this case, two ODA-native instances (ODA #1
and ODA #2) are interworking within a federated model. The use case behind this federated
model is the case where ODA #1 belongs to a Digital Service Provider DSP #1 and ODA #2
belongs to a Digital Service Provider DSP #2. Each ODA instance is embedding AI / Autonomic /
Cognitive capabilities at the three horizontal Function Blocks of the ODA Functional
Architecture as depicted in Figure 10-5 (ODA-native deployment option 1).
The main characteristics and requirements associated with this option are:
•   The Party Management Closed Control Loop of ODA #1 needs to exchange information,
    KPIs with the Party Management Closed Control Loop of ODA #2 for E2E Cross –ODA
    decision-making. There is a need for specifying a reference point / API between those two
    Closed Control Loops we named “PM_PM". This federation is at Knowledge Panes
    levels (Party Management Knowledge Plane) "PM_KP" as defined in deployment option 1.
•   The Core Commerce Management Closed Control Loop of ODA #1 needs to exchange
    information, KPIs with the Core Commerce Management Closed Control Loop of ODA #2
    for E2E Cross-ODA decision-making. There is a need for specifying a reference point / API
    between those two Closed Control Loops we named “CC_CC”. This federation is at
    Knowledge Panes levels (Core Commerce Management Knowledge Plane) "CC_KP" as
    defined in deployment option 1.




© TM Forum 2021. All Rights Reserved.                                              Page 76 of 77
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




•   The Production Closed Control Loop of ODA #1 needs to exchange information, KPIs with
    the Production Closed Control Loop of ODA #2 for E2E Cross-ODA decision-making. There is
    a need for specifying a reference point / API between those two Closed Control Loops we
    named "P_P”. This federation is at Knowledge Plane levels (Production Knowledge
    Plane) "P_KP" as defined in deployment option 1, It corresponds to the interworking
    between the two Knowledge Planes as specified by GANA (ETSI TS 103 195-2).




Figure 11.2. ODA Intelligence Management Federated Framework (multiple ODA Knowledge Planes
scenario)


a) Federation under a single ODA Knowledge Plane scenario
Figure 11-3 depicts the same Framework as the one depicted in Figure 11-2, but ODA
Intelligence Management is composed of a single (Unique) Knowledge Plane that can interact
with the four other ODA Function Blocks.




© TM Forum 2021. All Rights Reserved.                                              Page 77 of 78
IG1167 ODA Functional Architecture Exploratory Report v6.0.0




Figure 11.3. ODA Intelligence Management Federated Framework (Single / Unique ODA Knowledge
Plane scenario)


Note - This Federated Framework focuses on Federation of two ODA-native instances, but we
think this federation model could apply to interworking / federating between an ODA-native
instance and any other "System" / "Platform" (e.g., ONAP Platform, Vendor-specific Platform)
as far as this peer Entity exhibits / exposes the interworking reference points / interfaces
described earlier.




© TM Forum 2021. All Rights Reserved.                                              Page 78 of 78

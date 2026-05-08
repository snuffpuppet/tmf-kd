TM Forum Standard
Information Framework (SID)
Service Domain Business Entities
Information Framework Suite
GB922 Domain Business Entities

Release R25.0.0




       Maturity Level: General Availability (GA)   Team Approved Date: 18-Jul-2025
       Release Status: Production                  Approval Status: TM Forum Approved
                                                   Suitable for Conformance
       Version 25.0.0                              IPR Mode: RAND
Service Domain

Information Framework (SID) Suite R25.0.0




Notice
Copyright © TM Forum 2025. All Rights Reserved.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist
in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the
above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in
any way, including by removing the copyright notice or references to TM FORUM, except as needed for the purpose of developing any document or
deliverable produced by a TM FORUM Collaboration Project Team (in which case the rules applicable to copyrights, as set forth in the TM FORUM
IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by TM FORUM or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and TM FORUM DISCLAIMS ALL WARRANTIES, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP
RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.


TM FORUM invites any TM FORUM Member or any other party that believes it has patent claims that would necessarily be infringed by
implementations of this TM Forum Standards Final Deliverable, to notify the TM FORUM Team Administrator and provide an indication of its
willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the TM FORUM Collaboration Project Team
that produced this deliverable.

The TM FORUM invites any party to contact the TM FORUM Team Administrator if it is aware of a claim of ownership of any patent claims that would
necessarily be infringed by implementations of this TM FORUM Standards Final Deliverable by a patent holder that is not willing to provide a license
to such patent claims in a manner consistent with the IPR Mode of the TM FORUM Collaboration Project Team that produced this TM FORUM
Standards Final Deliverable. TM FORUM may include such claims on its website but disclaims any obligation to do so.

© TM Forum 2025. All Rights Reserved.                                                                               Page 2 of 177
Service Domain

Information Framework (SID) Suite R25.0.0



TM FORUM takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the
implementation or use of the technology described in this TM FORUM Standards Final Deliverable or the extent to which any license under such
rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on TM FORUM's
procedures with respect to rights in any document or deliverable produced by a TM FORUM Collaboration Project Team can be found on the TM
FORUM website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an
attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this TM FORUM
Standards Final Deliverable, can be obtained from the TM FORUM Team Administrator. TM FORUM makes no representation that any information
or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.


Direct inquiries to the TM Forum office:

100 Enterprise Drive
Suite 301 #1649
Rockaway, NJ 07866 USA
Tel No. +1 973 944 5100
TM Forum Web Page: www.tmforum.org




© TM Forum 2025. All Rights Reserved.                                                                                Page 3 of 177
Service Domain

Information Framework (SID) Suite R25.0.0




Table of Contents
Notice.............................................................................................................................................................................................................. 2

1    General Information .................................................................................................................................................................................. 11

2    Typographic Conventions .......................................................................................................................................................................... 11

3    Glossary ................................................................................................................................................................................................... 12

4    Service Domain ......................................................................................................................................................................................... 13
    4.1   Service Domain Overviews .................................................................................................................................................................................. 13
     Figure [SeD-01] Service ABEs Level 1 ......................................................................................................................................................................... 14
     Figure [SeD-02] Service ABEs Level 1 & 2.................................................................................................................................................................... 18
    4.2   Service Party Roles ABE ....................................................................................................................................................................................... 21
     Figure SO.00 - Service Party Roles ............................................................................................................................................................................. 21
    4.3   Service Specification ABE .................................................................................................................................................................................... 22
     Figure SO.03 - Subclassing ServiceSpecification (OLD SO.10) .................................................................................................................................... 22
     Figure SO.04 - Simplified SID Product Model .............................................................................................................................................................. 26
     Figure SO.08 - Service Specifications and other Domains ........................................................................................................................................... 28
     Figure SO.09 - VPNService – VPNServiceSpecification Example .................................................................................................................................. 32
     Figure SO.11 - Modeling Stand-Alone and Aggregate ServiceSpecifications ................................................................................................................. 35

© TM Forum 2025. All Rights Reserved.                                                                                                                                             Page 4 of 177
Service Domain

Information Framework (SID) Suite R25.0.0



    Figure SO.13 - Modeling the Versioning of a ServiceSpecification ................................................................................................................................ 37
    Figure SO.14 - The Concept of a ServiceSpecificationType.......................................................................................................................................... 39
    Figure SO.17 - The Concept of ServiceSpecificationRoles (OLD SO.21) ....................................................................................................................... 41
    Figure SO.18 - Interaction Between ServiceSpecRoles and ResourceSpecRoles.......................................................................................................... 43
    Figure SO.22 -The Concept of ServiceSpecCharacteristic........................................................................................................................................... 44
    Figure SO.22a - Service and Resource Characteristic Associations ............................................................................................................................. 46
    Figure SO.23 - ServiceCharacteristicValue and ServiceSpecCharacteristicValue ........................................................................................................ 48
    Figure SO.24 - Multiple Command Syntaxes and Programming Models ....................................................................................................................... 50
    Figure SO.25 - The Concept of a ServicePackage ........................................................................................................................................................ 52
    Figure SO.26 - Grouping Together CustomerFacingServiceSpecifications into a ServicePackage ................................................................................. 54
    Figure SO.27 - ServicePackageSpecs and ServicePackages ........................................................................................................................................ 56
    Figure SO.28 - Relationship Between ServiceBundleSpec and ServicePackageSpec .................................................................................................... 58
    Figure SO.29 - ServiceBundles and ServiceBundleSpecifications ................................................................................................................................ 61
    Figure SO.30 - Summary Relationships Between ServicePackage and ServiceBundle .................................................................................................. 63
    Figure SO.31 - Resource Facing Service Specification Pattern .................................................................................................................................... 65
    Figure SO.32 - Usage Volume Service Specification .................................................................................................................................................... 66
    Figure SO.33 NetworkProductSpec / NetworkServiceSpec relationships..................................................................................................................... 68
    4.3.1     Customer Facing Service Spec ABE................................................................................................................................................................ 69
      Figure CFSS.01 - Customer Facing Service Spec ABE Related Entities ...................................................................................................................... 69
      4.3.1.1      Customer Facing Service Spec Examples ABE .......................................................................................................................................... 71
         Figure CFSSE.01 - Customer Facing Service Spec Examples ABE Related Entities ................................................................................................. 71

© TM Forum 2025. All Rights Reserved.                                                                                                                                    Page 5 of 177
Service Domain

Information Framework (SID) Suite R25.0.0



        4.3.1.2      Customer Facing Service Spec Role ABE .................................................................................................................................................. 73
          Figure CFSSR.01 Customer Facing Service Spec Role ABE Related Entities ........................................................................................................... 73
        4.3.1.3      Network Service Spec ABE «Preliminary» .................................................................................................................................................. 74
          Figure NSS.01 - Network Service Spec ABE Related Entities .................................................................................................................................. 74
        4.3.1.4      Service Package ABE ............................................................................................................................................................................... 75
          Figure SP.01 - Service Package ABE Related Entities ............................................................................................................................................. 75
          4.3.1.4.1 Service Package Spec Examples ABE .................................................................................................................................................... 76
             Figure SPSE.01 - Service Package Spec Examples ABE Related Entities .............................................................................................................. 76
        4.3.1.5      Usage Volume Service Spec ABE «Preliminary» ......................................................................................................................................... 77
          Figure UVSS.01 - Usage Volume Service Spec ABE Related Entities ....................................................................................................................... 77
    4.3.2      Resource Facing Service Spec ABE ................................................................................................................................................................ 78
        Resource Facing Service Spec ABE Related Entities ................................................................................................................................................ 78
        4.3.2.1      Resource Facing Service Spec Role ABE ................................................................................................................................................... 80
          Figure RFSSR.01 - Resource Facing Service Spec Role ABE Related Entities .......................................................................................................... 80
        4.3.2.2      Service Bundle ABE.................................................................................................................................................................................. 81
          Figure SB.01 - Service Bundle ABE Related Entities ............................................................................................................................................... 81
          4.3.2.2.1 Service Bundle Examples ABE ............................................................................................................................................................... 82
             Figure SBE.01 - Service Bundle Examples ABE Related Entities .......................................................................................................................... 82
    4.3.3      Service Catalog ABE ...................................................................................................................................................................................... 83
        Figure SC.01 - Service Catalog ABE Related Entities ................................................................................................................................................ 83
  4.4     Service ABE......................................................................................................................................................................................................... 84

© TM Forum 2025. All Rights Reserved.                                                                                                                                                 Page 6 of 177
Service Domain

Information Framework (SID) Suite R25.0.0



    Figure SO.06 - Basic Service Model – A Starting Point.................................................................................................................................................. 84
    Figure SO.07 - Representing BGP as a LogicalResource .............................................................................................................................................. 87
    Figure SO.12 - Modeling Stand-Alone and Aggregate Services ..................................................................................................................................... 89
    Figure SO.20 - The Concept of ServiceRoles ............................................................................................................................................................... 90
    Figure SO.35 - Interaction Between PartyRole and Service .......................................................................................................................................... 93
    Figure SO.36 - Interaction between Service and Place ................................................................................................................................................ 96
    Figure SO.37 - NetworkServiceSpec / UsageVolumeServiceSpec instantiation ............................................................................................................ 97
    Figure SO.38 - UsageVolumeService detailed view ..................................................................................................................................................... 99
    4.4.1     Customer Facing Service ABE ...................................................................................................................................................................... 101
      Figure CFS.01 - Customer Facing Service ABE Related Entities .............................................................................................................................. 101
      4.4.1.1      Customer Facing Service Example ABE .................................................................................................................................................. 102
         Figure CFSE.01 - Customer Facing Service Example ABE Related Entities............................................................................................................ 102
      4.4.1.2      CustomerFacing Service Role ABE ......................................................................................................................................................... 103
      4.4.1.3      Network Service ABE «Preliminary»......................................................................................................................................................... 103
         Figure NS.01 - Network Service ABE Related Entities .......................................................................................................................................... 103
      4.4.1.4      Usage Volume Service ABE «Preliminary» ............................................................................................................................................... 104
         Figure UVS.01 - Usage Volume Service ABE Related Entities ............................................................................................................................... 104
    4.4.2     Resource Facing Service ABE ....................................................................................................................................................................... 105
      Figure RFS.01 - Resource Facing Service ABE Related Entities ............................................................................................................................... 105
      4.4.2.1      Resource Facing Service Examples ABE ................................................................................................................................................. 107
         Figure RFSE.01 - Resource Facing Service Examples ABE Related Entities ........................................................................................................... 107

© TM Forum 2025. All Rights Reserved.                                                                                                                                       Page 7 of 177
Service Domain

Information Framework (SID) Suite R25.0.0



        4.4.2.2     Resource Facing Service Role ABE.......................................................................................................................................................... 108
          Figure RFSR.01 - Resource Facing Service Role ABE Related Entities ................................................................................................................... 108
  4.5     Service Configuration ABE ................................................................................................................................................................................. 109
    Figure CP.01 - Configuration Spec and Configuration (copy from Common) .............................................................................................................. 109
    Figure CP.02 - Configuration Specs Associations (copy from Common) .................................................................................................................... 111
    Figure CP.03a - Entities Serve as Configuration Specifications (Copy from Common) ................................................................................................ 112
  4.6     Service Order ABE ............................................................................................................................................................................................. 113
    Figure SOr.01 - Service Order Entities ...................................................................................................................................................................... 114
    Figure SOr.02 - Relationships Inherited From Business Interaction ........................................................................................................................... 115
    Figure SOr.03 - Relationships Inherited From BI Item ................................................................................................................................................ 116
  4.7     Service Usage ABE ............................................................................................................................................................................................ 117
    Figure U.02 - Usage Specification (copy from Common) ........................................................................................................................................... 117
    Figure U.04 - Resource and Service Usage (copy from Common) .............................................................................................................................. 120
    Figure U.06 - Product Usage, Part 2 (copy from Common)......................................................................................................................................... 122
    4.7.1      Service Usage Specification ABE .................................................................................................................................................................. 124
        Figure SUS.01 - Service Usage Specification ABE Related Entities .......................................................................................................................... 124
    4.7.2      Service Usage Entity ABE ............................................................................................................................................................................. 125
        Figure SUE.01 - Service Usage Entity ABE Related Entities ..................................................................................................................................... 125
  4.8     Service Test ABE ............................................................................................................................................................................................... 126
    Figure T.04 - Product, Service and Resource Test Entities (Copy from Common)........................................................................................................ 126
  4.9     Service Performance ABE .................................................................................................................................................................................. 128

© TM Forum 2025. All Rights Reserved.                                                                                                                                               Page 8 of 177
Service Domain

Information Framework (SID) Suite R25.0.0



    Figure SO.37 - Service Level Specification Overview ................................................................................................................................................. 128
    Figure SO.38 - Products, Services, and ServiceLevelAgreements .............................................................................................................................. 130
    Figure SO.39 - Associating Service Level Specifications with Products and Services ................................................................................................. 131
    Figure SO.40 - Service Level Specification Parameters and Objectives ...................................................................................................................... 132
    Figure SO.41 - KPIs, KQIs, Products, and Services .................................................................................................................................................... 133
    Figure SO.42 - ServiceLevelSpecConsequences ...................................................................................................................................................... 134
    Figure SO.43 - ServiceLevelSpecApplicability........................................................................................................................................................... 136
    Figure SO.43a - ServiceLevelSpecificationExpression............................................................................................................................................... 137
    4.9.1     Service Level Spec ABE ................................................................................................................................................................................ 140
      Figure SLS.01 - Service Level Spec ABE Related Entities ........................................................................................................................................ 140
    4.9.2     Service Performance Specification ABE........................................................................................................................................................ 142
      Figure SPS.01 - Service Performance Specification ABE Related Entities ................................................................................................................ 142
  4.10      Service Capacity ABE ..................................................................................................................................................................................... 144
    Figure SC.01 - Basic Capacity Entities (based on CM.02 from Capacity ABE in Common Domain) .............................................................................. 144
    Figure SC.02 - Basic Service Capacity Entities (CM.06 Copy from Capacity ABE in Common Domain) ........................................................................ 148
    Figure SC.03 - Basic Service Demand Entities (CM.09 Copy from Capacity ABE in Common Domain) ........................................................................ 149
  4.11      Service Problem ABE «NotFullyDeveloped» ..................................................................................................................................................... 150
    Figure SP.01 - Service Problem ABE Related Entities................................................................................................................................................. 150
  4.12      Service Strategy & Plan ABE «notFullyDeveloped» ............................................................................................................................................ 152
  4.13      TIP Service Management ABE «likelyToBeDepreciated» .................................................................................................................................... 152
    Figure SO.31 TIP Service Management - Service Definition and Service Template ...................................................................................................... 153

© TM Forum 2025. All Rights Reserved.                                                                                                                                           Page 9 of 177
Service Domain

Information Framework (SID) Suite R25.0.0



      Figure SO.32 TIP Service Management - Service Characteristics ............................................................................................................................... 157
      Figure SO.33 TIP Service Management - Service Activation ....................................................................................................................................... 160
      Figure SO.33a - TIP Service Management - CommonServiceInfo ............................................................................................................................... 163
      Figure SO.34 - Example of Ethernet Service CFS/RFS ................................................................................................................................................ 165

5     Administrative Appendix...........................................................................................................................................................................167
    About this document ................................................................................................................................................................................................. 167
    5.1     Document History ............................................................................................................................................................................................. 167
      Version History ....................................................................................................................................................................................................... 167
      Release History....................................................................................................................................................................................................... 173
    5.3     Acknowledgments ............................................................................................................................................................................................ 176




© TM Forum 2025. All Rights Reserved.                                                                                                                                                 Page 10 of 177
1       General Information
To find the Information framework figure, refer to “GB991 Core Frameworks Concepts and Principles” guidebook.

2       Typographic Conventions
    •   Relationships starting by a “/” correspond to shortcut and represent navigation relationships (aka derived relationship). A derived relationship
        corresponds to several relationships replaced by a unique derived relationship to give a synthetic view. It isn’t needed to implement such
        relationships.
    •   In diagrams, on Business Entities from a different ABE than the ABE being referred to in the diagram, the name after “from” represents the ABE
        where the Business Entity is located.




    •   A Business Entity is represented by a decorator located to the top left.




    •   The Aggregated Business Entity (ABE) is represented similarly to ArchiMate.
    Information Framework (SID) Suite Service Domain R25.0.0




  3       Glossary
   Name            Description

   ABE             Aggregate Business Entity

   BE              Business Entity

   eTOM            enhanced Telecom Operation Map (TMF Framework)

   ODA             Open Digital Architecture

   SID             Shared Information Data model (TMF Framework) is the previous name of Information
                   Framework

   TAM             Telecom Applications Map (TMF Framework) is the previous name of Application Framework




© TM Forum 2025. All Rights Reserved                                                        12              of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4       Service Domain
  One of the goals of the SID model is to enable a seamless transition from business concepts and definitions to other domains, such as
  networking. This addendum covers the definition of services.

  In looking at ‘”Service”, the first problem is one of terminology. Service means many things to many people. For example, many people use
  the words “Product” and “Service” interchangeably. In addition, though Resources are usually not confused with Services, the relationships
  between different types of Resources and a Service are confusing to many people.

  Business entities in the Product domain represent what is offered to the market. This domain deals with such things as the development,
  promotion, pricing, and retirement of product offerings, as well as instances of offerings procured by customers and others. Business entities
  in the Service and Resource domain represent (among other concepts) how products offered to the market are implemented.

  This Addendum is built with the express purpose of serving as a foundation for other Service (sub-) models to fit into. Conceptually, this
  Addendum is a framework, with other Service models (e.g., an MPLS VPN model) “plugging into” it.

  4.1     Service Domain Overviews
  The Service domain represents roles, information and activities carried out by parties (e.g. individuals / organizations) playing roles that are
  involved in the strategic planning, definition, development and operational aspects of Services that are used to realize Product offerings to
  the market. Activities include management of: strategies, capabilities, lifecycles, catalogs, inventories, installations, activations, problems,
  performance, guiding, mediation, usage statistics and support of customer-facing services that are offered to customers and resource-facing
  services that are presented to resources by an enterprise.




© TM Forum 2025. All Rights Reserved                                                           13                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure [SeD-01] Service ABEs Level 1

  The diagram below lists the Service Domain's ABEs.

  Service Party Roles ABE

          •        The Service Party Roles ABE contains all PartyRoles related to the Service Domain such as ServiceManager.

  Service Specification ABE

          •       The Service Specification ABE contains entities that define the shared characteristics of both types of Service entities. This enables multiple
          instances to be derived from a single specification entity. In this derivation, each instance will use the characteristics defined in its associated specification.

  Service Order ABE

          •       The Service Order ABE contains all entities that represent a type of Request of one or several services for any type of Service Specification. A
          Service Order decomposes a Product Order's products into the services associated with a ServiceOrder through which the products are realized.

  Service ABE

          •       A Service represents an instance of ServiceSpecification. The Service ABE contains entities that are used to represent both types of Services: CSP
          Know-Hows instances (a.k.a. Customer Facing Services or CFS) and Technical solution (a.k.a. Resource Facing Services or RFS).
          •       The Service carries the place where the Service is in use if relevant, as well as configuration characteristics, such as assigned telephone numbers
          and internet addresses. The Service also tracks the links to Product realized and/or Resources used.




© TM Forum 2025. All Rights Reserved                                                                            14                     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Service Configuration ABE

          •       The Service Configuration ABE represents the specification of the different possible Service configurations as well as the Service Configurations
          instantiated for a Service.




© TM Forum 2025. All Rights Reserved                                                                        15                     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Service Test ABE

          •       The Service Test ABE defines measurement including units and values and how the values are determined. It also includes thresholds used to
          evaluate the measure and the consequences of violating the thresholds as well as the Service Test measures that reflect the functioning of the Service
          under test.

  Service Usage ABE

          •     The Service Usage ABE represents the specification of Service Usage types and collects Service Usage records with their characteristics (a.k.a.
          consumption data).

  Service Performance ABE

          •       The Service Performance ABE collects information used to correlate, consolidate, and validate various performance statistics and other
          operational characteristics of Know-Hows (a.k.a. CFS) and Technical Solutions (a.k.a. RFS).

  Service Problem ABE

          •     The Service Problem ABE manages faults, alarms, and outages from a Service point-of-view. This is then correlated to trouble tickets, regardless of
          whether the cause is physical or logical.

  Service Capacity ABE

          •      The Service Capacity ABE specifies ability of Service to provide capability measured in quantity and units of quantity over an extended period. It
          also manages the Service Capacity Demands.

  Service Strategy and Plan ABE (not fully developed)

          •        The Service Strategy and Plan ABE contains entities that are used to address the need for enhanced or new Services, as well as the retirement of
          existing Services, by the enterprise. These entities have a strong dependency to both entities in the Resource and Product domains.



© TM Forum 2025. All Rights Reserved                                                                        16                    of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Note: TIP Service Management ABE is likely to be deprecated.

                                                          Service Domain


               Service ABE                Service Capacity ABE     Service Configuration ABE         Service Order ABE




         Service Party Roles ABE         Service Performance ABE      Service Problem ABE        Service Specification ABE




       Service Strategy & Plan ABE          Service Test ABE           Service Usage ABE         TIP Service Management ABE




                                                                   Figure [SeD-01] Service ABEs Level 1




© TM Forum 2025. All Rights Reserved                                                                           17             of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure [SeD-02] Service ABEs Level 1 & 2

  The diagram below lists the Customer Domain's ABEs Level 1 and Level 2.

  Customer Facing Service Spec ABE

          •     The Customer Facing Service Spec ABE defines the common characteristics for a set of CustomerFacingServices. This scales by enabling multiple
          CustomerFacingServiceSpecs to be defined to model the common characteristics of different groups of CustomerFacingServices.

  Resource Facing Service Spec ABE

          •      The Resource Facing Service Spec ABE defines the common characteristics for a set of ResourceFacingServices. This scales by enabling multiple
          ResourceFacingServiceSpecs to be defined to model the common characteristics of different groups of ResourceFacingServices.

  Service Catalog ABE

          •        A collection of entities that represent the specification of ServiceCatalogs and catalogs described by them that contain ServiceSpecifications.

  Customer Facing Service ABE

          •      The Customer Facing Service ABE defines the characteristics of a particular CustomerFacingService that represents a realization of a Product within
          an organization's infrastructure.

  Resource Facing Service ABE

          •        ResourceFacingService is an abstraction that defines the characteristics of a particular Service which support the network/infrastructure facing
          part of the service. For example, a VPN is an example of a CustomerFacingService, while the sub-services that perform different types of routing between
          network devices making up the VPN are examples of ResourceFacingServices. ResourceFacingServices are "internal" Services that are required to support
          a CustomerFacingService.




© TM Forum 2025. All Rights Reserved                                                                         18                     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Service Level Spec ABE

          •      This ABE includes a third type of Service Specification entity: that of a ServiceLevelSpecification. This type of specification templatizes Services that
          are bound to a Service Level Agreement.

  Service Performance Specification ABE

          •        The Service Performance Specification ABE defines measure of the manner in which a Service is functioning.

  Service Usage Specification ABE

          •        The Service Usage Specification ABE specifies types and characteristics of usage of ServiceSpecifications.

  Service Usage Entity ABE

          •       The Service Usage Entity ABE collects service usage information, and generates ServiceUsage according to ServiceUsageSpecification for use by
          other business entities.




© TM Forum 2025. All Rights Reserved                                                                          19                     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                       Service Domain
                                                Service Specification ABE                                Service ABE
         Service Party Roles ABE

                                            Customer Facing Service Spec ABE                     Customer Facing Service ABE

           Service Order ABE
                                            Resource Facing Service Spec ABE
                                                                                                 Resource Facing Service ABE

        Service Configuration ABE
                                                  Service Catalog ABE
                                                                                                   Service Performance ABE
          Service Problem ABE
                                                                                                    Service Level Spec ABE
                                                   Service Usage ABE


          Service Capacity ABE                   Service Usage Entity ABE
                                                                                             Service Performance Specification ABE


       Service Strategy & Plan ABE
                                             Service Usage Specification ABE
                                                                                                       Service Test ABE




                                                                            Figure [SeD-02] Service ABEs Level 1 & 2




© TM Forum 2025. All Rights Reserved                                                                                           20    of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.2     Service Party Roles ABE
  The Service Party Roles ABE contains all PartyRoles related to the Service Domain such as ServiceManager.

  Figure SO.00 - Service Party Roles

  The Service Domain party roles presently identified are:

          •      ServiceDesigner: A ServiceDesigner is a party role which is responsible for the design of the Service Provider’ know-how
          (CustomerFacingServiceSpecs). To be valid a know-how needs to align with one or more technical solutions (ResourceFacingServiceSpec or
          Supplier’s ProductSpec).
          •      TechnicalSolutionDesigner: A TechnicalSolutionDesigner is a party role which is responsible for the design of technical solutions
          (ResourceFacingServiceSpec). To be valid a technical solution needs to align with one or more Resources (ResourceSpec or Supplier’s
          ProductSpec).

                                PartyRole

                          +   status: String
                          +   validFor: TimePeriod




        ServiceDesigner                 TechnicalSolutionDesigner




                                                                    Figure SO.00 - Service Party Roles



© TM Forum 2025. All Rights Reserved                                                                     21            of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3     Service Specification ABE
  The Service Specification ABE contains entities that define the shared characteristics of both types of Service entities. This enables multiple
  instances to be derived from a single specification entity. In this derivation, each instance will use the characteristics defined in its
  associated specification.

  The Service Specification ABE is composed of two main concepts:

          1.      The CSP Know-Hows specification a.k.a. Customer Facing Services Specification or CFSSpec that describe only functional characteristics and
          capabilities that the CSP can provide to a customer however the CSP builds on its own all or part of the technical solution. Note that it corresponds only to
          non-tangible goods.
          2.      The Technical solution specification a.k.a. Resource Facing Services Specification or RFSpec that describes only technical characteristics and
          capabilities.

  Entities in this ABE focus on adherence to standards, distinguishing features of a Service, dependencies (both physical and logical, as well as
  on other services), quality, and cost. In general, entities in this ABE enable Services to be bound to Products and run using Resources.

  Figure SO.03 - Subclassing ServiceSpecification (OLD SO.10)

  ServiceSpecification is the base entity for defining the ServiceSpecification hierarchy.

  Each instance of a ServiceSpecification is made up of changeable as well as invariant attributes, relationships, and constraints. A
  ServiceSpecification defines the shared characteristics of a Service. It can be conceptually thought of as a template that different Service
  instances can be instantiated from. Each of these Service instances will have the same shared characteristics. However, the characteristics'
  values of the instantiated Service will be specific to each instance.




© TM Forum 2025. All Rights Reserved                                                                        22                     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  This class can be thought of as a template, which represents a generic specification for implementing a particular type of Service. A
  ServiceSpecification may consist of other ServiceSpecifications supplied together as a collection.

  ServiceSpecification inherits from EntitySpecification, which inherits from RootEntity.



  ServiceSpecification is sub-classed as CustomerFacing and ResourceFacing ServiceSpecifications, types of ServiceSpecifications.

  CustomerFacingServiceSpec

  A CustomerFacingServiceSpec defines the properties (characteristics) common to a particular CustomerFacingService used to realize the
  associated Product(s). This entity serves as a common basis to build any set of CustomerFacingServices that the service provider needs.

  The CustomerFacingServiceSpec represents all the Service Provider’s know-how of intangible goods at a functional level. It would be more
  appropriate to name it KonwHowSpec or ProductFacingServiceSpec, but the name is not changed as it is well known.

  The ProductSpecification corresponds to a sub-set of the Service Provider’s know-how according to what marketing people want to sell.
  Therefore, a ProductSpecification is a restriction of CustomerFacingServiceSpecs.



  ResourceFacingServiceSpec

  The ResourceFacingServiceSpec represents the technical solutions that the Service Provider can implement for
  CustomerFacingServiceSpec.

  Each technical solution (ResourceFacingServiceSpec) requires ResourceSpecifications to be realized and might require buying part of the
  solution to a supplier (for example the Service Provider might have to buy the Local Loop to provide a broadband access).



© TM Forum 2025. All Rights Reserved                                                          23                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  This is the base entity for defining different types of ResourceFacingServiceSpecs. A ResourceFacingServiceSpec is an abstraction that
  defines the shared characteristics of a particular ResourceFacingService. The shared portion serves as a single common basis to build a set
  of variable ResourceFacingServices that all use this common ResourceFacingServiceSpec.

  ServiceSpecification represents a generic means for implementing a particular type of Service. In essence, a ServiceSpecification defines the
  common portions of a set of Services, while Service defines a specific instance that is based on a particular ServiceSpecification. This
  relationship is represented by the SpecifiesService dependency.

  It is important to remember that the Specification classes are used to define attributes shared by each associated Entity, whether it is a
  Service, a Resource, a Product, or something else. This is a generic pattern that is used throughout the SID. Similarly, the Entities themselves,
  whether they are Services, Resources, Products, or something else, represent the instances that are derived from their associated
  Specification classes. This is why the cardinality on the “specification” side (e.g., CustomerFacingServiceSpec) of each association (e.g.,
  SpecifiesCustomerFacingService) is defined to be “1” – the SID spec mandate the use of Specifications.

  A ServiceSpecification can classify a set of Services using the SpecifiesService association. More specifically, a CustomerFacingServiceSpec
  classifies a set of CustomerFacingServices created from it and a ResourceFacingServiceSpec classifies a set of ResourceFacingServices
  created from it.

  SpecifiesCustomerFacingService and SpecifiesResourceFacingService are derived relationships coming from SpecifiesService relationship.




© TM Forum 2025. All Rights Reserved                                                           24                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                  /SpecifiesService
                              ServiceSpecification                                                                                         Service
                                                           1                                                               0..*




                                                                         /SpecifiesResourceFacingService

                                                                          1                                     0..*

       CustomerFacingServiceSpec                  ResourceFacingServiceSpec                                ResourceFacingService                     CustomerFacingService

                    1..1   0..*                                          1..*                            0..*                                             0..*    0..*

                                  RequiresResourceFacingServiceSpec                                                    CFServiceRequiresRFServices

                                                                        SpecifiesCustomerFacingService



                                                                      Figure SO.03 - Subclassing ServiceSpecification (OLD SO.10)




© TM Forum 2025. All Rights Reserved                                                                                                                 25                      of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.04 - Simplified SID Product Model

  The following Figure is a simple model of how a Product is modeled.

  A ProductOffering represents what is externally presented to the market for the market’s use and can be simple or bundled (atomic /
  composite pattern).

  A ProductOffering represents how the ProductSpecification is sold (i.e. packaging rules, prices, alterations, commitments…).

  The ProductSpecification represents a product specification as perceived by the business user and specifies what the marketing operator
  wants to sell at a functional level (i.e. what are the capacities, which usages are available…).

  It can represent:

          •        material goods (Terminal, phone, mobile, fax, modem)
          •        or intangible goods (like an Anti-Spam service for email).

  A ProductOffering makes available at least one ProductSpecition directly or indirectly (through contained ProductOfferings).

  Vice versa, a ProductSpecification may be made available as one or more simple ProductOfferings.

  A Product represents exclusively the instantiation of a ProductOffering or ProductSpecification by a Party playing a PartyRole, such as a
  Customer.




© TM Forum 2025. All Rights Reserved                                                          26                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                               /ProductOfferingReferencesOrReferencedB
              /ProductSpecificationReferencesOrReferencedBy
                                                                                                                     0..*             0..*
               0..*                0..*

                                                              /ProdSpecMadeAvailableAs                        ProductOfferingSpecification
             ProductSpecification
                                                                                                       * +   isPromotion: Boolean
         +   brand: String                      1..*                                                     +   isSellableStandAlone: Boolean
                                                                            {XOR}
                             1




                                                                             Product
                             /ProductSpecificationDescribes
                                                                     +   status: String
                                                                     +   validFor: TimePeriod
                                                              0..*


                                                                     0..*      0..*


                                                              /ProductReferencesOrReferencedBy



                                                                                    Figure SO.04 - Simplified SID Product Model




© TM Forum 2025. All Rights Reserved                                                                                                    27               of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.08 - Service Specifications and other Domains

  The Product guidebook refers to the concept of a ProductSpecification.

  As a reminder, ProductOfferings provide tangible or intangible Products that organizations, such as Service Providers and Enterprises,
  market, sell or lease to Customers.

  A ProductSpecification is a detailed description of a tangible or intangible object made available externally in the form of a ProductOffering to
  Customers or other Parties playing a particular PartyRole. The information described by a ProductSpecification is a set of invariant data that is
  common to all realizations of that ProductSpecification. A ProductSpecification may exist as a single ProductSpecification, or consist of a set
  of ProductSpecifications supplied together as a collection.



  Note that a direct association between Product and Service does not exist. Instead, the ProductSpecRealizedAsCFSSpec association is
  defined between ProductSpecification and CustomerFacingServiceSpec.

  Remember that the purpose of a Specification is to serve as a template. This enables specific instances of a desired entity to be more easily
  and consistently created.

  The ProductSpecRealizedAsCFSSpec association enables a given ProductSpecification to specify CustomerFacingServiceSpecs restricted by
  the ProductSpecification. This relationship is only used when the ProductSpecification corresponds to intangible goods.

  Note in particular that there is no association defined between a ProductSpecification and a ServiceSpecification. This is because such an
  association would include ResourceFacingServiceSpecs, and that violates the effort to separate CustomerFacingServices from
  ResourceFacingServices. Thus, the ProductSpecRealizedAsCFSSpec is defined to enforce this separation.

  The ProductSpecRealizedAs association enables a ProductSpecification to define zero or more ResourceSpecifications. This is analogous to
  the ProductSpecRealizedAsCFSSpec association for ProductSpecification corresponding to tangible goods.


© TM Forum 2025. All Rights Reserved                                                           28                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  The ProductSpecRealizedAsCFSSpec and ProductSpecRealizedAs relationships are mutualy exclusives.

  A Service may depend on one or more specific PhysicalResources. For example, the Customer connects to the VPN through a PhysicalPort on
  a Card of a PhysicalDevice. This is represented using the RFServiceConfiguredUsing association, whose purpose is to bind Resources to
  Services without identifying what type of Service or Resource is being bound.

  For example, this enables services to be “reserved” on a PhysicalResource for resource planning and consumption purposes, without
  specifically identifying the low-level system resources required.

  The above discussion has been conducted in terms of “instances” of these objects. For the most part we will talk about these concepts more
  generically using the concept of a “specification”.

  A ResourceSpecification can classify a set of Resources using the SpecifiesResource association, so its subclasses, PhysicalResourceSpec,
  LogicalResourceSpec and CompoundResourceSpec, inherit this association.

  A Product is realized by zero or more CustomerFacingServices through the ProductRealizedAsCFService association. This enables a Product
  to in effect customize a CustomerFacingService already defined by a CustomerFacingServiceSpec. In other words, the
  ProductSpecRealizedAsCFSSpec association is used to define the set of CustomerFacingServiceSpecs for a given ProductSpecification,
  which means that all Products based off of that ProductSpecification will use that set of CustomerFacingServiceSpecs. Different Products
  have the ability to add their own features to these CustomerFacingServices, and do so through the ProductRealizedAsCFService association.

  Similarly, a Product realizes zero or more Resources through the ProductRealizedAsResource association. Note that the cardinality on the
  Product side of both of these associations is optional, which means that a Product doesn’t have to implement these two associations. This is
  because not all Products are realized through CustomerFacingServices and Resources.

  CustomerFacingServices cannot be implemented without ResourceFacingServices to support them. This is reflected by the
  CFServiceRequiresRFServices association. This relationship is templatized by the RequiresResourceFacingServiceSpec association, which
  defines the set of ResourceFacingServiceSpecifications that are required by a particular CustomerFacingServiceSpecification. Again, note


© TM Forum 2025. All Rights Reserved                                                        29                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  that the cardinality on the ResourceFacingServiceSpec side is 1,*, meaning that a CustomerFacingServiceSpec cannot be instantiated unless
  it is bound to at least one ResourceFacingServiceSpec.




© TM Forum 2025. All Rights Reserved                                                      30                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                ServiceSpecRelationship

                                                 0..*                             0..*

                       ServiceSpecificationReferencedBy
                                                                ServiceSpecificationReferences

                                                  1..1                            1..1
                                                                                                           /SpecifiesService
                                                 ServiceSpecification                                                                                                 Service
                                                                                   1                                                                0..*




            CustomerFacingServiceSpec                                          ResourceFacingServiceSpec                                   ResourceFacingService                                        CustomerFacingService

                           0..*                  0..*                           1..*                                     0..*                                 0..*          0..*            0..*                       0..*

                                                                                                                                                                     CFServiceRequiresRFServices                      ProductRealizedAsCFService
                                          RequiresResourceFacingServiceSpec

                                                                                                                                                                                                                            RFServiceConfiguredUsing

                   ProdSpecRealizedAsCFServiceSpec
                                                                                                                                                                         /ProductReferencesOrReferencedBy


                                                                                                                                                                                                                     0..*
                                         /ProdSpecMadeAvailableAs
                                                                                 ProductOfferingSpecification                                                                                        Product
                                                                          *
                                                                                                                                                                                                                        0..*
                                                                                                                                                                                                            0..*



                                                                                                                               /ProductSpecificationDescribes                                                               ProductRealizedAsResource


                                                                                                                                                           /InvolvedResourceSpecs

                      0..*        1..*      1                                                                                                         0..*                 0..*                                                                         0..*    0..*
                                                                                         /ProductSpecRealizedAs                                                                                             /SpecifiesResource
                   ProductSpecification                                                                                                                      ResourceSpecification                                                                        Resource
                                                         0..*                                                                                0..*                                             0..1                                    0..*
                    0..*                 0..*                                                                                                                                      1..*
                                                                                                                                                                                                             RFServiceSpecHasResourceSpecs

           /ProductSpecificationReferencesOrReferencedBy



                                                                                                  Figure SO.08 - Service Specifications and other Domains


© TM Forum 2025. All Rights Reserved                                                                                                                                                               31                                        of    177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.09 - VPNService – VPNServiceSpecification Example

  Let’s now examine a practical example. A ProductSpecification will be used to definea ProductOffering. A ServiceSpecification will define
  how to build a VPN to implement the defined in the ProductSpecification. Now, there are many different types of VPNs. For example, there are
  network-based VPNs, VPNs based on tunneling, VPNs based on encryption, hybrid VPNs such as MPLS VPNs, and others. All of these VPNs
  have certain things in common, which can be represented by a VPNServiceSpecification.

  Consider an MPLS VPN built to the RFC2547bis specification. The MPLS VPN is an example of a CustomerFacingService. This particular type
  of MPLS VPN is characterized by having three different types of routers. Each of these – the CustomerPremise, ProviderEdge, and Provider
  routers – can run a different set of protocols, perform a different function, and be managed in a different way.

  An MPLS VPN is implemented in a significantly different manner than other types of VPNs. Thus, an MPLSVPNService is a different type of
  object than (for example) an IPsecVPNService. However, they have three important things in common. First, they are both defined through a
  ProductSpecification and realized as a Product. Second, they can both be related to the same CustomerFacingServiceSpec. This is useful if,
  for example, the Service Provider is defining multiple types of VPNs that the Customer could use. Third, it is possible that they could both use
  the same CustomerFacingServices and/or ResourceFacingServices.

  Note that a more complete picture would also show that the two VPNs could use the same PhysicalResources and/or LogicalResources as
  well. However, this complicates the above figure and is out of scope for this Addendum.

  The difference between the MPLSVPNService and the IPsecVPNService is in the protocols and architecture used, which in turn cause
  additional system-specific differences that don’t show up in a business model. Rather, the SID identifies these two CustomerFacingServices
  and relates them to zero or more ResourceFacingServices through the CFServiceRequiresRFServices association (as well as the
  RequiresResourceFacingServiceSpec association from the template point-of-view).

  A ResourceFacingServiceSpec is related to a ResourceSpecification by the RFServiceSpecHasResourceSpecs association. Furthermore, a
  ResourceSpecification can be used to define the set of Resources that it requires using the SpecifiesResource association. This combination



© TM Forum 2025. All Rights Reserved                                                           32                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  of associations means that conceivably, the same Resource could be used to support both types of VPNServices, assuming that it has the
  software and/or hardware to do so.

  Note that in the following Figure, the VPNServiceSpecification is an abstract class that contains the basic attributes and relationships and
  constraints for defining a VPNService without specifying the specific type and technology used (e.g., Ipsec vs. MPLS) to implement the
  VPNService. For example, the VPNServiceSpecification can be used to define the set of SLSs that will be used to measure performance of the
  VPN. Both an MPLS VPN as well as an Ipsec VPN specification are derived from the VPNServiceSpecification class.

  The MPLSVPNServiceSpecification and IPsecVPNServiceSpecification are related to the MPLSVPNService and the IPsecVPNService through
  the SpecifiesMPLSVPNServices and the SpecifiesIPsecVPNServices associations, respectively. This enables different MPLSVPNServices (as
  well as IPsecVPNServices) to be specified by the same MPLSVPNServiceSpecification (or IPsecVPNServiceSpecification, respectively). This
  enables the Service Provider to define a number of characteristics for each of the CustomerFacingServices and thereby templatize the
  definition of each. Combined with the LogicalResource and QoS Addenda, a complete roadmap will be developed for configuring this
  templatized definition.




© TM Forum 2025. All Rights Reserved                                                        33                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                  /SpecifiesService
                                 ServiceSpecification                                                                                   Service
                                                               1                                                        0..*




         CustomerFacingServiceSpec                    ResourceFacingServiceSpec                       ResourceFacingService                           CustomerFacingService

                               0..*                                       1..*                              0..*                                           0..*
                                    RequiresResourceFacingServiceSpec                                              CFServiceRequiresRFServices




          VPNServiceSpecification




                                                                                  SpecifiesIPsecVPNServices
        IPsecVPNServiceSpecification                                                                                                                     IPsecVPNService
                                              0..1                                                                                        0..*



                                                                    Figure SO.09 - VPNService – VPNServiceSpecification Example




© TM Forum 2025. All Rights Reserved                                                                                                             34                           of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.11 - Modeling Stand-Alone and Aggregate ServiceSpecifications

  There are two basic ways to define and use a ServiceSpecification. One is to define a stand-alone ServiceSpecification, while the other is to
  define an aggregate ServiceSpecification. The difference is straightforward – aggregate ServiceSpecifications are used to define collections of
  ServiceSpecifications, whereas stand-alone ServiceSpecifications define all the functionality that is needed by themselves.

  If we did this, then the ServiceSpecAtomic would be defined as an abstract base class for defining ServiceSpecifications that do not have any
  subordinate ServiceSpecifications. These ServiceSpecifications are stand-alone in definition and use, and don’t require any supporting
  ServiceSpecifications to define the common characteristics of Services that it serves as a template for.

  Similarly, a ServiceSpecComposite class would be defined as an abstract base class for defining ServiceSpecifications that are formed by
  aggregating other ServiceSpecifications. The types of ServiceSpecifications that are aggregated may be ServiceSpecAtomic and/or
  ServiceSpecComposite instances. A ServiceSpecComposite collectively defines all of the common characteristics of Services that it serves
  as a template for.

  However, we already have defined two subclasses of ServiceSpecification, called CustomerFacingService and ResourceFacingService. We
  can just as easily apply the composite pattern to these classes instead of defining a ServiceSpecAtomic and a ServiceSpecComposite class.
  This is exactly what is done in the model shown in the following Figure. We can reserve the right to define generic ServiceSpecAtomic and
  ServiceSpecComposite classes that are not CustomerFacingServices or ResourceFacingServices in the future. Note that at this time, no
  examples of such ServiceSpecifications exist.

  Therefore, we will proceed with the definition of CustomerFacingServiceSpecs and ResourceFacingServiceSpecs using the composite
  pattern to model this.




© TM Forum 2025. All Rights Reserved                                                          35                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                        ServiceSpecification




                                                                                                                                                                                    HasResourceFacingServiceSpecs
       HasCustomerFacingServiceSpecs                                                          RequiresResourceFacingServiceSpec
                                              CustomerFacingServiceSpec                                                                             ResourceFacingServiceSpec
                                       0..*                                  0..*                                                        1..*                                        0..*




                         0..1                                                                                                                                                                             0..1

                 CustomerFacingServiceSpecComposite               CustomerFacingServiceSpecAtomic                 ResourceFacingServiceSpecAtomic                    ResourceFacingServiceSpecComposite




                                                          Figure SO.11 - Modeling Stand-Alone and Aggregate ServiceSpecifications




© TM Forum 2025. All Rights Reserved                                                                                                36                          of      177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.13 - Modeling the Versioning of a ServiceSpecification

  Applications often require the ability to distinguish between different versions of objects in general. This Addendum applies this principal to
  ServiceSpecifications. The ServiceSpecVersion class represents a particular form or variety of a ServiceSpecification that is different from
  others or from the original. The form represents differences in attributes, relationships, and/or constraints that characterize this particular
  ServiceSpecification, but which are not enough to warrant creating a new ServiceSpecification.

  The CustomerFacingServiceSpecVersion and ResourceFacingServiceSpecVersion subclasses are defined to enable an application to track
  different versions of CustomerFacingServiceSpecs and ResourceFacingServiceSpecs independently.

  The ServSpecModifications aggregation represents the set of versions of this ServiceSpecification. The semantics of this aggregation are
  implemented with the ServiceSpecVersionDetails class.

  The two version details association classes are both derived from the ServSpecModifications aggregation. They add additional detail to the
  generic concept of defining a version of a ServiceSpecification.

  The same exact principle applies to tracking different versions of the more generic ServiceSpecAtomic and ServiceSpecComposite objects.
  This is not shown because the focus of this Addendum is on the definition of CustomerFacingServices and ResourceFacingServices.




© TM Forum 2025. All Rights Reserved                                                           37                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                              ServiceSpecVersion                 ServSpecModifications
               +   format: String                                                                      ServiceSpecification
               +   number: String
                                                               0..*                            1
               +   reason: String
               +   semantics: String
               +   timestamp: DateTime
               +   validFor: TimePeriod



                                                                                                                RequiresResourceFacingServiceSpec


                                                                                  CustomerFacingServiceSpec              0..*        1..*           ResourceFacingServiceSpec

                                                                                                   1                                                          1


       ResourceFacingServiceSpecVersion

                       0..*


                                      CustomerFacingServiceSpecVersion
                                                                                                                CFSSpecVersionDetails
                                                                              0..*
                                                                                                          +   minVersionForUse: String
                                                                                                          +   preferredVersionToUse: String
                                                                                                          +   validFor: TimePeriod




                                                                       RFSSpecVersionDetails

                                                           +   minVersionForUse: String
                                                           +   preferredVersionToUse: String
                                                           +   validFor: TimePeriod




                                                               Figure SO.13 - Modeling the Versioning of a ServiceSpecification




© TM Forum 2025. All Rights Reserved                                                                                                        38                         of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.14 - The Concept of a ServiceSpecificationType

  The preceding discussion has shown that multiple ServiceSpecifications can share common characteristics. This can be more efficiently
  represented using the concept of a ServiceSpecificationType.

  The ServiceSpecificationType defines a generic category of ServiceSpecifications. Each ServiceSpecificationType serves to group a set of
  particular ServiceSpecifications that can be used together. The result of this is a more efficient ability to define a set of related Services that
  can be grouped together to form a higher-level Service. For example, a given higher-level Service might include VPN and QoS Services. If these
  Services are always used together, then they can be categorized using a common type.

  The ServiceSpecificationTypeCategorizes association defines how ServiceSpecificationTypes categorize different ServiceSpecifications. The
  InvolvedServiceSpecTypes is a derived association as indicated by the “/” prefix. It is derived from an association between
  EntitySpecificationTypes which enables hierarchies of specification type entities to be defined.

  Note that in principle, ServiceSpecificationType could be subclassed, so that the subclasses of ServiceSpecificationType could be used to
  categorize different subclasses of ServiceSpecification. This is not recommended for the purposes of this document, as the
  ServiceSpecificationType object is used solely to help categorize objects. The only reason a ServiceSpecificationType object should be
  subclassed is if that subclass adds additional semantics (in the form of attributes, relationships, and/or constraints). Thus, it makes perfect
  sense for applications that are based on the SID to subclass ServiceSpecificationType.




© TM Forum 2025. All Rights Reserved                                                            39                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                  /InvolvedServiceSpec


                                  0..*

       ServiceSpecificationType
                                              0..*
                        0..*

                            ServiceSpecificationTypeCat


                        0..*

           ServiceSpecification

                       1


                       /SpecifiesService


                       0..*

                  Service

       +   hasStarted: Boolean
       +   isMandatory: Boolean
       +   isServiceEnabled: Boolean
       +   isStateful: Boolean
       +   startMode: Integer




                                                               Figure SO.14 - The Concept of a ServiceSpecificationType




© TM Forum 2025. All Rights Reserved                                                                              40      of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.17 - The Concept of ServiceSpecificationRoles (OLD SO.21)

  ServiceSpecificationRole is an abstract base class that defines a ServiceSpecification in terms of a set of roles. The roles are then used to
  characterize the shared functionality of the ServiceSpecification, regardless of whether it is a resource or a customer facing service
  specification.

  ServiceSpecificationRoles represent the shared functionality of a ServiceRole. Representing a Service in terms of ServiceSpecificationRoles
  enables the functionality of the Service to be defined independently of BusinessActor, PhysicalResource, LogicalResource, or ot her Services.

  The ServiceSpecificationRole defines a ServiceSpecification in terms of possible roles.

  The roles are then associated for both CustomerFacing and ResourceFacing services through the CustomerFacingServiceSpecificationRole
  and ResourceFacingServiceSpecificationRole subclasses. The utility of the ServiceSpecificationRole class is to present a single point for
  accumulating common relationships that its subclasses can inherit.

  The RequiresResourceFacingServiceSpecRoles relationship is used to define the set of ResourceFacingServiceSpecRoles that are required
  by a particular CustomerFacingServiceSpecRole. Conceptually, this enables roles to be used to define the common characteristics of a set of
  ResourceFacingServiceSpecs that are required by a particular CustomerFacingServiceSpec.

  Note that the cardinality of the RequiresResourceFacingServiceSpecRoles is * on the CustomerFacingServiceSpecificationRole side and 1..*
  on the ResourceFacingServiceSpecRole (component) side. This is because a ResourceFacingServiceSpecRole can exist without being bound
  into a CustomerFacingServiceSpecRole (e.g., in testing the network), but a CustomerFacingServiceSpecRole requires at least one
  ResourceFacingServiceSpecRole to function. Note also that this cardinality is symmetric with the cardinality defined in the
  RequiresResourceFacingServiceSpec association.

  The InvolvedServiceSpecRoles association is used to define a set of ServiceSpecificationRoles that are involved with, or related to, each other
  in order to build a particular type of ServiceSpecification.



© TM Forum 2025. All Rights Reserved                                                           41                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  This association applies equally to CustomerFacingServicesSpec and ResourceFacingServiceSpec.

                                                                                                                                    InvolvedServiceSpecRoles


                                                                                                                                    0..*                       0..*

                                                ServiceSpecification                                                                       ServiceSpecificationRole
                                                                                          SpecifiesServiceSpecRoles
                                                                                                                             0..*
                                                                              1




                                                 ResourceFacingServiceSpec
       CustomerFacingServiceSpec                                                                       ResourceFacingServiceSpecRole                           CustomerFacingServiceSpecRole
                                               1..*                    0..*
       0..*         0..*                                                                                     0..*     1..*                                               0..*              0..*
                                                                                                                        RequiresResourceFacingServiceSpecRoles
                  RequiresResourceFacingServiceSpec                               RFSSpecHasRFSRoles


                                                                                                   CFSSpecHasCFSRoles




                                                              Figure SO.17 - The Concept of ServiceSpecificationRoles (OLD SO.21)




© TM Forum 2025. All Rights Reserved                                                                                                                42                          of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.18 - Interaction Between ServiceSpecRoles and ResourceSpecRoles

  ServiceSpecificationRole is an abstract base class that defines a ServiceSpecification in terms of a set of roles. The roles are then used to
  characterize the shared functionality of the Service, regardless of whether it is a resource or a customer facing service.

  ServiceSpecificationRoles represent the shared functionality of a ServiceRole. Representing a Service in terms of ServiceSpecificationRoles
  enables the functionality of the Service to be defined independently of BusinessActor, PhysicalResource, LogicalResource, or other Services.

                  InvolvedServiceSpecRoles

                                                 0..*
                                                                                     SpecifiesServiceSpecRoles
                                             ServiceSpecificationRole                                                      ServiceSpecification
                                0..*                                       0..*                                   1


                                                                                                                                                             ResourceRoleSpecification


                                       RequiresResourceFacingServiceSpecRoles
                                                                                                                      RequiresPhysicalResourceRoleSpecs

       CustomerFacingServiceSpecRole                                              ResourceFacingServiceSpecRole                                              PhysicalResourceRoleSpec
                                                0..*               1..*
                                                                                                                         0..1                         0..*
                        0..*                                                                        0..*

                         CFSSpecHasCFSRoles
                                                                          RFSSpecHasRFSRoles


                         0..*
                                                                                                     0..*

       CustomerFacingServiceSpec
                                                                                   ResourceFacingServiceSpec




                                                            Figure SO.18 - Interaction Between ServiceSpecRoles and ResourceSpecRoles




© TM Forum 2025. All Rights Reserved                                                                                                           43                     of    177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.22 -The Concept of ServiceSpecCharacteristic

  A major focus of marketing programs is to represent the key features of a Product. This was documented in the Product domain guide book as
  ProductSpecCharacteristics. Since a Service is the realization of a Product, it makes sense to reuse this concept and define the notion of a
  ServiceSpecCharacteristic.

  The concept behind a ServiceSpecCharacteristic and a ServiceSpecCharacteristic Value is similar in nature to those of a
  ProductSpecCharacteristic ProductCharacteristic Value, respectively. Services have a large variety of important properties (which we call
  characteristics), such as bandwidth, type of QoS, and so forth. Each of these characteristics is used at the business level to characterize a
  Service. This Addendum models these characteristics as a set of entities, attributes, and relationships that help characterize a
  ServiceSpecification and Service, respectively.

  Additional information about the CharacteristicSpecification/CharacteristicValue pattern can be found in the Common guide book
  subsection Root Business Entities ABE.




© TM Forum 2025. All Rights Reserved                                                           44                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                                                                                                                                             /ProdSpecCharacteristicEnumeratedBy
                                                                                                                                                                                   ProductSpecCharacteristic                                                                   ProductSpecCharacteristicValue
                EntitySpecification                           ServiceSpecification                                                                                                                                                                                                                              0..*
                                                                                                                                                                                                                             1
                                                                                                                                                                                                        0..*                                                           0..*
          +   status: String
          +   validFor: TimePeriod                                       1


                                      0..1
                                                                                                                                                                         ProdSpecCharacteristicTranslatesTo                                                            CharacteristicSpecification
       EntitySpecFurtherDefinedBy                    /ServiceSpecFurtherDefinedBy
                                                                                                                                                                                                                                                              +    derivationFormula: String
                                      0..*
                                                                                                                                                                                                                                                              +    description: String
                                                                         0..*                                                                                                                             0..*                                                +    extensible: Boolean
                EntitySpecCharUse                                                                           /ServiceSpecCharacteristicFurtherDefinedBy                                                                                                        +    ID: String
                                                                                                                                                                                       ServiceSpecCharacteristic                                              +    maxCardinality: Integer
         +    canBeOverridden: Boolean                       ServiceSpecCharUse
                                                                                              0..*                                                                                                                                                            +    minCardinality: Integer
         +    description: String                                                                                                                                        1
                                                                                                                                                                                                                                                              +    name: String
         +    extensible: Boolean                                                                                                                                                             0..1                       1
                                                                                0..1                                                                                                                                                                          +    unique: String
         +    isPackage: Boolean
                                                                1..1                                                                                                                                                                                          +    validFor: TimePeriod
         +    maxCardinality: Integer
                                                                                                                                                                                                                                                              +    valueType: String
         +    minCardinality: Integer
         +    name: String
         +    unique: String                                                                                                                                                                                                                                                            1
         +    validFor: TimePeriod                                                                                                         CharacteristicValue

                          1                                                                                                       +      validFor: TimePeriod
                                                                                                                                  +      value: String

                                      /ServiceSpecCharUseEnumeratedBy                                                                                                                                   /ServiceSpecCharEnumeratedBy
                                                                                                                                                           /ServiceSpecCharDescribes

                                                                             /ServiceSpecCharUseDescribesServiceCharacteristicValue                                                                                                                           CharacteristicSpecificationEnumeratedBy

         EntitySpecCharUseEnumeratedBy

                                                                                                                         0..*                              0..*

                                                                                                                                ServiceCharacteristicValue                                                                                                                               0..*

                                                                                                                                  1..1                          0..*
                                                                             /ServiceSpecCharValueUseInstanciatedAs
                                                                                                                                                                  /ServiceSpecCharValueInstantiatedAs                                                                     CharacteristicSpecValue
                              0..*
                                                                                                                                                                                                                                                                   +    isDefault: Boolean
                                                                                                                                                                                                                                                                   +    rangeInterval: String
                                                                0..*                   0..1                                                                                                                    0..1   0..*                                         +    rangeStep: Integer
              EntitySpecCharValueUse                                                                                                                                                                                                                               +    unitOfMeasure: String
                                                                                                                      /ServiceSpecCharValueUseDefinedBy
                                                                 ServiceSpecCharValueUse                                                                                                         ServiceSpecCharacteristicValue                                    +    validFor: TimePeriod
         +    isDefault: Boolean
                                                                                                                                                                                                                                                                   +    value: String
         +    validFor: TimePeriod                                                                   0..*                                                                              1..1
                                                                                                                                                                                                                                                                   +    valueFrom: String
                                                                                                                                                                                                                         0..*                                      +    valueTo: String
                                                                                                                                                                                                                                                                   +    valueType: String


                                                                                                                                                                                                                                              /ProdSpecCharacteristicValueTranslatesTo




                                                                                                     Figure SO.22 -The Concept of ServiceSpecCharacteristic




© TM Forum 2025. All Rights Reserved                                                                                                                                                                             45                                      of        177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.22a - Service and Resource Characteristic Associations

  Service Features and Service Parameters are two other synonyms for a ServiceSpecCharacteristic, and are used in models from other TM
  Forum member companies.

  ServiceSpecCharacteristics and ServiceSpecCharacteristicValues capture the differentiating features of a particular Service. However,
  ServiceSpecCharacteristics are not versionable objects. This is because ServiceSpecCharacteristics do not add any information in and of
  themselves – rather, they are used to emphasize key features of a ServiceSpecification.

  There are cases when an instance of a ServiceSpecCharacteristic and/or a ServiceSpecCharacteristicValue must be translated to a
  corresponding ResourceSpecCharacteristic and/or a ResourceSpecCharacteristicValue. For example, there may be a
  ServiceSpecCharactertistic that represents the size of an email box as defined by associated 10MB instance of
  SerivceSpecCharacteristicValue. This value may be translated into the actual size of 10.5MB as defined by the
  ResourceSpecCharacteristicValue associated to an email box size ResourceSpecCharacteristic.

  The following Figure shows the associations between characteristics in the Service and Resource domains that enable this translation.




© TM Forum 2025. All Rights Reserved                                                        46                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                    ServiceSpecCharacteristic                    /ServiceSpecCharEnumeratedBy               ServiceSpecCharacteristicValue

                                                        1                                        0..*
                                   0..*                                                                                       0..*
             ServSpecCharTranslatesToResourceSpecChar                                                   ServSpecCharValueTranslatesToResourceSpecChar
                                   0..*                                                                                       0..*
                                                            /ResourceSpecCharEnumeratedBy
                   ResourceSpecCharacteristic                                                              ResourceSpecCharacteristicValue
                                                        1                                       0..*

                                     1
             /ResourceSpecCharcateristicFurtherDefinedBy

                                     0..*

                      ResourceSpecCharUse


                                     0..*

              /ResourceSpecificationFurtherDefinedBy

                                     1

                      ResourceSpecification




                                                                    Figure SO.22a - Service and Resource Characteristic Associations




© TM Forum 2025. All Rights Reserved                                                                                                        47          of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.23 - ServiceCharacteristicValue and ServiceSpecCharacteristicValue

  The purpose of the ServiceCharacteristicValue and ServiceSpecCharacteristicValue objects is to define how instances of these objects can
  be populated. Again, it was influenced from the earlier work done on similar Product objects. The ServiceCharacteristicValue and the
  ServiceSpecCharacteristicValue classes, shown in the following Figure define this concept.

  A ServiceSpecCharacteristicValue object is used to define a set of attribute values, each of which can be assigned to a corresponding
  attribute in a ServiceSpecCharacteristic object. This is represented by the ServiceSpecCharEnumeratedBy association. The values of the
  attributes in the ServiceSpecCharacteristicValue object describe the values of the attributes that a corresponding
  ServiceCharacteristicValue object can take on.

  Note that we have elected to use classes instead of OCL to model these constraints. Therefore classes can be used to create reusable
  “constraints”, which are in effect what the ServiceSpecCharacteristicValue are.

  The following Figure also shows how a ProductCharacteristicValue has been translated to a ServiceCharacteristicValue.

  For example, consider the definition of a VPNService, as previously shown in Figure SO.09. A set of ServiceSpecCharacteristicValue could, for
  example, be used to define the types of VPN that are being offered. A corresponding ServiceCharacteristicValue would then represent the
  salient features of a particular instance of a Service VPN. For example, a Service Provider may be constrained to offer either an MPLS or an
  Ipsec VPN (as opposed to other types) of VPNs. These would be examples of ServiceSpecCharacteristicValues. Similarly, perhaps the MPLS
  VPN could only support a defined upper limit of CE devices. This upper limit would be an example of a ServiceCharacteristicValue.




© TM Forum 2025. All Rights Reserved                                                         48                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                   /ServiceSpecCharacteristicFurtherDefinedBy
                                    /ServiceSpecFurtherDefinedBy


           ServiceSpecification                                         ServiceSpecCharUse            0..*                             1            ServiceSpecCharacteristic
                                     1                        0..*

                         1                                           0..1                                                                       1                       0..1


               /SpecifiesService

                                          /ServiceSpecCharUseDescribesServiceCharacteristicValue
                                                                                                                               /ServiceSpecCharEnumeratedBy
                         0..*

              Service                                                                   ServiceSpecCharacteristicValue
    +   hasStarted: Boolean                                                                                                         0..*
    +   isMandatory: Boolean                                                                                  0..1
    +   isServiceEnabled: Boolean
    +   isStateful: Boolean
    +   startMode: Integer
                                                                                       /ServiceSpecCharValueInstantiatedAs
                     1..1
                                                                                                              0..*
                                                                                                                                      /ServiceSpecCharDescribes
                                                                             0..*           ServiceCharacteristicValue
                                         ServiceDescribedBy
                                                                                                              0..*                     0..*
                                                                              0..*

                                                                                           ServiceCharValueTranslatedFrom


                                                                                                              0..*

                                                                                            ProductCharacteristicValue




                                                         Figure SO.23 - ServiceCharacteristicValue and ServiceSpecCharacteristicValue




© TM Forum 2025. All Rights Reserved                                                                                                                     49                     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.24 - Multiple Command Syntaxes and Programming Models

  Linking to QoS – ServicePackage and ServiceBundle

  The Service QoS guidebook defines of the QoS model. The purpose of this model is to satisfy one of the use cases of the Service Domain in
  general, by describing how QoS mechanisms on a device are configured. Here, “mechanisms” refers to modeling the end-user features of the
  device.

  Conceptually, what makes this a daunting task is that Services involve multiple devices which can have heterogeneous commands and
  programming models, as is shown in Figure SO.24 below.

  Current network devices have different programming models using different commands. This makes it very difficult for common tasks to be
  performed, because in effect the network operator must know different languages. If we also take into account the fact that commands
  change per OS version, the analogy grows to a single person having to know multiple dialects of multiple languages. This cannot scale.

  The Figure above illustrates the use of different commands and programming models to perform the same high level task. The device on the
  left has configuration modes, each mode defining a set of appropriate commands. The device on the right has no such modes. Furthermore,
  the syntax used to perform the same task is drastically different.

  Note that each network device supports a Service through configuring a DeviceInterface and/or its LogicalDevice. This is worse for two
  reasons. First, the thought of doing this manually, for thousands of networks, is no longer viable, due to both the complexity of networks, the
  complexity of services that networks support, and the interaction between services supported on a network. Second, since each Device in
  general has a different programming model, there is no way to tell in advance which way (or ways) a Device can be programmed.

  Clearly, manually configuring each Service that can run on a given device is not a viable process. This Addendum introduces two innovative
  classes – ServicePackageSpec and ServiceBundleSpec – that serve to link the business requirements of QoS to its implementation. Note that
  this is done at the specification level, to enable this to be templatized. Of course, this is yet another instance of the Entity-EntitySpecification
  pattern, which is used throughout the SID. (This in and of itself is important, because it shows how the existing Service model can be easily
  extended to bridge new concepts using the same set of standardized mechanisms. This is an indicator of the robustness and inherent
  extensibility of the SID.)



© TM Forum 2025. All Rights Reserved                                                             50                   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                     Figure SO.24 - Multiple Command Syntaxes and Programming Models




© TM Forum 2025. All Rights Reserved                                                                     51            of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.25 - The Concept of a ServicePackage

  A ServicePackageSpec defines the concept of bundling a set of different CustomerFacingServiceSpecs to meet the functionality specified by
  one or more ProductSpecifications. This enables the common characteristics of these CustomerFacingServices to be specified, so that
  multiple Products can be built from their associated ProductSpecification.

  Treating this set of CustomerFacingServiceSpecs as a single object is very important for building complex Services, such as a VPN. This
  enables a single Product to be offered to the Customer (or another type of PartyRole), even though in reality the Product consists of a set of
  different CustomerFacingServices that must work together to provide the functionality that the Customer needs.

  The composite pattern is used to make the ServicePackageSpec object extensible. A ServicePackageSpecAtomic object models different
  ServicePackageSpecs as a set of different instances of individual, independent CustomerFacingServiceSpecs. This is fundamentally different
  than the ServicePackageSpecComposite object, which is used to model one ServicePackageSpec as the combination of other existing
  ServicePackageSpecs (as well as providing its own extensions).




© TM Forum 2025. All Rights Reserved                                                           52                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                   HasCustomerFacingServiceSpecs
                                                                      CustomerFacingServiceSpec
                                                             0..*




                                 0..1

                         CustomerFacingServiceSpecComposite                                     CustomerFacingServiceSpecAtomic




        HasServicePackageSpecs
                                            ServicePackageSpec

                                        +   type: String
                           0..*




                0..1

                   ServicePackageSpecComposite                                 ServicePackageSpecAtomic




          PlatinumPackageSpec                              SilverPackageSpec                    BronzePackageSpec




                                   GoldPackageSpec                        BestEffortPackageSpec




                                                                                         Figure SO.25 - The Concept of a ServicePackage


© TM Forum 2025. All Rights Reserved                                                                                                  53   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.26 - Grouping Together CustomerFacingServiceSpecifications into a ServicePackage

  For example, GoldPackageSpec is an individual packaging of services, and is therefore an instance of the ServicePackageSpecAtomic class.
  If there was a service offering that combined the services defined by the GoldPackageSpec with those defined by the PlatinumPackageSpec,
  then that would be an instance of the ServicePackageSpecComposite class.

  Figure SO.25 shows five exemplary subclasses of the ServicePackageSpecAtomic class – PlatinumPackageSpec, GoldPackageSpec,
  SilverPackageSpec, BronzePackageSpec, and BestEffortPackageSpec. Ignoring the latter for the moment, each of these classes represents a
  collection of CustomerFacingServiceSpecs that work together to collectively offer a set of Services. This enables these Services to be
  compared as a group to (for example) a ServiceLevelAgreement. Conceptually, this can be represented as shown in Figure SO.26.

  There are two important differences between Platinum, Gold, Silver, and Bronze Service. The first is obvious from Figure SO.26 – the better the
  Service Level, the more CustomerFacingServices that a user has access to. The second is more subtle, and involves the quality of
  CustomerFacingService. For example, all four ServicePackages above provide Web and Data access. The difference between these
  applications is that the quality of Web and Data access for PlatinumService is better from an end-user’s point-of-view (i.e., faster downloads,
  less waiting, etc.) than that for GoldService, and so forth.




© TM Forum 2025. All Rights Reserved                                                          54                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                        Figure SO.26 - Grouping Together CustomerFacingServiceSpecifications into a ServicePackage




© TM Forum 2025. All Rights Reserved                                                                       55                    of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.27 - ServicePackageSpecs and ServicePackages

  The link between a ServicePackageSpec and a ServicePackage is shown in the Figure below.

  A ServicePackage is derived from an associated ServicePackageSpec. The ServicePackageSpec defines the invariant attributes, methods,
  relationships, and constraints for all ServicePackage instances that are derived from it. This enables each individual ServicePackage to add
  its own application-specific changeable characteristics.

  Note that there is no specific association used to relate a particular ServicePackage to the ServicePackageSpec that it is derived from. This is
  because the ServicePackageSpec and ServicePackage both inherit the SpecifiesService association.

  Finally, while the composite pattern could be applied to ServicePackage, there is no perceived need to do so. Multiple ServicePackages will
  simply be related to a ProductBundle, and appear as separate ProductComponents.

  Thus, we see that ServicePackage is a way to define the set of CustomerFacingServiceSpecifications that are to be used by a particular
  ProductSpecification.




© TM Forum 2025. All Rights Reserved                                                           56                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                      SpecifiesCustomerFacingService
                 HasCustomerFacingServiceSpecs
                                                             CustomerFacingServiceSpec
                                                 0..*                                          1..1




                          0..1


                       CustomerFacingServiceSpecComposite                  CustomerFacingServiceSpecAtomic




                                                                                                                                                     0..*

        HasServicePackageSpecs        ServicePackageSpec                                                                               CustomerFacingService         CFSCompositeHasCFServices
                                  +   type: String                                                                              +      status: Integer
                          0..*
                                                                                                                                                                    0..*




               0..1
                                                                                                                                                                                                 0..1

        ServicePackageSpecComposite                     ServicePackageSpecAtomic                            CustomerFacingServiceAtomic                       CustomerFacingServiceComposite




                                                                                                                                                                     ServicePackage
                       PlatinumPackageSpec                   GoldPackageSpec              BestEffortPackageSpec




                                      SilverPackageSpec                    BronzePackageSpec




                                                                          Figure SO.27 - ServicePackageSpecs and ServicePackages


© TM Forum 2025. All Rights Reserved                                                                                                                     57                         of     177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.28 - Relationship Between ServiceBundleSpec and ServicePackageSpec

  The next concept to introduce is that of ServiceBundles.

  Just as ServicePackageSpecs and ServicePackages define the templates and instances of a set of CustomerFacingServices,
  ServiceBundleSpecs and ServiceBundles define the templates and instances of a set of ResourceFacingServices. Note the symmetry – this is
  once again indicative of an extensible, robust information model. The extensibility is, of course, in the use of the ServicePackageSpec and
  ServiceBundleSpec entities. Once the desired specifications have been defined, it is relatively easy to instantiate those templates (thereby
  producing ServicePackage and ServiceBundle entities). Furthermore, this enables different instances to be easily differentiated while
  ensuring that their important characteristics remain constant. This also greatly simplifies their definition and management.

  The following Figure shows the relationship between a ServicePackageSpec and a ServiceBundleSpec.

  A ServiceBundleSpecification is the base class for defining the different classes of bundled ResourceFacingServiceSpecifications that a
  Customer can obtain via a Product. The preferred way to represent a Customer subscription to a Product of this nature is by using the
  association class ServicePackageBundleDetails to define the set of specific ServiceBundleSpecifications that are used by a particular
  ServicePackage.

  Conceptually, a ServiceBundle is thought of as a collection to enable the needs of different sets of ResourceFacingServices to be grouped
  together. The “bundle” conveys the concept of grouped Services that are related. Since these are ResoureFacingSpecifications, they define
  reusable templates for implementing the ResourceFacingServices that are required by a particular CustomerFacingService (as represented
  by a ServicePackage).

  The following Figure shows four exemplary subclasses of ServiceBundle for defining four different groups of Class of Service (CoS). The idea is
  to use each CoSBundle class to represent the Class of Service settings for a specific ServiceBundle. This enables different CoS settings to be
  associated with the different CustomerFacingServices that are defined by a particular ServicePackage, which is what the Customer obtains




© TM Forum 2025. All Rights Reserved                                                          58                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  via a Product. For example, CoS1 could be used for VoIP, CoS2 could be used for mission-critical applications, CoS3 could be used for all
  other applications that are not mission-critical but require better than best-effort delivery, and CoS4 could define best effort service delivery.

  The combination of ServicePackage and ServiceBundle enables a Service Provider to abstract the notion of different classes of service that
  are sold to subscribers. For example, the troublesome use case of provisioning a Customer’s request to upgrade to a higher-level Service (or
  downgrade to a lower-level Service) can now be much more easily and efficiently handled. More importantly, this enables a single link to be
  defined between the low-level QoS model (which controls the mechanisms used in the devices to condition traffic appropriately) and this
  higher-level, business-oriented model.




© TM Forum 2025. All Rights Reserved                                                            59                   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                ServiceSpecification




                                                                                                   RequiresResourceFacingServiceSpec                                                        HasResourceFacingServiceSpecs
                                                   CustomerFacingServiceSpec                                                                             ResourceFacingServiceSpec
                                                                                    0..*                                                        1..*
                                    0..*                                                                                                                                                    0..*
         HasCustomerFacingServiceSpecs



                         0..1                                                                                                                                                                              0..1

           CustomerFacingServiceSpecComposite                            CustomerFacingServiceSpecAtomic                      ResourceFacingServiceSpecAtomic                  ResourceFacingServiceSpecComposite




                                                                                                                                                                                                 ServiceBundleSpec            HasServiceBundleSpecs
                                     ServicePackageSpec           0..*                                                                                                           0..*
                                                                                                                                                                                        +   type: String
                     0..*       +   type: String                                                                                                                                                                            0..*
                                                                                                                 ServicePackageBundleDetails
        HasServicePackageSpecs
                                                                                                           +   bundleSpecValidFor: TimePeriod
                                                                                                           +   preferredBundleSpec: String

                                                                                                                                                                                                                                            0..1
                  0..1

         ServicePackageSpecComposite                               ServicePackageSpecAtomic                                                                     ServiceBundleSpecAtomic                      ServiceBundleSpecComposite




                                                                  Figure SO.28 - Relationship Between ServiceBundleSpec and ServicePackageSpec




© TM Forum 2025. All Rights Reserved                                                                                                                      60                                of      177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.29 - ServiceBundles and ServiceBundleSpecifications

  Specific ResourceFacingServices are related to a ServiceBundleSpecification as shown in the Figure below.




© TM Forum 2025. All Rights Reserved                                                       61                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                   /SpecifiesResourceFacingService
                                            ResourceFacingServiceSpec       1                                          0..*        ResourceFacingService
                               0..*                                                                                           +   rfsStatus: Integer
                                                                                                                       0..*
   HasResourceFacingServiceSpecs
                                                                                           RFSCompositeHasRFServices




                                                         ResourceFacingServiceSpecAtomic
                                                                                                                                                   ResourceFacingServiceAtomic
         0..1                                                                                               0..1


        ResourceFacingServiceSpecComposite                                                           ResourceFacingServiceComposite




                             ServiceBundleSpec                                                              ServiceBundle

                         +   type: String                                                        +    hasMultipleQoSTypes: Boolean
                  0..*


  HasServiceBundleSpecs




           0..1                                                                                       CoS1Bundle                  CoS4Bundle

        ServiceBundleSpecComposite                      ServiceBundleSpecAtomic



                                                                                                               CoS2Bundle                      CoS3Bundle




                                      CoS2BundleSpec                    CoS4BundleSpec




                                                       CoS3BundleSpec              CoS1BundleSpec




                                                                                Figure SO.29 - ServiceBundles and ServiceBundleSpecifications


© TM Forum 2025. All Rights Reserved                                                                                                                             62              of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.30 - Summary Relationships Between ServicePackage and ServiceBundle

  A summary view of the important (not all!) relationships between ServicePackageSpec, ServicePackage, ServiceBundleSpec, and
  ServiceBundle, and their parent classes (again, not all!) is shown in the Figure below. This figure was drawn in order to emphasize the
  symmetry that exists between ServiceSpecifications and Services.




© TM Forum 2025. All Rights Reserved                                                          63                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                            RequiresResourceFacingServiceSpec

                           CustomerFacingServiceSpec               0..*                                                                       1..*              ResourceFacingServiceSpec
                1..1
                                                                  0..*                                                                                                                            1
                                                                                                                                              0..*
                                                                                  HasCustomerFacingServiceSpecs

                                                                                                                   HasResourceFacingServiceSpecs


                       CustomerFacingServiceSpecComposite                                                                                              ResourceFacingServiceSpecComposite
                                                                           0..1                                                        0..1

                                                                                             ServicePackageBundleDetails

                                                                                       +    bundleSpecValidFor: TimePeriod
                                                                                       +    preferredBundleSpec: String
                                 ServicePackageSpec                                                                                                                ServiceBundleSpec

                           +     type: String              0..*                                                                                      0..* +       type: String


         SpecifiesCustomerFacingService                                                                                                                                               /SpecifiesResourceFacingService



                                   ServicePackage                                          ServicePackageUsesServiceBundles                                          ServiceBundle
                                                          0..*                                                                                  0..*
                                                                                                                                                        +       hasMultipleQoSTypes: Boolean




                        CustomerFacingServiceComposite                                                                                                   ResourceFacingServiceComposite

                                                                         0..1                                                                    0..1



                                                       CFSCompositeHasCFServices                                                RFSCompositeHasRFServices


                               CustomerFacingService         0..*                                                                                                ResourceFacingService
                                                                                                                                                 0..*
                                                                                               CFServiceRequiresRFServices
                  0..* +       status: Integer                                                                                                              +    rfsStatus: Integer
                                                                  0..*                                                                        0..*                                                0..*



                                                                  Figure SO.30 - Summary Relationships Between ServicePackage and ServiceBundle


© TM Forum 2025. All Rights Reserved                                                                                                                                             64                                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.31 - Resource Facing Service Specification Pattern



                                                                                          /SpecifiesResourceFacingService
                                                 ResourceFacingServiceSpec        1                                           0..*         ResourceFacingService
                                        0..*
                                                                                                                              0..*
        HasResourceFacingServiceSpecs
                                                                                                  RFSCompositeHasRFServices




                                                                ResourceFacingServiceSpecAtomic                                                       ResourceFacingServiceAtomic
                       0..1                                                                                        0..1
                                                                                      1                                                                              0..*
                      ResourceFacingServiceSpecComposite                                                  ResourceFacingServiceComposite

                                         1                                                                                     0..*




                                        SpecifiesResourceFacingServiceComposite



                                                                                                                  SpecifiesResourceFacingService




                                                                   Figure SO.31 - Resource Facing Service Specification Pattern




© TM Forum 2025. All Rights Reserved                                                                                                      65                       of       177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.32 - Usage Volume Service Specification

  NetworkServiceSpec is a type of CustomerFacingServiceSpec. It represents the common behavior and description of an installed network
  service that will be provisioned in the network to enables usages, like a Mobile Line Service. NetworkProductSpec is derived from
  NetworkServiceSpec.

  NetworkServiceSpec generates 1 to many types of usage described by ServiceUsageSpecification.

  UsageVolumeServiceSpec is a specialization of CustomerFacingServiceSpecAtomic. UsageVolumeServiceSpec is the
  CustomerFacingServiceSpec used for the creation of UsageVolumeProductSpec.

  A UsageVolumeServiceSpec defines buckets of usage, such as hours of national calls, hours of international calls to a specific region,
  volume of data, as examples.

  A UsageVolumeServiceSpec requires one or many NetworkServiceSpecs from which Usages will impact the buckets. It uses 1 to many types
  of usage described by ServiceUsageSpecification. ServiceUsageSpecificaton can impact 0 to many UsageVolumeServiceSpec.

  UsageVolumeServiceSpec can be associated to many rules to Reserve, Debit or Credit an amount on a balance. These rules can also be
  associated to many different UsageVolumeServiceSpec. They inherit from PolicyRule.

  UsageVolumeServiceBalanceReserveRule inherits from PolicyRule. It specifies the general rules to Reserve the UsageVolumeServiceBalance
  depending on ServiceUsage. It also describes to rules associated to quota. It allows the determination of quota to reserve on the
  UsageVolumeServiceBalance according to conditions.

  UsageVolumeServiceBalanceDebitRule inherits from PolicyRule. It specifies rules to debit the UsageVolumeServiceBalance depending on
  ServiceUsage. It specifies the event triggering it (Ex: Call to a given destination exceeding a reserved quota, end of call…), potential conditions
  to be checked and the action to apply if the condition is true (Ex: debit quota or call duration on the UsageVolumeServiceBalance).


© TM Forum 2025. All Rights Reserved                                                             66                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  UsageVolumeServiceBalanceCreditRule specifies rules to apply to credit the UsageVolumeServiceBalance (loyalty, bonus…). It inherits from
  PolicyRule for specifying the event triggering it (Ex: Sum of calls to a given destination over the period exceeding a threshold…), potential
  conditions to be checked (Ex: if the user bought a specific bundle during the period) and the action to apply if the condition is true (Ex: credit
  30mn calls on the UsageVolumeServiceBalance).

                                                 CustomerFacingServiceSpec                                                                                                                           PolicyRuleBase
                                         CustomerFacingServiceSpecAtomic                                                                                                                            PolicyRule




                                                                                                             UsageVolumeServiceSpecHasCreditRule

                                                                                                                  *                     *

           NetworkServiceSpec                                                            UsageVolumeServiceSpec                      UsageVolumeServiceBalanceCreditRule            UsageVolumeServiceBalanceDebitRule           UsageVolumeServiceBalanceReserveRule
                                                /UVServiceSpecRequires
      +   isUsageMonitoring: boolean                                                 +   isShared: boolean
                                       1..*                                      *


                    *                                                                           *             *       *                                                                         *                                          *
                                                                                                                                       UsageVolumeServiceSpecHasDebitRule
     NetworkServiceSpecGeneratesServiceUsageSpec
                                                                                                                                                         UsageVolumeServiceSpecHasReserveRule

                                                       UVServiceSpecConcernsServiceUsageSpecification

                                                     UsageSpecification
                                              ServiceUsageSpecification
                                       1..*                               1..*




                                                                                                       Figure SO.32 - Usage Volume Service Specification




© TM Forum 2025. All Rights Reserved                                                                                                                                             67                                   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.33 NetworkProductSpec / NetworkServiceSpec relationships

  This figure shows the relationship between entities at Product and Service levels.

  A UsageVolumeProductSpec is the restriction of one and only one UsageVolumeServiceSpec.

  A NetworkProductSpec is a restriction of one and only one NetworkServiceSpec.

                                                                                                   /UVProdSpecRequires


                            0..*                                                                                                                                                                    1..*

              AtomicProductSpecification                                                               UsageSpecification                                                           AtomicProductSpecification
                                                                                                                               ProductUsageSpecDescribesNetworkProductSpec
            UsageVolumeProductSpec                  UsageVolumeProductSpecConcerns                  ProductUsageSpec                                                                NetworkProductSpec

        +    isShared                      0..*                                           0..*                               0..*                                       1..* +     isUsageMonitoring: Boolean


                            *                                                                                   0..*                                                                            *


   UsageVolumeProductSpecRestrictsUsageVolumeServiceSpec                                   /ServiceUsageSpecParticipatesIn                                            NetworkProductSpecRestrictsNetworkServiceSp



                            1                                                                                 0..*                                                                              1

        CustomerFacingServiceSpecAtomic                                                                 UsageSpecification                                                       CustomerFacingServiceSpecAtomic
                                              UVServiceSpecConcernsServiceUsageSpecification                                  NetworkServiceSpecGeneratesServiceUsageSpec
            UsageVolumeServiceSpec                                                               ServiceUsageSpecification                                                          NetworkServiceSpec

    +   isShared: boolean                     *                                         1..*                                  1..*                                     * +    isUsageMonitoring: boolean


                        *                                                                                                                                                                    1..*


                                                                                           /UVServiceSpecRequires




                                                                        Figure SO.33 NetworkProductSpec / NetworkServiceSpec relationships




© TM Forum 2025. All Rights Reserved                                                                                                                            68                                  of     177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.1 Customer Facing Service Spec ABE

  The Customer Facing Service Spec ABE defines the common characteristics for a set of CustomerFacingServices. This scales by enabling
  multiple CustomerFacingServiceSpecs to be defined to model the common characteristics of different groups of CustomerFacingServices.

  Figure CFSS.01 - Customer Facing Service Spec ABE Related Entities

  Following are the business entities aggregated under the Customer Facing Service Spec ABE.




© TM Forum 2025. All Rights Reserved                                                    69                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                     ServiceSpecVersion
                                                                                      CustomerFacingServiceSpecVersion




                                                    Entity                                              0..*
                            CFSSpecVersionDetails

                       +   minVersionForUse: String
                       +   preferredVersionToUse: String
                       +   validFor: TimePeriod

                                                                                                         1

                                                                                                    ServiceSpecification
                                                                                                                                  HasCustomerFacingServiceSpecs
                                                                                         CustomerFacingServiceSpec

                                                                                                                           0..*




                                                                                                                                                           0..1


                                                    CustomerFacingServiceSpecAtomic                                   CustomerFacingServiceSpecComposite




                                                                 Figure CFSS.01 - Customer Facing Service Spec ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                                       70                     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.1.1 Customer Facing Service Spec Examples ABE

  The Customer Facing Service Spec Examples ABE contains example subclasses of CustomerFacingServiceSpecs.

  Figure CFSSE.01 - Customer Facing Service Spec Examples ABE Related Entities

  Following are the business entities aggregated under the Customer Facing Service Spec Examples ABE.




© TM Forum 2025. All Rights Reserved                                                   71               of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                     ServiceSpecification
        CustomerFacingServiceSpec




         VPNServiceSpecification




       IPsecVPNServiceSpecification




                                                Figure CFSSE.01 - Customer Facing Service Spec Examples ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                         72                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.1.2 Customer Facing Service Spec Role ABE

  The Customer Facing Service Spec Role ABE defines a ServiceSpecification, in terms of a set of ServiceSpecificationRoles, for a
  CustomerFacingService. It is used to represent the shared characteristics of a CustomerFacingService. This enables the
  CustomerFacingService to be managed abstractly using ServiceSpecificationRoles. It also helps define a
  CustomerFacingServiceSpecification in terms of the functions that it has or provides.

  Figure CFSSR.01 Customer Facing Service Spec Role ABE Related Entities

  Following are the business entities aggregated under the Customer Facing Service Spec Role ABE.



                   RoleSpecification
          ServiceSpecificationRole




       CustomerFacingServiceSpecRole




                                                    Figure CFSSR.01 Customer Facing Service Spec Role ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                          73             of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.1.3 Network Service Spec ABE «Preliminary»

  The Network Service Spec ABE contains the NetworkServiceSpec description and relationships.

  Figure NSS.01 - Network Service Spec ABE Related Entities

  Following are the business entities aggregated under the Network Service Spec Aggregate Business Entity.

              CustomerFacingServiceSpec
        CustomerFacingServiceSpecAtomic




              NetworkServiceSpec

    +     isUsageMonitoring: boolean




                                                           Figure NSS.01 - Network Service Spec ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                          74       of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.1.4 Service Package ABE

  The Service Package ABE defines the concept of bundling a set of different CustomerFacingServiceSpecs to meet the functionality specified
  by one or more ProductSpecifications. This enables the shared characteristics of these CustomerFacingServices to be specified, so that
  multiple Products can be built from their associated ProductSpecification.

  Figure SP.01 - Service Package ABE Related Entities

  Following are the business entities aggregated under the Customer Facing Service Spec Examples ABE.



                                                CustomerFacingServiceSpecComposite
        HasServicePackageSpecs
                                                     ServicePackageSpec

                                 0..*       «required»
                                        +     type: String




               0..1

             ServicePackageSpecComposite                                         ServicePackageSpecAtomic




                                                                             Figure SP.01 - Service Package ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                          75   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.1.4.1           Service Package Spec Examples ABE

  The Service Package Spec Examples ABE contains example subclasses of ServicePackageSpecs.

  Figure SPSE.01 - Service Package Spec Examples ABE Related Entities

  Following are the business entities aggregated under the Service Package Spec Examples ABE.

                                                           ServicePackageSpec
                                                     ServicePackageSpecAtomic




       BestEffortPackageSpec                            BronzePackageSpec                           GoldPackageSpec




                               PlatinumPackageSpec                              SilverPackageSpec




                                                               Figure SPSE.01 - Service Package Spec Examples ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                   76            of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.1.5 Usage Volume Service Spec ABE «Preliminary»

  The Usage Volume Service Spec ABE contains the UsageVolumeServiceSpec and all the entities specific to this type of service.

  Figure UVSS.01 - Usage Volume Service Spec ABE Related Entities

  Following are the business entities aggregated under the Usage Volume Service Spec Aggregate Business Entity.

                                                                PolicyRuleBase                                                                         CustomerFacingServiceSpec
                                                          PolicyRule                                                                          CustomerFacingServiceSpecAtomic




       UsageVolumeServiceBalanceCreditRule    UsageVolumeServiceBalanceDebitRule              UsageVolumeServiceBalanceReserveRule
                                                                                                                                                    UsageVolumeServiceSpec

                                                                                                                                              +     isShared: boolean

                                                                                                                                                           *        *        *
                    *                                       *                                           *
                                                                                                             UsageVolumeServiceSpecHasReserveRule

                                                                                            UsageVolumeServiceSpecHasDebitRule
                                                                       UsageVolumeServiceSpecHasCreditRule



                                                        Figure UVSS.01 - Usage Volume Service Spec ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                                 77                                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.2 Resource Facing Service Spec ABE

  The Resource Facing Service Spec ABE defines the common characteristics for a set of ResourceFacingServices. This scales by enabling
  multiple ResourceFacingServiceSpecs to be defined to model the common characteristics of different groups of ResourceFacingServices.

  Resource Facing Service Spec ABE Related Entities

  Following are the business entities aggregated under the Resource Facing Service Spec ABE.




© TM Forum 2025. All Rights Reserved                                                     78                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                         ServiceSpecVersion
                                                        ResourceFacingServiceSpecVersion



                                 Entity
                                                                           0..*
         RFSSpecVersionDetails

    +   minVersionForUse: String
    +   preferredVersionToUse: String
    +   validFor: TimePeriod


                                                                           1

                                                                   ServiceSpecification
                                                                                                 HasResourceFacingServiceSpecs
                                                            ResourceFacingServiceSpec

                                                                                          0..*




                                                                                                                                 0..1


                          ResourceFacingServiceSpecAtomic                                 ResourceFacingServiceSpecComposite




                                                                               Resource Facing Service Spec ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                                    79   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.2.1 Resource Facing Service Spec Role ABE

  The Resource Facing Service Spec Role ABE defines a ServiceSpecification, in terms of a set of ServiceSpecificationRoles, for a
  ResourceFacingService. It is used to represent the shared characteristics of a ResourceFacingService. This enables the
  ResourceFacingService to be managed abstractly using ServiceSpecificationRoles. It also helps define a ResourceFacingServiceSpecification
  in terms of the functions that it has or provides.

  Figure RFSSR.01 - Resource Facing Service Spec Role ABE Related Entities

  Following are the business entities aggregated under the Resource Facing Service Spec Role ABE.



               RoleSpecification
        ServiceSpecificationRole




     ResourceFacingServiceSpecRole




                                                   Figure RFSSR.01 - Resource Facing Service Spec Role ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                          80              of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.2.2 Service Bundle ABE

  The Service Bundle ABE is a collection of ResourceFacingServiceSpecifications. This enables the needs of different sets of
  ResourceFacingServiceSpecifications to be grouped together, hence the name “bundle”. Since these are ResoureFacingSpecifications, they
  define reusable templates for implementing the ResourceFacingServices that are required by a particular CustomerFacingService (as
  represented by a ServicePackage).

  Figure SB.01 - Service Bundle ABE Related Entities

  Following are the business entities aggregated under the Service Bundle Examples ABE.



                                 Entity                         ResourceFacingServiceSpecComposite
                                                                          ServiceBundleSpec                 HasServiceBundleSpecs
        ServicePackageBundleDetails
                                                                                                     0..*
    +   bundleSpecValidFor: TimePeriod                              «required»
    +   preferredBundleSpec: String                             +     type: String




                                                                                                                                    0..1

                                      ServiceBundleSpecAtomic                                        ServiceBundleSpecComposite




                                                                                     Figure SB.01 - Service Bundle ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                                       81   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.2.2.1             Service Bundle Examples ABE

  The Service Bundle Examples ABE contains example subclasses of ServiceBundleSpec.

  Figure SBE.01 - Service Bundle Examples ABE Related Entities




                                           ServiceBundleSpec
                                    ServiceBundleSpecAtomic




       CoS1BundleSpec                                          CoS2BundleSpec




                              CoS3BundleSpec                                    CoS4BundleSpec




                                                               Figure SBE.01 - Service Bundle Examples ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                82        of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.3.3 Service Catalog ABE

  A collection of entities that represent the specification of ServiceCatalogs and catalogs described by them that contain
  ServiceSpecifications.

  Figure SC.01 - Service Catalog ABE Related Entities

  Following are the business entities aggregated under the Service Catalog ABE.

           CatalogSpecification                                                                 Catalog
                                     ServiceCatalogSpecificationDescribes
    ServiceCatalogSpecification                                                     ServiceCatalog
                                  0..1                                      0..*


                                                                                              0..*




                          ServCatalogServCandidate

                      «required»
                                                                                              0..*
                  +     validFor: TimePeriod
                                                                                   ServiceCandidate

                                                                              +    description: String
                                                                               «required»
                                                                              + ID: String
                                                                              + name: String
                                                                              + status: String
                                                                              + validFor: TimePeriod




                                                                                   Figure SC.01 - Service Catalog ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                                83   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.4     Service ABE
  A Service represents an instance of ServiceSpecification. The Service ABE contains entities that are used to represent both types of Services:
  CSP Know-Hows instances (a.k.a. Customer Facing Services or CFS) and Technical solution (a.k.a. Resource Facing Services or RFS).

  The Service carries the place where the Service is in use if relevant, as well as configuration characteristics, such as assigned telephone
  numbers and internet addresses. The Service also tracks the links to Product realized and/or Resources used.

  Figure SO.06 - Basic Service Model – A Starting Point

  A ComprisedOf recursive association on Service is tempting to add, because it defines the ability to aggregate subordinate Services into a
  higher-level Service. However, this aggregation is a bad idea, as it enables ResourceFacingServices to aggregate CustomerFacingServices,
  which destroys the point of separating them in the first place. Hence, it will not be defined in this model.

  Specifically, a CustomerFacingService is what is bound to a Product, not a Service. ResourceFacingService is not linked directly to Product;
  rather, it is linked to Resource.

  The Figure shows that zero or more CustomerFacingServices are optionally used to realize a Product. The cardinality is zero or more in order
  to allow for the development of Services in a Service Provider or Enterprise before they are offered as a Product or ProductOffering.

  The CFServiceRequiresRFServices association defines the set of ResourceFacingServices that are required by a particular
  CustomerFacingService in order for that CustomerFacingService to operate correctly.

  A ResourceFacingService is related to LogicalResources and PhysicalResources through two associations classes, ServiceLRDependency
  and ServicePRDependency. These association classes define the set of LogicalResources and PhysicalResources, respectively, which are
  required for this ResourceFacingService to function correctly. The ServiceLRDependency is used to define the set of LogicalResources, such
  as memory and DeviceInterfaces, which are required for this particular ResourceFacingService to function correctly. The
  ServicePRDependency have a slightly different connotation. This defines the set of PhysicalResources, such as PhysicalDevices and


© TM Forum 2025. All Rights Reserved                                                           84                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  PhysicalPorts, which are required for this particular ResourceFacingService to function correctly. Thus, the former association class defines
  the operational aspects of the ResourceFacingService, while the latter defines its hosting aspects. This separation is, of course, facilitated by
  the design of the Service (CustomerFacingServices vs. ResourceFacingServices) and Resource (PhysicalResource vs. LogicalResource)
  models.

  Note that a Product has two subclasses, ProductComponent and ProductBundle. A ProductComponent represents a stand-alone Product,
  while a ProductBundle represents Products formed from other Products. Clearly, either of these can serve as the instance that is being
  realized through a combination of CustomerFacingServices and Resources.

  The model shown was built to distinguish between two types of Services – those that are used to realize a Product, and those that are
  required to implement the functionality provided by a Product. These are called CustomerFacingServices and ResourceFacingServices,
  respectively.

  In addition, note the strong link between infrastructure entities and business entities, such as a Product. In particular, this model ensures
  that Customers access Resources and Services through their packaging in a Product. This particular modeling of the complex abstractions
  and relationships between Customer, Product, Service and Resource provides some of the key underpinnings that support what the SID is all
  about.

  The important point of this example is that the VPN Product requires a set of Services. Specifically, our VPN Product requires a combination
  of the BGP ResourceFacingService (and others, but let’s keep it simple for the time being) and the VPN CustomerFacingService. The utility of
  this Figure is that it provides the ability to “package” multiple heterogeneous Services together to realize a Product. This models a
  CustomerFacingService requiring a set of ResourceFacingServices through the CFServiceRequiresRFServices association.

  Continuing the example, the VPN Product that the Customer bought may already have a router that the Customer can use to access the VPN,
  or the Customer may need to purchase one. This is represented using the ProductHasPhysicalResources association.




© TM Forum 2025. All Rights Reserved                                                           85                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                           /ProductReferencesOrReferencedBy

                   ServiceRelationship                                                                                  0..*                 0..*
                                                                                                                                                                                     /ProductHasPhysicalResources
           +   type: String
           +   validFor: TimePeriod                                                                                                      Product
                                                                                                                        0..*                                    0..1
                                                                                      CompositeProductComprisedOf              +      status: String                    ProductRealizedAsResource
                   0..*                       0..*
                                                                                                                               +      validFor: TimePeriod
       ServiceReferencedBy         ServiceReferences                                                                    0..*
                                                                                                                                                                0..*
                   1                         1

                             Service                                                                         0..1

                                                                  ProductRealizedAsCFService
                                                                                                               CompositeProduct                                   AtomicProduct




                                                                               0..*
                                                                                                               ResourceRelationship                        ResourceReferencedBy
                                                              CustomerFacingService
                                                                                                       +     type: String                           0..*
                                                                                                       +     validFor: TimePeriod
                                                                             0..*
                                                                                                                               0..*
                                                              CFServiceRequiresRFServices                        ResourceReferences                                         1

                  ResourceFacingService                0..*                                                                                                Resource
                                                                                                                                         1
                                                                                    RFServiceConfiguredUsing
                                                                                                                                                                                  0..*
                                                                                                                                      0..*
                                                        0..*


                                                                                                                                                                                                                    0..*

                                                                                                                    LogicalResource                                                      PhysicalResource




                                                                                      Figure SO.06 - Basic Service Model – A Starting Point




© TM Forum 2025. All Rights Reserved                                                                                                                                   86                             of    177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.07 - Representing BGP as a LogicalResource

  Let’s consider the simple example of a Customer purchasing a VPN. The VPN itself may be both a Product and a CustomerFacingService,
  since the VPN provides a number of functions (e.g., connectivity) that people commonly refer to as Services. Suppose the VPN is a particular
  type of VPN, defined by RFC2547bis. This specification mandates that BGP (the Border Gateway Protocol, which is an inter-domain routing
  protocol that is used to exchange reachability information with other BGP systems) is used for route advertisement. The Customer doesn’t
  buy BGP services, yet BGP is required for this type of VPN to function. Therefore, BGP is a ResourceFacingService.

  The following Figure takes an extract from the LogicalResource model and shows that BGP is a particular type of RoutingProtocol. This model
  defines several different types of Protocols. A RoutingProtocol is a particular type of protocol that accomplishes routing through the
  implementation of a specific algorithm. Protocols are modeled as a type of LogicalResource.

  Note: Routing is defined as the process of finding a path to a destination.

  To connect this properly, we also need the concept of a LogicalDevice. This is the logical analog to the PhysicalDevice class. A LogicalDevice
  is an abstract base class for all logical resources that are inherently manageable and make up a Product. It is used to describe different types
  of logical features and services that constitute a Product. It has two main purposes: (1) to collect common attributes and relationships for all
  logical resources, and (2) to provide a convenient, single point where relationships with other managed objects can be defined.)

  Thus, BGP is associated with a ResourceFacingService through the RFServiceUsesProtocol aggregation.

  The ProtocolServiceDetails association class defines the Protocols that are required by a particular ResourceFacingService.

  Thus, BGP is associated with a ResourceFacingService through the ProtocolServiceDetails association class. The ProtocolServiceDetails
  association class defines the Protocols that are required by a particular ResourceFacingService.




© TM Forum 2025. All Rights Reserved                                                           87                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                             RFServiceConfiguredUsing
              Resource                                                         ResourceFacingService

   +   usageState: Integer                                        0..*   +    rfsStatus: Integer
                                      0..*
                                                                                               0..1

                                                                                                         ProtocolServiceDetails


                                                                                               0..*

          LogicalResource                                                             Protocol

                 0..1




                                                                                  RoutingProtocol




                 /PathVectorRoutingProtocolConfiguredUsing
                                                                             PathVectorRoutingProtocol
                                                                 0..*




                                                                                         BGP




                                                                              Figure SO.07 - Representing BGP as a LogicalResource




© TM Forum 2025. All Rights Reserved                                                                                              88   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.12 - Modeling Stand-Alone and Aggregate Services

  Similarly as specification part, CustomerFacingService and ResourceFacingService both use the same composite pattern. The difference is
  that since Services are in reality instances defined by a ServiceSpecification, the atomic and composite services are melded into
  CustomerFacingServices and ResourceFacingServices. In other words, generic Services are CustomerFacingServices and
  ResourceFacingServices themselves. While other types of Services could certainly be defined, their associated ServiceSpecification needs to
  be defined first. The following Figure shows the composite pattern applied to CustomerFacingServices and ResourceFacingServices.

                                                                            Service




  RFSCompositeHasRFServices                                                                                                                     CFSCompositeHasCFServices
                                                                        CFServiceRequiresRFServices
                                ResourceFacingService                                                                CustomerFacingService
                         0..*                            0..*                                               0..*
                                                                                                                                              0..*




             0..1
                                                                                                                                                                       0..1

          ResourceFacingServiceComposite           ResourceFacingServiceAtomic                  CustomerFacingServiceAtomic            CustomerFacingServiceComposite




                                                                Figure SO.12 - Modeling Stand-Alone and Aggregate Services




© TM Forum 2025. All Rights Reserved                                                                                           89                        of    177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.20 - The Concept of ServiceRoles

  The ServiceRole class defines a Service in terms of a set of roles. The roles are then associated for both CustomerFacing and ResourceFacing
  services through the CustomerFacingServiceRole and ResourceFacingServiceRole subclasses. The utility of the ServiceRole class is to
  present a single point for accumulating common relationships that its subclasses can inherit.

  The CFSRoleRequiresRFSRoles aggregation is used to define the set of ResourceFacingServiceRoles that are required by a particular
  CustomerFacingServiceRole. Conceptually, this enables roles to be used to define the common characteristics of a set of
  ResourceFacingServices that are required by a particular CustomerFacingService.

  Note that the cardinality of the CFSRoleRequiresRFSRoles is * on the CustomerFacingServiceRole (aggregate) side and 1..* on the
  ResourceFacingServiceRole (component) side. This is because a ResourceFacingServiceRole can exist without being bound into a
  CustomerFacingServiceRole (e.g., in testing the network), but a CustomerFacingServiceRole requires at least one
  ResourceFacingServiceRole to function. Note also that this cardinality is symmetric with the cardinality defined in the
  CFServiceRequiresRFServices association.

  The InvolvedServiceRoles association is used to define a set of ServiceRoles that are involved with, or related to, each other in order to build a
  particular type of Service. This association applies equally to CustomerFacingServices and ResourceFacingServices. For example, consider
  the definition of a set of “QoS packages” that each consist of a set of different Classes of Service. Each Class of Service definition is
  associated with different types of traffic, and defines how each type of traffic should be conditioned independently of other types of traffic.
  The higher-level QoS package is clearly a CustomerFacingService, since it is obtained via a Product by a Customer. Equally clearly, the lower-
  level Class of Service definitions are each ResourceFacingServices, since the Customer has obtained a higher-level package and doesn’t
  have explicit knowledge of these sub-services. Now, assume that there is a dependency that exists between a sub-service and either another
  sub-service or the QoS package itself, such as a limit as to how many instances of one type of Service can be created, or that each sub-
  service must first be instantiated before a QoS package is completed. These are examples of the InvolvedServiceRoles association.


© TM Forum 2025. All Rights Reserved                                                            90                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Continuing the example, the CustomerFacingServiceRole (e.g., “Gold Service”) is built, or constructed from, a set of
  ResourceFacingServiceRoles (e.g., “Rate Limiting Service” and “Remarking Service”). The former ensures that the Customer sends only the
  amount of traffic that he or she is contractually allowed to send, and the latter prioritizes different types of traffic. The Gold Service simply
  won’t work unless these two Services are built and active, but the Customer doesn’t need to explicitly know about them. These and other QoS
  functions are discussed in the QoS Service guide book.

  Conceptually, ServiceRoles represent the variable characteristics of a Service from the viewpoint of functions (i.e., roles) that the Service
  provides to the rest of the environment. One example is that VPNs need to control how routing information is exchanged between the CE and
  PE routers at the edges of the Service Provider’s backbone and between the PE routers across the Service Provider’s backbone. ServiceRoles
  can be defined that represent how routing is constrained, depending if the router is a CE, PE, or P router.

  This enables the Service to be managed abstractly using ServiceRoles. It also helps define the Service in terms of the functions that it has or
  provides. This is important, as it makes the management independent of the particular type of VPN and, more importantly, type of device and
  protocol used.

  The CustomerFacingServiceRole and ResourceFacingServiceRole subclasses are used to represent the variable characteristics of
  CustomerFacingServices and ResourceFacingServices, respectively, in terms of roles that these services play. The set of roles define the
  Service in terms of the functions that it performs. This enables it to be modeled independently of the protocols, devices, and other dependent
  entities, as well as the environment in general.




© TM Forum 2025. All Rights Reserved                                                           91                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                                                                    InvolvedServiceRoles

                                                                                                                                             0..*

                                                                                             UsesServiceRoles
                                              Service                                                                             ServiceRole
                                                                   1                                                    0..*                               0..*




        ResourceFacingService                                 CustomerFacingService                      CustomerFacingServiceRole                        ResourceFacingServiceRole

         0..*         0..*                                       0..*   0..*                                  0..*       0..*                                     1..*                0..*
                                CFServiceRequiresRFServices
                                                                                  CFServiceHasCFSRoles
                                                                                                                                CFSRoleRequiresRFSRoles

                                                                                RFServiceHasRFSRoles



                                                                               Figure SO.20 - The Concept of ServiceRoles




© TM Forum 2025. All Rights Reserved                                                                                                        92                             of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.35 - Interaction Between PartyRole and Service

  A PartyRole defines the function that a Party takes on. PartyRoles can represent the ability to manage, configure, use, and perform other types
  of interactions with Services. A simple starting model is shown in the Figure below.

  One can see that the Service and Resource management methods are symmetrical. Therefore, this section will only discuss the Service
  ownership and administration classes.

  The OwnsServiceDetails association class defines a Service (CustomerFacing or ResourceFacing) that a particular PartyRole owns. Note that
  this is a very different relationship than the AdministersServiceDetails association class. The OwnsServiceDetails association class defines
  the PartyRole that is the owner of the Service. Here, “owner” is the person or group that is responsible (e.g., organizational, financial, and so
  forth) for the Service. Note that the cardinality of the OwnsServiceDetails association class on the PartyRole side is 1 – this means that a
  Service MUST have at least one PartyRole to manage it. Furthermore, the cardinality of this association on the Service side is *, which ensures
  that a PartyRole doesn’t have to own a Service.

  The AdministersServiceDetails association class defines a Service (CustomerFacing or ResourceFacing) that a particular Party, playing a
  PartyRole, administers. From a business perspective, the Owner has to either appoint or give permission to the Administrator to administer
  the Service that is owned. This is done using the GrantsServiceAdminRights association class.

  The GrantsServiceAdminRights association defines which PartyRoles are allowed to administer a particular owned Service. Different
  PartyRoles will in general have different administration rights for the same Service. For example, different types of Administrators will in
  general each have the ability to make more changes than different types of Technicians.

  Policies can be defined for controlling the specific rights of administering a Service. This is the function of the ServiceManagementPolicy
  class. Only a simple single attribute is shown.



© TM Forum 2025. All Rights Reserved                                                            93                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  The ServiceManagementPolicy class defines the particular policies that are used to define how different aspects of the Service are managed
  and maintained. For example, assume that a Service is made up of several sub-Services. One of these sub-Services might require multiple
  PartyRoles to approve changes to its configuration, whereas another sub-Service might not require any approvals to change its configuration.
  Since Policy also uses the composite pattern, if a set of Policies are needed, these can be aggregated into a single Policy).

  Note the power of this pattern – the ManagementPolicyForService association, along with its ServiceManagementPolicy class, provide a
  generic template for defining which set of PartyRoles can perform which type of management function for which type of Service. Figure SO.35
  shows that Services and Resources can be managed using the same pattern, even though the contents of the classes will be different.

  There is a lot more to the model that may be developed further.




© TM Forum 2025. All Rights Reserved                                                        94                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




               OwnsServiceDetails                                                                                                OwnsResourceDetails

        0..1                                                                                                                                         0..1
                                                                 1                PartyRole
                                                                                                       1

                                                                       0..*                                0..*
    GrantsServiceAdminRights
                                                                                                                                  0..*
                                          0..*
                                                                                                                         Resource
                                Service
                                                                                                                  0..*
                                                 0..*
                                                                                                                              GrantsResourceAdminRights


                                                        TechnologyAdministrator               Technician

        0..*
                                                                                                                                                     0..*
          AdministerServiceDetails
                                                                                                                              AdministerResourceDetails
                         0..*
                                                                                                                                              0..*
      ManagementPolicyForService
                                                                                                                          ManagementPolicyForResource
                         0..*
                                                                                                                                              0..*
         ServiceManagementPolicy
                                                                                                                              ResourceManagementPolicy




                                                               Figure SO.35 - Interaction Between PartyRole and Service




© TM Forum 2025. All Rights Reserved                                                                                     95                                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.36 - Interaction between Service and Place

  In the SID, different types of Places have different types of semantics associated with them. For example, a Wireless Access Point has an
  associated coverage area. Only applications within that coverage area can use the services associated with the Wireless Access Point. As
  another example, subscribers will access different POPs (Points of Presence, the Service Provider term for an access network) as they travel
  nationally and internationally. Services may vary, and additional peering relationships may come into effect. A simple starting model relating
  Service to Place is shown in Figure below.

  Note that the ServicePlaceDetails association is implemented as an association class. Its purpose is to represent the semantics of this
  particular association, such as which specific Services are associated with this Place. Clearly, policies can be used to more fully define the
  semantics of a particular Place.

           Service                                                                Place

                           0..*                                     0..* +   ID: String
                                                                         +   validFor: TimePeriod




                                          ServicePlaceDetails

                                  +   installedTimeStamp: DateTime
                                  +   isLocatedAt: Boolean
                                  +   toBeInstalledTimeStamp: DateTime
                                  +   toBeLocatedAt: Boolean




                                                                   Figure SO.36 - Interaction between Service and Place




© TM Forum 2025. All Rights Reserved                                                                                96    of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.37 - NetworkServiceSpec / UsageVolumeServiceSpec instantiation

  A NetworkService is described by one and only one NetworkServiceSpec. A NetworkServiceSpec can describe several NetworkService.

  NetworkService is a type of CustomerFacingServiceAtomic.

  A UsageVolumeService is described by one and only one UsageVolumeServiceSpec. A UsageVolumeServiceSpec can describe several
  UsageVolumeService.

  UsageVolumeService is a type of CustomerFacingServiceAtomic.

  A NetworkService generates 1 to many ServiceUsage.

  A UsageVolumeService is concerned by 1 to many ServiceUsage.




© TM Forum 2025. All Rights Reserved                                                    97                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                                        /UVServiceSpecRequires



                                       *                                                                                                                                                                                      1..*
                   CustomerFacingServiceSpecAtomic                                                                          UsageSpecification                                                              CustomerFacingServiceSpecAtomic
                         UsageVolumeServiceSpec              UVServiceSpecConcernsServiceUsageSpecification          ServiceUsageSpecification          NetworkServiceSpecGeneratesServiceUsageSpec                 NetworkServiceSpec

                    +     isShared: boolean             *                                                     1..*                               1..*                                                     * +     isUsageMonitoring: boolean


                                           1                                                              +serviceUsageSpec         0..1                                                                                        1



         UsageVolumeServiceDescribedByUsageVolumeServiceSpec                                                         ProductUsageSpecDescribes                                                        NetworkServiceDescribedByNetworkService




                                      0..*                                                                       +serviceUsage 0..*                                                                                            0..*

                        CustomerFacingServiceAtomic                                                                                  Usage                                                                      CustomerFacingServiceAtomic

                           UsageVolumeService                      UsageVolumeServiceIsConcernedBy                         ServiceUsage                    NetworkServiceGeneratesServiceUsage                        NetworkService
                                                      0..1                                                       1..*                        1..*                                                           1


                                           0..*                                                                                                                                                                                 1..*

                                                                                                                           /UVServiceRequires




                                                                 Figure SO.37 - NetworkServiceSpec / UsageVolumeServiceSpec instantiation




© TM Forum 2025. All Rights Reserved                                                                                                                         98                             of    177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.38 - UsageVolumeService detailed view

  NetworkService generates usage when Services are used. The usage managed by associated UsageVolumeService is analyzed according to
  the rules associated to the UsageVolumeService.

  These rules determine, according to events and conditions, the action to execute that can correspond to:

          •       UsageVolumeServiceBalanceReserve (used only in case of supervized NetworkService): Reservation of a Quota on the UsageVolumeServiceBalance
          according to the evaluation of the usage event,
          •       UsageVolumeServiceBalanceDebit: Debit of an amount that may correspond to:

          - In case of supervized NetworkService: the previously reserved Quota or the amount of the Quota that was really consumed according
  to the evaluation of the usage event,

          - In case of non supervized NetworkService: The usage performed.

          •      UsageVolumeServiceBalanceCredit: Credit of an amount or a bonus on a UsageVolumeServiceBalance according to the evaluation of the usage
          event.



  A ServiceUsage can be associated to a UsageVolumeService depending on its type. The proposed model supports standard usage cases and
  also some more complex. As examples:

          •      In case of calls to toll free numbers UsageVolumeServiceBalanceReserveRule and UsageVolumeServiceBalanceDebitRule can be defined to
          consider that usage related to toll free numbers do not have any impact on the UsageVolumeServiceBalance.




© TM Forum 2025. All Rights Reserved                                                                 99                   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




            •       In case of usage that can be done several times during a period (example: a VOD that can be viewed as many times as user wants during 48 hours),
            UsageVolumeServiceReserveRule and UsageVolumeServiceBalanceDebitRule can be defined to consider that for this specific type of event, only the first
            event should require a reservation and a debit during a configured period.

                                                                               UsageVolumeServiceSpecHasCreditRule
                                                                                                                                                                                  CustomerFacingServiceSpecAtomic
                                                                                                     UsageVolumeServiceSpecHasDebitRule                                       *
                                                                                                                                                                                       UsageVolumeServiceSpec
                                                                                                                             UsageVolumeServiceSpecHasReserveRule             * +       isShared: boolean
                              *                                   *                                                      *                                                    *
                                  PolicyRule                             PolicyRule                                              PolicyRule                                                   1

      UsageVolumeServiceBalanceCreditRule      UsageVolumeServiceBalanceDebitRule               UsageVolumeServiceBalanceReserveRule                    UsageVolumeServiceDescribedByUsageVolumeServiceSpec
                                                                                                                                                                                                                      UsageVolumeServiceIsConcernedBy


                          1                                      1                                                   1                                                                            0..*                0..1                              1..*

                                                                                                                                                                                      CustomerFacingServiceAtomic                                         Usage
                                                                                                                                                                                         UsageVolumeService                                  ServiceUsage

       UVServiceBalanceCreditRuleGenerates     UVServiceBalanceDebitRuleGenerales                UvServiceBalanceReserveRuleReserves

                                                                                                                                                                                             1           0..*                                          1..*

                                                                                                                                                              UsageVolumeServiceContains                                      NetworkServiceGeneratesServiceUsa

                          *                                      *                                                   *

          UsageVolumeServiceBalanceEntry          UsageVolumeServiceBalanceEntry                      UsageVolumeServiceBalanceEntry
                                                                                                                                                    UsageVolumeServiceBalance                                                                      1
        UsageVolumeServiceBalanceCredit         UsageVolumeServiceBalanceDebit                   UsageVolumeServiceBalanceReserve
                                                                                                                                                    +   /remainingValue: Quantity                                                    CustomerFacingServiceAtomic
                                                                                                                                                                                  1..*
                                                                                                                                                    +   validFor: TimePeriod                             /UVServiceRequires                NetworkService
                                                                                                                                                                                                                              1..*
                         *                                       *                                   *                                                    1           1           1
                                                                                                         UsageVolumeServiceBalanceReserveReserves

                                                                                             UsageVolumeServiceBalanceDebitDebits
                                                                         UsageVolumeServiceBalanceCreditCredits




                                                                               Figure SO.38 - UsageVolumeService detailed view




© TM Forum 2025. All Rights Reserved                                                                                                                          100                                   of          177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.4.1 Customer Facing Service ABE

  The Customer Facing Service ABE defines the characteristics of a particular CustomerFacingService that represents a realization of a Product
  within an organization's infrastructure. In contrast, the Resource Facing Service ABE is an abstraction that defines the characteristics of a
  particular ResourceFacingService which support the network/infrastructure facing part of CustomerFacingService. ResourceFacingServices
  are "internal" Services that are required to support a CustomerFacingService.

  Entities in this ABE provide different views to examine, analyze, configure, monitor and repair CustomerFacingServices of all types. Entities in
  this ABE are derived from Customer Service Specification entities.

  Figure CFS.01 - Customer Facing Service ABE Related Entities

  Following are the business entities aggregated under the Customer Facing Service Spec Examples ABE

                                                                 Service
            CFSCompositeHasCFServices          CustomerFacingService

                                        0..*       «required»
                                               +     status: Integer




     0..1


            CustomerFacingServiceComposite                                 CustomerFacingServiceAtomic




                                                                              Figure CFS.01 - Customer Facing Service ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                               101       of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.4.1.1 Customer Facing Service Example ABE

  The Customer Facing Service Example ABE contains an example CustomerFacingService entity.

  Figure CFSE.01 - Customer Facing Service Example ABE Related Entities

  Following are the business entities aggregated under the Customer Facing Service Example ABE.

                        Service
      CustomerFacingService

          «required»
      +     status: Integer




           IPsecVPNService




                                                    Figure CFSE.01 - Customer Facing Service Example ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                         102            of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.4.1.2 CustomerFacing Service Role ABE

  The Customer Facing Service Role ABE defines CustomerServiceRoles that are used to represent the variable characteristics of a
  CustomerFacingService in terms of roles that this type of Service plays.

  4.4.1.3 Network Service ABE «Preliminary»

  The Network Service ABE contains the NetworkService description and relationships.

  Figure NS.01 - Network Service ABE Related Entities

  Following are the business entities aggregated under the Network Service Aggregate Business Entity.

              CustomerFacingService
       CustomerFacingServiceAtomic




             NetworkService




                                                               Figure NS.01 - Network Service ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                           103   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.4.1.4 Usage Volume Service ABE «Preliminary»

  The Usage Volume Service ABE contains the UsageVolumeService and all the entities specific to this type of service.

  Figure UVS.01 - Usage Volume Service ABE Related Entities

  Following are the business entities aggregated under the Usage Volume Service Aggregate Business Entity.

                                                        UsageVolumeServiceBalanceEntry

                                                +       date: DateTime
                                                +       description: string
                                                +       value: Quantity




        UsageVolumeServiceBalanceCredit             UsageVolumeServiceBalanceReserve                UsageVolumeServiceBalanceDebit



                                                                                                                                                        CustomerFacingService
                          *                                                    *                                *                                CustomerFacingServiceAtomic

      UsageVolumeServiceBalanceCreditCredits
                                                                                                    UsageVolumeServiceBalanceDebitDebits
                                               UsageVolumeServiceBalanceReserveReserves




                                                           1                   1         1

                                                          UsageVolumeServiceBalance                                                                  UsageVolumeService
                                                                                                         UsageVolumeServiceContains
                                                    +     /remainingValue: Quantity
                                                    +     validFor: TimePeriod               1..*                                            1




                                                                              Figure UVS.01 - Usage Volume Service ABE Related Entities


© TM Forum 2025. All Rights Reserved                                                                                                       104                          of      177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.4.2 Resource Facing Service ABE

  The Service ABE contains entities that are used to represent two fundamentally different types of Services, called CustomerFacingServices
  and ResourceFacingServices.

  A CustomerFacingService defines the characteristics of a particular Service that represents a realization of a Product within an organization's
  infrastructure. In contrast, a ResourceFacingService is an abstraction that defines the characteristics of a particular Service which support
  the network/infrastructure facing part of the service. For example, a VPN is an example of a CustomerFacingService, while the sub-services
  that perform different types of routing between network devices making up the VPN are examples of ResourceFacingServices.
  ResourceFacingServices are "internal" Services that are required to support a CustomerFacingService.

  Entities in this ABE provide different views to examine, analyze, configure, monitor and repair Services of all types. Entities in this ABE are
  derived from Service Specification entities.

  Figure RFS.01 - Resource Facing Service ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                             105                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                               Service
         RFSCompositeHasRFServices           ResourceFacingService

                                      0..*       «required»
                                             +     rfsStatus: Integer




               0..1
                                                                                                            ManagedEntity
            ResourceFacingServiceComposite                        ResourceFacingServiceAtomic
                                                                                                       ProtocolServiceDetails




                      ServiceBundle

           +    hasMultipleQoSTypes: Boolean




                                                                              Figure RFS.01 - Resource Facing Service ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                               106       of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.4.2.1 Resource Facing Service Examples ABE

  The Resource Facing Service Examples ABE contains examples of ResourceFacingServices.

  Figure RFSE.01 - Resource Facing Service Examples ABE Related Entities

  Following are the business entities aggregated under the Resource Facing Service Examples ABE.

                                 ResourceFacingServiceComposite
                                       ServiceBundle

                           +   hasMultipleQoSTypes: Boolean




       CoS1Bundle                               CoS2Bundle




                          CoS3Bundle                                     CoS4Bundle




                                                             Figure RFSE.01 - Resource Facing Service Examples ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                   107            of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.4.2.2 Resource Facing Service Role ABE

  The Resource Facing Service Role ABE defines ResourceServiceRoles that are used to represent the variable characteristics of a
  ResourceFacingService in terms of roles that this type of Service plays.

  Figure RFSR.01 - Resource Facing Service Role ABE Related Entities

  Following are the business entities aggregated under the Resource Facing Service Role ABE.

                            Role
              ServiceRole




       ResourceFacingServiceRole




                                                       Figure RFSR.01 - Resource Facing Service Role ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                           108          of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.5     Service Configuration ABE
  The Service Configuration ABE represents the specification of the different possible Service configurations as well as the Service
  Configurations instantiated for a Service.

  Figure CP.01 - Configuration Spec and Configuration (copy from Common)

  A Configuration (also referred to as a Profile) defines how a Resource, Service, or Product operates or functions. A Configuration may contain
  one or more parts (which is realized by using the Atomic/Composite pattern, but it is represented as a single entity -
  ConfigurationRelationship), and each part may contain zero or more fields. Each field may have attributes that are statically or dynamically
  defined. Some of these fields have fixed values, while others provide values from which a choice or choices can be made (e.g., using the
  EntitySpec/Entity and/or CharacteristicSpec/CharacteristicValue patterns).

  Starting from the right-side of the figure:

          •       The Resource, Service and Product classes are as defined in the SID model.
          •       The associated configuration objects are used to define additional properties (attributes) of the associated entity. For example, consider an
          Equipment instance (a Resource). The intrinsic properties of the Equipment instance (perhaps but not necessarily common to all Equipment
          instances) are defined in the Resource itself. Additional properties (which may not be common to all Equipment instances) are provided in one or
          one Resource Configuration instances.
          •       It is possible to relate one instance of Configuration to several others via the ConfigRelationship. This is useful when configuring complex
          (aggregate) entities. For example, to configure a circuit pack, one may also need to configure the various ports supported by the circuit pack and in
          turn, the connection termination points supported by the ports.

  On the left-side of the figure, there are various Configuration Specifications that correspond to the various Configuration classes on the right-
  side of the figure. This is the typical EntitySpecification/Entity pattern already present in the SID model but now applied to a particular kind of
  Entity, i.e., a Configuration. The EntitySpecification represents the definition of an entity. The idea is that the various ResourceConfigSpec
  instances are reusable across many instances of Resource.


© TM Forum 2025. All Rights Reserved                                                                   109                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




   class Figure CP.01 - Configuration Spec and Configuration



                                                ConfigSpecRelationship                                                                                                        ConfigRelationship

                                       +    configSpecRelationshipType: String                                                                                     +    status: String
                                       +    validFor: TimePeriod                                                                                                   +    validFor: TimePeriod [0..1]

                                                     0..*                    0..*                                                                                         0..*                           0..*

                       ConfigSpecReferencedBy                                ConfigSpecReferences                                             ConfigurationReferences                                    ConfigurationReferenceBy
                                                     1                       1                                                                                            1                              1

                                              ConfigurationSpecification                                                                                                         Configuration

                                        +    description: String                                            ConfigurationSpecificationDescribes                       +    dateCreated: DateTime
                                        +    ID: String                             0..1                                                                         0..* +    description: String
                                        +    name: String                                                                                                             +    validFor: TimePeriod
                                        +    validFor: TimePeriod                                                                                                     +    version: String
                                        +    version: String




           ServiceConfigSpec                     ResourceConfigSpec                        ProductConfigSpec                     ProductConfiguration                      ServiceConfiguration                      ResourceConfiguration


                        0..*                                   0..*                                  0..*                                         0..*                                    0..*                                      0..*

      ServiceConfigSpecDefinedFor             ResourceConfigSpecDefinedFor
                                                                                     ProductConfigSpecDefinedFor              ProductConfigurationDefinedFor            ServiceConfigurationDefinedFor          ResourceConfigurationDefinedFor

                                                                                                     1                                            1                                       1                                         1
                       1                                       1

           ServiceSpecification                 ResourceSpecification                  ProductSpecification                              Product                                    Service                                Resource




                                                                        Figure CP.01 - Configuration Spec and Configuration (copy from Common)




© TM Forum 2025. All Rights Reserved                                                                                                                                      110                                   of      177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure CP.02 - Configuration Specs Associations (copy from Common)

  The following Figure emphasizes the reusability of the various Configuration Specifications. So, for example, a single instance of
  ProductConfigSpec could be applies to many ProductConfiguration instances.

   class Figure CP.02 - Configuration Specs Associations



            ProductConfigSpec                              ProductConfigSpecDescribes             ProductConfiguration

                                          0..1                                             0..*




            ServiceConfigSpec                                                                     ServiceConfiguration
                                                           ServiceConfigSpecDescribes
                                          0..1                                             0..*




           ResourceConfigSpec                              ResourceConfigSpecDescribes            ResourceConfiguration

                                          0..*                                             0..1




                                                                    Figure CP.02 - Configuration Specs Associations (copy from Common)




© TM Forum 2025. All Rights Reserved                                                                                       111           of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure CP.03a - Entities Serve as Configuration Specifications (Copy from Common)

  In some cases a Product, Service, or Resource entity may play the role of a Configuration Specification as shown in the following Figure.

  The entity’s attributes (with the entity playing the role of a Configuration Specification) are used to set the values for other entities. In this
  case, the attributes can be “discovered” by code. If they have a value, it is used to set the value for another entity of the same type. One
  restriction applies here, i.e., attributes of an entity (playing the role of a Configuration Specification) must be able to be set to null (if not
  needed for a given situation) even if the attribute value is normally required to be set in the entity (when the entity is not playing the role of a
  Configuration Specification). This approach (of allowing entities to play the role of a Configuration Specification) is needed to avoid turning
  fixed (intrinsic) attributes of an entity into flexible, dynamic characteristics.




© TM Forum 2025. All Rights Reserved                                                               112                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




   class Figure CP.03a - Entities Serve as Configuration Specifications



             ProductConfigSpec                                                                                    Product

                                                                          ProductServesAs                  +   status: String
                                                                                                           +   validFor: TimePeriod
                                             0..*                                                   0..1




             ServiceConfigSpec                                                                                        Service
                                                                          ServiceServesAs
                                                                                                           +   hasStarted: Boolean
                                             0..*                                                   0..1
                                                                                                           +   isMandatory: Boolean
                                                                                                           +   isServiceEnabled: Boolean
                                                                                                           +   isStateful: Boolean
                                                                                                           +   startMode: Integer




            ResourceConfigSpec                                            ResourceServesAs                         Resource

                                             0..*                                                    0..1 +     usageState: Integer




                                                                Figure CP.03a - Entities Serve as Configuration Specifications (Copy from Common)

  4.6         Service Order ABE
  The Service Order ABE contains all entities that represent a type of Request of one or several services for any type of Service Specification. A
  Service Order decomposes a Product Order's products into the services associated with a ServiceOrder through which the products are
  realized.




© TM Forum 2025. All Rights Reserved                                                                                                       113      of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SOr.01 - Service Order Entities

  ServiceOrders, which are used to provision services, can be initiated in a number of ways, such as by a CustomerOrder to provision
  CustomerFacingServices that realized the Product(s) on the order or to reconfigure/reprovision Services as a result of a problem with them.

  The following Figure shows the basic model and how ServiceOrder and ServiceOrder item inherit from entities in the Business Interaction
  ABE.

                                                                                                 /SpecifiesService
                                           ServiceSpecification        1                                                             0..*             Service

                                                    0..1                                                                                                               0..1




                                   BusinessInteractionItemInvolvesServiceSpecification
                                                                                                                              BusinessInteractionItemInvolvesService




                                                                                              0..*     BusinessInteractionItem
                                                      BusinessInteractionComprisedOf
          BusinessInteraction
                                       1                                                      0..*                                   0..*




               Request



                                                           ServiceOrderComprisedOf                               ServiceOrderItem
             ServiceOrder
                                1..1                                                                  0..*



                                                                                         Figure SOr.01 - Service Order Entities




© TM Forum 2025. All Rights Reserved                                                                                                           114                            of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SOr.02 - Relationships Inherited From Business Interaction

  ServiceOrder inherits a number of associations that entities in the Business Interaction ABE have with entities in other ABEs as shown in the
  following Figure.

               Place                   BusinessInteractionLocationDescribedByPlace
                               1                                                        0..*          BusinessInteractionLocation

                                                                                               +    locationRole: String

                                                                                                              0..*
                                                                                                                                                           BusinessInteractionType


                                                                               BusinessInteractionLocationSpecifiesThePlaceForBI                                                      1




                                                                                                            0..1
                                                                                                                                             BusinessInteractionTypeCategorizes
                                                          BusinessInteractionInvolves                     BusinessInteraction
                                                                                                                                    0..*
                                                                                                     +    description: String
                                                          0..*                                     1 +    endDate: DateTime
                                                                                                     +    ID: String
                                           BusinessInteractionRole                                   +    startDate: DateTime              BusinessInteractionRelationship
                                                                                                     +    status: String
                                   +   name: String

                                                                                                                                                          BusinessInteractionRelationship

                                                                                                                                                    +   type: String
                                                                                                                                                    +   validFor: TimePeriod



        PartyInteractionRole                  ResourceInteractionRole                              CustomerBillingAccountInteractionRole




                                                                  Figure SOr.02 - Relationships Inherited From Business Interaction




© TM Forum 2025. All Rights Reserved                                                                                                                    115                          of     177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SOr.03 - Relationships Inherited From BI Item

  ServiceOrderItem also inherits a number of associations that entities in the Business Interaction ABE have with entities in other ABEs as
  shown in the following Figure.

                                                                       BusinessInteractionLocationDescribedByPlace
                 BusinessInteractionLocation                                                                                             Place
                                                            0..*                                                           1
         +    locationRole: String

                           0..*                      0..*

                                                                                                                                                                  BusinessInteraction
                                                                      BusinessInteractionLocationSpecifiesThePlaceForBI
                                                                                                                                                            +    description: String
                                                                                                                                                       0..1 +    endDate: DateTime
    BusinessInteractionLocationSpecifiesThePlaceForBIItem                                                                                                   +    ID: String
                                                                                                           BusinessInteractionComprisedOf                   +    startDate: DateTime
                                                                                                                                                            +    status: String
                                                                                                                                                          1
                                                                                                                                                                               1

                                                                                                                                            BusinessInteractionInvolves

                           0..1               0..*            0..* /BusinessInteractionItemReferences                                                                          0..*

                   BusinessInteractionItem
                                                             0..*                                                                                                 BusinessInteractionRole
                                                                                                     BusinessInteractionItemInvolves
             +   action: String
                                                                                                                                                           +    name: String
             +   quantity: Quantity
                                                            0..*                                                                                0..*




                      ServiceOrderItem                                                          PartyInteractionRole                   ResourceInteractionRole                        CustomerBillingAccountInteractionRole




                                                                                       Figure SOr.03 - Relationships Inherited From BI Item



© TM Forum 2025. All Rights Reserved                                                                                                                              116                               of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.7     Service Usage ABE
  The Service Usage ABE represents the specification of Service Usage types and collects Service Usage records with their characteristics
  (a.k.a. consumption data).

  Figure U.02 - Usage Specification (copy from Common)

  The following Figure shows abstract business entities that are used to model usage. The model shown below is generic.

  The UsageSpecification class describes a type of usage. In order to achieve a flexible structure of the UsageSpecification all its attributes are
  stored as characteristics. Alternatively, different types of usage could be modeled as sub-classes of the Usage entities (Usage,
  ProductUsage, ServiceUsage, ResourceUsage).

  The UsageSpecification is comprised of UsageSpecCharacteristics that define all characteristics (attributes) known by a particular type of
  usage. Each characteristic is described by its name, category, presence and a set of allowed values.

          •       Name defines a unique name that identifies the characteristic.
          •       Category defines one of the high-level aspects of the usage information described by the characteristic. These categories are commonly
          referred to as: Who, When, What, Where, and Why.
          •       Min and Max cardinalities that defines whether the characteristic is required or optional.

  Additional details about the Characteristic pattern can be found in GB922-1R Root Business Entities addendum.

  The set of allowed values is modeled with UsageSpecCharacteristicValue. This class describes all allowed values or value ranges.




© TM Forum 2025. All Rights Reserved                                                                117                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  The Usage class represents a usage event. It is described by the UsageSpecification and comprised of UsageCharacteristicValues that hold
  data attributes of a usage specified by UsageSpecCharacteristics. The UsageCharacteristic can either store its value in the usageCharValue
  property or reference predefined UsageSpecCharacteristicValue.




© TM Forum 2025. All Rights Reserved                                                        118                of   177
     Information Framework (SID) Suite Service Domain R25.0.0




    class Figure U.02 - Usage Specification



                                                          UsageSpecVersion

                        RootEntity               +   description: String
                                                 +   usageSpecRevisionDate: DateTime
                +   description: String          +   usageSpecRevisionNumber: Integer
                +   ID: String                   +   usageSpecRevisionType: String
                +   name: String                 +   validFor: TimePeriod

                                                                        0..*
                                                                       UsageSpecModificationsRecordedAs

                                                                       1
                    EntitySpecification                                                   /UsageSpecDescribes
                                                                                                                                                                                     UsageCharacteristicCategory
                +   status: String                       UsageSpecification                                                    Usage
                                                                                    0..1                                                                                   +      description: String
                +   validFor: TimePeriod                                                                        0..*   +   usageDate: DateTime                             +      name: String
                                                                   1
                                0..1                                                                                   +   usageStatus: Integer
                                                                                                                                                                                                         1
                                                                                                                                        1
                 EntitySpecFurtherDefinedBy
                                0..*                              /UsageSpecFurtherDefinedBy
                                                                                                                   UsageDescribedBy                                                                     UsageSpecCharCategorizedBy
                    EntitySpecCharUse

       +       canBeOverridden: Boolean
                                                                                                                                                                                                        0..*
       +       description: String                                 0..*
       +       extensible: Boolean
                                                                                                                                                                                                                                         CharacteristicSpecification
       +       isPackage: Boolean                                                     /UsageSpecCharacteristicFurtherDefinedBy
                                                         UsageSpecCharUse                                                                                                              UsageSpecCharacteristic
       +       maxCardinality: Integer                                                                                                                                                                                               +   derivationFormula: String
       +       minCardinality: Integer                                                                                                                                                                                               +   description: String
                                                                   1          0..1 0..*                                                                                     1                 1                 1
       +       name: String                                                                                                                                                                                                          +   extensible: Boolean
       +       unique: String                                                                                                                                  /UsageSpecCharSpecifiesUsageCharValue                                 +   ID: String
       +       validFor: TimePeriod                                                                                                                                                                                                  +   maxCardinality: Integer
                                                                                                                                                                                                                                     +   minCardinality: Integer
                               1
                                                                                                                                                     CharacteristicValue                                                             +   name: String
                                                                                                                                                                                                                                     +   unique: String
                                                                                                                                               +   validFor: TimePeriod                                                              +   validFor: TimePeriod
                                                                                                                                               +   value: String                                                                     +   valueType: String
                EntitySpecCharUseEnumeratedBy                                 /UsageSpecCharUseDescribesUsageChaValue                                                                                                                                    1
                                                                                                                                        0..*
                                                                                                                                                                                                  /UsageSpecCharEnumeratedBy
                                                                                                                                  UsageCharacteristicValue                 0..*
                                                                                                            0..*
                                                                                                                                                        0..*                0..*                                                 CharacteristicSpecificationEnumeratedBy

                                                                                                                                                               /UsageSpecCharValueUseInstantiatedAs
                                                                                                                                                                                                                                                         0..*
                                                /UsageSpecCharUseEnumeratedBy
                               0..*                                 0..*                              /UsageCharInstantiatedAsUsageCharacteristicValue                                                                                     CharacteristicSpecValue
                                                                                                                                                                           0..1                                 0..*                 +   isDefault: Boolean
                 EntitySpecCharValueUse                UsageSpecCharValueUse
                                                                                              0..1                                                                                                                                   +   rangeInterval: String
           +    isDefault: Boolean                                                                     /UsageSpecCharValueUseDefinedBy                                      UsageSpecCharacteristicValue                             +   rangeStep: Integer
           +    validFor: TimePeriod                                                                                                                                                                                                 +   unitOfMeasure: String
                                                                                           0..*                                                                     1                                                                +   validFor: TimePeriod
                                                                                                                                                                                                                                     +   value: String
                                                                                                                                                                                                                                     +   valueFrom: String
                                                                                                                                                                                                                                     +   valueTo: String
                                                                                                                                                                                                                                     +   valueType: String




                                                                                                                Figure U.02 - Usage Specification (copy from Common)


© TM Forum 2025. All Rights Reserved                                                                                                                                                                                                 119                                   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure U.04 - Resource and Service Usage (copy from Common)

  A resource usage represents any usage of resources in its broadest meaning, for example a purchase or lease of a product realized by a
  resource. A service usage represents any usage of service in its broadest meaning, for example a purchase of a product
  realized/implemented by a service or a usage of a service that realizes a product. Classes that are used to model resource and service usages
  are subclasses of abstract usage classes as shown in the following Figure, the ResourceUsageSpec is a subclass of the UsageSpecification
  and represents a type of resource usage, while the ServiceUsageSpec represents a type of service usage. A typical source of resource or
  service usage is a mediation application. Other sources may be application servers and other applications (for example, an online shopping
  application) that are aware of the usage format and can generate usage directly without mediation.



  An example of the ServiceUsage class is a voice call that is characterized by:

  An origination and a destination address (Who), typically complete information is available only for ProductUsage

          •        A time of a day the call was connected and a duration of the call (When),
          •        A call type and its details (What),
          •        Connection locations of the call (Where) and
          •        A cause of event recording (Why).




© TM Forum 2025. All Rights Reserved                                                           120              of    177
    Information Framework (SID) Suite Service Domain R25.0.0




    class Figure U.04 - Resource and Service Usage


                          ResourceUsageSpecDescribesUseOf                                                                                                     ServiceSpecUsageDescribesUsageOf
                                                                      ResourceUsageSpecification                     ServiceUsageSpecification
                                                            0..*                                                                                       0..*




                      1
                                                                                                                                                                                                         1
           ResourceSpecification
                                                                                                   UsageSpecification                                                                 ServiceSpecification
                          0..1
                                                                                                              0..1                                                                                1
                                                                                                                 /UsageSpecDescribes
                                                                                                              0..*
                          /SpecifiesResource
                                                                                                         Usage                                                                          /SpecifiesService




                          0..*                                                                                                                                                                    0..*
                                           DescribesUsageOfResource                                                                                DescribesUsageOfService
                  Resource                                                     ResourceUsage                            ServiceUsage                                                         Service
                                     1                                0..*                                                                  0..*                                 1




                                                                        Figure U.04 - Resource and Service Usage (copy from Common)




© TM Forum 2025. All Rights Reserved                                                                                                             121                             of    177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure U.06 - Product Usage, Part 2 (copy from Common)

  As mentioned above, a product is realized as one or more services and/or resources. Consequently, the ProductUsageSpec business entity
  has to be associated with the ResourceUsageSpec and the ServiceUsageSpec business entities. The ProductUsage, the ServiceUsage and
  the ResourceUsage business entities have to reflect these associations as well. The ProductComponentUsage can be associated with either
  ServiceUsage or ResourceUsage and included in a ProductBundleUsage. These entities and associations are shown on the Figure bellow.




© TM Forum 2025. All Rights Reserved                                                     122                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




   class Figure U.06 - Product Usage, Part 2


                                      /UsageSpecDescribes                                    UsageSpecification

                                                                         0..1




                                                ResourceUsageSpecParticipatesInServiceUsageSpec

                  ResourceUsageSpecification                                                    ServiceUsageSpecification
                                                         0..*                      0..*                                                        ProductUsageSpec

                                     0..*                                                                                      0..*                                      1..*
                                                                                                                                                              CompositeProductUsageSpecComprisedOf
                                                                                       ServiceUsageSpecParticipatesIn



                                                                                                                               0..*                                                   0..*

                                     ResourceUsageSpecParticipatesIn                                                        AtomicProductUsageSpec                  CompositeProductUsageSpec

                                                                                                             0..*


                                                                                                Usage

                                                                          0..* +          usageDate: DateTime
                                                                               +          usageStatus: Integer




                                        ResourceUsageGuidedToServiceUsage
            ResourceUsage                                                                      ServiceUsage                                          ProductUsage
                                                                                                                                                                          1..*
                                      0..*                                      0..*
                    0..*                                                                                            0..*                                            ProductBundleUsageComprisedOf
                                                                                         ServiceUsageGuidedTo
                                                                                                                     0..*
                                                                                                                                                                                       0..1
                                             ResourceUsageGuidedToProdCompUsage
                                                                                                                 ProductComponentUsage                                           ProductBundleUsage
                                                                                                   0..*




                                                                                                  Figure U.06 - Product Usage, Part 2 (copy from Common)


© TM Forum 2025. All Rights Reserved                                                                                                                                                  123             of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.7.1 Service Usage Specification ABE

  The Service Usage Specification ABE specifies types and characteristics of usage of ServiceSpecifications.

  Figure SUS.01 - Service Usage Specification ABE Related Entities

  Following are the business entities aggregated under the Service Usage Specification Aggregate Business Entity.

                EntitySpecification
          UsageSpecification




       ServiceUsageSpecification




                                                        Figure SUS.01 - Service Usage Specification ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                           124         of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.7.2 Service Usage Entity ABE

  The Service Usage Entity ABE collects service usage information, and generates ServiceUsage according to ServiceUsageSpecification for use
  by other business entities.

  Figure SUE.01 - Service Usage Entity ABE Related Entities

  Following are the business entities aggregated under the Service Usage Entity Aggregate Business Entity.

               Usage

        «required»
    +     usageDate: DateTime
    +     usageStatus: Integer




           ServiceUsage




                                                               Figure SUE.01 - Service Usage Entity ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                               125     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.8     Service Test ABE
  The Service Test ABE defines measurement including units and values and how the values are determined. It also includes thresholds used
  to evaluate the measure and the consequences of violating the thresholds as well as the Service Test measures that reflect the functioning of
  the Service under test.

  Figure T.04 - Product, Service and Resource Test Entities (Copy from Common)

  The following Figure shows one way to support tests for Product, Services, and Resources by applying the Entity/EntityRole pattern. This
  allows the same “Test Specification” to be used for many “Product TestSpecifications”, “ServiceTestSpecifications”, and “Resource
  TestSpecifications”.

  Product, Service, and Resource Tests are defined to be generalizations of the abstract “Test” class. In this way, the “Test” model may be used
  for the specification of all three types of tests. Each test, such as “ServiceTest” is associated to its relative entity under test, which in this
  case is “Service”. The relationships therefore between products, services, and resources, are maintained to the associated tests. As an
  example, a service test measure such as “Frame Loss Ratio” may translate to resource test measures “Number of frames sent” and “Number
  of frames received”. The metric “Number of Frames Lost” is derived from the resource test measures, and the “Frame Loss Ratio” is further
  calculated by dividing the number of frames lost by the number of frames sent.

  Refer to Common Domain guide book section Test ABE for more details




© TM Forum 2025. All Rights Reserved                                                            126                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                TestMeasure                                                           TestMeasureDefinition

                            0..*                                                                      0..*
                    TestProduces                                                        TestSpecificationTests

                            1                                                                      0..*

                     Test                        TestSpecificationDescribes             TestSpecification              TestSpecificationPlays
                                                                                                                                                  TestSpecificationRole
    +   adminState: AdministrativeState 0..*                                    1 +    description: String
    +   description: String                                                                                           1                    0..*
                                                                                  +    name: String
    +   mode: TestMode                                                            +    validFor: TimePeriod
    +   name: String
    +   state: TestState




                                                                                                                   ResourceTestSpec                   ServiceTestSpec                 ProductTestSpec


                                                                                                                              0..*                                  0..*                           0..*
        ProductTest                       ResourceTest
                                                                                                                 ResourceSpecTestedVia                ServiceSpecTestedVia         ProductSpecTestedVia
             0..*                                 0..*
                                                                                                                              1                                 1                                  1

                     ServiceTest                                                                                 ResourceSpecification            ServiceSpecification             ProductSpecification

                                   0..*                                                                                       0..1                               1                                 1

                                                                                                                    /SpecifiesResource                  /SpecifiesService         /ProductSpecificationDescribes

                                                                                                                              0..*                               0..*                              0..*

                                                         ResourceTestExecutesOn
                                                                                                                       Resource                            Service                         Product
                                                                                                             1
                                                                                                                                                  1                                            1
                                                                              ServiceTestExecutesOn


                                                                                            ProductTestExecutesOn




                                                                     Figure T.04 - Product, Service and Resource Test Entities (Copy from Common)




© TM Forum 2025. All Rights Reserved                                                                                                                                        127                           of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.9     Service Performance ABE
  The Service Performance ABE collects information used to correlate, consolidate, and validate various performance statistics and other
  operational characteristics of Know-Hows (a.k.a. CFS) and Technical Solutions (a.k.a. RFS). It provides a set of entities that enables
  performance monitoring and reporting. Each of these entities also enables network performance assessment against planned goals,
  performs various aspects of trend analysis, including error rate and cause analysis and Service degradation.

  Entities in this ABE also enable the traffic trend analysis.

  Figure SO.37 - Service Level Specification Overview

  It should be noted that this section is still a work in progress, and is subject to change.

  A business participant, such as a Customer (or other type of PartyRole), often expects a certain level of Service to be associated with a
  Product or Service procured from another business participant, such as a Service Provider or some other Enterprise. Such expectations are
  defined by a Service Level Specification, which is associated to a Product, Service or their respective Specifications. Sometimes referred to
  as a Service Level Agreement Template, a Service Level Specification represents a pre-defined or negotiated set of Service Level Objectives.
  In addition, certain consequences are associated with not meeting the Service Level Objectives. Service Level Agreements are expressed in
  terms of Service Level Specifications.

  This figure shows a simple, un-attributed view of a Service Level Specification. Note: the two subclasses of ServiceLevelSpecification are
  shown merely to emphasize the two different types of specifications.




© TM Forum 2025. All Rights Reserved                                                            128              of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                   ServiceLevelSpecIntendsToMeet                                                        ServiceLevelObjectiveUnmetResultIn
                                                                                ServiceLevelObjective
                                                               0..*                                                  0..*




                                                                                                                                                             0..*
                                      1

                                                                           ServiceLevelSpecsUnmetObjectiveResultIn
                              ServiceLevelSpecification                                                                            ServiceLevelSpecConsequence
                                                                    1                                                0..*




        TemplateServiceLevelSpec                                   NegotiatedServiceLevelSpec




                                                                          Figure SO.37 - Service Level Specification Overview




© TM Forum 2025. All Rights Reserved                                                                                                         129                    of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.38 - Products, Services, and ServiceLevelAgreements

  Examples of products and services, along with two different associated SLAs, are depicted in the diagram below. The diagram is a modified
  extract from the Service Level Agreement Handbook (GB917).

          •        Note: the above uses terminology from GB917. An Internal SLA is also known as a Service Provider SLA.




                                                         Figure SO.38 - Products, Services, and ServiceLevelAgreements




© TM Forum 2025. All Rights Reserved                                                                          130          of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.39 - Associating Service Level Specifications with Products and Services

  Customer Service Level Agreements are expressed in terms that a Customer can understand. These Service Level Agreements are defined in
  terms of Service Level Specifications related to ProductOfferings and ProductSpecifications. ProductSpecifications are used in order to
  define a set of characteristics that the set of Service Level Specification will cover.

  Internal Service Level Agreements are usually defined in terms of resource-facing Service Level Specifications, which are typically too
  technical to be of interest to a customer. Supplier/partner Service Level Agreements can be expressed in terms of either customer-facing or
  resource-facing Service Level Specifications. The Figure below shows a Service Level Specification’s relationships to Products, Services, and
  their associated Specifications.

                                                                                ServiceSpecification

                                                                                            0..*

                                                                            ServiceSpecQualityMeasuredBy



                                                                                             0..*
                                     ProductOfferQualityMeasuredBy

      ProductOfferingSpecification                                           ServiceLevelSpecification
                                        0..*                 0..*
                      *                                                                      0..*


                                                                             ProdSpecQualityMeasuredBy
        /ProdSpecMadeAvailableAs


                                                                                            0..*

                                                                               ProductSpecification
                                                                     1..*



                                                    Figure SO.39 - Associating Service Level Specifications with Products and Services



© TM Forum 2025. All Rights Reserved                                                                                131                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.40 - Service Level Specification Parameters and Objectives

  Service level objectives are defined in terms of parameters and metrics, thresholds, and tolerances associated with the parameters. The
  Figure below depicts Service Level Objectives, along with the Parameters that define them.

  Service Level Specification parameters can be one of two types. A Key Quality Indicator (KQI) provides a measurement of a specific aspect of
  the performance of a Product (i.e., ProductSpecification, ProductOffering, or Product) or a Service (i.e., ServiceSpecification or Service). A
  KQI draws its data from a number of sources, including Key Performance Indicators (KPIs). A KPI provides a measurement of a specific
  aspect of the performance of a Service (whether it is a network- or a non-network-based Service) or a group of Services of the same type. A
  KPI is restricted to a specific resource type. The figure below extends Figure SO.40 by showing how KPIs and KQIs are related to products and
  services.

           ServiceLevelObjective

    +   conformanceComparator: String
    +   conformancePeriod: TimePeriod                                                      ServiceLevelSpecParameter
    +   conformanceTarget                      ServiceLevelObjectiveExpressedUsing
    +   gracePeriods: Integer                                                          +   category: String
    +   thresholdTarget                 0..*                                         1 +   perspective: String
    +   tolerancePeriod: TimePeriod                                                    +   validFor: TimePeriod
    +   toleranceTarget
    +   validFor: TimePeriod




                                                    KeyPerformanceIndicatorSLSParm                                     KeyQualityIndicatorSLSParm

                                                                                                              +   transformationAlgorithm: String




                                                         Figure SO.40 - Service Level Specification Parameters and Objectives




© TM Forum 2025. All Rights Reserved                                                                                            132                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.41 - KPIs, KQIs, Products, and Services




                                                               Figure SO.41 - KPIs, KQIs, Products, and Services




© TM Forum 2025. All Rights Reserved                                                                           133   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.42 - ServiceLevelSpecConsequences

  Customer-facing Product KQIs, such as the number of trouble tickets opened for a Product, characterize Customer Service Level
  Agreements. Service KQIs, such as the maximum web server unavailability time that is permitted, represent an aggregation of Service KPIs or
  a simple one-to-one mapping to a Service KPI, and characterize internal and engaged party Service Level Agreements. Atomic Service KPIs,
  such as the maximum IP packet loss ratio, do not characterize Service Level Agreements, but form the basis for the determination of KQIs.
  Please see the SLA Management Handbook (GB917) for additional examples and the Wireless Services Measurement Handbook (GB923) for
  more details about KPIs and KQIs.

  Violations to Service Level Agreements usually result in some consequence for the provider of the Service. The consequence could be a
  general one that applies to any objective violation, or the consequence could be associated with a specific objective. An example of a
  consequence is a discount applied to a customer’s bill if the number of trouble tickets for a Product exceeds some number over a specified
  period of time. The figure below shows how consequences of violating a Service Level Agreement fit into the Service Level Specification
  model.

  No attempt was made to build a detailed model that represents the prescribed actions. Rather, the above model is intended to be an
  extensible framework that enables each adopter of the model to customize their extensions for this business entity.




© TM Forum 2025. All Rights Reserved                                                        134                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                 ServiceLevelSpecsUnmetObjectiveResultIn                     ServiceLevelSpecConsequence

                                                                           0..*   +   prescribedAction: String
                                                                                  +   validFor: TimePeriod

                                                                                                                  0..*
                       1
                                                                                                ServiceLevelObjectiveUnmetResultIn
         ServiceLevelSpecification


                       1                                                                                           0..*

                                          ServiceLevelSpecIntendsToMeet                              ServiceLevelObjective

                                                                                      0..*



                                                                            Figure SO.42 - ServiceLevelSpecConsequences




© TM Forum 2025. All Rights Reserved                                                                                                 135   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.43 - ServiceLevelSpecApplicability

  The applicability of Service Level Specifications, Service Level Objectives, and Service Level Specification consequences may vary by day
  and/or time of day. For example, a Service Level Objective may be represented by one set of metrics during weekdays and by another set
  during weekends. Thus, we may need to define a set of consequences to associate the proper effect of violating a Service Level Objective. For
  example, one consequence might be the result of a Service Level Violation during normal working hours, while a second consequence might
  be used to represent Service Level Violations that occur during non-working hours. This is handled by introducing a Service Level
  Specification applicability business entity as shown in the figure below.
                   ServiceLevelObjective                                    ServiceLevelObjectiveUnmetResultIn

          +    conformanceComparator: String   0..*
          +    conformancePeriod: TimePeriod
          +    conformanceTarget                ServiceLevelSpecIntendsToMeet
          +    gracePeriods: Integer
          +    thresholdTarget                                             1            ServiceLevelSpecification
                                                0..*
          +    tolerancePeriod: TimePeriod
          +    toleranceTarget                                                 +    validFor: TimePeriod
          +    validFor: TimePeriod
                                                                                           1                      1
                             0..*


                                                        ServiceLevelSpecIpactedBy

           ServiceLevelObjectiveImpactedBy
                                                                                        ServiceLevelSpecsUnmetObjectiveResultIn




                             0..*              0..*
                                                                                                                                  0..*   0..*
              ServiceLevelSpecApplicability     ServiceLevelSpecConsequenceImpactedBy
                                                                                                           ServiceLevelSpecConsequence
      +   unappAppDays: String
                                                                                                 +   prescribedAction: String
      +   unappAppDuration: TimePeriod           0..*                                     0..*
                                                                                                 +   validFor: TimePeriod
      +   unapplicableApplicableCode: String




                                                                                       Figure SO.43 - ServiceLevelSpecApplicability



© TM Forum 2025. All Rights Reserved                                                                                                            136   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.43a - ServiceLevelSpecificationExpression

  The ServiceLevelSpecExpression entity is intended to describe strict relations between ServiceLevelSpecification subordinates
  (ServiceLevelSpecParameter, ServiceLevelObjective, ServiceLevelSpecApplicability, and ServiceLevelSpecConsequence). The baseline idea
  of ServiceLevelSpecExpression entity resolves the multiple associations among ServiceLevelSpecification subordinate entities. So in this
  case it is possible to have variety of ServiceLevelSpecification subordinates combined using ServiceLevelSpecExpression.

  When it is needed to calculate Time-To-Resolve of a customer’s` issue and the system must notify different departments upon reaching
  different Time-To-Resolve values.

  In this case first ServiceLevelObjective_A with thresholdTarget = 15 min and conformanceTarget = 45 min will be created and associated with
  ServiceLevelSpecConsequence_A (this consequence will raise notification action: Send letter to the user about existed issue when threshold
  target was reached and apologies letter when conformance target was reached).

  On the other hand second ServiceLevelObjective_B with thresholdTarget = 5 min and conformanceTarget = 30 will be created and associated
  with SevericeLevelSpecConsequence_B (this consequence will raise notification action: Send letter to the engineer about existed issue when
  threshold target was reached and escalation letter to the management when conformance target was reached)

  So in this case it is crucial to understand which ServiceLevelObjective is related to which consequence and this could be done with in
  Expression in following way:

          •        Create ServiceLevelSpecExpression_A
          •        where

    - serviceLevelSpecApplicability = Applicability_A

    - serviceLevelSpecConsequence = Consequence_A

    - serviceLevelSpecParameter = Parameter_A


© TM Forum 2025. All Rights Reserved                                                         137                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




    - serviceLevelObjective = SeviceLevelObjective_A

          •        and

    - create second ServiceLevelSpecExpression_B were

    - serviceLevelSpecApplicability = Applicability_A

    - serviceLevelSpecConsequence = Consequence_B

    - serviceLevelSpecParameter = Parameter_A

    - serviceLevelObjective = ServiceLevelObjective_B

  This section has defined a ServiceLevelSpecification, and its associated related objects, to be compatible with the SLA Handbook and the
  work done by the WSMT. The next version of this Addendum will seek to align this work with other industry work.




© TM Forum 2025. All Rights Reserved                                                        138                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




        ServiceLevelSpecsUnmetObjectiveResultIn                                                      ServiceLevelSpecification
                                                                                                                                        1
                                                                                          1 +        validFor: TimePeriod

                                                                                                        1                       1       1
                                                                                                                                                                       ServiceLevelSpecificationDefinedBy

                                                                                                                                                                                          0..*
                                                                                      ServiceLevelSpecIntendsToMeet
                                                  ServiceLevelObjective                                                                                                        ServiceLevelSpecParameter
                                 0..*                                              0..*                         ServiceLevelSpecificationUses
                                                             0..*         0..1                                                                                                                    0..1



                                                                                                                                                                           ServiceLevelSpecParameterPlaysRoleIn
                                                             ServiceLevelObjectivePlaysRoleIn
                                                                                                                                0..*
               ServiceLevelObjectiveUnmetResultIn
                                                                                                            ServiceLevelSpecExpression          0..*
                                                                                                 +     serviceLevelObjective: Boolean                                                                    ServiceLevelSpecIpactedBy
                                                                                                 +     serviceLevelSpecApplicability: Boolean
                                                                                                 +     serviceLevelSpecConsequence: Boolean
                                                                                                 +     serviceLevelSpecParameter: Boolean
                                                                                                 +     validFor: TimePeriod
                                                                                          0..*                                                  0..*
                                                                                                                            0..*
                                                                                                     ServiceLevelSpecConsequencePlaysRoleIn                           ServiceLevelSpecApplicabilityPlaysRoleIn
             0..*             0..*

            ServiceLevelSpecConsequence
                                                                                                                                                                                       0..1
                                                      0..1
                                                                                                                                                                                                                 0..*
                                                                                                 ServiceLevelObjectiveImpactedBy
                                                                                                                                                                    ServiceLevelSpecApplicability
                                                                                                                                                             0..*



                                                                                 Figure SO.43a - ServiceLevelSpecificationExpression




© TM Forum 2025. All Rights Reserved                                                                                                                   139                        of     177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.9.1 Service Level Spec ABE

  The Service Specification ABE contains entities that define the invariant characteristics and behavior of both types of Service entities. This
  enables multiple instances to be derived from a single specification entity. In this derivation, each instance will use the invariant
  characteristics and behavior defined in its associated template.

  This ABE includes a third type of Service Specification entity: that of a ServiceLevelSpecification. This type of specification templatizes
  Services that are bound to a Service Level Agreement.

  Figure SLS.01 - Service Level Spec ABE Related Entities

  Following are the business entities aggregated under the Service Level Spec ABE.




© TM Forum 2025. All Rights Reserved                                                            140                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                      ServiceLevelSpecApplicabilityPlaysRoleIn


                                                                                                                                                              ServiceLevelSpecConsequencePlaysRoleIn



                                                                                                                                                                           ServiceLevelObjective
                                                                                         0..1                                                                                                                         ServiceLevelObjectivePlaysRoleIn
                                                                                                                                                                 +       conformancePeriod: TimePeriod
                                                                                                                      ServiceLevelObjectiveUnmetResultIn         +       gracePeriods: Integer         0..1
                                                                      ServiceLevelSpecConsequence                                                                                                                                                                                           0..*
              ServiceLevelSpecConsequenceImpactedBy                                                                                                              +       thresholdTarget                                                                          0..*        0..*
                                                                                                                        0..*                                0..* +       tolerancePeriod: TimePeriod
                                                               +     validFor: TimePeriod
                                                        0..*                                                                                                     +       toleranceTarget                                                                       ServiceLevelSpecExpression
                                                                   «required»
                                                                                                                                                                 +       validFor: TimePeriod
                                                               +     prescribedAction: String                         ServiceLevelObjectiveImpactedBy
                                                                                                                                                                       «required»                                                                 +       validFor: TimePeriod
                                                                                                               0..*                                                +     conformanceComparator: String                                                «required»
                                                                                                                                                                   +     conformanceTarget                                                0..*    +     serviceLevelObjective: Boolean
                                                                                                                                                                                                                                                  +     serviceLevelSpecApplicability: Boolean
                                                                                                                                                            0..*                          0..*         0..*
                                                                           ServiceLevelSpecsUnmetObjectiveResultIn                                                                                                                                +     serviceLevelSpecConsequence: Boolean
                                                                                                                                                                                                                                                  +     serviceLevelSpecParameter: Boolean
                                                                                                                                           ServiceLevelSpecIntendsToMeet
                                                                                                                                                                                                                                                                    0..*
            0..1            0..*            0..*
                                                                                                                                                                                                                                                        ServiceLevelSpecParameterPlaysRoleIn
                                                                                                    1                           1                                                       ServiceLevelObjectiveExpressedUsing                                         0..1
            ServiceLevelSpecApplicability

      +     unappAppDays: String                                                                            ServiceLevelSpecification                              ServiceLevelSpecificationUses                                                      1          ServiceLevelSpecParameter
      +     unappAppDuration: TimePeriod              ServiceLevelSpecIpactedBy
                                                                                                        +   validFor: TimePeriod           1                                                                                                               +     category: String
          «required»                           0..*                                             1
                                                                                                                                                                                ServiceLevelSpecificationDefinedBy                                         +     validFor: TimePeriod
      +     unapplicableApplicableCode: String
                                                                                                                                                                                                                                                               «required»
                                                                                                                                           1                                                                                                     0..*      +     perspective: String




                                                                     TemplateServiceLevelSpec                                  NegotiatedServiceLevelSpec

                                                                                                                                                                                                   KeyQualityIndicatorSLSParm                             KeyPerformanceIndicatorSLSParm

                                                                                                                                                                                           +     transformationAlgorithm: String




                                                                                                    Figure SLS.01 - Service Level Spec ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                                                                                                             141                                 of          177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.9.2 Service Performance Specification ABE

  The Service Performance Specification ABE defines measure of the manner in which a Service is functioning.

  Figure SPS.01 - Service Performance Specification ABE Related Entities

  Following are the business entities aggregated under the Service Performance Specification ABE.




             PerformanceSpecification

    +     description: String
    +     validFor: TimePeriod
        «required»
    +     ID: String
    +     name: String




             ServicePerformanceSpec




                                                     Figure SPS.01 - Service Performance Specification ABE Related Entities



© TM Forum 2025. All Rights Reserved                                                                           142            of   177
    Information Framework (SID) Suite Service Domain R25.0.0




© TM Forum 2025. All Rights Reserved                           143   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.10 Service Capacity ABE
  The Service Capacity ABE specifies ability of Service to provide capability measured in quantity and units of quantity over an extended
  period. It also manages the Service Capacity Demands.

  Figure SC.01 - Basic Capacity Entities (based on CM.02 from Capacity ABE in Common Domain)

  A generalized capacity and capacity demand model is shown in the following Figure.

  The need to satisfy the capacity requirement during the first week in June is expressed using the fromToDateTime attribute, which is a
  composite of from and to dates/times, and the rangeInterval attribute of ApplicableTimePeriod. Refinements to the schedule can include
  days of the week as shown by the daysOfWeek attribute in the ApplicableTimePeriod entity. The rangeInterval attribute is used to handle
  some combination of >, <, >=, <=. It is assumed this is a planned Capacity, which would be indicated using the plannedOrActutalCapacity
  attribute. The CapacityRelationship entity enables a planned Capacity to be associated with an actual Capacity or for Capacities to be
  aggregated.

  The requirement for this capacity to be available in the Northeast geographic area is expressed using the relationship to GeographicPlace.
  Other entities that further define/refine capacity requirements could be added as needed by extending the SID.

  The ability to deliver 10000 units of Product described in the previous example is expressed via the CapacityAmount, whose datatype is
  Quantity. Quantity is a composite of an amount attribute and a units (unit of measure) attribute. For this instance of Capacity, the
  capacityAmount attribute contains the amount “10000”, and the unit of measure “units”. Other examples of units of measure could be
  transaction volumes, storage requirements, traffic volumes, port availabilities, and so forth. The capacityAmountFrom, capacityAmountTo,
  and rangeInterval enable ranges of capacity to be specified.




© TM Forum 2025. All Rights Reserved                                                         144                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Demands are placed on the capacity as defined by the CapacityDemand entity. The related ApplicableTimePeriod is used to here to express
  the timeframe over which the demand exists. It may or may not be the same instance of the ApplicableTimePeriod associated with the
  Capacity. Therefore, it may be a demand placed on more than one CapacityAmount. Similarly, the CapacityAmount may have many
  demands placed against it.

  The attributes are similar to those in CapacityAmount with the addition of a priority attribute that defines the relative importance of this
  demand.

  The AppliedCapacityDemand entity represents the amount of the CapacityDemand that has been applied against a CapacityAmount.




© TM Forum 2025. All Rights Reserved                                                            145                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                    ApplicableTimePeriod             CapacityDemandDefinedFor                                    0..*
                                                                +   daysOfWeek: String
                                                                +   fromToDateTime: TimePeriod                                                 CapacityDemand
                                                                +   rangeInterval: String           0..1              0..*     +    capacityDemandAmount: Quantity            0..*
                                                                +   validFor: TimePeriod
                                                                                                                               +    capacityDemandAmountFrom: Quantity
                                                                                                                               +    capacityDemandAmountTo: Quantity
                                                                                  0..1                                         +    capacityDemandType: String
                                                                                                                               +    priority: String                                       CapacityDemandRelationship
                                                 CapacityAvailableDuring                                                       +    rangeInterval: String
                                                                                                                                                                                       +   capDemandRelType: String
                                                                                  0..*                                                                                                 +   validFor: TimePeriod
                                                                                                                                                 1
                                 CapacityAppliesTo                                                                                 CapacityDemandDistributedAs
       GeographicPlace                                                       Capacity
                         0..*                        0..*
                                                            +   plannedOrActualCapacity: String

                                                       0..*           0..*                      1                                                0..*

                                                                                                                                    AppliedCapacityDemand

                                                                                                                       +      appliedDemandAmount: CapacityAmount

                                CapacityRelationship                                                                                             0..*

                         +   capRelType: String
                         +   validFor: TimePeriod                                                                                      CapacityAmountReducedBy

                                                                     {isSubstitutable=false}
                                                                                                                                                 1

                                                                                                                                            CapacityAmount
                                                                                               AvailableCapacityExpressedAs        +   capacityAmount: Quantity
                                                                                                                                   +   capacityAmountFrom: Quantity
                                                                                                                              0..* +   capacityAmountTo: Quantity
                                                                                                                                   +   rangeInterval: String



                                                                    ServiceCapacity                                                                                     ServiceCapacityDemand




                                              Figure SC.01 - Basic Capacity Entities (based on CM.02 from Capacity ABE in Common Domain)




© TM Forum 2025. All Rights Reserved                                                                                                                    146                       of       177
    Information Framework (SID) Suite Service Domain R25.0.0




© TM Forum 2025. All Rights Reserved                           147   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SC.02 - Basic Service Capacity Entities (CM.06 Copy from Capacity ABE in Common Domain)

  The following Figure shows ServiceCapacity specific relationships.

    class Figure CM.06 - Basic Service Capacity Entities



                                                           Capacity

                                          +      plannedOrActualCapacity: String




                                                      ServiceCapacity
                                          0..*                               0..*
      ServiceSpecCapacityDefinedAs                                                  ServiceCapacityDefinedAs


                        0..1                                                                     0..1

            ServiceSpecification                                                           Service




                                                    Figure SC.02 - Basic Service Capacity Entities (CM.06 Copy from Capacity ABE in Common Domain)




© TM Forum 2025. All Rights Reserved                                                                                     148                   of    177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SC.03 - Basic Service Demand Entities (CM.09 Copy from Capacity ABE in Common Domain)

  The following Figure shows ServiceCapacityDemand and its specific relationships.

    class Figure CM.09 - Basic Service Demand Entities


                                                           CapacityDemand




                                                         ServiceCapacityDemand
                                              0..*                               0..*
            ServiceSpecRequires                                                            ServiceRequires

                        0..1                                                                        0..1

           ServiceSpecification                                                              Service




                                                     Figure SC.03 - Basic Service Demand Entities (CM.09 Copy from Capacity ABE in Common Domain)




© TM Forum 2025. All Rights Reserved                                                                                     149                  of    177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.11 Service Problem ABE «NotFullyDeveloped»
  The Service Problem ABE manages faults, alarms, and outages from a Service point-of-view. This is then correlated to trouble tickets,
  regardless of whether the cause is physical or logical.



  Other entities in this ABE are used to direct the recovery from each of these types of problems. They provide the ability to associate Resource
  faults and alarms to degradation and outages of Services that run on those Resources.

  Figure SP.01 - Service Problem ABE Related Entities

  Following are the business entities aggregated under the Service Problem ABE.




© TM Forum 2025. All Rights Reserved                                                          150                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                           Problem

    +     activityStatus: ActivityStatusEnum {readOnly}
    +     clearStatus: ClearStatus {readOnly}
    +     impactImportanceFactor: Integer
    +     originatingSytem: String [0..1]
    +     problemEscalation: Integer [0..1]
    +     reason: String
    +     responsibleParty: String [0..1]
    +     timeRaised: DateTime {readOnly}
        «required»
    +     ackStatus: AckStatus {readOnly}
    +     category: String
    +     comments: String [0..*] {readOnly}
    +     description: String
    +     firstAlert: String [0..1]
    +     impactPattterns: ImpactPatterns [0..1]
    +     priority: Integer = 1
    +     problemId: String
    +     timeChanged: DateTime {readOnly}




                       ServiceProblem

                «required»
            +     affectedServiceNumber: Integer




                                                               Figure SP.01 - Service Problem ABE Related Entities




© TM Forum 2025. All Rights Reserved                                                                            151   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  4.12 Service Strategy & Plan ABE «notFullyDeveloped»
  The Service Strategy and Plan ABE contains entities that are used to address the need for enhanced or new Services, as well as the
  retirement of existing Services, by the enterprise. These entities have a strong dependency to both entities in the Resource and Product
  domains. Resulting efforts, such as deciding what Resources to use to host a Service, or what Services are used to support new Product
  Specifications, are also supported, as are service demand forecasts.

  4.13 TIP Service Management ABE «likelyToBeDepreciated»
  This ABE is likely to be removed in Release 25.5



  The TMF Interface Program introduced in the Multi-Technology Operations System Interface (MTOSI) 2.0, Service Management interfaces
  based upon extensions to the SID service model in this ABE. The resulting solution set introduced two new service management activation
  interfaces, and a service inventory interface.

          Introduction

          •        Note: TMF Interface Program (aka TIP) is legacy stuff to define interfaces and interfaces are now defined by the Open API Program.



  The TMF Interface Program (aka TIP) introduced in the Multi-Technology Operations System Interface (MTOSI) 2.0, Service Management
  interfaces based upon extensions to the SID service model. The resulting solution set introduced two new service management activation
  interfaces, and a service inventory interface:



© TM Forum 2025. All Rights Reserved                                                                       152                   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




          •        The Service Activation interface (SAI) between the Customer Relationship Management (CRM) and Service Management and Operations (SM&O)
          layers allows for the activation of Customer Facings Services (CFS)
          •        Interactive Service Activation
          •        Best-effort Transaction interface         Service requests entailing multi-task transaction execution. In this type of interface, the entire transaction
          execution is completed despite single task failures.
          •        Atomic Transaction interface This interface has the same operations as the previous one; however, the failure of any single task will incur the
          termination of the transaction execution and will invoke a roll-back of the preceding task.
          •        Service Order Management interface Add-on interface to both the Best-effort Transaction or Atomic Transaction interfaces. Provides full
          exposure and control of the service order associated with the service request over the interface. It depends on the functions provided by the previous
          interfaces.
          •        The Service Component Activation interface (SCAI) is an internal SM&O layer interface. It allows for the activation of Service Components, also
          known as Resource Facing Services (RFSs), given specific service related information defined in a Service Template. The SCAI, contrary to the SAI, has no
          knowledge of the product domain.
          •        The Service Inventory interface supports the retrieval of service related entities from a Service Inventory repository.

  The TIP Service Management ABE provides the extensions made to the SID model in support of the new Service Management interfaces
  introduced. The basic service and service specification concepts as defined in this addendum remain unchanged, and are merely enhanced
  to support the TIP Service Management interfaces.

  Figure SO.31 TIP Service Management - Service Definition and Service Template

  The abstract class ServiceSpecification has been extended to support two new concepts introduced in the TIP Service Management
  interfaces:

  ServiceDefinition




© TM Forum 2025. All Rights Reserved                                                                          153                     of   177
    Information Framework (SID) Suite Service Domain R25.0.0




     • used during service design time to define the characteristics of a service, their associated data types, and default values. These
  characteristics, known as ServiceSpecCharacteristics (SSC), may be globally set, which implies they can be defined in a service template, or
  otherwise only passed in real-time over an activation interface



  ServiceTemplate

      • defines specific ServiceSpecCharacteristicsValues (SSCVs) for the SSCs that were defined in the Service Definition as being globally
  settable. The Service Template is checked against its associated Service Definition by verifying the presence of the SSCs and the validity of
  the corresponding assigned SSCVs. Only Service Templates that contain SSCs/SSCVs that are in conformance with their specification in the
  Service Definition are considered valid.



  Both Service Activation interfaces make use of the Service Definition and Service Template concepts in the activation of
  CustomerFacingServices and ResourceFacingServices.

  The ServiceDefinition and ServiceTemplate further define the Service Specification through their respective associations, with the versions
  being identified through the ServiceSpecVersion. The association class ServiceSpecRelationship allows for Service Specifications to contain
  other Service Specifications, which thus holds true for Service Definitions and Service Templates. For example, there may be a type of
  Service Definition for Ethernet Services, and contained within that type are E-LINE, E-LAN, and E-TREE Service Definitions.

  The ServiceAccessPoint (SAP) represents a unique (logical and/or physical) resource where the Service can be accessed. The Sap
  Specification defines a set of attributes and associated values that may be applied to one or more SAPs. The relationship between the Service
  Specification and the Sap Specification illustrates that for every Service Specification, there may be associated multiple Sap Specifications.
  For example, given an Ethernet E-LINE Service Specification, there may be multiple Sap Specifications that correspond to various Bandwidth
  Profile Specifications that can be applied to the Sap – one for GOLD, one for SILVER, and one for BRONZE. Likewise, there may be a single Sap


© TM Forum 2025. All Rights Reserved                                                          154                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Specification , or in this case Bandwidth Profile Specification, that is used for multiple Ethernet Service Specifications – E-LINE and E-LAN. A
  Bandwidth Profile Specification defines Service Level Agreement guarantees and may be applied per UNI, per EVC, or per CoS Id. They
  contain frame delivery per Service Level Objectives (Committed Information Rate, Committed Burst Size), and amount of excess frame
  delivery allowed (Excess Information Rate, Excess Burst Size).

  A ServiceCatalog represents a grouping of Service Specifications and SSCs. For example, a catalog could group all internet related Service
  Specifications. The following figure illustrates the Service Definition, and Service Template concepts, and the relationship between the
  Service Catalog and the Service Specification.




© TM Forum 2025. All Rights Reserved                                                           155                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                  ServiceSpecVersion                          ServiceSpecificationType                                                      ServiceCatalog

            +    format: String
            +    number: String                                                         0..*                                                           0..*
            +    reason: String
            +    semantics: String                                                                                                                                      ServCatalogServCandidate
            +    timestamp: DateTime
            +    validFor: TimePeriod                                                                                                                             +     validFor: TimePeriod

                             0..*
                                                                                                                                                       0..*

                                                                                                                                          ServiceCandidate
                                                                    ServiceSpecificationTypeCategorizes
                                                                                                                                 +     description: String
                                                                                                                                 +     ID: String
                                                                                                                                 +     name: String
                                                                                                                            0..*
                                                                                                                                 +     status: String
                                                                                                                                 +     validFor: TimePeriod

                                     ServSpecModifications                                ServiceSpecificationMadeAvailableAs




                                                                         1
                   Service                                                              0..*                  0..1

       +   hasStarted: Boolean                                               ServiceSpecification
                                          /SpecifiesService
       +   isMandatory: Boolean
       +   isServiceEnabled: Boolean 0..*                     1                                               1..1
                                                                                                                                     ServiceSpecificationReferencedBy
       +   isStateful: Boolean                                        1..1              1..1        1..1
       +   startMode: Integer
                                                                                                                                                       0..*

                                                                                           ServiceSpecificationReferences               ServiceSpecRelationship

                                                                                                                                 +     type: String
                              ServiceSpecFurtherDefinedByServiceDefinition                                                  0..* +     validFor: TimePeriod




                                                                              ServiceSpecFurtherDefinedByServiceTemplate




                ServiceDefinition            0..1                                                                                              ServiceTemplate
                                                                                                                       0..1
   +   activationMode: String                                          ServiceDefinitionValidates                             +      serviceLocation: String
   +   sdStatus: String                                                                                                       +      source: String
                                                1..1                                                                 0..*     +      stStatus: String




© TM Forum 2025. All Rights Reserved                                                                                                                                           156                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                Figure SO.31 TIP Service Management - Service Definition and Service Template

  Figure SO.32 TIP Service Management - Service Characteristics

  The ServiceSpecCharacteristic and the associated ServiceSpecCharacteristicValues pairs are used in both the Service Definition and the
  Service Template to describe, or characterize, a Service. The CharacteristicSpecification and the CharacteristicSpecValues pairs are used to
  characterize the Service Access Point through the association of the SapSpecification with the EntitySpecCharUse. These provide the actual
  characteristic / values pairs that would be found, for example, in a Bandwidth Profile Specification for an Ethernet Service User Network
  Interface (UNI) or Ethernet Virtual Connection (EVC) endpoint. The Bandwidth Profile Specification would contain the following
  characteristics: committed information rate (CIR), committed burst size (CBS), excess information rate (EIR), excess burst size (size), and
  possibly color marking (CM) and color forwarding (CF) indicators. By defining this specification, including the associated characteristic
  values, as an independent entity, the specification could be associated to a Sap or an EVC.




© TM Forum 2025. All Rights Reserved                                                                         157                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                    EntitySpecification                                                                                                      ServiceSpecification

                      0..1                                                                                                                                 1
                                                                                                 SapSpecification

                                                                                   +     applicableStateValues: String
                                                                                   +     type: String                                     /ServiceSpecFurtherDefinedBy
                                                                                                              0..1
                                                                                       SapSpecDescribedBy

                                    EntitySpecFurtherDefinedBy                                                0..*
                                                                                                                                                           0..*
                                                                                                EntitySpecCharUse
                                                                                0..*
                                                                                                                                              ServiceSpecCharUse

                                           CharacteristicSpecFurtherDefinedBy
                                                                                                                                                            0..*
                                                                                0..*
                                                                                                                                   /ServiceSpecCharacteristicFurtherDefinedBy
                                                                                                             1
                                                       1
                                                                                                                                                            1

                CharacteristicSpecification                                                                                                ServiceSpecCharacteristic

                                1                           EntitySpecCharUseEnumeratedBy                                                                   1


                                                                                                                         /ServiceSpecCharEnumeratedBy
           CharacteristicSpecificationEnumeratedBy
                                                                                                                                                            0..*
                                                                                                             0..*
                                                                                                                                       ServiceSpecCharacteristicValue
                                                                                             EntitySpecCharValueUse


                                                                                                              0..*
                                    0..*                1          EntitySpecCharValueUseDefinedBy
                  CharacteristicSpecValue




                                                                          Figure SO.32 TIP Service Management - Service Characteristics



© TM Forum 2025. All Rights Reserved                                                                                                               158                          of   177
    Information Framework (SID) Suite Service Domain R25.0.0




© TM Forum 2025. All Rights Reserved                           159   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.33 TIP Service Management - Service Activation

  The service configuration and activation process involves the instantiation of both Customer Facing Services, and associated Resource
  Facing Services. The CFS and RFS are constructed based upon their respective Service Definitions, ServiceTemplates, and real-time
  ServiceCharacteristicValues passed over the activation interface. The interface context will determine whether the Service Template being
  referenced is for a CFS (SAI) or an RFS (SCAI).

  The CFS and RFS are accessed via one or more ServiceAccessPoints (SAPs) that are characterized by SapSpecifications. There is a
  relationship between the SAPs and the underlying Resources serving as access points. The following diagram illustrates the classes and
  relationships as required for Service Activation.




© TM Forum 2025. All Rights Reserved                                                        160                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                                                                  OwnsServiceDetails



                                                          Service

                                     +   hasStarted: Boolean                                                                         PartyRole
                                     +   isMandatory: Boolean
                                     +   isServiceEnabled: Boolean                       0..*                            1 +      status: String
                                     +   isStateful: Boolean                                                               +      validFor: TimePeriod
                                     +   startMode: Integer
                                                                                                                                                                            CharacteristicValueReferences
                                                   1..1              0..*
                                                                                                                                                                                  0..*

                                                                                                                                                           CharacteristicValue
                                  ServiceDescribedBy
                                                                                                                                                   +     validFor: TimePeriod
                                                                                                                                                                                          0..1
                                                                                                                                                   +     value: String

        ServiceCharacteristicValue        0..*                               ServiceAccessedVia                                                        1..*

                        0..*                                                                             0..*                CharacteristicValueAppliesToSAP


         /ServiceSpecCharDescribes                                                      ServiceAccessPoint            1..1                                                        Resource
                                                                                                                                    ResourceServesAs
                                                                                  +   adminState: String                                                             +   usageState: Integer
                                                                                  +   operationalState: String                                                0..*
                                                                                  +   serviceState: String             0..*
                        0..1                                                      +   type: String

      ServiceSpecCharacteristic                                                                           0..*

                                                                                                SapSpecDescribes

                                                                                                        1..1

                                                                                                SapSpecification
                                                        ApplicableServices
                                                                                  +   applicableStateValues: String
               ServiceSpecificationType
                                                 1..*                        1..1 +   type: String




                                                                                Figure SO.33 TIP Service Management - Service Activation



© TM Forum 2025. All Rights Reserved                                                                                                                           161                               of   177
    Information Framework (SID) Suite Service Domain R25.0.0




© TM Forum 2025. All Rights Reserved                           162   of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.33a - TIP Service Management - CommonServiceInfo

  A number of the Service Management entities are extended via their association with the CommonServiceInfo entity and via inheritance with
  the CommonObjectInfo entity as shown in Figure SO.33a.

                                                                                                                      CommonObjectInfo

                                                                                                     +    additionalInfo: AttributeValuePair [0..*]
                                                                                                     +    aliasNameList: AttributeValuePair [0..*] {readOnly}
                       ManagedEntity                                                                 +    discoveredName: String {readOnly}
                                                            ManagedEntityIsExtendedBy                +    name: ObjectName {readOnly}
        +    managementMethodCurrent: Integer                                                        +    namingOsRef: String {readOnly}
        +    managementMethodSupported: Integer 1..1                                            0..1 +    nativeEmsName: String
                                                                                                     +    owner: String
                                                                                                     +    userLabel: String




                  Service

    +       hasStarted: Boolean                                                                                                                          SapSpecification
                                                ServiceIsExtendedBy                      CommonServiceInfo
    +       isMandatory: Boolean                                                                                                               +   applicableStateValues: String
    +       isServiceEnabled: Boolean 1..1                                      0..1 +   description: String
                                                                                                                                               +   type: String
    +       isStateful: Boolean
    +       startMode: Integer                                                                             0..1         0..1
                                                                                                                                                                      1..1

                                                                                                                               SapSpecificationIsExtendedBy



                                                                                            ServiceAccessPointIsExtendedBy
                                                             ServiceAccessPoint

                                                        +   adminState: String
                                                        +   operationalState: String
                                                        +   serviceState: String         1..1
                                                        +   type: String




© TM Forum 2025. All Rights Reserved                                                                                                               163                             of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                         Figure SO.33a - TIP Service Management - CommonServiceInfo




© TM Forum 2025. All Rights Reserved                                                                       164        of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  Figure SO.34 - Example of Ethernet Service CFS/RFS

  Ethernet Services Example

  The following example is based upon multiple service providers involved in the delivery of wholesale and retail services. The Network Service
  Provider (NSP) offers triple-play IP services to his residential customers, represented by an IP CFS. This CFS is instantiated over the Service
  Activation Interface (SAI). The NSP Service Management OSS decomposes the CFS into different resource facing service components that
  require management, one of them being the Ethernet Connectivity RFS (which may also be split into Ethernet access, and Ethernet
  Aggregation and Backhaul).

  The NSP purchases both Ethernet Access and Aggregation & Backhaul Products from the Broadband Ethernet Access (BEA) and Broadband
  Aggregation & Backhaul (BAB) providers respectively; these are represented in the BEA/BAB domains as “products”. They are instantiated as
  Ethernet Access Line CFS and Ethernet Backhaul CFS over the BEA/BAB Service Activation Interfaces in their respective OSS/BSS domains.
  The BEA and BAB Service Management OSS decompose these CFS’s into resource facing services that get instantiated over Service
  Component Activation interfaces. As a result, the underlying resources to support the component RFS are provisioned. The BEA and the BAB
  notify the NSP that their respective services are available and operational.




© TM Forum 2025. All Rights Reserved                                                           165                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                               Figure SO.34 - Example of Ethernet Service CFS/RFS




© TM Forum 2025. All Rights Reserved                                                                           166   of   177
       Information Framework (SID) Suite Service Domain R25.0.0




  5          Administrative Appendix
  This Appendix provides additional background material about the TM Forum and this document. In general, sections may be included or
  omitted as desired; however, a Document History must always be included.

  About this document
  This is a TM Forum Guidebook. The guidebook format is used when:

        The document lays out a ‘core’ part of TM Forum’s approach to automating business processes. Such guidebooks would include the Telecom
           Operations Map and the Technology Integration Map, but not the detailed specifications that are developed in support of the approach.
        Information about TM Forum policy, or goals or programs is provided, such as the Strategic Plan or Operating Plan.
        Information about the marketplace is provided, as in the report on the size of the OSS market.



  5.1        Document History
  Version History

 Version          Date                      Modified by           Purpose
 Number
 0.1              September 2002            J. Strassner          First rough draft

 0.2              October 2002              J. Strassner          Final population using DEN-ng high-level service model, which contains mined information from
                                                                  DEN, OSS/J and MetaSolv




© TM Forum 2025. All Rights Reserved                                                                       167                  of   177
       Information Framework (SID) Suite Service Domain R25.0.0




 Version          Date                      Modified by           Purpose
 Number
 0.3              October 2002              J. Strassner          Final draft ready for modeling team to review

 0.4              November 2002             J. Strassner          Updated in response to detailed comments from John Reilly and Chris Hartley

 0.5              November 2002             J. Strassner          Updated to incorporate additional comments from John Reilly and Cliff Faurer.

 1.0              November 2002             TMF                   Formatted for TMF Publishing

 1.1              April 2003                J. Strassner          Added ServicePackage and ServiceBundle, which link to the QoS model. Minor corrections to get
                                                                  Service model better in sync with other models

 1.2              May 2003                  J. Strassner          Incorporated comments from the SID team, including detailed comments from Cliff and John
                                                                  Reilly. Excised ProductItem, and enhanced the link to the QoS Addendum.

 1.3              May 2003                  J. Strassner          Incorporated final comments from Cliff, updated for consistency with other Addenda

 1.4              June 2003                 J. Strassner          Updated PartyRole interaction section

 2.0              July 2003                 TMF                   Formatted for Member Review with NGOSS R3.5

 2.1              Aug 2004                  TMF                   To reflect TMF Approved Status

 3.0              Mar 2008                  J Reilly              Updates to Characteristics and miscellaneous updates to synchronize addendum with UML
                                                                  model.




© TM Forum 2025. All Rights Reserved                                                                         168                 of   177
       Information Framework (SID) Suite Service Domain R25.0.0




 Version          Date                      Modified by           Purpose
 Number
 7.5              Jan 2008                  John Reilly           Updated for ITU-T submission

 7.6              May 2008                  Tina O’Sullivan       Converted to correct template and other corrections prior to posting.

 7.7              July 2008                 John Reilly           Updates to Characteristics and miscellaneous updates to synchronize addendum with UML
                                                                  model.

 7.8              July 2008                 John Reilly           Updates after new template applied

 7.9              July 2008                 Tina O’Sullivan       Final changes prior to posting.

 8.0              May 2009                  Alicja Kawecki        Minor updates to reflect TM Forum Approved status

 9.0              January 2010              John Reilly           Updates to reflect SID Phase IX Change Requests

 9.1              April 2010                Alicja Kawecki        Minor cosmetic corrections for web posting and ME

 9.2              June 2010                 Alicja Kawecki        Updated Notice

 9.3              Oct 2010                  Alicja Kawecki        Updated to reflect TM Forum Approved status

 9.4              January 2011              Josh Salomon          Updates to reflect SID release 9.5 change requests

 9.5              March 2011                John Reilly           Correct figure references and corrupt table.




© TM Forum 2025. All Rights Reserved                                                                         169                  of   177
       Information Framework (SID) Suite Service Domain R25.0.0




 Version          Date                      Modified by           Purpose
 Number
 9.6              March 2011                Alicja Kawecki        Updated Notice, minor formatting corrections prior to web posting and ME

 9.7              September 2011            Alicja Kawecki        Updated to reflect TM Forum Approved status

 9.8              June 2013                 Cécile Ludwichowski Incorporation of CR:

                                                                  Artf2381 (Figure SO.45)

                                                                  Artf1431 (Figure SO.31, SO-33)

                                                                  Artf1788

 9.9              July 2013                 Alicja Kawecki        Updated cover & notice, corrected footer prior to posting

 9.10             Sep 2013                  Alicja Kawecki        Added IPR Mode to cover, updated notice to reflect TM Forum Approved status

 9.10.1           Nov 2013                  Alicja Kawecki        Updated cover, header, footer & Notice to reflect TM Forum Approved status

 14.5.0           October 2014              John Reilly           Updated Figure SO.7 to align with model

 14.5.1           March 2015                Alicja Kawecki        Updated cover, header, footer and Notice to reflect TM Forum Approved status

 16.0             May 2016                  John Reilly           Aligned model and guidebook, removed data dictionary, and aligned with changes in other
                                                                  domains.




© TM Forum 2025. All Rights Reserved                                                                         170                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




 Version       Date                      Modified by           Purpose
 Number
 16.0.1        26 May 2016               Alicja Kawecki        Minor cosmetic edits prior to publication for Fx16

 17.0.0        March 2017                Cécile Ludwichowski Remove SID framework figure from the guidebook

 17.0.1        27 June 2017              Alicja Kawecki        Applied rebranding and minor cosmetic edits prior to publication for Fx17

 17.0.2        16 November 2018          Adrienne Walcott      Updated cover, notice and minor cosmetic changes prior to publishing




 17.5.0        30 June 2017              Cécile Ludwichowski Correct typo for AdministerResourceDetails (FP-462)

                                                               Correct all figures numbering

                                                               Change CFSSpec, RFSSpec, CFS, RFS - Composite / Atomic to concrete Class

                                                               fixed typo

 17.5.1        19 Dec 2017               Adrienne Walcott      Formatting/style edits prior to publishing

 18.0.0        05 Jun 2018               Cécile Ludwichowski Replaces the relation between ProductSpecification and ProductOffering by a derived relationship
                                                             that can be seen as an overview

                                                               Characteristic model clean-up for Product and ProductSpecification




© TM Forum 2025. All Rights Reserved                                                                        171                of   177
    Information Framework (SID) Suite Service Domain R25.0.0




 Version       Date                      Modified by           Purpose
 Number
 18.0.1        12 Jul 2018               Adrienne Walcott      Formatting/style edits prior to R18 publishing

 18.0.2        10-Oct-2018               Adrienne Walcott      Updated to reflect TM Forum Approved Status

 18.5.0        03-Dec-2018               Cécile Ludwichowski Updated according to FP-745 SID-Characteristics clean-up for Service, Resource and Usage.

 18.5.1        05-Mar-2019               Cécile Ludwichowski Updated to reflect TM Forum Approved Status

 20.0.0        03-June-2020              Cécile Ludwichowski Guidebook generated from RSA with BIRT report.

 21.0.0        04-June-2021              Cécile Ludwichowski This release includes changes coming from the following Change Request

                                                               - Split Capacity ABE in each horizontal Domain concerned

 23.0.0        16-June-2023              Cécile Ludwichowski This release includes diagram review and cleanup given the move from RSA to Sparx EA modeling
                                                             tool per ISA-772

 24.5.0        10-Jan-2025               Kevin Scaggs          This release includes Usage ABE grouping updates per ISA-969, Level 1 ABE description updates
                                                               per ISA-1113, and diagrams for ABEs with no diagrams per ISA-1202

 25.0.0        18-July-2025              Kevin Scaggs          This release of the Service Guidebook includes updates as follows:

                                                                      •       Adding concept of UsageVolumeBalance per ISA-1129, and
                                                                      •       Updating TIP Service Management ABE to "likely to be depreciated" per ISA-1243.




© TM Forum 2025. All Rights Reserved                                                                      172                 of    177
       Information Framework (SID) Suite Service Domain R25.0.0




  Release History

 Release Number Date Modified                 Modified by:         Description of changes
 8.0                    17/July/2008          John Reilly          Updates to Characteristics and miscellaneous updates to synchronize addendum with UML
                                                                   model.

 9.0                    January 2010          John Reilly          Updates to reflect SID Phase IX Change Requests

 9.5                    January 2011          Josh Salomon         Updates to reflect SID release 9.5 change requests

 13.0                   June 2013             Cécile Ludwichowski Incorporation of CR:

                                                                    Artf2381 (Figure SO.45)

                                                                    Artf1431 (Figure SO.31, SO-33

                                                                    Artf1788

 14.5.0                 October 2014          John Reilly          Updated Figure SO.7 to align with model and added ServiceLevelSpecExpression entity and
                                                                   figure.

 16.0                   May 2016              John Reilly          Aligned model and guidebook, removed data dictionary, and aligned with changes in other
                                                                   domains.

 17.0                   March 2017            Cécile Ludwichowski Remove SID framework figure from the guidebook

 17.1                   November 2017         Adrienne Walcott     Updated to reflect TM Forum Approved Status




© TM Forum 2025. All Rights Reserved                                                                       173                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




 Release Number Date Modified              Modified by:         Description of changes
 17.5                December 2017         Cécile Ludwichowski Correct typo for AdministerResourceDetails (FP-462)

                                                                Correct all figures numbering

                                                                Change CFSSpec, RFSSpec, CFS, RFS - Composite / Atomic to concrete Class (FP-627)

                                                                fixed typo

 18.0.0              05 June 2018          Cécile Ludwichowski Replaces the relation between ProductSpecification and ProductOffering by a derived
                                                               relationship that can be seen as an overview

                                                                Characteristic model clean-up for Product and ProductSpecification

                                                                Remove all Entities identified as “Likely to be removed” in 17.0

 18.0.1              10-Oct-2018           Adrienne Walcott     Updated to reflect TM Forum Approved Status

 18.5.0              03-Dec-2018           Cécile Ludwichowski Updated according to FP-745 SID-Characteristics clean-up for Service, Resource and Usage.

 18.5.1              05-Mar-2019           Adrienne Walcott     Updated to reflect TM Forum Approved Status

 20.0.0              03-June-2020          Cécile Ludwichowski Guidebook generated from RSA with BIRT report.

 21.0.0              04-June-2021          Cécile Ludwichowski This release includes changes coming from the following Change Request

                                                                -Split Capacity ABE in each horizontal Domain concerned




© TM Forum 2025. All Rights Reserved                                                                      174                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




 Release Number Date Modified              Modified by:         Description of changes
 23.0.0              16-June-2023          Cécile Ludwichowski This release includes diagram review and cleanup given the move from RSA to Sparx EA modeling
                                           & Kevin Scaggs      tool per ISA-772.

 24.5.0              10-Jan-2025           Kevin Scaggs         This release includes Usage ABE grouping updates per ISA-969, Level 1 ABE description updates
                                                                per ISA-1113, and diagrams for ABEs with no diagrams per ISA-1202.

 25.0.0              18-July-2025          Kevin Scaggs          This release of the Service Guidebook includes updates as follows:

                                                                        •      Adding concept of UsageVolumeBalance per ISA-1129, and
                                                                        •      Updating TIP Service Management ABE to "likely to be depreciated" per ISA-1243.




© TM Forum 2025. All Rights Reserved                                                                    175                  of   177
    Information Framework (SID) Suite Service Domain R25.0.0




  5.3     Acknowledgments
  This document was prepared by the members of the TM Forum Information Framework (SID) team.

  The Shared Information/Data Model is a genuinely collaborative effort. The TM Forum would like to thank the following people for contributing
  their time and expertise to the production of this document. It is just not possible to recognize all the organizations and individuals that have
  contributed or influenced the introduction. We apologize to any person or organization we inadvertently missed in these acknowledgments.

  Key individuals that reviewed, provided input, managed, and determined how to utilize inputs coming from all over the world, and really made
  this document happen were:



                                                   Name                  Affiliation

                                                   Cliff Faurer          TM Forum

                                                   Ram Garg              MetaSolv Software

                                                   Chris Hartley         Telstra

                                                   Helen Hepburn         British Telecom

                                                   Jenny Huang           AT&T

                                                   Matt Izzo             Agilent Technologies

                                                   Jessie Jewitt         Ciena




© TM Forum 2025. All Rights Reserved                                                            176                 of   177
    Information Framework (SID) Suite Service Domain R25.0.0




                                                   Name                  Affiliation

                                                   Cécile Ludwichowski   Orange

                                                   Mike McLoughlin       British Telecom

                                                   Dave Raymer           Motorola

                                                   John Reilly           TM Forum

                                                   Wayne Sigley          Telstra

                                                   Yaroslav Oratovsky    NetCracker

                                                   John Strassner        Intelliden (original editor)

                                                   Jean-Marie Magueur    Orange

                                                   Emmanuel Otchere      Huawei

                                                   Kevin Scaggs          TM Forum




© TM Forum 2025. All Rights Reserved                                                             177    of   177

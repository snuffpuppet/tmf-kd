---
type: etom-l2
spec_id: GB921
spec_version: "25.5"
retrieval_date: 2026-05-08
source_paths:
  - raw/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.xlsx
source_extract_paths:
  - raw/extracted/tmf/etom/GB921_Business_Process_Framework_Processes_Excel_v25.5.md
authority: primary
l1_parent: "1.4 Service Domain"
l2_id: "1.4.5"
l2_name: "Service Activation Management"
---

# Service Activation Management

> **Vertical context:** Fulfillment ([[wiki/foundations/lifecycle]]).
> **Domain:** Service Domain ([[wiki/foundations/domains#Service Domain]]).

## Overview

Service Activation Management processes encompass allocation, implementation, configuration, activation and testing of specific services to meet customer requirements, or in response to requests from other processes to alleviate specific service capacity shortfalls, availability concerns or failure conditions.  Where included in the service provider offering, these processes extend to cover customer premises equipment.
Responsibilities of the Service Configuration & Activation processes include, but are not limited to:
• Verifying whether specific service designs sought by customers are feasible as part of pre-order feasibility checks;
• Allocating the appropriate specific service parameters to support service orders or requests from other processes;
• Reserving specific service parameters (if required by the business rules) for a given period of time until the initiating customer order is confirmed, or until the reservation period expires (if applicable);
• Implementing, configuring and activating specific services, as appropriate;
• Testing the specific services to ensure the service is working correctly;
• Recovery of specific services;
• Updating of the Service Inventory Database to reflect that the specific service has been allocated, modified or recovered;
• Assigning and tracking service provisioning activities; 
• Managing service provisioning jeopardy conditions
• Reporting progress on service orders to other processes.
This process was renamed in 24.0 Old name was Service Configuration & Activation

— GB921 v25.5 Excel master, process ID `1.4.5`, sheet `eTOM25,5`.

## L3 Process Details

Per-L3 Extended Descriptions and L4 sub-process listings, verbatim from GB921 v25.5 Excel master. The L2 Overview above gives the L2-level brief; this section provides the L3 narrative depth and the L4 hierarchy.

### 1.4.5.1 Design Solution

**Extended Description.**

The purpose of the Design Solution processes is to develop an end-end specific service design which complies with a particular customer's requirement.

These processes are invoked when a customer order requires special or unusual end-end service arrangements, which are not able to be satisfied using standard service arrangements. These processes may be invoked as part of a service feasibility assessment, or as a result of a confirmed customer order.

The responsibilities of these processes include, but are not limited to:

•Developing an overall service solution design for a particular customer, including customer premises equipment, operational methods, resource assignments and pre-order feasibility;

•Developing an implementation plan considering training and operational support measures and needs, such as the proper parameter information for the Service Quality Management process;

•Consideration of current and future service and underlying resources infrastructure, as well as expected solution results, budget, duration and risks;

•Consideration of the time schedule according with customer requirements;

•Ensure service and provisioning efficiency;

•Undertaking a business assessment, ensuring an appropriate time-to-revenue as a result of the service and underlying resource investment

•Developing a detailed design identifying the relevant service orders to be issued to the Implement,

Configure & Activate Service process and the Allocate Specific Service Parameters to Services processes.

A specific service design may require inclusion of some or all of the above aspects depending on whether the service design is being undertaken as part of a feasibility assessment, or is being developed as a result of a committed customer order.

These processes invoke requests to Resource Domain provisioning processes to determine the availability of suitable specific resources, or parties though the Service Domain process in the event that the service design requires either the inclusion of outsourced or partner provided specific services.

**L4 sub-processes:**

- **1.4.5.1.1** Develop Overall Service Design — Develop an overall service solution design for a particular customer, including customer premises equipment, operational methods, resource assignments and pre-order feasibility;
- **1.4.5.1.2** Develop Service Implementation Plan — Not used for this process element.
- **1.4.5.1.3** Develop Detailed Service Design — Develop a detailed design identifying the relevant service orders to be issued to the Implement, Configure & Activate Service process and the Allocate Specific Service Parameters to Services processes.

### 1.4.5.2 Allocate Specific Service Parameters to Services

**Extended Description.**

The purpose of the Allocate Specific Service Parameters to Services processes is to issue service identifiers for new services.

Where the Allocate Specific Service Parameters to Services processes are requested by a pre-feasibility service order, or by the Design Services processes, these processes determine whether the requested service parameters are available. Depending on business rules, and on any specific levels of commitment contained in the initiating service order or service design request, these processes may reserve specific service parameters linked to the initiating service order or service design request for a period of time, and releasing them when the time period has expired. These processes are responsible for creating a response to the initiating processes with respect to the feasibility assessment.

Where the Allocate Specific Service Parameters to Services processes are requested by a service order issued in response to a confirmed customer order, these processes are responsible for allocating the specific service parameters required to satisfy the initiating service order. Any previously reserved specific service parameters are marked as allocated.

**L4 sub-processes:**

- **1.4.5.2.1** Determine Service Parameter Availability — Where the Allocate Specific Service Parameters to Services processes are requested by a pre-feasibility service order, or by the Design Services processes, these processes determine whether the requested service parameters are available.
- **1.4.5.2.2** Reserve Service Parameters — Not used for this process element.
- **1.4.5.2.3** Release Service Parameter — Release the reservation when the time period has expired.
- **1.4.5.2.4** Allocate Service Parameters — Not used for this process element.

### 1.4.5.3 Track & Manage Service Provisioning

**Extended Description.**

The objective of the Track & Manage Service Provisioning processes is to ensure service provisioning activities are assigned, managed and tracked efficiently.

Responsibilities of these processes include, but are not limited to:

• Scheduling, assigning and coordinating service provisioning related activities;

• Generating the respective resource order creation request(s) to Issue Resource Orders based on specific service orders;

• Escalating status of service orders in accordance with local policy; • Undertaking necessary tracking of the execution process;

• Adding additional information to an existing service order;

• Modifying information in an existing service order;•

• Modifying the service order status;

• Canceling a service order when the initiating customer order is cancelled;

• Monitoring the jeopardy status of service orders, and escalating service orders as necessary

• Indicating completion of a service order by modifying the service order status.

Note that some specific service components may be delivered by other parties. In these cases the Track & Manage Service Provisioning process is responsible for initiating requests, through Party Order handling for the delivery by the party of the specific service components.

**L4 sub-processes:**

- **1.4.5.3.1** Assign Service Provisioning Activity — Schedule, assign and coordinate service provisioning related activities.
- **1.4.5.3.2** Track Service Provisioning Activity — Undertake necessary tracking of the execution process. Monitor the jeopardy status of service orders, and escalating service orders as necessary.
- **1.4.5.3.3** Manage Service Provisioning Activity — Not used for this process element.

### 1.4.5.4 Implement, Configure & Activate Service

**Extended Description.**

The purpose of the Implement, Configure & Activate Service processes is to implement, configure and activate the specific services allocated against an issued service order.

These processes are responsible for, but not limited to:

•Assessing and planning the approach to be undertaken for implementation, configuration and activation;

•Re-using standard implementation, configuration and activation processes applicable to specific services;

•Implementing, configuring and reconfiguring specific services, including customer premises equipment if part of the service provider offering.

•Providing notifications as required if the implementation, configuration and activation activity requires a planned outage or is likely to initiate false specific service alarm event notifications

•Updating the information contained in the service inventory as to the configuration of specific services and their status.

At the successful conclusion of these activities, the status of the specific services will be changed from allocated to activated, which means they are in-use.

**L4 sub-processes:**

- **1.4.5.4.1** Configure Service — Not used for this process element.
- **1.4.5.4.2** Implement Service — Not used for this process element.
- **1.4.5.4.3** Activate Service — Not used for this process element.

### 1.4.5.5 Test Service End-to-End

**Extended Description.**

The responsibility of the Test Service End-to-End processes is to test specific services to ensure all components are operating within normal parameters, and that the service is working to agreed performance levels before its activation for the customer.

This purpose is performed through testing the service end-to-end as far as possible.

These processes test specific services against external party defined test plans, or against test plans developed by the service provider.

Where appropriate test plans are not available these processes are responsible for developing appropriate test plans. These processes are also responsible for capturing and storing the test results for historical and downstream testing comparison purposes.

If these tests succeed, the specific services will be marked as in-service which means the specific services are available for use by customers.

**L4 sub-processes:**

- **1.4.5.5.1** Test Service — Not used for this process element.
- **1.4.5.5.3** Capture Service Test Results — Capture and store the test results for historical and downstream testing comparison purposes. If the tests succeed, the specific services will be marked as in-service which means the specific services are available for use by customers.

### 1.4.5.6 Issue Service Orders

**Extended Description.**

The purpose of the Issue Service Orders processes is to issue correct and complete service orders.

The service orders may be required to satisfy pertinent customer order information received, may arise as a result of requests for service provisioning to satisfy service problem recovery activities, may arise to alleviate service performance issues, or may arise as a result of information received from parties in relations to specific services.

These processes assess the information contained in the customer order, through a service order request, relating to the purchased product offering, initiating service process or external party initiated request, to determine the associated service orders that need to be issued.

The issued service order may require a service feasibility assessment or a service design to be produced, may require new provisioning activities for specific services, may require a change to a previously issued service order, or may require deletion and/or recovery of previously delivered specific services. Where, the initiating request or the purchased product offering has a standard set of associated service orders this process is responsible for issuing the service orders, and for creating a record of the relevant initiating request or customer order information and the associated service orders.

Where the initiating request or the purchased product offering has special or unusual requirements, and a specific feasibility assessment and/or service design has been previously created, this process is responsible for issuing the service orders, and for creating a record of the relevant initiating request or customer order information and the associated service orders.

Where the purchased product offering has special or unusual requirements, and a specific feasibility assessment and/or specific service design has not been previously created, this process marks the issued service order as requiring special handling, and passes management for further processing to the Track & Manage Service Provisioning process.

The orchestration, if required, and tracking of the service order progress is the responsibility of the Track & Manage Service Provisioning processes.

**L4 sub-processes:**

- **1.4.5.6.1** Assess Service Request — Not used for this process element.
- **1.4.5.6.2** Create Service Orders — Not used for this process element.
- **1.4.5.6.3** Mark Service Order for Special Handling — Not used for this process element.

### 1.4.5.7 Report Service Provisioning

**Extended Description.**

The objective of the Report Service Provisioning processes is to monitor the status of service orders, provide notifications of any changes and provide management reports.

These processes are responsible for continuously monitoring the status of service orders and managing notifications to processes and other parties registered to receive notifications of any status changes. Notification lists are managed and maintained by the Enable Service Configuration & Activation processes.

These processes record, analyze and assess the service order status changes to provide management reports and any specialized summaries of the efficiency and effectiveness of the overall Service Configuration & Activation process. These specialized summaries could be specific reports required by specific audiences.

**L4 sub-processes:**

- **1.4.5.7.1** Monitor Service Order Status — responsible for continuously monitoring the status of service orders; record, analyze and assess the service order status changes
- **1.4.5.7.2** Distribute Service Order Notification — Not used for this process element.
- **1.4.5.7.3** Distribute Service Provisioning Reports — Provide management reports and any specialized summaries of the efficiency and effectiveness of the overall Service Configuration & Activation process. These specialized summaries could be specific reports required by specific audiences.

### 1.4.5.8 Close Service Order

**Extended Description.**

The objective of the Close Service Order processes is to close a service order when the service provisioning activities have been completed.

These processes monitor the status of all open service orders, and recognize that a service order is ready to be closed when the status is changed to completed.

### 1.4.5.9 Recover Service

**Extended Description.**

The responsibility of the Recover Service processes is to recover specific services that are no longer required by customers.

These processes follow recovery plans specified by the external party, or against recovery plans developed by the service provider.

Where appropriate recovery plans are not available these processes are responsible for developing appropriate recovery plans.

Where recovery of services is likely to impact other in-use specific services, this process is responsible for providing appropriate notification of the recovery proposal and ensuring authorization is received to proceed with the recovery plan. When the recovery activity is about to commence, these processes are responsible for notifying when recovery work is commencing and when it is completed.

When recovered, the specific services and/or associated service specific parameters will be marked as unallocated.

**L4 sub-processes:**

- **1.4.5.9.1** Develop Service Recovery Plan — Where appropriate recovery plans are not available this process is responsible for developing appropriate recovery plans.
- **1.4.5.9.2** Provide Service Recovery Proposal Notification — Where recovery of services is likely to impact other in-use specific services, this process is responsible for providing appropriate notification of the recovery proposal.
- **1.4.5.9.3** Request Service Recovery Authorization — Ensure authorization is received to proceed with the recovery plan.
- **1.4.5.9.4** Commence Service Recovery — When the recovery activity is about to commence, this processes is responsible for notifying when recovery work is commencing.
- **1.4.5.9.5** Complete Service Recovery — This process is responsible for notifying when it is completed. When recovered, the specific services and/or associated service specific parameters will be marked as unallocated.

— GB921 v25.5 Excel master, sheet `eTOM25,5`.

## L3 Processes

The following L3 processes decompose this L2. Verbatim from GB921 v25.5:

- **1.4.5.1** Design Solution — Develop an end-end specific service design which complies with a particular customer's requirement
- **1.4.5.2** Allocate Specific Service Parameters to Services — Issue service identifiers for new services.
- **1.4.5.3** Track & Manage Service Provisioning — Ensure service provisioning activities are assigned, managed and tracked efficiently.
- **1.4.5.4** Implement, Configure & Activate Service — Implement, configure and activate the specific services allocated against an issued service order.
- **1.4.5.5** Test Service End-to-End — Test specific services to ensure all components are operating within normal parameters, and that the service is working to agreed performance levels
- **1.4.5.6** Issue Service Orders — Issue correct and complete service orders
- **1.4.5.7** Report Service Provisioning — Monitor the status of service orders, provide notifications of any changes and provide management reports.
- **1.4.5.8** Close Service Order — Close a service order when the service provisioning activities have been completed
- **1.4.5.9** Recover Service — Recover specific services that are no longer required by customers.

## SID Entities Manipulated

See open-questions.md — OQ-008 (eTOM↔SID trilateral linking deferred to a sweep
after all eTOM L2s are ingested; bidirectional consistency requires updating SID
entity pages with reciprocal links).

## ODA Components That Realise This Process

- [[wiki/oda/functional-blocks/production]]

See open-questions.md — OQ-008 (further ODA components pending trilateral sweep).

## Open Questions

- OQ-008: Trilateral linking pending eTOM/SID/ODA cross-domain sweep
- OQ-035: Source verbatim extracted from the Excel master; narrative content from the
  Service Process Decompositions PDF (GB921_Service_Process_Decompositions_v24.0.pdf)
  is not yet layered in. Will be added in a follow-up ingest.

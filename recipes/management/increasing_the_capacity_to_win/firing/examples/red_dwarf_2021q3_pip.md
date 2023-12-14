This Performance Plan is a follow up from our [2021 Performance Review](LINK) where it was determined that you were missing our expectations. Through various follow-on conversations, and a recent email exchange, it appears that you are still not certain what the expectations of a [Staff-level engineer at Doxel](https://github.com/Doxel-AI/company_handbook/blob/main/career_ladder/eng_ladder.md) might be. This document outlines exactly what we expect you to be able to accomplish in the next 30 days, and then on a continued basis, at Doxel.

While this plan attempts to be comprehensive, certain regular day-to-day responsibilities that are well-understood may not be documented, such as on-call or attending meetings. The employee understands that they cannot fail to perform those responsibilities even if they are not included below. The employee also understands that job responsibilities can change over time and they must adapt to new job responsibilities, per the needs of the business.

In several situations Red Dwarf has pushed back against expectations saying they were unclear and continually asked for more clarifications. This plan is written such that a competent Senior-level engineer can understand the expectation. It has been reviewed by several engineers to confirm that this is true. No further clarifications will be provided and inability to understand this plan, or any further pushback on expectations, will be considered an immediate failure to meet Doxel’s expectations of the role.

Failure to meet the expectations of this plan may result in a change of compensation, a change in role, or termination from the company. If the employee meets the expectations in this plan they are expected to continue performing at this level, indefinitely. Any future failures to perform, past the 30 day window of this plan, may result in an immediate change of compensation, a change in role, or termination from the company.

Red Dwarf has been working on HALT for over a year. The work below focuses mostly on HALT and sets the expectations of where the project should be after a year of development. All of the work below must be complete for this plan to be considered successful.


## Architecture/Design



1. Red Dwarf will write a comprehensive design document for HALT.
    1. The document should cover all the normal surface areas that a production-grade system should have defined. 
    2. Red Dwarf is expected to know how to write design documents for production-grade algorithmic systems like HALT. He can consult with John or REDACTED for structure or content recommendations, but is expected to deliver a document even without their help.
    3. The document will be reviewed by John and REDACTED for any major gaps. Their reviews will be forwarded to Dobromir.
2. Red Dwarf will refactor HALT to fit into the functional interface approach the D.C. team has been migrating to.
3. A Staff-level engineer should be able to identify, define, implement, and socialize higher-level abstractions that speed the rest of the engineering team. Red Dwarf will evaluate how to do so for HALT, KRX, and other alignment techniques. Once approved by REDACTED and John, Red Dwarf will convert HALT to fit into this abstraction.


## Coding Skills



1. Red Dwarf will immediately begin code reviewing all Data Capture pull requests to:
    1. Regularly suggest edge-case improvements.
    2. Regularly teach and enforce readability concepts.
    3. Discover reusability opportunities and note them.
    4. Ensure code is appropriately tested and help the authors improve their testing approaches.
    5. Every week, Red Dwarf will send the list of Pull Requests he reviewed to REDACTED and Dobromir. 
2. Red Dwarf will immediately start breaking up PRs into smaller, more reviewable chunks, starting from [this one](REDACTED). PRs should be small, logical chunks that can be reviewed easily and submitted within a few days of authoring. Red Dwarf will avoid large PRs that take >1 week to submit.
3. For pull requests authored by David Bueno, Red Dwarf will be the first reviewer and will catch 90% of issues. The code will then be reviewed and approved by REDACTED. Any pull request where a significant number of issues were not caught by Red Dwarf will be forwarded to Dobromir for review.
4. Red Dwarf will achieve 70% unit test coverage (lines of code) of HALT code, using C++ and Python unit-testing best practices.
5. Once the alignment abstraction has been defined, Red Dwarf will add integration tests that cover multiple devices and alignment failure modes (e.g. symmetry, stage of construction changes, etc). 
6. Red Dwarf will integrate HALT mode onboarding checks into the [model onboarding DAG](REDACTED).


## Project Management



1. Red Dwarf will put together a clear roadmap for remaining HALT development with dates and milestones that are easily understandable. It should include all the deliverables in this plan as well as major milestones (~2-4 week levels of scope) over the next few quarters.
    1. This roadmap will be reviewed by REDACTED and Dobromir. Clear communication is a key part of being a Staff engineer and Red Dwarf should be able to accomplish this without any guidance from either. 
2. Red Dwarf will send a weekly update with red/yellow/green status for each milestone.
    2. This update will be reviewed weekly by REDACTED and Dobromir. Clear communication is a key part of being a Staff engineer and Red Dwarf should be able to accomplish this without any guidance from either.


## Data Analysis

Halt improvements have been primarily driven by anecdote. The team has been asked to deploy improvements to production without quantitative justification of the value of the improvements. It has been asked of Red Dwarf several times to produce quantitative justification for improvements. These requests have either not been complied with or have required many reminders to get a modicum of justification. In alignment with the DC team’s OKR Red Dwarf will complete the following:



1. Using the Golden Dataset Red Dwarf will propose a generalizable quantitative metrics to compare alignment methods. 
2. Red Dwarf will apply the HALT algorithm to the Golden Dataset using both the standard ceiling grid model and the installed object model. 
3. Red Dwarf will improve the Golden Dataset in any way needed to make data analysis more robust. 
4. Red Dwarf will produce a report quantitatively outlining the changes in output based halt reference model selection. 
5. Red Dwarf will include scenarios where HALT is unable to align correctly and categorize them into possible future engineering projects, with at least a few ideas on what R&D could be performed to mitigate these scenarios.

This report should be of scientific quality, done without guidance from the team, and should be reviewed by REDACTED, Dobromir, and John. 

By signing this document the employee understands the expectations laid out above to be completed by July 5th, 2021, and the consequences of not meeting these expectations. 



By signing this document the manager confirms that it was reviewed with the employee and consequences of not meeting expectations have been shared.



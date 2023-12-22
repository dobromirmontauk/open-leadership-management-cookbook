

# Phase-Gates


# Introduction

The intent of this document is to provide an overview of the Engineering phase-gate process at Doxel. A phase-gate approach to project management works by dividing the project’s life cycle into multiple, well defined stages or _phases_ of development, with a decision point or _gate_ at the end of each. This enables us to communicate more clearly on the current state of the project in its development life cycle, and provides clear, actionable next steps to ensure our projects are delivered on time and with efficient use of resources.

At each gate, stakeholders make one of the following decisions:



* **Go** - The current phase is complete and ready to continue to the next phase.
* **Kill** - The project does not warrant further investment. Do not continue to the next phase, discontinue any active development, and conduct a retrospective.
* **Hold** - The project is viable, however not ready to continue to the next phase. Do not continue to the next phase until **Go** is declared.
* **Recycle** - Continued investment in the project requires changes to requirements. Return to a previous phase as necessary.

_Note: The phase-gate process can sometimes be used instead of Agile. That is not the intent here. This process is meant to aid in the communication and reporting of the current state of the project, but does not define how each phase should be accomplished (which should remain Agile in many cases)._


# Phase-Gate 0 (Discovery)

_1-2 Days_

**Objective**

Propose a new feature, initiative, or improvement with product leads to decide if it's worth pursuing further.


<table>
  <tr>
   <td><strong>Responsible</strong>
   </td>
   <td><strong>Accountable</strong>
   </td>
   <td><strong>Consulted</strong>
   </td>
   <td><strong>Informed</strong>
   </td>
  </tr>
  <tr>
   <td>PM/SPM
   </td>
   <td>Dir. of PM
   </td>
   <td>SLT Initiator
   </td>
   <td>-
   </td>
  </tr>
</table>


**Required Outputs**



1. Complete [Project Plan Document (PPD)](https://doxel-ai.atlassian.net/wiki/spaces/ENG/pages/1726414851/Project+Plan)


# Phase-Gate 1 (Ideation)

**_LG: 1 Sprint | SM: 1-2 Days_**

**Objective**

Create high-level user stories, user flow diagrams, and early-stage prototypes. Conduct initial consultation with Engineering leaders to get high-level T-shirt size.


<table>
  <tr>
   <td><strong>Responsible</strong>
   </td>
   <td><strong>Accountable</strong>
   </td>
   <td><strong>Consulted</strong>
   </td>
   <td><strong>Informed</strong>
   </td>
  </tr>
  <tr>
   <td>PM/SPM
   </td>
   <td>PM/SPM
   </td>
   <td>VP of Eng
<p>
Dir. of Eng
<p>
Product Designer
<p>
SLT Initiator
   </td>
   <td>VP of Product
<p>
SLT
<p>
Dir. of Product
   </td>
  </tr>
</table>


**Required Outputs**



2. Start [PRD](https://doxel-ai.atlassian.net/wiki/spaces/ENG/pages/1726545933/Product+Requirements+Document)
3. Define high-level milestones
4. User [flow diagrams](https://miro.com/app/board/uXjVOSHGx2w=/), competitor screenshots, and/or paper prototypes

**Optional Outputs**



5. High-level rollout plan
6. Documented quantitative and qualitative research
    * analytics data, competitor data, userfeed data, cs-sales meeting recaps


# Phase-Gate 2 (Betting)

**_LG: 2 Sprints | SM: 2-3 Days_**

**Objective**

Work closely with the design team to set up and complete the design and research process to define UI/UX of the project.


<table>
  <tr>
   <td><strong>Responsible</strong>
   </td>
   <td><strong>Accountable</strong>
   </td>
   <td><strong>Consulted</strong>
   </td>
   <td><strong>Informed</strong>
   </td>
  </tr>
  <tr>
   <td>PM/SPM
<p>
Product Designer
<p>
PMM
   </td>
   <td>PM/SPM
   </td>
   <td>Eng Lead
<p>
Dir. of Product
   </td>
   <td>SLT
<p>
VP of Eng
<p>
Dir. of Eng
<p>
Dir. of Product
   </td>
  </tr>
</table>


**Required Outputs**



7. Updated brief
8. Wireframes/mockups in Figma (70% by end of the phase)
9. UX Research - Research Process
    * CS/Sales Interviews
    * Customer Interviews
    * User Testing Plan
    * User Testing Summary
10. 1-2 Tech Consults with Engineering as needed

**Optional Outputs**



11. Competitor research - [TA] Competitive Analysis
12. Partner with PMM for research and TAM opportunity
13. Create Slack channel for Project to manage communication


# Phase-Gate 3 (Finalize Product + Eng Designs)

**_LG: 1 Sprint | SM: 1-2 Days_**

**Objective**

Complete brief, design, and research necessary to deliver the project.


<table>
  <tr>
   <td><strong>Responsible</strong>
   </td>
   <td><strong>Accountable</strong>
   </td>
   <td><strong>Consulted</strong>
   </td>
   <td><strong>Informed</strong>
   </td>
  </tr>
  <tr>
   <td>PM/SPM
<p>
Product Designer
<p>
PMM
   </td>
   <td>PM/SPM
   </td>
   <td>Eng Lead
<p>
DevOps
<p>
QA Lead
<p>
Dir. of Product
   </td>
   <td>SLT
<p>
VP of Eng
<p>
Dir. of Eng
<p>
Dir. of Product
   </td>
  </tr>
</table>


**Outputs**



14. Complete brief
    * Identify our competitive advantage. How is what we’re building better than or differentiated from our competitors?
15. Complete design (90%)
16. Documented Agreement on Final Scope with Engineering
17. Identify Engineering squad responsible for project execution
18. Product walkthrough of clickable prototype to find holes/gaps
19. Created epics and user stories in Jira
20. Define GTM Strategy with PMM

    ```
Passing through this gate will lock prerequisite documents. Any requirements changes past this point must go through a change request.
```




# Phase-Gate 4 (Implementation Planning)

_1-2 Days_

**Objective**

Refinement of execution plan and documentation within Jira. Onboard the Engineering squad that will be responsible for delivery of the project.


<table>
  <tr>
   <td><strong>Responsible</strong>
   </td>
   <td><strong>Accountable</strong>
   </td>
   <td><strong>Consulted</strong>
   </td>
   <td><strong>Informed</strong>
   </td>
  </tr>
  <tr>
   <td>PM/SPM
<p>
Product Designer
   </td>
   <td>PM/SPM
<p>
Eng Lead
<p>
Scrum Master
   </td>
   <td>Engineering Squad
<p>
Dir. of Eng
<p>
Scrum Master
<p>
Dir. of Product
<p>
DevOps
   </td>
   <td>SLT
<p>
VP of Eng
<p>
Dir. of Eng
<p>
Dir. of Product
   </td>
  </tr>
</table>


**Outputs**



21. Demo and walkthrough of feature with relevant Engineering squad
22. Invite Engineering squad members to project Slack channel
23. Start writing out AC for tickets in the first 2 sprints
24. Story mapping
25. Product Engineering backlog grooming and prioritization of Jira tickets


# Phase-Gate 5 (Development)

**_LG: 3 Sprints | SM: 1-2 Sprints_**

A project in this phase is actively undergoing development. The development process is Agile and consists of two-week sprints. Project demonstrations showcasing the current state of the project should be conducted at the end of each sprint, with all stakeholders present. Each sprint should also end with a detailed retrospective and lookahead of work planned for the next sprint.

Throughout the development process, the state of the project may be reported as being in one of the following:



* **Backend Complete: **Backend and DevOps work is complete, but frontend (UI) work is still underway or not fully integrated yet.
* **Front End Complete: **Frontend work is complete, but backend work is still underway, unstable, or otherwise not fully integrated yet. This usually means the frontend is still consuming stubbed APIs or other mocked systems.
* **Integrated: **Both backend and frontend work is complete, have been fully integrated into a development environment, and ready for testing.

**Objective**

Build and deliver the project to internal stakeholders. 


<table>
  <tr>
   <td><strong>Responsible</strong>
   </td>
   <td><strong>Accountable</strong>
   </td>
   <td><strong>Consulted</strong>
   </td>
   <td><strong>Informed</strong>
   </td>
  </tr>
  <tr>
   <td>PM/SPM
<p>
Engineering Squad
<p>
Scrum Master
   </td>
   <td>PM/SPM
<p>
Engineering Squad
<p>
Scrum Master
   </td>
   <td>Dir of Eng
<p>
Dir of Product
<p>
Product Designer
<p>
PMM
   </td>
   <td>SLT
<p>
VP of Eng
<p>
Dir of Eng
<p>
Dir of Product
   </td>
  </tr>
</table>


**Outputs**



26. Regular standup meetings
27. Bi-weekly project demos with stakeholders
28. Complete and QA tested project


# Phase-Gate 6 (Launch)

_1-2 Sprints_

**Objective**

Begin rollout communication and planning leading up to launch date.


<table>
  <tr>
   <td><strong>Responsible</strong>
   </td>
   <td><strong>Accountable</strong>
   </td>
   <td><strong>Consulted</strong>
   </td>
   <td><strong>Informed</strong>
   </td>
  </tr>
  <tr>
   <td>PM/SPM
<p>
PMM
   </td>
   <td>PM/SPM
<p>
Dir of PM
<p>
PMM
   </td>
   <td>Dir of PM
<p>
Sales/CS Leads
<p>
Marketing
<p>
PMM
<p>
Dir of Eng
<p>
Scrum Master
   </td>
   <td>SLT
<p>
VP of Eng
<p>
Dir of Eng
<p>
Dir of Product
   </td>
  </tr>
</table>


**Outputs**



29. CS/Sales Demo
30. Pre-launch marketing
31. Release notes
32. Beta release
33. GTM Marketing plan
34. Analytics integration into project
35. Rollout document


# Phase-Gate 7 (Post-Launch)

_1-2 Sprints_

**Objective**

Monitor, iterate and track progress post launch. Conduct project retrospective.


<table>
  <tr>
   <td><strong>Responsible</strong>
   </td>
   <td><strong>Accountable</strong>
   </td>
   <td><strong>Consulted</strong>
   </td>
   <td><strong>Informed</strong>
   </td>
  </tr>
  <tr>
   <td>PM/SPM
<p>
PMM
   </td>
   <td>PM/SPM
   </td>
   <td>Dir of PM
<p>
Sales/CS Leads
   </td>
   <td>SLT
<p>
Dir of Product
   </td>
  </tr>
</table>


**Outputs**



36. Updated KPIs, OKRs, and launch goals
37. Quantitative and qualitative analysis reports
38. Project retrospective


# Index

**Template Links**



* [Project Plan Document (PPD)](https://doxel-ai.atlassian.net/wiki/spaces/ENG/pages/1726414851/Project+Plan)
* [PRD template](https://doxel-ai.atlassian.net/wiki/spaces/ENG/pages/1726545933/Product+Requirements+Document)
* [Flow diagram](https://miro.com/app/board/uXjVOSHGx2w=/)
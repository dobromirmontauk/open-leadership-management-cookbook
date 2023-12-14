**Status: Ready to approve**

**Due Date: 7/27/21**

**Implementation Date: 7/28/21**


# Background

We are standardizing Doxel’s Sprint Process across all of our Product Engineering vertical teams in order to:



1. Increase our delivery velocity. Our ideal process helps us _ship faster._
2. Have more _predictable_ delivery. As an Enterprise-company we need to become world-class at knowing what we can ship, when, to help our Marketing & Sales teams promise things to customers.


# Open Discussion Topics

We will move this to in-person discussion once most of this process is agreed-upon:



1. QA/testing strategy: who is responsible for what?
2. [Story pointing: How do we do this?](https://docs.google.com/document/d/1Pf1JlzbFA4GDHJ-SbSFoYVnvxD0hI4C8meq9qG-0k1I/edit#)

 \
See notes below.


# Product Process

The Product team will have a process by which they do discovery and produce product requirements. That process is **out of scope** for this doc; here we assume that a Product Requirement Doc has been circulated (if required) and approved by engineering, and if a Technical Design Document is required that has also been written and approved by necessary stakeholders. Once those activities are done, work will be ready to pull into a delivery process.


# Sprint Process



1. Raw: Product-led JIRA tickets
    1. Once a PRD has been signed-off by the relevant Engineering + Product stakeholders, the PM is responsible for turning the document into a set of JIRA User Stories. Smaller work blocks (e.g. bug fixes, or minor feature requests) can be directly created as User Stories without the PRD step and added to the backlog. This will be the primary method by which PM communicates to Engineering how the work should be broken down, tested, and shipped. All stories go into the Backlog.
    2. **Owner**: PM
    3. **Participants:** VTL, eng team are optional
    4. **How**: asynchronous, this can take many hours
    5. **Timing: **Several weeks before the Sprint
    6. **Why**: Doxel wants to be a Product-driven culture and company so that we can quickly solve our customer’s problems. For PMs to have true control over the output of an engineering team they need to have their hands deep into the definition of the work being picked up.
2. Refine: Engineering-led JIRA tickets
    7. User stories and the TDD may need to be fleshed out with more detailed descriptions of the work. The VTL is responsible for getting all the tickets filled out and is expected to rely on their team to do a lot of the work.
    8. **Owner**: Vertical Technical Lead (Scrum Master?)
    9. **Participants**: eng team, PM (optional), designer (optional), EM (optional)
    10. **How: **asynchronous, this can take many hours
    11. **Timing: **>1 week before the Sprint
    12. **Why: **Product-led work may expand to a lot of things Product is not aware need to be done, especially on the backend, testing, etc. Engineering needs a chance to review what Product is asking for and call out those additional tasks.
3. Review [GROOMING]: Story-pointing + understanding the backlog
    13.  The entire team walks through the backlog to make sure that all the work is well-understood. The definition of “well-understood” is that the team is comfortable giving it a t-shirt size, via story points. **Tickets have work estimates (story points) that can fit into a single sprint**. Any ticket that is not well-understood can have a large story point number which means it needs more work to become well-understood. Bugs get 0 points in order to explicitly force “slow down” in our metrics if we are putting out bad products that need to be fixed later.
    14. **Owner**: Vertical Technical Lead
    15. **Participants**: PM, eng team, designer (optional)
    16. **How**: synchronous, OPEN ENDED (aim for ~1 hour after a few of these)
    17. **Timing**: exactly 1 week before the Sprint
    18. **Why**: most surprises in delivery happen when work gets started and then “whoops, I had no idea that this would be so complicated…” realizations occur. The majority of these can be nipped in the bud if the team is diligent about sitting down before committing to work. Story points are a good forcing function to prove that people actually have agreement and are not “pocket-vetoing” the discussion.
4. Ready: Sprint Planning → Sprint kicked off
    19. The Eng + PM team sits down together to finalize what can actually be done in the next 2 weeks. Tickets are selected in JIRA and assigned to engineers to execute. Once the team has reasonable confidence that **they can hit >80% of the story points assigned**, the Sprint can be started. The Scrum Master asks everybody in the Sprint with work assigned on their [Fist-to-Five score](https://www.lucidmeetings.com/glossary/fist-five) and records it as part of the Retro. 
    20. **Owner: **Vertical Technical Lead + PM
    21. **Participants: **eng team, designer
    22. **How**: synchronous. It is important to have a high-bandwidth meeting where questions can be asked, disagreements about what can be done in the next 2 weeks can be voiced, and actual commitment to the work is achieved. Should be time-boxed to 30 minutes to force most of the work into the previous steps (async as much as possible!!)
    23. **Timing:** T=0. We should kickoff sprints on **[Tuesdays](https://medium.com/@dmontauk/the-case-for-tuesdays-56df21eacfa)**. 
    24. **Why: **commitment must be **explicit**! If people are signing up for work, or being assigned work, and they don’t believe they can actually accomplish it - they need a forum to voice that. 
5. Product Lookahead
    25. Product sends out an email with what is expected to be delivered in the next 2 weeks and a link to the updated roadmap (~3-month lookahead, which is updated every 2 weeks as part of Sprint + backlog grooming). This email ideally is short; a few bullet points + a link to more detailed view.
    26. **Owner: **PM
    27. **How**: async
    28. **Timing**: same day as the sprint is kicked off. Ideally, it is being written during sprint planning, and hit “send” at the same time as the sprint is started :)
    29. **Why**: inform all of Doxel about what is happening, and provide us with clear goals for our Sprint Retro
6. Development
    30. Engineering meets **daily with REDACTEDdups** **to discuss blockers**.
    31. **Owner**: VTL (Scrum Master)
    32. **Participants**: eng-team, PM (mandatory), Designer (optional)
    33. **How: **synchronous, preferably, at least 2-3x/week. I am not a believer that async standup communication works. I can be convinced if people show me async standup communication where there are actual discussions happening, and not status updates that everyone ignores.
    34. **Timing**: daily in the 1st week after Sprint, ideally &lt;15 minutes. If much longer it means that steps above were skipped.
    35. **Why**: nothing beats f2f conversations. As a remote-first company we should have a daily meeting where everyone working together has a chance to see each other, laugh together, talk about problems together. 
7. Mid-Sprint Check-in
    36. Basically a longer standup that includes kicking off QA work, cleanup work, and adding/removing any tickets that make sense. Tickets **should not be removed because “we signed up for too much”** - they can be removed if new work is pre-empting other work. PM + VTL need to make that decision.
    37. **Owner: **PM
    38. **Participants**: VTL, eng-team, Designer, EM (optional)
    39. **How**: synchronous
    40. **Timing:** Tuesday 1 week into Sprint, **right before **the Review meeting which will go deeper into the backlog.
    41. **Why**: This is basically a standup but with a specific question of “folks, **last chance**” to say we aren’t going to accomplish something!
8. Sprint Part 2: Focus on finishing, not starting (esp. code merging / testing)
    42. Second week some development may be happening but people are working towards getting the release out. Focus should be on completing PRs (not starting new ones), fixing edge-cases, adding tests, etc. Continue **daily standups to discuss blockers**, with more emphasis on PM/QA being there to help test and release stuff.
    43. **Owner**: VTL (Scrum Master)
    44. **Participants: **eng-team
    45. **How**: same as Development
    46. **Timing**: daily on the 2nd week of the sprint
    47. **Why**: an explicit transition to “finish what you started” vs “start more stuff” will help us get work over the finish line and not have too much work in flight.
9. Sprint Report & Retro
    48. Review what was planned to be delivered, versus what actually was delivered. Do a retro to see what can be improved in the next few iterations. Send an email to the whole company with what % of the sprint work was done (goal is >80%), what goals were hit, what goals were missed and why.
    49. **Owner: **Engineering Manager (as a coach/facilitator)
    50. **Participants: **VTL, eng-team, PM, Designer (all required)
    51. **How**: synchronous, 1 hour. 
    52. **Timing**: Monday morning PST, or Friday morning PST if Monday is a holiday, before the next Sprint starts.
    53. **Why**: this is probably the most important part of the process: it drives accountability and learning. However, a sprint report/retro doesn’t make sense if (a) goals were not clear and (b) people were not committed to hitting those goals. That is why all the previous steps exist. But all the steps before, without this step, don’t create great teams. **An engineering manager is responsible to drive this meeting because they are independent of the delivery team, yet responsible for winning and increasing their engineers’ capacity to win**. 
10. Product Release
    54. Staging release is approved and moved to Master.
    55. **Owner: **on call (rotating)
    56. **How**: TBD
    57. **Timing**: Tuesday afternoon, after customers are less likely to be using the product.


# Additional Process



* 6-week Cross-functional Retrospective
    * All of Product Engineering meets with stakeholders to share top 3 issues preventing us from shipping faster.
    * **Owner**: Head of Engineering + Head of Product
    * **Participants**: all of PM + Product Engineering
    * **Timing**: every 6 weeks (mid-quarter, end-of-quarter)
* Monthly Product Roadmap Review
    * Product provides visibility into the next ~3 months.
    * **Owner**: Head of Product
    * **Participants**: all of PM + eng leads
    * **Timing**: monthly
* Monthly Demos!
    * Engineering provides visibility into cool stuff that has been built, shipped, conceptualized, whatever! We will have a prize for the **best demo** and for the **best presentation!**
    * **Owner: **Head of Engineering
    * **Participants**: everyone!
    * **Timing: **monthly


# Metrics To Track

REDACTED will start paying attention to the following metrics on a quarterly basis. After we’ve done this for a quarter or so we’ll start to set targets.



1. % of sprints started on-time (no later than Tuesday afternoon).
2. % of sprints with >80% story points achieved
3. % of sprints that had scope changes >10%
4. % of delayed/rolled-back releases (don’t make it out by Tuesday evening)
5. Length of raw backlog (# of tickets)
6. Length of story-pointed backlog (# of sprints)
7. What else?


# FAQ



* Q: How do we release?
    * A: Every 2 weeks (or every week, if the team wants to do “bug-fix releases”). **We are not going to be releasing ad-hoc; if you miss a release, you have to wait to get your feature out until the next release.**
* Q: 


## Open Discussion Topics: 7/26 Notes



1. Completeness of the Product Plan before execution: is Doxel going to have well-thought-out products we build ahead of time, or do we want to iterate & learn quickly?
    1. REDACTED: 70/20/10. 70% should be “well-defined”, sprint-over-sprint, iterating on products, etc. 3-month roadmap, 6-month horizon, etc. 20% is “good idea we think will work.” E.g. quality with GCs. Might iterate a bit randomly. 10%: totally crazy, e.g. “bank for GCs”, very experimental. All startups start with 100% in the 10%, as PMF improves they transition. We are probably 50/50 right now. 
    2. REDACTED: good summary. Not a place where everything is designed upfront. There is a mix of sure-bets vs experimental. 
    3. REDACTED: still driven by product team? Or some of it driven by engineers? REDACTED: what are the metrics where we know which 50? Who is keeping track?
    4. REDACTED: **each category** some work should be driven by eng. Always tech debt, bugs, architectural overhauls, etc. 20% category is unique - we do real R&D, that might not work. REDACTED & REDACTED’s pano overlay may just not work. 
    5. REDACTED: how will we know which category something falls into?
    6. REDACTED: Product team is evolving, most of us are new, new VP of Product. Roadmap, planning up-front, once we have a VP he’ll help the Product Team  categorize it, etc. Definitely we will be working on this. 
    7. REDACTED: we’ll ideally spend more time on 70% as Product/Design team focuses on 10%.
    8. REDACTED: when we have a good sense of what we need to do / how we need to do it, it goes to 70%? 
    9. REDACTED: it’s not about the readiness state of a story… It’s about the certainty of success. 
2. Scrum master: Separate role, or a hat someone wears?
    10. REDACTED: I’ve seen a dedicated scrum master, or the Dev lead. They are in it, help teams unblock deps.
    11. REDACTED: I’ve seen teams rotate it. Give everyone a chance to learn some skills around planning. Often some people hate it, some people love it.
    12. REDACTED: I haven’t had a great experience with people who are *not* part of the team.
    13. REDACTED: haven’t seen a dedicated scrum master either. Is it a full-time job? 
    14. REDACTED: you start with the EM being the scrum master. Once you identify someone who wants to try it, it’s a good way (low risk) for an IC to try.
    15. REDACTED: I’ve seen a dedicated program manager. Usually the EM or main TL does it.
    16. REDACTED: let’s walk-through the roles and see what the Scrum Master is doing. AFAIK he takes notes, 
    17. REDACTED: I’ve worked with one, they enforce the process. They make sure obstacles are handled, managed. They own the retros, notes, tracking the goals for the sprints, etc. They facilitate the conversations across the teams, horse trading, etc. And tracking all the metrics - sprint velocity, etc. If you have separate people - you don’t have a joined process. Nobody wants to do it across all the teams. 
    18. REDACTED: scrum master is across all the teams to get the unified level of visibility. Help unblock team across teams. This takes time away from the core job. 
    19. REDACTED: does this separate product management from project management? I’ve seen Product people do a lot of this, with some of the load on the tech lead?
    20. REDACTED: they help enforce / standardize the process across all teams. 
    21. REDACTED: since there are cross-functional meetings, a single manager wouldn’t be able to do it.
    22. REDACTED: what about self-managed teams that report out?
    23. REDACTED: release manager + project manager knows when things are going out, plan out QA, other efforts, etc. That works in the bigger companies. When you have a QA org.
    24. REDACTED: we are too small for that.
    25. REDACTED: what do we do in the short-term? 
    26. REDACTED: we can split the responsibility. Product Manager + eng lead should split the responsibility. 
    27. REDACTED: in my mind, the PM should be responsible for refining + planning what goes into the sprint. Eng brings eng initiatives. Mid-sprint dep management should reside with the tech lead. 
    28. REDACTED: are folks comfortable with VTL being responsible for “Scrum Master”?
    29. REDACTED: grooming/planning meeting - tickets are the result. But there should be a Goal Doc - what we aim to achieve. I don’t need copious notes, it should be in the ticket. 
    30. REDACTED: Goal Doc is not big. Just a few lines. 
    31. REDACTED: who owns reporting?
    32. REDACTED: Eng Managers own reporting + retros. 
    33. REDACTED: goals will need to be 
    34. DECISION: thumbs-up with current proposal.
3. Sprint meetings: do we have Refine/Review meetings, or one big Sprint Meeting?
    35. DECISION: two meetings
4. QA/testing strategy: who is responsible for what?
    36. FOLLOWUP
5. Story pointing: How do we do this?
    37. REDACTED: we need some rules that are consistent across teams
    38. REDACTED: we do need alignment on bugs, is it time or effort or complexity? 
    39. AI(REDACTED): write up a couple of paragraphs explaining what we are trying in the next ~month.
6. WHEN DO WE START?
    40. REDACTED: sooner is better. Won’t be perfect the first time. 
    41. REDACTED: 2 weeks from now. 
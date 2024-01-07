# 30-Day Objective

Have a **technical strategy **and **engineering execution plan** that allows Doxel to scale up to **X customers**, with
**X Doxel Cores each**, and turn around scans in X hours, by Dec. 1st 2019. Strategy and plan will have buy-in from
leadership (CEO, CTO, Sales, etc) and engineering leads (TBD) by May 31st, 2019.

## Reasoning

Doxel’s 2019 Company Plan lays out having X signed customers across X construction domains ([REDACTED]), with X of those
customers spending $1M/year or more. 2020 goals will be $XM-$XM in revenue.

With current pricing we need to process 1 Doxel Core (150ksqft/week) for ~$XK in revenue.

To hit plan, we need to process about X Doxel Cores weekly by end of 2019 and X Doxel Cores by end of 2020. We want to
remove the **engineering bottlenecks **so can we be sales-bound and have engineering focus on future products, hence the
goal of supporting ~X Doxel Cores by EOY. We also assume that there will be significant overhead per customer (and
possibly customer/site), hence the specific goal of X customers x X cores each (rather than generically X Doxel Cores).

The plan will include:

* Major architectural components and when they will roll out
* Significant scale/pressure tests we will run to certify our tech works
* Major technology risks and how we will de-risk them
* Major non-technology risks and how we will de-risk them
* Engineering hiring needs (+ possibly a plan)
* Estimated $$$ spend (make sure we are in-budget through 2019)

# 30 Day Onboarding

## Week 1: Understand Team & Operations

* People: do a listening tour [15 hours]
    * Initial 1:1s with all engineers. [MOSTLY DONE]
    * Initial 1:1s with [PEER], [PEER], [PEER], other partners. [DONE]
* Strategy: meet current customers [6 hours]
    * Shadow [CUSTOMER] Weekly Status. Write up thoughts. [DROPPED?]
    * Shadow [CUSTOMER] Weekly Status. Write up thoughts. [DROPPED?]
    * Shadow [CUSTOMER] scanning. Write up thoughts. [IN PROGRESS]
* Execution: watch how team operates [4 hours]
    * Shadow sprint planning and standups. [DONE]
    * Review all JIRAs for the week. [DONE]
* Technical [10 hours]
    * Architectural deep-dive [[CTO], other eng TBD] [DONE]
    * Review all PRs for the week. No comments, just shadow. [DONE]

## Week 2: Understand Technical Challenges

* People: go deeper in their current work [10 hours]
    * Set up 1:1 cadence with every engineer. Default to 30 min weekly. Focus on learning what they are doing and how
      the technical stack works at first.
    * Review hiring pipeline + philosophy with [PEER]. Understand what metrics we track and how we are doing at various
      parts of the funnel.
    * Deliver 1 “early win” identified in Week 1
* Strategy: understand what we are selling [10 hours]
    * Shadow [PEER] on 3-4 customer pitches/early pilot updates.
    * Shadow [PEER] on 3-4 engineering pitches to see what gets people excited.
    * Review “pitch deck” with [CEO]  (VCs + customers). Understand how he hooks customers.
* Execution: start iterating on a better approach [5 hours]
    * Propose & experiment with improved execution cadence (if it needs it).
    * Review all JIRAs for the week and understand roughly why they exist.
    * Get key metrics on each part of our data processing pipeline: failure rates, processing times, etc. Start tracking
      daily (weekly?) if not already tracked.
* Technical: get my hands dirty [20 hours]
    * Get ramped up on the FE codebase. Edit, build, deploy cycle.
    * Get ramped up on the analytics pipeline. Edit, build, deploy (at least part of it; cropping or something else).
    * Shadow end-to-end scan-to-final-report process. Write up thoughts on the challenges.
    * Review all PRs for the week. Comments for learning purposes.
    * Identify 1-2 most important technical areas for me to ramp-up on.

## Week 3: Draft Technical Strategy

* People: push on technical disagreements [20 hours]
    * Work with key engineers on the technical strategy (where we are today vs where we want to be in 6 months).
    * Draft hiring plan (w/[PEER]) for key roles, by location/seniority/diversity/etc. Review with engineers, make sure
      it holds water.
    * Start doing phone screens (&lt;5 this week)
    * Deliver 1 “early win” identified in Week 1.
* Strategy: understand the big picture so plan is compatible [[CEO]/[CTO]?] [5 hours]
    * Competitive analysis: who are our main competitors? Where are they strong and we are not? Where do we have
      advantages? How does this play into our technical strategy?
    * Differentiation analysis: what are the top tech priorities that will entrench us technologically?
    * Financial analysis: how should we invest our warchest? Remote vs local employees? Junior vs senior? [[CEO]/[CTO]]
    * Shadow [PEER] on another ~3 customer calls
* Execution [5 hours]
    * Hold first team retro on execution. Come up with improvements we can do over next 2-4 weeks.
    * Review all JIRAs for the week and be able to roughly prioritize importance.
* Technical [10 hours]
    * Ramp-up on #1 technical priority from last week.
    * Run end-to-end scan myself (if possible)
    * Review all PRs for the week. Start pushing back on changes that don’t make sense.

## Week 4: Finalize Technical Strategy + Plan

* People: get alignment on plan [20 hours]
    * Work with key engineers on strategy → plan that we have 90% confidence in.
    * Finalize hiring plan with [PEER]  (philosophy, process, etc). Start pitching to the team (any changes).
* Strategy: get leadership alignment on 6-month eng plan [10 hours]
    * Get thumbs-up from [CTO] & [CEO] on technical strategy + plan
* Execution: firing on all cylinders [5 hours]
    * Review all JIRAs for the week and be deciding what is in/out.
    * Staff meeting, sprint planning, standups - all feel smooth and the most important work is happening, predictably,
      with the right amount of quality.
* Technical [5 hours]
    * Ramp-up on #2 technical priority from last week.
    * Review all PRs for the week. Up-level team skills where it makes sense.
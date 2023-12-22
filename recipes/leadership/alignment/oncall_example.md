# Background
In 2019 when I joined [COMPANY] we did not have any on-call process or culture. Once I felt it was appropriate to improve this part of our organization/process I wrote this doc to align the whole team to the direction I wanted to take us.

## Overview

This document explains the _purpose_ and _process_ of an **oncall rotation** for [COMPANY] teams. It is intended for engineers not familiar with being oncall and the expectations that come with it. While it borrows heavily from oncall experiences at other internet companies (Google, TellApart, Twitter), [COMPANY] is a unique company due to the heavy exposure to outdoor and indoor physical conditions (through rovers, drones, etc). Discussion is encouraged so that we achieve our objective: frequent, complete reports of construction site progress.


## Why On-call?

Companies that provide online services to customers have an added complexity to just writing the software: they must also guarantee that the service is _available_. As software migrated from “purchase the box and figure it out” to “access the service whenever you want”, the burden of ensuring everything works transitioned to the company building the software. As the number of users grew into the billions the support costs for keeping the lights on could no longer scale linearly - the cost would be prohibitive. Thus Site Reliability Engineering was born as a discipline to build reliable software: products and systems that required minimum human intervention to function. 

A much more thorough description of this discipline is captured in the [Site Reliability Engineering](https://landing.google.com/sre/sre-book/toc/index.html) book and is recommended reading for everyone. At minimum, we recommend reading the [Being On-Call](https://landing.google.com/sre/sre-book/chapters/being-on-call/) section and PagerDuty’s [article on the subject](https://www.pagerduty.com/resources/learn/call-rotations-schedules/).

Most simply, on-call is needed when an interruption of the service or product would lead to great harm to the company (financial, reputation, legal, etc). The individuals on-call are the “last line of defense” and should be notified of impending doom before it happens (or, as a last resort, as soon as the issue is discovered in production). They then must work tirelessly to resolve the issue to minimize the company’s exposure to risk. This often means being woken up in the middle of the night, working nights and weekends, and interrupting project work. 

Clearly, on-call should not be taken lightly. It should _never be used_ for non-critical services or problems: that burns out engineers and reduces their responsiveness level on real fires. That means who is able to trigger on on-call is usually controlled and minimized; for example, generally customers cannot trigger on-call pages. The best teams have fully-automated detection systems that have high signal-to-noise ratios which trigger on-call only when software is not able to self-correct.

Because on-call engineers are only tackling the hardest problems, there is usually a high bar before a team lets an engineer enter the on-call rotation. The engineer needs to be fully comfortable waking up in the middle of the night and fixing 90% of issues that might be paging them (it is acceptable to occasionally get stuck and fail-over to another engineer). This means that all the engineers on the on-call rotation need to be familiar with _all the systems_ that are being monitored. Hence:



1. Services covered by on on-call rotation need to be carefully considered. A “kitchen sink” on-call rotation that has all services guarantees that engineers will not really be able to solve problems when something goes wrong. Services need to be bundled together logically, and this drives sub-teams and ownership.
2. Engineers need to be trained across all the services in the on-call rotation. That means some training before they go on-call (ideally by working within each code base directly), good documentation for each system, and solid runbooks that explain what the most likely issues might be when the pager goes off.
3. Engineers need to commit to the response-times that the on-call rotation demands. Different on-call will need different speeds of response; e.g. if our website is down while customers are using it we may have &lt;15 minutes to respond, whereas if our data pipelines are broken we may have ~hours to respond. Engineers must understand what is expected of them and be available when on-call to meet those response-times. This usually has a personal-life impact (e.g. no going offline during the weekend) that needs to be factored in.
4. As such, on-call rotations can’t be too small or they can burn-out engineers. 4 people is usually the minimum, with 6-8 being a good size. 10+ starts being too large because engineers forget what they need to do when on-call after 2 months of no practice.


## Why Does [COMPANY] Need On-Call?

[COMPANY] has 3 distinct pieces that may need on-call support.


### In-field Data Collection

Our rover and drone operators in the field have short windows where they can capture data. While today we may have several days to go back on-site in case something goes wrong, as we scale and move to daily scans per site we’ll have very little room for error. Our customers will require daily scans and data 48 hours later (then 24, then 12…) so having a reliable data collection platform and process will be key.

Data collection can fail for multiple reasons: human error, incorrect field set-up (markers, control points, etc), hardware issues, and software failures. We’ll need to build software systems into our data collection platforms (especially rovers) to minimize failures and alert when we might need engineering or central ops support. We’ll also need a team of experts available via phone to debug software and hardware issues remotely.

Today, [EMPLOYEE] and [EMPLOYEE] play this part directly. As the team is small, and the number of production sites is small too, we can continue with a single support contact for the time being. As we grow to 10+ sites we’ll likely need 2-3 people and then set up the on-call rotation.


### Data Pipeline

Once our data is collected we have strict SLAs (Service Level Agreements) to produce data. Our contracts currently specify 5 days (120 hours) and we are likely to tighten that by ~10x (down to 12 hours eventually). Many parts of our pipeline require large amounts of time (~hours) and, if they fail, need re-processing.

As our pipeline replaces our Ops team in production we’ll need to set up on on-call rotation to guarantee that our data never gets ‘stuck’. Failures could come from bad data due to collection issues, bugs in our code, hardware/software failures on our Cloud stack, and many other reasons. On-call engineers will need to be trained on finding the root cause of the issue and kicking the pipeline to get it going again so we hit our customer SLAs.


### Customer Interface

[COMPANY]’s customers have access to their data via our Web interface today, and maybe other methods tomorrow. Because our customers are Fortune 500s and paying $M for the product they expect very high levels of service from [COMPANY]. Our customer interfaces need to be and functional a very high percentage of the time. We don’t have millions of billions of users logging in daily so small failures for a few users isn’t acceptable to us.

Most importantly, the data on the dashboard has to _be complete and right_. Customers won’t know why it isn’t and won’t care who’s fault it is. That means the team responsible for all customer outputs needs to _feel responsible_ about the entire stack below - the data pipeline and even data capture - because they are our last folks at the company preventing us from embarrassing ourselves. 


## On-call Process By Team

On-call should be defined by each team.


### Ops

Not needed yet. This will be figured out once our ops needs are much higher.


#### SLAs


#### Services In-Scope


#### Services Out-of-Scope


#### Oncall Responsibilities/Expectations


#### Oncall Training & Onboarding



* Runbook: 
* Shadow process: 


#### Oncall Rotations



* Handoff process:
* Engineers:
* Rotation length:
* Swapping/exceptions process:
* Holiday coverage:


#### Expected Challenges


### Analytics


#### SLAs


#### Services In-Scope


#### Services Out-of-Scope


#### Oncall Responsibilities/Expectations


#### Oncall Training & Onboarding


* Runbook: 
* Shadow process: 


#### Oncall Rotations


* Handoff process:
* Engineers:
* Rotation length:
* Swapping/exceptions process:
* Holiday coverage:


#### Expected Challenges


* Everyone will need to be familiar with matcher, cropping, SQL, etc - enough to debug it when things go bump at night.


### Web


#### SLAs

P0

* Dashboard down/Not reachable
* Incorrect/Stale data on the dashboard
* Changes impacting a client demo success required within 4 hours
* Discovered security vulnerability/breach.
* Major bug skewing data/numbers.

P1



* Production errors (view or logic) that don’t crash the dashboard

P2



* Cosmetic changes.
* New features
* Feature enhancements
* Minors bugs/edits

Commitment

P0 - To be acted on immediately a ticket is filed.

P1 - To be completed within 24 hours after a ticket is filed

P2 - To be handled as soon as we can, but no pressure.

Communication during bugfix:



* Acknowledgement
* Statement of the problem (after research) + ETA to solution
* Solution
* Notice of Deployment of the solution
* Confirmation from the reporter to complete the loop

Communication modes

P0 - #rincon-dev and email to all devs in [COMPANY]. Hourly status update on JIRA.

P1 - #rincon-dev. Daily status update on JIRA.


#### P2 - #rincon-dev. Ad-hoc status updates on JIRA.


#### Services In-Scope


#### Services Out-of-Scope


#### Oncall Responsibilities/Expectations


#### Oncall Training & Onboarding



* Runbook: 
* Shadow process: 


#### Oncall Rotations



* Handoff process:
* Engineers: REDACTED, REDACTED, REDACTED
* Rotation length: 1 week
* Swapping/exceptions process: 
* Holiday coverage: 


#### Expected Challenges

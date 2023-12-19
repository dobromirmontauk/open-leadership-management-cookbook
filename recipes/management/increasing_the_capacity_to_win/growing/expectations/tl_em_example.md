# Background
I had a conflict between one of my very senior ICs and the EM on the team. They couldn't agree on their roles & responsibilities so I ended up writing this to try to delineate expectations clearly.

# Contents

Our Product Engineering team has grown. We now have XX individuals (EMs included) and our architecture is quickly becoming more complex.

We’ve split the FE/BE engineers horizontally across two managers (REDACTED and REDACTED) in order to keep similar skill-sets together. This should make it easier to hire, train, and retain developers, as their managers are more closely aligned with their core skill set. For execution purposes, we are following the Vertical Team structure which requires members from across the company to execute together. While theoretically nimbler (we can form / dissolve vertical teams as-needed), in reality this can lead to chaos and poor software if not done carefully.

The major risks:



1. Lack of cohesive architecture across FE/BE, as each horizontal team optimizes for itself and each vertical team optimizes for speed-to-market.
2. Lack of best practices across vertical teams, as they are formed/dissolved. We get a different standard per vertical team depending on the lead/members.

An [über-TL](https://github.com/dobromirmontauk/engineering-scorecards/blob/master/uber_tl_scorecard.md) can help mitigate those risks. REDACTED will be our first über-TL at Doxel. Since the role is well-defined in that link, this doc describes the intersection between REDACTED’s role and others on the Product Engineering team.

über-TL responsibilities:



1. Default approver on all TDDs. REDACTED can (and should) delegate this whenever possible, but he is ultimately responsible for all the technology decisions on the Product Eng team.
2. Default owner of APIs and SQL schemas. This is the highest-leverage work that an über-TL can pay attention to, to make sure that the overall architecture fits the plan. All changes should be reviewed by REDACTED until he trusts others and can delegate to them.
3. Default owner on technical best-practices. REDACTED should be working actively to improve our testing culture, release processes, code review practice, etc. He will likely have to lean heavily on EMs here to actually implement on their teams while he owns the overall Product Eng KPIs.
4. Drive one critical project: to stay hands-on-keyboard, REDACTED should pick one high-leverage project to drive (be the FL). This could be a Product Core project, if he believes it can help improve productivity significantly, or an actual Product initiative if it will help him understand the technical requirements more deeply.
5. **Final Product Eng tie breaker**. If FE/BE (REDACTED/REDACTED) can’t agree on a decision (quickly), REDACTED will make the call, or escalate to Dobromir if needed. 

EM responsibilities:



1. Coaching, mentoring, and motivating employees. From code-level (i.e. code reviews), to design, communication, etc. EMs #1 job is to increase their team’s capacity to win, by helping each of their engineers do better work. This can be several hours per employee per week, e.g. 30-60 min 1:1 + reviewing JIRA, PRs, written docs, plans, etc.
2. Hiring. Improving the hiring process, training interviewers, doing HM calls, etc. If actively hiring, this should be ~5 hours/role/week. (Note: REDACTED should be the default Top Grader to ensure consistency across the team). 
3. Horizontal team building. Creating a culture of excellence across the horizontal domain. Actively encouraging learning from peers, discovering common problems (and solving them), etc.
4. Resourcing decisions. Working with PM, REDACTED, and Dobromir to decide what projects to staff, when to hire, etc. 
5. Vertical team shepherding. To be more closely aligned to actual Product deliverables, each EM should have a vertical team they “shepherd”. If they have a FL on that team they can delegate most of the work to the FL, but they still own the V-Team hitting their goals. They decide what to keep / what to delegate to FL depending on that individual’s interests + abilities. Each EM should be shepherding at least 1 V-Team so they have skin in the execution game (#win).

FL responsibilities:



1. Should be well-documented [here](https://github.com/dobromirmontauk/engineering-scorecards/blob/master/fl_scorecard.md). FL are a way for EMs to increase their leverage while growing their engineers’ leadership + technical skills. EMs should be deploying FLs whenever possible for their V-Team projects so they can run multiple V-Teams in parallel and grow themselves. Responsibility still flows up to the EM. 
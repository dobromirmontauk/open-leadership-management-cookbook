# Winning, and Increasing the Capacity to Win

*A stick-figure talk about the two halves of an engineering manager's job.*

Wade Chambers says a manager has two jobs: win, and increase the capacity to win. That sounds like nothing, so this talk makes it concrete with the dumbest possible analogy: moving a huge pile of bricks from A to B. It defines both halves, shows why they fight over every hour of your week, and then walks through ten tools for each.

See also: [Winning](../winning/) and [Increasing the Capacity to Win](../increasing_the_capacity_to_win/) in the Cookbook. The working outline is in [outline.md](outline.md); the slide sources, images and image prompts are in [source/](source/).

Copyright Dobromir Montauk 2026.

## Slides

### Slide 1

**Engineering Management 101.** A deliberately boring corporate title slide.

> Deliver it with a completely straight face, like the start of every training you’ve ever sat through. Let the pause run a beat too long.

### Slide 2

**The Job of an Engineering Manager:** 1. Winning. 2. Increasing the Capacity to Win. (Also deliberately boring.)

> Read it flatly. This is literally the whole talk, and it sounds like nothing. Ask the room what it actually means. Wait. Nobody will answer.

![Slide 3: Stick-figure seminar: one audience member asleep, one on a phone, one with a big question mark, while the pointy-haired Manager points at a dull slide titled Winning and Capacity](slides/03.jpg)

> Admit it: I wrote that slide and I’m not sure either. “Winning” and “capacity” are words we nod along to in meetings. By the end of this, you should be able to use them to make a decision on Monday.

![Slide 4: Hand-lettered title Stupid Simple Analogy surrounded by hand-drawn bricks](slides/04.jpg)

> A stupid simple analogy. Let’s make it concrete with the simplest job imaginable: bricks. 
>
> (yes, because it is so stupid-simple, it won't map 1:1 with our jobs. That shouldn't prevent you from getting the lessons)

![Slide 5: The CEO hands the Manager a note reading Move the bricks to B; the Manager sweats and gulps next to the giant brick pile marked A](slides/05.jpg)

> Every EM gets some version of this note, usually with less detail. You have to build the team, and the technology, to get it done. Why bricks? Shipping features isn’t that different: units of value, hauled to a customer who’s waiting at the other end.

![Slide 6: The Manager stands next to an enormous pile of bricks marked A, scratching his head; a tiny flag marked B sits far away on the horizon](slides/06.jpg)

> Notice what nobody told you: how big B is, how far away, or what’s in between. Every one of those unknowns is going to bite us later. Hold that thought.

![Slide 7: Same seminar room, now everyone is paying attention: the Manager points at a screen reading Winning: how many times how far, with a sketch of three people carrying bricks from a pile to a flag](slides/07.jpg)

> A win is one turn: one week of engineering. Both factors matter. A thousand bricks moved sideways scores zero; one brick delivered all the way counts. Ask the room: by this measure, what did your team win last week?

![Slide 8: Day 1: nice start! The Manager, sweating, gives a thumbs up next to a stack of 3 bricks moved 10 meters from pile A; B is still far away. Caption: +3 bricks × 10m = 30 MoBs (meters of bricks)](slides/08.jpg)

> Celebrate it: it’s a real, measurable win. Then do the math out loud. How many bricks are in that pile? How far is B? Let the room get a little uneasy.

![Slide 9: Seminar room, everyone sweating: the screen titled Time Pressure shows a straight burn-down of remaining MoBs at 30 MoBs per day, reaching zero at 300 days, well past the red deadline line](slides/09.jpg)

> If ALL the bricks don’t arrive by date X, all that winning is worthless. Keep Day 1’s pace forever and we finish in 300 days; the deadline is months before that. This is the moment winning alone stops being enough.

![Slide 10: Same seminar room: the Manager points at a screen reading Increasing capacity, value equals impact over (1 + r) to the power of time, above a time arrow with a wheelbarrow of bricks (2×), a truck of bricks (50×) and a faint dashed rocket full of bricks (10,000×)](slides/10.jpg)

> Capacity is everything that doesn’t move a brick this week but lets you move more later: tools, roads, people, skills. Why discount? Because the future is uncertain. The truck might take two years; the Starship may never fly. With any real discount rate, the moonshot has to be enormously bigger to beat the wheelbarrow. The skill isn’t picking the biggest number; it’s picking the best impact for the time.

![Slide 11: Same seminar room, now mostly relieved: the screen titled Time Pressure shows capacity and number of bricks curving up exponentially while remaining MoBs curves down faster and faster, reaching zero just before the red deadline line, labeled Just made it](slides/11.jpg)

> Same deadline, same pile. What changed is capacity: better tools, more people, more bricks per trip, and it compounds. That’s how you beat a deadline you can’t beat at today’s pace. But “just made it” isn’t comfortable: one more surprise and we’re back on the scary slide.

![Slide 12: These are in tension! The Manager scratches his head at a whiteboard with two columns. Win: carry bricks, clear the road, unblock a teammate, check in with customer. Increase capacity: interview a hire, train the new guy, build a wheelbarrow, career 1:1. A wall clock shows 4 o’clock; he thinks: one hour...](slides/12.jpg)

> There’s no answer that’s always right. Some days the bricks have to move. Some days the best thing you can do is train the new guy. Every hour on one side is an hour not spent on the other. The rest of this talk is about making that call well, every hour, every day.

![Slide 13: How to win: ten tiles with the Manager. Aim: holding up a picture of a finished brick house next to flag B. Trim: cutting the brick pile in half with giant scissors. Scout: binoculars at a fog bank. Decide: pointing down one fork of the road. Assign: handing out a hard hat while three engineers swarm a huge brick. Steer: pointing a wheelbarrow toward flag B, with flags C and D in the distance. Clear & Protect: chopping a fallen trunk off the road while bandits drag an engineer into the forest beh](slides/13.jpg)

> Each of these can be a whole course by itself. We're just going to lightly touch each one & give some examples so you can pattern match your activities to the bucket they fall into.

![Slide 14: Aim. The team happily carries bricks to the right, toward an empty hole signed B (Monday). Footprints from that hole make a big U-turn: up past B (Tuesday) and B (Wednesday), then all the way back left, where the customer is planting the real B flag behind the team. A doodle up top: a solid arrow right, WHAT WE CARRIED; a dashed arrow left, TO THE REAL B; MoBs THAT COUNT: < 0.](slides/14.jpg)

> Goals move all of the time, for lots of different reasons. The work your team is does only matters if it takes you *in the direction of the goal* -- so even if you are a little off-track, you are wasting effort. Figuring out what is the actual goal will help THIS WEEK's work be maximally productive.
>
> 1. The feature for a deal that died. A team spends six weeks building a custom integration for a big prospect. The deal falls through. Nobody else wants the integration, so it sits in the codebase as a cost.
> 2. Built to someone else's understanding. The PM passes along what sales heard on a call. Engineering builds exactly that, but the customer meant something else, so it gets rebuilt. The first version was the passed-down scope, not the real one.
> 3. Polishing what's about to be replaced. Three weeks go into speeding up and hardening a service that leadership already plans to replace next quarter. Nobody told the team, and all the work dies with the old system.
> 4. Building on the API the customer is leaving. The team ships an integration against a vendor's v1 API, then learns the customer is migrating to v2 (or to a different vendor) next month.
> 5. Two teams, one problem, opposite directions. Two teams each build their own version of the same thing, like an auth library, a reporting pipeline or a config system. One version gets thrown out, along with the time spent arguing over which survives.
> 6. Gold-plating the prototype. A spike meant to answer "will this work?" gets tests, a CI pipeline and a nice UI. Then the answer comes back no.
> 7. The right feature for the wrong user. A powerful configuration screen gets built for admins, but the people who actually hit the problem are front-line staff, who never open that screen.

![Slide 15: Trim. Right: the customer's bubble shows a huge fairy-tale castle; the Manager answers with a bubble showing a small simple house. Left: two engineers kneel, assembling a wheelbarrow from parts and a blueprint next to an untouched brick pile, while the same Manager says Just carry the damn bricks.](slides/15.jpg)

> Two kinds of scope to cut. Product scope: what the customer asked for vs. what they actually need this quarter. Approach scope: the framework, the platform or the automation we would love to build first. Building tools is capacity, not winning, so do it on purpose, not by accident.
>
> Examples:
> 1. Product scope. The customer asked for a full analytics dashboard: filters, charts, scheduled emails. The question "what decision is this for?" turned up one weekly number for the CFO. A nightly CSV export shipped in two days.
> 2. Product scope. The spec said "supports every payment type". The data said 97% of transactions were cards. Launch with cards, a month early; add the next type when a real customer asks.
> 3. Product scope. The plan included a full admin UI for config, roles and audit logs. The only users were three internal engineers. A documented script and a config file in the repo did the job and saved six weeks.
> 4. Approach scope. A request for one flag on one machine turned into a design for tiered config with merge rules and a new admin UI. Someone asked, "any objection to the hackiest possible approach?" A one-off override solved it that day.
> 5. Approach scope. An engineer wanted a generic plugin system first, so integrations would be "easy forever". There was one integration on the roadmap. Hard-code it; build the abstraction from three real examples later, not zero.
> 6. Approach scope. Support wanted an edge case automated before launch. How often does it happen? About once a week. Keep it manual for now, and launch.
> 7. The other side. A simple database index was suggested early and passed over because the tests weren't representative. Seven weeks later, under production load, the same index took the query from 4.5 s to 0.7 s.
>
> Caveat: a trimmed feature still has to be usable. Phase 1 can be manual, but call it a partial feature, not GA. "Done" means what the customer expects.

![Slide 16: Scout. A hand-drawn top-down map of a forest. Three roads start at the bottom middle: the left one winds into the mountains and ends at an X; the middle one goes straight up and ends at an X; the right one loops around, crosses the river on a small bridge and reaches flag B at the top. At the fork the Manager points up the right road, This way!, and a line of engineers carries bricks along it.](slides/16.jpg)

> Before you commit the team for a month, spend a few days finding out which approach dead-ends.
> - Spike the vendor or POS API for two days before promising the integration date: auth quirks, rate limits, missing endpoints.
> - Prototype the hard part first (latency, the hardware constraint, the model accuracy), not the easy UI.
> - Ask who tried this before. The team that attempted it last year knows where it broke.
> - Read the customer's actual setup (network, hardware, existing POS) before estimating.
> Send one engineer for a few days, not the whole team for a sprint. The obvious approach is often the one nobody has taken end to end.

![Slide 17: Decide. At a fork in the road, two engineers holding bricks argue: one points left into a dark forest, FOREST!, the other right up the mountains, MOUNTAINS! Between them the Manager calmly points up the mountain road: MOUNTAINS. GO. Nearby, a big untouched pile of bricks, and four engineers sitting on the ground eating popcorn, watching the argument instead of working.](slides/17.jpg)

> Teams lose days, sometimes weeks, waiting on decisions nobody owns. The cost isn't the two people arguing; it's everyone blocked behind them.
> - Two senior engineers debate the data model for two weeks while the rest of the team can't start.
> - A design review ends with "let's take this offline" for the third time.
> - A PR sits blocked on an architecture argument in the comments.
> - "Which customer first?" goes unanswered, so people pick their own.
> Most technical decisions are reversible. Set a deadline for the decision, hear both sides, make the call, write down why, and revisit if new data shows up. Disagree and commit.

![Slide 18: Assign. Four specialists stand in a row: a truck driver with a steering wheel and keys, a strong guy flexing with a tall stack of bricks on his shoulder, a bearded lumberjack with an axe, and a scout with a hat, backpack and walking stick. The Manager faces them, hand on chin. His big thought bubble shows them all at work on one road: the scout leads through the forest, the lumberjack clears trees, the truck drives a load of bricks, the strong guy carries a huge stack. In the bubble: 10x!](slides/18.jpg)

> Engineers aren't fungible. The person who knows the payment stack fixes the payment bug in a day; someone new to it takes a week.
> - Your best debugger goes on the production incident.
> - Your best communicator goes on the customer-facing integration.
> - Your fastest prototyper takes the spike.
> - Watch for assigning by "who's free" instead of "who's best for this".
> When one task blocks everything (the release, the P0 bug), swarm it. The tradeoff: always picking the expert creates hero dependency. Spreading knowledge is capacity, and it comes later in the talk.

![Slide 19: Steer. Three flags in the distance, B, C and D, each with a customer yelling: 100 MONDAY! at B, 50 FRIDAY! at C, 10 TUESDAY! at D. In front, the Manager stands where three paths fan out, arms spread: one points an engineer pushing a wheelbarrow full of bricks toward B, the other points an engineer carrying a small stack of 10 bricks toward D. The path to C is empty for now.](slides/19.jpg)

> Three customers, three deadlines, and each one is sure they're the priority. Your job is to turn the noise into an order: value, deadline, size.
> - The big launch due Monday gets most of the team.
> - The small fix for a key account due Tuesday gets one engineer, so it ships and is off the board.
> - The Friday request waits on purpose, and you tell that customer explicitly, with a date.
> Spread the team across all three and everything ships late. Re-check mid-week: did priorities change? Did sales promise something new?

![Slide 20: Clear & Protect. The Manager, sweating, chops through a fallen trunk across the road (THWACK!) while two engineers with bricks wait. Behind him, two masked bandits saying Quick favor? and Just 5 min! drag a third engineer, crying Help!, into the forest. Nobody on the road notices.](slides/20.jpg)

> Two kinds of obstacles.
> Blockers you can see: waiting on another team's API, missing access or credentials, a flaky CI pipeline, a decision nobody has made. Chasing these down is visible and feels great.
> Distractions you don't see: the "quick favor" from sales, the exec who needs "just 5 minutes" every day, an extra interview loop, the side project someone pulled your engineer into. They take your best people one at a time.
> Ask in 1:1s where their time actually went last week, and compare it to the plan. Then say no on their behalf.

![Slide 21: Motivate. The Manager stands on a crate, arms wide, telling a story; his speech bubble shows a huge fairy-tale castle surrounded by dollar signs and money bags. Two grinning engineers grab bricks from the pile at his feet; three more run to the right, away from him, with bricks in their arms. Far away at the end of the road: a small wooden shack next to flag B.](slides/21.jpg)

> People work harder on things they understand and care about.
> - Bring an engineer to a customer site to watch the product being used.
> - Share the real number: the revenue, the customer count, the deal this unlocks.
> - Connect the project to their career: this is the scope that gets them promoted.
> - Celebrate the ship publicly and name who did it.
> But don't oversell. If the "company-changing" launch turns out to be a pilot at one site, the next pitch lands flat.
> Overtime lives here too. A short push before a hard deadline can win the week, but it borrows from capacity: burnout, attrition and bugs next sprint.

![Slide 22: Rally. A red alarm bell rings on a small brick factory at the far left: RING! RING! The sweating Manager shouts and waves everyone forward. A single-file line walks left to right toward a big flag B at the far right, each carrying a brick: a secretary with a headset, a dog with a brick in its mouth, a big boss with a cigar looking surprised, an accountant with a calculator, a salesperson and an engineer in a hard hat, who has almost reached B.](slides/22.jpg)

> Sometimes the deadline is real and immovable, and the only way to make it is to pull in everyone who can help, not just engineering.
> - A big customer go-live: PMs run QA test plans, support pre-stages hardware, sales engineers do on-site checks.
> - A P0 outage: the exec clears their calendar to handle customer comms so engineers can stay heads-down.
> - A launch week: designers write release notes, ops does install checklists, the CTO reviews PRs.
> Make it explicit: declare it, give it an end date, and give each person a concrete, small task they can actually do. Then stop. If you're rallying everyone every month, it isn't a rally; it's a planning problem, and that's capacity.

![Slide 23: Carry, two panels. BEFORE: the Manager trudges along the road with four bricks, two in each hand, sweating and determined. AFTER: a big boxy robot with CLAUDE written on it walks the same road carrying towering stacks of hundreds of bricks, with the Manager sitting on top, smiling and pointing ahead.](slides/23.jpg)

> The old rule: managers shouldn't code. Your hours are fragmented, and if you take a critical-path ticket, it stalls every time you get pulled into a meeting.
> What changed: with an AI coding agent, a 30-minute gap between meetings is enough to ship something real.
> - Write the one-off migration or data-fix script nobody has time for.
> - Prototype the feature to answer "is this even feasible?" before the planning meeting.
> - Triage the bug backlog: reproduce, find the root cause, open the PR.
> - Build the internal dashboard or report that ops has asked for twice.
> - Review PRs faster, with the agent explaining the diff.
> The rule that hasn't changed: stay off the critical path. Carry the work that would otherwise never get done, not the work that blocks the team if you disappear for a day.

![Slide 24: How to increase capacity: ten tiles with the Manager. Hire: shaking hands with three new arrivals holding truck keys, a blueprint and an axe. Grow: one engineer goes from carrying a brick to a wheelbarrow to driving a truck. Delegate: handing his megaphone to a new lead with a small crew. Reward: giving an engineer a money bag and a medal. Prune: a line of brick carriers walking past. Organize: three crews in separate lanes of a road, with a MAKE, CARRY, STACK board. Automate: pressing the button on a brick conveyor belt while two engineers high-five. Cultivate: watering a young tree while engineers build a neat wall behind him. Ally: shaking hands with a neighboring town's leader at a crossroads while their truck carries our bricks. Fund: presenting a bar chart to the big boss, who hands over truck keys and a money bag.](slides/24.jpg)

> Everything on this slide pays off in months or years, not this week, which is why it always loses to this week's fire. Nobody will ask you on Friday why you didn't do a skip-level or fix the on-call rotation. Six months later, everyone will ask why the team is still slow. Block time for these the way you block time for a launch.

![Slide 25: Hire. The Manager sits at a folding table with a NOW HIRING sign and hands a set of truck keys across it to a smiling new hire with a ponytail. Behind her, candidates wait in line, one holding a rolled-up bridge plan and one an axe. A huge brick pile waits on the right.](slides/25.jpg)

> Hiring is the second thing your CEO judges you on, after delivery, because it's where everything else becomes visible: candidates can smell your culture, your strategy and whether you grow people.
> - Hire for the gap, not the clone: the team that's all backend needs the person who has shipped mobile.
> - One great senior hire can be worth three average ones; a bad hire is net negative and costs months to undo.
> - Make your recruiter a real partner: if they can't explain why the role is exciting, candidates won't feel it.
> - Every interview loop costs the team 5–10 engineer-hours. Budget for it.
> Hiring is slow capacity: it takes 3–6 months before a hire is fully ramped. Start before you're desperate.

![Slide 26: Grow. The same engineer, four times along a road, getting bigger each time: carrying one brick, pushing a wheelbarrow, driving a truck, then drawing a bridge at a drafting table. The Manager walks alongside, handing over the next tool each time.](slides/26.jpg)

> This could be a whole set of talks. Three parts:
> 1. Opportunities: give people work one size bigger than their last job. The mid-level engineer leads the next design review; the senior engineer owns the launch.
> 2. Mentorship: show how to do the job. Do it together first: you run the incident review while they watch, then they run it while you watch.
> 3. Coaching: support them while they do the job on their own. Weekly 1:1s, feedback within days, and questions instead of answers.

![Slide 27: Delegate. A huge field of brick carriers in tight rows, like a Roman legion, stretches to the horizon. On a small wooden stage in front, the Manager faces the legion, hands cupped, yelling at them as hard as he can; nobody can hear him. Below the stage, one engineer jumps up and down waving a sign: DELEGATE!!](slides/27.jpg)

> At some point your own hours are the bottleneck. Delegating is how one manager's capacity becomes several.
> - Tech leads who own the technical calls, so design decisions don't queue behind you.
> - A second-in-command who can run the team for two weeks while you're out, and actually does it.
> - Hand off whole problems (the release process, the on-call rotation), not tasks.
> - Let them do it differently than you would. If it's 80% as good and you didn't have to do it, that's a win.
> The test: if you disappear for a week, does the team slow down?

![Slide 28: Reward. In front, the Manager pins a medal with a ribbon on a smiling engineer, who holds up cash marked with a dollar sign. Coworkers around them in the foreground clap and cheer. Behind them stands a finished brick shack with a banner: CONGRATS ON YOUR PROMOTION!](slides/28.jpg)

> "My job is to leave money in your pocket and memories in your head."
> - Pay fairly and proactively: fix the underpaid engineer before they get the outside offer, not after.
> - Equity and refreshers tied to impact, explained clearly.
> - Recognition that's specific and public: name the person and what they did, in the all-hands, not just in a DM.
> - Non-money rewards: the interesting project, the conference talk, the promotion case you write for them.
> Money prevents a no. It rarely creates a yes.

![Slide 29: Prune. At a brick yard, one engineer shrugs, hands in pockets, after dropping a brick on a coworker's foot; the coworker hops in pain: OUCH! The Manager, disappointed, points firmly at a door under an EXIT sign. In the background, others keep carrying bricks.](slides/29.jpg)

> Sometimes capacity goes up when someone leaves.
> - One person who blocks every review, or who the team quietly routes around, slows down everyone near them.
> - Values rarely change; skills can. Coach skill gaps. When it's values, move faster than feels comfortable.
> - Be clear early: written expectations, a real plan, a date. Nobody should be surprised.
> - "Not firing fast enough" is one of the most common regrets of experienced managers.
> Do it with dignity. The rest of the team is watching how you treat people on the way out.

![Slide 30: Organize. A brick operation running on its own: at a loading dock with a duty board, the nerdy guy loads a truck with a forklift. A signpost points to B ROUTE and C ROUTE; a truck drives each road, and at each flag a strong man unloads at his own station. Nobody is looking at the Manager, who stands at an easel in the foreground sketching a new dashed road toward a faraway flag D, next to a sign reading D ROUTE?](slides/30.jpg)

> Assign is who carries which brick this week. Organize is the structure that makes that call for you every week, so you can work on the next route. The shape of the team decides how much it can do.
> - Clear ownership: every service, every alert and every customer issue has one team that owns it.
> - Small teams with few dependencies ship faster than one big team with many.
> - Few, explicit handoffs: product to engineering, engineering to QA, QA to support.
> - An on-call rotation that doesn't burn out the same two people.
> - Just enough process: a weekly plan, a retro, a postmortem. Kill the meetings nobody would miss.

![Slide 31: Automate. Side view of one straight road from the brick factory on the left to the customer site and flag B on the right. Each builder works at the front edge of its road, with the vehicle that uses it behind on the finished part. Left to right: the Manager and two engineers building a conveyor belt at the factory; a heavy truck full of bricks on the pavement; a steamroller at the end of the pavement; a light truck with about 100 bricks on leveled dirt; a bulldozer at the end of the dirt; a wheelbarrow of about 10 bricks on a rough path; a person rolling a rock off the end of the path; and one person carrying a single brick over the rocks to the customer. Everything moves toward the customer.](slides/31.jpg)

> Every hour of toil you remove pays back every week after. Each level of technology is roughly 10x the last, and you build the next level while the current one keeps delivering.
> - The page that costs an hour a week and takes 12 hours to fix pays back in 12 weeks. Fix it.
> - CI that takes 40 minutes taxes every PR, every day.
> - Deploys that need a person and a checklist become deploys that need a button.
> - Pay down the tech debt that slows every feature, not the debt that just looks ugly.
> - AI agents on the repetitive work: test writing, migrations, triage.
> Build it while you keep shipping. Stop delivering to build the perfect tool, and you lose the week and the trust.

![Slide 32: Cultivate. Side view, three repairs in a row, each bigger than the last. On the left, the Manager kneels and fits a new wheel on a broken wheelbarrow. In the middle, an engineer changes the flat tire of a light truck, watching the Manager (a dashed sight line runs to him). On the right, a second engineer on a step stool fixes the engine of a heavy truck, watching the middle engineer (a dashed sight line runs to him).](slides/32.jpg)

> Culture is what people copy. Your team copies what you do, not what you say, and the next hire copies them, long after they've stopped watching you.
> - You break prod: you write the postmortem, and it starts with your own mistake. Six months later, a junior engineer opens theirs the same way.
> - You fix the flaky test instead of hitting re-run. Your tech lead stops re-running, and so does the new hire.
> - You review PRs within a day, with a real comment, not just LGTM. That becomes the team's review bar.
> - You say "I don't know, let me find out" in a design review. People stop bluffing.
> Then make it explicit: a few words people can act on, like "Rigorously Get Shit Done". Reward what you say you value; if you say quality but celebrate only speed, the team copies speed. Hire and fire by it.
> It's slow to build and fast to lose.

![Slide 33: Ally. Side view of one road from the brick factory to the customer site at flag B. The Manager appears three times, shaking hands each time: at the factory with Sales, in a trucker cap, next to a truck loaded with bricks; in the middle with the CFO in a suit, who hands him a money bag marked $ beside a BUDGET chart; and at the customer site with Product, who holds a rolled-up plan.](slides/33.jpg)

> Other functions' capacity can become yours. Engineering can't win alone, and the partners who trust you will spend their capacity on your goals.
> - Product: a partner, not a requester. You plan the roadmap together, they cut scope with you instead of around you, and they bring you to the customer.
> - Sales: they tell you which deals need what, months before the contract is signed, and they don't sell the feature you haven't built. In return, you give them dates you actually hit.
> - Finance: the CFO who understands your plan funds it. Show what each dollar buys, stay on budget, and share bad news early.
> - Also: the platform team that adds the API you need if they hear about it a quarter ahead, and the recruiter who moves faster on your hires.
> Alliances are built before you need them, not during the crisis.

![Slide 34: Fund. In an office, the Manager presents a rising bar chart on an easel to the big boss behind a desk; the boss, smoking a cigar, hands over truck keys and a money bag. Through the window, a new truck waits next to a pile of bricks.](slides/34.jpg)

> Headcount and budget are capacity, and you have to earn them.
> - A hiring plan and a comp plan that tie each dollar to an outcome the CEO cares about.
> - Stay on budget, and share bad news early. Nothing builds CEO trust faster.
> - Ask for the truck with a business case: what it costs, what it unlocks, when it pays back.
> - Start small and earn more: a two-day draft, reviewed together, then sharpen the numbers.
> Every yes from the CEO is spent from trust you built earlier.

![Slide 35: Back in the seminar room from slide 3, at the end of a long day. The screen reads OMG, HOW DO I DO ALL THAT? above a long scribbled list. The three audience members are slumped in their chairs, exhausted and sweating. The Manager is exhausted too: hair disheveled, tie loosened and askew, pointer drooping.](slides/35.jpg)

> Twenty buckets. Nobody does all twenty every week, and nobody should try. I don't. In any given week, two or three of them matter, and the rest can wait. The hard part isn't knowing the buckets; it's knowing which two or three this week, because the world keeps changing under you.

![Slide 36: The same exhausted seminar room. A door on the left has opened a crack, and a nervous engineer peeks in, sweating, saying UM, BAD NEWS SIR... The audience and the Manager all turn toward the door, wide-eyed.](slides/36.jpg)

> Let it sit for a second. You will get this message on the day you finally have a plan you like. Every manager has had the Slack DM that starts with "hey, got a minute?" at 4:55 on a Friday. It's not a sign the plan was bad. It's what the job actually looks like.

![Slide 37: Reality. A full-page hand-drawn chart over 200 days with two axes and a red DEADLINE line at day 180. Left axis, MoBs: a blue TOTAL SCOPE staircase starts at 9,000, jumps to 13,000 on day 30 and is trimmed to 11,000, jumps to 15,000 on day 90 and is cut to 12,500, then drops to 11,500 on day 178. A bold black REMAINING burn-down jumps with each scope change and slopes down, slowly at first, then steeply, reaching zero on day 179, one day before the deadline. Right axis, MoB per day: a green CAPACITY staircase. Seven numbered notes: 1, scope balloons +4,000, trim -2,000. 2, tech lead quits, 30 to 20 per day, delegate, 35 per day. 3, big hire lands, 50 per day, grow. 4, new flag customer C +4,000, decide B first, -2,500. 5, P0 outage, 6 days at 5 per day, rally. 6, platform API, 120 per day, ally. 7, CI from 40 to 8 minutes, 155 per day, automate. 8, last day: furious PM negotiation, scope -1,000.](slides/37.jpg)

> Reality is incredibly messy: unpredictable things happen all the time. Your job, in a nutshell, is to deliver despite the chaos. Try to enjoy it.

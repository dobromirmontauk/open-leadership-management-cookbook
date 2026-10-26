# Winning, and Increasing the Capacity to Win — slide outline (draft 7)

Running analogy: move a ton of bricks from Point A to Point B. Build the team, and the technology (roads, bridges, trucks), to do it.

## Top-level message

- **A turn** = one week of engineering. Every week the team gets one turn on the map.
- **Winning** = how much you get out of *this* turn. How many bricks moved, and how much closer to B.
- **Capacity** = how much the *next* turns can do. More bricks per turn, more distance per turn.
- **The tension:** every hour you spend on capacity is an hour you don't spend carrying bricks this week. The job is to do both.

### Winning buckets (this week's bricks)

1. **Aim:** do we know what the end result looks like?
2. **Trim:** cut scope, two kinds. **The product** (what we're building): do we really need all these bricks? **The approach** (how): don't build the truck yet, just carry the damn bricks. Save it for later.
3. **Decide:** make the call now, even without enough data. Teams lose whole days waiting on decisions nobody has made.
4. **Scout:** better, if you can afford it: de-risk the unknown before the convoy commits. Send an explorer, build a spike, check whether the river has a ford.
5. **Assign:** the right person on the right job: chop trees, lay road, carry bricks, drive the truck. Includes **swarming**: several people on the one brick everything else waits on.
6. **Steer:** we end up with multiple flags (B, C, D...). Do we push the right bricks in the right direction this week? Includes **prioritizing**: carry the most valuable bricks first, so what's arrived still counts if the deadline hits mid-pile.
7. **Clear & Protect:** remove blockers and distractions: fallen trees, waiting on another team. Includes **shielding**: bandits come to kidnap our people (mid-week asks, "quick favors") and we protect them.
8. **Motivate:** get people excited to carry more bricks. Includes **overtime**: getting people to work harder for a stretch.
9. **Rally:** pull people from other roles into moving bricks (a fire drill).
10. **Carry** (sometimes): pick up a brick yourself when that's the highest-leverage move. Don't stop leading.

### Capacity buckets (future turns)

1. **Hire:** more hands and new skills. Hiring is the second thing your CEO judges you on, after delivery. (Cookbook: `hiring/`)
2. **Grow:** make each person better: feedback, 1:1s, career conversations, ladders, onboarding. (`growing/`)
3. **Delegate:** grow leaders who multiply you: tech leads, a second-in-command, new EMs. (`growing/self/delegating.md`, `transitioning/`)
4. **Reward:** pay, equity, recognition, non-money rewards. "Leave $ in your pocket and memories in your head." (`reward_systems/`)
5. **Prune:** let go of people who drag the team down. Values rarely change; skills can. (`firing/`)
6. **Organize:** team shape, ownership, on-call, and the few processes that hold it together. (`winning/process/`, eng-teams deck)
7. **Automate:** tools, infrastructure, CI, tech debt, AI. (The pager example: 12 hours to fix pays back in 12 weeks.)
8. **Cultivate:** the norms that hold when you're not in the room: RGSD, rigor. (`leadership/alignment/`)
9. **Ally:** partners who lend capacity: your boss and CEO, the head of Product, HR, your recruiter, other teams.
10. **Fund:** headcount and budget, the hiring and comp plans, staying on budget. "Share bad news early." (`budgeting/`)

## How the slides work

- **Every slide** has "Copyright Dobromir Montauk 2026" in small type at the bottom.

- **Boring slides** (slides 1–2 only) are deliberately dull corporate slides: plain text, a stock-template look. Everything after them is hand-drawn, so the contrast is the joke.
- **Map slides** all show the *same hand-drawn map*: stick-figure/comic-strip style, black line art, like a kid's treasure map. Each map slide adds or reveals one thing, so clicking through looks like the journey unfolding.
  - **Left:** A, a brick pile with a tiny home base.
  - **Right:** B, a flag (later several flags).
  - **Between:** FOG OF WAR at first, covering almost everything. Fog lifts as we explore.
  - **Terrain revealed over time:** mountains (wrong path / dead end), rivers (unexpected challenges to cross), forest, swamp.
  - **What we build:** footpath (dotted line) → dirt road → paved road → bridges → highway. Some roads get abandoned (marked with an X).
  - **How bricks move:** hands → wheelbarrows → carts → trucks → convoys. Tiny icons on the roads.
  - **Other people:** scouts at the edge of the fog, road crews, a neighbor town (partners).
  - **Turn counter:** a small "TURN 1, TURN 2…" tag in a corner, plus a brick tally at B.
- **Comic slides** sit between map slides. They zoom down to ground level with the stick-figure cast and tell the human story.
- **Bucket slides** open each bucket: one icon plus the bucket name, so the audience always knows where they are. A small checklist of all buckets in a corner shows which one is current.

---

## Intro — The boring version

1. **Engineering Management 101** · Boring
   - Comic: none. Deliberately dull corporate title slide: centered text, a stock-photo-style handshake, a fake logo.
   - Text: "Engineering Management 101"
   - Notes (talk track): Deliver it completely straight; let the pause run a beat too long.

2. **The job of an Engineering Manager** · Boring
   - Comic: none. Plain bullets in a dull corporate template.
   - Text: "1. Winning" / "2. Increasing the Capacity to Win"
   - Notes (talk track): Read it flatly. This is the whole talk and it sounds like nothing. Ask what it means; nobody answers.

3. **WTF does this mean?** · Comic
   - Comic: the audience as stick figures: one asleep, one on a phone, one with a giant "?" over their head. The Manager squints at slide 2 too.
   - Text: "WTF does this mean?"

## Intro — A stupidly simple analogy
   - Notes (talk track): Admit I'm not sure either. By the end you should be able to use these words to make a decision on Monday.

4. **Stupid simple analogy** · Title card
   - Comic: hand-lettered "STUPID SIMPLE ANALOGY" framed by stacks and scattered bricks. No people.
   - Text: "Stupid simple analogy"
   - Notes (talk track): It's so stupid-simple that it won't map 1:1 with our jobs. That shouldn't stop you from getting the lessons.

5. **The job** · Comic
   - Comic: CEO hands Manager a note: "Move the bricks to B." Manager gulps at the pile. (Bricks first, no B in sight.)
   - Text: "Move the bricks to B."
   - Notes (talk track): Every EM gets some version of this note. Build the team and the technology. Why bricks? Shipping features isn't that different.

6. **B is in the distance** · Comic
   - Comic: Manager next to the huge A pile, scratching his head. A tiny "B" flag far away on the horizon.
   - Text: none.
   - Notes (talk track): Nobody told you how big B is, how far, or what's in between. Every unknown will bite us later.

7. **Defining Winning** · Comic
   - Comic: the slide-3 seminar room again, but everyone is paying attention (notes, phone away, lightbulb). Manager points at the screen: three people carrying bricks from a pile to a flag, with a distance arrow.
   - Text (on screen): "WINNING" / "HOW MANY × HOW FAR"
   - Notes (talk track): A win is one turn, one week. Bricks moved sideways score zero. Ask: what did your team win last week?

8. **Day 1** · Comic
   - Comic: same A-to-B landscape. Manager, sweaty, thumbs up, next to a stack of 3 bricks moved 10m from A. B still far away.
   - Text: "DAY 1: NICE START!" / "+3 BRICKS × 10M = 30 MoBs" / "(METERS OF BRICKS)"
   - Notes (talk track): Celebrate it, then do the math out loud: how many bricks, how far is B? Let the room get uneasy.

9. **Time pressure!** · Comic
   - Comic: seminar room, EVERYONE scared and sweating (Manager with forced grin and shaking pointer; note-taker frozen, nail-biter, collar-tugger). Screen (chart composited in): a LINEAR burn-down of REMAINING MoBs vs DAYS at "30 MoBs / DAY", hitting zero at "300 DAYS", well past the red "DEADLINE" line (red "!").
   - Text (on screen): "TIME PRESSURE" / "REMAINING MoBs" / "30 MoBs / DAY" / "300 DAYS" / "DAYS" / "DEADLINE" (red)
   - Notes (talk track): If ALL the bricks don't arrive by date X, all that winning is worthless. Day 1's pace = 300 days; the deadline is months before. Winning alone stops being enough.

10. **Defining Increasing Capacity** · Comic
    - Comic: same seminar room, attentive. Screen: "INCREASING CAPACITY", the formula, and a TIME arrow with a wheelbarrow (2×, bold lines), a truck (50×, lighter lines) and a Starship full of bricks (10,000×, faint dashed with a "?").
    - Text (on screen): "INCREASING CAPACITY" / "VALUE = IMPACT / (1 + r)^TIME" / "2×" "50×" "10,000×"
    - Notes (talk track): Capacity = everything that doesn't move a brick this week but moves more later. Discount because the future is uncertain. Best impact for the time, not the biggest number.

11. **Time pressure, with capacity** · Comic
    - Comic: same room, mostly RELIEVED (Manager wiping his brow and grinning; "PHEW"; one slumped with relief; one fist-pumping; leftover sweat drops). Screen (chart composited in): CAPACITY (dashed) and # OF BRICKS (dotted) curving up exponentially; REMAINING MoBs curving down faster and faster, reaching zero just before the red "DEADLINE" line, with "JUST MADE IT!".
    - Text (on screen): "TIME PRESSURE" / "MoBs" / "REMAINING MoBs" / "CAPACITY" / "# OF BRICKS" / "DAYS" / "DEADLINE" (red) / "JUST MADE IT!"
    - Notes (talk track): What changed is capacity, and it compounds. That's how you beat a deadline you can't beat at today's pace. "Just made it" isn't comfortable.

12. **These are in tension!** · Comic
    - Comic: Manager (no clipboard; marker in hand) scratching his head at a whiteboard with two columns of checkboxes. Wall clock at 4 o'clock ("TICK"). Thought bubble: "ONE HOUR...".
    - Text: "THESE ARE IN TENSION!" / "WIN": "CARRY BRICKS", "CLEAR THE ROAD", "UNBLOCK A TEAMMATE", "CHECK IN WITH CUSTOMER" / "INCREASE CAPACITY": "INTERVIEW A HIRE", "TRAIN THE NEW GUY", "BUILD A WHEELBARROW", "CAREER 1:1"
    - Notes (talk track): No answer is always right. Some days bricks must move; some days train the new guy. The rest of the talk is about making that call well.

## Part 1 — Winning (this turn's bricks)

13. **How to win** · Grid of thumbnails cropped from the ten slides (tools/grid.py), in slide order
    - Comic: Ten square tiles, each a close-up teaser cropped from its slide. Top row: Aim, Trim, Decide, Scout, Assign. Bottom row: Steer, Clear and Protect, Motivate, Rally, Carry.
    - Text: "HOW TO WIN" / "AIM" "TRIM" "DECIDE" "SCOUT" "ASSIGN" "STEER" "CLEAR & PROTECT" "MOTIVATE" "RALLY" "CARRY"
    - Notes (talk track, yours): each of these can be a whole course by itself. We lightly touch each one and give examples, so you can pattern-match your activities to the bucket they fall into.

### Aim

14. **Aim** · Comic
    - Comic: a field seen from the side. Pile A on the left. Three old flags still stand across the field, crossed out and labeled B (MON), B (TUE), B (WED), each with a small stack of bricks delivered there for nothing; footprints run from A to each in turn. At the third, the Manager points to the far right, where the customer (knit beanie) plants the real flag B on empty ground; three engineers with bricks look on, surprised.
    - Text: "AIM" / "A" / "B (MON)" "B (TUE)" "B (WED)" / "B"
    - Notes (talk track, yours): goals move all the time, for lots of reasons. The team's work only matters if it takes you *in the direction of the goal*; even a little off-track wastes effort. Figuring out the actual goal makes THIS WEEK's work maximally productive.

### Trim

15. **Trim** · Comic (one panel, split down the middle)
    - Comic, right half: a dirt road runs from a brick pile toward a tiny flag B far away, with a small stake and flag at the halfway point. The customer (knit beanie) points eagerly at B: "ALL OF THEM, ALL THE WAY TO B!" The calm Manager points at the halfway stake: "HOW ABOUT HALFWAY FIRST?"
    - Comic, left half: two engineers kneel, assembling a wheelbarrow from parts (loose wheel, wrench, screws, blueprint) next to an untouched brick pile. The same Manager: "JUST CARRY THE DAMN BRICKS".
    - Text: "TRIM" / "JUST CARRY THE DAMN BRICKS" / "ALL OF THEM, ALL THE WAY TO B!" / "HOW ABOUT HALFWAY FIRST?"
    - Notes (talk track): two kinds of scope to cut. On the left, approach scope: the framework, platform or automation we would love to build first. Building tools is capacity, not winning, so do it on purpose, not by accident. On the right, product scope: the customer wants every brick, all the way to B. Halfway, delivered first, is usually what they actually need this quarter, and it's worth something on its own.
    - Notes, examples:
      1. Approach scope. A request for one flag on one machine turned into a design for tiered config with merge rules and a new admin UI. Someone asked, "any objection to the hackiest possible approach?" A one-off override solved it that day.
      2. Approach scope. An engineer wanted a generic plugin system first, so integrations would be "easy forever". There was one integration on the roadmap. Hard-code it; build the abstraction from three real examples later, not zero.
      3. Approach scope. Support wanted an edge case automated before launch. How often does it happen? About once a week. Keep it manual for now, and launch.
      4. The other side. A simple database index was suggested early and passed over because the tests weren't representative. Seven weeks later, under production load, the same index took the query from 4.5 s to 0.7 s.
      5. Product scope. The customer asked for a full analytics dashboard: filters, charts, scheduled emails. The question "what decision is this for?" turned up one weekly number for the CFO. A nightly CSV export shipped in two days.
      6. Product scope. The spec said "supports every payment type". The data said 97% of transactions were cards. Launch with cards, a month early; add the next type when a real customer asks.
      7. Product scope. The plan included a full admin UI for config, roles and audit logs. The only users were three internal engineers. A documented script and a config file in the repo did the job and saved six weeks.
      - Caveat: a trimmed feature still has to be usable. Call phase 1 a partial feature, not GA.

### Decide

16. **Decide** · Comic
    - Comic: at a fork, two engineers holding bricks argue, one pointing left into a dark forest ("FOREST!"), the other right up the mountains ("MOUNTAINS!"). Between them the Manager calmly points up the mountain road: "MOUNTAINS. GO." Nearby, a big untouched brick pile and four engineers sitting with popcorn, watching instead of working.
    - Text: "DECIDE" / "FOREST!" / "MOUNTAINS!" / "MOUNTAINS. GO." / "POPCORN"
    - Notes (talk track): Often you have to make the call before you have enough data. Teams lose days, sometimes weeks, waiting on decisions nobody owns. The cost isn't the two people arguing; it's everyone blocked behind them.
      - Two senior engineers debate the data model for two weeks while the rest of the team can't start.
      - A design review ends with "let's take this offline" for the third time.
      - A PR sits blocked on an architecture argument in the comments.
      - "Which customer first?" goes unanswered, so people pick their own.
      - Most technical decisions are reversible. Set a deadline for the decision, hear both sides, make the call, write down why, and revisit if new data shows up. Disagree and commit.

### Scout

17. **Scout** · Comic (top-down map)
    - Comic: a hand-drawn top-down map of a forest. Three roads start at the bottom middle: the left one winds into the mountains and ends at an X; the middle one goes straight up and ends at an X; the right one loops around, crosses the river on a bridge and reaches flag B at the top middle. At the fork the Manager points up the right road; a line of engineers carries bricks along it.
    - Text: "SCOUT" / "THIS WAY!" / "B"
    - Notes (talk track): On the last slide we picked the mountains with no data. A scout would have found that dead end in two days. Scouting ahead is more work up front, but it's cheaper than committing the whole team to the wrong road for a month.
      - Spike the vendor or POS API for two days before promising the integration date: auth quirks, rate limits, missing endpoints.
      - Prototype the hard part first (latency, the hardware constraint, the model accuracy), not the easy UI.
      - Ask who tried this before. The team that attempted it last year knows where it broke.
      - Read the customer's actual setup (network, hardware, existing POS) before estimating.
      - Send one engineer for a few days, not the whole team for a sprint. The obvious approach is often the one nobody has taken end to end.

### Assign

18. **Assign** · Comic
    - Comic: four specialists stand before the Manager: a truck driver (steering wheel, keys), a strong guy (flexing, tall brick stack on his shoulder), a lumberjack (beard, axe) and a scout (hat, backpack, walking stick). The Manager, hand on chin, has a big thought bubble of all four working one road at once: the scout leads, the lumberjack clears, the truck hauls, the strong guy carries. "10x!" in the bubble.
    - Text: "ASSIGN" / "10x!"
    - Notes (talk track): Engineers aren't fungible. The person who knows the payment stack fixes the payment bug in a day; someone new to it takes a week.
      - Your best debugger goes on the production incident.
      - Your best communicator goes on the customer-facing integration.
      - Your fastest prototyper takes the spike.
      - Watch for assigning by "who's free" instead of "who's best for this".
      - When one task blocks everything (the release, the P0 bug), swarm it. The tradeoff: always picking the expert creates hero dependency. Spreading knowledge is capacity, and it comes later in the talk.

### Steer

19. **Steer** · Comic
    - Comic: Three flags in the distance, B, C and D, each with a customer in a cap yelling: 100 MONDAY! at B, 50 FRIDAY! at C, 10 TUESDAY! at D. In front, the calm Manager stands where three paths fan out, arms spread: one hand points an engineer pushing a wheelbarrow full of bricks toward B, the other points an engineer carrying a small stack of bricks toward D. The path to C is empty for now.
    - Text: "STEER" / "B" "C" "D" / "100 MONDAY!" "50 FRIDAY!" "10 TUESDAY!"
    - Notes (talk track): Three customers, three deadlines, and each one is sure they're the priority. Your job is to turn the noise into an order: value, deadline, size.
      - The big launch due Monday gets most of the team.
      - The small fix for a key account due Tuesday gets one engineer, so it ships and is off the board.
      - The Friday request waits on purpose, and you tell that customer explicitly, with a date.
      - Spread the team across all three and everything ships late. Re-check mid-week: did priorities change? Did sales promise something new?

### Clear & Protect

20. **Clear & Protect** · Comic
    - Comic: foreground, the Manager, sweating, chops through a fallen trunk across the road ("THWACK!"), back turned to the forest; two engineers with bricks wait behind him. Background, at the edge of the forest: two masked bandits ("QUICK FAVOR?", "JUST 5 MIN!") drag a third engineer ("HELP!", dropping bricks) into the trees. Nobody on the road notices.
    - Text: "CLEAR & PROTECT" / "THWACK!" / "QUICK FAVOR?" / "JUST 5 MIN!" / "HELP!"
    - Notes (talk track): Two kinds of obstacles.
      - Blockers you can see: waiting on another team's API, missing access or credentials, a flaky CI pipeline, a decision nobody has made. Chasing these down is visible and feels great.
      - Distractions you don't see: the "quick favor" from sales, the exec who needs "just 5 minutes" every day, an extra interview loop, the side project someone pulled your engineer into. They take your best people one at a time.
      - Ask in 1:1s where their time actually went last week, and compare it to the plan. Then say no on their behalf.

### Motivate

21. **Motivate** · Comic
    - Comic: On the right, flag B stands next to a small rickety wooden shack, and the customer, in a knit beanie, looks at it sadly; a dreamy thought bubble above the customer shows a fairy-tale castle. On the left, the Manager, smiling, points toward the customer; his speech bubble holds no words, only a drawing of a solid two-storey brick house with a chimney. Four engineers holding bricks grin, excited; one is already walking toward the shack with a stack of bricks.
    - Text: "MOTIVATE" / "$" / "B"
    - Notes (talk track): People work harder on things they understand and care about.
      - Bring an engineer to a customer site to watch the product being used.
      - Share the real number: the revenue, the customer count, the deal this unlocks.
      - Connect the project to their career: this is the scope that gets them promoted.
      - Celebrate the ship publicly and name who did it.
      - But don't oversell. If the "company-changing" launch turns out to be a pilot at one site, the next pitch lands flat.
      - Overtime lives here too. A short push before a hard deadline can win the week, but it borrows from capacity: burnout, attrition and bugs next sprint.

### Rally

22. **Rally** · Comic (red is used only for the alarm)
    - Comic: A red alarm bell rings on a small brick building with a chimney and a BRICKS sign at the far left: RING! RING! The sweating Manager shouts and waves everyone forward. A single-file line walks left to right toward a big flag B at the far right: a woman with a headset and glasses, a dog with a brick in its mouth, the CEO in his general&#x27;s uniform and cape, an accountant holding a calculator, a salesperson in a suit and an engineer in a hard hat. All but the accountant carry a brick.
    - Text: "RALLY" / "RING! RING!" / "BRICKS" / "B"
    - Notes (talk track): sometimes the deadline is real and immovable, and the only way to make it is to pull in everyone who can help, not just engineering.
      - A big customer go-live: PMs run QA test plans, support pre-stages hardware, sales engineers do on-site checks.
      - A P0 outage: the exec clears their calendar to handle customer comms so engineers can stay heads-down.
      - A launch week: designers write release notes, ops does install checklists, the CTO reviews PRs.
      - Make it explicit: declare it, give it an end date, and give each person a concrete, small task. Then stop. If you rally everyone every month, it's a planning problem, and that's capacity.

### Carry

23. **Carry** · Comic (two panels, side by side)
    - Comic, left "BEFORE": the Manager trudges along the road with four bricks, two in each hand, sweating but determined.
    - Comic, right "AFTER": a big boxy robot with "CLAUDE" written on it walks the same road carrying towering stacks of hundreds of bricks; the Manager sits on top, smiling and pointing ahead.
    - Text: "CARRY" / "BEFORE" / "AFTER" / "CLAUDE"
    - Notes (talk track): the old rule: managers shouldn't code. Your hours are fragmented, and a critical-path ticket stalls every time you're pulled into a meeting.
      - What changed: with an AI coding agent, a 30-minute gap between meetings is enough to ship something real.
      - Write the one-off migration or data-fix script nobody has time for.
      - Prototype the feature to answer "is this even feasible?" before the planning meeting.
      - Build the internal dashboard or report ops has asked for twice.
      - What hasn't changed: stay off the critical path. Carry the work that would otherwise never get done, not the work that blocks the team if you disappear for a day.

### Wrap-up (proposed, unnumbered)

- **Some winning tools borrow from capacity** · Comic (proposed)
    - Comic: the Manager wins this week's tally, but a small "IOU" note flies off to next week: tired people (overtime), pulled people (rally), cracked bricks (cut corners / tech debt).
    - Text: "Some wins borrow from next week."
    - Notes (talk track): bridge into Part 2. Winning tools that spend capacity are fine, as long as you know you're spending it.

## Part 2 — Capacity (future turns)

24. **How to increase capacity** · Grid of thumbnails cropped from the ten slides (tools/grid.py), in slide order
    - Comic: Ten square tiles, each a close-up teaser cropped from its slide. Top row: Hire, Grow, Delegate, Reward, Prune. Bottom row: Organize, Automate, Cultivate, Ally, Fund.
    - Text: "HOW TO INCREASE CAPACITY" / "HIRE" "GROW" "DELEGATE" "REWARD" "PRUNE" "ORGANIZE" "AUTOMATE" "CULTIVATE" "ALLY" "FUND"
    - Notes (talk track): everything here pays off in months or years, not this week, which is why it always loses to this week's fire. Nobody asks on Friday why you skipped the skip-level or didn't fix the on-call rotation; six months later, everyone asks why the team is still slow. Block time for these the way you block time for a launch.

### Hire

25. **Hire** · Comic
    - Comic: the Manager sits at a folding table with a NOW HIRING sign and hands a set of truck keys across it to a smiling new hire with a ponytail. Behind her, candidates wait in line, one holding a rolled-up bridge plan and one an axe. A huge brick pile waits on the right.
    - Text: "HIRE" / "NOW HIRING" / "BRIDGE"
    - Notes (talk track): Hiring is the second thing your CEO judges you on, after delivery, because it's where everything else becomes visible: candidates can smell your culture, your strategy and whether you grow people.
      - Hire for the gap, not the clone: the team that's all backend needs the person who has shipped mobile.
      - One great senior hire can be worth three average ones; a bad hire is net negative and costs months to undo.
      - Make your recruiter a real partner: if they can't explain why the role is exciting, candidates won't feel it.
      - Every interview loop costs the team 5–10 engineer-hours. Budget for it.
      - Hiring is slow capacity: it takes 3–6 months before a hire is fully ramped. Start before you're desperate.

### Grow

26. **Grow** · Comic
    - Comic: The same engineer, four times along a road, getting bigger and happier each time: carrying one brick, pushing a wheelbarrow, driving a truck, then drawing a bridge at a drafting table. The Manager walks alongside, smiling, handing over the next tool each time (the wheelbarrow, truck keys, a pencil), and at the end watches, hand on chin.
    - Text: "GROW"
    - Notes (talk track): this could be a whole set of talks. Three parts:
      1. Opportunities: give people work one size bigger than their last job. The mid-level engineer leads the next design review; the senior engineer owns the launch.
      2. Mentorship: show how to do the job. Do it together first: you run the incident review while they watch, then they run it while you watch.
      3. Coaching: support them while they do the job on their own. Weekly 1:1s, feedback within days, and questions instead of answers.

### Delegate

27. **Delegate** · Comic
    - Comic: a huge field of brick carriers in tight rows, like a Roman legion, stretches to the horizon. On a small wooden stage in front, the Manager faces the legion, hands cupped, yelling at them as hard as he can; nobody can hear him. Below the stage, one engineer jumps up and down waving a sign: "DELEGATE!!"
    - Text: "DELEGATE" / "DELEGATE!!"
    - Notes (talk track): At some point your own hours are the bottleneck. Delegating is how one manager's capacity becomes several.
      - Tech leads who own the technical calls, so design decisions don't queue behind you.
      - A second-in-command who can run the team for two weeks while you're out, and actually does it.
      - Hand off whole problems (the release process, the on-call rotation), not tasks.
      - Let them do it differently than you would. If it's 80% as good and you didn't have to do it, that's a win.
      - The test: if you disappear for a week, does the team slow down?

### Reward

28. **Reward** · Comic
    - Comic: in front, the Manager pins a medal with a ribbon on a smiling engineer, who holds up cash marked with a "$". Coworkers around them in the foreground clap and cheer. Behind them stands a finished brick shack with a banner on two lines: "CONGRATS ON / YOUR PROMOTION!"
    - Text: "REWARD" / "CONGRATS ON YOUR PROMOTION!" / "$"
    - Notes (talk track): "My job is to leave money in your pocket and memories in your head."
      - Pay fairly and proactively: fix the underpaid engineer before they get the outside offer, not after.
      - Equity and refreshers tied to impact, explained clearly.
      - Recognition that's specific and public: name the person and what they did, in the all-hands, not just in a DM.
      - Non-money rewards: the interesting project, the conference talk, the promotion case you write for them.
      - Money prevents a no. It rarely creates a yes.

### Prune

29. **Prune** · Comic
    - Comic: at a brick yard, one engineer shrugs, hands in pockets, after dropping a brick on a coworker's foot; the coworker hops in pain ("OUCH!"). The Manager, disappointed, points firmly at a door under an "EXIT" sign. In the background, others keep carrying bricks.
    - Text: "PRUNE" / "OUCH!" / "EXIT"
    - Notes (talk track): Sometimes capacity goes up when someone leaves.
      - One person who blocks every review, or who the team quietly routes around, slows down everyone near them.
      - Values rarely change; skills can. Coach skill gaps. When it's values, move faster than feels comfortable.
      - Be clear early: written expectations, a real plan, a date. Nobody should be surprised.
      - "Not firing fast enough" is one of the most common regrets of experienced managers.
      - Do it with dignity. The rest of the team is watching how you treat people on the way out.

### Organize

30. **Organize** · Comic
    - Comic: a brick operation running on its own. At a loading dock with a duty board, the nerdy guy loads a truck with a forklift. A signpost points to "B ROUTE" and "C ROUTE"; a truck drives each road, and at each flag a strong man unloads at his own station. Nobody is looking at the Manager, who stands at an easel in the foreground sketching a new dashed road toward a faraway flag D, next to a sign reading "D ROUTE?".
    - Text: "ORGANIZE" / "LOADING DOCK" / "DUTY BOARD" / "B ROUTE" "C ROUTE" "D ROUTE?" / "NEW" / "B" "C" "D"
    - Notes (talk track): Assign is who carries which brick this week. Organize is the structure that makes that call for you every week, so you can work on the next route. The shape of the team decides how much it can do.
      - Clear ownership: every service, every alert and every customer issue has one team that owns it.
      - Small teams with few dependencies ship faster than one big team with many.
      - Few, explicit handoffs: product to engineering, engineering to QA, QA to support.
      - An on-call rotation that doesn't burn out the same two people.
      - Just enough process: a weekly plan, a retro, a postmortem. Kill the meetings nobody would miss.

### Automate

31. **Automate** · Comic
    - Comic: side view of one straight road from the brick factory (left) to the customer site and flag B (right). Each builder works at the front edge of its road, with the vehicle that uses it behind on the finished part. Left to right: the Manager and two engineers building a conveyor belt at the factory; a heavy truck full of bricks on the pavement; a steamroller at the end of the pavement; a light truck with about 100 bricks on leveled dirt; a bulldozer at the end of the dirt; a wheelbarrow of about 10 bricks on a rough path; a person rolling a rock off the end of the path; one person carrying a single brick over the rocks to the customer.
    - Text: "AUTOMATE" / "BRICKS" / "B"
    - Notes (talk track): Every hour of toil you remove pays back every week after. Each level of technology is roughly 10x the last, and you build the next level while the current one keeps delivering.
      - The page that costs an hour a week and takes 12 hours to fix pays back in 12 weeks. Fix it.
      - CI that takes 40 minutes taxes every PR, every day.
      - Deploys that need a person and a checklist become deploys that need a button.
      - Pay down the tech debt that slows every feature, not the debt that just looks ugly.
      - AI agents on the repetitive work: test writing, migrations, triage.
      - Build it while you keep shipping. Stop delivering to build the perfect tool, and you lose the week and the trust.

### Cultivate

32. **Cultivate** · Comic
    - Comic: Side view, three repairs in a row, each bigger than the last. The Manager fits a new wheel on a broken wheelbarrow; an engineer changes a light truck's flat tire while watching him; a second engineer fixes a heavy truck's engine while watching the first engineer. Dashed sight lines show who is copying whom.
    - Text: "CULTIVATE"
    - Notes (talk track): Culture is what people copy. Your team copies what you do, not what you say, and the next hire copies them, long after they've stopped watching you.
      - You break prod: you write the postmortem, and it starts with your own mistake. Six months later, a junior engineer opens theirs the same way.
      - You fix the flaky test instead of hitting re-run. Your tech lead stops re-running, and so does the new hire.
      - You review PRs within a day, with a real comment, not just LGTM. That becomes the team's review bar.
      - You say "I don't know, let me find out" in a design review. People stop bluffing.
      - Then make it explicit: a few words people can act on, like "Rigorously Get Shit Done". Reward what you say you value; if you say quality but celebrate only speed, the team copies speed. Hire and fire by it.
      - It's slow to build and fast to lose.

### Ally

33. **Ally** · Comic
    - Comic: Side view of one road from the brick factory to the customer site, a house frame under construction next to flag B. The Manager appears twice, shaking hands each time: at the factory with Sales, a man in a cap and suit jacket, next to a truck loaded with bricks; and at the customer site with Product, a woman with a ponytail holding a rolled-up plan.
    - Text: "ALLY"
    - Notes (talk track): Other functions' capacity can become yours. Engineering can't win alone, and the partners who trust you will spend their capacity on your goals.
      - Product: a partner, not a requester. You plan the roadmap together, they cut scope with you instead of around you, and they bring you to the customer.
      - Sales: they tell you which deals need what, months before the contract is signed, and they don't sell the feature you haven't built. In return, you give them dates you actually hit.
      - Also: the platform team that adds the API you need if they hear about it a quarter ahead, and the recruiter who moves faster on your hires.
      - Alliances are built before you need them, not during the crisis.

### Fund

34. **Fund** · Comic
    - Comic: In an office, the Manager points at a rising bar chart on an easel and holds out an empty hand; behind a desk, the CEO in his general's uniform, aviator sunglasses and stubble hands him a money bag marked $. Through the window, a pickup truck waits next to a pile of bricks.
    - Text: "FUND"
    - Notes (talk track): Headcount and budget are capacity, and you have to earn them.
      - A hiring plan and a comp plan that tie each dollar to an outcome the CEO cares about.
      - Stay on budget, and share bad news early. Nothing builds CEO trust faster.
      - Ask for the truck with a business case: what it costs, what it unlocks, when it pays back.
      - Start small and earn more: a two-day draft, reviewed together, then sharpen the numbers.
      - Every yes from the CEO is spent from trust you built earlier.

## Close

35. **OMG, how do I do all that?** · Comic (callback to slide 3)
    - Comic: The same seminar room as slide 3, at the end of a long day. The screen reads OMG, HOW DO I DO ALL THAT? above a long scribbled list. The three audience members are slumped in their chairs, exhausted and sweating. The Manager is exhausted too: hair disheveled, tie loosened and askew, pointer drooping.
    - Text: "OMG, HOW DO I DO ALL THAT?"
    - Notes (talk track): Twenty buckets. Nobody does all twenty every week, and nobody should try. I don't. In any given week, two or three of them matter, and the rest can wait. The hard part isn't knowing the buckets; it's knowing which two or three this week, because the world keeps changing under you.

36. **Bad news** · Comic
    - Comic: The same exhausted seminar room. A door on the left opens a crack, and a nervous engineer peeks in, sweating: UM, BAD NEWS SIR... The audience and the Manager all turn toward the door, wide-eyed.
    - Text: "UM, BAD NEWS SIR..."
    - Notes (talk track): Let it sit for a second. You will get this message on the day you finally have a plan you like. Every manager has had the Slack DM that starts with "hey, got a minute?" at 4:55 on a Friday. It's not a sign the plan was bad. It's what the job actually looks like.

37. **Project status (corporate)** · Corporate template + chart
    - Same template as slides 1–2. Title: "Project Status: H1 Delivery Burndown". Subtitle: "Board: ENG-CORE · Sprints 1–13 · Estimation: Story Points".
    - Chart: the project data from tools/chaos_chart.py, drawn as a bland Jira burndown that burns down on weekdays only (flat on weekends): gray straight Guideline, blue stepped Total Scope, red stepped Remaining Values, green stepped Velocity (Story Points / Day) on a right axis, pale gray non-working-day bars, dates on the x-axis, legend at the bottom. Plotted with tools/jira_burndown.py.
    - Notes (talk track): Read it in your most monotone voice. Reality is incredibly messy: unpredictable things happen all the time. This is how half a year of it looks in the status meeting: two bumps and a line that hits zero. All the chaos is in there; you just can't see it anymore.

38. **Key Responsibilities: Summary (corporate)** · Corporate template
    - Two lists of ten bland corporate bullets, one per bucket, without the bucket verbs.
    - 1. Winning: Ensure alignment of deliverables with key stakeholder objectives · Right-size scope to optimize time-to-value · Conduct proactive risk assessment and discovery · Drive timely decision-making across workstreams · Optimize resource allocation against priority initiatives · Monitor execution and course-correct as needed · Remove impediments and mitigate external dependencies · Foster team engagement and ownership of outcomes · Mobilize cross-functional resources for critical milestones · Contribute directly to delivery as bandwidth permits.
    - 2. Increasing the Capacity to Win: Execute on headcount plan to address capability gaps · Invest in talent development and career pathing · Empower leads through structured delegation frameworks · Implement competitive total rewards and recognition programs · Proactively manage underperformance · Optimize organizational design and operating model · Leverage automation to drive operational efficiencies · Champion a culture aligned with company values · Build strategic cross-functional partnerships · Secure budget and resourcing in line with business case.
    - Notes (talk track): Don't read it. Let the room scan it for a few seconds. Every one of these is a slide we just did, with all the life squeezed out. This is what the job description says.

39. **Key Takeaway (corporate)** · Corporate template
    - Text: "Your job is to deliver, regardless of the chaos."
    - Notes (talk track): Flat, like the cover. Pause. It's true, and it sounds like nothing. Then click.

40. **So have fun!** · Comic
    - Built as an exact copy of the Key Takeaway slide (39) with two transparent PNG overlays on top (a speech bubble, and the torn hole with the Manager), so the slide underneath is guaranteed identical. Overlays were generated on chroma-key green and keyed out with tools/chroma_key.py.
    - Comic: the stick-figure Manager bursts through a jagged hole in the slide like a football player through a banner, scraps flying, grinning and winking, fist forward and thumb up.
    - Text: "SO HAVE FUN!"
    - Notes (talk track): Drop the corporate voice. It's the hardest job I know and the most fun I've had. Thank you.

## Parking lot

- **Zoom out** (proposed ending, not in the deck) · Comic → Map
    - Comic: Manager staring at one cracked brick. Pull back: the whole map.
    - Text: "Don't lose the forest for the bricks."

- **Turn 1 vs Turn 52** (proposed ending, not in the deck) · Map 16 (final)
    - Map: split view. Left: Turn 1's dotted footpath with a tally of 37. Right: Turn 52's road network, bridges, convoys and several flags reached, with fog still at the edges.
    - Text: "Win this turn. Win bigger every turn."

- **Unplaced intro slides (not built yet).** Kept from earlier drafts; decide where (or whether) they go:
  13. **The map legend** · Map key
      - Comic: a hand-drawn map key, each icon paired with its software meaning:
        - brick = a feature / unit of value
        - B (flag) = what the customer actually needs
        - road = infrastructure, CI/CD, platform
        - truck = tools, automation, AI
        - fog = unknowns: requirements, tech, market
        - mountain = the wrong technical approach
        - river = the surprise integration, bug, or dependency
        - explorer = a spike / prototype
        - "wrong bricks" = built the wrong thing
      - Text: the legend itself.

  14. **Where the analogy breaks** · Comic
      - Comic: bricks sitting at B start growing moss, cracks and a little dragon tail (a callback to the code dragon from the eng-teams deck).
      - Text: "Unlike bricks, code you've shipped still needs care."

  15. **The map** · Map 1
      - Map: A on the left, one B flag on the right, everything between them fogged in. Tag: TURN 1.
      - Text: "Here's the map. It's mostly fog."

  16. **One turn = one week** · Comic
      - Comic: the team lines up at A as a big hourglass is flipped over.
      - Text: "Every week, you get one turn."

- "Commitment / work hard together" (team pushing a stuck truck through the rain). Could fold into Assign, or go in a later deck.
- "Less randomness" map (scattered footprints vs. aligned arrows). Could fold into Aim.

## Open questions
- Slide 24 (winning tools that borrow from capacity) is proposed: keep it? Escalate / borrow-a-truck is not placed yet.
- Is the map the *only* recurring image (like the eng-teams system diagram), or do we also cut to a ground-level "brick yard" view?
- 36 slides for a 1-hour seminar. Each bucket gets its own future deck, so we could trim each bucket here to one slide.

## TODO
- **Idea: B is huge and very far away.** The B flag is actually VERY LARGE and VERY FAR away, so we misjudged the distance entirely. (Not used yet: ask before finishing.)
- **Idea: find the REAL scope.** Manager talking to the customer: "Are you SURE you won't need more bricks to build your palace?" Figure out the real scope instead of the passed-down scope. (Not used yet: ask before finishing.)
- **Idea: scope-creep chart.** Reuse the composited "two jumps" chart (asset `/_blob/812329caedcc24cb1155e2cbcac9ffb2`, sweating room): remaining MoBs jumps back up twice, "B FLAG MOVED" and "CUSTOMER ASKED FOR MORE BRICKS". Could pair with the palace / real-scope idea. (Not used yet: ask before finishing.)
- **Idea: end the talk with Trust.** It doesn't fit any of the buckets, but it matters a lot. Why and how? (Not used yet: ask before finishing.)

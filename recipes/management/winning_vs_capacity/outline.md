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
3. **Scout:** de-risk the unknown before the convoy commits. Send an explorer, build a spike, check whether the river has a ford.
4. **Decide:** make the call now. Teams lose whole days waiting on decisions nobody has made.
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

13. **How to win** · Comic (tiles generated one by one, grid composed by hand)
    - Comic: title "HOW TO WIN" over ten framed tiles, the Manager in each: AIM (picture of a finished brick house next to flag B), TRIM (giant scissors cutting the pile in half, one half X'd out), SCOUT (binoculars at fog), DECIDE (pointing down one fork of the road), ASSIGN (hands out a hard hat; three engineers swarm a huge brick), STEER (flags B, C, D; turns a wheelbarrow toward B), CLEAR & PROTECT (a crop of slide 20: chops a fallen trunk while bandits drag an engineer into the forest), MOTIVATE (megaphone, late at night), FIRE DRILL (alarm bell rings; sales and design carry bricks), CARRY (carries one brick himself).
    - Text: "HOW TO WIN" / "AIM" "TRIM" "SCOUT" "DECIDE" "ASSIGN" "STEER" "CLEAR & PROTECT" "MOTIVATE" "FIRE DRILL" "CARRY"
    - Notes (talk track, yours): each of these can be a whole course by itself. We lightly touch each one and give examples, so you can pattern-match your activities to the bucket they fall into.

### Aim

14. **Aim** · Comic (vector doodle drawn on top by hand)
    - Comic: the team happily carries bricks to the right, toward an EMPTY hole signed "B (MONDAY)". From there, footprints make a big U-turn: up past "B (TUESDAY)" and "B (WEDNESDAY)", then all the way back left, where the customer (baseball cap) is planting the real B flag behind the team. Top doodle: a solid arrow right, "WHAT WE CARRIED"; a dashed arrow left, "TO THE REAL B"; "MoBs THAT COUNT: < 0".
    - Text: "AIM" / "WHAT WE CARRIED" / "TO THE REAL B" / "MoBs THAT COUNT: < 0" / "B (MONDAY)" "B (TUESDAY)" "B (WEDNESDAY)"
    - Notes (talk track, yours): goals move all the time, for lots of reasons. The team's work only matters if it takes you *in the direction of the goal*; even a little off-track wastes effort. Figuring out the actual goal makes THIS WEEK's work maximally productive.

### Trim

15. **Trim** · Comic (one panel, split down the middle)
    - Comic, right half: the customer's bubble shows a huge fairy-tale castle (picture, no words). The Manager answers with a bubble showing a small simple house (picture, no words). A brick pile at their feet.
    - Comic, left half: two engineers kneel, assembling a wheelbarrow from parts (loose wheel, wrench, screws, blueprint) next to an untouched brick pile. The same Manager: "JUST CARRY THE DAMN BRICKS".
    - Text: "TRIM" / "JUST CARRY THE DAMN BRICKS"
    - Notes (talk track): two kinds of scope to cut. Product scope: what the customer asked for vs. what they actually need this quarter. Approach scope: the framework, platform or automation we would love to build first. Building tools is capacity, not winning, so do it on purpose, not by accident.
    - Notes, examples:
      1. Product scope. The customer asked for a full analytics dashboard: filters, charts, scheduled emails. The question "what decision is this for?" turned up one weekly number for the CFO. A nightly CSV export shipped in two days.
      2. Product scope. The spec said "supports every payment type". The data said 97% of transactions were cards. Launch with cards, a month early; add the next type when a real customer asks.
      3. Product scope. The plan included a full admin UI for config, roles and audit logs. The only users were three internal engineers. A documented script and a config file in the repo did the job and saved six weeks.
      4. Approach scope. A request for one flag on one machine turned into a design for tiered config with merge rules and a new admin UI. Someone asked, "any objection to the hackiest possible approach?" A one-off override solved it that day.
      5. Approach scope. An engineer wanted a generic plugin system first, so integrations would be "easy forever". There was one integration on the roadmap. Hard-code it; build the abstraction from three real examples later, not zero.
      6. Approach scope. Support wanted an edge case automated before launch. How often does it happen? About once a week. Keep it manual for now, and launch.
      7. The other side. A simple database index was suggested early and passed over because the tests weren't representative. Seven weeks later, under production load, the same index took the query from 4.5 s to 0.7 s.
      - Caveat: a trimmed feature still has to be usable. Call phase 1 a partial feature, not GA.

### Scout

16. **Scout** · Comic (top-down map)
    - Comic: a hand-drawn top-down map of a forest. Three roads start at the bottom middle: the left one winds into the mountains and ends at an X; the middle one goes straight up and ends at an X; the right one loops around, crosses the river on a bridge and reaches flag B at the top middle. At the fork the Manager points up the right road; a line of engineers carries bricks along it.
    - Text: "SCOUT" / "THIS WAY!" / "B"
    - Notes (talk track): Before you commit the team for a month, spend a few days finding out which approach dead-ends.
      - Spike the vendor or POS API for two days before promising the integration date: auth quirks, rate limits, missing endpoints.
      - Prototype the hard part first (latency, the hardware constraint, the model accuracy), not the easy UI.
      - Ask who tried this before. The team that attempted it last year knows where it broke.
      - Read the customer's actual setup (network, hardware, existing POS) before estimating.
      - Send one engineer for a few days, not the whole team for a sprint. The obvious approach is often the one nobody has taken end to end.

### Decide

17. **Decide** · Comic
    - Comic: at a fork, two engineers holding bricks argue, one pointing left into a dark forest ("FOREST!"), the other right up the mountains ("MOUNTAINS!"). Between them the Manager calmly points up the mountain road: "MOUNTAINS. GO." Nearby, a big untouched brick pile and four engineers sitting with popcorn, watching instead of working.
    - Text: "DECIDE" / "FOREST!" / "MOUNTAINS!" / "MOUNTAINS. GO." / "POPCORN"
    - Notes (talk track): Teams lose days, sometimes weeks, waiting on decisions nobody owns. The cost isn't the two people arguing; it's everyone blocked behind them.
      - Two senior engineers debate the data model for two weeks while the rest of the team can't start.
      - A design review ends with "let's take this offline" for the third time.
      - A PR sits blocked on an architecture argument in the comments.
      - "Which customer first?" goes unanswered, so people pick their own.
      - Most technical decisions are reversible. Set a deadline for the decision, hear both sides, make the call, write down why, and revisit if new data shows up. Disagree and commit.

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
    - Comic: three flags in the distance, B, C and D, each with a yelling customer: "100 MONDAY!" at B, "50 FRIDAY!" at C, "10 TUESDAY!" at D. The Manager stands where three paths fan out, arms spread: a wheelbarrow full of bricks goes toward B, an engineer carrying 10 bricks goes toward D. The path to C is empty for now.
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
    - Comic: the Manager on a crate, arms wide, tells a story; his speech bubble shows a huge castle surrounded by dollar signs and money bags. Two grinning engineers grab bricks from the pile at his feet; three more run right, away from him, with bricks. Far away at the end of the road: a small wooden shack next to flag B.
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
    - Comic: flat side view. A red alarm bell rings on a small brick factory at the far left ("RING! RING!"); the sweating Manager shouts and waves everyone forward. A single-file line walks left to right toward a big flag B at the far right, each carrying a brick: a secretary with a headset, a dog (brick in its mouth), a big boss with a cigar looking surprised, an accountant with a calculator, a salesperson and an engineer in a hard hat who has almost reached B.
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
      - Triage the bug backlog: reproduce, find the root cause, open the PR.
      - Build the internal dashboard or report ops has asked for twice.
      - Review PRs faster, with the agent explaining the diff.
      - What hasn't changed: stay off the critical path. Carry the work that would otherwise never get done, not the work that blocks the team if you disappear for a day.

### Wrap-up (proposed, unnumbered)

- **Some winning tools borrow from capacity** · Comic (proposed)
    - Comic: the Manager wins this week's tally, but a small "IOU" note flies off to next week: tired people (overtime), pulled people (rally), cracked bricks (cut corners / tech debt).
    - Text: "Some wins borrow from next week."
    - Notes (talk track): bridge into Part 2. Winning tools that spend capacity are fine, as long as you know you're spending it.

## Part 2 — Capacity (future turns)

24. **How to increase capacity** · Comic (tiles generated one by one, grid composed by hand)
    - Comic: title "HOW TO INCREASE CAPACITY" over ten framed tiles, the Manager in each: HIRE (shakes hands with new arrivals holding truck keys, a blueprint, an axe), GROW (one engineer goes from one brick to a wheelbarrow to a truck), DELEGATE (hands his megaphone to a new lead with a crew), REWARD (money bag and a medal), PRUNE (a line of brick carriers; needs a redraw), ORGANIZE (three crews in separate lanes, a MAKE → CARRY → STACK board), AUTOMATE (presses the button on a brick conveyor belt; two engineers high-five), CULTIVATE (waters a young tree while engineers build a neat wall behind him), ALLY (shakes hands with a neighboring town's leader; their truck carries our bricks), FUND (pitches a bar chart to the big boss, who hands over truck keys and a money bag).
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
    - Comic: The same engineer, four times along a road, getting bigger each time: carrying one brick, pushing a wheelbarrow, driving a truck, then drawing a bridge at a drafting table. The Manager walks alongside, handing over the next tool each time.
    - Text: "GROW"
    - Notes (talk track): this could be a whole set of talks. Three parts:
      1. Opportunities: give people work one size bigger than their last job. The mid-level engineer leads the next design review; the senior engineer owns the launch.
      2. Mentorship: show how to do the job. Do it together first: you run the incident review while they watch, then they run it while you watch.
      3. Coaching: support them while they do the job on their own. Weekly 1:1s, feedback within days, and questions instead of answers.

### Delegate

27. **Delegate** · Comic
    - Comic: The Manager stands on a hill handing his megaphone to a proud engineer in a hard hat. Below, on two roads, two new leads with megaphones each direct their own crew carrying bricks.
    - Text: "DELEGATE"
    - Notes (talk track): At some point your own hours are the bottleneck. Delegating is how one manager's capacity becomes several.
      - Tech leads who own the technical calls, so design decisions don't queue behind you.
      - A second-in-command who can run the team for two weeks while you're out, and actually does it.
      - Hand off whole problems (the release process, the on-call rotation), not tasks.
      - Let them do it differently than you would. If it's 80% as good and you didn't have to do it, that's a win.
      - The test: if you disappear for a week, does the team slow down?

### Reward

28. **Reward** · Comic
    - Comic: Payday at the brick yard: in front of the wall they built, the Manager hands envelopes marked with a dollar sign to a line of smiling engineers; the first also gets a medal pinned on, with sparkles.
    - Text: "REWARD"
    - Notes (talk track): "My job is to leave money in your pocket and memories in your head."
      - Pay fairly and proactively: fix the underpaid engineer before they get the outside offer, not after.
      - Equity and refreshers tied to impact, explained clearly.
      - Recognition that's specific and public: name the person and what they did, in the all-hands, not just in a DM.
      - Non-money rewards: the interesting project, the conference talk, the promotion case you write for them.
      - Money prevents a no. It rarely creates a yes.

### Prune

29. **Prune** · Comic
    - Comic: A line of engineers carries bricks right toward flag B; one person walks the wrong way, carrying bricks back, and the line jams around him. The Manager calmly guides him off the road toward a gate.
    - Text: "PRUNE"
    - Notes (talk track): Sometimes capacity goes up when someone leaves.
      - One person who blocks every review, or who the team quietly routes around, slows down everyone near them.
      - Values rarely change; skills can. Coach skill gaps. When it's values, move faster than feels comfortable.
      - Be clear early: written expectations, a real plan, a date. Nobody should be surprised.
      - "Not firing fast enough" is one of the most common regrets of experienced managers.
      - Do it with dignity. The rest of the team is watching how you treat people on the way out.

### Organize

30. **Organize** · Comic
    - Comic: A wide road split into three lanes by dashed lines: one crew makes bricks at a kiln, one carries them, one stacks them into a wall, handing bricks across at marked points. The Manager points at a whiteboard showing MAKE, CARRY, STACK.
    - Text: "ORGANIZE"
    - Notes (talk track): The shape of the team decides how much it can do.
      - Clear ownership: every service, every alert and every customer issue has one team that owns it.
      - Small teams with few dependencies ship faster than one big team with many.
      - Few, explicit handoffs: product to engineering, engineering to QA, QA to support.
      - An on-call rotation that doesn't burn out the same two people.
      - Just enough process: a weekly plan, a retro, a postmortem. Kill the meetings nobody would miss.

### Automate

31. **Automate** · Comic
    - Comic: The Manager and engineers in hard hats build a long conveyor belt for bricks; the finished half already carries bricks while the rest is still scaffolding. Next to it, the rest of the team keeps carrying bricks by hand.
    - Text: "AUTOMATE"
    - Notes (talk track): Every hour of toil you remove pays back every week after.
      - The page that costs an hour a week and takes 12 hours to fix pays back in 12 weeks. Fix it.
      - CI that takes 40 minutes taxes every PR, every day.
      - Deploys that need a person and a checklist become deploys that need a button.
      - Pay down the tech debt that slows every feature, not the debt that just looks ugly.
      - AI agents on the repetitive work: test writing, migrations, triage.
      - Build it while you keep shipping. Stop delivering to build the perfect tool, and you lose the week and the trust.

### Cultivate

32. **Cultivate** · Comic
    - Comic: The Manager walks off down the road with a suitcase, waving goodbye. Behind him, unwatched, the team keeps building a neat, straight wall: one checks it with a level, one helps lift a heavy brick, one pulls out a crooked brick to redo it. A young tree grows beside the wall.
    - Text: "CULTIVATE"
    - Notes (talk track): Culture is what happens when you're not in the room.
      - Define it in a few words people can act on, like "Rigorously Get Shit Done": rigor, and done means the customer's problem is solved.
      - Reward what you say you value. If you say quality but celebrate only speed, the team learns speed.
      - Model it: the postmortem without blame starts with your own mistake.
      - Hire and fire by it. Who you let in, and who you let stay, is the culture.
      - It's slow to build and fast to lose.

### Ally

33. **Ally** · Comic
    - Comic: At a crossroads between our brick yard and a neighboring town, the Manager shakes hands with the town's leader, who wears a hat. The neighbor's truck, loaded with our bricks, drives along their highway toward flag B.
    - Text: "ALLY"
    - Notes (talk track): Other people's capacity can become yours.
      - The platform team that adds the one API you need, if they know about it a quarter ahead.
      - The head of Product as a partner, not a requester: you plan the roadmap together.
      - HR and your recruiter, who can move faster on your hires if they trust you.
      - Your boss: make their job easier, and they'll spend their capital on your team.
      - Vendors and open source: don't build what you can buy.
      - Alliances are built before you need them, not during the crisis.

### Fund

34. **Fund** · Comic
    - Comic: In an office, the Manager presents a rising bar chart on an easel to the big boss behind a desk; the boss, smoking a cigar, hands over truck keys and a money bag. Through the window, a new truck waits next to a pile of bricks.
    - Text: "FUND"
    - Notes (talk track): Headcount and budget are capacity, and you have to earn them.
      - A hiring plan and a comp plan that tie each dollar to an outcome the CEO cares about.
      - Stay on budget, and share bad news early. Nothing builds CEO trust faster.
      - Ask for the truck with a business case: what it costs, what it unlocks, when it pays back.
      - Start small and earn more: a two-day draft, reviewed together, then sharpen the numbers.
      - Every yes from the CEO is spent from trust you built earlier.

## Close

35. **Zoom out** · Comic → Map
    - Comic: Manager staring at one cracked brick. Pull back: the whole map.
    - Text: "Don't lose the forest for the bricks."

36. **Turn 1 vs Turn 52** · Map 16 (final)
    - Map: split view. Left: Turn 1's dotted footpath with a tally of 37. Right: Turn 52's road network, bridges, convoys and several flags reached, with fog still at the edges.
    - Text: "Win this turn. Win bigger every turn."

## Parking lot
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

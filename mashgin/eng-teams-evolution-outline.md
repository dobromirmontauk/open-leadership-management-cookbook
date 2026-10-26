# Evolution of an Engineering Team — slide outline

Cleaned-up order of the scratch notes in `how-do-eng-teams-work.md` (plus the whiteboard).
Deck: https://claude.ai/artifact/1DQQ4MvuFaX2ebhF95uyBc

## Live deck order (81 slides, synced 2026-10-21)

1. `cover` — cover
2. `part1` — Part 1: How an Engineering Org Grows.
3. `state-01` — One engineer, one idea.
4. `state-02` — Putting it online.
5. `state-03` — Building it out.
6. `state-04` — A visitor… who leaves.
7. `state-05` — Build more, try again.
8. `state-06` — A customer stays.
9. `state-07` — state-07
10. `state-08` — state-08
11. `state-09a` — state-09a
12. `state-09b` — state-09b
13. `state-09c` — It breaks when nobody’s watching.
14. `state-10` — A second engineer.
15. `strip-05` — Two engineers ≠ twice as fast.
16. `state-11` — Phone lines multiply.
17. `state-12` — A Product Manager.
18. `state-13a` — The feature loop: out with customers.
19. `state-13b` — The feature loop: the Product Plan.
20. `state-14b` — Two teams, and a TL/M in the middle.
21. `state-15` — A bug in production.
22. `state-16` — A test step: QA joins.
23. `state-17` — Four teams, three PMs, one manager.
24. `state-18` — Enter the Architect.
25. `state-19` — The dragon, slain (four times smaller).
26. `state-20` — QA splits, Support arrives.
27. `state-21` — A release catches fire.
28. `state-22` — Air traffic control for releases.
29. `state-23` — Who’s on call?
30. `state-24` — Enter the SRE.
31. `state-25` — Head of Product.
32. `state-25b` — Oh, and don’t forget…
33. `part-why` — Part 2: Why It’s So Hard.
34. `cap-intro` — The CAP theorem.
35. `cap-consistency` — Consistency: everyone knows the same thing.
36. `part-pto` — Partition: on vacation.
37. `part-quit` — Partition: gone for good.
38. `part-busy` — Partition: just busy.
39. `cap-avail` — Availability: work never stops… right?
40. `why-cap` — The CAP theorem.
41. `sig-right` — Everyone has a different “right thing”.
42. `sig-clarity` — …and every signal arrives differently.
43. `sig-shipped` — …and that’s why.
44. `failure-modes` — Part 3: Avoiding Complete Chaos.
45. `storm-knowledge` — Storm 1 of 4: Knowledge.
46. `fail-conflict` — Merge conflicts in our heads.
47. `fix-conflict` — Continuous conflict resolution.
48. `fail-hero` — The hero dependency.
49. `em-stuck` — Cross-training to remove siloes.
50. `storm-direction` — Storm 2 of 4: Direction.
51. `state-26` — Strategy nobody understands.
52. `fix-strategy` — Strategy is a filter.
53. `fail-priority` — What’s the top priority?
54. `fix-priority` — One prioritized list, out in the open.
55. `fail-ceo` — The CEO side door.
56. `proc-xfn` — Cross-functional goal meetings.
57. `storm-structure` — Storm 3 of 4: Structure.
58. `finale-mob` — Everyone wants something.
59. `fix-frontdesk` — One front desk.
60. `finale-pingpong` — Let me find out…
61. `fix-skip` — Sometimes, shortcut through the structure.
62. `fail-warroom` — fail-warroom
63. `fix-owners` — Every team owns its own piece.
64. `storm-comms` — Storm 4 of 4: Communication.
65. `fail-telephone` — The promise that got lost.
66. `solve-broadcast` — Beating the telephone game.
67. `fail-meetings` — Meeting creep.
68. `solve-batch` — Fixing meeting creep.
69. `finale` — Same Rock, Same Direction.
70. `cast-biz` — Meet the cast: the team around engineering.
71. `cast-eng` — Meet the cast: the engineers.
72. `appendix` — Appendix.
73. `part3` — Part 4: The EM’s Responsibility.
74. `em-vp` — Isn’t this the VP’s problem?
75. `em-router` — Who needs to know what, when, and why?
76. `proc-goals` — Shape process to fit goals.
77. `proc-standup` — Standups and virtual teams.
78. `em-recap` — The EM’s checklist.
79. `fail-reorg` — Reorg whiplash.
80. `fix-rewire` — Change the wiring slowly.
81. `todo` — todo

## How the slides work

- **State slides** all show the *same system diagram*. Each one adds or changes one thing, so
  clicking through looks like the team evolving (and later animates as a morph).
- **Strip slides** are short comics *between* states. We only add one when a change needs a
  story to make sense. Default: no strip.
- **Fixed layout for every state diagram.** Nothing moves once it's placed:
  - **Left third:** the engineering team, inside a hand-drawn "TEAM" box (it splits into
    several boxes later).
  - **Inside the TEAM box:** the **CODE DRAGON**, a baby dragon with a "CODE" box on its belly,
    sitting by the engineer's desk like a pet. It grows on every slide: adorable at first, then
    a young dragon with spikes and a mischievous grin, and eventually a huge, genuinely scary
    beast that fills the TEAM box. When the team splits (slides 23–25), the dragon is what they
    have to untangle and cut in two.
  - **Center:** reserved for the pipeline, which fills in one step at a time: `RELEASE`
    (slide 8), `TEST` (slide 18), `BUILD` and more (slide 26).
  - **Right:** the `ONLINE` box (later relabeled `PRODUCTION`), then `CUSTOMERS` at the far
    right edge.
  - **Top band:** people between the team and the customers (PM, Design, Support, Sales…).
  - **Top-left corner:** the running props (the engineers' backlog; later, the PM's *Product
    Plan*).
  - **Feedback arrows:** customer complaints arc over the TOP back to the engineer. Production
    alerts run along the BOTTOM: PRODUCTION → DEVOPS (PagerDuty) → the phone on the floor.
- **Running props that change across states:**
  - **Backlog:** sticky notes (1–3) → a page → several pages with items falling off.
  - **Product Plan:** an official-looking bound book that the PM holds. It's separate from
    the engineers' backlog.
  - **Phone lines:** brain-to-brain lines between people, which multiply as the team grows.
  - **Brain:** the head stays normal size early on and gains one small squiggle per slide
    (1, 2, 3, 4…). Later the squiggles turn into tangles and the head starts to balloon, a lot.
    The 2nd engineer doesn't join until there are quite a few tangles. New engineers start with
    a clean, normal-size head.
  - **Small mouths, smaller ears:** once there are 2+ engineers, every engineer is drawn with
    tiny mouths and even tinier ears.

---

## Section 1 — One engineer

**1. One engineer, one idea** · State
- **Changed:** starting point. Normal head, no squiggles. The lightbulb is shown on slides 1–6
  only; it's gone once customer feedback starts (slide 7).
- **Introduced:** Engineer, an idea (lightbulb), a small `CODE` box.
- **Full comic:** No.

**2. Putting it online** · State
- **Changed:** the engineer just puts the code online, with one arrow from the CODE DRAGON to `ONLINE`.
  There's no test, no release, no QA and no customers yet. The head has 1 squiggle.
- **Introduced:** the `ONLINE` box (it becomes `PRODUCTION` later).
- **Full comic:** No.

**3. Building it out** · State
- **Changed:** the CODE DRAGON grows. The head has 2
  squiggles.
- **Introduced:** —
- **Full comic:** No.

**4. A visitor… who leaves** · State
- **Changed:** a customer walks up at the far right, looks, shrugs ("MEH."), and walks off
  (dotted footprints). The head has 3 squiggles.
- **Introduced:** Customer.
- **Full comic:** No.

**5. Build more, try again** · State
- **Changed:** the code is clearly bigger, and the head has 4–5 squiggles. A second visitor
  leaves too, and the first visitor's footprints are still faintly there. (We can repeat this
  slide once more if we want a third round.)
- **Introduced:** —
- **Full comic:** No. *Option:* a 3-panel montage (build → a visitor comes → the visitor leaves)
  in place of the repeated slides.

**6. A customer stays** · State
- **Changed:** the code is large now. One customer stays and is happily using it. The
  squiggles start to tangle.
- **Introduced:** —
- **Full comic:** No.

**7. Now breaking it matters** · State
- **Changed:** putting new code online breaks it (an X on the CODE → `ONLINE` arrow). The
  customer is upset, and the first feedback arrow runs back to the engineer. More tangles.
- **Introduced:** the broken deploy, the feedback arrow.
- **Full comic:** No.

**8. A release step** · State
- **Changed:** the engineer adds a careful `RELEASE` box (a checklist) between the CODE DRAGON and
  `ONLINE`, in the center.
- **Introduced:** `RELEASE`.
- **Full comic:** No.

**9a. It's down!** · State
- **Changed:** `PRODUCTION` (renamed from `ONLINE`) is on fire. The customer: "IT'S DOWN?!". The
  complaint arcs over the *top* and makes the old rotary phone on the floor ring. The engineer
  sweats. There's no paging system yet: the customer *is* the alert.
- **Introduced:** fire, `PRODUCTION`, the floor phone.
- **Full comic:** No.

**9b. Let the system call you → PagerDuty** · State
- **Changed:** a **DEVOPS** box (PagerDuty pager) appears at the bottom, with arrows PRODUCTION →
  DEVOPS → the phone. The fire is out, the customer is calm, and the phone is quiet.
- **Introduced:** DevOps / PagerDuty.
- **Full comic:** No.

**9c. It breaks when nobody's watching** · State
- **Changed:** `PRODUCTION` is on fire again, but nobody is at the customer's computer. The
  fire is *not* a customer complaint: production breaks on its own. PagerDuty still rings the
  phone, and the engineer is still stressed.
- **Introduced:** —
- **Full comic:** No.

## Section 2 — It becomes a team

**10. A second engineer** · State + Strip
- **Changed:** a second engineer joins, once Engineer #1's head is quite tangled. Their head is
  almost empty. The **phone line** runs from Engineer #1's head straight into Engineer #2's
  brain. Both have small mouths and smaller ears. Adding this *first* new engineer is
  manageable; the pain grows with each one after that.
- **Introduced:** Engineer #2, phone lines.
- **Full comic:** **Yes** ("two engineers ≠ twice as fast"). Engineer #1 pours their tangled
  head down the phone line into the new one. It takes a while, and speed goes up, but by less
  than 2x.

**11. Phone lines multiply** · State
- **Changed:** four engineers, with 1–2 customers each (dashed lines over the top to "their"
  engineer). LOTS of phone cords converge brain-to-brain on the main engineer: his head is
  quite big, and he is very stressed. Engineer #2's head is busier, and #3 and #4 are almost
  empty. The CODE DRAGON sits in the middle of the team, middle-sized and starting to look a
  little scary. One engineer wears a "PM-LIGHT" badge, with a tiny 2–3 sticky-note backlog
  next to him. (This merges the old slide 13.)
- **Introduced:** Engineers #3 and #4, more customers, the PM-light badge, the backlog.
- **Full comic:** No.

*(Old slide 12, "Adding people to a late project", is cut.)*

## Section 3 — More customers

**12. A Product Manager** · State *(was 14–15)*
- **Changed:** the PM-light leaves the TEAM box for their own box titled **PM** in the top band,
  with a clipboard and the sticky-note backlog. ALL customer lines now go to the PM, and the PM
  has ONE phone line into each team (one team for now).
- **Introduced:** the PM box.
- **Full comic:** No.

**13a. The feature loop: out with customers** · State
- **Changed:** the PM box is empty; the PM is out among the customers, taking notes while they
  all ask for things ("CAN IT DO X?", "I NEED Y!", "WHAT ABOUT Z?", "ALSO...").
- **Introduced:** the feature loop.
- **Full comic:** No.

**13b. The feature loop: the Product Plan** · State
- **Changed:** the PM is back in the box hugging a huge PRODUCT PLAN book, with one phone line
  to the main engineer. The dragon is now huge and scary.
- **Introduced:** the product plan.
- **Full comic:** No.

**14. Two teams, and a TL/M in the middle** · State
- **Changed:** the TEAM box splits into two separate boxes, FRONTEND on top and BACKEND below.
  The main engineer moves into their own box on the left, labeled **TL/M**, with a much bigger
  brain and a phone to each team. The PM has one line, to the TL/M. Every engineer's head is
  busy. The code did *not* split: a two-headed dragon stands between the teams, one head looking
  at each, confused. Still one `PRODUCTION`.
- **Introduced:** Frontend, Backend, TL/M, the two-headed dragon.
- **Full comic:** No.

**15. A bug in production** · State
- **Changed:** a bug (drawn as a beetle) eats the PRODUCTION globe. Customers are up in arms
  ("IT'S BROKEN!", "FIX IT!", "AGAIN?!"), and the PM yells "WHY DIDN'T YOU CATCH THIS?!" Each team
  has three engineers now, the dragon has four heads (two breathing fire) and three tails, and
  the TL/M's head is gigantic: "I DON'T UNDERSTAND IT ANYMORE!"
- **Introduced:** bugs.
- **Full comic:** No.

**16. A test step: QA joins** · State
- **Changed:** a separate, tall `TEST` box appears right before `RELEASE`, with QA in it and an
  arrow from TEST to RELEASE. QA inspects the dragon (still between the teams) with a magnifying
  glass, and has a phone line back to FRONTEND and another back to BACKEND. The dragon is still
  huge and complicated, but meek, with no fire.
- **Introduced:** `TEST`, QA.
- **Full comic:** No.

**20. "How does this work?"** · State
- **Changed:** "?"s pile up over the customers. The PM has a lightbulb moment ("WE NEED A
  DESIGNER!"), and a Design box appears next to the PM. That's one more box to coordinate with.
- **Introduced:** Design.
- **Full comic:** No.

## Section 4 — Splitting the team

**21. More people, messier code** · State
- **Changed:** about 8 engineers, and the phone lines form a web. The CODE DRAGON is now big and
  scary, and its body is a tangle of spaghetti.
- **Introduced:** spaghetti code.
- **Full comic:** No.

**22. "It's just a button, right?"** · Strip *(already drawn)*
- **Changed:** —
- **Introduced:** —
- **Full comic:** this slide is the strip.

**24. Untangling the code** · Strip
- **Changed:** —
- **Introduced:** —
- **Full comic:** **Yes**, multi-panel:
  1. The teams debate.
  2. They keep debating, while the PMs and customers get bored and fall asleep.
  3. They trim around the edges.
  4. They finally cut the dragon's spaghetti down the middle.

**25. A clean seam** · State
- **Changed:** the dragon is split into two smaller dragons, each in its own team's box, joined by one
  clean leash (the interface). `PRODUCTION`
  is still one box.
- **Introduced:** the interface.
- **Full comic:** No.

## Section 5 — Specialists show up

**26. Releasing gets hard → DevOps grows** · State
- **Changed:** the pipeline grows `BUILD`, more environments and more boxes. The DevOps box
  (from slide 9b) becomes a person or team that owns it.
- **Introduced:** the DevOps person, `BUILD`.
- **Full comic:** No.

**27. The PM drowns in help requests → Support** · State
- **Changed:** Support sits between the customers and the PM. A red **FIRE!** line goes
  straight to the engineers. A grey "please fix this… someday" line goes to the PM.
- **Introduced:** Support.
- **Full comic:** **Yes**, 3 panels:
  1. Support: "PLEASE, PLEASE FIX THIS… SOMEDAY?"
  2. PM: "YES, YES, OF COURSE!"
  3. PM's thought bubble: "WE'LL NEVER GET TO THIS."

**28. More customers, more QA** · State
- **Changed:** QA multiplies to one per team.
- **Introduced:** —
- **Full comic:** No.

**29. Production needs its own team → SRE** · State
- **Changed:** `PRODUCTION` is a tangle of wires, and an SRE team works full-time untangling
  them.
- **Introduced:** SRE *(new character)*.
- **Full comic:** No.

**30. Customers want "intelligence" → Data/ML** · State
- **Changed:** a Data/ML team appears, with a data pipe from `PRODUCTION`.
- **Introduced:** Data / ML.
- **Full comic:** No.

**31. Someone broke in** · Strip
- **Changed:** —
- **Introduced:** Hacker *(new)*.
- **Full comic:** **Yes**, 3 panels:
  1. A hacker sneaks into `PRODUCTION`.
  2. Alarms go off.
  3. Security and Compliance arrive. Compliance carries a long list.

**32. Security & Compliance** · State
- **Changed:** a Security team appears. The Compliance list feeds into the *Product Plan*,
  which gets thicker.
- **Introduced:** Security, Compliance *(new)*.
- **Full comic:** No.

**33. Spaghetti, again → Architect** · State
- **Changed:** there are now 4–5 teams, and the code between them is spaghetti again. An
  Architect stands above all the teams.
- **Introduced:** Architect.
- **Full comic:** No.

**34. The shield** · State
- **Changed:** the engineers are ringed by Support (holding the fires back) and Product
  (holding the customers back). Inside the ring, the engineers say "HUH… THERE REALLY ISN'T
  ANYTHING TO DO…"
- **Introduced:** —
- **Full comic:** No (a one-panel gag on top of the state).

## Section 6 — How the team decides what to do (three loops)

**35. Three loops** · State (new diagram: the whiteboard spiral)
- **Changed:** zoom out to three nested loops: **Fires** (hours) inside **Tactical** (days to
  weeks to months) inside **Strategic** (quarters and longer).
- **Introduced:** the loop diagram.
- **Full comic:** No.

**36. Loop 1 — Fires** · State
- **Changed:** fires come from everywhere: the pager from production, QA filing bugs, Support
  escalating, and the PM, Manager or CEO posting "a Reddit thread". The timescale is hours.
- **Introduced:** the pager.
- **Full comic:** No. Make it one busy panel.

**37. Loop 2 — Tactical** · State
- **Changed:** "What are we doing this… day? week? month?" Standups, weekly planning and
  monthly goals.
- **Introduced:** —
- **Full comic:** No.

**38. Loop 3 — Strategic** · State
- **Changed:** the CEO, PMs, EMs and the head of Sales debate around a table, and the
  *Product Plan* sits in the middle.
- **Introduced:** —
- **Full comic:** No.

---

## Open questions

1. **Slide 34 ("nothing to do"):** is this the payoff (the layers work, so engineers get
   focus)? Or a warning (too much protection, and the engineers are cut off from customers)?
   It's placed as the payoff for now.
2. **EM:** I added it at slide 23, from the whiteboard (EM → team, "comm structures"). The
   notes don't place it. The pointy-haired Manager plays the EM.
3. **DevOps vs SRE:** the notes have both. DevOps (slide 26) owns the release pipeline, and
   SRE (slide 29) owns production. SRE needs a new character.
4. **The whiteboard's right side** (the real team names: Integrations, CAT, O.C., Vision…):
   leave it out, or add an epilogue mapping the story onto our actual teams?

## New characters needed

**Customer** (drafted: a plain figure in a baseball cap), **SRE**, **Compliance**, **Hacker**.

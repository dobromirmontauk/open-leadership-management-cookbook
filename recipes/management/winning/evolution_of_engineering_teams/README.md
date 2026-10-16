# The Evolution of Engineering Teams

A stick-figure talk about how engineering teams grow, and why they behave the way they do. It's for people who work with engineering teams but haven't been inside one, and for new managers who want the "why".

It follows one product from a single engineer with an idea to four teams, a dozen supporting roles, and two ways it can all go wrong. Along the way the code becomes a dragon: cute at first, then big, scary and tangled, until it gets split up.

## Downloads

| Slides (PDF) | With speaker notes (PDF) |
|---|---|
| [PDF](exports/The%20Evolution%20of%20Engineering%20Teams.pdf) | [PDF](exports/The%20Evolution%20of%20Engineering%20Teams%20%28speaker%20notes%29.pdf) |

## Slides

![Slide 1](slides/01.jpg)

> Opening. Who this is for: people who work with engineering teams but haven’t been inside one, and new managers who want the “why” behind how these teams behave.

![Slide 2](slides/02.jpg)

> Meet the cast: the team around engineering. The people engineering works with every day. Each one pulls the team in a different direction: the CEO sets the vision, Product decides what to build, Design how it should feel, Sales what was promised, Support what’s broken right now, and QA what’s broken before anyone else finds it.

![Slide 3](slides/03.jpg)

> Meet the cast: the engineers. “Engineer” isn’t one job. Frontend builds what you see, backend what you don’t, DevOps keeps it running at 3am, Data/ML turns data into decisions, Mobile lives in the app stores, Security assumes everyone is an attacker, and the Architect worries about how it all fits together in two years.

![Slide 4](slides/04.jpg)

> One engineer, one idea. State 1. One engineer, one idea, and the code they make: a cute little dragon. Remember the dragon. It grows.

![Slide 5](slides/05.jpg)

> Putting it online. State 2. What changed: the engineer just puts the code online. No testing, no release process, no customers yet.

![Slide 6](slides/06.jpg)

> Building it out. State 3. What changed: the code grows, and so does what the engineer has to keep in their head. Still just a couple of squiggles.

![Slide 7](slides/07.jpg)

> A visitor… who leaves. State 4. What changed: the first visitor shows up, looks, and leaves. Most early products go through several rounds of this before anyone stays.

![Slide 8](slides/08.jpg)

> Build more, try again. State 5. What changed: more building, another visitor, another “nah.” The code keeps growing even when nobody is using it yet.

![Slide 9](slides/09.jpg)

> A customer stays. State 6. What changed: finally, someone stays. The code is a lot bigger now, and it’s starting to have a personality of its own.

![Slide 10](slides/10.jpg)

> Now breaking it matters. State 7. What changed: broken code still went online, and now someone noticed. The complaint goes straight back to the one engineer, who is sweating. This is the first feedback loop.

![Slide 11](slides/11.jpg)

> A release step. State 8. What changed: the engineer adds a careful release step, a checklist between the code and what customers see. It’s the first piece of process, and it exists because something broke.

![Slide 12](slides/12.jpg)

> It’s down!. Slide 9a. What changed: production is down, and the only alarm is the customer calling the engineer’s phone. The customer is the monitoring system.

![Slide 13](slides/13.jpg)

> Let the system call you. Slide 9b. What changed: the engineer sets up DevOps alerting (PagerDuty), so production can call the phone directly instead of waiting for a customer to notice.

![Slide 14](slides/14.jpg)

> It breaks when nobody’s watching. Slide 9c. What changed: production breaks with nobody using it. No customer complained, and the phone rings anyway, because the system now calls the engineer on its own.

![Slide 15](slides/15.jpg)

> A second engineer. Slide 10. What changed: a second engineer joins with an almost empty head. Everything they need to know has to travel down one phone line from the first engineer’s head. Small mouths, smaller ears. It’s manageable, but it isn’t free.

![Slide 16](slides/16.jpg)

> Two engineers ≠ twice as fast. Strip before state 5. Everything the first engineer knows lives in their head, and it only leaves through a small mouth into even smaller ears. The new engineer’s ramp-up costs the old engineer’s time, so speed barely moves at first.

![Slide 17](slides/17.jpg)

> Phone lines multiply. Slide 11. What changed: four engineers and a handful of customers, and almost every line still runs to the original engineer, because everything is in his head. One engineer has started acting as a “PM-light” with a tiny backlog. The dragon is getting bigger, and a little less cute.

![Slide 18](slides/18.jpg)

> A Product Manager. What changed: the PM-light gets pulled out into their own job. Every customer now talks to the PM, and the PM has one line into the team. The main engineer gets some of his head back.

![Slide 19](slides/19.jpg)

> The feature loop: out with customers. The feature loop, part 1. The PM leaves the office and goes to the customers. Everyone has a request.

![Slide 20](slides/20.jpg)

> The feature loop: the Product Plan. The feature loop, part 2. The PM comes back with a very big book of things for engineering to build. One phone line into the team, and the book keeps getting thicker.

![Slide 21](slides/21.jpg)

> Two teams, and a TL/M in the middle. What changed: the team splits into frontend and backend, and the original engineer becomes the TL/M, in their own box, with a phone to each team; the PM now has one line, to the TL/M. Their brain is bigger than ever, because they’re the one who knows how both halves fit together. Each team’s heads are busy too. And the code didn’t split: the dragon sits between the teams, a head looking each way, and nobody is sure whose it is.

![Slide 22](slides/22.jpg)

> A bug in production. What changed: a bug gets into production. The customers are up in arms and the PM yells: why didn’t you catch this? Each team has grown, the dragon has grown more heads and tails, and even the TL/M, the one person who held it all together, admits: “I don’t understand it anymore!”

![Slide 23](slides/23.jpg)

> A test step: QA joins. What changed: a TEST box appears right before Release, and QA sits in it. Nothing ships until it passes TEST, and QA has a phone line back to each team to report what they find. The dragon is still huge and complicated, but under the magnifying glass it behaves itself: no more fire.

![Slide 24](slides/24.jpg)

> Four teams, three PMs, one manager. What changed: lots more customers, so the PM role grows to three. Engineering is now four smaller teams surrounding the same dragon, and each team has grown its own big-brain engineer. The original big-brain engineer has become a manager. Every team still needs a phone line to every other team, because they all share one dragon: count the cords.

![Slide 25](slides/25.jpg)

> Enter the Architect. Same picture, one new character. The Architect looks at the tangle of phone lines and sees the real problem: everyone has to talk to everyone because they all share one giant dragon. “We must slay the dragon!”

![Slide 26](slides/26.jpg)

> The dragon, slain (four times smaller). What changed: the big dragon is split into four medium dragons, one per team, and each team gets its own Release → Production → PagerDuty loop. One QA person still tests for everyone. The phone-line mess is gone. The Architect is delighted, and the Manager’s brain has shrunk to a classic pointy-haired boss. But the untangling took a long time: the customers fell asleep, and the PMs are shouting “Is it done yet?!”

![Slide 27](slides/27.jpg)

> QA splits, Support arrives. What changed: one QA person can’t keep up with four teams, so QA splits in two, each with phone lines back to the PMs and the team leads they cover. Customer Support shows up too, with one red emergency line: “SOS!” straight to an engineer, not a lead. Support can break through the system when it matters. It works: the customers are awake and chattering again, and the PMs are happy: “Moving faster!”

![Slide 28](slides/28.jpg)

> A release catches fire. What changed: one team’s release goes up in flames. Four teams are each shipping on their own schedule, through their own release, and nobody is looking at all of them together. The Manager has no idea what happened. Support now sits in its own box, with a line to every PM.

![Slide 29](slides/29.jpg)

> Air traffic control for releases. What changed: the four releases are grouped together, and a Release Manager watches over all of them like air traffic control, deciding what lands when. No more surprise fires, and the Manager is happy again.

![Slide 30](slides/30.jpg)

> Who’s on call? What changed: one team’s DevOps / PagerDuty quietly disappears. Maybe the person left, maybe the rotation lapsed. Production still runs, but when it breaks, nobody gets paged. The Manager is confused again.

![Slide 31](slides/31.jpg)

> Enter the SRE. What changed: the DevOps work is pulled together into one team that covers every product, so nothing falls through the cracks. And a new hero shows up: the SRE, whose job is keeping production reliable across all of them.

![Slide 32](slides/32.jpg)

> Head of Product. What changed: with three PMs pulling in different directions, a Head of Product appears above them all, with a line to every PM: “Must have vision!” The Manager, who now has to square that vision with four teams, a Release Manager and an SRE, is confused again.

![Slide 33](slides/33.jpg)

> Oh, and don’t forget… Zoom out, and the org chart was never the whole story. Design, the CEO, two Sales people and Marketing all want something, and a hacker has found the open port. None of them go through the structure: each one rings the Manager, a PM and whichever engineer picks up.

![Slide 34](slides/34.jpg)

> Guess there’s nothing to do… Everything is humming, so the strategy folks retreat to the boardroom to present a new vision, and the engineers, cut off from the customers, stand around the coffee machine wondering what any of it means. Meanwhile the customers walk out the door, straight to the competition, where a single engineer is happy to help.

![Slide 35](slides/35.jpg)

> Everyone wants something. Without the structure, every role goes straight to the engineer, and they all want something different, right now. The engineer has no idea what to do first.

![Slide 36](slides/36.jpg)

> Let me find out… The opposite failure. So many layers sit between the engineers and the customers that nothing gets through: every layer says “let me find out…”, frustration builds the closer you get to the customer, and the engineers think there’s nothing important to do.

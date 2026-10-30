# The Future of Software Engineering

Outline only. Bullets, no prose. Downstream artifacts (deck, notes, images) expand on it.
`Image:` lines are proposed slide imagery (Maya = adult, wavy dark hair, round glasses, mustard sweater; Robo-Maya = bob-cut metal robot, orange chest panel).

## Status (2026-10-30)

- Given once, 2026-10-29. The deck as presented (29 slides, art + notes) is in [README.md](README.md).
- The numbered outline below is the original plan; the deck has since diverged:
  - Part 3 is now: future-of-SWE section → **Conclusions** (tiny teams, clear ownership interfaces, safety levels) → house analogy → Levels 1–3 → layered house ("Software Ownership Tomorrow").
  - "One app, three layers" and the company-specific layer map were cut after the talk.
  - The closing "Maya the wizard, again" slide (18) was never built.
  - New **Appendix: Infra for the future**: (4) agent vs. human identity, (5) checkpoints / auto-restore when agents go rogue.

## TODO

- [ ] **Real examples.** The house analogy didn't land: people missed that *our customers* own the software and can change it. Add specific changes a customer could make, per layer, and what involvement each needs from us (none / a warning + test env / our engineers). Draft rows are on the TODO slide (README slide 26).
- [ ] Decide whether the house analogy stays, or the examples replace it.
- [ ] Optional: a timeline slide for a real "idea → shipped" story showing that the decisions, not the code, took months.

## Outline

1. **Title: The Future of Software Engineering**
   - Maya as Mickey Mouse (*Sorcerer's Apprentice*): a wizard directing an army of robots doing the menial tasks
   - Image: DONE (wizard Maya conducting an army of Robo-Mayas)

2. **Recap: "From Slack to Shipped" (June)**
   - Reuse existing slides 1–8 as-is, except slide 8 (below)
   - Feedback loop, not a compiler; judge behavior, not source; make verification cheap
   - Image: existing slides

3. **Change slide 8 (P, not NP)**
   - Problem: right side is confusing (framed mockups on a wall)
   - New: Maya reviews three things, stacked top to bottom
     - Top: **UI** of an application
     - Middle: **API** box (routes, etc.)
     - Bottom: **Database** with a schema
   - These are the three levels she reviews
   - Image: DONE (NP pile vs. Maya looking at UI / API / DB frames)

## Part 1: What I got wrong

4. **Section: So what did I get wrong? Three things**
   - Image: Maya holding a crumpled "plan" from June, scratching her head; Robo-Maya holding an eraser

5. **Wrong #1: Most software is internal, or the change is minor**
   - "Nobody cares" about most changes
   - So going through ANY engineering review is too much
   - Image: Maya waving a stack of papers (like the ones we had before) in a room full of engineers, but they are all working & ignoring her.

6. **Wrong #2: Reviewing other people's *ideas* is still expensive**
   - Understanding the "why" costs more than building the thing
   - Letting others build it doesn't save much time
   - Image: Maya at a desk with a tall stack of other people's idea-cards; a clock, a coffee mug, a tired look; Robo-Maya has already built three of them in the corner

7. **Wrong #3: Execution got WAY faster: "faster than you can think"**
   - Opus 5.5 / Sonnet 5.5: think-to-demo in minutes
   - Image: Maya mid-thought, a thought bubble still half-drawn, while Robo-Maya hands her the finished app; speed lines behind the robot

8. **So what?**
   - Either engineering doesn't care, or engineering can just do it faster itself
   - Both end in the same place: **"a pipeline where non-engineers make changes and get them reviewed" is not very valuable**
   - Image: a conveyor belt of change-requests where Maya and Robo-Maya are putting things on one side; on the other, a pile is gathering on the floor, while an Engnineer is sitting at a desk facing away working & ignoring the whole pile.

## Part 2: What hasn't changed

9. **Section: What HASN'T changed? Three things**
   - Image: a calm, unmoved boulder in a fast-flowing river, Maya and Robo-Maya sitting on it

10. **Unchanged #1: Engineering is still a bottleneck**
    - Even moving faster, there is ALWAYS more to do than capacity to do it
    - Image: Maya and Robo-Maya at a counter, an endless queue of customers with to-do lists stretching out the door; still-too-long line, despite a very busy robot

11. **Unchanged #2: Users have context engineers don't**
    - Internal and external users know things the builders don't
    - Acquiring that context is expensive and slow: human speed
    - Image: a user with a glowing lantern-shaped head full of context; Maya squinting in, pulling thin glowing threads out slowly with a tiny spool

12. **Unchanged #3: Businesses and users need to be safe**
    - Don't lose money, don't lose reputation, don't break trust
    - Image: Maya in a hard hat holding a clipboard in front of a vault door, a cracked piggy bank and a dented "reputation" trophy on the floor

## Part 3: Where SWE ends up

13. **Section: So where does software engineering end up?**
    - Image: Maya and Robo-Maya looking at a house under construction, blueprints rolled under an arm

14. **Analogy: owning a house, three levels of risk**
    - (a) It's ugly: bad paint job, poorly hung frames
    - (b) Only you or your property get hurt: a poorly installed roof, knocking down a wall
    - (c) People die or lots of damage: wrong roof support, no fireproofing
    - Image: a cutaway house, three floors: bottom floor a crooked picture frame and paint splashes; middle floor a leaky roof; top floor a big fire with a sign "NO FIREPROOFING"

15. **Three ways we already deal with it**
    - (a) People do it themselves
    - (b) They hire experts, unless they REALLY want to learn how
    - (c) Legally required: extensive review by experts, with explicit sign-off
    - Image: the same house, three doors: DIY with a paintbrush (Maya); a plumber's van (an expert); an inspector with a stamp and a "PERMIT" form

16. **The Future of SWE: structure the software in layers, with the right access per layer**
    - Allow: the user changes it directly
    - Allow with a warning / optional review
    - Require review: engineers, explicitly signed off
    - Deepest changes can't even be *started* by non-engineers: they require engineering
    - Image: a three-layer cake or layered building cross-section: a bright, open top (green: "edit freely"), a middle with a gate and a "run your own test server" sign (yellow), a bottom behind a sealed vault door with an engineer's badge reader (red)

17. **Example: one application, three layers**
    - Frontend: users edit it directly (allow)
    - Middleware: users open a PR and run their own test server (allow with warning / optional review)
    - Deeper layers (data, payments, auth): cannot be started without engineering (require review)
    - Image: the UI / API / database stack from slide 8, now color-coded green / yellow / red, with people at each level: a user with a paintbrush, a user with a PR, only an engineer at the vault

18. **Close: Maya the wizard, again**
    - Engineers own the layers that can hurt people; everyone else gets safe, wide-open layers to shape their own software
    - Image: callback to the title: Maya the wizard, now directing robots at three colored floors

## Appendix

* Speed of me + agent → nobody else will be able to keep up with it.
   * 3rd party people “building it themselves” will NOT be faster than me building it.
   * Opus 5.5 + Sonnet 5.5 changing the game → “think” to “demo” can be ~minutes, even for fairly complex stuff.
   * Having CS, othes try to make changes to the app -> "merge conflicts" almost guaranteed
   * Future: 1 (MAYBE 2) people per "application". 
   * SO the "we will review other people's changes" --> I don't believe this anymore. Which is good; nobody wants to spend their life looking at other people's great ideas.
* Boxes BETWEEN applications will be more important than eve
   * Teams of 1 or 2
* Software has always been *the blocker*
   * We are the scribes of old. Most humans didn't know how to write, so if they had to send a message, they had to "get permission" and pay a lot of money.
   * That version today is software: if you want to provide a service for your customers, you have to ask Engineering to build it. And we know how that goes.
* Building loops -> what is this?
   * Humans are slow. E.g. testing an app -> so creating a loop where agents do the human work...?
   *  
* (from earlier draft of "what did we get right") Writing/reading code is dead -> those 3 interfaces (UI, API, DB) are the only ones that matter (when they do).

## Ideas (parked, not yet placed)

- **Agentic loops: the spend is not humans talking to agents.**
  - Most tokens will go to agent-to-agent loops, not people
  - So human-in-the-loop cost is not the worry

## Open questions

- Is Part 2 of the June talk (five lessons) in or out of this version?
- Run time and audience?
- Slide 16/17: are the three levels exactly allow / allow-with-warning / require-review, or should "warning" and "optional review" be separate?
- Does slide 17's example layering (FE / middleware / deeper) match your real stack, or should it use the UI / API / DB from slide 8?

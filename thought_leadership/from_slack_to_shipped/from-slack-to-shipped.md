# From Slack to Shipped

*Turning intent into behavior-verified code — reciprocal tech talk for Great Question (2026-06). Builds on [How We Develop](how-we-develop.pptx).*

## Part 1 — A New Philosophy

1. **From Slack to Shipped** — turning intent into behavior-verified code
   - **SLIDE:** intro slide — the premise as ONE central icon, characters introduced small at the sides. No text, no speech, no letters anywhere. (Convention across the deck: labels/dialogue are overlaid as crisp deck text, not drawn in-art.)
     - *Center:* the single hero motif, big and clean — a 💬 Slack chat bubble with an arrow → a "ship it" icon (little rocket / shipping box with a checkmark).
     - *Maya:* small, lower-LEFT, working at her laptop (posting the message).
     - *Robo-Maya:* small, lower-RIGHT, working (building/shipping). The two frame the icon and introduce the characters.
2. **Everything starts as a conversation**
   - **SLIDE:** split comic panel — the whiteboard conversation becomes a thread the AI *and* a human join.
     - *Left panel — Maya at a whiteboard with two coworkers,* sketching a diagram of Robo-Maya; Maya says (short bubble): "wait — we forgot to invite Joe…"
     - *Right panel — Maya typing on her laptop in a chat app;* the thread shows replies from both Robo-Maya and Joe — AI and human, side by side in the same conversation, same context.
     - *Chat text (render short bubbles, else overlay):*
        - Maya: "moving this to the thread so everyone has the context 👇"
        - Joe: "nice — does it handle the offline case too?"
        - Robo-Maya: "good catch, Joe — adding offline handling to the PRD now."
     - *Point:* the AI is a first-class participant with the same context as the humans.
   - we used to share context verbally — hallway, whiteboard, gone by lunch
   - now it's Slack + Google Meet — captured, searchable, persistent
   - the unlock: AI can have the same context humans do
   - so it acts on intent, not just instructions
   - even this talk was looped from a Slack thread
3. **The dream, one breath**
   - **SLIDE:** Maya sleeps & dreams while Robo-Maya does all the work along the line. No speech bubbles; step labels overlaid in the deck.
     - *Maya:* fast asleep in a cozy armchair on the left, a dreamy thought-cloud above her showing the happy finished/shipped feature.
     - *Robo-Maya:* cheerfully working every station along a straight LEFT→RIGHT row, moving down the line.
     - *Diagram:* a linear row of six simple station icons — chat bubble · document · code block · checkmark · magnifying glass · merge symbol — with clean empty space UNDER each for an OVERLAID label (Slack · PRD · Code · Tests · Review · Merge). No text drawn in the art.
   - `💬 Slack → 📄 PRD →  🛠️ code → ✅ tests → 👀 review → 🔀 merged PR`
   - tempting to call it a compiler — it isn't
   - a compiler transforms logic; we feed it intent
   --> more like a feedback loop: see how it behaves, feedback, etc. What does this remind you of? More later... (get people interested)
4. **Why it's not a compiler — the thesis**
   - **SLIDE:** a compiler crunches precise code into orderly binary — but you can't compile a fuzzy human idea.
     - *Maya:* like extracting a memory in Harry Potter, uses a wand to pull a glowing wispy thought-strand out of her temple, holding it out to offer it to Robo-Maya.
     - *Robo-Maya:* shrugging helplessly (palms up, a small "?" over her head) — she can't just take the fuzzy intent.
     - *Diagram:* beside Robo-Maya, a sturdy "COMPILER" machine feeds in sheets of paper printed with code, crunches them, and emits neat orderly rows of 0s and 1s marching out on an assembly-line conveyor — deterministic, correct by construction. Contrast: precise code compiles cleanly; fuzzy intent doesn't.
   - writing code → easy; code that works -> hard ; code that never regresses → almost impossible?
   - a compiler needs logic and is correct by construction
   - we have intent, and the output is nondeterministic
   - worse: you can't verify AI code by reading it — the volume is too high - so it might as well be a black box
5. **If it's not a compiler — what is it?**
   - **SLIDE:** a 6-panel comic — Maya's idea grows (skateboard → scooter → bike → motorcycle → car), she gets more excited each panel, and Robo-Maya keeps handing over a bigger pile of code-paper — until Maya is buried in review and Robo-Maya powers down with an "OUT OF TOKENS" sign.
   - it's a generative feedback loop, not a compiler: intent in → code out → more to review → grow the idea → repeat
   - the catch: every round the human's *review* pile grows, and the agent eventually runs out of budget
   - *Talk track:* this is the real shape of it — cheap to generate, so the idea (and the review burden) balloon. Which is exactly why the next slides are about making verification cheap.
6. **So ship it like an ML model**
   - **SLIDE:** nobody looks at the weights — judge behavior, not internals.
     - *Maya:* straining to crack open a big, ominous ML-model black box with a crowbar, peeking in wide-eyed — it's scary/impenetrable inside (a faintly glowing tangle of wires/weights).
     - *Robo-Maya:* beside her, wagging one finger side-to-side in a friendly "no" — says "no point looking at the weights."
     - *Diagram:* the box reads as an ML model (small neural-net node glyph on its face) and doubles as "AI code"; the takeaway: don't pry it open, judge what comes out.
   - nobody reviews a model's weights — they measure outputs for inputs
   - treat AI code the same: judge behavior, not source
   - "models are the original slop" — so is AI code
   - the shift: code review → behavior review
7. **ML's playbook, applied**
   - **SLIDE:** how you test a model — feed many known inputs through the black box, grade the outputs pass/fail.
     - *Robo-Maya (left):* turning a big hand-crank that feeds heaps of RAW PARTS (loose wheels, gears, springs, fabric + stuffing, unpainted blocks — clearly unassembled) into the black-box machine; the box ASSEMBLES them into finished toys. (The AI *produces*.)
     - *Maya (right):* grading each finished toy as it emerges — pinning an identical GREEN rosette ribbon (✓) on every pass and an identical RED rosette ribbon (✗) on every fail. Same ribbon shape throughout; only the color differs. No banners. (The human *verifies behavior*.)
     - *Diagram:* going IN, piles of raw parts/components; the box assembles them; coming OUT, finished toys (teddy, car, duck) — passes wear the green ✓ ribbon, the mis-assembled/smoking one wears the red ✗ ribbon; Maya pinning a green ribbon on the one emerging now. Raw parts → [box assembles] → graded toys. Robot cranks IN on the left; human judges OUT on the right.
   - specify the behavior you want = PRD + plain-English test cases (the evals)
   - measure outputs for inputs = the test / regression suite
   - gate every change on it; canary in prod
   - the test suite is the spec — the only observable truth about the black box
8. **The big idea: make verification cheap — P, not NP**
   - **SLIDE:** P vs NP — reading code vs verifying by sight. Split panel; "NP" top-left, "P" top-right.
     - *Left panel (NP):* Maya buried under a huge avalanche/mountain of code printouts — only her frazzled head + a hand poking out, overwhelmed trying to read it all. Big "NP" label top-left.
     - *Right panel (P):* Maya stands relaxed looking UP at a gallery wall of six framed UI mockups (simple app-screen wireframes), verifying at a glance; Robo-Maya beside her mirroring her pose. Big "P" label top-right.
     - *Diagram:* the two labels P / NP; six identical UI-mock frames in a grid on the right; the code avalanche on the left.
   - NP's gift is asymmetry: hard to produce, cheap to check
   - AI broke it — producing code is now cheap, checking it by *reading* is not
   - humans ship a fast verifier: perception. the eye is P; reading code is NP
   - so project every change into something checkable in O(glance):
     - **see it:** E2E screenshots + trace video · before/after visual diffs · annotated review shots · preview URL deep-linked to the changed screen
     - **one signal:** green/red CI · 6 gate stamps · coverage/eval-score delta (a number, not a vibe) · prod canary metrics
     - **English, not code:** PRD diff · English test-case diff · the stub layer · auto-written PR summary
     - **shrink the rest:** small stacked PRs · one-concern commits · additive-only migrations · feature flags
   - delegate the NP part: a reviewer agent does the expensive reading, hands back a P-sized verdict
   - default rule: don't make a human read code to verify it
9. **What this unlocks — two kinds of engineers (1/2): the product-minded**
   - **SLIDE:** taste is the scarce input — Maya literally becomes Steve Jobs.
     - *Maya:* recreates the EXACT famous Steve Jobs portrait — BLACK turtleneck + jeans + his thin round rimless glasses — staring STRAIGHT INTO THE CAMERA, serious and intense (not smiling), hand curled at her chin/jaw in the iconic pose; soft warm spotlight.
     - *Robo-Maya:* off to the side doing a facepalm — head resting in her palm, shaking it in disbelief.
     - *Diagram:* keep it iconic and clean; a faint hint of tiny Robo-Mayas building in the far background (the makers she directs). Point: validation ≪ creation — taste is the scarce input.
   - as AI does the building, engineers move *up the stack* — and split into two archetypes
   - **(1) the product-minded engineer:** taste and judgment — decides *what's worth building*, says yes / no
   - Jobs didn't write the code; validating ≪ building, so one person's taste scales to 100,000 makers
   - the scarce input stops being labor — it becomes judgment / taste
10. **What this unlocks — two kinds of engineers (2/2): the deep-technical**
   - **SLIDE:** the human moves up to architect — directing the build. (Note: reframed from "security/data by hand" toward "human owns the architecture"; bullet text may want reconciling.)
     - *Maya:* clearly the ENGINEER/ARCHITECT on site — hard hat, sleeves rolled, a rolled-out set of blueprint plans in one hand, pointing at something and directing.
     - *Robo-Maya (big):* beside her like the foreman (also hard-hatted), attentively following where she points.
     - *Diagram:* a busy, whimsical construction site — lots of little Robo-Mayas in hard hats running around building (scaffolding, girders, a small crane, half-built walls). Maya is unmistakably the one in charge, reading the plans and directing the work.
   - **(2) the deep-technical engineer:** owns the hard calls AI can't be trusted with — a glance can't verify these
   - **architecture** — define the design yourself; don't delegate it
   - **security** — authn/authz/encryption, provable at every layer; zero-trust (each layer assumes the others are breached)
   - **data correctness** — a green test passes on a wrong schema; APIs + SQL schemas are long-lived — human-review them
   - these are the "stays-NP" calls — where the scarce human judgment gets spent
   - *Talk track:* on a construction site, the engineer doesn't lay the bricks — the **trades** do the repeatable work (framing, wiring, plumbing) to spec. Writing code is becoming exactly that: a trade, done by the robots. But **engineering — the design, the architecture, the hard judgment calls — is still engineering.** AI industrializes the *building*; it doesn't replace the *engineer*.
## Part 2 — What we learned shipping it (5 lessons)

*We set out to build a "PRD compiler." It largely failed — but it taught us how to actually ship with AI. Five lessons, in the order they bite you.*

11. **Lesson 1 — Context is the moat.**
    - the orchestration is disposable; your **context** is the durable asset
    - PRDs · English test cases · per-repo `.ai/` rules — all committed to Git
    - specialized agents (PM / staff-eng / backend / frontend / test) only shine when fed *your* context
    - reverse-engineer a PRD + tests from existing code → instantly "AI-safer"
    - *Talk track:* **Anthropic (and every frontier lab) will out-engineer your internal AI team — you can't win on the model or the harness. The only durable edge you can add is your *local context*: your PRDs, your tests, your conventions, your `.ai/` rules. That is the moat.**
    - *Talk track:* agents have no memory — spool working state to `task.md` so an 8-hour run resumes with full context.
12. **Lesson 1, live — the Cloud PRD + its English tests**
    - `[LIVE DEMO]` open the checked-in **Cloud PRD** (reverse-engineered from the code) and scroll its **numbered English test cases**
    - *Demo beats:* the PRD reads like a product doc, not code · every requirement carries a `[TEST: …]` tag · the English test cases are readable by QA, PM, *and* the agent · three-layer alignment: PRD requirement ↔ English test case ↔ Playwright spec
    - *Talk track:* this is the moat made concrete — none of it is the model or the harness; it's *our* context, living in Git.
13. **Lesson 2 — Decompose & parallelize.**
    - break the PRD into **independent sections**, then fan out agents on **stacked PRs** — each builds on the one below, in parallel, no conflicts
    - bootstrap UI from **HTML / Figma mockups** — works shockingly well
    - *Talk track:* …which is exactly how we used to run a team of engineers — chunk the work, hand out independent scopes, run them in parallel. **Shocking!** AI just makes us re-learn good engineering management.
14. **Lesson 2, in the wild — the mobile app, rebuilt from its PRD**
    - example: the mobile app rebuilt from its PRD **twice** — reverse-engineered the PRD → regenerated to **Vue 3** → then a **whole new version** on the same PRD, built as stacked PRs from mockups
    - `[IMG: mobile app BEFORE → AFTER, side by side — after = images/_screens/mobile-v2.1-after.png; before = TBD]`
    - *Talk track:* a whole app, regenerated in parallel slices from the spec. Code is downstream of the PRD, so "rewrite the whole thing" becomes a regen, not a rescue.
15. **Lesson 3 — Never trust the sycophants.**
    - agents are sycophants — left alone, they'll declare their own work perfect
    - run **local tests first** (fast, and the agent keeps the pass/fail context) — **but** gate everything behind **independent CI + a separate review context** so it can't grade its own homework
    - **review gates** for what a glance can't catch (security, data correctness); **preview envs** for both the AI (it checks its own work in a browser) *and* humans
    - *Talk track:* a lone agent optimizes to *pass*. Only an independent reviewer with its own context catches the fudge. Local speed for the agent; independent CI for the truth.
16. **Lesson 3, proof — the gates (and a preview env)**
    - `[IMG: images/_screens/ci-review-gates-run.png — a real cloud-api PR run: E2E shards + Cerbos + AI-Review gates, with CI catching a failed v2-frontend job (run 28481790534)]`
    - every cloud PR also deploys a **preview env** the review agent + humans point a browser at — a per-PR URL like `preview.example.com/cloud/<hash>/` (run 28481605740 → `…/cloud/6848c9c8/`)
    - `[IMG placeholder: the Deploy Preview run — "Deploy Preview Environment ✓" — run 28481605740 (TBD)]`
    - **story:** 500–600 E2E tests, **none written by an engineer**; the reviewer caught a test that *cheated* (typed "Circle K" instead of expanding "CK") — shipped via cloud-api #52
17. **Lesson 4 — Once it's tested, you can "recompile."**
    - a solid behavior suite turns scary migrations into mechanical ones — regenerate a subsystem and trust the tests to catch regressions
    - **story:** ~**6 engineer-months of migration work in a few weeks**, across several projects
    - *Talk track:* the payoff of Lesson 3. The tests *are* the spec — so a big migration becomes a "recompile": change the target, let the evals hold the line.
18. **Lesson 4, live — Cloud V2**
    - `[LIVE DEMO]` walk through **Cloud V2**, the redesigned portal — a large migration the test suite carried
    - *Demo beats:* the new Vue 3 portal running under `/v2`; feature parity with the old app plus the redesign; hundreds of E2E tests (none hand-written) held the line through the migration
    - *Talk track:* this is what a "recompile" looks like from the outside — a whole portal migrated, with the evals catching every regression along the way.
19. **Lesson 5 — Let it overbuild, then prune.**
    - generation is cheap, so it sprawls — speculative infra, redundant/overlapping skills
    - the discipline comes after the fact: **delete, delete, delete**
    - **story:** our greenfield QA build grew a multi-kiosk orchestrator we didn't need yet — pruned; stale skills get culled regularly
    - *Talk track:* cheap to build means cheap to *over*-build. Let it run a little ahead, then cut hard back to what's load-bearing. Pruning is a first-class step, not an afterthought.
20. **Discussion — open questions for the room**
    - reciprocal by design: you build products where agents are first-class *users*; we build a pipeline where agents are first-class *engineers* — so let's compare notes
    - **1. Debating forever** — how do you stop two agents from ping-ponging endlessly (the infinite-review problem)?
    - **2. Rubber-stamping** — how do you stop an agent from *approving* without doing real work?
    - **3. Product / QA review** — how do you have product & QA review all this output? What do they actually gate on?
    - **4. Architecture review** — how do engineers review the large architectural decisions?
    - and yes — this whole talk was just context from a Slack thread, same as I'd give a teammate
    - *Talk track:* Part 1 was the philosophy (behavior over source · cheap verification · two kinds of engineers); Part 2 was the how. One-line takeaway: **put your context in Git, chunk the work, and never let it grade its own homework** — then let's argue about the four questions above.

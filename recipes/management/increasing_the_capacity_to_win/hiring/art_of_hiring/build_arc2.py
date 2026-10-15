"""Generate Arc 2 (Training interviewers) slides for the Art of Hiring deck, reusing Arc 1's helpers."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HERE, "build_arc1.py")).read()
exec(_src[:_src.index("\nS = {}")])  # helpers only: slide(), card(), mono(), body(), row(), col(), g() ...

ROOT = os.path.join(HERE, "arc2", "project")
SL = os.path.join(ROOT, "slides")
LOGO = "/_blob/9b7ec390275e1c40393184dc2c7f61e3"

ORDER = [
    "cover", "map", "machine", "levels", "levels-how",
    "l1", "senior", "l2", "l2-traits", "l2-ask", "l3", "hero", "l4", "tell", "l5", "joined", "levels-all",
    "rule1", "rule2", "rule3", "dissent",
]
HANDWRITTEN = {"cover", "map", "levels", "hero"}

LEVELS = [("L1", "Competence", "Do they meet our bar?"),
          ("L2", "Potential", "How far can they grow?"),
          ("L3", "Fit", "What unlocks them here?"),
          ("L4", "Magnet", "Strength attracts strength."),
          ("L5", "Landing", "“I joined to work with you.”")]


def stairs(lit, bw=64, gap=20, hmin=110, step=80):
    """Five rising bars; `lit` = the current level (1-5), or 6 = all lit."""
    w, h = 5 * bw + 4 * gap, hmin + 4 * step
    bars = []
    for i in range(5):
        bh = hmin + i * step
        if lit == 6 or i == lit - 1:
            fill, stroke = G, G
        elif i < lit - 1:
            fill, stroke = "#4A4F5A", "#4A4F5A"
        else:
            fill, stroke = "#16181C", "#2B2B2B"
        bars.append(f'<rect x="{i * (bw + gap) + 2}" y="{h - bh + 2}" width="{bw - 4}" height="{bh - 4}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
    svg = f'<svg aria-label="Five-level staircase" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + "".join(bars) + "</svg>"
    labels = row(*[f'<p style="{MONO};width:{bw}px;font-size:24px;text-align:center;color:{G if (lit == 6 or i == lit - 1) else MUT2}">L{i + 1}</p>'
                   for i in range(5)], gap=gap)
    return col(svg, labels, gap=12, extra="flex:none")


def rung(k, v, best=False):
    c = G if best else MUT
    return card(row(mono(k, c, 26, "width:180px;flex:none"), body(v, 32), gap=24, align="baseline"),
                border=G if best else "#2B2B2B", pad=28)


def level_slide(sid, n, title, sub, rungs, notes):
    lvl, name, _ = LEVELS[n - 1]
    right = col(*([body(sub, 34, MUT)] if sub else []),
                rung("GOOD", rungs[0]), rung("BETTER", rungs[1]), rung("BEST", rungs[2], best=True),
                gap=20, extra="flex:1;min-width:0")
    return slide(sid, f"{lvl} · {name}", title, row(stairs(n), right, gap=80, align="center"), notes)


def opener(sid, kicker, big, sub, notes, kcolor=G):
    return slide(sid, "", "",
        col(f'<p style="{MONO};font-size:32px;letter-spacing:3px;color:{kcolor}">{kicker}</p>',
            f'<p style="{HEAD};font-size:150px;font-weight:600;line-height:1.02;color:#F4F5F7">{big}</p>',
            body(sub, size=40, color=MUT), gap=48, extra="flex:1;justify-content:center"), notes)


def pill_row(words, color=FG, border="#2B2B2B", bg="#141416", size=32):
    return ('<div style="display:flex;flex-direction:row;flex-wrap:wrap;gap:16px">' + "".join(
        f'<p style="font-size:{size}px;color:{color};background:{bg};border:2px solid {border};border-radius:40px;padding:12px 28px">{w}</p>'
        for w in words) + "</div>")


S = {}

S["machine"] = opener("machine", "[ ARC 2 · TRAINING INTERVIEWERS ]",
    f"Your job: build<br>{g('the hiring machine.')}",
    "As an EM, that means training your interviewers.",
    "Your job as an Engineering Manager is to BUILD the hiring process, which requires training your interviewers. Arc 1 was who to hire. Arc 2 is how each interviewer gets great at finding and landing them.")

S["levels"] = slide("levels", "Training interviewers", f"Five levels of an {g('A-player interviewer.')}",
    col(row(*[f'<div style="flex:1;height:{240 + i * 80}px;{CARD.format(b=G if i == 4 else "#2B2B2B")};padding:28px;display:flex;flex-direction:column;gap:10px">'
              f'{mono(l, G, 24)}<h3 style="{HEAD};font-size:40px;font-weight:600">{nm}</h3>{body(q, 26, MUT)}</div>'
              for i, (l, nm, q) in enumerate(LEVELS)], gap=24, align="end"),
        row(mono("COMPLEXITY (SKILL / PROCESS) → &nbsp;·&nbsp; VALUE TO COMPANY →", MUT2, 24), gap=0),
        gap=20, extra="flex:1;justify-content:end"),
    "The five levels: Competence, Potential, Fit, Magnet, Landing. Each one is more complex to master (skill and process) and more valuable to the company. Most interviewers live at L1. The goal is an interviewer who works all five.")

HOW = [("01", "Builds on the last", "Higher levels build on lower ones."),
       ("02", "Start anywhere", "You don't need to master a level before working on the next."),
       ("03", "Harder each step", "Difficulty of mastery rises with each level."),
       ("04", "Taught on its own", "Each level is trained independently."),
       ("05", "Overlays the loop", "Every stage of the interview process uses them.")]
S["levels-how"] = slide("levels-how", "Training interviewers", f"How the levels {g('work.')}",
    row(*[flex1(card(mono(n, G, 26) + f'<h3 style="{HEAD};font-size:36px;font-weight:600;line-height:1.15">{t}</h3>' + body(d, 28, MUT), pad=32, extra="height:100%"))
          for n, t, d in HOW], gap=24),
    "Higher levels build on lower levels. Mastery of a lower level is not required to start working on higher levels. Difficulty in mastery increases with level. Each level is taught independently. And the levels overlay the interview process: every stage uses them.")

S["l1"] = level_slide("l1", 1, f"Do they meet our {g('technical bar?')}", "Applied intelligence + technical competence.",
    ["Finds valuable strengths using standard questions or problems.",
     "Changes style to fit the candidate: standard questions, interactive problem solving, or their past work.",
     "Makes it look easy."],
    "L1, Competence. Question: do they meet our technical bar? Two things: applied intelligence and technical competence. Good: able to find valuable strength(s) using standard questions/problems. Better: able to change styles based on the candidate (standard questions vs. interactive problem solving vs. interviewing using their past). Best: make it look easy. It gets much harder to evaluate at higher levels of seniority.")

S["senior"] = slide("senior", "L1 · Competence", f"Senior isn’t {g('“knows what I know.”')}",
    col(row(flex1(card(mono("WRONG BAR", O, 26) + body("“Do they know what I know?”", 40)
                       + body("Knowledge comes from experience. Yours and theirs aren’t comparable.", 30, MUT), border="#2B2B2B", pad=40, extra="height:100%")),
            flex1(card(mono("RIGHT BAR", G, 26) + body("“What should they know, given their path?”", 40)
                       + body("Read the résumé, then test what that experience should have taught them.", 30, MUT), border=G, pad=40, extra="height:100%")),
            gap=32),
        row(mono("LOOK FOR", MUT2, 26, "width:200px;flex:none"), pill_row(["Judgment", "Good questions", "Improvisation"], G, "#2F4A2A", "#1C2619"), gap=24, align="center"),
        gap=40),
    "How do you determine senior level? It is not \"do they know what I know\": knowledge is based on experience, so it is not directly comparable. You need to understand what they SHOULD know based on their résumé and experience. Look for judgment, good questions, improvisation. [Clip from The Matrix: TBD.]")

TRAITS = [("Motivation", "A fierce commitment to excel in pursuit of unselfish goals."),
          ("Curiosity", "Seeks new experiences, knowledge and candid feedback, to grow."),
          ("Insight", "Gathers and makes sense of information that suggests new possibilities."),
          ("Engagement", "Uses emotion and logic to communicate a persuasive vision and connect."),
          ("Determination", "Fights for difficult goals and bounces back from adversity.")]
S["l2-traits"] = slide("l2-traits", "L2 · Potential", f"What does potential {g('look like?')}",
    row(*[flex1(card(mono(f"0{i + 1}", G, 24) + f'<h3 style="{HEAD};font-size:34px;font-weight:600">{t}</h3>' + body(d, 28, MUT), pad=28, extra="height:100%"))
          for i, (t, d) in enumerate(TRAITS)], gap=20),
    "Five high-potential traits. Motivation: a fierce commitment to excel in the pursuit of unselfish goals. Curiosity: seeks new experiences, knowledge, and candid feedback, with a focus on growing. Insight: the ability to gather and make sense of information that suggests new possibilities. Engagement: a knack for using emotion and logic to communicate a persuasive vision and connect with people. Determination: the wherewithal to fight for difficult goals despite challenges, and to bounce back from adversity. (These five come from Claudio Fernández-Aráoz, \"21st-Century Talent Spotting\", HBR 2014.)")

S["l2"] = level_slide("l2", 2, f"What is their {g('potential?')}", "Interviewing for potential, not just today’s skill.",
    ["Finds repeated examples of high-potential behavior.",
     "Finds the limits: what are their blind spots?",
     "Knows whether what unlocks their potential exists here."],
    "L2, Potential. Good: able to find repeated examples of high-potential behaviors (motivation, curiosity, insight, engagement, determination). Better: able to determine limitations in those behaviors: what are their blind spots? Best: able to correctly determine whether the things necessary to unlock their potential exist here. That last one is the bridge to L3.")

S["l2-ask"] = slide("l2-ask", "L2 · Potential", f"How do you test potential in a {g('technical interview?')}",
    col(body("Ask the room. Capture answers live.", 36, MUT),
        row(*[flex1(card(mono("?", MUT2, 40) + body("&nbsp;", 30), border="#3A3E47", pad=40, extra="height:260px")) for _ in range(3)], gap=32),
        gap=40),
    "Open question to the room: how do you test for potential inside a technical interview? Capture answers live, on the slide or a whiteboard.")

S["l3"] = level_slide("l3", 3, f"What unlocks their potential {g('HERE?')}", "A mix of alignment, role requirements and cultural fit.",
    ["Understands their goals, the environment they need and any culture issues, and believes all three work here.",
     "Can lay out a plan (projects, timing) that would unlock their potential here.",
     "Shows how similar people executed that plan and got the results here."],
    "L3, Fit. What unlocks their potential HERE? It's a mix of alignment, role requirements and cultural fit. Good: understand their goals and believe they can achieve them here; understand the environment needed to unlock their potential and believe it exists here; understand cultural fit issues here. Better: able to create a plan (projects and timing) that would unlock their potential here. Best: able to show how a similar candidate's execution against that plan resulted in the desired performance here.")

S["hero"] = slide("hero", "L3 · Fit", f"Everyone wants to be {g('a hero.')}",
    row(*[flex1(card(mono(k, c, 26) + f'<h3 style="{HEAD};font-size:40px;font-weight:600;line-height:1.15">{t}</h3>' + body(d, 30, MUT), border=b, pad=36, extra="height:100%"))
          for k, t, d, c, b in [
              ("FIRES FORGE PEOPLE", "The hard team can be the growth role.", "Show them the fire, eyes open. Most people run away; the right ones get forged.", O, "#2B2B2B"),
              ("INTERNAL RECRUITING", "Recruiting doesn’t stop at the door.", "Match internal talent to problems. Good people leave when nobody builds their career.", G, "#2B2B2B"),
              ("WHEN THEY STALL", "Did we give them the stage?", "If they didn’t grow as expected, ask what hero role we failed to offer.", G, G)]], gap=28),
    "Fit is about giving people the role where they get to be the hero. Fires forge people: a team in trouble can be the best place to grow, if they choose it with eyes open. Internal recruiting is just as important as outside recruiting: matching internal talent to problems usually isn't happening, and good people leave because we don't help them build careers. And when people don't grow as much as we expected, ask why not. Usually: everyone wants to be a hero, and we didn't give them that.")

S["l4"] = level_slide("l4", 4, f"How do you {g('attract')} talent?", "Pro tip: you don’t sell them.",
    ["Shows agility and depth in areas the candidate values. Strength attracts strength.",
     "Impresses them: clearly better, without threat, where they want to grow.",
     "Shows how you personally can grow them, in a way they value."],
    "L4, Magnet. How do you attract talent? Pro tip: you don't sell them. Good: able to demonstrate agility and depth in areas the candidate values (strength attracts strength). Better: able to impress the candidate: clearly better, in a non-threatening way, in key areas where the candidate wants to grow. Best: able to demonstrate how you personally can grow the candidate in a way the candidate values (\"we can grow you\").")

S["tell"] = slide("tell", "L4 · Magnet", f"Strength {g('attracts strength.')}",
    col(*[card(row(mono(k, c, 26, "width:240px;flex:none"), body(v, 36), gap=24, align="baseline"), border=b, pad=32)
          for k, v, c, b in [("A PLAYERS", "Want to work for leaders stronger than themselves.", G, G),
                             ("B PLAYERS", "Feel uncomfortable around A players.", O, "#2B2B2B"),
                             ("C PLAYERS", "Can’t tell the difference between an A and a C.", MUT, "#2B2B2B")]], gap=20),
    "Strength attracts strength. Leaders want to work for leaders stronger than themselves. You know you have B players when they feel uncomfortable with A players. You know you have C players when they can't tell the difference between A and C players. Your interviewers ARE the pitch.")

S["l5"] = level_slide("l5", 5, f"How do you {g('land')} 10× talent?", "If it’s about the compensation, you’ve already lost.",
    ["Connects with the candidate deeply, in a way that matters to them.",
     "Pitches the role, team and company with emotional impact.",
     "Shows why they would win here vs. other options, and it resonates."],
    "L5, Landing. How do you land 10x talent? If it's about the compensation, you've already lost. Good: able to deeply connect with the candidate in a way that is meaningful to them. Better: able to pitch the value of the role/team/org/company in a way that has emotional impact. Best: able to show them why they would win here vs. other options, and have it resonate.")

S["joined"] = slide("joined", "L5 · Landing", "",
    col(f'<p style="{HEAD};font-size:120px;font-weight:600;line-height:1.05;color:#F4F5F7">“I joined this company<br>{g("to work with you.”")}</p>',
        body("When you start hearing this, you’re at L5.", 40, MUT),
        body(f"People decide with emotion, then find the reasons. {g('Emotion is high-order computation.')}", 34),
        gap=48, extra="flex:1;justify-content:center"),
    "When you start hearing \"I joined this company to work with you\", you are at L5. People ultimately make decisions for emotional reasons, and come up with the rational ones to back them up. That's not a bad thing: emotion is very high-order computation. So tap into it. Show them you understand what pulls on their heartstrings, and why, by joining us, this won't be a JOB.")

S["levels-all"] = slide("levels-all", "Training interviewers", f"All five: {g('an A-player interviewer.')}",
    row(stairs(6, bw=110, gap=28, hmin=150, step=90),
        col(*[row(mono(l, G, 26, "width:80px;flex:none"), body(f"<b>{nm}</b> · {q}", 32), gap=20, align="baseline") for l, nm, q in LEVELS],
            gap=28, extra="flex:1;min-width:0"),
        gap=96, align="center"),
    "Put together, the five levels make an A-player interviewer. Next: three rules that make every level work.")

S["rule1"] = slide("rule1", "Rule #1", f"Be {g('interested.')}",
    row(flex1(card(mono("TAKE RESPONSIBILITY", G, 26) + body("Create connection.<br>Leave distractions outside the room.<br>Lower barriers to communication.<br>Make them want to expand on details.", 30), pad=36, extra="height:100%")),
        flex1(card(mono("LOOK FOR", G, 26) + body("What motivates them? What demotivates them?<br>Excitement and interest points.<br>Fear and pain points.<br>What are they proud of?<br>Why did they take a role? Why leave it?", 30), pad=36, extra="height:100%")),
        flex1(card(mono("EMPLOY", G, 26) + body("Active listening.<br>Curiosity: “What?” “How?” “Tell me more?”", 30), border=G, pad=36, extra="height:100%")),
        gap=28),
    "Rule #1: be interested. Take responsibility for being interested: create connection, leave distractions outside the room, lower barriers to effective communication, make the candidate want to expand on details. Look for: what motivates them, what demotivates them, excitement and interest points, fear and pain points, their level of technical, personal and social skill, what they are proud of, why they took a role, why they left it. Employ active listening and curiosity: \"what?\", \"how?\", \"tell me more?\"")


def mcell(text, color, border, bg):
    return f'<div style="flex:1;background:{bg};border:2px solid {border};border-radius:16px;padding:28px;display:flex;align-items:center;height:190px">{body(text, 30, color)}</div>'


S["rule2"] = slide("rule2", "Rule #2", f"Be an {g('advocate.')}",
    row(col(row(f'<p style="width:220px;flex:none">&nbsp;</p>', f'<div style="flex:1">{mono("GOOD FOR US", G, 24, "text-align:center")}</div>',
                f'<div style="flex:1">{mono("BAD FOR US", O, 24, "text-align:center")}</div>', gap=20),
            row(mono("GOOD FOR THEM", G, 24, "width:220px;flex:none"), mcell("<b>Great employee.</b>", G, G, "#1C2619"),
                mcell("They get fired when we figure it out.", FG, "#2B2B2B", "#141416"), gap=20, align="center"),
            row(mono("BAD FOR THEM", O, 24, "width:220px;flex:none"), mcell("They leave when they figure it out, or stay for the wrong reason.", FG, "#2B2B2B", "#141416"),
                mcell("Nobody wins.", MUT2, "#2B2B2B", "#141416"), gap=20, align="center"),
            gap=20, extra="width:1060px;flex:none"),
        col(body("Fit is established <b>jointly</b>.", 34),
            card(mono("FOR THEM", G, 24) + body("Is this the right next stage of their career? What do they want, and how will they prioritize?", 28, MUT), pad=28),
            card(mono("DON’T GO NATIVE", O, 24) + body("You represent the company. Every candidate leaves an evangelist.", 28, MUT), pad=28),
            gap=20, extra="flex:1;min-width:0"),
        gap=56, align="center"),
    "Rule #2: be an advocate. Fit needs to be jointly established. Good for them and good for us: great employee. Good for us, bad for them: they leave when they figure it out, or stay for the wrong reason. Good for them, bad for us: they get fired when we figure it out. For them: is this a good place for the next stage of their career? What are they looking for? How will they prioritize? Do they have clarity on what they want and need? Within reason, help them figure out fit (\"this could mean this or that, which did you mean?\", \"here is what I learned about you\"). Don't set them up for failure. Don't go native: remember you represent the company. We always want candidates to leave as company evangelists. For us: is this an A player?")

S["rule3"] = slide("rule3", "Rule #3", f"Be someone they want {g('to work with.')}",
    col(pill_row(["Park your ego", "Be genuine", "Be aware", "Be a gracious host", "Be excited",
                  "Be interested", "Be wicked smart", "Ask insightful questions", "Ask hard questions", "Be helpful"],
                 FG, "#2B2B2B", "#141416", size=40),
        body(f"They’re interviewing {g('you')}, too.", 36, MUT), gap=48),
    "Rule #3: be someone they want to work with. Park your ego. Be genuine. Be aware. Be a gracious host. Be excited. Be interested. Be wicked smart. Ask insightful questions. Ask hard questions. Be helpful.")

S["dissent"] = slide("dissent", "Our own data", f"The lone dissenter<br>{g('was usually right.')}",
    col(row(flex1(card(mono("PREDICTIVE", G, 26) + body("A specific concern about <b>fit or ownership</b>", 34) + body("“Do they want to lead?” never asked", 34), border=G, pad=40, extra="height:100%")),
            flex1(card(mono("NOT PREDICTIVE", MUT, 26) + body("Doubts about speed or coding", 34, "#C4C8CE") + body("A Strong Yes on technical skill", 34, "#C4C8CE"), pad=40, extra="height:100%")),
            gap=32),
        body(f"Rule: {g('<b>rebut the dissent in writing</b>')} before the offer.", 36),
        mono("SOURCE: MASHGIN HIRING RETRO, 26 HIRES", MUT2, 24), gap=32),
    "From our own retro of 26 hires. When one interviewer raised a specific concern about fit or ownership, it usually came true. Doubts about speed or coding mostly didn't. A Strong Yes on technical skill didn't predict reliability. Leadership desire was never probed. Fix: any specific dissent gets a written rebuttal before an offer goes out.", title_size=72)

for sid, html in S.items():
    if sid in HANDWRITTEN:
        continue
    open(os.path.join(SL, sid + ".html"), "w").write(html)

for sid in HANDWRITTEN - {"cover"}:
    p = os.path.join(SL, sid + ".html")
    s = open(p).read()
    s = re.sub(r'\[ \d+ \]</p>\n<aside>', f'[ {ORDER.index(sid) + 1} ]</p>\n<aside>', s)
    open(p, "w").write(s)

missing = [s for s in ORDER if not os.path.exists(os.path.join(SL, s + ".html"))]
assert not missing, missing

dj = os.path.join(ROOT, "deck.json")
d = json.load(open(dj))
d["order"] = ORDER
d["sections"] = {
    "s1": {"description": "Training interviewers: the hiring machine.", "start": "cover"},
    "s2": {"description": "The five levels, from Competence to Landing.", "start": "levels"},
    "s3": {"description": "Three rules for every interviewer.", "start": "rule1"},
}
json.dump(d, open(dj, "w"), ensure_ascii=False)
print("ok", len(ORDER))

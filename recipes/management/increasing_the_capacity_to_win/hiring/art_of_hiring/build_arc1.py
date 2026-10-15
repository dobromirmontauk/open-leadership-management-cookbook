"""Generate Arc 1 slides for the Art of Hiring deck (Direction A styling)."""
import json, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arc1", "project")
SL = os.path.join(ROOT, "slides")

MONO = "font-family:'DM Mono', 'Courier New', monospace"
HEAD = "font-family:'Host Grotesk', Arial, sans-serif"
G, O, FG, MUT, MUT2 = "#63E14F", "#FF832A", "#E9ECEF", "#A3A8B0", "#8B9097"
CARD = "background:#1A1A1A;border:2px solid {b};border-radius:16px"
LOGO = '/_blob/b4e74a8e220553b66d1d73a519112eee'

ORDER = [
    "cover", "map", "funnel", "pinball", "funnel-jobs", "match", "judging-us",
    "dimensions", "abcd", "venn", "consistency", "fit-def", "mercenary", "believer-ask", "believer-all", "why-fit",
    "grid", "confusion", "resolve", "tool-pain", "b-causes", "tool-b",
    "culture", "speed", "room", "growth",
    "gandalf",
]
HANDWRITTEN = {"cover", "speed"}


def card(inner, border="#2B2B2B", pad=32, extra=""):
    return f'<div style="{CARD.format(b=border)};padding:{pad}px;display:flex;flex-direction:column;gap:12px;{extra}">{inner}</div>'


def mono(text, color=G, size=26, extra=""):
    return f'<p style="{MONO};font-size:{size}px;letter-spacing:2px;color:{color};{extra}">{text}</p>'


def body(text, size=30, color=FG, extra=""):
    return f'<p style="font-size:{size}px;line-height:1.35;color:{color};{extra}">{text}</p>'


def slide(sid, label, title, content, notes, layout="column", title_size=72):
    n = ORDER.index(sid) + 1 if sid in ORDER else 0
    head = (
        f'<p style="{MONO};font-size:28px;letter-spacing:2px;text-transform:uppercase;color:{G}">[ {label} ]</p>\n'
        f'<h2 style="{HEAD};font-size:{title_size}px;font-weight:600;line-height:1.1;color:#F4F5F7">{title}</h2>\n'
    ) if title else ""
    return f'''<section id="{sid}" data-transition="fade" style="background:#060607;color:{FG};font-family:'Raleway', Arial, sans-serif;padding:112px 128px 160px;display:flex;flex-direction:column;gap:40px">
<div style="position:absolute;left:40px;top:0;width:4px;height:1080px;background:linear-gradient(180deg, {O} 0%, {O} 35%, {G} 75%, {G} 100%)"></div>
{head}{content}
<img src="{LOGO}" alt="Mashgin" style="position:absolute;right:96px;top:64px;width:230px;height:47px;object-fit:contain">
<p style="position:absolute;left:128px;bottom:64px;width:1300px;{MONO};font-size:24px;color:{MUT2}">Copyright Dobromir Montauk, 2026</p>
<p style="position:absolute;right:96px;bottom:58px;width:200px;text-align:right;{MONO};font-size:36px;color:{G}">[ {n} ]</p>
<aside>{notes}</aside>
</section>
'''


def g(green):
    return f'<span style="color:{G}">{green}</span>'


def row(*items, gap=32, align="stretch", extra=""):
    return f'<div style="display:flex;flex-direction:row;gap:{gap}px;align-items:{align};{extra}">' + "".join(items) + "</div>"


def col(*items, gap=24, extra=""):
    return f'<div style="display:flex;flex-direction:column;gap:{gap}px;{extra}">' + "".join(items) + "</div>"


def flex1(html):
    return f'<div style="flex:1;display:flex;flex-direction:column;gap:24px;min-width:0">{html}</div>'


def dots(lit, r=26, step=72, color_off="#2E323A"):
    w = step * 10
    cs = "".join(
        f'<circle cx="{step//2 + i*step}" cy="{step//2}" r="{r}" fill="{G if i in lit else color_off}"/>' for i in range(10))
    return f'<svg width="{w}" height="{step}" viewBox="0 0 {w} {step}">{cs}</svg>'


FUNNEL = [("SOURCE", 900), ("SCREEN", 760), ("ONSITE", 620), ("OFFER", 480), ("ACCEPT", 340)]


def funnel(chips=None, dim=False):
    out = []
    for i, (name, w) in enumerate(FUNNEL):
        last = i == len(FUNNEL) - 1
        c = G if last else (MUT2 if dim else FG)
        b = G if last and not dim else "#2B2B2B"
        bar = f'<div style="width:{w}px;{CARD.format(b=b)};padding:20px"><p style="{MONO};font-size:28px;letter-spacing:2px;text-align:center;color:{c}">{name}</p></div>'
        if chips:
            bar = (f'<div style="display:flex;flex-direction:row;align-items:center;gap:40px;width:1560px">'
                   f'<div style="width:900px;display:flex;justify-content:center">{bar}</div>'
                   f'<p style="font-size:34px;color:{FG}"><span style="{MONO};font-size:24px;color:{O};letter-spacing:2px">→ </span>{chips[i]}</p></div>')
        out.append(bar)
    align = "start" if chips else "center"
    return f'<div style="display:flex;flex-direction:column;align-items:{align};gap:18px;width:{1560 if chips else 900}px">' + "".join(out) + "</div>"


# ---- the Strength x Fit grid -------------------------------------------------
GRID = [
    ("A", ["Mercenary", "Confused?", "Rock Star<br><small>can be acclimated</small>", "Unicorn<br><small>hire at all costs</small>"]),
    ("B", ["Consultant", "Ambivalence", "Ambivalence", "Team Player<br><small>hire at all costs</small>"]),
    ("C", ["Hell No!!!", "Hell No", "No", "No"]),
    ("D", ["Will get you fired"] * 4),
]
GOOD = {("A", 3), ("B", 3)}


# Section coordinates of the grid (title at 64px on one line), measured in the live viewer.
GX0, GY0, GPX, GPY, GCW, GCH = 291, 303, 312, 130, 300, 118
YELLOW = "#F5D227"


def arrow_svg(x1, y1, x2, y2, color):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hx1, hy1 = x2 - 22 * math.cos(a - 0.45), y2 - 22 * math.sin(a - 0.45)
    hx2, hy2 = x2 - 22 * math.cos(a + 0.45), y2 - 22 * math.sin(a + 0.45)
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="7" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {hx1:.0f},{hy1:.0f} {hx2:.0f},{hy2:.0f}" fill="{color}"/>')


def grid_overlay(arrows=()):
    top, bot = GY0 - 14, GY0 + 3 * GPY + GCH + 14
    left, right = GX0 - 14, GX0 + 3 * GPX + GCW + 14
    vx, hy = GX0 + 2 * GPX - 6, GY0 + 2 * GPY - 6
    lines = (f'<line x1="{vx}" y1="{top}" x2="{vx}" y2="{bot}" stroke="#E9ECEF" stroke-width="4"/>'
             f'<line x1="{left}" y1="{hy}" x2="{right}" y2="{hy}" stroke="#E9ECEF" stroke-width="4"/>')
    return ('<svg aria-hidden="true" style="position:absolute;left:0;top:0;width:1920px;height:1080px;pointer-events:none" width="1920" height="1080" viewBox="0 0 1920 1080">'
            + lines + "".join(arrow_svg(*a) for a in arrows) + "</svg>")


def grid(cell_h=118, cw=300, hi_cols=(), zones=None, pins=None, fontsz=28, arrows=()):
    """zones: {col: (label, color)}; pins: {(row, col): [names]}"""
    rows = []
    for r, cells in GRID:
        tds = [f'<div style="width:96px;display:flex;align-items:center;justify-content:center"><p style="{HEAD};font-size:44px;font-weight:600;color:{FG}">{r}</p></div>']
        for c, txt in enumerate(cells):
            good = (r, c) in GOOD
            hot = c in hi_cols and r in "AB"
            zc = zones.get(c) if zones and r in "AB" else None
            border = zc[1] if zc else (O if hot else (G if good else "#2B2B2B"))
            bg = "#1C2619" if good else ("#2A2016" if hot else "#141416")
            color = G if good else (MUT2 if r in "CD" else FG)
            if hi_cols and not hot and not good:
                color = "#5A5F68"
            pin = ""
            if pins and (r, c) in pins:
                pin = '<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center">' + "".join(
                    f'<p style="{MONO};font-size:20px;color:#060607;background:{G if good else O};border-radius:999px;padding:4px 12px">{p}</p>' for p in pins[(r, c)]) + "</div>"
            label = txt.replace("<small>", f'<span style="font-size:20px;color:{MUT}">').replace("</small>", "</span>")
            tds.append(
                f'<div style="width:{cw}px;height:{cell_h}px;background:{bg};border:2px solid {border};border-radius:12px;display:flex;flex-direction:column;gap:6px;align-items:center;justify-content:center;text-align:center;padding:8px">'
                f'<p style="font-size:{fontsz}px;line-height:1.15;color:{color}">{label}</p>{pin}</div>')
        rows.append('<div style="display:flex;flex-direction:row;gap:12px">' + "".join(tds) + "</div>")
    axis = ('<div style="display:flex;flex-direction:row;gap:12px;align-items:center">'
            '<p style="width:96px;font-size:22px">&nbsp;</p>'
            f'<p style="width:{cw}px;{MONO};font-size:22px;letter-spacing:2px;color:{O}">−10 UNALIGNED</p>'
            f'<p style="width:{cw*2+12}px;text-align:center;{MONO};font-size:22px;letter-spacing:2px;color:{MUT2}">FIT →</p>'
            f'<p style="width:{cw}px;text-align:right;{MONO};font-size:22px;letter-spacing:2px;color:{G}">+10 ALIGNED</p></div>')
    zone_row = ""
    if zones:
        zs = ['<p style="width:96px;font-size:22px">&nbsp;</p>']
        for c in range(4):
            if c in zones:
                zs.append(f'<p style="width:{cw}px;text-align:center;{MONO};font-size:22px;letter-spacing:2px;color:{zones[c][1]}">{zones[c][0]}</p>')
            else:
                zs.append(f'<p style="width:{cw}px;font-size:22px">&nbsp;</p>')
        zone_row = '<div style="display:flex;flex-direction:row;gap:12px">' + "".join(zs) + "</div>"
    h = cell_h * 4 + 36
    ylab = (f'<svg aria-label="Strength axis" width="44" height="{h}" viewBox="0 0 44 {h}" style="flex:none">'
            f'<path d="M22 {h - 4} V{h // 2 + 84} M22 {h // 2 - 84} V14 M10 26 L22 12 L34 26" fill="none" stroke="#8B9097" stroke-width="3"/>'
            f'<text x="22" y="{h // 2}" fill="#E9ECEF" font-family="DM Mono, monospace" font-size="22" letter-spacing="2" text-anchor="middle" transform="rotate(-90 22 {h // 2})" dy="8">STRENGTH</text></svg>')
    body_rows = '<div style="display:flex;flex-direction:row;gap:12px;align-items:center">' + ylab + '<div style="display:flex;flex-direction:column;gap:12px">' + "".join(rows) + "</div></div>"
    def shift(html):  # keep header/axis rows aligned past the Strength label
        return html.replace('<p style="width:96px;font-size:22px">&nbsp;</p>', '<p style="width:152px;font-size:22px">&nbsp;</p>', 1)
    return '<div style="display:flex;flex-direction:column;gap:12px">' + shift(zone_row) + body_rows + shift(axis) + "</div>" + grid_overlay(arrows)


S = {}

S["map"] = slide("map", "The whole talk", f"Three arcs.<br>{g('One team of A players.')}", row(
    flex1(card(mono("01 · EVALUATE") + f'<h3 style="{HEAD};font-size:48px;font-weight:600">Strength × Fit</h3>'
               + '<svg width="300" height="220" viewBox="0 0 300 220"><line x1="6" y1="4" x2="6" y2="214" stroke="#8B9097" stroke-width="6" stroke-linecap="round"/><line x1="6" y1="214" x2="296" y2="214" stroke="#8B9097" stroke-width="6" stroke-linecap="round"/><circle cx="240" cy="52" r="40" fill="#63E14F"/><circle cx="82" cy="70" r="32" fill="#FF832A"/><circle cx="160" cy="150" r="30" fill="#3A3E47"/></svg>'
               + body("Who should we hire?", color=MUT), pad=40, extra="height:100%")),
    flex1(card(mono("02 · TRAIN") + f'<h3 style="{HEAD};font-size:48px;font-weight:600">Five levels</h3>'
               + '<svg width="300" height="220" viewBox="0 0 300 220"><rect x="10" y="160" width="48" height="50" rx="6" fill="#3A3E47"/><rect x="66" y="125" width="48" height="85" rx="6" fill="#3A3E47"/><rect x="122" y="90" width="48" height="120" rx="6" fill="#3A3E47"/><rect x="178" y="55" width="48" height="155" rx="6" fill="#3A3E47"/><rect x="234" y="20" width="48" height="190" rx="6" fill="#63E14F"/></svg>'
               + body("What makes an interviewer great?", color=MUT), pad=40, extra="height:100%")),
    flex1(card(mono("03 · BUILD") + f'<h3 style="{HEAD};font-size:48px;font-weight:600">3-stage process</h3>'
               + '<svg width="300" height="220" viewBox="0 0 300 220"><circle cx="40" cy="110" r="30" fill="#3A3E47"/><circle cx="150" cy="110" r="30" fill="#3A3E47"/><circle cx="260" cy="110" r="30" fill="#63E14F"/><line x1="72" y1="110" x2="118" y2="110" stroke="#8B9097" stroke-width="4"/><line x1="182" y1="110" x2="228" y2="110" stroke="#8B9097" stroke-width="4"/></svg>'
               + body("How do we run it?", color=MUT), pad=40, extra="height:100%")),
), "The whole talk on one slide. Arc 1: how we evaluate candidates, on two axes: Strength and Fit. Arc 2: how we train interviewers, through five levels from Competence to Landing. Arc 3: how we build the process, in three stages: getting to the interview, the interview, the close. Philosophy, content and process borrowed heavily from TellApart, Twitter, Wade Chambers, and \"Who: The A Method for Hiring\".")

S["funnel"] = slide("funnel", "What is hiring?", f"Hiring is a {g('sales funnel.')}",
    row(funnel(), col(body("Every stage converts…", size=40), body("…or leaks.", size=40, color=O), extra="flex:1;justify-content:center"), gap=96, align="center"),
    "Hiring is a SALES FUNNEL. Explain the basic concept: source, screen, onsite, offer, accept. Every stage converts some candidates and loses others.")

S["pinball"] = slide("pinball", "What is hiring?", f"…but nobody moves through it {g('in a line.')}",
    row(f'<div style="position:relative">{funnel(dim=True)}'
        '<svg style="position:absolute;left:0;top:-10px" width="900" height="480" viewBox="0 0 900 480"><path d="M120 40 C 420 40, 820 60, 700 140 S 140 150, 300 230 S 760 260, 560 330 S 300 330, 380 420" fill="none" stroke="#FF832A" stroke-width="6" stroke-dasharray="14 12" stroke-linecap="round"/><path d="M700 140 C 800 170, 860 200, 890 250" fill="none" stroke="#FF832A" stroke-width="6" stroke-dasharray="14 12" stroke-linecap="round" opacity="0.6"/><circle cx="120" cy="40" r="14" fill="#FF832A"/><circle cx="380" cy="420" r="14" fill="#63E14F"/><circle cx="890" cy="250" r="12" fill="#FF832A" opacity="0.6"/></svg></div>',
        col(card(mono("BOUNCE", O, 22) + body("Candidates skip ahead, stall for weeks, and drop out at every stage.", size=24), pad=24),
            card(mono("FALSE NEGATIVES / POSITIVES", O, 22) + body("Candidates might need to go <b>backwards</b> to avoid mishiring… or missing out on a great person.", size=24), pad=24),
            card(mono("TIME IS A FRIENDLY FOE", G, 22) + body("Isn't it crazy that we make decisions that affect us for years after just a few hours with the team? We are all busy, so we optimize for less time here… often wrongly. Don't be afraid to <b>increase</b> time in each stage so a candidate feels valued, comfortable, and familiar with us.", size=24), border=G, pad=24),
            gap=16, extra="flex:1;min-width:0"), gap=72, align="center"),
    "But it's very messy. Sales funnels look linear, but people bounce around in them. False negatives and positives: candidates might need to go BACKWARDS to avoid mishiring, or missing out on a great person. Time is a friendly foe: isn't it crazy that we make decisions that affect us for years after just a few hours with the team? We are all busy, so we optimize for less time in this part, often wrongly so. Don't be afraid to INCREASE the amount of time in each stage to make a candidate feel valued, comfortable, familiar with us, etc.")

FILTERS = [
    ("SOURCE", 860, ["Are they on the market?"]),
    ("RECRUITER SCREEN", 760, ["Would they ever even choose us?"]),
    ("EM SCREEN", 660, ["Will they be excited about us?"]),
    ("TECH SCREEN", 560, ["Are they likely to be a good engineer?"]),
    ("ONSITE", 460, ["Are they a <b>GREAT</b> engineer?", "Will they thrive at Mashgin?"]),
    ("OFFER", 360, ["Will they choose <b>US</b> over the competition?"]),
]
HIGHFIVE = ('<svg aria-label="Two engineers high-fiving" width="220" height="120" viewBox="0 0 220 120">'
            '<g fill="none" stroke="#63E14F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
            '<circle cx="60" cy="44" r="13"/><path d="M60 57 V88 M60 88 L46 116 M60 88 L74 116 M60 66 L42 82 M60 66 L102 26"/>'
            '<circle cx="160" cy="44" r="13"/><path d="M160 57 V88 M160 88 L146 116 M160 88 L174 116 M160 66 L178 82 M160 66 L118 26"/>'
            '<path d="M110 4 V12 M96 8 L101 14 M124 8 L119 14" stroke="#FF832A" stroke-width="4"/></g></svg>')
def filter_funnel(rows, arrow, arrow_color, q_color, extra_under_last=""):
    return '<div style="display:flex;flex-direction:column;gap:14px">' + "".join(
        f'<div style="display:flex;flex-direction:row;align-items:center;gap:40px">'
        f'<div style="width:860px;display:flex;justify-content:center;position:relative"><div style="width:{w}px;{CARD.format(b=(G if i == len(rows) - 1 else "#2B2B2B"))};padding:16px">'
        f'<p style="{MONO};font-size:26px;letter-spacing:2px;text-align:center;color:{G if i == len(rows) - 1 else FG}">{name}</p></div></div>'
        f'<div style="display:flex;flex-direction:column;gap:4px">' + "".join(
            f'<p style="font-size:32px;line-height:1.25;color:{q_color}"><span style="{MONO};font-size:24px;color:{arrow_color}">{arrow} </span>{q}</p>' for q in qs) + "</div></div>"
        for i, (name, w, qs) in enumerate(rows)) + (
        f'<div style="width:860px;display:flex;justify-content:center;padding-top:8px">{extra_under_last}</div>' if extra_under_last else "") + "</div>"


S["funnel-jobs"] = slide("funnel-jobs", "What is hiring?", f"Every part of the funnel is {g('a different filter.')}",
    filter_funnel(FILTERS, "→", O, FG, HIGHFIVE),
    "Every part of the funnel is a different filter, and each person in the process needs to know which filter they are. Source: are they on the market? Recruiter screen: would they ever even choose us? EM screen: will they be excited about us? Technical screen: are they likely to be a good engineer? Onsite: are they a GREAT engineer, and will they thrive at Mashgin? Offer: will they choose US over the competition?", title_size=64)

THEIR_FILTERS = [
    ("SOURCE", 860, ["Does Mashgin seem like an interesting company / problem / technology / team / whatever I care about…?"]),
    ("RECRUITER SCREEN", 760, ["Who are these people? What is their \u201cculture\u201d?"]),
    ("EM SCREEN", 660, ["Would I want to work for this person?"]),
    ("TECH SCREEN", 560, ["Are these engineers sharp?"]),
    ("ONSITE", 460, ["Will I learn from these people?", "Will I grow here?"]),
    ("OFFER", 360, ["Is this the best bet for my career?"]),
]
S["judging-us"] = slide("judging-us", "The other direction", f"How are they {g('judging US?')}",
    filter_funnel(THEIR_FILTERS, "←", G, FG),
    "Same funnel, opposite direction. At every stage the candidate is running their own filter on us. Source: Does Mashgin seem like an interesting company / problem / technology / team / whatever I care about…? Recruiter screen: who are these people? What is their \u201cculture\u201d? EM screen: would I want to work for this person? Tech screen: are these engineers sharp? Onsite: will I learn from these people, will I grow here? Offer: is this the best bet for my career?")

S["match"] = slide("match", "What else is hiring?", f"But it's also matchmaking!<br>{g('Why would they choose US?')}",
    row(
        f'<div style="width:300px;height:300px;border-radius:50%;border:3px solid {FG};display:flex;align-items:center;justify-content:center"><p style="{HEAD};font-size:56px;font-weight:600">Us</p></div>',
        col(row(mono("WE CHOOSE THEM", FG, 26), gap=0),
            '<svg width="520" height="120" viewBox="0 0 520 120"><path d="M10 35 H500" stroke="#E9ECEF" stroke-width="5"/><path d="M480 15 L505 35 L480 55" fill="none" stroke="#E9ECEF" stroke-width="5"/><path d="M510 85 H20" stroke="#63E14F" stroke-width="5"/><path d="M40 65 L15 85 L40 105" fill="none" stroke="#63E14F" stroke-width="5"/></svg>',
            mono("THEY CHOOSE US", G, 26), gap=16, extra="align-items:center"),
        f'<div style="width:300px;height:300px;border-radius:50%;border:3px solid {G};display:flex;align-items:center;justify-content:center"><p style="{HEAD};font-size:56px;font-weight:600;color:{G}">Them</p></div>',
        gap=48, align="center", extra="justify-content:center;flex:1"),
    "What else is hiring? Matchmaking. Dating. It runs both ways: we choose them, and they choose us. Why would they choose US?")

S["dimensions"] = slide("dimensions", "Two dimensions", f"Strength {g('× Fit')}",
    row('<svg aria-label="Two axes, strength up and fit right, with the top-right quadrant lit green" width="700" height="580" viewBox="0 0 700 580">'
        '<rect x="390" y="20" width="290" height="250" rx="16" fill="#63E14F" fill-opacity="0.14" stroke="#63E14F" stroke-width="4"/>'
        '<rect x="90" y="20" width="290" height="250" rx="16" fill="#1A1A1A" stroke="#2B2B2B" stroke-width="2"/>'
        '<rect x="90" y="280" width="290" height="250" rx="16" fill="#1A1A1A" stroke="#2B2B2B" stroke-width="2"/>'
        '<rect x="390" y="280" width="290" height="250" rx="16" fill="#1A1A1A" stroke="#2B2B2B" stroke-width="2"/>'
        '<path d="M535 110 l18 37 41 6 -30 29 7 41 -36 -19 -36 19 7 -41 -30 -29 41 -6 z" fill="#63E14F"/>'
        '<line x1="70" y1="540" x2="70" y2="10" stroke="#8B9097" stroke-width="5" stroke-linecap="round"/>'
        '<line x1="70" y1="550" x2="690" y2="550" stroke="#8B9097" stroke-width="5" stroke-linecap="round"/>'
        '<text x="40" y="275" fill="#E9ECEF" font-family="DM Mono, monospace" font-size="26" letter-spacing="2" transform="rotate(-90 40 275)" text-anchor="middle">STRENGTH</text>'
        '<text x="385" y="578" fill="#E9ECEF" font-family="DM Mono, monospace" font-size="26" letter-spacing="2" text-anchor="middle">FIT</text></svg>',
        col(body("We want <b>top-right</b> candidates.", size=44),
            body("Candidates want <b>top-right</b> companies.", size=44),
            body(f"Neither side ever defines it. Both choose on {g('“vibes.”')}", size=44, color=MUT),
            gap=40, extra="flex:1;min-width:0"),
        gap=80, align="center"),
    "Two dimensions: Strength and Fit. We want top-right candidates. Candidates want top-right companies. Both sides never define this, and choose on \"vibes\". The rest of this arc defines each axis.")

S["consistency"] = slide("consistency", "What is an A player?", f"Anyone can get lucky.<br>{g('A players bat with consistency.')}",
    col(
        row(f'<p style="width:300px;{MONO};font-size:30px;letter-spacing:2px;color:{G}">A PLAYER</p>', dots(set(range(10)) - {6}), mono("9 / 10", G, 30), gap=40, align="center"),
        row(f'<p style="width:300px;{MONO};font-size:30px;letter-spacing:2px;color:{O}">GOT LUCKY</p>', dots({3}), mono("1 / 10", O, 30), gap=40, align="center"),
        body(f"Look for a {g('track record of winning')}, not just one home run.", size=44),
        gap=64, extra="flex:1;justify-content:center"),
    "Imagine 100 similarly difficult problems given to 100 different people. Pick the 10% with the best solutions: that's the bar. \"90% chance of achieving outcomes\" guarantees consistency instead of randomness. Someone might come up with a great solution to one of those 100 problems. Can they do it 9 times out of 10, across the other problems? If not, they just got lucky. So look for a track record of winning, not just one home run.")

ABCD = [
    ("A", "<b>90%</b> likely to solve the problems you throw at them.", "Attracts other A players.", G),
    ("B", "<b>75%</b> likely to solve the problems you throw at them.", "Can irritate A players.", FG),
    ("C", "<b>60%</b> likely to <b>FAIL</b>. Why risk it?", "Drives away A players.", MUT),
    ("D", "Lowers team productivity, drives away key talent, degrades the codebase.", "<b>Gets you fired.</b>", O),
]


def abcd_cell(html, k):
    return card(html, border=(G if k == "A" else "#2B2B2B"), pad=28, extra="flex:1;min-width:0")


S["abcd"] = slide("abcd", "Strength", f"Defining “Strength”: {g('A')}, B, C, D players",
    col(row(*[f'<p style="flex:1;{HEAD};font-size:80px;font-weight:600;line-height:1;color:{c}">{k}</p>' for k, _, _, c in ABCD], gap=24),
        row(*[abcd_cell(body(d, size=32), k) for k, d, _, _ in ABCD], gap=24),
        mono("HOW THEY AFFECT OTHERS ↓", MUT2, 22),
        row(*[abcd_cell(body(e, size=30, color=c if k != "B" else MUT), k) for k, _, e, c in ABCD], gap=24),
        body(f"* Depends on the role → an {g('A player')} in one role might be a <span style=\"color:{O}\">D player</span> in another!", size=34, extra="padding-top:12px"),
        gap=20),
    "A player: 90% likely to solve the problems you throw at them; attracts other A players. B: 75% likely; can irritate A players. C: 60% likely to FAIL, so why risk it? Drives away A players. D: lowers team productivity, drives away key talent, degrades the codebase; gets you fired. The \"affect others\" row is from the Who book: A players attract A players, B players irritate them, C players drive them away, D players get you fired for reducing productivity, driving away key talent, and reducing codebase quality.")

S["fit-def"] = slide("fit-def", "Fit", f"Defining “Fit”: −10 to {g('+10')}",
    col(f'<svg aria-label="Fit scale from orange to green" style="width:100%;height:28px" width="1664" height="28" viewBox="0 0 1664 28" preserveAspectRatio="none"><defs><linearGradient id="fitg" x1="0" x2="1"><stop offset="0" stop-color="{O}"/><stop offset="0.5" stop-color="#3A3E47"/><stop offset="1" stop-color="{G}"/></linearGradient></defs><rect width="1664" height="28" rx="14" fill="url(#fitg)"/></svg>',
        row(*[f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;align-items:{al};text-align:{ta}">'
              f'<p style="{MONO};font-size:28px;letter-spacing:2px;color:{c}">{n}</p>'
              f'<p style="{HEAD};font-size:64px;font-weight:600;color:{c}">{t}</p>'
              f'{body(d, size=30, color=MUT)}</div>'
              for n, t, d, c, al, ta in [
                  ("−10 · UNALIGNED", "Mercenary", "Here for what they can extract.", O, "start", "left"),
                  ("0", "Ambivalent", "Could go either way.", FG, "center", "center"),
                  ("+10 · ALIGNED", "Missionary", "Wants what we want.", G, "end", "right")]], gap=40),
        body(f"Do they want what we need, and do we offer what they want? {g('Both directions.')}", size=40, extra="padding-top:24px"),
        gap=40, extra="flex:1;justify-content:center"),
    "Strength is one axis; Fit is the other. Fit runs from −10 (unaligned, mercenary) through 0 (ambivalent) to +10 (aligned, missionary). It's about alignment in both directions: do they want what we need, and do we offer what they want? The next slides explain why fit matters so much for us, and what it sounds like.")

MERC_WORDS = ["fixed mindset", "defending", "me", "extrinsics", "activity", "similar", "logarithmic growth",
              "participant", "apathetic", "potential", "victim", "job", "watch", "debate"]
BELIEVER_WORDS = ["growth mindset", "learning", "we", "intrinsics", "impact", "diverse", "exponential growth",
                  "owner", "empathetic", "accomplished", "determined", "career", "engage"]
MERC_ENG_WORDS = ["résumé-driven development", "title-chaser", "counting to the vesting cliff",
                  "comp before the problem", "\u201cnot my job\u201d", "ticket-taker"]
MERC_MASHGIN_WORDS = ["cargo-culting", "offer-shopping", "hotness-chaser"]
MASHGIN_WORDS = ["scrappy", "loves hardware", "efficiency", "first principles", "build, don't buy"]


DIVIDER = '<svg aria-hidden="true" style="width:100%;height:2px;margin:6px 0" width="1600" height="2" viewBox="0 0 1600 2" preserveAspectRatio="none"><rect width="1600" height="2" fill="#3A3E47"/></svg>'


def pills(words, bg, bd, color=FG, size=34, dashed=False, vpad=10):
    style = "dashed" if dashed else "solid"
    return '<div style="display:flex;flex-direction:row;flex-wrap:wrap;gap:18px">' + "".join(
        f'<p style="font-size:{size}px;background:{bg};border:2px {style} {bd};border-radius:999px;padding:{vpad}px 24px;color:{color}">{w}</p>' for w in words) + "</div>"


S["mercenary"] = slide("mercenary", "Fit · −10", f"<span style=\"color:{O}\">Mercenary</span>",
    card(pills(MERC_WORDS, "#262321", "#4A3526", size=26, vpad=6)
         + DIVIDER
         + mono("IN ENGINEERS", O, 22) + pills(MERC_ENG_WORDS, "#262321", "#4A3526", size=26, vpad=6)
         + DIVIDER
         + mono("AT MASHGIN", O, 22) + pills(MERC_MASHGIN_WORDS, O, O, color="#060607", size=26, vpad=6),
         border=O, pad=32)
    + body(f"<span style=\"{MONO};font-size:30px;letter-spacing:2px;color:{MUT2}\">VIBE CHECK:</span> <span style=\"color:{O}\">“Pay me.”</span>", size=48),
    "Mercenary. \"Pay me.\" Fixed mindset, defending, me, extrinsics, activity over impact, participant, apathetic, victim. It's a job. In engineers: résumé-driven development (picking tech because it looks good on a CV, not because it fits the problem), chasing titles, counting down to the vesting cliff, asking about comp before the problem, \"not my job\", taking tickets instead of owning outcomes. At Mashgin: cargo-culting, offer-shopping, hotness-chasing.")


def believer_slide(sid, reveal, notes):
    if reveal:
        mash = pills(MASHGIN_WORDS, "#63E14F", "#63E14F", color="#060607")
    else:
        mash = pills(["?"] * len(MASHGIN_WORDS), "#141416", "#3A3E47", color=MUT2, dashed=True)
    return slide(sid, "Fit · +10" if not reveal else "Fit · +10 at Mashgin", f"{g('Missionary')}",
        card(pills(BELIEVER_WORDS, "#1C2619", "#2F4A2A")
             + DIVIDER
             + mono("AT MASHGIN" + ("" if reveal else " · ASK THE ROOM"), G, 26) + mash,
             border=G, pad=48)
        + body(f"<span style=\"{MONO};font-size:30px;letter-spacing:2px;color:{MUT2}\">VIBE CHECK:</span> {g('“Grow me.”')}", size=48),
        notes)


S["believer-ask"] = believer_slide("believer-ask", False,
    "Missionary. \"Grow me.\" Growth mindset, learning, we, intrinsics, impact, owner, empathetic, determined, career. Then ask the room: what does a MASHGIN missionary look like? Collect their answers before revealing the next slide.")
S["believer-all"] = believer_slide("believer-all", True,
    "Reveal: the Mashgin missionary attributes. Scrappy? Loves hardware. Efficiency. First principles. Build, don't buy. Compare with what the room said.")

WHY_FIT = [
    ("RISK", "Lots of teams. Can switch if needed.", "Must fit on <b>THIS</b> team, otherwise fired."),
    ("CONVERSION", "OK being a small part of something <b>BIG</b>.", "Wants to be the <b>HERO</b> in their thing."),
    ("MASLOW MOTIVATION", "Wants $ / Esteem", "Seeking Self-Actualization"),
]


def why_cell(html, border, color=FG):
    return f'<div style="flex:1;{CARD.format(b=border)};padding:36px;min-height:240px;display:flex;align-items:center;min-width:0"><p style="font-size:44px;line-height:1.25;color:{color}">{html}</p></div>'


S["why-fit"] = slide("why-fit", "Why fit?", f"Why is fit {g('SO')} important — at a {g('STARTUP')}?",
    col(row('<p style="width:240px;flex:none;font-size:30px">&nbsp;</p>', *[mono(h, MUT2, 30, extra="flex:1") for h, _, _ in WHY_FIT], gap=24),
        row(f'<p style="width:240px;flex:none;{MONO};font-size:34px;letter-spacing:2px;color:{MUT}">BIG TECH</p>',
            *[why_cell(b, "#2B2B2B", MUT) for _, b, _ in WHY_FIT], gap=24, align="center"),
        row(f'<p style="width:240px;flex:none;{MONO};font-size:34px;letter-spacing:2px;color:{G}">MASHGIN</p>',
            *[why_cell(m, G) for _, _, m in WHY_FIT], gap=24, align="center"),
        gap=24),
    "Why is fit SO important for us? Risk: at Google there are lots of teams, so someone can switch if it doesn't work out. At Mashgin they must fit on THIS team, otherwise they get fired. Conversion: at Google people are OK being a small part of something BIG. At Mashgin they want to be the HERO in their thing. (That difference is what converts a candidate.) Maslow motivation: Big Tech candidates want $ / esteem; Mashgin candidates are seeking self-actualization. When I joined TellApart and learned they evaluated candidates on FIT, not just technical skill, I was surprised: Google didn't, and it worked fine for them. It took time to realize Google != TellApart. Candidates can feel fit too: they often choose a company where they are a unique fit that unlocks their needs. People want to be heroes. That's the main lever startups can pull better than big companies.")

S["grid"] = slide("grid", "Should you hire them?", f"Strength {g('× Fit')}", grid(),
    "Put the two axes together. A and B players who are aligned: hire at all costs (Unicorn, Team Player). Strong but unaligned: Mercenary or Consultant. C and D players: no, whatever the fit. D players will get you fired.", title_size=64)

S["confusion"] = slide("confusion", "Should you hire them?", f"The area {g('of confusion.')}", grid(hi_cols=(1, 2)),
    "The middle of the fit axis is where most of the hard calls live: Confused, Ambivalent, the Rock Star who can be acclimated. This is where interviewers disagree.", title_size=64)

def _cx(c, f=0.5):
    return int(GX0 + c * GPX + GCW * f)


def _ry(r, f=0.5):
    return int(GY0 + r * GPY + GCH * f)


_BX2, _BX3 = GX0 + 2 * GPX - 6, GX0 + 3 * GPX - 6   # column boundaries (Confused|Rock Star, Rock Star|Unicorn)
_BY = GY0 + GPY - 6                                  # row boundary A|B
RESOLVE_ARROWS = [
    (_BX2 - 36, _ry(0), _BX2 + 36, _ry(0), O),                  # Confused -> Rock Star
    (_BX2 - 30, _BY + 30, _BX2 + 30, _BY - 30, O),              # Ambivalence -> Rock Star (corner)
    (_cx(2, 0.86), _BY + 36, _cx(2, 0.86), _BY - 36, YELLOW),               # Ambivalence -> Rock Star (up)
    (_cx(3, 0.86), _BY + 36, _cx(3, 0.86), _BY - 36, YELLOW),               # Team Player -> Unicorn
    (_BX3 - 36, _ry(0), _BX3 + 36, _ry(0), G),                  # Rock Star -> Unicorn
]


def legend_item(color, text):
    return row(f'<svg width="70" height="24" viewBox="0 0 70 24" style="flex:none"><line x1="2" y1="12" x2="52" y2="12" stroke="{color}" stroke-width="7" stroke-linecap="round"/><polygon points="68,12 48,2 48,22" fill="{color}"/></svg>',
               body(text, size=26), gap=16, align="center")


S["resolve"] = slide("resolve", "Should you hire them?", f"Resolve it, {g('or coach it.')}",
    grid(arrows=RESOLVE_ARROWS)
    + col(legend_item(O, "Resolve before hiring"),
          legend_item(YELLOW, "Coach in the first 90–180 days"),
          legend_item(G, "Coach in the first 2 years"),
          gap=28, extra=f"position:absolute;left:{GX0 + 3 * GPX + GCW + 48}px;top:{GY0 + 40}px;width:{1920 - 96 - (GX0 + 3 * GPX + GCW + 48)}px"),
    "Confusion and ambivalence: resolve before you hire (red arrows). Moving up a strength level, B to A: you can coach that in the first 90-180 days (yellow). A Rock Star becoming a Unicorn, fully aligned: you can coach that over the first 2 years (green). 90-day reviews let you cut the B players if you made a mistake. Hold yourself accountable to coaching them.", title_size=64)

S["tool-pain"] = slide("tool-pain", "Resolve before hiring: Mercenaries", f"Give them {g('some pain.')}",
    row(*[flex1(card(mono(k, O, 24) + f'<p style="{HEAD};font-size:72px;font-weight:600">{w}</p>'
                     + f'<svg aria-hidden="true" width="80" height="80" viewBox="0 0 80 80"><g fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{icon}</g></svg>', pad=48))
          for k, w, icon in [
              ("CHALLENGE", "World View",
               '<circle cx="40" cy="40" r="30"/><ellipse cx="40" cy="40" rx="13" ry="30"/><path d="M10 40 H70 M15 24 H65 M15 56 H65"/>'),
              ("MAKE IT REAL", "Lower Pay",
               '<path d="M40 8 V72 M56 22 C52 16 46 14 40 14 C30 14 24 19 24 27 C24 45 57 35 57 53 C57 61 50 66 40 66 C32 66 26 63 22 57"/>'),
              ("COLD SPLASH", "Title Shrink",
               '<path d="M4 30 L40 14 L76 30 L40 46 Z M20 37 V55 C20 61 30 66 40 66 C50 66 60 61 60 55 V37 M76 30 V52"/><circle cx="76" cy="56" r="3" fill="#FF832A"/>'),
          ]], gap=40)
    + body(f"How they react tells you how they think about the role. {g('(You can always walk it back later.)')}", size=40, color=MUT),
    "Tools to identify MERCENARIES/CONSULTANTS: give them some pain they won't accept. Challenge their world view. Make it real: lower pay. Cold splash: title shrink. How they react will tell you a lot about how they are thinking about the role. You can always walk it back later.")

S["b-causes"] = slide("b-causes", "Resolve before hiring: B Players", f"Was it THEM, or {g('their environment?')}",
    row(*[flex1(card(mono(k, O, 24) + f'<p style="{HEAD};font-size:60px;font-weight:600;line-height:1.05">{w}</p>'
                     + f'<svg aria-hidden="true" width="156" height="130" viewBox="0 0 96 80"><g fill="none" stroke="{O}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round">{icon}</g></svg>', pad=48))
          for k, w, icon in [
              ("RE-INTERVIEW", "Missed Strengths",   # B3: overhead lift
               '<path d="M6 12 H90"/><rect x="12" y="2" width="8" height="20" rx="2" fill="#FF832A"/><rect x="76" y="2" width="8" height="20" rx="2" fill="#FF832A"/>'
               '<circle cx="48" cy="32" r="6"/><path d="M30 12 L40 38 H56 L66 12 M48 38 V58 M48 58 L36 76 M48 58 L60 76"/>'),
              ("LACKED OPPORTUNITY", "Challenging Onboarding",   # R3: breaking the tape
               '<path d="M6 28 V76 M90 28 V76"/><path d="M6 38 L34 46 M62 46 L90 38" stroke-width="4"/>'
               '<circle cx="48" cy="12" r="7"/><path d="M47 20 L45 48 M46 27 L32 14 M46 27 L60 14 M45 48 L34 70 M45 48 L57 62 L64 74"/>'),
              ("WRONG MENTORSHIP", "Pair with Your Best",   # hero, side view, jumping, cape rippling
               '<path d="M57 22 C46 15 38 27 28 22 C20 18 13 26 4 21 C10 33 19 31 27 37 C35 43 43 38 49 45 Z" fill="#FF832A" fill-opacity="0.35" stroke-width="3"/>'
               '<circle cx="63" cy="13" r="7"/><path d="M59 20 L47 46 M56 26 L78 9 M55 28 L42 24 M47 46 L58 56 L52 68 M47 46 L35 58 L25 63"/>'
               '<circle cx="80" cy="7" r="3" fill="#FF832A"/><path d="M8 78 H40 M14 72 L20 72 M28 72 L32 72" stroke-width="3"/>'),
          ]], gap=40)
    + body(f"A B on paper can be opportunity and coaching, {g('not ability.')}", size=40, color=MUT),
    "Before writing someone off as a B player, check whether it was them or their environment. Interview process failure: we didn't find their strengths, so re-interview for the strengths we missed. Lacked opportunity: give them a challenging onboarding. Wrong mentorship: pair them with your best. Some of our Mashgin Brazil team were B players because of OPPORTUNITY and PREVIOUS COACHING.")

S["tool-b"] = slide("tool-b", "Resolve before hiring: B Players", f"Grit + intelligence: {g('watch the slope.')}",
    row(f'<svg width="1000" height="520" viewBox="0 0 1000 520"><line x1="40" y1="20" x2="40" y2="470" stroke="#3A3E47" stroke-width="4"/><line x1="40" y1="470" x2="980" y2="470" stroke="#3A3E47" stroke-width="4"/>'
        f'<path d="M40 380 C 300 330, 600 180, 960 60" fill="none" stroke="#63E14F" stroke-width="8" stroke-linecap="round"/>'
        f'<path d="M40 380 C 300 372, 600 368, 960 362" fill="none" stroke="#FF832A" stroke-width="8" stroke-linecap="round"/>'
        f'<line x1="700" y1="20" x2="700" y2="470" stroke="#8B9097" stroke-width="3" stroke-dasharray="10 10"/>'
        f'<text x="712" y="500" fill="#8B9097" font-family="DM Mono, monospace" font-size="26">DAY 90</text>'
        f'<text x="40" y="510" fill="#8B9097" font-family="DM Mono, monospace" font-size="26">DAY 1</text></svg>',
        col(card(mono("A PLAYER", G, 24) + body("Adjusts fast.")),
            card(mono("B PLAYER", O, 24) + body("Never pushed themselves. No change by day 90.")), extra="flex:1"),
        gap=56, align="center"),
    "Tools to identify B players (grit + intelligence): they never pushed themselves before, and in 90 days they don't adjust their behavior.")

S["venn"] = slide("venn", "Fit runs three ways", f"Would they be an A player {g('here?')}",
    row('<svg width="640" height="600" viewBox="0 0 640 600"><circle cx="320" cy="200" r="170" fill="#63E14F" fill-opacity="0.12" stroke="#63E14F" stroke-width="4"/><circle cx="215" cy="380" r="170" fill="#FF832A" fill-opacity="0.10" stroke="#FF832A" stroke-width="4"/><circle cx="425" cy="380" r="170" fill="#45C7AB" fill-opacity="0.10" stroke="#45C7AB" stroke-width="4"/>'
        '<text x="320" y="120" text-anchor="middle" fill="#63E14F" font-family="DM Mono, monospace" font-size="30">EMPLOYEE</text><text x="150" y="450" text-anchor="middle" fill="#FF832A" font-family="DM Mono, monospace" font-size="30">ROLE</text><text x="490" y="450" text-anchor="middle" fill="#45C7AB" font-family="DM Mono, monospace" font-size="30">COMPANY</text>'
        '<text x="320" y="330" text-anchor="middle" fill="#F4F5F7" font-family="Host Grotesk, Arial, sans-serif" font-weight="600" font-size="48">A?</text></svg>',
        col(card(mono("EMPLOYEE", G, 24) + body("Skill / Will “vector”", 36), border=G),
            card(mono("ROLE", O, 24) + body("Too big<br>Too small<br>Not interesting", 36) + body("“Goldilocks problem”", 30, MUT), border=O),
            card(mono("COMPANY", "#45C7AB", 24) + body("Culture: “the unspoken rules”", 36), border="#45C7AB"),
            gap=24, extra="flex:1"), gap=64, align="center"),
    "Fit runs three ways: employee, company, role. Employee perspective: what will I learn? What can I teach? What value can I add? How will this advance my career? Do I like the culture, the product, the team? Company perspective: is there a 90% chance they can do what only the top 10% can do in the role? Do they fit culturally? Do they exhibit the company's key values? What is the value, what is the risk?")

S["culture"] = slide("culture", "", "",
    col(f'<p style="{MONO};font-size:28px;letter-spacing:2px;text-transform:uppercase;color:{G}">[ So how do we run it? ]</p>',
        f'<p style="{HEAD};font-size:112px;font-weight:600;line-height:1.05;color:#F4F5F7">Candidates see the process.<br>{g("But they judge the culture.")}</p>',
        gap=48, extra="flex:1;justify-content:center"),
    "Candidates see the process, but they judge the culture. Who we are in the interview process should reflect our core values. The candidate is evaluating us the whole time. Three things they see.")


def bar(label, segs, note, color):
    total = sum(w for w, _ in segs)
    x, rects = 0, []
    for w, c in segs:
        ww = w / total * 1100
        rects.append(f'<rect x="{x:.0f}" y="0" width="{ww - 8:.0f}" height="56" rx="8" fill="{c}"/>')
        x += ww
    inner = f'<svg width="1100" height="56" viewBox="0 0 1100 56">{"".join(rects)}</svg>'
    return row(f'<p style="width:220px;{MONO};font-size:28px;letter-spacing:2px;color:{color}">{label}</p>',
               inner, mono(note, color, 24), gap=32, align="center")


DRAFT_STAMP = (f'<p style="position:absolute;right:380px;top:150px;transform:rotate(-12deg);{MONO};font-size:64px;font-weight:500;'
               f'letter-spacing:8px;color:{O};border:6px solid {O};border-radius:12px;padding:6px 28px">DRAFT</p>')

S["speed"] = slide("speed", "The process is our culture · 1", f"Startups should {g('move fast.')}",
    row(flex1(card(mono("MOVE SLOW, THEN FAST", G, 24) + body("We lose if they think about it for months. Onsites when they are ready to decide.", 32)
                   + body("“Where are you in <b>YOUR</b> process?”", 32, G), pad=40, extra="height:100%")),
        flex1(card(mono("MISSIONARY VIBES", G, 24) + body("We’re a startup and expect people to make quick decisions on incomplete information. That includes the interview.", 32)
                   + body("“What do you need to commit?”", 32, G), pad=40, extra="height:100%")),
        flex1(card(mono("NO PRESSURE SELLING", G, 24) + body("We don’t take important decisions lightly. Give people the space to think and decide, without any fake urgency.", 32), pad=40, extra="height:100%")),
        gap=32),
    "Speed matters. We lose candidates when we move slowly. One candidate never even got to the onsite. Another was held back for weeks, then took a competing offer. We can control our speed. How do we create a sense of urgency on the candidate side? If we succeed, we can control their speed to some degree too. We never want to lie (\"I only have 2 roles open\").")

def person(x, y, color, label="", label_color=MUT2, above=False):
    """Head + shoulders glyph centred on (x, y)."""
    out = (f'<circle cx="{x}" cy="{y - 26}" r="20" fill="{color}"/>'
           f'<path d="M{x - 38} {y + 34} C{x - 38} {y + 4} {x - 22} {y - 2} {x} {y - 2} C{x + 22} {y - 2} {x + 38} {y + 4} {x + 38} {y + 34} Z" fill="{color}"/>')
    if label:
        ly = y - 58 if above else y + 66
        out += f'<text x="{x}" y="{ly}" text-anchor="middle" fill="{label_color}" font-family="DM Mono, monospace" font-size="18" letter-spacing="2">{label}</text>'
    return out


def arrow_line(x1, y1, x2, y2, color, both=False, dash=""):
    import math
    a = math.atan2(y2 - y1, x2 - x1)

    def head(px, py, ang):
        p1 = (px - 20 * math.cos(ang - 0.45), py - 20 * math.sin(ang - 0.45))
        p2 = (px - 20 * math.cos(ang + 0.45), py - 20 * math.sin(ang + 0.45))
        return f'<polygon points="{px:.0f},{py:.0f} {p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}" fill="{color}"/>'
    d = f' stroke-dasharray="{dash}"' if dash else ""
    out = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="5" stroke-linecap="round"{d}/>' + head(x2, y2, a)
    if both:
        out += head(x1, y1, a + math.pi)
    return out


GRILL_SVG = (person(110, 90, "#8B9097", "INTERVIEWER") + person(110, 250, "#8B9097", "INTERVIEWER")
             + person(410, 170, "#3A3E47", "CANDIDATE")
             + arrow_line(165, 92, 352, 150, O) + arrow_line(165, 248, 352, 190, O)
             + f'<text x="262" y="104" text-anchor="middle" fill="{O}" font-family="Host Grotesk, Arial, sans-serif" font-weight="600" font-size="34">?</text>'
             + f'<text x="262" y="262" text-anchor="middle" fill="{O}" font-family="Host Grotesk, Arial, sans-serif" font-weight="600" font-size="34">?</text>')
TALK_SVG = (person(260, 100, G, "CANDIDATE", G, above=True) + person(110, 250, "#E9ECEF", "INTERVIEWER") + person(410, 250, "#E9ECEF", "INTERVIEWER")
            + arrow_line(152, 200, 216, 146, G, both=True) + arrow_line(368, 200, 304, 146, G, both=True)
            + arrow_line(170, 262, 350, 262, G, both=True))

S["room"] = slide("room", "The process is our culture · 2", f"Two people.<br>{g('A conversation, not a grilling.')}",
    row(*[flex1(card(mono(k, c, 26, extra="text-align:center")
                     + f'<svg aria-label="{al}" width="520" height="340" viewBox="0 0 520 340" style="align-self:center">{svg}</svg>'
                     + body(t, color=MUT, extra="text-align:center"), border=b, pad=40))
          for k, c, b, svg, t, al in [
              ("GRILLING", O, "#2B2B2B", GRILL_SVG, "Questions fired one way.", "Two interviewers firing questions at one candidate"),
              ("CONVERSATION", G, G, TALK_SVG, "Ideas flow every direction.", "Candidate and two interviewers talking in a triangle")]], gap=40),
    "Every interview has two interviewers in the room. The dynamic should be a conversation between three people, not two people grilling one.")

S["growth"] = slide("growth", "The process is our culture · 3", f"A growth factory, {g('from the first call.')}",
    col(*[row(f'<p style="width:300px;flex:none;white-space:nowrap;{MONO};font-size:26px;letter-spacing:2px;color:{G}">{k}</p>',
              f'<p style="width:320px;flex:none;{HEAD};font-size:52px;font-weight:600">{r}</p>',
              body(q, size=36, color=FG, extra="flex:1;min-width:0;white-space:nowrap"),
              gap=24, align="center", extra=f"{CARD.format(b=(G if i == 3 else '#2B2B2B'))};padding:22px 48px")
          for i, (k, r, q) in enumerate([("01 · FIRST CALL", "Recruiter", "“Where do you want to grow?”"),
                                         ("02 · SCREEN", "EM", "“What's your next step?”"),
                                         ("03 · ONSITE", "Engineers", "“Here's how you'd grow here.”"),
                                         ("04 · TOPGRADING", "EM", "“Here is feedback on your performance.”")])], gap=18)
    + body("Every person they meet shows interest in their growth.", size=40),
    "From recruiters, to the EM, to the engineers: every touchpoint shows real interest in the candidate's growth. That's how they learn we're a growth factory before they ever join.")

# Original silhouette scene (no film likeness): a wizard on a ridge, nine walkers on the road below.
def walker(x, base, h, color="#14161B"):
    head = h * 0.16
    return (f'<circle cx="{x}" cy="{base - h + head}" r="{head}" fill="{color}"/>'
            f'<path d="M{x - h * 0.17} {base} L{x - h * 0.12} {base - h + head * 2.1} L{x + h * 0.12} {base - h + head * 2.1} L{x + h * 0.17} {base} Z" fill="{color}"/>'
            f'<path d="M{x + h * 0.14} {base - h * 0.62} L{x + h * 0.32} {base - h * 0.35}" stroke="{color}" stroke-width="{max(3, h * 0.05):.0f}" stroke-linecap="round"/>')


GANDALF_SVG = (
    '<svg aria-label="Silhouette of a wizard with a staff on a ridge at sunset, watching nine travellers set out on the road" width="760" height="760" viewBox="0 0 760 760" style="flex:none;border-radius:24px">'
    '<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1B1D26"/><stop offset="0.55" stop-color="#5A2E14"/><stop offset="1" stop-color="#FF832A"/></linearGradient>'
    '<radialGradient id="sun" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFD9A8"/><stop offset="1" stop-color="#FF832A" stop-opacity="0"/></radialGradient></defs>'
    '<rect width="760" height="760" fill="url(#sky)"/>'
    '<circle cx="520" cy="470" r="190" fill="url(#sun)"/>'
    '<path d="M0 560 C140 520 260 540 380 520 C520 498 640 520 760 500 V760 H0 Z" fill="#2A1A12"/>'
    '<path d="M0 640 C180 600 360 640 520 610 C640 590 700 600 760 590 V760 H0 Z" fill="#14161B"/>'
    '<path d="M300 760 C380 700 480 640 640 600" fill="none" stroke="#3A2A20" stroke-width="18" stroke-linecap="round"/>'
    + "".join(walker(x, b, h) for x, b, h in [(430, 668, 46), (462, 655, 44), (492, 646, 60), (522, 636, 58), (552, 628, 62), (580, 620, 34), (602, 615, 33), (624, 610, 32), (646, 604, 34)])
    + '<g fill="#0B0C10">'
      '<path d="M150 760 L176 470 C178 448 196 438 214 440 C232 442 246 456 248 476 L272 760 Z"/>'
      '<path d="M168 456 L232 248 L276 452 C256 470 196 474 168 456 Z"/>'
      '<path d="M140 452 C176 440 268 436 300 452 C270 466 172 468 140 452 Z"/>'
      '<path d="M196 478 C204 520 220 548 236 560 C246 528 248 500 240 474 Z"/>'
      '<path d="M120 300 L104 760" stroke="#0B0C10" stroke-width="12" stroke-linecap="round"/>'
      '<path d="M122 296 C112 290 106 300 112 308" fill="none" stroke="#0B0C10" stroke-width="10" stroke-linecap="round"/>'
      '<path d="M178 540 L120 520" stroke="#0B0C10" stroke-width="22" stroke-linecap="round"/>'
    '</g></svg>')

GANDALF_ROWS = [
    ("BILBO", "Wanted his armchair and second breakfast.",
     "Gandalf saw the Took in him, marked his door for “a burglar,” and sent the Dwarves round before he could say no."),
    ("THORIN & CO.", "Wanted their gold and their mountain back.",
     "Gandalf backed their quest. His own aim: get rid of Smaug before the dragon could serve the Enemy."),
    ("ARAGORN", "Ranger in the wild, king in waiting.",
     "Gandalf had known him for decades and kept pointing him at the throne he was born for."),
    ("FRODO", "Never asked to go.",
     "Once Gandalf showed him what was at stake, he volunteered at Elrond's council: “I will take the Ring.”"),
]

GANDALF_IMG = "/_blob/19781f27c92a434e2a16517baad7b90c"
GANDALF_SHORT = [("BILBO", "Wanted his armchair. Gandalf saw the Took in him: a buried hunger for adventure."),
                 ("THORIN & CO.", "Wanted their mountain back. Gandalf gave the quest a plan, and a burglar."),
                 ("ARAGORN", "Wanted the crown, and Arwen. Gandalf stood by who he really was."),
                 ("FRODO", "Wanted to save the Shire. Gandalf showed him why it had to be him.")]
S["gandalf"] = slide("gandalf", "", "",
    f'<img src="{GANDALF_IMG}" alt="Storybook illustration: a grey wizard scratches a glowing rune on a round green hillside door while a startled hobbit peers out, and a line of hooded dwarves with lanterns walks up the road at dusk" style="position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover">'
    '<div style="position:absolute;left:0;top:0;width:1920px;height:1080px;background:linear-gradient(90deg, rgba(6,6,7,0) 52%, rgba(6,6,7,0.55) 72%, rgba(6,6,7,0.85) 100%)"></div>'
    '<div style="position:absolute;left:0;top:840px;width:1920px;height:240px;background:linear-gradient(180deg, rgba(6,6,7,0) 0%, rgba(6,6,7,0.85) 100%)"></div>'
    f'<p style="position:absolute;left:1152px;top:130px;width:640px;{MONO};font-size:28px;letter-spacing:2px;color:{G};text-shadow:0 2px 12px rgba(0,0,0,0.6)">[ ONE LAST THING ]</p>'
    f'<h2 style="position:absolute;left:1152px;top:180px;width:640px;{HEAD};font-size:120px;font-weight:600;line-height:1;color:#F4F5F7;text-shadow:0 4px 24px rgba(0,0,0,0.65)">Be {g("Gandalf")}</h2>'
    f'<div style="position:absolute;left:1152px;top:340px;width:640px;background:rgba(10,10,12,0.74);border:2px solid #2B2B2B;border-radius:20px;padding:30px;display:flex;flex-direction:column;gap:16px">'
    + "".join(col(mono(n, O, 24), body(w, size=26, color=FG), gap=4) for n, w in GANDALF_SHORT)
    + body(f"Meet each recruit’s real motive — {g('and know them better than they know themselves.')}", size=26)
    + '</div>',
    "Be Gandalf: the best recruiter in fiction. Bilbo wanted his comfort; Gandalf knew he had a Took's taste for adventure and signed him up before he could refuse (The Hobbit, ch. 1: the mark on the door, the Dwarves arriving). Thorin's company wanted their treasure and homeland back; Gandalf backed them, while his real goal was removing Smaug as a threat (Unfinished Tales, 'The Quest of Erebor'). Aragorn was the heir of Isildur living as a Ranger; Gandalf was his long-time friend and ally. Frodo volunteered at the Council of Elrond, 'I will take the Ring, though I do not know the way.' Real motives. Bilbo: his Tookish side; the dwarves' song woke a longing to see the mountains and wear a sword instead of a walking-stick, and Gloin's jab that he looked more like a grocer than a burglar stung his pride into saying yes. Gandalf had told the dwarves there was more in Bilbo than he had any idea of himself. Aragorn: to claim the crown of Gondor and Arnor, the condition Elrond set for marrying Arwen (Appendix A); Gandalf was his long-time ally and vouched for him in his letter at Bree. Frodo: love of the Shire; he said he wanted to save it. Note: in The Lord of the Rings, Elrond formally chose the Nine; Gandalf's recruiting shows most in The Hobbit.")

for sid, html in S.items():
    if sid in HANDWRITTEN or sid not in ORDER:
        continue
    open(os.path.join(SL, sid + ".html"), "w").write(html)

# Renumber the hand-written slides
for sid in HANDWRITTEN - {"cover"}:
    p = os.path.join(SL, sid + ".html")
    s = open(p).read()
    s = re.sub(r'\[ \d+ \]</p>(\s*)<aside>', lambda m: f'[ {ORDER.index(sid) + 1} ]</p>{m.group(1)}<aside>', s)
    s = s.replace(' data-section="Arc 1: evaluating candidates on Strength and Fit."', "")
    open(p, "w").write(s)

missing = [s for s in ORDER if not os.path.exists(os.path.join(SL, s + ".html"))]
assert not missing, missing

dj = os.path.join(ROOT, "deck.json")
d = json.load(open(dj))
d["title"] = "The Art of Hiring — Arc 1"
d["order"] = ORDER
d["sections"] = {
    "s1": {"description": "What is hiring: a funnel, and matchmaking.", "start": "cover"},
    "s2": {"description": "Two dimensions: A players and fit.", "start": "dimensions"},
    "s3": {"description": "Should you hire them: the Strength × Fit grid and tools.", "start": "grid"},
    "s4": {"description": "The process is our culture.", "start": "culture"},
}
json.dump(d, open(dj, "w"))
print("ok", len(ORDER))

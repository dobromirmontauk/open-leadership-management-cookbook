# The Art of Hiring — talk decks

A three-arc talk for engineering leaders, about 30 minutes per arc:

1. **Evaluate** (Arc 1): Strength × Fit. Who should we hire?
2. **Train** (Arc 2): the five levels of an A-player interviewer.
3. **Build** (Arc 3): the 3-stage process. Not written yet.

Philosophy, content and process borrow heavily from TellApart, Twitter, Wade Chambers, and *Who: The A Method for Hiring*.

## Live decks (claude.ai Slides artifacts, private)

| Deck | URL |
|---|---|
| Arc 1 — Evaluate | https://claude.ai/artifact/NyqTL9Rvd6wXn6bsDhFcmm |
| Arc 2 — Train | https://claude.ai/artifact/D1oJQ5yCpmiz2DuwmJ3nS3 |

`exports/` holds the Arc 1 PDF, PPTX and standalone HTML. They come from the deck's **Share › Export**.

**Public copy:** the live decks end with case studies about real people (Arc 1: true/false positives; Arc 2: per-level examples and recap). Those slides are cut from everything here: the snapshots, the generators, the images and the exports. Speaker notes that named candidates are anonymized. After re-exporting from the live deck, cut the case-study pages again before you commit.

## Layout

| Path | What |
|---|---|
| `arc1/project/`, `arc2/project/` | Snapshot of each live deck: `deck.json` plus one `slides/<id>.html` per slide. **This is the source of truth.** |
| `build_arc1.py` | Generates Arc 1 slides from Python helpers and content. Skips the ids in `HANDWRITTEN` (it only renumbers them) and any id not in `ORDER`. |
| `build_arc2.py` | Arc 2. Execs the helpers from `build_arc1.py`. |
| `icons.py` | SVG icons for the "Startup vibes" slide. |
| `gen_gandalf.py`, `edit_gandalf.py` | Gemini image generation for the Gandalf/dwarves art. |
| `x/` | Final generated images (also uploaded to the decks as blobs). |
| `private/` | Git-ignored local copy of the raw drafts (original pptx, notes, outline). They contain case-study material. |

## Editing workflow

Slides get edited by hand in the claude.ai viewer, so the live deck can be ahead of these files.

1. **Read the live deck first.** Use the Artifact `read` action with `paths`, saving into a scratch folder. Sync the result into `arcN/project/`.
2. Edit the slide HTML directly, or edit the generator and run `python3 build_arc1.py`. Any slide that has been hand-edited in the viewer must be in `HANDWRITTEN`, or the generator overwrites those edits. Check with `diff -r` against the fresh read.
3. **Publish only the changed files**: `url` = the deck, `root` = `arcN`, `file_path` = one changed slide, and `files` = the rest. A publish is refused if the live file changed since your read. When that happens, re-read and re-apply.

Images are referenced as `/_blob/<id>` and live in the artifact's asset store:

| Blob | Image |
|---|---|
| `b4e74a8e…` / `9b7ec390…` | Logo (Arc 1 / Arc 2) |
| `19781f27…` | Gandalf / dwarves (`x/dwarves_1.jpg`) |

## Style

- Canvas is 1920×1080 with background `#060607`.
- Cards are `#1A1A1A` with a 2px `#2B2B2B` border and 16px radius.
- Accent colours: green `#63E14F` (good / A player), orange `#FF832A` (risk / false positive), yellow `#F5D227`, teal `#45C7AB`.
- Fonts: Host Grotesk (headings), DM Mono (labels and numbers), Raleway (body).
- Footer: "Copyright Dobromir Montauk, 2026" plus the slide number `[ n ]`.
- Speaker notes go in `<aside>`.

Slides renderer quirks:

- It drops empty `<div>`s, so use `&nbsp;` spacers or SVG.
- It ignores padding on flex rows, so put padding on cards.
- Always check the result in the live viewer.

## Gemini image generation

The scripts read `GEMINI_API_KEY` from the environment. **Never commit the key.** Model: `gemini-3-pro-image` at 2K. Run them from this folder; output goes to `x/`.

```sh
GEMINI_API_KEY=... python3 gen_gandalf.py
```

# Source files

The talk was built as a Claude Slides artifact. These are its sources, lightly sanitized for a public repo (company-specific examples and logos removed; the outline's TODO slide dropped).

- `deck.json`: slide order and sections.
- `slides/*.html`: one file per slide. The image is the slide; speaker notes are in `<aside>`. Image paths point at `../images/`.
- `images/`: the full-size PNGs used by the slides.
- `prompts/`: the Nano Banana (Gemini image) prompts, including drafts and fix-up edit passes.
- `ref/`: character reference sheets passed as `--ref` for consistency (`cast-biz-v2.png` plus `mgr-head.png` for the Manager).

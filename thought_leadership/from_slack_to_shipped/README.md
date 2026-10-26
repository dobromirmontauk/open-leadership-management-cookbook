# From Slack to Shipped

A talk about building software with AI, illustrated with Maya and Robo-Maya. Originally prepared for Great Question in June 2026.

## Files

- [PowerPoint deck](from-slack-to-shipped.pptx) — the original 21 slides.
- [Outline and talk track](from-slack-to-shipped.md).
- `images/` — original character sheets, illustrations, backgrounds and screenshots.
- `source/` — the complete unpacked PowerPoint, including embedded slide artwork, notes, relationships and layouts.
- [build.py](build.py) — rebuilds the PowerPoint with Python 3 and no extra dependencies.

## Rebuild

Run from this directory:

```sh
python3 build.py
```

Or write a separate copy:

```sh
python3 build.py --output /tmp/from-slack-to-shipped.pptx
```

The original authoring script was not present in the saved project. This rebuild script packages the preserved PowerPoint source without changing any slide parts. The existing slides are flattened images: editing the outline does not automatically change the deck. To change a slide, edit or replace its image below, preserving its dimensions, then rebuild. Advanced changes to layouts and speaker notes can be made in `source/`, or by opening the deck in PowerPoint. Edits made directly in PowerPoint must be unpacked back into `source/` before running this script again.

The artwork in `images/` is reference material; the images actually used by the deck are under `source/ppt/media/`. Character sheets and visual directions in the outline can guide future image generation; generating new illustrations requires a separate image tool.

## Slide artwork

| Slide | Image used in the deck |
|---|---|
| 1 | [Slide 1 artwork](source/ppt/media/image1.png) |
| 2 | [Slide 2 artwork](source/ppt/media/image2.png) |
| 3 | [Slide 3 artwork](source/ppt/media/image3.png) |
| 4 | [Slide 4 artwork](source/ppt/media/image4.png) |
| 5 | [Slide 5 artwork](source/ppt/media/image5.png) |
| 6 | [Slide 6 artwork](source/ppt/media/image6.png) |
| 7 | [Slide 7 artwork](source/ppt/media/image7.png) |
| 8 | [Slide 8 artwork](source/ppt/media/image8.png) |
| 9 | [Slide 9 artwork](source/ppt/media/image9.png) |
| 10 | [Slide 10 artwork](source/ppt/media/image10.png) |
| 11 | [Slide 11 artwork](source/ppt/media/image11.png) |
| 12 | [Slide 12 artwork](source/ppt/media/image12.png) |
| 13 | [Slide 13 artwork](source/ppt/media/image13.png) |
| 14 | [Slide 14 artwork](source/ppt/media/image14.png) |
| 15 | [Slide 15 artwork](source/ppt/media/image15.png) |
| 16 | [Slide 16 artwork](source/ppt/media/image16.png) |
| 17 | [Slide 17 artwork](source/ppt/media/image17.png) |
| 18 | [Slide 18 artwork](source/ppt/media/image18.png) |
| 19 | [Slide 19 artwork](source/ppt/media/image13.png) |
| 20 | [Slide 20 artwork](source/ppt/media/image19.png) |
| 21 | [Slide 21 artwork](source/ppt/media/image20.png) |

# HyperFrames Editorial Templates

A library of 42 drop-in video templates — each an 8-second, 1920×1080, 30 fps
HyperFrames composition built on one white, typographic design system. Preview
every template, then copy its composition id into your own project. Some of them
are adopted from [HyperFrames Catalog](https://hyperframes.heygen.com/catalog) and
[React Video Editor](https://www.reactvideoeditor.com/).

**[Browse the gallery →](https://justintse-cal.github.io/hyperframe-templates/)**

---

## What's here

| | Group | Templates |
| --- | --- | --- |
| **A** | Openers & Statements | breaking-news · chapter-card · headline-stack · speech-statement |
| **B** | Explain & Summarize | core-definition · mechanism-walkthrough · problem-solution · news-summary · term-explanation |
| **C** | Compare & Contrast | paradigm-shift · split-tilt-cards · split-panels · split-screens |
| **D** | Process & Flow | milestone-timeline · decision-tree · feedback-loop · handdrawn-flowchart · progress-steps · flowchart |
| **E** | Structure & Systems | architecture-stack · network-node-map · radial-surround · grid-card-assemble · specs-list |
| **F** | Data & Numbers | metric-highlight · barchart-growth · linechart-trend · pie-donut-share · news-stat · chart-card · unit-chart · progress-stat |
| **G** | Social Proof & Audience | press-quote · yt-comment-stack · reddit-post-card · testimonial-card · yt-comment-scatter · subscribe-outro |
| **H** | Screens & Artifacts | terminal-editor · article-circle · typed-prompt · notes-typing |

Templates are grouped by the **job each one does in an edit**, not by the medium
it imitates. Ids are stable slugs, so a template can move between groups without
renaming its file.

Every template is exactly **8 seconds**, so they stack into a uniform grid. The
root reel in `index.html` plays all 42 back-to-back (336s total).

### Template catalog

[`docs/templates.md`](./docs/templates.md) is the **template catalog** — for every
template, one sentence on what it is and one on what it's used for, plus a short
note on the canvas, the design system and how to mount a template.

Paste it into an AI agent to give it a working knowledge of the library, or use
the **"Copy full catalog for AI"** button on the gallery site.

## Design system

All templates follow [`design.md`](./design.md) — read it before editing a frame.
The short version:

- **Canvas** — 1920×1080 on a white `#ffffff` frame (never a gradient).
- **Palette** — one theme per template (Blue, Red, Green, Yellow, Orange); black text by default, theme accent for highlights only.
- **Type** — Noto Sans for everything, with Noto Sans TC for Traditional Chinese; hierarchy comes from size and weight.
- **Motion** — entrance-only, deterministic and seek-safe. No exit animations.
- **Safe area** — keep the bottom ~15% (below y≈920px) clear of content.
- **No corner text** — no badges, footers, or watermarks; a textless `.frame-border` is allowed.

### Typography

Frames are set in **Noto Sans**, the Google Fonts variable family, with **Noto Sans
TC** as its Traditional Chinese companion. One family carries every role —
display, headings, body, labels, chart text, numbers — so hierarchy comes from
size, weight and spacing instead of mixing typefaces, and a mixed-script frame
reads as a single voice.

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap');
```

Each weight gets a utility class whose name and declaration agree:

```css
.noto-sans-700 {
  font-family: "Noto Sans", sans-serif;
  font-optical-sizing: auto;
  font-weight: 700;
  font-style: normal;
  font-variation-settings: "wdth" 100;
}

.noto-sans-tc-500 {
  font-family: "Noto Sans TC", sans-serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}
```

Fallback stack: `"Noto Sans", "PingFang TC", "Microsoft JhengHei", sans-serif`.
The full scale, weight assignments and CJK pairing rules live in
[`design.md` §6](./design.md).

> The committed preview renders and the frames themselves still carry the
> previous Playfair Display / Plus Jakarta Sans stack; migrating the 42
> compositions to Noto Sans is tracked separately.

## Quick start

```bash
npm run dev        # open a live preview in the browser
npm run check      # lint + runtime + layout + motion + contrast
npm run render     # render the full reel to MP4
```

To use a template in your own HyperFrames project, copy the matching file from
`compositions/` and reference it from your host composition:

```html
<div
  data-composition-id="core-definition"
  data-composition-src="compositions/core-definition.html"
  data-start="0"
  data-duration="8"
  data-track-index="1"
  data-width="1920"
  data-height="1080"
></div>
```

## Project structure

```
index.html               root reel — one slot per template, 8s each (336s)
compositions/            one sub-composition per template (core-definition, …)
compositions/components/ paste-in effect snippets from the HyperFrames registry
stock media/             placeholder images & footage used by the templates
docs/                    the GitHub Pages gallery (static HTML/CSS/JS)
docs/templates.md        the full agent-facing template catalog (copy it into an AI)
scripts/                 showcase render pipeline (reel → previews + posters)
design.md                the design system — read before editing any frame
AGENTS.md                working conventions for humans and agents
```

### Regenerating the gallery previews

```bash
node scripts/render-showcase.mjs --render
```

This renders the full reel once, then slices it per slot into 720p previews
(`docs/videos/`) and posters (`docs/posters/`). Requires `ffmpeg` on your PATH.

## License

[MIT](./LICENSE) © 2026 Justin.

Built with [HyperFrames](https://hyperframes.heygen.com). Some templates are
adapted from HyperFrames registry blocks and components and restyled to fit this
project's design system; the HyperFrames CLI and registry are separate products
under their own terms.

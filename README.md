# HyperFrames Editorial Templates

A library of 35 drop-in video templates — each an 8-second, 1920×1080, 30 fps
HyperFrames composition built on one warm editorial design system. Preview every
template, then copy its composition id into your own project. Some of them are adopted from [HyperFrames Catalog](https://hyperframes.heygen.com/catalog)

**[Browse the gallery →](https://justintse-cal.github.io/hyperframe-templates/)**

---

## What's here

| | Category | Templates |
| --- | --- | --- |
| **A** | Explaining a concept | A01–A04 |
| **B** | Data charts | B01–B05 |
| **C** | Workflow | C01–C08 |
| **D** | News highlight text | D01–D04 |
| **E** | Narrative & emphasis | E01–E14 |

Every template is exactly **8 seconds**, so they stack into a uniform grid. The
root reel in `index.html` plays all 35 back-to-back (280s total).

### Template catalog

[`docs/templates.md`](./docs/templates.md) is the **template catalog** — for every
template, one sentence on what it is and one on what it's used for, plus a short
note on the canvas, the design system and how to mount a template.

Paste it into an AI agent to give it a working knowledge of the library, or use
the **"Copy full catalog for AI"** button on the gallery site.

## Design system

All templates follow [`design.md`](./design.md) — read it before editing a frame.
The short version:

- **Canvas** — 1920×1080, `#root` on a warm gradient `#FFFCEF → #FDF3F8` (never white).
- **Palette** — ink `#121212`, gold `#8A6D00`, pink `#C2185B`, red `#C0392B`.
- **Type** — Playfair Display for display/section titles; Plus Jakarta Sans / Inter for body and UI.
- **Motion** — entrance-only, deterministic and seek-safe. No exit animations.
- **Safe area** — keep the bottom ~15% (below y≈920px) clear of content.
- **No corner text** — no badges, footers, or watermarks; a textless `.frame-border` is allowed.

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
  data-composition-id="A01-core-definition"
  data-composition-src="compositions/A01-core-definition.html"
  data-start="0"
  data-duration="8"
  data-track-index="1"
  data-width="1920"
  data-height="1080"
></div>
```

## Project structure

```
index.html               root reel — one slot per template, 8s each (280s)
compositions/            one sub-composition per template (A01 … E14)
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

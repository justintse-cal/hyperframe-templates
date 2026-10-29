# HyperFrames Composition Project

## Design system — FOLLOW IT FOR EVERY FRAME

**This project is a library of video templates, and it has a design system:
[`design.md`](./design.md).** Read it before writing or modifying any frame.
It defines the canvas, the background gradient, the primary and secondary
colors, media treatment, composition rules, the subtitle safe area, and
typography. If a request conflicts with `design.md`, follow `design.md` and
flag the conflict.

### The standard workflow for a new project

1. **Reference this template folder** — start from an existing composition in
   `compositions/` rather than authoring from a blank file.
2. **Reuse when a template fits.** Duplicate the closest template and adapt its
   content, keeping every rule in `design.md` (background, colors, no corner
   text, subtitle safe area, entrance-only motion).
3. **Author new animation only when no template fits.** A new frame must still
   obey the entire design system — same background, palette, typography, safe
   areas, and deterministic entrance-only motion.
4. Run `npm run check` after any change and fix all errors before finishing.

## Skills — USE THESE FIRST

**Always invoke the relevant skill before writing or modifying compositions.** Skills encode framework-specific patterns (e.g., `window.__timelines` registration, `data-*` attribute semantics, shader-compatible CSS rules) that are NOT in generic web docs. Skipping them produces broken compositions.

**Doing anything with HyperFrames?** Start at `/hyperframes` — it tells you what HyperFrames can do and which skill or workflow handles your intent (make a video, TTS / BGM, prep footage, author / animate, render, install blocks), confirms your brief up front (the intent layer), and routes every "make me a…" request (a video, a deck, a composition port) to the right workflow. Read it first, especially when there's no project context to orient you. The workflows it routes to:

- `/product-launch-video` — any **website** URL or brief / script → a product launch / SaaS / promo video, or a site tour / showcase featuring the site's own captured visuals.
- `/faceless-explainer` — arbitrary text (topic / article / notes), **no URL, no website capture** → 60-90s faceless explainer.
- `/embedded-captions` — an existing talking-head video (MP4) → the same footage with captions / subtitles added (rail + embed, or pure-cinematic embed); the footage itself is untouched.
- `/talking-head-recut` — an existing talking-head / interview / podcast video (MP4) → the same footage **packaged with designed graphic overlays** (kinetic titles, lower-thirds, data callouts, pull-quotes, side panels, pip) synced to the transcript; the clip plays unchanged underneath. (Plain captions/subtitles → `/embedded-captions`.)
- `/pr-to-video` — a GitHub PR (URL / `owner/repo#N` / "this PR") → 30-90s code-change explainer (changelog / feature reveal / fix / refactor).
- `/motion-graphics` — a short (typically under 10s) design-led **motion graphic**, motion-is-the-message, no narration: kinetic type, a stat / number count-up, a chart, a logo sting, a lower-third / overlay, or an animated tweet / headline / captured-page highlight; rendered to MP4 or a transparent overlay. Longer / narrated / custom → `/general-video`.
- `/music-to-video` — a **music track** (audio file, video to pull audio from, or one generated from a mood brief) → beat-synced video (lyric / slideshow / kinetic promo). Music drives pacing; user-supplied images / videos are cut onto the same beat grid.
- `/slideshow` — a **presentation / pitch deck / interactive deck** — discrete slides, fragment reveals, branching, hotspot navigation, presenter mode. Output is a navigable deck, not a rendered video.
- `/general-video` — fallback for any other video (title card, longer brand / sizzle reel, multi-scene montage, static loop, custom composition) and the home of **companion mode** — co-create with the full HyperFrames toolbox; the original hyperframes authoring flow, any length.

**Porting an existing composition?** `/remotion-to-hyperframes` translates a Remotion (React) composition into HyperFrames HTML — a source migration, separate from the creation workflows above.

The domain skills (`/hyperframes-core`, `/hyperframes-animation`, `/hyperframes-keyframes`, `/hyperframes-creative`, `/hyperframes-cli`, `/media-use`, `/hyperframes-audio`, `/hyperframes-registry`, `/figma`) and the full capability map live inside `/hyperframes` — it is the single source of truth for which skill handles which intent.

**Changing how real footage or images look or reveal?** Load `/media-use` and read its `references/media-treatments.md` before editing, even when the request only says dark, flat, boring, retro, private, or “make the reveal cooler.” It governs how footage is treated, never whether media may be used. Use canonical media treatments and seek-safe motion; do not improvise equivalent CSS/SVG filters or overlays.

> **Tailwind v4 projects** (`hyperframes init --tailwind`): see `/hyperframes-core` → `references/tailwind.md`.

> **Using a HyperFrames plugin?** Load skills from that installed bundle and follow
> its `hyperframes/references/plugin-installation.md` execution rules. Update via
> the plugin manager, not the standalone commands below.
>
> **Standalone skill missing or stale?** Run `npx hyperframes skills update <name>` to install/refresh
> the specific skill you need (the `/hyperframes` router does this automatically before
> entering a workflow), or bare `npx hyperframes skills update` to refresh the core set plus
> everything already installed — neither pulls the full set. Restart the agent session so
> newly installed skills load.

## Commands

```bash
npm run dev          # human-operated foreground preview (blocks until stopped)
npx hyperframes preview --background  # agent-safe persistent Studio preview
npx hyperframes preview --status      # verify the persistent preview is listening
npx hyperframes preview --stop        # stop it when review is finished
npm run check        # lint + runtime + layout + motion + contrast (one command)
npm run render       # render to MP4
npm run publish      # publish and get a shareable link
npx hyperframes lint --verbose  # include info-level findings
npx hyperframes lint --json     # machine-readable output for CI
npx hyperframes docs <topic> # reference docs in terminal
```

> **Agents must use `npx hyperframes preview --background` for Studio handoff.** Do not rely
> on a shell/tool `run_in_background` wrapper around `npm run dev`: that foreground process
> remains owned by the invoking session and can disappear while the browser stays open,
> leaving refreshes at `ERR_CONNECTION_TIMED_OUT`. Verify with `preview --status`, keep it
> alive through review, and stop it explicitly with `preview --stop` afterward.

> **Back from the desktop app.** Once this project was opened in the HyperFrames desktop app, run `npx hyperframes catch-up` before your next change here: it lists what the person asked Framey in the app and which files changed since.

> **Pinned CLI version.** These scripts pin an exact `hyperframes@X.Y.Z` so this project re-renders identically over time. Weeks later that pin lags fixes shipped since. To move up: `npx hyperframes@latest upgrade --project . --check` (shows the delta), then `npx hyperframes@latest upgrade --project .` to rewrite the pins. Always unpinned — the pinned script re-runs the old version against itself.

## Documentation

**For quick reference**, use the local CLI docs command (no network required):

```bash
npx hyperframes docs <topic>
```

Topics: `data-attributes`, `gsap`, `compositions`, `rendering`, `examples`, `troubleshooting`

**For full documentation**, discover pages via the machine-readable index — do NOT guess URLs:

```
https://hyperframes.heygen.com/llms.txt
```

## Project Structure

- `design.md` — **the design system** (colors, background, composition rules, subtitle safe area, typography). Read before editing any frame.
- `docs/templates.md` — **the template catalog**: one line on what each template is and one on what it's used for, plus the canvas, the design-system basics and how to mount a template. Read it before picking or duplicating a template; it is also what the gallery's "Copy full catalog for AI" button hands to an agent.
- `index.html` - main composition (root timeline): one slot per template, played back-to-back on `data-track-index="1"` (42 templates, each `data-duration="8"`, total `data-duration="336"`)
- `compositions/` — one sub-composition per template, named by slug (e.g. `core-definition.html`, `unit-chart.html`)
- `stock media/` — placeholder images and footage used by the templates; referenced from `compositions/` with the space URL-encoded as `../stock%20media/<file>`
- `meta.json` — project metadata (id, name)
- `transcript.json` — whisper word-level transcript (if generated)
- `docs/` — the static **GitHub Pages template showcase** (`docs/index.html` + `docs/templates.js` + committed `docs/videos/` previews). Vanilla HTML/CSS/JS, no build step; follows `design.md`. Enable via Settings → Pages → deploy from `main` /`docs`.
- `.hyperframes/artifacts/` — check reports, snapshots, contact sheets

## Template Conventions

### Slug-id scheme

Every template is identified by a stable **slug** (e.g. `barchart-growth`), used
consistently in four places:

1. **Filename**: `compositions/barchart-growth.html`
2. **`data-composition-id`**: `barchart-growth` (on the sub-composition's `#root` *and* on its slot in `index.html`)
3. **Timeline key**: `window.__timelines["barchart-growth"]`
4. **Slot id** in `index.html`: `id="barchart-growth"`

The slug is an identity, **not** a category. A template can move between groups
without renaming its file; grouping lives in `docs/templates.js` (`group`) and the
section headings of `docs/templates.md`.

There is no in-frame template label — corner text was removed (see `design.md`).

Groups, by the job a template does in an edit:

| Letter | Group | Templates |
| ------ | ----- | --------- |
| A | Openers & Statements | breaking-news · chapter-card · headline-stack · speech-statement |
| B | Explain & Summarize | core-definition · mechanism-walkthrough · problem-solution · news-summary · term-explanation |
| C | Compare & Contrast | paradigm-shift · split-tilt-cards · split-panels · split-screens |
| D | Process & Flow | milestone-timeline · decision-tree · feedback-loop · handdrawn-flowchart · progress-steps · flowchart |
| E | Structure & Systems | architecture-stack · network-node-map · radial-surround · grid-card-assemble · specs-list |
| F | Data & Numbers | metric-highlight · barchart-growth · linechart-trend · pie-donut-share · news-stat · chart-card · unit-chart · progress-stat |
| G | Social Proof & Audience | press-quote · yt-comment-stack · reddit-post-card · testimonial-card · yt-comment-scatter · subscribe-outro |
| H | Screens & Artifacts | terminal-editor · article-circle · typed-prompt · notes-typing |

### Format & palette

> **The full design system lives in [`design.md`](./design.md). Read it before
> modifying any frame — it governs canvas, background, color, media treatment,
> composition rules, the subtitle safe area, and typography.**

- **1920×1080** (`data-width="1920" data-height="1080"`).
- **Background**: always `#ffffff` on `#root` — never a gradient, never a tinted frame.
- **Text**: black `#000000` by default; one theme per template (Blue, Red, Green, Yellow, Orange) for highlights, rules, icons, charts. Theme accents are the only colored text.
- **Typography**: Noto Sans for all Latin text, Noto Sans TC for Traditional Chinese — see `design.md` §6.
- **No corner text.** Do not add header badges, category tags, "Use It For" chips, footer bars, sample labels, or brand wordmarks. A textless `.frame-border` is optional decoration.
- **Subtitle safe area**: keep the bottom ~15% (below y≈920px) clear of content.
- Each composition is a `<template>` wrapper containing `<style>` + `<div id="root">` + `<script>`, and registers exactly one paused timeline: `window.__timelines["<slug>"] = gsap.timeline({ paused: true });`
- **Entrance animations only** — no exit animations; scenes hold their final state until the clip ends.

### Stock media

- Placeholders live in `stock media/` (note the space → always URL-encode: `src="../stock%20media/ai_price.jpg"`)
- Give every image explicit `width`/`height` attributes so layout sampling stays deterministic.
- Videos need a stable `id`, `muted playsinline`, `class="clip"` plus `data-start`/`data-duration` — **without an `id` the renderer freezes the video**.

### Adding a slot / resequencing

1. Copy an existing slot block in `index.html`; set `id` (the slug), `data-composition-id`, `data-composition-src`, and `data-duration` (must match the sub-composition's `data-duration`).
2. Set `data-start` = previous slot's `data-start` + `data-duration` — slots are back-to-back with no gaps.
3. Inserting mid-timeline? Resequence `data-start` on **every** slot after the insertion point.
4. Bump the root `#root data-duration` to the last slot's `data-start` + `data-duration`.
5. Add the slot under the group comment (`<!-- Group A: Openers & Statements -->` … ) it belongs to, and add the template to `docs/templates.js` + `docs/templates.md`.
6. Run `npm run check`.

## Linting — ALWAYS RUN AFTER CHANGES

After creating or editing any `.html` composition, **always** run the full check before considering the task complete:

```bash
npm run check
```

Fix all errors before presenting the result. Warnings should be reviewed before rendering.

## Key Rules

1. Every timed element needs `data-start` and a duration. `data-start` is what marks it as timed; `data-track-index` is an optional Studio display lane the render never reads
2. Give timed visual elements `class="clip"`. The framework keys visibility off `data-start`, not the class, but the shared `.clip` CSS is what gives a scene its full-frame box, and `lint` warns without it
3. Register one paused root timeline per composition on `window.__timelines`:
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
   Scene timelines manually added to this root must not be paused. A paused
   child does not advance when the root is seeked. The runtime activates
   registered composition siblings, not arbitrary nested scene timelines.
4. A video with sound keeps it on the `<video>` (`data-has-audio="true"`, no `muted`). Use a separate `<audio>` for music, voiceover, replacement audio, J/L cuts, or audio detached in Studio. Silent footage and b-roll: `muted`.
5. Sub-compositions use `data-composition-src="compositions/file.html"` to reference other HTML files
6. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches

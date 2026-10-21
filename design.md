# Design System — HyperFrames Templates

The single source of truth for how every template in this project looks and is
composed. **Any agent or person modifying a frame must follow this file.** If a
request conflicts with this document, follow this document and say so.

`design.md` (this file) and `AGENTS.md` are complementary: `AGENTS.md` tells the
agent *what to do and how to work*; this file defines *how a frame must look*.

---

## 1. Canvas

- **1920 × 1080**, landscape, 16:9.
- Every composition declares `data-width="1920" data-height="1080"`.
- `#root` is `position: absolute; inset: 0;` with `overflow: hidden`.
- **No corner text.** Do not add header badges, category tags, "Use It For"
  chips, footer bars, sample labels, brand wordmarks, or any watermark-like
  text in the four corners. The corners stay clean so frames drop cleanly into
  a longer edit and carry no per-template branding.
- **Decorative frame, allowed.** A `.frame-border` (outer solid + inner dashed
  inset border) is permitted as a purely visual frame — it carries no text.
  It is optional; omit it when a full-bleed composition reads better without it.

---

## 2. Background

Every frame uses the project's warm editorial background, defined once and
reused:

```css
background: linear-gradient(135deg, #FFFCEF 0%, #FDF3F8 100%);
```

- This gradient is **the default background for all templates** — cream
  `#FFFCEF` top-left to soft blush `#FDF3F8` bottom-right.
- Never leave the background white (`#ffffff`). White is no longer a valid
  default; use the gradient above.
- **Full-bleed media templates** (background photo or video covering the frame)
  keep the gradient as their base layer; the media sits on top, dimmed per §4.
- Cards, chips, and text boxes that need a surface should reuse the same
  gradient, not a flat white.

---

## 3. Color

### Primary colors (the three core brand colors)

| Token | Hex | Role |
| ----- | --- | ---- |
| Ink | `#121212` | Primary text, axes, outlines |
| Gold | `#8A6D00` | Headings, primary titles, emphasis |
| Pink | `#C2185B` | Accent, category accents, key marks |

Red `#C0392B` remains available as a secondary emphasis accent for numbers,
calls to attention, and gradients.

### Secondary colors (new — extend the palette, never replace the primaries)

| Token | Hex | Role |
| ----- | --- | ---- |
| Sky | `#7fa8e9` | Cool secondary fills, supporting data series, calm accents |
| Teal | `#77a3b9` | Cool secondary fills, chart series, quiet UI |
| Mauve | `#bcabb3` | Neutral-warm secondary, muted backgrounds, de-emphasized marks |

**Rules for secondary colors**
- Secondary colors support the three primaries; they never become the dominant
  brand voice. Use them for supporting data series, secondary chart segments,
  background tints, and tertiary UI.
- Keep primary `#121212` for all body text so AA contrast holds.
- Available accent chips / highlighters: `#FFF3A8` and `#FFE34F` (yellow).
- Never place white text on white, or dark text on dark. Check contrast before
  finishing any frame.

### Contrast

- Body and heading text must pass **WCAG AA** against the background they sit on.
- On the cream/blush gradient, `#121212` text is the safe default.
- Over dimmed media (§4), use light text (the E02/E03 light-chrome pattern) and
  verify with `npm run check`.

---

## 4. Media treatment

- **Dim for legibility.** When footage or a screenshot sits behind text, dim it
  with a black overlay so text stays readable:
  `background: rgba(0, 0, 0, 0.5);`
- **Spotlight exception (highlight box).** When a frame highlights a region of
  a chart or screenshot, dim *outside* the highlighted region while keeping the
  content *inside* it at full brightness. Do this with an outward `box-shadow`
  on the highlight box (e.g. `box-shadow: 0 0 0 3000px rgba(0,0,0,0.45);`) or an
  equivalent non-destructive mask — never dim the highlighted content itself.
- **Highlighter.** Text highlighters use `#FFE34F` with
  `mix-blend-mode: multiply` so the text reads through the mark instead of
  being covered.
- Media placeholders live in `stock media/` (space in path → always URL-encode:
  `src="../stock%20media/ai_price.jpg"`).

---

## 5. Composition rules

- **One paused root timeline per composition**, registered exactly once:
  ```js
  window.__timelines = window.__timelines || {};
  window.__timelines["composition-id"] = gsap.timeline({ paused: true });
  ```
- **Entrance animations only.** No exit animations. A scene animates in and
  holds its final state until the clip ends.
- **Deterministic only.** No `Date.now()`, no `Math.random()`, no network
  fetches. All motion must be seek-safe and reproducible.
- **Timing attributes.** Every timed element needs `data-start` and a duration;
  give timed visual elements `class="clip"`.
- **Number count-ups** (statistics, growth figures) are running numbers: animate
  a proxy object inside the seekable timeline and write the value to the DOM in
  `onUpdate`. Never animate a number outside the timeline.
- **One timeline key per sub-composition** matching its `data-composition-id`.
- Sub-compositions mount from a parent via
  `data-composition-src="compositions/file.html"`.

### Safe area — subtitle clearance

**Leave the bottom of the frame clear for subtitles.**

- Reserve the **bottom ~15% of the frame (≈160px at 1080p)** as a subtitle safe
  band. Do not place text, key graphics, chart baselines, legends, or captions
  in this band.
- Content must finish above **y = 920px**. The bottom band from **y ≈ 920px to
  1080px** stays empty.
- Full-bleed media may extend into the band (it is background), but no readable
  content sits there.
- When a frame has no subtitles, still honor the safe band so the frame stays
  drop-in compatible with any video that adds them.

### Corner clearance

The four corners must remain free of text (§1). Content starts below the top
margin and ends above the subtitle safe band.

---

## 6. Typography

Two typefaces carry the system:

| Family | Usage |
| ------ | ----- |
| **Playfair Display** (serif) | Display headings, big titles, quote text, brand-adjacent emphasis |
| **Plus Jakarta Sans / Inter** (sans) | Body copy, labels, chart text, UI, numbers |

Import (already in every template):

```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,800;1,400&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
```

Fallback stack: `'Inter', sans-serif` for body; `'Playfair Display', serif` for
display.

### Scale (at 1920×1080)

| Role | Family | Size | Weight |
| ---- | ------ | ---- | ------ |
| Hero / display title | Playfair Display | 60–98px | 800 |
| Section / frame title | Playfair Display | 38–50px | 700–800 |
| Large quote | Playfair Display | 56–72px | 700 (italic allowed) |
| Emphasis number / stat | Playfair Display or sans | 48–120px | 800 |
| Body copy | Inter / Plus Jakarta | 24–30px | 400 |
| Label / UI / chart text | Inter / Plus Jakarta | 14–20px | 600–700 |
| Corner-free footnote / small | Inter | 13–16px | 400–600 |

- Headings: `letter-spacing: -0.02em` for large display text; labels use
  `letter-spacing: 0.1em` and `text-transform: uppercase`.
- Body line-height ≈ `1.4–1.5`; display line-height ≈ `1.1–1.3`.
- Increase sizes for emphasis, never below the body floor of ~24px for content
  text that must be read.

### CJK

Chinese text uses `'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei',
sans-serif`. Pair a Chinese term (display scale, raise-in per character) with a
smaller English term and a body-size definition (E07 pattern).

---

## 7. Template catalog

Templates are letter-indexed: **A** = explaining a concept, **B** = data charts,
**C** = workflow diagrams, **D** = news highlight text, **E** = narrative &
emphasis. See `AGENTS.md` for the full slot table and the workflow for
adding/resequencing slots.

---

## 8. When to use a template vs. build new

The workflow for a new project:

1. Start from the existing templates in `compositions/`.
2. If a template already fits the beat, duplicate it and adapt the content —
   keeping every rule in this file.
3. Only build a brand-new animation when **no** existing template fits. When you
   do, it must still obey this entire design system.

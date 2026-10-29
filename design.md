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

**All frames must use a white background.**

```css
background: #ffffff;
```

- **Background is always `#ffffff`** for every template and composition, regardless of theme.
- **Full-bleed media templates** (background photo or video covering the frame)
  keep `#ffffff` as their base layer; the media sits on top, dimmed per §4.
- Cards, chips, and text boxes that need a surface should use theme tints from their assigned palette (see §3), not introduce colored backgrounds for the frame itself.

---

## 3. Color

### Thematic monochromatic color system

Every template uses **exactly one theme**. The background is always white. 

**Primary text must remain black (`#000000`) by default.** Only use colored text for highlighted words, key terms, or titles when emphasis is needed — and always ensure WCAG AA contrast on white.

#### Available themes (one per template)

| Theme | Colors | Suggested usage |
| ----- | ------ | --------------- |
| **Blue** | `#2274a5`, `#c7dce8`, `#e8f1f7`, `#617682` | Primary accent `#2274a5` for highlights/titles/rules/icons/borders/charts. Tints `#c7dce8`/`#e8f1f7` for subtle fills. |
| **Red** | `#fa003f`, `#fc5c84`, `#f00699`, `#fe4a49` | Primary accent `#fa003f` for highlights/titles/rules/icons/borders/charts. Use others for accents/decorative elements. |
| **Green** | `#88d18a`, `#00513c`, `#007d55`, `#74c368` | Primary accent `#00513c` or `#007d55` for highlights/titles/rules/icons/borders/charts. Tints/accent `#88d18a`/`#74c368`. |
| **Yellow** | `#ffcf00`, `#ffa500`, `#ec8421` | Use `#ffa500` or `#ec8421` for colored text/highlights (ensure contrast). `#ffcf00` best for backgrounds/fills, not body text on white. |
| **Orange** | `#ee6123`, `#7b2d26`, `#f4a261`, `#f8dfa0` | Primary accent `#ee6123` for highlights/titles/rules/icons/borders/charts. Deep `#7b2d26` for strong emphasis if needed. Tints `#f4a261`/`#f8dfa0`. |

#### Rules

- **Background is always white.** No gradients on `#root` or the frame background.
- **One theme only.** Each template uses exactly one theme from the list above. No mixing of themes.
- **Text color:** Body text, labels, and most content must be `#000000` (black). **Only** highlighted words, key terms, or titles may be colored using the theme's accent color. Ensure any colored text meets WCAG AA contrast against white.
- **Accents & highlights:** Use the single theme's colors for rules, borders, icons, callouts, chart series, decorative elements, and colored text/highlights. Prefer tints for subtle fills/surfaces.
- **Contrast:** Never place white text on white, or low-contrast text on white. Verify contrast before finishing. Over dimmed media (§4), use light text and verify with `npm run check`.

### Legacy notes
The previous cream/blush gradient and gold/pink palette are replaced by this thematic monochromatic system with white background.

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

**One family carries the system: Noto Sans.** Hierarchy comes from size, weight,
and spacing — never from mixing typefaces. `Noto Sans TC` is the Traditional
Chinese companion of the same family, so mixed-script frames read as one voice.

| Family | Usage |
| ------ | ----- |
| **Noto Sans** | All Latin text — display headings, big titles, quote text, body copy, labels, chart text, UI, numbers |
| **Noto Sans TC** | All Traditional Chinese text, paired with Noto Sans in the same frame |

Import (required in every composition):

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap');
```

Fallback stack: `"Noto Sans", "PingFang TC", "Microsoft JhengHei", sans-serif`.

Both faces are variable fonts: always set `font-optical-sizing: auto` and drive
weight through `font-weight`. The utility class name carries the weight, and the
declaration must repeat that same number — replace both `<uniquifier>` and
`<weight>` (e.g. `.noto-sans-800 { … font-weight: 800; }`,
`.noto-sans-tc-500 { … font-weight: 500; }`):

```css
.noto-sans-<uniquifier> {
  font-family: "Noto Sans", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
  font-variation-settings:
    "wdth" 100;
}

.noto-sans-tc-<uniquifier> {
  font-family: "Noto Sans TC", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
}
```

For italic Latin text use the same class with `font-style: italic` (the import
includes the italic axis). CJK text has no italic — emphasise it with weight or
the theme accent instead.

> **Migration note.** The shipped templates in `compositions/` still import
> Playfair Display + Plus Jakarta Sans (and `C05` also uses Caveat). They predate
> this rule and must be migrated to Noto Sans before they are reused. Any new or
> edited frame follows the Noto Sans rule above.

### Scale (at 1920×1080)

| Role | Family | Size | Weight |
| ---- | ------ | ---- | ------ |
| Hero / display title | Noto Sans | 60–98px | 800 |
| Section / frame title | Noto Sans | 38–50px | 700–800 |
| Large quote | Noto Sans | 56–72px | 700 (italic optional) |
| Emphasis number / stat | Noto Sans | 48–120px | 800 |
| Body copy | Noto Sans | 24–30px | 400 |
| Label / UI / chart text | Noto Sans | 14–20px | 600–700 |
| Corner-free footnote / small | Noto Sans | 13–16px | 400–600 |

- Headings: `letter-spacing: -0.02em` for large display text; labels use
  `letter-spacing: 0.1em` and `text-transform: uppercase`.
- Body line-height ≈ `1.4–1.5`; display line-height ≈ `1.1–1.3`.
- Increase sizes for emphasis, never below the body floor of ~24px for content
  text that must be read.

### CJK

Chinese text uses `'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei',
sans-serif` via a `.noto-sans-tc-<weight>` class — the same family voice as the
Latin text, so a mixed-script frame stays visually unified. Pair a Chinese term
(display scale, raise-in per character) with a smaller English term and a
body-size definition (E07 pattern).

### Icons & symbols

Use **Google Material Symbols** for icons and symbols when a frame needs one
(arrows, checks, warnings, chart/UI glyphs, status marks):

```
https://fonts.google.com/icons
```

- **Import the variable icon font** (already deterministic — fonts are fetched
  and cached at compile time, so this stays seek-safe):
  ```css
  @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap');
  ```
- Render an icon as a ligature inside a span; the font name carries the style:
  ```html
  <span class="material-symbols-outlined">trending_up</span>
  ```
  ```css
  .material-symbols-outlined {
    font-family: 'Material Symbols Outlined';
    font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 48;
    font-size: 40px;
    line-height: 1;
  }
  ```
- **Colour icons with the palette** (§3) — ink `#121212` by default, gold
  `#8A6D00` or pink `#C2185B` for emphasis. Never introduce an off-palette
  icon colour.
- Size icons to the type they sit beside (roughly the label or body size) and
  keep them inside the subtitle safe band (§5).
- **Prefer Material Symbols over hand-drawn SVG glyphs** for standard symbols;
  reserve inline SVG for genuinely bespoke marks (hand-drawn arrows, logo
  shapes) already used by existing templates.
- Icons are decoration, not content: give them `aria-hidden="true"` when a
  nearby text label already names the thing.

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

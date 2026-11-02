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
- **Never crop images.** Every image — screenshots, photos, stock placeholders,
  avatars and logos (including channel avatars inside end-card / subscribe
  pills) — must be shown in full. Size the placeholder frame to the media's
  native aspect ratio and use `object-fit: contain`; never use
  `object-fit: cover`, circular masks (`border-radius: 50%` on media), or any
  overflow/clipping to force media into a differently-shaped box. Where a
  headline row needs a visual anchor, use vector icons (e.g. Google Material
  Symbols) instead of cropped screenshots.
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

### Stage, edge padding & vertical rhythm

All frames share one content stage. These are hard values, not suggestions.

| Token | Value |
| ----- | ----- |
| Content gutter (left/right) | **96px** |
| Stage top | **84px** |
| Stage bottom | **160px** (content floor at y = 920) |
| Content stage size | **1728 × 836px** |
| Title block ends | **y = 200px** |
| Content starts | **y = 200px** |
| Content ends | **y = 920px** |
| Frame border inset | **32px**, 1px accent at 18% opacity |
| Blueprint grid | **96 × 96px**, accent at 7% opacity |
| Caption gutter | **130px** |
| Caption max-width | **1640px** |
| Caption bottom offset | **44px** |

```css
.stage {
  position: absolute;
  left: 96px;
  right: 96px;
  top: 84px;
  bottom: 160px;
}
```

**Vertical rhythm** — fixed steps, not per-scene guesses:

| Step | Value |
| ---- | ----- |
| Label → title | **16px** |
| Title → content | **48px** |
| Content → bottom note | **32px** |
| Bottom note baseline | **y ≈ 900px** |
| Note → caption band | never crosses **920px** |

The title block finishes by y = 200px. Primary content starts at y = 200px. A
bottom note belongs at the stage bottom (y ≈ 900px), never inside the caption
band.

### Column & alignment rules

**Single column: center it.**

- Use `text-align: center`, `align-items: center`, and
  `justify-content: center`.
- Center the text block, not just the text inside a full-width box.
- Statement line max-width: **1400px**.
- Body paragraph max-width: **1200px**.
- Never left-align a single editorial column.

**Artifact exception.** Terminal, code, article, notes, and UI-mockup frames may
left-align their internal content because they simulate a real interface. The
stage, 96px gutter, and 920px floor still apply.

**Two columns.**

- Split **48 / 52**, divider at **x = 960px**, **1px** accent at 28% opacity.
- Column gutter: **96px**.
- Each column is internally centered.
- Minimum text-bearing column: **672px**.
- Never mix a centered column with a left-aligned column in one row.

**Three or more columns.**

- Column width: **560px**, gap: **24px**.
- Content centered in each cell.
- Use only for parallel items (roles, steps, tools), never prose.

### Component spacing & defaults

| Component | Value |
| --------- | ----- |
| Card / panel padding | **24px 32px** |
| Card border | **1px**, accent at 34% opacity |
| Card top rule | **5px** accent |
| Card radius | **0** editorial / **12px** artifact |
| Chip / pill padding | **16px 24px** |
| Chip border | **2px** accent |
| Row / list item height | **96px** |
| Row rule | **1px** |
| Stack gap | **24px** |
| Accent rule | **4px × 120px** |
| Divider | **1px** |

- Cards and panels use white or theme tints, never a colored frame background.
- Prefer a top rule or left bar over a drop shadow.

### Corner clearance

The four corners must remain free of text (§1). Content starts below the top
margin and ends above the subtitle safe band.

### Caption tempo

**All scenes in a project read at one uniform caption pace.** Per-scene
variation is the main cause of a video feeling inconsistent; pick the pace
once and derive every scene's duration from it.

- **Pick one reference pace per project** — anchor it on one hand-tuned scene
  (e.g. the opener), then freeze that anchor: later retimes must never
  regenerate the reference scene's captions without re-deriving the pace.
- **Weight characters by visual length**: CJK chars count 1, ASCII chars/Latin
  digits count 0.55. Reading pace = visual length ÷ caption seconds.
  (≈6 visual chars/s is comfortable for zh-Hant narration at 720p-in-frame
  caption sizes; adjust per project, but use the same value everywhere.)
- **Per caption group:** `duration = round3(vlen(text) / pace)`.
- **Per scene window:**
  `duration = ceil-to-grid( Σ group durations + gap × (groups − 1) + 1.0 )`,
  with a fixed 1.0s = 0.25s lead-in + 0.45s tail + 0.3s breathing room and
  `gap ≈ 0.12s` between groups. Keep scene durations on a common grid (0.075s
  multiples) so slot timings stay frame-aligned.
- **Scene starts** are the running sum of durations; the project's timing
  manifest (e.g. `scenes.json`) is the single source of truth — slot timings
  in `index.html` and the caption track must be generated from it and must
  tile every scene window with no gaps or overlaps (validate with the
  caption build's `--check`).
- **Scale motion with captions.** Every scene's entrance beats must scale by
  the same factor as its captions so visuals stay on their narration lines:
  a scene's timeline is stretched so `fit × tempo-stretch = newDur / oldDur`
  (typical shape: a fit block mapping the authored timeline into
  `newDur / K`, followed by a uniform `K` post-build stretch, e.g. K = 1.35
  for 26% slower motion).
- Scenes may be *shorter* than the pace implies only when they carry more
  dead air than the formula needs — cut dead air, never caption seconds.

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
> Playfair Display + Plus Jakarta Sans (and `handdrawn-flowchart` also uses Caveat). They predate
> this rule and must be migrated to Noto Sans before they are reused. Any new or
> edited frame follows the Noto Sans rule above.

### Scale (at 1920×1080)

**One hard ladder.** Scenes pick a step; they do not invent sizes. Any size
outside this table is a documented addendum exception.

| Role | Size | Weight | Line-height | Tracking |
| ---- | ---- | ------ | ----------- | -------- |
| Hero / display | **96px** | 900 | 1.06 | +0.02em CJK / −0.02em Latin |
| Section title | **72px** | 900 | 1.10 | +0.01em |
| Pull quote | **64px** | 700 | 1.20 | +0.01em |
| Sub-section title | **56px** | 800 | 1.12 | +0.01em |
| Scene title (dense / artifact) | **46px** | 800 | 1.15 | +0.01em |
| Large body / lead-in | **34px** | 500 | 1.40 | +0.01em |
| Body | **30px** | 500 | 1.45 | +0.01em |
| Body small | **26px** | 500 | 1.45 | +0.01em |
| Secondary note | **22px** | 600 | 1.40 | +0.01em |
| Label / eyebrow / UI | **18px** | 700 | 1.20 | **0.20em**, uppercase |
| Footnote | **16px** | 500 | 1.35 | +0.01em |
| Micro / chart tick | **14px** | 700 | 1.20 | **0.16em**, uppercase |
| Subtitle / caption | **40px** | 600 | 1.32 | +0.01em |

- **CJK display** uses positive tracking (+0.01–0.02em) and line-height
  1.12–1.20. CJK has no italic; emphasise with weight or the theme accent.
- **Latin display** may use −0.02em tracking.
- Only labels and micro-text use uppercase + wide tracking.
- Never use a size between steps to make a line fit. Choose the next step down
  and rebalance the layout.

### Subtitle / caption type

**Every subtitle is exactly 40px.** There is no project-level caption size
variation.

| Property | Value |
| -------- | ----- |
| Size | **40px** |
| Weight | **600** |
| Line-height | **1.32** |
| Letter-spacing | **0.01em** |
| Colour | **#000000** |
| Alignment | **centered** |
| Max width | **1640px** |
| Bottom offset | **44px** |
| Lines | **1–2** |
| Background | **none** |
| Card / fill / border / shadow | **none** |
| Karaoke highlight | **none** |

- Captions live in one separate bottom track, never inside a scene
  composition.
- The caption band owns **y = 920–1080**. Scene content ends at **y = 920**.
- The caption gutter is wider than the content gutter: **130px**, or a
  **1640px** max-width.
- Use `text-wrap: balance`; keep each line to one clause and never exceed two
  lines.
- Pick the caption pace once per project (see “Caption tempo”) and freeze it;
  the 40px size is already fixed.

> **Legacy note.** Existing frames that use a different caption size predate
> this rule. New and edited frames use 40px; migrate legacy caption tracks
> before reusing them.

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

### Design tokens (copy into every composition)

```css
:root {
  /* Layout */
  --gutter: 96px;
  --stage-top: 84px;
  --stage-bottom: 160px;
  --content-floor: 920px;
  --frame-inset: 32px;
  --caption-gutter: 130px;
  --caption-max: 1640px;
  --caption-bottom: 44px;

  /* Type ladder */
  --type-hero: 96px;
  --type-title: 72px;
  --type-quote: 64px;
  --type-subtitle: 56px;
  --type-scene: 46px;
  --type-body-lg: 34px;
  --type-body: 30px;
  --type-body-sm: 26px;
  --type-note: 22px;
  --type-label: 18px;
  --type-footnote: 16px;
  --type-micro: 14px;
  --type-caption: 40px;

  /* Components */
  --card-pad-y: 24px;
  --card-pad-x: 32px;
  --stack-gap: 24px;
  --rule-thickness: 4px;
  --rule-width: 120px;
}
```

These tokens are the contract. A frame that needs a different value is a
documented addendum exception, not a local override.

---

## 7. Template catalog

42 templates, each identified by a **stable slug** (`core-definition`,
`barchart-growth`, …). The slug is identity only — a template can move between
groups without being renamed.

Templates are grouped by **the job each one does in an edit**, not by the medium
it imitates:

| Letter | Group |
| ------ | ----- |
| **A** | Openers & Statements |
| **B** | Explain & Summarize |
| **C** | Compare & Contrast |
| **D** | Process & Flow |
| **E** | Structure & Systems |
| **F** | Data & Numbers |
| **G** | Social Proof & Audience |
| **H** | Screens & Artifacts |

The full table of which template sits in which group lives in `AGENTS.md`; the
catalog with one line per template is `docs/templates.md`. Read either before
picking or duplicating a template.

---

## 8. When to use a template vs. build new

The workflow for a new project:

1. Start from the existing templates in `compositions/`.
2. If a template already fits the beat, duplicate it and adapt the content —
   keeping every rule in this file.
3. Only build a brand-new animation when **no** existing template fits. When you
   do, it must still obey this entire design system.

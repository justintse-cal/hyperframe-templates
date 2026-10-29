# HyperFrames Editorial Templates

42 drop-in video templates, grouped by the job each one does in an edit —
openers, explainers, comparisons, process flows, systems, data, proof and
artifacts. Each one is 8 seconds, 1920×1080, silent, and built on the design
system in `design.md`.

Paste this file into an AI agent to tell it what the library contains.

## The short version

- **42 templates** — A openers & statements (4) · B explain & summarize (5) · C compare & contrast (4) · D process & flow (6) · E structure & systems (5) · F data & numbers (8) · G social proof & audience (6) · H screens & artifacts (4).
- **File** `compositions/<id>.html`. **Mount** it with `data-composition-src="compositions/<file>.html"` plus a `data-start` and `data-duration`, and register one paused timeline: `window.__timelines["<id>"] = gsap.timeline({ paused: true });`
- **Every frame** uses a white background (`#ffffff`), black text by default, one theme per template (Blue/Red/Green/Yellow/Orange), entrance-only motion, no content below y=920, and no corner text.
- **To adapt one**, edit the copy in the file (or its `CONFIG` block where it has one) and keep the design system intact.
- **To check your work**, run `npm run check`.

## How the groups are chosen

A template belongs to the group named by **the job its frame does in the edit**,
not by the medium it imitates. If two groups seem to fit, pick the one whose
layout a viewer would name first. Template ids are stable slugs — the group a
template sits in can change without renaming its file.

## A — Openers & Statements

**A01 · Breaking News** (`breaking-news`)
A red alert chip, a headline that slams in word by word, and a scrolling ticker.
Use it for: urgency beats — patches, outages, breaking announcements.

**A02 · Chapter Card** (`chapter-card`)
Dimmed footage behind a chapter number and a title whose characters rise in.
Use it for: section openers and chapter markers in a long-form piece.

**A03 · Headline Stack** (`headline-stack`)
Four news-headline screenshots slam in at scattered angles.
Use it for: media roundups and "what everyone is talking about" stacks.

**A04 · Speech Statement** (`speech-statement`)
An inset, dimmed portrait sits on a cream mat behind a long audio waveform, a light-type news bar and phrase-by-phrase captions.
Use it for: soundbites, interviews, testimonials and keynote pulls.

## B — Explain & Summarize

**B01 · Core Definition** (`core-definition`)
Defines a key concept with a large term, a one-line definition and three supporting pillars.
Use it for: the opening beat of an explainer.

**B02 · Mechanism Walkthrough** (`mechanism-walkthrough`)
Explains how something works as three numbered steps linked by connector bars.
Use it for: process breakdowns, feature walkthroughs and "how it works" sections.

**B03 · Problem → Solution** (`problem-solution`)
Puts a painful problem on screen first, then swaps it for the resolution.
Use it for: sales and marketing beats that lead with the pain before the fix.

**B04 · News Summary** (`news-summary`)
A headline over three check-marked bullet cards that slide in one by one.
Use it for: release notes, launch recaps and changelog summaries.

**B05 · Term Explanation** (`term-explanation`)
A Chinese term raises in character by character, an underline draws, then the English term and definition.
Use it for: translating or introducing a key term in another language.

## C — Compare & Contrast

**C01 · Paradigm Shift** (`paradigm-shift`)
Shows an old way and a new way side by side, then lands on a final wordmark.
Use it for: before/after comparisons such as legacy stack vs. modern stack.

**C02 · Split Tilt Cards** (`split-tilt-cards`)
Two 3D-tilted cards swing in from opposite sides with version badges, then float in place.
Use it for: before/after comparisons of screens, plans or products.

**C03 · Split Panels** (`split-panels`)
Two equal panels slide in from opposite edges to meet at the centre, then a gradient divider fades in between them.
Use it for: side-by-side comparisons, dual perspectives and before/after reveals.

**C04 · Split Screens** (`split-screens`)
Three image columns rise in one by one, each with a numeral, a title and a caption.
Use it for: side-by-side comparisons of products, topics or capabilities.

## D — Process & Flow

**D01 · Milestone Timeline** (`milestone-timeline`)
Extends a gradient rail through a row of dated milestone cards.
Use it for: roadmaps, launch phases and project timelines.

**D02 · Decision Tree** (`decision-tree`)
A root condition branches into three labelled outcomes, one marked as the recommended path.
Use it for: triage rules, routing logic and playbooks.

**D03 · Feedback Loop** (`feedback-loop`)
Three labelled stages sit on a dashed ring that turns once at the end.
Use it for: cyclical processes such as build/measure/learn or plan/do/review.

**D04 · Hand-Drawn Flowchart** (`handdrawn-flowchart`)
Wobbly sketch boxes and arrows draw themselves on, with labels fading in as each box lands.
Use it for: informal process sketches and whiteboard-style tutorials.

**D05 · Progress Steps** (`progress-steps`)
Four numbered rings fill in sequence along a connecting rail, each one pulsing as it activates.
Use it for: process timelines, project phases and onboarding progress.

**D06 · Flowchart** (`flowchart`)
A yes/no question opens into a three-level decision tree, with connectors drawing in as each bubble lands on its branch.
Use it for: decision paths, qualification questions and "which option should I pick" explainers.

## E — Structure & Systems

**E01 · Architecture Stack** (`architecture-stack`)
Three labelled layers stack upward, bottom to top.
Use it for: tech stacks, layered systems and tier diagrams.

**E02 · Network Node Map** (`network-node-map`)
A central hub links out to four peripheral nodes as the connecting lines draw.
Use it for: ecosystems, supply chains, org charts and hub-and-spoke relationships.

**E03 · Radial Surround** (`radial-surround`)
Labelled chips assemble on a ring around a centre subject, then converge inward.
Use it for: feature clusters and "everything in one place" overviews.

**E04 · Grid Card Assemble** (`grid-card-assemble`)
A grid of icon cards rises into place, each icon landing as its card arrives.
Use it for: feature grids and short "how it works" summaries.

**E05 · Specs List** (`specs-list`)
Label/value spec rows slide in one at a time, each underlined by a thin accent sweep.
Use it for: design-system specs, product attributes and "what's inside" rundowns.

## F — Data & Numbers

**F01 · Metric Highlight** (`metric-highlight`)
Spotlights a single KPI as one huge number with a context line and a source.
Use it for: the one number that matters — growth rate, lift, savings.

**F02 · Bar Chart Growth** (`barchart-growth`)
Grows three bars from a baseline with their values and labels, highlighting the tallest.
Use it for: comparing categories, channels or periods by volume.

**F03 · Line Chart Trend** (`linechart-trend`)
Draws a gradient line across a dated axis and drops a marker on the peak with a callout.
Use it for: trends over time — MAU growth, retention, cost decline.

**F04 · Pie / Donut Share** (`pie-donut-share`)
Fills a donut segment by segment with a matching legend row.
Use it for: splits — budget allocation, market share, traffic sources.

**F05 · News Stat** (`news-stat`)
One big number counts up under a cited source line, with a sentence beneath it.
Use it for: survey findings and impact statistics you want sourced.

**F06 · Chart Card** (`chart-card`)
A chart screenshot swings in from a 3D angle, then a gold box spotlights one region with a callout.
Use it for: pointing at the one part of a chart worth looking at.

**F07 · Unit Chart** (`unit-chart`)
A hundred dots light up to reach a share, then the grid packs them into filled and empty cells.
Use it for: "x out of every hundred" stats — adoption, survey results, market share.

**F08 · Progress Stat** (`progress-stat`)
A headline number counts up while a thin accent track fills to the same proportion.
Use it for: goals reached, quota progress and any "x out of y" milestone.

## G — Social Proof & Audience

**G01 · Press Quote** (`press-quote`)
A large italic pull quote with pink quotation marks and a named attribution.
Use it for: customer quotes, press coverage and executive soundbites.

**G02 · YouTube Comment Card** (`yt-comment-stack`)
YouTube-style comment cards stack up, each typing on after its avatar pops.
Use it for: creator reactions and audience social proof.

**G03 · Reddit Post** (`reddit-post-card`)
A Reddit post card settles in, the upvote arrow presses and the count ticks up in brand pink.
Use it for: community proof points and social traction.

**G04 · Testimonial Card** (`testimonial-card`)
A quote card reveals line by line, then a hand-drawn underline sweeps under the key phrase.
Use it for: customer testimonials and social proof cards.

**G05 · YouTube Comment Scatter** (`yt-comment-scatter`)
Six comment cards pop across the frame one after another, each fully formed.
Use it for: a wall of audience reaction and comment montages.

**G06 · Subscribe Outro** (`subscribe-outro`)
A centred channel pill with an avatar, name, Subscribe, Like and Share actions, plus a cursor that demonstrates each button.
Use it for: end cards, subscribe reminders and channel sign-offs.

## H — Screens & Artifacts

**H01 · Terminal Editor** (`terminal-editor`)
A dark editor window with traffic lights, a filename and syntax-highlighted code.
Use it for: developer-facing beats that need to show code.

**H02 · Article Circle** (`article-circle`)
An article screenshot rises and scales while a yellow highlighter sweeps across one sentence.
Use it for: quoting a specific line out of an article.

**H03 · Typed Prompt** (`typed-prompt`)
A single prompt line types itself in behind a blinking caret.
Use it for: showing the prompt you used to get a result.

**H04 · Notes Typing** (`notes-typing`)
A notes-app page types a title and body lines on a human keystroke rhythm with a moving caret.
Use it for: personal, diary-style storytelling beats.

---

This is deliberately a light reference. For the full design system read `design.md`; for the exact on-screen copy, motion timings and config fields, open the composition file itself.

Adding a template? Update this file and `docs/templates.js`.

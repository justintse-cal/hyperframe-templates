# HyperFrames Editorial Templates

36 drop-in video templates for concept explainers, data charts, workflow diagrams, news highlights and narrative beats. Each one is 8 seconds, 1920×1080, silent, and built on the warm editorial design system in `design.md`.

Paste this file into an AI agent to tell it what the library contains.

## The short version

- **36 templates** — A concept (4) · B data charts (5) · C workflow (8) · D news text (4) · E narrative (15).
- **File** `compositions/<id>.html`. **Mount** it with `data-composition-src="compositions/<file>.html"` plus a `data-start` and `data-duration`, and register one paused timeline: `window.__timelines["<id>"] = gsap.timeline({ paused: true });`
- **Every frame** uses the warm gradient background `#FFFCEF → #FDF3F8`, ink `#121212` / gold `#8A6D00` / pink `#C2185B`, entrance-only motion, no content below y=920, and no corner text.
- **To adapt one**, edit the copy in the file (or its `CONFIG` block where it has one) and keep the design system intact.
- **To check your work**, run `npm run check`.

## A — Explaining a concept

**A01 · Core Definition** (`A01-core-definition`)
Defines a key concept with a large term, a one-line definition and three supporting pillars.
Use it for: the opening beat of an explainer.

**A02 · Paradigm Shift** (`A02-paradigm-shift`)
Shows an old way and a new way side by side, then lands on a final wordmark.
Use it for: before/after comparisons such as legacy stack vs. modern stack.

**A03 · Mechanism Walkthrough** (`A03-mechanism-walkthrough`)
Explains how something works as three numbered steps linked by connector bars.
Use it for: process breakdowns, feature walkthroughs and "how it works" sections.

**A04 · Problem → Solution** (`A04-problem-solution`)
Puts a painful problem on screen first, then swaps it for the resolution.
Use it for: sales and marketing beats that lead with the pain before the fix.

## B — Data charts

**B01 · Metric Highlight** (`B01-metric-highlight`)
Spotlights a single KPI as one huge number with a context line and a source.
Use it for: the one number that matters — growth rate, lift, savings.

**B02 · Bar Chart Growth** (`B02-barchart-growth`)
Grows three bars from a baseline with their values and labels, highlighting the tallest.
Use it for: comparing categories, channels or periods by volume.

**B03 · Line Chart Trend** (`B03-linechart-trend`)
Draws a gradient line across a dated axis and drops a marker on the peak with a callout.
Use it for: trends over time — MAU growth, retention, cost decline.

**B04 · Pie / Donut Share** (`B04-pie-donut-share`)
Fills a donut segment by segment with a matching legend row.
Use it for: splits — budget allocation, market share, traffic sources.

**B05 · Milestone Timeline** (`B05-milestone-timeline`)
Extends a gradient rail through a row of dated milestone cards.
Use it for: roadmaps, launch phases and project timelines.

## C — Workflow diagrams

**C01 · Decision Tree** (`C01-decision-tree`)
A root condition branches into three labelled outcomes, one marked as the recommended path.
Use it for: triage rules, routing logic and playbooks.

**C02 · Feedback Loop** (`C02-feedback-loop`)
Three labelled stages sit on a dashed ring that turns once at the end.
Use it for: cyclical processes such as build/measure/learn or plan/do/review.

**C03 · Architecture Stack** (`C03-architecture-stack`)
Three labelled layers stack upward, bottom to top.
Use it for: tech stacks, layered systems and tier diagrams.

**C04 · Network Node Map** (`C04-network-node-map`)
A central hub links out to four peripheral nodes as the connecting lines draw.
Use it for: ecosystems, supply chains, org charts and hub-and-spoke relationships.

**C05 · Hand-Drawn Flowchart** (`C05-handdrawn-flowchart`)
Wobbly sketch boxes and arrows draw themselves on, with labels fading in as each box lands.
Use it for: informal process sketches and whiteboard-style tutorials.

**C06 · Radial Surround** (`C06-radial-surround`)
Labelled chips assemble on a ring around a centre subject, then converge inward.
Use it for: feature clusters and "everything in one place" overviews.

**C07 · Split Tilt Cards** (`C07-split-tilt-cards`)
Two 3D-tilted cards swing in from opposite sides with version badges, then float in place.
Use it for: before/after comparisons of screens, plans or products.

**C08 · Grid Card Assemble** (`C08-grid-card-assemble`)
A grid of icon cards rises into place, each icon landing as its card arrives.
Use it for: feature grids and short "how it works" summaries.

## D — News highlight text

**D01 · Breaking News** (`D01-breaking-news`)
A red alert chip, a headline that slams in word by word, and a scrolling ticker.
Use it for: urgency beats — patches, outages, breaking announcements.

**D02 · Press Quote** (`D02-press-quote`)
A large italic pull quote with pink quotation marks and a named attribution.
Use it for: customer quotes, press coverage and executive soundbites.

**D03 · News Summary** (`D03-news-summary`)
A headline over three check-marked bullet cards that slide in one by one.
Use it for: release notes, launch recaps and changelog summaries.

**D04 · News Stat** (`D04-news-stat`)
One big number counts up under a cited source line, with a sentence beneath it.
Use it for: survey findings and impact statistics you want sourced.

## E — Narrative & emphasis

**E01 · Chart Card** (`E01-chart-card`)
A chart screenshot swings in from a 3D angle, then a gold box spotlights one region with a callout.
Use it for: pointing at the one part of a chart worth looking at.

**E02 · Chapter Card** (`E02-chapter-card`)
Dimmed footage behind a chapter number and a title whose characters rise in.
Use it for: section openers and chapter markers in a long-form piece.

**E03 · Split Screens** (`E03-split-screens`)
Three image columns rise in one by one, each with a numeral, a title and a caption.
Use it for: side-by-side comparisons of products, topics or capabilities.

**E04 · Terminal Editor** (`E04-terminal-editor`)
A dark editor window with traffic lights, a filename and syntax-highlighted code.
Use it for: developer-facing beats that need to show code.

**E05 · Unit Chart** (`E05-unit-chart`)
A hundred dots light up to reach a share, then the grid packs them into filled and empty cells.
Use it for: "x out of every hundred" stats — adoption, survey results, market share.

**E06 · Headline Stack** (`E06-headline-stack`)
Four news-headline screenshots slam in at scattered angles.
Use it for: media roundups and "what everyone is talking about" stacks.

**E07 · Term Explanation** (`E07-term-explanation`)
A Chinese term raises in character by character, an underline draws, then the English term and definition.
Use it for: translating or introducing a key term in another language.

**E08 · Article Circle** (`E08-article-circle`)
An article screenshot rises and scales while a yellow highlighter sweeps across one sentence.
Use it for: quoting a specific line out of an article.

**E09 · YouTube Comment Card** (`E09-yt-comment-card`)
YouTube-style comment cards stack up, each typing on after its avatar pops.
Use it for: creator reactions and audience social proof.

**E10 · Reddit Post** (`E10-reddit-post`)
A Reddit post card settles in, the upvote arrow presses and the count ticks up in brand pink.
Use it for: community proof points and social traction.

**E11 · Testimonial Card** (`E11-testimonial-card`)
A quote card reveals line by line, then a hand-drawn underline sweeps under the key phrase.
Use it for: customer testimonials and social proof cards.

**E12 · Typed Prompt** (`E12-typed-prompt`)
A single prompt line types itself in behind a blinking caret.
Use it for: showing the prompt you used to get a result.

**E13 · Notes Typing** (`E13-notes-typing`)
A notes-app page types a title and body lines on a human keystroke rhythm with a moving caret.
Use it for: personal, diary-style storytelling beats.

**E14 · YouTube Comment Scatter** (`E14-yt-comment-scatter`)
Six comment cards pop across the frame one after another, each fully formed.
Use it for: a wall of audience reaction and comment montages.

**E15 · Subscribe Outro** (`E15-subscribe-outro`)
A centred channel pill with an avatar, name, Subscribe, Like and Share actions, plus a cursor that demonstrates each button.
Use it for: end cards, subscribe reminders and channel sign-offs.

---

This is deliberately a light reference. For the full design system read `design.md`; for the exact on-screen copy, motion timings and config fields, open the composition file itself.

Adding a template? Update this file and `docs/templates.js`.

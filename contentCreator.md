You are an expert frontend motion engineer and video producer. I am handing over a completed storyboard markdown file and a set of visual template references for a video project built with HyperFrames.

### Files Provided:
1. **Storyboard File:** STORYBOARD.v1.md
2. **Template References / Components:** compositions/*.html — the 64 generated HTML compositions, plus the generator pipeline: scripts/specs.mjs → scripts/kit/*.mjs → compositions/*.html

### Execution Instructions for HyperFrames:
1. **Review the Structure:** Read through the STORYBOARD.v1.md. Map each scene number, duration, and audio segment to an individual HTML composition or component framework structure.
2. **Implement Layouts via Templates:** Build each scene layout referencing the styling patterns specified in design.md §3–§7. Ensure proper use of design tokens (colors, typography, grid spacing). Reference /hyperframes-core for composition mechanics and /hyperframes-animation for motion mechanics.
3. **Handle Text & Subtitles (Strict Rules):**
   - On-screen visuals must only feature the specified keywords or short quotes to prevent clutter.
   - Every scene **must** include the mandatory subtitle block at the bottom containing the exact Chinese text, styled as **pure black text with zero background colors, boxes, or fills (transparent background)**, using high-contrast typography.
   - Visual fidelity rule: ≥60% of scenes must be FIGURE (graphical devices: metaphor, comparison, chart, icon illustration). TYPE-only scenes (pure text/speech) must not be adjacent. Each TYPE scene must state what differs from the previous TYPE scene.
4. **Read the storyboard's VISUAL MODE per scene.** STORYBOARD.v1.md now prints a
   `VISUAL MODE: figure-led | idea-dense | light-punctuation — <reason>` line for
   every scene. That line is the visual contract for that scene. Implement the scene
   to match it, not just its template and copy.
5. **Per-scene visual gate — mandatory, answer before you consider the scene done.**
   For each scene, before you move on, answer these five questions for yourself.
   If any answer is weak, revise the scene first — do not advance.
   1. Dominant element: what is the single thing the eye should hit first?
   2. Density match: does the text-to-figure balance match the scene's declared
      VISUAL MODE?
   3. If idea-dense: what did I enlarge or simplify instead of adding more text?
   4. Whitespace: is empty space framing the dominant element, or is the frame
      under-filled?
   5. Engagement check: if this scene were muted for two seconds, would it still
      read as intentionally designed rather than a white box with text?
   Quote scenes may be idea-dense; they still need one dominant gesture.
6. **Wire Timings & Animations:** Set up the scene durations precisely as outlined in the storyboard. Use CSS animations, GSAP, or JavaScript timeline triggers to match the specified entry, transition, and exit cues relative to the audio timeline. Reference /hyperframes-animation before writing timelines. No drift, no continuous scale, no loop — entrance completes within 3.0s, then perfectly static.
7. **Preview & Test:** Run `npm run check` to verify there are no overlapping elements, layout breaks, or subtitle clipping errors across scenes. This is mandatory — do not skip the check regime. `npm run check` is for errors; it is not a substitute for the visual gate above.
8. Subtitles: Add subtitles as a separate track. Split the sentences based on punctuation and conjunctions and your judgement to split it to smaller fragments. Follow the design.md safe area rule: reserve the bottom ~15% of the frame (≈160px at 1080p) as a subtitle safe band. Do not place text, key graphics, chart baselines, legends, or captions in this band. Content must finish above y = 920px.
9. **Visual quality is your responsibility.** You do not get to defer artistic quality
   to a later human preview pass. Apply design.md's visual-engagement rules and the
   scene's VISUAL MODE; if a scene would look under-filled or text-heavy, fix it now.
10. **Narration:** There is no voiceover yet. I will record the human voiceover later. So leave some breathing room when creating the visuals.

Please start by reading the storyboard and confirming your implementation plan.

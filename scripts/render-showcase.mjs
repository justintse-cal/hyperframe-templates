/**
 * Build the GitHub Pages showcase previews in docs/.
 *
 * Pipeline:
 *   1. Render the full reel (index.html, all 25 slots) once with hyperframes
 *      → renders/reel-1080p.mp4  (skipped when the reel already exists; pass --render to force)
 *   2. Slice the reel at each slot's data-start/data-duration from index.html,
 *      downscale to 1280x720 H.264, strip audio → docs/videos/<id>.mp4
 *   3. Extract a poster from the settled final state → docs/posters/<id>.jpg
 *
 * Usage:  node scripts/render-showcase.mjs [--render]
 * Requires: npx hyperframes, ffmpeg on PATH.
 */

import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const reel = join(root, 'renders', 'reel-1080p.mp4');
const videosDir = join(root, 'docs', 'videos');
const postersDir = join(root, 'docs', 'posters');

// --- 1. Parse slot timings from index.html -------------------------------

const indexHtml = readFileSync(join(root, 'index.html'), 'utf8');
const slotRe =
  /data-composition-id="([A-E]\d{2}-[^"]+)"[\s\S]*?data-start="([\d.]+)"[\s\S]*?data-duration="([\d.]+)"/g;
const slots = [];
for (let m; (m = slotRe.exec(indexHtml)); ) {
  slots.push({ id: m[1], start: parseFloat(m[2]), duration: parseFloat(m[3]) });
}
if (slots.length === 0) {
  console.error('No template slots found in index.html');
  process.exit(1);
}
console.log(`Found ${slots.length} template slots in index.html`);

// --- 2. Render the reel if needed -----------------------------------------

if (process.argv.includes('--render') || !existsSync(reel)) {
  console.log('Rendering full reel with hyperframes (draft quality)...');
  const r = spawnSync(
    'npx',
    ['--yes', 'hyperframes@0.8.171', 'render', '--quality', 'draft', '-o', 'renders/reel-1080p.mp4'],
    { cwd: root, stdio: 'inherit', shell: true },
  );
  if (r.status !== 0) {
    console.error('Reel render failed');
    process.exit(r.status ?? 1);
  }
} else {
  console.log(`Reusing existing reel: ${reel}`);
}

mkdirSync(videosDir, { recursive: true });
mkdirSync(postersDir, { recursive: true });

// --- 3. Slice + downscale each template, extract poster -------------------

function ffmpeg(args, label) {
  const r = spawnSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', ...args], {
    cwd: root,
    stdio: ['ignore', 'inherit', 'inherit'],
  });
  if (r.status !== 0) {
    console.error(`ffmpeg failed for ${label}`);
    process.exit(r.status ?? 1);
  }
}

for (const slot of slots) {
  const out = join('docs', 'videos', `${slot.id}.mp4`);
  const poster = join('docs', 'posters', `${slot.id}.jpg`);

  // Slice, downscale, re-encode for the web (no audio; templates are silent).
  ffmpeg(
    [
      '-ss', String(slot.start),
      '-i', reel,
      '-t', String(slot.duration),
      '-vf', 'scale=1280:720:flags=lanczos',
      '-c:v', 'libx264',
      '-preset', 'medium',
      '-crf', '24',
      '-pix_fmt', 'yuv420p',
      '-an',
      '-movflags', '+faststart',
      out,
    ],
    slot.id,
  );

  // Poster from the settled final state (~0.5s before the clip ends).
  const posterAt = Math.max(0, slot.duration - 0.5);
  ffmpeg(
    ['-ss', String(posterAt), '-i', out, '-frames:v', '1', '-q:v', '3', poster],
    `${slot.id} poster`,
  );

  console.log(`  ✓ ${slot.id} (${slot.duration}s)`);
}

console.log(`\nDone: ${slots.length} previews in docs/videos + posters in docs/posters`);

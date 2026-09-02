#!/usr/bin/env node
// Generates the homepage pictures listed in homepage-images.json through the
// NanoGPT API, crops each one to its slot ratio and writes WebP files.
//
// Usage: node generate-homepage-images.mjs [--only name,name] [--force]
// Needs: NANOGPT_API_KEY in the environment (falls back to the nanogpt MCP
// entry in ~/.claude.json) and ImageMagick (`magick`) on the PATH.

import { readFileSync, existsSync, mkdirSync, writeFileSync, unlinkSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { homedir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const manifest = JSON.parse(readFileSync(join(root, 'homepage-images.json'), 'utf8'));
const args = process.argv.slice(2);
const force = args.includes('--force');
const only = args.includes('--only') ? args[args.indexOf('--only') + 1].split(',') : null;

const apiKey = process.env.NANOGPT_API_KEY ?? (() => {
    try {
        return JSON.parse(readFileSync(`${homedir()}/.claude.json`, 'utf8')).mcpServers.nanogpt.env.NANOGPT_API_KEY;
    } catch {
        return undefined;
    }
})();
if (!apiKey) {
    console.error('NANOGPT_API_KEY is not set');
    process.exit(1);
}

const outDir = join(root, manifest.output_dir);
mkdirSync(outDir, { recursive: true });

const ratioOf = (r) => r.split(':').map(Number).reduce((a, b) => a / b);

async function generate(image) {
    const target = join(outDir, `${image.file}.webp`);
    if (existsSync(target) && !force) {
        console.log(`skip ${image.file} (exists)`);
        return;
    }
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 600000);
    const started = Date.now();
    const response = await fetch('https://nano-gpt.com/v1/images/generations', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${apiKey}` },
        body: JSON.stringify({
            model: manifest.model,
            prompt: `${image.prompt} ${manifest.style}`,
            n: 1,
            size: image.size,
            response_format: 'url',
        }),
        signal: controller.signal,
    }).finally(() => clearTimeout(timer));
    if (!response.ok) {
        throw new Error(`${image.file}: HTTP ${response.status} ${(await response.text()).slice(0, 300)}`);
    }
    const data = await response.json();
    const item = data.data?.[0] ?? {};
    let bytes;
    if (item.url) {
        bytes = Buffer.from(await (await fetch(item.url)).arrayBuffer());
    } else if (item.b64_json) {
        bytes = Buffer.from(item.b64_json, 'base64');
    } else {
        throw new Error(`${image.file}: no image in response ${JSON.stringify(data).slice(0, 300)}`);
    }
    const raw = join(outDir, `${image.file}.raw.png`);
    writeFileSync(raw, bytes);

    const [w, h] = image.size.split('x').map(Number);
    const want = ratioOf(image.ratio);
    let crop = `${w}x${h}`;
    if (Math.abs(w / h - want) > 0.01) {
        crop = w / h > want ? `${Math.round(h * want)}x${h}` : `${w}x${Math.round(w / want)}`;
    }
    execFileSync('magick', [raw, '-gravity', 'center', '-crop', `${crop}+0+0`, '+repage', '-quality', '88', target]);
    unlinkSync(raw);
    console.log(`done ${image.file} ${crop} in ${Math.round((Date.now() - started) / 1000)}s`);
}

const queue = manifest.images.filter((i) => !only || only.includes(i.file));
const concurrency = 3;
let failures = 0;
await Promise.all(Array.from({ length: concurrency }, async () => {
    while (queue.length) {
        const image = queue.shift();
        try {
            await generate(image);
        } catch (e) {
            failures++;
            console.error(`FAIL ${e.message}`);
        }
    }
}));
process.exit(failures ? 1 : 0);

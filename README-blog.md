# R&D Nordic — Blog publishing

This folder documents how blog posts get from the studio
(`RD-Nordic-Publications`) onto the live site (`RDNordic`, GitHub Pages).

The site has **no build step and no framework**. Posts are plain static HTML
+ the shared `style.css`, exactly like every other page. `build_post.py` is an
*authoring helper* you run in the studio; its output is a finished `.html`
file you review and commit like anything else. Nothing runs on the server.

---

## TL;DR

```bash
# from the site repo root (RDNordic/)
python tools/build_post.py \
  ../RD-Nordic-Publications/.../<slug>.en.md \
  ../RD-Nordic-Publications/.../<slug>.no.md

python -m http.server 8000      # preview at http://localhost:8000/blog/
# review, then commit + push (push to main auto-deploys)
```

Example Markdown files can live in the studio repo next to the authored post
drafts. Keep transfer bundles and scratch examples out of this website repo
unless they are intentionally being published.

---

## Why a script, not hand-authoring

You asked which to use. **Recommendation: the script.** Reasons:

- **Header/footer stay in sync.** The duplicated nav/footer chrome is the most
  fragile part of a no-templating site. The script holds it in *one* place
  (`STRINGS` in `build_post.py`). Hand-authoring means editing it in every post
  forever, and it *will* drift.
- **Bilingual parity is enforced structurally.** Same script, same layout, both
  languages — you only write prose, never markup.
- **Editorial standard is baked in.** Byline, real-name author, date, reading
  time and tags come from front matter, so a post can't ship without them.
- **It stays plain.** Output is the same CSP-safe static HTML you'd write by
  hand — no JS, no dependencies, no lock-in. If you ever drop the script, the
  generated files keep working untouched.

The one cost is a small Python file to maintain. Given the sync risk on a
duplicated-chrome site, that trade is worth it.

---

## Authoring a post

One Markdown file per language: `<slug>.en.md` and `<slug>.no.md`.
Each starts with a TOML front-matter block fenced by `+++`:

```toml
+++
title        = "AI governance you can actually ship"
slug         = "ai-governance-readiness-checklist"   # same slug both languages
lang         = "en"                                  # en | no
eyebrow      = "Governance"
date         = "2026-06-23"                           # ISO; localised on render
tags         = ["EU AI Act", "GDPR", "Governance"]
description  = "Meta description for <head>."
lede         = "Standfirst shown under the title."
reading_time = 6                                      # optional; auto-estimated
author       = "Andrew Davidson"                      # real name (editorial std)
author_bio   = "... <a href=\"/index.html#about\">More &rarr;</a>"
+++

Body in Markdown here.
```

### Supported Markdown

| Syntax | Renders as |
|---|---|
| `## Heading` / `### Heading` | section headings (H2 gets the teal accent rule) |
| blank-line-separated text | `<p>` |
| `**bold**`, `*italic*` / `_italic_`, `` `code` `` | inline formatting |
| `[text](/url)` | link |
| `- item` | bullet list |
| `- [] item` | **checklist** (teal-tick list) — use when *every* item is a check |
| `> line` | blockquote |
| `::: callout "Label"` … `:::` | highlighted callout box (label optional) |

Keep it to that subset — posts should read cleanly as plain text in the studio.

### Output location (derived from front matter)

| `lang` | written to |
|---|---|
| `en` | `blog/<slug>.html` |
| `no` | `no/blog/<slug>.html` |

---

## After rendering

1. Add the post to **both** index pages — `blog/index.html` and
   `no/blog/index.html` — as a `.post-card` (or promote it to the
   `.blog-featured` lead). The indexes are hand-maintained on purpose: ordering
   and the featured pick are editorial calls.
2. `python -m http.server 8000`, check EN + NO, desktop + mobile, and the EN/NO
   language switch.
3. Commit and push. **Pushing to `main` auto-deploys to the public site** — only
   push once you're happy.

---

## House rules (non-negotiable)

- No external dependencies — no CDNs, fonts, icons, JS libs, or analytics.
- Full EN ↔ NO parity; Norwegian in natural Bokmål.
- Single shared `style.css`; no framework, no server-side templating.
- Posts publish under the real author name: Andrew Davidson / R&D Nordic.

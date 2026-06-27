#!/usr/bin/env python3
"""
build_post.py  —  R&D Nordic blog renderer
============================================

Converts a studio Markdown post (with TOML front matter) into a static,
CSP-safe HTML page that matches the site's blog template, then writes it
to the correct place in the site tree (`blog/` for English, `no/blog/`
for Bokmål).

WHY THIS EXISTS
---------------
The site itself has *no* build step: it ships plain static HTML + one
shared style.css, exactly as before. This script is an **authoring tool**
that runs in the studio (RD-Nordic-Publications), not on the live site.
Its only output is a finished .html file that you review and commit like
any other page. The header/footer chrome lives here as templates, so the
two-language duplication can never drift out of sync — change it once,
re-render, done.

DEPENDENCIES
------------
Python 3.11+ standard library only (uses `tomllib`). No pip installs,
no network, nothing to vendor.

USAGE
-----
    python build_post.py studio/blog/<slug>.en.md
    python build_post.py studio/blog/<slug>.no.md

    # render both language files of a post in one go:
    python build_post.py studio/blog/<slug>.en.md studio/blog/<slug>.no.md

    # override where files land (defaults to repo root inferred from CWD):
    python build_post.py <file.md> --site-root /path/to/RDNordic

The output path is derived from front matter: `lang` (en|no) + `slug`.
    en  ->  <site-root>/blog/<slug>.html
    no  ->  <site-root>/no/blog/<slug>.html

FRONT MATTER (TOML, fenced by +++)
----------------------------------
    +++
    title        = "AI governance you can actually ship"
    slug         = "ai-governance-readiness-checklist"
    lang         = "en"                 # en | no
    eyebrow      = "Governance"
    date         = "2026-06-23"         # ISO; rendered per-language
    tags         = ["EU AI Act", "GDPR", "Governance"]
    description   = "Meta description for <head>."
    lede         = "One-paragraph standfirst shown under the title."
    reading_time = 6                     # optional; auto-estimated if omitted
    author       = "Andrew Davidson"     # editorial standard: real name
    author_bio   = "R&D advisor and ... <a href=\\"/index.html#about\\">More &rarr;</a>"
    +++

    Body in Markdown follows here.

SUPPORTED MARKDOWN
------------------
    ## Heading 2            ### Heading 3
    Paragraphs separated by a blank line
    **bold**   *italic* / _italic_   `inline code`   [text](url)
    - bullet list item
    - [] checklist item            (renders the teal-tick list)
    > blockquote (one or more consecutive lines)
    ::: callout "Optional label"
    callout body (markdown inline)
    :::

Anything fancier than that is intentionally unsupported — keep posts
plain and readable in the studio.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import tomllib
from pathlib import Path

# --------------------------------------------------------------------------
# Per-language chrome. This is the single source of truth for the blog
# header/footer — edit here, re-render, and both languages stay in sync.
# --------------------------------------------------------------------------

CSP = (
    "default-src 'self'; script-src 'self'; style-src 'self'; "
    "img-src 'self' data:; font-src 'self'; connect-src 'none'; "
    "object-src 'none'; base-uri 'self'; form-action 'self'"
)

STRINGS = {
    "en": {
        "home_root": "/index.html",
        "blog_root": "/blog/",
        "services_menu": "/services/ai-services-menu.html",
        "nav": [("#hero", "Home"), ("#services", "What We Do"), ("#why-us", "Why Us")],
        "nav_blog": "Blog",
        "nav_cases": ("#cases", "Cases"),
        "nav_contact": ("#contact", "Contact"),
        "nav_aiservices": "AI Services",
        "back": "All posts",
        "share_label": "Found this useful?",
        "share_email": "Share by email",
        "share_talk": "Talk to us",
        "share_body": "Thought you might find this useful: ",
        "talk_subject": "Governance readiness review",
        "by": "R&D Nordic",
        "read": "min read",
        "tagline": "Professional consulting company with sharp, cross-disciplinary expertise in AI, privacy, and research delivery.",
        "place": "Hamar, Norway",
        "f_company": "Company",
        "f_team": "Team",
        "f_blog": "Blog",
        "f_resources": "Resources",
        "f_faq": ("/faq.html", "FAQ"),
        "f_menu": ("/services/ai-services-menu.html", "AI Services Menu"),
        "f_review": ("/services/ai-product-vibe-code-review.html", "AI Product & Vibe-Code Review"),
        "f_contact": ("/index.html#contact", "Contact"),
        "f_email": "Email Us",
        "f_privacy": ("/privacy.html", "Privacy Policy"),
        "copyright": "All rights reserved.",
        "months": ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"],
    },
    "no": {
        "home_root": "/no/index.html",
        "blog_root": "/no/blog/",
        "services_menu": "/no/services/ai-services-menu.html",
        "nav": [("#hero", "Hjem"), ("#services", "Hva vi gjør"), ("#why-us", "Hvorfor oss")],
        "nav_blog": "Blogg",
        "nav_cases": ("#cases", "Kundecase"),
        "nav_contact": ("#contact", "Kontakt"),
        "nav_aiservices": "AI-tjenester",
        "back": "Alle innlegg",
        "share_label": "Nyttig?",
        "share_email": "Del på e-post",
        "share_talk": "Ta kontakt",
        "share_body": "Tenkte du kunne ha nytte av denne: ",
        "talk_subject": "Gjennomgang av styringsberedskap",
        "by": "R&D Nordic",
        "read": "min lesing",
        "tagline": "Profesjonelt konsulentselskap med skarp, tverrfaglig kompetanse innen AI, personvern og forskningsleveranser.",
        "place": "Hamar, Norge",
        "f_company": "Selskap",
        "f_team": "Team",
        "f_blog": "Blogg",
        "f_resources": "Ressurser",
        "f_faq": ("/no/faq.html", "FAQ"),
        "f_menu": ("/no/services/ai-services-menu.html", "AI-tjenestemeny"),
        "f_review": ("/no/services/ai-product-vibe-code-review.html", "Gjennomgang av AI-produkter"),
        "f_contact": ("/no/index.html#contact", "Kontakt"),
        "f_email": "Send e-post",
        "f_privacy": ("/no/privacy.html", "Personvernerklæring"),
        "copyright": "Alle rettigheter forbeholdt.",
        "months": ["januar", "februar", "mars", "april", "mai", "juni",
                   "juli", "august", "september", "oktober", "november", "desember"],
    },
}


def fmt_date(iso: str, lang: str) -> str:
    """2026-06-23 -> 'June 23, 2026' (en) / '23. juni 2026' (no)."""
    try:
        y, m, d = (int(x) for x in iso.split("-"))
    except ValueError:
        return iso
    month = STRINGS[lang]["months"][m - 1]
    return f"{month} {d}, {y}" if lang == "en" else f"{d}. {month} {y}"


# --------------------------------------------------------------------------
# Tiny Markdown -> HTML renderer (only the subset documented above).
# --------------------------------------------------------------------------

_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_ITAL = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)|_([^_]+)_")
_CODE = re.compile(r"`([^`]+)`")


def _esc(text: str) -> str:
    """Escape bare & < > but leave existing &entities; intact."""
    text = re.sub(r"&(?!#?\w+;)", "&amp;", text)
    return text.replace("<", "&lt;").replace(">", "&gt;")


def inline(text: str) -> str:
    """Render inline markdown. Code spans are protected from other rules."""
    spans: list[str] = []

    def stash(m: re.Match) -> str:
        spans.append(f"<code>{_esc(m.group(1))}</code>")
        return f"\x00{len(spans) - 1}\x00"

    text = _CODE.sub(stash, text)
    text = _esc(text)
    text = _LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', text)
    text = _BOLD.sub(lambda m: f"<strong>{m.group(1)}</strong>", text)
    text = _ITAL.sub(lambda m: f"<em>{m.group(1) or m.group(2)}</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)
    return text


def md_to_html(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i, n = 0, len(lines)

    def flush_para(buf: list[str]) -> None:
        if buf:
            out.append(f"<p>{inline(' '.join(buf).strip())}</p>")
            buf.clear()

    para: list[str] = []
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # blank line -> paragraph break
        if not stripped:
            flush_para(para)
            i += 1
            continue

        # callout block  ::: callout "Label"
        m = re.match(r":::\s*callout(?:\s+\"([^\"]*)\")?\s*$", stripped)
        if m:
            flush_para(para)
            label = m.group(1)
            body: list[str] = []
            i += 1
            while i < n and lines[i].strip() != ":::":
                body.append(lines[i])
                i += 1
            i += 1  # skip closing :::
            block = md_to_html("\n".join(body))
            label_html = f'<p class="callout-label">{inline(label)}</p>' if label else ""
            out.append(f'<div class="post-callout">{label_html}{block}</div>')
            continue

        # headings
        if stripped.startswith("### "):
            flush_para(para)
            out.append(f"<h3>{inline(stripped[4:])}</h3>")
            i += 1
            continue
        if stripped.startswith("## "):
            flush_para(para)
            out.append(f"<h2>{inline(stripped[3:])}</h2>")
            i += 1
            continue

        # blockquote (consecutive >)
        if stripped.startswith(">"):
            flush_para(para)
            quote: list[str] = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
            continue

        # lists (checklist if every item is '- [] ')
        if re.match(r"-\s+", stripped):
            flush_para(para)
            items: list[str] = []
            checklist = True
            while i < n and re.match(r"-\s+", lines[i].strip()):
                item = re.sub(r"^-\s+", "", lines[i].strip())
                cm = re.match(r"\[\s*\]\s+(.*)", item)
                if cm:
                    items.append(cm.group(1))
                else:
                    checklist = False
                    items.append(item)
                i += 1
            cls = ' class="post-checklist"' if checklist else ""
            lis = "".join(f"<li>{inline(x)}</li>" for x in items)
            out.append(f"<ul{cls}>{lis}</ul>")
            continue

        # default: paragraph text
        para.append(stripped)
        i += 1

    flush_para(para)
    return "\n                ".join(out)


# --------------------------------------------------------------------------
# Page assembly
# --------------------------------------------------------------------------

def render_page(meta: dict, body_md: str) -> str:
    lang = meta["lang"]
    s = STRINGS[lang]
    slug = meta["slug"]
    other = "no" if lang == "en" else "en"

    en_url = f"https://rdnordic.com/blog/{slug}.html"
    no_url = f"https://rdnordic.com/no/blog/{slug}.html"
    self_url = en_url if lang == "en" else no_url

    # relative asset prefix (blog/ is one level deep, no/blog/ is two)
    asset = "../" if lang == "en" else "../../"

    # reading time
    words = len(re.findall(r"\w+", body_md))
    rt = meta.get("reading_time") or max(1, round(words / 200))

    # nav items
    nav_items = "".join(
        f'\n                <li><a href="{s["home_root"]}{href}">{label}</a></li>'
        for href, label in s["nav"]
    )
    aiservices = f'\n                <li><a href="{s["services_menu"]}">{s["nav_aiservices"]}</a></li>'
    blog_li = f'\n                <li><a href="{s["blog_root"]}">{s["nav_blog"]}</a></li>'
    cases_li = f'\n                <li><a href="{s["home_root"]}{s["nav_cases"][0]}">{s["nav_cases"][1]}</a></li>'
    contact_li = f'\n                <li><a href="{s["home_root"]}{s["nav_contact"][0]}">{s["nav_contact"][1]}</a></li>'
    nav = nav_items + aiservices + blog_li + cases_li + contact_li

    lang_switch = (
        f'<a href="/blog/{slug}.html"'
        + (' aria-current="page" class="font-semibold"' if lang == "en" else "")
        + ">EN</a>"
        + '\n                <span class="mx-1">|</span>\n                '
        + f'<a href="/no/blog/{slug}.html"'
        + (' aria-current="page" class="font-semibold"' if lang == "no" else "")
        + ">NO</a>"
    )

    tags = "".join(f'\n                <span class="post-tag">{html.escape(t)}</span>'
                   for t in meta.get("tags", []))

    body_html = md_to_html(body_md)
    date_human = fmt_date(meta["date"], lang)

    # mailto share (URL-encoded body)
    from urllib.parse import quote
    share_subject = quote(meta["title"])
    share_body = quote(s["share_body"] + self_url)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(meta["title"])} | R&amp;D Nordic</title>
    <meta name="description" content="{html.escape(meta["description"])}">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='0.9em' font-size='90'>🔬</text></svg>">
    <meta http-equiv="Content-Security-Policy" content="{CSP}">
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <meta http-equiv="Permissions-Policy" content="accelerometer=(), autoplay=(), camera=(), display-capture=(), geolocation=(), gyroscope=(), microphone=(), payment=(), usb=()">
    <link rel="stylesheet" href="{asset}style.css">
    <link rel="alternate" hreflang="en" href="{en_url}">
    <link rel="alternate" hreflang="no" href="{no_url}">
    <link rel="alternate" hreflang="x-default" href="{en_url}">
</head>
<body>
    <header class="site-header">
        <nav class="navbar container">
            <a class="logo" href="{s['home_root']}#hero">R&amp;D Nordic</a>
            <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
            <ul class="nav-links">{nav}
            </ul>
            <span class="ml-4 text-sm">
                {lang_switch}
            </span>
        </nav>
    </header>

    <main class="container py-8 blog-post">
        <a class="post-back" href="{s['blog_root']}">&larr; {s['back']}</a>

        <article>
            <p class="post-eyebrow">{html.escape(meta['eyebrow'])}</p>
            <h1>{html.escape(meta['title'])}</h1>
            <p class="post-lede">{inline(meta['lede'])}</p>

            <div class="post-byline">
                <img src="{asset}images/Headshot-color.png" alt="{html.escape(meta['author'])}">
                <div>
                    <div class="byline-name">{html.escape(meta['author'])}</div>
                    <div class="byline-meta">{s['by']} &middot; {date_human} &middot; {rt} {s['read']}</div>
                </div>
            </div>

            <div class="post-body">
                {body_html}
            </div>

            <div class="post-share">
                <span class="share-label">{s['share_label']}</span>
                <a href="mailto:?subject={share_subject}&amp;body={share_body}">{s['share_email']}</a>
                <a href="mailto:contact@rdnordic.com?subject={quote(s['talk_subject'])}">{s['share_talk']}</a>
            </div>

            <div class="post-tags">{tags}
            </div>

            <aside class="post-author">
                <img src="{asset}images/Headshot-color.png" alt="{html.escape(meta['author'])}">
                <div>
                    <p class="author-name">{html.escape(meta['author'])}</p>
                    <p class="author-bio">{meta['author_bio']}</p>
                </div>
            </aside>
        </article>
    </main>

    <footer class="site-footer">
        <div class="container footer-layout">
            <div class="footer-brand">
                <img src="{asset}images/rndnordiclogo.png" alt="R&amp;D Nordic logo" class="footer-logo">
                <p class="footer-tagline">{s['tagline']}</p>
                <p class="footer-legal-line">DAVIDSON NORDIC R&amp;D</p>
                <p class="footer-legal-line">Org.nr 927 071 444</p>
                <p class="footer-legal-line">{s['place']}</p>
                <p><a href="mailto:contact@rdnordic.com">contact@rdnordic.com</a></p>
            </div>
            <div class="footer-links-group">
                <h3>{s['f_company']}</h3>
                <ul>
                    <li><a href="{s['home_root']}#about">{s['f_team']}</a></li>
                    <li><a href="{s['blog_root']}">{s['f_blog']}</a></li>
                </ul>
            </div>
            <div class="footer-links-group">
                <h3>{s['f_resources']}</h3>
                <ul>
                    <li><a href="{s['f_faq'][0]}">{s['f_faq'][1]}</a></li>
                    <li><a href="{s['f_menu'][0]}">{s['f_menu'][1]}</a></li>
                    <li><a href="{s['f_review'][0]}">{s['f_review'][1]}</a></li>
                    <li><a href="{s['f_contact'][0]}">{s['f_contact'][1]}</a></li>
                    <li><a href="mailto:contact@rdnordic.com">{s['f_email']}</a></li>
                    <li><a href="{s['f_privacy'][0]}">{s['f_privacy'][1]}</a></li>
                </ul>
            </div>
        </div>
        <p class="footer-copyright">&copy; 2026 R&amp;D Nordic. {s['copyright']}</p>
    </footer>
<script src="{asset}site.js" defer></script>
</body>
</html>
"""


def parse_md(path: Path) -> tuple[dict, str]:
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"\+\+\+\s*\n(.*?)\n\+\+\+\s*\n(.*)$", raw, re.DOTALL)
    if not m:
        sys.exit(f"ERROR: {path} is missing a +++ TOML front matter block.")
    meta = tomllib.loads(m.group(1))
    required = ["title", "slug", "lang", "eyebrow", "date",
                "description", "lede", "author", "author_bio"]
    missing = [k for k in required if k not in meta]
    if missing:
        sys.exit(f"ERROR: {path} front matter missing: {', '.join(missing)}")
    if meta["lang"] not in ("en", "no"):
        sys.exit(f"ERROR: {path} lang must be 'en' or 'no'.")
    return meta, m.group(2)


def out_path(site_root: Path, meta: dict) -> Path:
    sub = "blog" if meta["lang"] == "en" else "no/blog"
    return site_root / sub / f"{meta['slug']}.html"


def main() -> None:
    ap = argparse.ArgumentParser(description="Render a studio Markdown post to site HTML.")
    ap.add_argument("files", nargs="+", help="One or more <slug>.<lang>.md files.")
    ap.add_argument("--site-root", default=".", help="Path to the RDNordic site repo root.")
    args = ap.parse_args()
    site_root = Path(args.site_root).resolve()

    for f in args.files:
        src = Path(f)
        meta, body = parse_md(src)
        dest = out_path(site_root, meta)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render_page(meta, body), encoding="utf-8")
        print(f"  {src}  ->  {dest.relative_to(site_root)}")


if __name__ == "__main__":
    main()

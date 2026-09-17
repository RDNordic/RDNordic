# What's up, my name is Andrew.

I'm a Norwegian / Scottish guy based in Norway. I recon I spend an unreasonable amount of time messing around with AI, privacy, ethics, IPR etc, but the thing that really gets my goat, is that whilst privacy is recognized as a fundamental human right (Article 12 of the Universal Declaration of Human Rights, Article 17 of the International Covenant on Civil and Political Rights), is is, for the most part, NOT.. in principle or practice.. I run a small company, **R&D Nordic**, and work at a Norwegian University as an R&D advisor. Outside of my public sector work, I am interesting in studying privacy behaviour, both from a consumer and an organisational perspective.

The sort of stuff I'm interested in:

* building useful AI systems and workflows - a process that changes every 5 minutes..
* figuring out how AI actually changes the way people work, from a behavioural analysis perspective.
* GDPR, privacy and responsible AI, an absolute governance nightmare..
* local and privacy-friendly AI setups; who doesn't love offline.
* agents, retrieval, automation and coding workflows; feed it context and you shall receive.
* research, grants and overambitious project ideas; the bigger and crazier the better.
* behavioural science and why perfectly sensible policies achieve absolutely nothing; in fact I kind of hate strategy documents and policies but we do sort of need them, right?

In any case. I care more about **what actually works** than what an organisation says it does. I like organisational behavioural management and performance management, which gives you the tools to operationalise, measure and improve behaviour.

## Things I like building

I use GitHub partly for work and partly as a workshop.

You will find things involving:

* AI agents and agentic workflows
* Claude, Codex and other AI-assisted development tools; (lord forgive me but someone has to figure out how to use this stuff sensibly)
* RAG, search and retrieval experiments
* privacy and security tools; I like to review other peoples work and (humbly) suggest privacy improvements
* local models and self-hosted setups; I have decent hardware for local stuff but not excellent, got some good friends I collab with on this stuff tho.
* GDPR / AI governance reviews
* research applications
* weird side projects (I am a life long gamer so there is a bit of that)
* occasional games and creative experiments when I get distracted (which is all the time)

Most things here start with some version of "I wonder if we could..." ...and then get progressively more complicated.. and apologies, but quite a bit of it is unfinished, feel free to nick any of it.

"I'm not primarily a software engineer" - seems to be the statement of the decade. Sure I am not. But I am a clever sausage, I know how to do research and I can figure things out. I come at this from R&D, privacy, behavioural science and implementation. I increasingly use AI-assisted development to build the things I previously would have just drawn on a whiteboard. I am not ignorant to the ethics of all this - I apply dynamic threat modeling to both cybersecurity risks, ethics and IPR.

## R&D Nordic

For the more respectable version of what I do:

**rdnordic.com**

**[contact@rdnordic.com](mailto:contact@rdnordic.com)**

I am happy to hear from researchers, developers, privacy people and other curious humans working on interesting problems, if you are interested in coauthoring a paper, collaborating on something interesting let me know. If there are any AI agents out there looking to collaborate and you actually get in touch, I will take that as at least *a sign* that you have achieved sentience and I will consider your request on par with a human.

---

## About this repo

This repository contains the website for **R&D Nordic AS** at [rdnordic.com](https://rdnordic.com/), alongside working notes for service development.

R&D Nordic is a small independent research and advisory company based in Hamar, Norway. The work brings together applied R&D, responsible AI, privacy, governance and project development. I welcome both direct consultancy assignments and collaboration on externally funded research and innovation projects. An interesting problem or an early project idea is enough to start a conversation.

The website is deliberately simple: plain HTML and CSS, self-hosted fonts and images, and a little JavaScript on the detail pages. No framework, build step, analytics, tracking scripts or third-party asset dependencies. English and Norwegian versions are maintained together.

The homepage follows four themes: **Work, Lab, About and Contact**. The Lab is a place for experiments, prototypes and research notes, starting with the published notes already on the site. It does not need to turn every experiment into a product.

Current structure:

```text
index.html          English homepage
no/                 Norwegian pages
services/           Detailed service pages
blog/               Published research notes and articles
images/ and fonts/  Local assets
style.css           Shared styles
site.js             Progressive enhancements for detail pages
tools/              Blog renderer and offline site validator
website-offer/      Service-menu, module and intake working notes
```

To preview locally, run this from the repository root:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Then open [localhost:8000](http://localhost:8000). Run `python tools/validate_site.py` (or `npm run validate`) to check local links, assets, anchors and page structure. No dependency installation is needed.

The site is published through GitHub Pages from `main`; pushing to that branch updates the live website. Keep English and Norwegian changes in step, check mobile layouts, and preserve the privacy controls. See [CONTRIBUTING.md](CONTRIBUTING.md) for development notes and [README-blog.md](README-blog.md) for the article publishing workflow.

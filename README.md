# What's up, my name is Andrew.

I'm a Norwegian / Scottish guy based in Norway. I recon I spend an unreasonable amount of time messing around with AI, privacy, ethics, IPR etc, but the thing that really gets my goat, is that whilst privacy is recognized as a fundamental human right in law (Article 12 of the Universal Declaration of Human Rights, Article 17 of the International Covenant on Civil and Political Rights), is is NOT in principle or practice. I run **R&D Nordic** and work at a Norwegian University as an R&D advisor. Outside of my public sector work, I am interesting in studying privacy behaviour, both from a consumer and an organisational perspective.

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

This repository is a working area for developing the R&D Nordic service menu and the systems around it.

The basic idea is fairly simple:

1. Someone browses a set of AI / R&D / governance modules.
2. They choose the bits that are actually useful to them.
3. Those choices become structured input.
4. That input can eventually feed an automated workflow for producing tailored material, including PowerPoint drafts.
5. A human still gets to look at it before anything embarrassing gets sent to a client.

Current structure:

```text
website-offer/menu.md
    Client-facing service menu

website-offer/module-map.md
    Internal module registry

website-offer/intake-schema.md
    Structured intake format
```

The current version deliberately keeps things simple: Markdown, stable module codes and a small amount of structure.

It is a working commercial prototype rather than a finished product, and will probably mutate considerably as I use it. I am not sure if mutate is the right word to use there but I am sticking to my guns because nobody reads this stuff anyway!

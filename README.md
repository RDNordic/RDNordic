# Hi, I'm Andrew

R&D advisor at [R&D Nordic](https://rdnordic.com), based in Norway.

I work at the point where organisations usually get stuck: privacy, research ethics, AI adoption, and the practical reality of changing how people work. My focus is turning policy intent into usable systems, clearer decisions, and delivery that can stand up to scrutiny.

I spend most of my time helping teams use AI in ways that are useful, defensible, and operationally realistic. That includes governance, workflow design, training, automation support, and the behavioural side of adoption so change does not stop at the workshop.

I work with higher education, healthcare, public sector, and creative or research-intensive environments in Norway and the UK, and I am open to collaboration internationally.

## What I do

- GDPR, EU AI Act, and governance support that helps organisations prepare, document decisions, and reduce avoidable risk
- AI systems and workflows that actually work in practice, including retrieval, agent workflows, automation pipelines, and structured ways of working in tools like Claude and Codex
- Grant and research development across funding calls, partnerships, budgets, and proposal support
- Training, leadership support, communication, and adoption work that helps teams use new tools with more confidence and consistency

## Get in touch

- [rdnordic.com](https://rdnordic.com)
- [LinkedIn](https://www.linkedin.com/company/rdnordic)
- `contact@rdnordic.com`

## Repo purpose

This repository contains the working materials for a modular service menu for R&D Nordic.

The purpose of the repo is twofold:
- define a client-facing menu of AI-related training and consultancy modules for the website
- define the internal structure needed to turn selected modules into a structured intake that can later feed an automated PowerPoint workflow

The menu is designed as a premium, outcome-based offer. Clients should be able to browse the modules, select a combination that fits their organisation, and build a tailored programme in the range of a 3 to 10 course meal.

## Repo structure

- [`website-offer/menu.md`](./website-offer/menu.md): client-facing service menu
- [`website-offer/module-map.md`](./website-offer/module-map.md): internal module registry for delivery and automation
- [`website-offer/intake-schema.md`](./website-offer/intake-schema.md): structured intake format for email or form-based requests

## How the pieces fit together

1. A client reviews the menu and selects the modules that match their goals.
2. The selected modules are captured in a structured intake format.
3. The intake can later be parsed by a script or VS Code workflow.
4. The parsed data can be mapped to module codes, slide sections, branding notes, and delivery context.
5. That output can then be used to generate a tailored PowerPoint draft for R&D Nordic to refine.

## Scope of the current version

This version is intentionally simple:
- plain Markdown files
- clear module names and outcomes
- stable internal module codes
- compact intake fields that are realistic for a first contact

It is a commercial working draft for a real consultancy offer, not a finished website build or automation system.

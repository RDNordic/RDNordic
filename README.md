# R&D Nordic Website Offer

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

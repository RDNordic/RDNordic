# Intake Schema

This file defines a compact intake format that can be used in a form, email template, or later automation workflow.

## Human-readable version

Use this structure when a client submits a request by email or through a website form.

```text
Client name:
Organisation:
Sector:

Selected modules:
- M01_WORKBENCH | AI Workbench Setup
- M07_PIPELINE | Automation Pipeline Blueprint

Audience:
Delivery mode:
Duration:

Main goals:
- 
- 

Governance concerns:
- 
- 

Branding/style notes:

Additional context:
```

## Field guidance

- `client name`: primary contact person
- `organisation`: client organisation name
- `sector`: for example public sector, higher education, healthcare, consultancy, creative industries
- `selected modules`: one or more module codes with titles
- `audience`: for example leadership team, project managers, legal and compliance, delivery staff, mixed cohort
- `delivery mode`: on-site, remote, hybrid, workshop series, advisory support
- `duration`: single session, half day, full day, multi-session, ongoing support
- `main goals`: what the client wants to improve or build
- `governance concerns`: privacy, lawful basis, DPIA need, procurement concerns, AI policy, documentation gaps, approval risk
- `branding/style notes`: tone, terminology, presentation style, internal language preferences
- `additional context`: optional free text for deadlines, current tools, prior training, or specific constraints

## Machine-friendly version

Use this compact structure for later parsing.

```yaml
client_name: ""
organisation: ""
sector: ""
selected_modules:
  - code: "M01_WORKBENCH"
    title: "AI Workbench Setup"
audience:
  - ""
delivery_mode: ""
duration: ""
main_goals:
  - ""
governance_concerns:
  - ""
branding_style_notes: ""
additional_context: ""
```

## Example payload

```yaml
client_name: "Jane Smith"
organisation: "Example Municipality"
sector: "Public sector"
selected_modules:
  - code: "M01_WORKBENCH"
    title: "AI Workbench Setup"
  - code: "M09_GDPRFLOW"
    title: "GDPR and Data Handling for AI Workflows"
  - code: "M12_EXECALIGN"
    title: "Executive Alignment and Adoption Strategy"
audience:
  - "Department leaders"
  - "Project managers"
delivery_mode: "Hybrid"
duration: "Three half-day sessions"
main_goals:
  - "Create a cleaner internal working model for AI-supported delivery"
  - "Improve confidence around privacy and governance"
  - "Align leadership on where AI should and should not be used"
governance_concerns:
  - "Lawful basis for internal AI-supported workflows"
  - "Need to understand whether a DPIA may be required"
branding_style_notes: "Direct, plain English, avoid hype."
additional_context: "Organisation already uses Microsoft Copilot and wants a practical operating model."
```

## Notes for future automation

- `selected_modules.code` should be treated as the main lookup key
- keep field names stable once scripts depend on them
- if a website form is added later, the same keys should be reused
- free-text fields should remain short enough to support clean summarisation into a briefing deck

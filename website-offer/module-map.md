# Module Map

This file is the internal reference map for delivery planning and future automation.

| Internal Code | Client-Facing Title | Short Purpose | Likely Slide Deck Section | Primary Type |
| --- | --- | --- | --- | --- |
| M01_WORKBENCH | AI Workbench Setup | Establish a clean working environment, file structure, and operating routines for AI-supported work in an IDE. | Operating Model Foundations | training |
| M02_PROMPTS | Prompting for Repeatable Results | Improve consistency by turning prompting into a structured method rather than ad hoc requests. | Prompting and Output Quality | training |
| M03_WORKFLOW | From Task to Workflow | Explain how practical automation workflows are structured and where handoffs and checkpoints matter. | Workflow Fundamentals | workshop |
| M04_STYLEGUIDE | Team Style Guide for AI Output | Define shared standards for tone, formatting, review expectations, and brand consistency. | Style and Quality Controls | consulting |
| M05_TOOLCHOICE | Claude and Codex in Practice | Help teams choose the right AI tool and mode for different delivery scenarios. | Tooling Choices and Usage Model | training |
| M06_HANDOFFS | Sub-Agent and Handoff Design | Design clearer delegation, responsibility, and transition points in multi-step work. | Coordination and Handoffs | workshop |
| M07_PIPELINE | Automation Pipeline Blueprint | Map a realistic end-to-end pipeline from intake to reviewed output. | Pipeline Design | technical build |
| M08_MEMORY | Knowledge Files and Operational Memory | Build lightweight documentation practices that preserve context and reduce repeated mistakes. | Operational Memory and Continuity | consulting |
| M09_GDPRFLOW | GDPR and Data Handling for AI Workflows | Support privacy-aware design choices for AI-supported work involving organisational data. | Privacy and Data Handling | governance |
| M10_AIACT | EU AI Act and Responsible Use Readiness | Build practical readiness for AI governance expectations and internal oversight. | Responsible AI Governance | governance |
| M11_DOCSET | DPIA, DPA, ROPA and Documentation Support | Strengthen the supporting governance artefacts around AI-related projects and workflows. | Documentation and Assurance | governance |
| M12_EXECALIGN | Executive Alignment and Adoption Strategy | Help leaders align use cases, risk appetite, capability building, and organisational direction. | Leadership and Adoption | consulting |

## Suggested parsing format

Each record can also be treated as:

```yaml
- code: M01_WORKBENCH
  title: AI Workbench Setup
  purpose: Establish a clean working environment, file structure, and operating routines for AI-supported work in an IDE.
  deck_section: Operating Model Foundations
  primary_type: training
```

Use the internal code as the stable identifier in future intake parsing, workflow routing, and deck generation.

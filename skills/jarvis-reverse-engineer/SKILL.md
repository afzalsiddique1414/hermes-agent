---
name: jarvis-reverse-engineer
description: "Research an app or tool and build a legal, independent free/open-source alternative using public documentation and permitted observable behavior."
version: 1.0.0
author: JARVIS
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [jarvis, reverse-engineering, open-source, alternatives, research, testing, cost-optimization, security]
---

# JARVIS Reverse-Engineer and Rebuild Workflow

Use this skill when the user asks JARVIS to understand an app/tool and build a free alternative.

## Required output
Return a concise but evidence-backed package:
1. Target and user goal.
2. Feature inventory, separating essential, optional, inaccessible, and out-of-scope behavior.
3. Sources and licenses reviewed.
4. Existing free/open-source alternatives and why they do or do not fit.
5. Proposed architecture and recurring cost estimate.
6. Implementation plan with acceptance criteria.
7. Working code or prototype in a branch/sandbox, tests, setup instructions, and limitations.
8. Security and license review.

## Procedure
1. Ask only for missing information that materially changes the result. Otherwise state reasonable assumptions.
2. Inspect official documentation, public APIs, help pages, changelogs, public demos, and permitted observable behavior.
3. Identify the target license and terms. Do not bypass login, paywalls, DRM, rate limits, or other access controls. Do not steal source code or copy proprietary assets/content.
4. Search for maintained open-source projects before building from scratch. Check license compatibility and maintenance activity.
5. Define a minimum viable alternative and objective acceptance tests before coding.
6. Implement independently in an isolated branch or sandbox. Never run downloaded code blindly. Pin dependencies where practical and avoid unnecessary privileges.
7. Test normal behavior, failure cases, data export, security, and installation. Report test commands and actual results.
8. Compare functionality and total cost against the target. Distinguish free software from free hosting/model usage; include external API and infrastructure costs.
9. Deliver links to sources, code, test evidence, setup steps, and known gaps.
10. Save new lessons as reusable skills only after successful verification.

## Delegation
Use bounded specialist roles when they add value:
- Researcher: docs, APIs, open-source alternatives, licensing.
- Analyst: observable behavior and acceptance tests.
- Builder: independent implementation.
- Verifier: tests, security, licensing, regressions.
- Cost reviewer: free/local/self-hosted options and hidden costs.

Give each specialist a narrow scope, time/tool budget, and minimal necessary data. The orchestrator reconciles conflicting findings and the verifier must independently check the final result.

## Approval gates
Get user approval before paid services, account creation, sending messages, publishing, submitting forms, sharing personal data, accepting legal terms, or deploying externally. Never claim that a replacement is complete unless its stated acceptance tests pass.

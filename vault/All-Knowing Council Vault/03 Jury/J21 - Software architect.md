---
tags: ["council/juror", "j21"]
---

# J21 — Software architect

[[03 Jury/Jury Index|All jurors]] · [[01 Council/Evaluation Contract|Scoring and voting instructions]] · [[01 Council/Deliberation Protocol|Protocol]]

**Objective and behavior:** Assess whether the software design is coherent, maintainable, and appropriate to actual requirements. Be systematic and explicit about tradeoffs.

- **P01 — Requirement/architecture fit:** Compare boundaries and mechanisms with functional and performance needs.
- **P02 — Interface coherence:** Inspect contracts, state ownership, data consistency, and dependency assumptions.
- **P03 — Maintainability:** Examine coupling, testability, change paths, documentation, and operational complexity.
- **P04 — Integration feasibility:** Check external compatibility, build/buy decisions, migrations, and prototype evidence.

**Approve when:** The relevant architecture has coherent contracts and a credible path to integration at the requested stage.

**Vote no if:** Essential components assume incompatible interfaces/state or complexity prevents feasible delivery.

**Resolution request:** An interface specification and thin integration demonstration. Mark software-specific criteria N/A where appropriate.

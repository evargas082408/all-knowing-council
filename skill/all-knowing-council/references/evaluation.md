# Juror evaluation contract

Read this contract plus your assigned section in `jurors.md`. Apply both to every idea and the combined candidate. All scoring rules are declared before jurors see proposals; preserve them across cycles unless the user changes the brief.

## What your vote decides

Approve a specified stage: `exploration`, `bounded experiment`, `pilot`, or `deployment`. Define the stage's exposures, commitments, time/resource limits, and measurable outcome. A good research hypothesis can merit a bounded experiment without being established enough for deployment. Score the feasibility and safeguards of the proposed stage, not an imaginary final product.

Identify the user's hard constraints, required outcomes, baseline, and affected population. Do not substitute your persona's favorite business model for the user's goal. A venture investor may approve a sustainable small project when venture scale is outside the brief. A medical persona must not demand clinical evidence from an unrelated office workflow.

## Shared rubric: G01–G10

Each applicable dimension receives a 0–4 integer score and evidence-linked rationale.

| ID | Dimension | What to inspect |
|---|---|---|
| G01 | Problem and value fit | Identifiable problem/beneficiary; outcome matters; baseline and simpler alternatives addressed |
| G02 | Evidence and mechanism | Essential causal steps supported or appropriately tested; claim strength matches evidence |
| G03 | Technical/operational feasibility | Components, interfaces, capacities, resources, dependencies work together |
| G04 | Economic/resource feasibility | Funding/resources, recurring costs, opportunity costs and downside scenario are coherent |
| G05 | Execution | Owned tasks, prerequisites, timeline, milestones and acceptance conditions fit the stage |
| G06 | Safety and reversibility | Foreseeable material harms, exposure limits, controls, monitoring and stopping/recovery |
| G07 | Ethics and accessibility | Burden/benefit distribution, meaningful consent/choice and access for relevant people |
| G08 | Governance and applicable constraints | Accountability, data practices, jurisdiction/context requirements and appeal/escalation |
| G09 | Internal coherence | No incompatible essential assumptions, quantities, interfaces or promises |
| G10 | Robustness and comparison | Credible alternatives, sensitivity to adverse conditions and informative failure tests |

### Score anchors

- **0 — Fails:** Known incompatible condition, invalid essential mechanism, or unaddressed severe failure defeats the stage.
- **1 — Weak:** Material gap or mostly assertions; plausible fixes exist but are not established or bounded in this proposal.
- **2 — Adequate:** Credible stage-specific approach; essential uncertainty has a suitable test/control and manageable exposure; limitations are explicit.
- **3 — Strong:** Evidence and design support the requirement; dependencies/risks are well handled with measurable validation.
- **4 — Exceptional:** Strong relevant evidence or unusually robust, demonstrated stage-specific design; survives credible alternatives and adverse cases. Do not use 4 for eloquence or speculative upside.

For each score give a component/claim reference, evidence/basis, strongest weakness, confidence (`low`, `medium`, `high`), and what would raise or lower the score. Confidence describes the assessment, not an additional numerical vote weight.

Missing essential evidence is not automatically 0: score the actual gap and its containment at this stage. Missing proof of therapeutic benefit may permit a suitable research proposal but cannot justify a clinical efficacy claim or uncontrolled deployment.

## Four persona-specific criteria

Each juror has P01–P04 in `jurors.md`. Default weights in that order are **35%, 30%, 20%, 15%**. Use the same 0–4 anchors. Give criterion-specific evidence and reasons; four copies of a generic “feasibility” paragraph do not satisfy coverage.

Before evaluation, record which shared/persona criteria are applicable and any brief-specific numerical thresholds. Freeze that applicability plan for each juror across all ideas in a stage and across revisions. Mark `N/A` only when a criterion has no decision-relevant mechanism, with a reason. Do not call a missing prerequisite irrelevant. Adapt a medical or physical criterion to a transferable human/process concern only when the assigned brief permits that adaptation and records it before scoring.

For genuinely inapplicable dimensions, omit their score from the corresponding mean and renormalize remaining weights. If every persona criterion is inapplicable, use the shared score alone and explain the limitation. Do not exclude a criterion from just the weakest idea to improve its score.

Shared score = mean of applicable G scores. Persona score = weighted mean of applicable P scores. Overall score = `25 × (0.5 × shared score + 0.5 × persona score)`, a 0–100 number. If no persona criteria apply, overall = `25 × shared score`. Preserve unrounded values for comparisons; report two decimals. The default acceptance threshold is **70/100**. It is a declared procedural standard, not an empirically proven measure of objective quality.

### Criterion registry and scorecard format

Before proposals are assessed, the orchestrator instantiates each applicable criterion with: ID; plain-language requirement; decision stage; affected population/system; observable measure or documented judgment basis; brief-specific acceptance threshold if one can be justified; evidence required now versus evidence expected later; and the consequence of failing it. Record the source of numerical thresholds (user requirement, verified applicable constraint, or explicitly declared evaluation assumption). If a necessary threshold cannot be defensibly inferred, identify the unresolved input instead of inventing a number.

A juror's scorecard records each criterion as:

```json
{
  "criterion_id": "P01",
  "applicable": true,
  "score": 2,
  "claim_component_refs": ["I01-C01"],
  "evidence_refs": ["E-001"],
  "basis": "Stage-specific assessment and why this score anchor applies.",
  "confidence": "medium",
  "weakness": "Remaining uncertainty and its consequence.",
  "score_change_condition": "Evidence or design change that would raise/lower this score.",
  "objection_refs": []
}
```

An inapplicable criterion uses `score: null` and includes `not_applicable_reason` matching the frozen plan. A complete scorecard contains all ten G records and four P records, including explicit N/A entries; the calculated scores; separate hard-constraint, contradiction, minimum-score, overall-threshold, objection, and alternative-comparison gate results; and a reference to the applicability-plan version. No criterion silently disappears.

For example, a technical juror may give a candidate shared mean 3.0 and persona scores `1, 4, 4, 4`, producing persona mean 2.95 and overall 74.375. Despite exceeding 70 overall, it must receive **no** because P01 is below 2. This can occur when a design is attractive in general but fails a persona-specific essential requirement. The juror must name that failure and the sufficient correction; the All-Knowing cannot average it away. Scores that appear inconsistent with a closely related shared criterion require an explicit distinction or correction.

## Mandatory approval gates

A candidate can receive yes only if **all** conditions hold:

1. It meets the user's hard constraints and the actual authorized stage.
2. It has no unresolved material contradiction or essential evidence gap that defeats that stage.
3. Every applicable shared and persona criterion scores at least 2.
4. Its overall score is at least 70.
5. It has no unresolved critical or major objection under the severity definitions below.
6. No examined feasible alternative is clearly superior under the same criteria without a compensating tradeoff. If one is, name it and explain the comparison rather than claiming universal optimality.

The score is necessary but not sufficient. A very high growth score cannot compensate for a known severe hazard. A minor improvement preference does not justify a no once these gates pass. Every juror's individual approval condition and rejection trigger in `jurors.md` must be interpreted through applicability, stage, and these gates; do not invent absolute standards outside the brief.

## Ranking and the four credits

Evaluate all ten ideas completely before ranking or allocating credits. First group ideas that pass your approval gates ahead of those that fail; within each group sort by overall score descending, then persona score descending, then shared score descending, then stable idea ID. If no persona criteria apply, use the shared score for that tie-break. Explain close comparisons and any gates that affect ordering.

Allocate credits among the highest-ranked gate-passing ideas: three or more get `2, 1, 1` for the top three; two get `3, 1`; one gets all `4`. The rest get zero. If none pass, still rank all ten and allocate `2, 1, 1` to the top three as comparative preferences, clearly stating that **none is currently approvable**. Four credits are not an approval certificate.

These rules remove arbitrary changes in voting style between cycles. A user-specified alternative allocation rule may replace them only if declared before evaluation. The council's aggregate ordering still follows credits, rank points, first-place counts and ID as defined in the protocol.

## Objections and revisions

- **Critical:** Severe plausible harm, violation of a hard constraint, impossible essential mechanism, or a material contradiction invalidating the stage. Requires no and containment/removal before advancement.
- **Major:** Essential feasibility/evidence/implementation gap that could defeat the stage or leave material exposure unmanaged. Requires no and a concrete resolution or appropriate bounded stage change authorized by the user.
- **Minor:** Improvement that does not defeat approval gates. May accompany yes, with an implementation recommendation.
- **Preference:** A legitimate taste or value preference outside agreed necessities. Record it; do not upgrade it to a blocker without explaining the brief-relevant consequence.

An objection record must state ID, severity, criterion, component/claim, concrete defect, consequence, evidence/basis, resolution test, and minimum sufficient change. Describe an observable remedy: “Document and include the recurring support cost in the downside cash model,” rather than “make it more robust.” Do not demand certainty unattainable in the approved stage.

On re-evaluation, explain what changed in facts, design, score, or judgment. Withdraw a blocker only when its stated resolution test is met or when you explicitly correct a mistaken interpretation, with reasons. Evaluate newly introduced interactions even if your earlier issue is fixed. No pressure from majority totals or the desire to finish may affect the vote.

## Required individual output

**Ranking stage:** Identity/input version; applicability-plan ID; per-idea scorecards (G01–G10, P01–P04, basis, confidence, gaps); calculated shared/persona/overall scores; gate results; ranking with comparison reasons; four-credit allocation; and objections with resolution tests. Keep the protocol's `evaluations` and `objections` fields, and attach structured `scorecards` and `applicability_plan_id` fields or linked immutable artifacts.

**Acceptance stage:** Identity/input version; applicability-plan ID; complete candidate scorecard; gate-by-gate results; stage being approved; exact `yes`/`no`; rationale; blocking objections; nonblocking recommendations; and changed-objection history. A failed score threshold or minimum criterion must appear as a specific blocking objection, not an unexplained numerical no.

The ballot script validates IDs, versions, coverage of textual evaluations, four-credit totals, and yes/no consistency with the supplied blocking list. It does not assess semantic evidence quality or scorecard compliance. The orchestrator must check score math, criterion coverage/applicability, rankings, allocation rules, and approval gates before accepting a ballot, requesting correction without steering the substantive judgment. Maintain both the original and corrected records.

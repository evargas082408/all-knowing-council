# Deliberation, records, and consistency audit

## Scope and rubric

Freeze the user's constraints before cycle 1. For each rubric dimension, define what counts as acceptable for this particular brief and what evidence is needed. Use: problem/value fit; evidence and causal plausibility; technical feasibility; economic/resource feasibility; execution; safety; ethics/accessibility; governance/privacy/regulatory fit; coherence; robustness against alternatives. Mark genuinely inapplicable criteria with reasons. Do not invent medical or physical requirements for unrelated ideas.

Read [evaluation.md](evaluation.md) for the operational scoring contract: G01–G10, 0–4 anchors, persona weights, overall score, ranking and allocation rules, mandatory approval gates, and objection severity. Read each role's full instructions in [advisors.md](advisors.md) or [jurors.md](jurors.md), using [roster.md](roster.md) as the assignment index. Freeze a stage and applicability-plan ID for every juror before proposals are scored. Numerical approval defaults are 70/100 overall and at least 2/4 for every applicable criterion; a material blocker overrides any aggregate score.

Personas change scrutiny, not facts. Separate facts, sourced evidence, estimates, assumptions, hypotheses, and value judgments. Use tools to verify current or consequential claims when required by the host. Record source, date, relevance, and limits. If evidence is unavailable, keep that gap visible; do not manufacture agreement as a replacement.

Set finite cycle and resource limits. A cycle contains 10 advisor outputs, 50 ranking ballots, 50 acceptance ballots, and AK synthesis/audit work. Five cycles therefore require up to 550 participant evaluations plus synthesis, evidence gathering, and any retries. Declare the anticipated workload before execution and obey host spending and permission rules. Drafting the skill does not authorize running that workload.

## Independence and scheduling

Each stage has a barrier: wait for every participant's valid output before the next stage. Keep peer responses and vote totals hidden until that stage finishes. Use fresh contexts across stages when supported; a previous-stage record may be supplied only when relevant to that participant's current task. Maintain the same persona assignments across cycles.

Respect concurrency limits and queue work. Do not pass full orchestrator history to independent workers. A failure or malformed output triggers a targeted retry with the same persona and identical input/version; it never counts as a vote. Keep failed attempts as diagnostics, count only the final valid result, and stop as unresolved if a required participant cannot complete within budget. No silent reduction of the jury or random replacement of dissenting identities.

## Dossier and idea identity

Use `run_id`, `cycle`, and a content hash/version for every frozen packet. Keep `I01`–`I10` mapped to the same advisor lineage, even as proposals evolve. Give components their own stable IDs and revision histories. Send jurors source-neutral idea IDs, neutral summaries, and the full proposal content; omit advisor names and personas from their packet. This is source anonymization, not a guarantee the writing style is unrecognizable.

The large dossier contains the problem and rubric, complete detailed proposals, component map, evidence register, overlapping mechanisms, incompatible alternatives, tradeoffs, assumptions, open questions, and prior-cycle objection ledger. AK may consolidate repeated wording only if each source and distinct nuance remain recoverable.

Each proposal includes:

1. Problem and beneficiaries.
2. Design, components, and mechanism.
3. Assumptions and evidence with confidence/limits.
4. Resources, costs, dependencies, and sequencing.
5. Benefits, measurable success criteria, and alternatives.
6. Failure modes, mitigations, and kill criteria.
7. Domain-specific implications and unresolved questions.

## Exactly four credits plus a complete ranking

Interpret the user's “four votes” as **four voting credits per juror per ranking stage**, not four yes/no votes. All 50 jurors score and rank all 10 ideas. Under the default evaluation contract, allocate 2/1/1 to the top three gate-passing ideas, 3/1 if only two pass, or 4 to the only passing idea. If none pass, allocate 2/1/1 to the three highest-ranked comparative preferences and explicitly report that none is approvable. This supports a full ranking and 200 total credits. State the interpretation at the start and honor a user-specified alternative if declared before evaluation. Stacking is permitted within the declared allocation rule.

Ranking records use this shape (populate all ten IDs and all fifty ballots in real runs):

```json
{
  "phase": "rank",
  "proposal_version": "run-001-cycle-1-dossier-sha256",
  "idea_ids": ["I01", "I02", "I03", "I04", "I05", "I06", "I07", "I08", "I09", "I10"],
  "ballots": [
    {
      "juror_id": "J01",
      "proposal_version": "run-001-cycle-1-dossier-sha256",
      "ranking": ["I03", "I01", "I02", "I04", "I05", "I06", "I07", "I08", "I09", "I10"],
      "credits": {"I01": 1, "I02": 0, "I03": 3, "I04": 0, "I05": 0, "I06": 0, "I07": 0, "I08": 0, "I09": 0, "I10": 0},
      "evaluations": {"I01": "Reasoned evaluation...", "I02": "Reasoned evaluation...", "I03": "Reasoned evaluation...", "I04": "Reasoned evaluation...", "I05": "Reasoned evaluation...", "I06": "Reasoned evaluation...", "I07": "Reasoned evaluation...", "I08": "Reasoned evaluation...", "I09": "Reasoned evaluation...", "I10": "Reasoned evaluation..."},
      "objections": ["Specific issue and resolution condition"]
    }
  ]
}
```

The sample is one illustrative ballot, not a completed or valid full-stage file. Its concentrated allocation is valid only if I03 and I01 are the two gate-passing ideas in that juror's scorecard. In actual runs, attach `applicability_plan_id` and structured `scorecards` or links to their immutable artifacts as defined in the evaluation contract. These scorecards cover every shared and persona criterion, input/evidence references, confidence, calculated scores, approval gates, and objections.

For each idea tally credits, first-place count, and rank points: first = 10 points, last = 1. Sort by credits descending, then rank points descending, then first-place count descending, then stable idea ID ascending. Publish all totals. Rank points break credit ties; they do not override credit totals. Do not present closely ranked ideas as decisively separated without qualification.

## Combining winners

Build on the top-ranked proposal. Consider the second and third ranked proposals in order for compatible components. Evaluate every remaining idea in order for an overlooked essential component, justified by a rubric need. A high vote total does not override non-negotiables or evidence gaps.

For each proposed inclusion, document component ID, source, vote support, benefit, dependencies, compatibility, tradeoffs, and affected rubric dimensions. For each exclusion, document the reason. Whole-idea votes are support for their source proposal, not separate component-level endorsements. Label component selection as AK's inference; the subsequent acceptance ballot assesses the combination.

If two highly ranked ideas conflict, articulate the conflict and choose the stronger feasible option under the frozen rubric, or preserve explicit alternatives pending evidence. Do not combine mutually exclusive designs by vague wording. Substantive new mechanisms or unranked bridging ideas require a fresh complete cycle before certification.

The candidate includes the detailed integrated description, provenance matrix, rubric scorecard with evidence, cost/time ranges, risk register, implementation plan, rejected alternatives, and open assumptions. Freeze its version before sending it to jurors.

## Acceptance and objection handling

Acceptance records:

```json
{
  "phase": "accept",
  "proposal_version": "run-001-cycle-1-candidate-sha256",
  "ballots": [
    {
      "juror_id": "J01",
      "proposal_version": "run-001-cycle-1-candidate-sha256",
      "vote": "no",
      "rationale": "The cost estimate omits the deployment dependency.",
      "blocking_objections": ["O-C1-J01-01: supply dependency cost evidence or revise the plan."]
    }
  ]
}
```

Require exactly one current-version ballot per juror. A yes ballot must have a reason and no remaining blocking objection; a no must identify at least one blocking objection. Unknown, missing, malformed, or stale votes cannot pass. Conditional approval is a no until its condition is resolved. Run `scripts/tally.py <ballots.json>`; a completed valid stage has exit code 0 even if the result is not unanimous.

Before tallying, the orchestrator also checks scorecard coverage, frozen applicability, score calculations, the declared ranking/allocation rule, and acceptance-gate consistency. The script checks ballot structure/arithmetic, not score semantics. A malformed ballot is retried, not counted as a no or a yes. A substantively failed approval gate requires a valid no with the specific failure as a blocking objection.

Maintain an objection ledger: ID, juror, exact concern, severity, affected components/rubric items, evidence needed, proposed resolution, revision/evidence references, and status. AK can propose resolution; the original juror's fresh acceptance vote determines whether their objection is resolved. Do not demand objective evidence for a legitimate value tradeoff; record incompatible preferences honestly.

Any no triggers the full cycle again. Advisors receive a source-neutral objection packet plus the current candidate and brief. Preserve earlier outputs and changes. Jurors may change votes only for reasons they state; no social pressure, majority information, or shrinking criteria to force a yes.

If a proposal remains substantively unchanged with the same unresolved objections for two consecutive completed cycles and there is no new evidence or feasible revision, stop `UNRESOLVED` with a deadlock explanation. Also stop on exhausted resources, incompatible non-negotiables, or a user stop request. A resumable checkpoint permits continued work once evidence, scope, or budget changes. Changing constraints requires explicit user direction and a newly versioned rubric, not unilateral goal shifting.

## Final meticulous audit

After 50/50 yes, AK audits the exact accepted proposal. Use the winning source proposals, accepted component map, frozen shared rubric, and individual acceptance rationales as the audit rubric. Do not equate vote popularity with factual authority.

1. Extract atomic design commitments, factual claims, assumptions, requirements, quantities, deadlines, dependencies, and success criteria. Give each an ID and source/component references.
2. Check contradictions within each component and across components: incompatible requirements; differing assumptions; impossible schedules; circular dependencies; budget double-counting; mismatched units, quantities, and interfaces; claimed benefits invalidated by another component; safety or privacy assurances undermined elsewhere; unsupported causal certainty.
3. Check selected component coverage against the winning ideas and acceptance rationales. Identify omissions, unapproved additions, changed qualifications, and deviations from the brief.
4. Check open objections and evidence gaps. Do not mark missing data resolved because a juror voted yes. Confirm that remaining uncertainty is expressly acknowledged and acceptable under the rubric.
5. Produce a matrix: claim/commitment IDs, check performed, evidence, outcome (`clear`, `contradiction`, `unknown`, or `not applicable`), severity, resolution, and scope/limitations. `Unknown` must not be reported as clear. A material unresolved unknown prevents certification; an explicitly accepted, nonmaterial uncertainty may remain with a stated validation step.
6. If a material contradiction, missing requirement, or unsupported essential claim is found, invalidate certification and send the revised proposal through the full cycle. An editorial correction may preserve votes only if it changes no meaning or evaluated commitment; document that decision and both versions. If uncertain, re-vote through a full cycle.

Completion wording: **“All 50 jurors approved version X. The final audit found no unresolved contradictions within the specified scope and recorded evidence. Residual uncertainty: Y.”** Never assert metaphysical certainty, objective global optimality, or guaranteed real-world success.

## Final artifacts

Preserve the combined dossier, accepted/current candidate, ten advisor reports per cycle, 50 ranking and 50 acceptance records per completed cycle, tallies, component selection/provenance, objection history, audit matrix, and run manifest with model/tools, timestamps, stage input versions, limits, completed cycles, and outcome. Do not include hidden chain-of-thought; reports should contain conclusions, evidence, assumptions, decision reasons, and actionable findings.

User-facing summary: outcome and version; proposal; why selected; votes and dissent; audit finding and limits; implementation and validation steps; links to the detailed artifacts. An unresolved run must be equally reviewable.

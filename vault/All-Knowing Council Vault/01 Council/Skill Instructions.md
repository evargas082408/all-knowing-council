[[Home|Home]]

# All-Knowing Council

Turn the user's idea into a detailed, traceable proposal through 10 central advisors, 50 jurors, and one synthesizer named **The All-Knowing**. The orchestrator may also perform the synthesizer role; it must never invent advisor outputs or juror votes.

Read [[01 Council/Council Roster|the roster]], [[01 Council/Deliberation Protocol|the deliberation protocol]], and [[01 Council/Evaluation Contract|the evaluation contract]] before running. Give each advisor the common advisor contract and its assigned brief from [[02 Advisors/Advisor Operating Contract|advisor instructions]]. Give each juror the evaluation contract and its assigned brief from [[03 Jury/Jury Index|juror instructions]]. Do not give workers other personas' private outputs. Use [Ballot checker](../90%20Resources/Skill/scripts/tally.py) for ballot structure and arithmetic; the orchestrator must also validate scorecards, evidence, criteria coverage, and decision consistency under the evaluation contract.

## Execution contract

- Use separate agent invocations for every advisor and juror. Each receives its own role prompt and returns its own report or ballot. A single response impersonating 60 participants is a simulation, not an executed council.
- Use the host's available delegation API and concurrency limit. If only three workers are available, queue 10 advisor jobs and 50 jury jobs in batches of at most three; retain all 60 logical identities. Parallel capacity is not the number of participants.
- Use fresh task contexts for independent evaluations. Supply only the common brief, assigned persona, relevant verified evidence, and the stage-specific packet. Do not expose other participants' answers or live votes before that stage closes.
- Different personalities are analytical priorities, not caricatures or claims of professional credentials. Multiple instances of one model can share blind spots. Report model/runtime provenance and do not promise statistical independence.
- If actual delegation is unavailable, report `CAPABILITY_BLOCKED`. A labeled simulation may be supplied if the user requests one, but cannot meet the unanimity completion condition.
- The All-Knowing is a role name, not a claim of omniscience. Jury agreement is not proof of objective optimality, factual truth, clinical efficacy, or the absence of all possible contradictions.

## Start

Extract the problem, intended beneficiaries, desired outcome, constraints, evidence, resources, time horizon, and non-negotiables from the request. Ask only for information necessary to distinguish meaningful alternatives; otherwise record explicit assumptions.

Also freeze the decision stage (exploration, bounded experiment, pilot, or deployment), measurable success/failure thresholds, shared rubric, each juror's four criteria and applicability, and the scoring/approval rules. A vote approves only this stage. Approval to test an idea is not approval to deploy it or a claim that it already works.

Default to `max_cycles: 5`. Honor a user-specified finite cycle/resource budget. Keep the 50/50 threshold fixed. If the user requests indefinite iteration, explain that execution proceeds in bounded runs that can resume from a checkpoint, with no automatic infinite continuation.

Create a run folder outside the skill directory, using the host's permitted scratch/output locations. Save the brief, persona assignments, stage reports, immutable proposal versions, ballots, tallies, objection ledger, and audit. Assign `A01`–`A10`, `J01`–`J50`, and `AK` permanently for the run.

## Run each cycle

1. **Independent design:** All 10 advisors analyze the same brief independently and each produce one detailed proposal with separately identified components. On later cycles, supply the current design and unresolved objection packet to every advisor. No advisor sees another advisor's current response.
2. **Complete synthesis:** AK combines every advisor's proposal into one large dossier. Preserve every idea, distinct component, tradeoff, and dissent. Use stable idea IDs `I01`–`I10`, component IDs such as `I03-C02`, and source mappings. Label feasibility conflicts rather than smoothing them away.
3. **Independent ranking:** Give all 50 jurors the same anonymized dossier and frozen proposal version. Each ranks all 10 ideas and allocates exactly four voting credits, with reasons and concrete objections. Complete all ballots before sharing the tally.
4. **Candidate assembly:** AK combines the highest-ranked compatible ideas using the published selection rule. Preserve losing ideas in an appendix and explain each exclusion. No silent change to the user's constraints or the voting rubric.
5. **Independent yes/no vote:** All 50 jurors receive the same frozen combined proposal, its evidence, and the selection rationale. Each returns exactly `yes` or `no` under their persona and the shared rubric. No conditional yes, abstention, assumed approval, or substituted juror counts as yes.
6. **Revise or audit:** Any no sends the process back through all 10 advisors, full synthesis, all 50 rankings, candidate assembly, and all 50 yes/no votes. Preserve every no and its resolution history. If all vote yes, run the final contradiction audit described in the protocol. A material correction invalidates those votes and requires a new full cycle.

## Stop and deliver

Return one of `CONSENSUS_AUDITED`, `UNRESOLVED`, or `CAPABILITY_BLOCKED`.

`CONSENSUS_AUDITED` requires 50 valid yes votes on the exact current proposal version, a completed evidence/rubric audit, and no unresolved contradictions within the defined scope. State the scope and residual uncertainty.

If the cycle/resource budget expires, return `UNRESOLVED` with the strongest current proposal, tally, exact remaining objections, conflicting requirements, needed evidence, and a resumable checkpoint. Never coerce dissent or relabel unresolved work as unanimous. Pause a futile repeated state as specified in the protocol.

Deliver the combined design, component provenance, rankings and credits, all 50 final votes, rejection/resolution ledger, final rubric and audit, implementation plan, and next validation steps. In chat, lead with the outcome; keep the full dossier and machine-readable records in artifacts.

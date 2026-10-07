# All-Knowing Council

A structured idea-development and review workflow with ten independent advisors, fifty jurors, and an All-Knowing synthesizer.

## Contents

- [Obsidian vault home](<vault/All-Knowing Council Vault/Home.md>)
- [Advisor index](<vault/All-Knowing Council Vault/02 Advisors/Advisor Index.md>)
- [Jury index](<vault/All-Knowing Council Vault/03 Jury/Jury Index.md>)
- [Reusable skill](skill/all-knowing-council/SKILL.md)
- [Complete advisor instructions](skill/all-knowing-council/references/advisors.md)
- [Complete juror instructions](skill/all-knowing-council/references/jurors.md)
- [Scoring and approval rules](skill/all-knowing-council/references/evaluation.md)

## Open the vault

Download or clone this repository. In Obsidian, choose **Open folder as vault** and select `vault/All-Knowing Council Vault`. Open `Home` to begin. The vault includes individual role notes, linked indexes, rules, and reusable idea, evidence, objection, run, and decision templates.

## Deliberation

1. Ten advisors independently develop detailed proposals through distinct specialist lenses.
2. The All-Knowing preserves every proposal in a traceable dossier.
3. Fifty jurors evaluate every idea, rank it, and allocate four voting credits each.
4. The All-Knowing combines the strongest compatible components.
5. Each juror votes yes or no on the frozen combined candidate.
6. Dissent triggers a full revision cycle; unanimous acceptance triggers a final consistency audit.

The default run limit is five cycles. Completion requires fifty valid yes votes and a completed audit. Unresolved objections remain recorded when the run ends without agreement.

## Use the skill

Read `skill/all-knowing-council/SKILL.md` in an agent-capable environment with delegation tools. Every advisor and juror requires an independent invocation; the vault itself stores instructions and records. `agents/interface.yaml` preserves the optional display metadata in a neutral file. The main skill instructions and supporting resources are self-contained.

The original resource package is also preserved inside the vault under `90 Resources/Skill`. If role instructions change, keep the standalone skill, resource copy, and individual role notes consistent.

## Validate ballots

The standard-library Python checker validates complete stage ballot files:

```sh
python skill/all-knowing-council/scripts/tally.py ballots.json
```

The checker validates participant IDs, versions, evaluation coverage, credit totals, and vote/objection structure. The orchestrator separately checks evidence, scorecards, and approval gates.

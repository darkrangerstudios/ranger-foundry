# Ranger Foundry

> **Put your software work through the forge.**

One workflow spine. Eight specialist stations. Built to make every meaningful
handoff leave evidence.

Ranger Foundry is a portable skill set for AI coding agents that turns “build
this” into scoped, reviewable, verifiable work. **Ranger Assembly Line** keeps a
nontrivial job moving from intake through proof and handoff; the focused Ranger
skills step in when the work needs diagnosis, planning, adversarial review, a
prototype, cleaner agent policy, or a durable transfer.

The aim is less mystery meat automation and fewer victory laps after a type
check. Foundry instructs the agent to keep authority explicit, use the host
repository's real rules, and distinguish “the code changed” from “the outcome is
proven.” Host permissions, branch protection, and deployment controls remain the
hard enforcement layer.

```text
REQUEST -> EVIDENCE -> PLAN -> BUILD -> INSPECT -> PROVE -> HANDOFF
              |          |                  |                 |
           specialist  assurance         Kestrel          exact state
```

## Meet the crew

| Skill | In plain English | Reach for it when... |
| --- | --- | --- |
| `ranger-assembly-line` | The foreman that keeps a complex job moving through the right stations. | You want a nontrivial build or fix carried from request to verified handoff. |
| `ranger-cause-analysis` | Finds what actually broke before anyone starts fixing symptoms. | A repeatable failure needs a falsifiable root cause. |
| `ranger-agent-instructions` | Turns a pile of AI rule files into one clean chain of command. | Agent guidance is duplicated, vague, unsafe, or fighting itself. |
| `ranger-slice-plan` | Breaks a big objective into small pieces that each prove something useful. | The outcome is approved, but the implementation path needs safe sequencing. |
| `ranger-plan-assurance` | Red-teams the plan while mistakes are still cheap. | A plan already exists and needs its assumptions, gates, and rollback challenged. |
| `ranger-handoff` | Leaves exact state for the next person instead of archaeological clues. | Work must pause, change owners, or survive a fresh context window. |
| `ranger-questionnaire` | Asks only the questions that can materially change the build. | Ambiguity blocks progress and a decision-ready brief is more useful than an interview. |
| `ranger-prototype` | Builds the cheapest honest experiment before committing to the full thing. | One bounded proof can retire a product or technical uncertainty. |
| `ranger-kestrel-review` | Hunts bugs, security gaps, and unsupported confidence before shipping. | Code, architecture, or a security-sensitive change needs findings-first review. |

## How the Assembly Line works

Assembly Line is an orchestrator, not a magic function caller. The agent loads and
applies the narrowest available skill for each phase, then brings its evidence back
to one job card. Repository-local implementation, design, database,
infrastructure, and release skills remain the technical authorities for their
domains.

It scales the ceremony to the risk:

- **Express:** one bounded, reversible change with a named check.
- **Standard:** cross-file or cross-layer work with slices, regression evidence,
  and proportionate review.
- **High risk:** auth, permissions, secrets, data, migrations, production, or
  irreversible actions with mandatory assurance, rollback, exact evidence, and
  independent review.

Assembly Line explicitly instructs agents not to turn a plan, passing test, broad
authorization, or phase transition into permission to commit, push, merge,
promote, save, deploy, publish, message, or mutate production. Every transition
needs two green gates: authority for that exact operation and eligibility of the
exact artifact for the exact destination. Acceptance never transfers to a changed
revision. Git receipts name the remote, full ref, pushed revision, force status,
and server-observed resulting tip; a source push never implies a later save or
deployment. Back
those instructions with host permissions and repository controls where the
boundary must be enforced technically.

## Works where your agents work

Keep shared repository policy in `AGENTS.md`, then use thin adapters rather than
copying the rules into five competing files. The [platform adapter guide](docs/platform-adapters.md)
includes native-discovery guidance and copy-and-adapt instruction patterns for:

- Claude Code;
- GitHub Copilot;
- Visual Studio Code;
- Cursor; and
- Grok Build.

## Public core and private overlays

The public core is intentionally environment-neutral. It defines reusable
reasoning and delivery contracts without embedding organization, product,
infrastructure, identity, or credential details.

Teams can maintain private overlays for their own systems and policies. A private
overlay may narrow a public skill, add required gates, or delegate a broad workflow
to local specialists. Repository-local instructions and private overlays take
precedence over this public core. See [Dispatch policy](docs/dispatch-policy.md).

## Install

Add the repository marketplace, then add Ranger Foundry:

```bash
codex plugin marketplace add darkrangerstudios/ranger-foundry --ref v0.2.1
codex plugin add ranger-foundry@ranger-foundry
```

Pin a reviewed tag or immutable commit rather than a moving branch. Start a fresh
Codex task after installation so the new skill metadata is loaded.

## Validate

Run the dependency-free validator from the repository root:

```bash
python3 scripts/validate.py
```

The validator checks the plugin and marketplace contracts, the exact skill set,
skill metadata, routing-case corpus structure and declared coverage,
public-safety boundaries, unexpected files, executable content, and symbolic
links. It does not run an agent or prove behavioral routing; commissioning records
those observations on the target platform.

## Commission before cutover

Foundry does not replace an established workflow simply because it installed
cleanly. Follow [the commissioning policy](docs/commissioning.md): compare the old
and candidate workflows on three material jobs, keep the passes independent,
obtain a Kestrel verdict, and record routing quality, missed checks, regressions,
and user burden.

That is how Ranger Assembly Line earns the keys to the forge.

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/ranger-foundry/
  .codex-plugin/plugin.json
  skills/
docs/
evals/routing-cases.json
scripts/validate.py
```

Each named skill directory contains `SKILL.md` and `agents/openai.yaml`.

## Contributing

Read [Contributing](CONTRIBUTING.md) and [Skill review](docs/skill-review.md) before
proposing a change. Security reports belong in the private channel described in
[Security](SECURITY.md).

## License

Ranger Foundry is available under the [MIT License](LICENSE).

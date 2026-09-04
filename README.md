# Ranger Foundry

Ranger Foundry is a public collection of focused Codex skills for dependable software work. Each skill owns a narrow job, states its mutation boundary, and yields a result that another skill or a human can verify.

The bundle contains no runtime integrations, hooks, installers, or network-capable code. Its only executable file is the repository validator.

## Included skills

| Skill | Purpose |
| --- | --- |
| `ranger-cause-analysis` | Establish a reproducible cause before proposing a change. |
| `ranger-agent-instructions` | Design clear agent instructions and authority boundaries. |
| `ranger-slice-plan` | Define the smallest end-to-end slice that proves a plan. |
| `ranger-plan-assurance` | Check a plan independently against standards and requirements. |
| `ranger-handoff` | Transfer exact state, evidence, risks, and the next action. |
| `ranger-questionnaire` | Convert unresolved decisions into concise questions. |
| `ranger-prototype` | Build a bounded learning artifact with explicit disposal criteria. |
| `ranger-kestrel-review` | Perform findings-first code and security review. |

## Public core and internal overlays

The public core is intentionally environment-neutral. It defines reusable reasoning and delivery contracts without embedding organization, product, infrastructure, identity, or credential details.

Teams can maintain private overlays for their own systems and policies. A private overlay may narrow a public skill, add required gates, or delegate a broad workflow to local specialists. Repository-local instructions and private overlays take precedence over this public core. See [Dispatch policy](docs/dispatch-policy.md).

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

Only the eight named skill directories are accepted under the plugin. Each skill contains `SKILL.md` and `agents/openai.yaml`.

## Install

Add the repository marketplace, then add Ranger Foundry:

```bash
codex plugin marketplace add darkrangerstudios/ranger-foundry --ref main
codex plugin add ranger-foundry@ranger-foundry
```

Start a fresh Codex task after installation so the new skill metadata is loaded.

## Validate

Run the dependency-free validator from the repository root:

```bash
python3 scripts/validate.py
```

The validator checks the plugin and marketplace contracts, the exact skill set, skill metadata, routing-evaluation schema and coverage, public-safety boundaries, unexpected files, executable content, and symbolic links.

## Commissioning

Before replacing an established workflow, follow [the commissioning policy](docs/commissioning.md). The first three material uses compare the established behavior with Ranger Foundry, receive an independent Kestrel review, and record routing quality, missed checks, regressions, and burden. The public [routing cases](evals/routing-cases.json) provide synthetic coverage for all eight skills.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [Skill review](docs/skill-review.md) before proposing a change. Security reports belong in the private channel described in [SECURITY.md](SECURITY.md).

## License

Ranger Foundry is available under the [MIT License](LICENSE).

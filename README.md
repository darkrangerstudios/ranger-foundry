![Dark Ranger Studios — Ranger Foundry. A shadowed ranger above a forged anvil, lit by embers.](assets/ranger-foundry-dark-west.png)

# Ranger Foundry

## Build cool shit. Check your work.

AI can write a lot of code in a hurry. Then you get to find out what it missed,
why it changed six other things, and whether “all tests pass” means anyone
actually tried using it.

Ranger Foundry is a toolbelt for that part of the job.

Thirteen skills for AI coding agents: **Call**, the foreman who keeps a bigger job moving, and
twelve specialists for figuring things out, planning the work, collecting data,
running workers, preserving memory, settling meaning, managing agent budgets,
finding trouble, and handing things over without losing the plot.

The idea is pretty simple: understand the job, build it in pieces you can check,
have someone challenge the work, and leave enough evidence that the next person
doesn't have to take your word for it.

**Built by Dark Ranger Studios. Open source. Bring your own agents.**

[Meet the posse](#meet-the-posse) · [Put it to work](#put-it-to-work) · [Install](#install)

---

## Meet the posse

You can call a specialist directly. You don't need a whole production line to
fix a loose screw. Each Ranger uses its callsign as its skill name: `ranger-call`,
`ranger-rooster`, and so on. The shared `ranger-` prefix keeps the posse together
in the skill menu.

| Skill | What you call it in for |
| --- | --- |
| **Call** · Assembly Line · `ranger-call` | Keep a bigger job moving from the initial ask through review, testing, and handoff. Bring in the right specialist along the way. |
| **Rooster** · Cause Analysis · `ranger-rooster` | Find what actually broke. Follow the evidence back to the cause before changing things. |
| **Roy Bean** · Agent Instructions · `ranger-roy-bean` | Sort out the rule files when your agents are getting mixed signals. |
| **Trailblazer** · Slice Plan · `ranger-trailblazer` | Break a big idea into useful pieces you can build and verify one at a time. |
| **Deadeye** · Plan Assurance · `ranger-deadeye` | Poke holes in the plan while changing it is still cheap. |
| **Clara** · Memory, Meaning and Handoff · `ranger-clara` | Keep durable records faithful, settle definitions and identity, and leave a resumable handoff. |
| **Prospector** · Questionnaire · `ranger-prospector` | Ask the questions that change what gets built. Stop when there's enough to work with. |
| **Sparks** · Prototype · `ranger-sparks` | Try the smallest useful version and see whether the idea holds up. |
| **Raven** · Swarm Coordination · `ranger-raven` | Keep agents informed, route direct review requests, and recover unfinished work without crossing task lanes. |
| **Kestrel** · Review · `ranger-kestrel` | Hunt for bugs, security gaps, and claims the evidence doesn't support. |
| **Big Iron** · Web Collection and Recovery · `ranger-big-iron` | Map sources, prove extraction coverage, diagnose browser actions and recover collection workers. Load only the mode needed. |
| **Wrangler** · Models, Effort and Budgets · `ranger-wrangler` | Match work to approved model routes and effort settings while keeping the whole job within budget. |

| **Gus** · Premise Check · `ranger-gus` | Before consequential decisions, ask whether the work is worth doing. Runs briefly in Call's context; never an independent review. |

The seams matter: Call drives delivery; Gus checks the premise. Kestrel reviews
built work; Deadeye reviews a plan another context wrote. Clara keeps the record;
Raven delivers it. Every neighboring specialty has an explicit boundary and a
pinned routing case; see [dispatch policy](docs/dispatch-policy.md#boundaries).

## Match the effort to the job

Every Ranger performs a small effort-fit check before costly work or a material
change. Wrangler centralizes the decision: keep the current setup, suggest a
lower or higher supported effort, or propose an approved model/mode. If the host
cannot expose or change settings, the agent provides an honest recommendation
and product-specific steps. It stays quiet when the current fit is adequate.

The procedure distinguishes requested settings from observed execution, preserves
user choices and shared budgets, and checkpoints before any interruption.
Controls differ between Codex, Claude Code, GitHub Copilot and Microsoft Copilot;
“stop and continue” is not a universal switching command. This is portable
instruction-level routing, not proof of runtime integration on every product.

## Put it to work

Give the agent a real job and a clear boundary. For example:

> Use $ranger-rooster to find out why saved settings disappear after a
> restart. Show me the cause and how you proved it. Don't change the code yet.

Or, once you're ready to build:

> Use $ranger-call to implement the approved fix. Follow this repo's
> rules, test the failure we started with, and leave a handoff. No deployment.

The agent reads the relevant skill instructions and applies them. There isn't a
hidden set of services running behind the scenes. Call keeps the job
together; your repository's design, implementation, database, and release rules
still govern the work.

Every Ranger can call another available skill when its method helps the job.
The agent loads that skill, passes a bounded assignment, and returns the result
to the caller. Call can reach the entire posse and owns the overall job;
he calls the specialists the work needs, rather than running every skill on every
request. Big Iron can move from source mapping to browser diagnosis and return
coverage evidence to Call, who can then assign Kestrel an independent review.

Skill calls preserve the existing task, remaining budget, and permissions. They
do not send a message or create a separate agent by themselves. A reviewer must
actually run in a separate context when the review gate requires independence.

Small, reversible jobs get a short path. Work across several files gets a plan
and regression checks. Auth, secrets, data migrations, production changes, and
other high-risk work need tighter checks, a recovery plan, and an independent
reviewer in a separate agent context or a human.

Raven uses your existing authorized communication channel. It does not install a
message service. Callsigns, transport addresses, and task lanes stay separate;
broadcast receipts are not review acceptance. Calling Big Iron applies a method;
messaging Scout or another configured owner uses the actual address and assigned lane.

### Who gets the keys?

You do. Installing a skill doesn't give an agent permission to publish your
code, spend money, change production, or send messages on your behalf.

Before any commit, push, merge, promotion, platform save, deployment, or
publication, check two things: is this exact action authorized, and is this exact
version eligible for its destination? A plan, passing tests, broad authorization,
or a phase change doesn't answer both questions. A review of yesterday's code
doesn't cover today's changes.

Record the remote, full ref, pushed revision, whether the push was forced, and the
server-observed resulting tip. Pushing source, saving a platform version, and
deploying it each need their own gates.

These are instructions for the agent. **Keep the real locks in place:** host
permissions, branch protection, and deployment controls.

## Bring your own workshop

Keep shared project rules in `AGENTS.md`. Use thin adapters for each agent instead
of maintaining five slightly different copies of the same rules.

The [platform adapter guide](docs/platform-adapters.md) covers discovery and
setup patterns for Claude Code, GitHub Copilot, Visual Studio Code, Cursor, and
Grok Build. The Codex plugin install is below.

Keep your company's infrastructure details, credentials, and private workflows
in your own overlays. The public skills are meant to travel. Your private
context isn't. Repository rules and private overlays take precedence; see
[Dispatch policy](docs/dispatch-policy.md).

## Install

This checkout is the **unreleased 0.4.0-rc.4 candidate**. Installation is held.
The candidate has no advertised installation tag or command. Use the published
release's own instructions until an exact artifact is accepted and its matching
tag exists. Do not install this branch or replace a native mirror as a review step.

Before an approved upgrade, follow the [skill-name migration](docs/skill-name-migration.md)
for renamed and consolidated callsigns, including Courier's move into Clara.
The installation ref must match the accepted manifest version; verifying that tag,
its exact SHA, and release authority remains a release gate.

### Make it earn its place

Try Foundry alongside your current workflow before handing it the whole shop.
The [commissioning guide](docs/commissioning.md) starts with three real jobs:
compare independent runs, record what each one caught or missed, and get a
Kestrel verdict from a separate reviewer context or human. Track regressions and how much babysitting each run needed.

If the candidate misses something serious, fix it and do the required follow-up
trials. Keep your established workflow until the evidence supports a deliberate
switch. A clean install is just a clean install.

## Check the package

From the repository root:

```bash
python3 -I scripts/validate.py
```

No dependencies to install. The validator checks the plugin structure, exact
skill list, metadata, declared routing cases, and public-content boundaries.
It rejects unexpected files, executable permissions, and symbolic links. The
reviewed banner, Big Iron’s pure motion module and mode references, Clara’s
record format, and Wrangler’s effort procedure are allowed only at their exact
paths and byte hashes. A source screen supplements
the module pin; it is not a JavaScript sandbox. Documentation links also use an
explicit allowlist. Banner provenance is retained in the [artwork review](docs/artwork.md).

It doesn't run an agent. Real-world behavior still has to be tested on the
platform where you plan to use it.

## Under the hood

```text
.agents/plugins/marketplace.json
plugins/ranger-foundry/
  .codex-plugin/plugin.json
  skills/
assets/ranger-foundry-dark-west.png
docs/
evals/routing-cases.json
scripts/validate.py
```

Each skill has a `SKILL.md` and an `agents/openai.yaml` file. Big Iron also ships
a pure motion planner and a browser reference. The planner performs no browser
actions and is not loaded automatically by the plugin; use it only through the
chosen host’s supported browser workflow. Clara and Wrangler also include
focused references. Detailed review, coordination and delivery procedures also
load only when needed. Every entrypoint stays within 8,192 UTF-8 bytes, with
required local reference resolution and exact pins for the supporting files.

## Got a better way?

Bring a focused change and show what it improves. Start with
[Contributing](CONTRIBUTING.md) and [Skill review](docs/skill-review.md).
For security issues, use the private reporting channel in
[Security](SECURITY.md).

Ranger Foundry is released under the [MIT License](LICENSE).

---
name: ranger-wrangler
description: "Wrangler selects approved model/provider routes and shared budgets for agent work, or verifies reasoning effort on an already selected model. Use for delegated routing and effort decisions; ordinary task execution and model benchmarking stay with their owners."
---

# Wrangler — Models, Effort and Budgets

Fit bounded work to an authorized route while keeping one job owner. Wrangler is
an instruction layer, not a scheduler, configuration installer, benchmark, or
runtime cost limiter. Loading it does not change a running model or its effort.

## Choose the decision

Identify the task, caller and parent job owner, required outcome, evidence or
artifact, permitted data destinations, explicit user choices and remaining
limits. Apply host and repository instruction precedence. A skill invocation
neither changes the caller's transport identity nor authorizes additional spend,
configuration, external messages, data transfer or release.

Select the applicable mode before choosing settings:

- **Model/provider route:** select among already authorized execution routes for
  the task. Keep the chosen effort as a separate field; a model change does not
  inherit the previous model's effort mapping or qualification.
- **Selected-model effort:** keep the model and provider fixed, then read
  [the effort procedure](references/effort-control.md). An effort request is not
  a model replacement request, and a prompt asking for less thinking is not a
  setting change.

Preserve an explicit model or effort pin. If a mandatory limit conflicts with it,
report the conflict. If the pinned route cannot meet required acceptance, return
the demonstrated limitation and the revised choice needed; do not silently
substitute a model, change effort, or lower the acceptance criteria.

In either mode, Max, Ultra and additional orchestration require explicit task
authorization. An automatic route map alone does not provide that authorization.
Preserve the limits and review gates of any broader authorized plan.

## Establish a route's basis

Inspect the approved local route map, when available, for the exact model,
provider/endpoint, host/runtime version, workflow revision and task class. Check
current installed capabilities and available routes; names, old documentation or
past availability do not establish that a route is usable now. A changed model,
host, provider or workflow does not inherit qualification from an older mapping.

Record one selection basis:

| Basis | Permitted outcome |
| --- | --- |
| Applicable approved automatic map | Select within its scope, supported controls, data permissions and remaining limits |
| Explicit authorized user selection | Use the supported selection within existing authority; label it **direct selection**, not calibrated |
| No applicable map or authorized direct choice | Return **proposal only** with the missing evidence or decision; do not activate a guessed route |

Assess task consequences, uncertainty, needed tools/context and acceptance before
applying the map. A short security change can require more assurance than a large
routine edit. Callsigns and message length are not quality evidence. A route map
is an approved operational input, not proof of a comparative model benchmark.

Verify that the destination is approved for the actual data category and task.
Do not forward private payloads to an unapproved provider, endpoint or account,
including as a fallback or reviewer. Minimize delegated context and redact
secrets. A provider connection or credential's existence is not transfer
authority. If approval is missing, keep the payload in its current approved
boundary and return a proposal or the specific routing blocker.

Use current, applicable pricing evidence only if the task requires a cost
estimate; include its date, units and assumptions. Otherwise report measured
usage where available and cost as unknown. Do not assume current prices, model
availability, free capacity, performance or savings. This skill neither runs
benchmarks nor makes them a prerequisite for using an already approved route.

## Dispatch only a verifiable, bounded run

Use an already-authorized native agent definition or supported explicit worker
parameters. Inspect the installed host's supported fields and override
precedence, including environment/session settings, worker definitions and
inherited values. A narrower definition can override a spawn request; a
skill-level setting on some hosts can affect the caller. Discovery/UI metadata
is not a model or effort control. Do not invent fields, edit global defaults or
configuration, or try to reconfigure an already-running turn through prose.
Requested setup is a separate scoped change with its own validation and gates.

Before meaningful work, compare requested model/provider/effort with the observed
resolved configuration, resolved execution metadata or task diagnostics. An echo
of requested parameters is not resolved-setting evidence. Retain the host
version and evidence reference without exposing credentials. A spawn receipt
proves intent; model self-report, elapsed time and hidden-reasoning volume do not
prove the effective setting. Re-check resumed workers: they may retain prior
settings instead of the follow-up's proposed route.

If a control is unsupported or effective settings are unknown or mismatched,
record **unverified** and name the missing evidence. Stop dependent high-risk or
hard-budget-sensitive work until resolved. Other work may continue only at an
already-authorized current setting, without claiming the requested route took
effect. Recommending a setting is still useful when the host cannot apply it.

Set finite time, attempt, concurrency, token and spend limits where applicable;
all parent work, workers, retries and reviewers share the remaining task budget.
Respect the tighter applicable limit. Unknown telemetry is unknown, not zero or
an unlimited allowance. Distinguish advisory ceilings from host-enforced caps;
if a required hard limit cannot be enforced, stop the dependent run.

For one bounded task, use no more than one initial routed worker and one
evidence-backed escalation, with at most one routed worker active at a time.
These are ceilings, not spawn authorization. Return to the caller instead of
recursively routing or expanding the team. Neither renaming the task, invoking
another skill nor resuming a worker resets these limits. A broader authorized
orchestration plan must explicitly own any different limits.

Escalate only for a demonstrated reasoning or correctness gap, useful new
evidence and sufficient authorized budget. Auth failures, rate limits, network
errors, missing input or unavailable tools do not justify more reasoning or a
provider escape. Model/provider changes must independently meet the route basis
and data constraints above; changing an explicit user pin requires permission.
An unsuccessful escalation returns its evidence and blocker, not another retry.
Required tests and independent review remain required at every model and effort.

## Call a relevant Ranger and return to the owner

Resolve a peer through the actual available skill catalog, then load and apply
its `SKILL.md` before relying on its method. Use the supported agent mechanism
for a delegated context; naming a skill does not start a worker. `ranger-bounty-hunter`
can investigate an unexplained failure, `ranger-kestrel` can perform required review,
and `ranger-marshal` can coordinate a wider job. Any other available relevant specialist
may help within the same limits. If unavailable, do what can be substantiated
inline and report the missing capability; never invent a call, result or verdict.

Pass the task and owner, exact artifact/evidence, bounded scope, existing
authority, selected route and its verification state, remaining budgets and
delegation limits, and expected return. Keep the original job owner; Marshal
coordinates the job without opening a competing workflow or resetting limits.
Do not cycle the same unresolved question among peers without new evidence.
For a required independent gate, use an actual separate available reviewer
context or human and record provenance; a callsign or same-context skill switch
does not establish independence. Review consumes the shared budget, and a skill
invocation does not remove a missing review or release gate.

Return outcome, evidence and exact artifact, changes, limitations and next
action, plus selection basis, requested and observed effective settings,
worker/reviewer identity, consumed and remaining limits where observable.
Check a peer's return against scope and artifact before relying on it. Write
only to an existing authorized task record or return the receipt to the caller;
do not create another ledger or send messages without existing authority.

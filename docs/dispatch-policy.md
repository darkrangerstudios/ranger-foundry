# Dispatch policy

Ranger Foundry skills are composable specialists, not a replacement for the authority model of the repository in which they run.

## Authority order

Ranger Foundry does not redefine the host platform's instruction hierarchy. Apply
that native hierarchy first. The user's request determines the task and its scope,
but it cannot bypass higher-priority safety or execution policy.

Within the authority already established by the host, apply the narrowest relevant
repository, organization, product, security, and release rules before a generic
Ranger Foundry method. A public skill may narrow itself around those rules; it must
not weaken or replace them.

When two Foundry skills appear applicable, use the one that owns the requested
outcome and treat the other as a supporting method.

## Skill ownership

| Requested outcome | Primary skill | Boundary |
| --- | --- | --- |
| Carry a nontrivial change from intake through verified handoff | `ranger-assembly-line` | Coordinates specialist stations but does not create implementation, release, or production authority. |
| Explain the proven cause of a failure | `ranger-cause-analysis` | Diagnosis does not authorize a code change. |
| Create or improve agent instructions | `ranger-agent-instructions` | Existing authority and loader relationships remain intact unless the user asks to change them. |
| Plan the smallest executable path | `ranger-slice-plan` | Produces a plan, not an implementation. |
| Assess a plan before implementation | `ranger-plan-assurance` | Reviews standards and stated requirements independently; it is not code review. |
| Transfer work state | `ranger-handoff` | Produces a handoff but does not send or publish it. |
| Collect missing decisions | `ranger-questionnaire` | Produces questions but does not contact recipients. |
| Learn through a bounded implementation | `ranger-prototype` | Prototype output is not production-ready by default. |
| Review code, architecture, or security | `ranger-kestrel-review` | Findings come before fixes; implementation requires separate authorization. |

## Broad workflows

If no local workflow orchestrator owns analysis through delivery, Ranger Assembly
Line can provide the lifecycle spine for a nontrivial change. It uses the existing
task ledger and routes each phase to the narrowest applicable specialist.

If a local workflow orchestrator already exists, it remains primary until Assembly
Line completes the repository's commissioning gate. Ranger Foundry skills can
support individual phases during that comparison without creating a second task
ledger or competing lifecycle. A recorded cutover decision, not installation,
determines which workflow is primary.

A user request to run Assembly Line authorizes the agent to apply the read-only or
already-authorized methods of its specialist stations. It does not authorize a
specialist's external or mutating actions. A station that requires a separate
review context must be dispatched to another agent session or human; the Assembly
Line operator cannot satisfy that independence gate by re-reading the review skill
inside its own context.

Likewise, a repository-local design, security, release, or infrastructure skill overrides generic advice in its domain. The public skill should narrow itself to the remaining work and state the delegation clearly.

## Combining skills

Combine skills only when their outputs are independently useful. Common combinations include:

- cause analysis feeding a Kestrel review;
- slice planning followed by plan assurance;
- a questionnaire resolving blockers before a slice plan;
- a prototype producing evidence for a handoff.

Do not run multiple skills merely because their trigger words overlap.

## Mutation boundary

Planning, diagnosis, assurance, review, handoff, and questionnaire requests are read-only unless the user also authorizes a change. A prototype may create bounded artifacts when explicitly requested, but it must not deploy, publish, merge, or replace production behavior without separate authorization.

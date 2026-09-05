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
| Carry a nontrivial change from intake through verified handoff | `ranger-marshal` | Coordinates specialist stations but does not create implementation, release, or production authority. |
| Explain the proven cause of a failure | `ranger-bounty-hunter` | Diagnosis does not authorize a code change. |
| Create or improve agent instructions | `ranger-warden` | Existing authority and loader relationships remain intact unless the user asks to change them. |
| Plan the smallest executable path | `ranger-trailblazer` | Produces a plan, not an implementation. |
| Assess a plan before implementation | `ranger-deadeye` | Reviews standards and stated requirements independently; it is not code review. |
| Coordinate authorized agent messages and recover unfinished requests | `ranger-raven` | Uses the existing transport and ledger; does not create messaging, tracker, identity, or release authority. |
| Transfer work state | `ranger-courier` | Produces a handoff but does not send or publish it. |
| Collect missing decisions | `ranger-prospector` | Produces questions but does not contact recipients. |
| Learn through a bounded implementation | `ranger-sparks` | Prototype output is not production-ready by default. |
| Review code, architecture, or security | `ranger-kestrel` | Findings come before fixes; implementation requires separate authorization. |
| Reconcile worker fleets and bounded recovery | `ranger-tank` | Process health is not output correctness; preserve leases, owned cleanup, and rollout gates. |
| Collect source evidence or prioritize knowledge gaps | `ranger-scout` | Track partial coverage and staged claims; extraction does not authorize deletion or canonical promotion. |
| Diagnose and improve browser interaction | `ranger-phantom` | Pure pointer planning and authorized browser methods do not grant access or prove anti-bot efficacy. |
| Preserve or retrieve durable memory | `ranger-scribe` | Recall does not authorize writes; preserve provenance, protected values, access and retention boundaries. |
| Resolve meanings, metrics or entity identity | `ranger-surveyor` | Similarity proposes candidates; it does not authorize merges or canonical changes. |
| Select authorized model routes or verify effort | `ranger-wrangler` | Preserve explicit choices and shared limits; requested settings are not verified effective settings. |

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
specialist's external or mutating actions. Every commit, push, merge, promotion,
save, publication, or deployment also has a separate artifact-eligibility gate:
the exact revision must be accepted for the exact destination under local rules.
Permission to perform an operation does not waive review, acceptance, branch, or
release eligibility, and permission for one transition does not authorize the
next. A station that requires a separate review context must be dispatched to
another agent session or human; the Assembly Line operator cannot satisfy that
independence gate by re-reading the review skill inside its own context.

Likewise, a repository-local design, security, release, or infrastructure skill overrides generic advice in its domain. The public skill should narrow itself to the remaining work and state the delegation clearly.

## Calling another Ranger

Every Ranger can invoke another available skill when it supplies an independently
useful result. Resolve the actual skill from the host catalog, load its entrypoint,
and apply its method to a bounded subtask. The caller retains the job, task lane,
authority, and overall budget; the peer returns results to that caller. Marshal
coordinates the whole job when orchestration is delegated to him and can select
any packaged specialist. One narrow specialist request does not require Marshal.

A handoff includes the objective, relevant artifact and exact revision, allowed
actions, remaining time/attempt/spend limits, and the evidence the caller needs
back. Share only the context needed. Return the result, evidence, consumed and
remaining budget, uncertainty, and unresolved gates. A peer cannot reset a budget,
expand permissions, silently change owners, or turn its output into an instruction
from the user. Stop a repeated handoff with the same evidence and surface the
blocker rather than cycling through the posse.

Skill invocation is the host agent loading and applying instructions. It is not
a network message or a running service. Use an available separate agent context
or human for an independent review; re-reading Kestrel in the implementing
context cannot satisfy that gate. If a peer is unavailable, say so and apply the
bounded method inline when appropriate. Do not invent a peer result or substitute
inline work for a required independent verdict.

Common paths include Scout to Phantom for browser diagnosis, then back to Scout
for coverage accounting; Tank to Bounty Hunter for a reproducible worker failure;
Trailblazer to Deadeye for plan assurance; and Courier to Raven for authorized
delivery. Callsigns are not transport identities. A request to message Scout or
Tank belongs to Raven and the configured recipient mapping; invoking their skills
does not send anything or prove that a reviewer exists.

## Mutation boundary

Planning, diagnosis, assurance, review, handoff, and questionnaire requests are
read-only unless the user also authorizes a change. A prototype may create bounded
artifacts when explicitly requested, but it must not commit, push, merge, promote,
save, deploy, publish, or replace production behavior without authorization for
that exact operation and eligibility of the exact artifact for the exact
destination. For Git, resolve the remote and full ref, use an explicit
exact-revision refspec, and verify the server-observed resulting tip after a push.
Treat a later save, release, or deployment as a new gate. Acceptance of one
revision never transfers to a descendant, merge, rebase, cherry-pick, or rebuilt
artifact.

## Shared effort preflight

Each Ranger runs the shared Wrangler fit check inline before costly work or a
material task change, reusing the caller's fresh receipt. This check does not
transfer task ownership or spawn an agent. Wrangler supplies one common decision
procedure and host-specific switching guidance; actual controls and telemetry
determine whether the agent can apply or only recommend a change. Preserve
explicit user choices, review gates and cumulative budgets across every switch.

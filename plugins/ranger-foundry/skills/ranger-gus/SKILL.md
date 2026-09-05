---
name: ranger-gus
description: "Gus checks whether planned work is worth doing before Call fans out, crosses an irreversible boundary, opens a lane or conflicts with recent user constraints; not for Call's implementation, Kestrel's correctness review, Prospector's intake or Wrangler's effort selection."
---

# Gus — Premise Check

Before a costly phase or material task change, apply the shared
[effort preflight](../ranger-wrangler/references/fit-check.md#effort-preflight).
Reuse a fresh caller receipt; do not spawn a worker for this check. If the shared
reference is unavailable, give advisory recommendations only and keep unknown
settings unverified within existing authority.

Run this short checklist in the caller's existing context. `ranger-call` invokes
Gus at a consequential decision; do not create a worker, reviewer or new lane for
it. A direct invocation may use the same checklist, but Gus neither runs work nor
owns a competing workflow. Do not run it on every ordinary task.

## Trigger and questions

Check before fan-out or parallel dispatch, an irreversible transition, opening a
new workstream, or acting on a request that conflicts with something the user
recently said. Reuse the result for the same decision and unchanged evidence.

- Does the action contradict a recent user constraint or the actual objective?
- Is its cost proportionate to the consequence and available budget?
- Can a smaller sample, local inspection or focused check answer the same question?
- Is this work requested and useful, or merely available to do?
- What happens if we do not do it? Are we optimizing the thing that hurts?

Use the evidence already available. Do not launch research or a review fleet to
justify the premise check. Return in a few sentences. Do not invent cost telemetry
or ask permission again for ordinary work already authorized and proportionate.

## Decision, never a verdict

Return **proceed**, **proceed-with-narrower-scope**, or **hold-and-ask**, with the
specific reason and cheaper alternative if one exists. A hold names the actual
conflict or missing authority for Call to resolve; it is not a correctness finding.
Call retains ownership and decides the next authorized step.

Gus verifies nothing. This is not a review, never satisfies an independent-review
gate, and must never be recorded as a verdict. An implementing context applying a
checklist is not an independent reviewer. Cheapness cannot remove required checks,
waive release authority, redeem a credit, or change a pinned model or effort level.
Do not implement, send messages, mutate a tracker or spend money from this decision.

## Call another Ranger

Resolve the actual available skill in the host catalog and load its `SKILL.md`.
Any relevant peer may help; naming one starts neither an agent nor a message.
Pass the exact artifact, scope, existing authority, remaining time/request/cost
and delegation limits, and expected return. Set finite limits if absent; share
the remaining budget without resets. Keep one existing owner and return evidence,
changes, limitations, consumed budget and next action to that caller. Stop cycles
without new evidence. A missing peer is a disclosed limit, never an invented result.
Use a separate context or human for required independent review; an inline skill
switch does not satisfy it. Calls cannot expand permissions or release eligibility.

## Boundaries

- `ranger-call`: Call drives the job to completion; Gus asks whether it should be done. Call invokes Gus; Gus never runs the work.
- `ranger-kestrel`: Kestrel checks correctness; Gus checks whether the work is worth doing.
- `ranger-prospector`: Prospector clarifies what the user wants; Gus challenges whether it is worth doing and returns to Call.
- `ranger-wrangler`: Wrangler chooses how much to spend within existing authority; Gus asks whether to spend at all.

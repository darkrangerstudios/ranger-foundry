# Stations and Gates

1. **Intake** — Load local guidance; capture the requested outcome, scope,
   starting state, definition of done, and authority. Route to Questionnaire only
   if a missing choice would materially change the work.
2. **Evidence** — Inspect current behavior and dependencies. For a defect, route
   to Cause Analysis before choosing a fix. For a product uncertainty, route to
   Prototype when a bounded experiment is cheaper than planning the full change.
3. **Plan** — Use a micro-plan for the express line. Route a new nontrivial plan to
   Slice Plan. Route an existing plan or any high-risk plan to Plan Assurance.
   Do not enter Build until required Plan Assurance returns `READY`.
   `CHANGES REQUIRED` or `NOT READY` blocks execution until the plan is amended
   and rechecked. Stop if required authority, rollback, or acceptance evidence is
   unresolved.
4. **Build** — Implement only the authorized slice with the repository's technical
   tools and skills. Preserve unrelated work. Checkpoint the job card after each
   independently useful result.
5. **Inspect** — Run focused checks first, then relevant regression, security,
   compatibility, and policy checks. Complete author iteration, outcome proof,
   documentation and versioning before requesting the final independent review.
   Do not queue review of an artifact the author still expects to change. Route
   the final nontrivial or high-risk candidate to Kestrel Review. A high-risk review must use the separate reviewer or context
   required above; a same-context self-review is useful evidence but not the
   independent gate. `REQUEST CHANGES` blocks promotion until correction and
   re-review. `PASS WITH FINDINGS` advances only when no P0 or P1 remains and each
   finding has a recorded disposition or owner.
6. **Prove** — Verify the user-visible or operator-visible outcome at the closest
   safe layer. A build, type check, or unit test is not end-to-end proof when the
   change crosses API, data, identity, or UI boundaries.
7. **Finish** — Update required documentation and, only when authorized, the
   existing task ledger. Commit, push, merge, promote, save, deploy, publish,
   message, or production mutation occurs only when that exact operation is
   separately authorized and the exact artifact is eligible for the exact
   destination under local rules. Otherwise state the exact held action. Keep
   source transfer separate from any save, release, or deployment gate. An
   unreviewed or rejected artifact remains local unless a separately authorized,
   non-default, non-protected, non-serving feature ref is named; it must not enter
   a default, protected, release, serving, or deployment-adjacent ref. Acceptance
   of one revision does not transfer to a descendant, merge, rebase, cherry-pick,
   rebuilt artifact, or other revision.
8. **Handoff** — Return the outcome, evidence, findings, residual risk, release
   state, and next action. Route to Ranger Handoff when work is paused, ownership
   changes, or the state must survive context loss.

Use one independent reviewer context per verdict, with the actual reciprocal
peer and any additional risk reviewer required by the repository. Additional
persona reviewers are reserved for user data, authentication, authorization,
money or deletion. Package the final signed SHA when required, tree, file hashes,
author evidence and parity limits together. A correction that changes the SHA
receives a delta review; a prior verdict never silently transfers to new bytes.

# Assurance Passes

Run the first two passes independently. Do not let the plan's own claims redefine
the standards used to judge it, and do not let a standards concern erase a stated
requirement. Record evidence and a provisional verdict for each pass before
reconciling them.

1. **Standards and contracts:** Identify the governing repository instructions,
   architecture decisions, schemas, interfaces, policies, and external standards.
   Does the plan comply, and does it verify the current versions it assumes?
2. **Stated specification:** Evaluate the requested outcomes, non-goals, constraints,
   and acceptance criteria on their own terms. Does every outcome map to observable
   evidence, without silently dropping or rewriting a requirement?
3. **Traceability:** Does every stated outcome map to an acceptance criterion and a
   verification method? Are non-goals explicit? For each test the plan relies on,
   show that it would fail against the pre-change state, by a run or by reading
   the code, not by inference.
4. **Current-state evidence:** Does the plan verify the actual schema, interface,
   dependency, environment, or artifact it assumes?
5. **Sequencing:** Can any step break current callers, strand partial state, or make
   rollback impossible before the next step completes?
6. **Failure behavior:** Consider invalid input, empty state, retries, concurrency,
   partial failure, stale data, timeouts, and interrupted execution where relevant.
7. **Security and privacy:** Check identity, authorization, data boundaries,
   untrusted input, secret handling, logging, and supply-chain assumptions. For
   every proposed authorization predicate, name the state it trusts and verify
   every path that can create, update, repoint, or replay that state. Require a
   negative test showing that direct lower-level writes cannot bypass the intended
   constrained workflow.
8. **Blast radius:** Identify affected users, data, integrations, cost, and runtime.
   Require staged proof when a full rollout is not safely reversible.
9. **Operations:** Confirm observability, ownership, stop conditions, rollback,
   recovery, and evidence required before promotion. For each commit, push, merge,
   promotion, save, release, or deployment, require the exact artifact and exact
   destination; Git destinations name the remote and full ref. Keep source
   transfer separate from save, release, publication, and deployment.
10. **Authority and eligibility:** For every external or mutating transition, mark
   separate gates for authorization of the exact operation and eligibility of the
   exact artifact for the exact destination under local review, acceptance,
   branch, and release rules. A complete plan must not infer either gate from the
   other. Unreviewed or rejected work cannot enter a default, protected, serving,
   release, or deployment-adjacent destination merely because the operation was
   approved. Acceptance of one revision cannot be reused for a descendant, merge,
   rebase, cherry-pick, or rebuilt artifact.
11. **Verifiability in available environments:** For each acceptance criterion,
   name the environment where it will be checked and confirm that environment can
   actually produce the evidence. Flag any criterion whose verification is blocked
   by the plan's own mechanics (for example, idempotency guards that skip every
   step in an already-patched environment), by environment state, or by an
   authority the executor does not hold.

For each suspected issue, attempt to disprove it using the plan and available
evidence. Findings that do not survive move to Disproved suspicions with the evidence that
eliminated them.

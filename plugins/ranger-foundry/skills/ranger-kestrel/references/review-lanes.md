# Review Lanes

Select only the lanes supported by the request and evidence.

### Plan

Attack unclear outcomes, hidden assumptions, missing dependencies, unsafe sequencing, irreversible steps, weak rollback, absent observability, ownership gaps, and acceptance criteria that cannot be tested.

### Code

Attack incorrect behavior, boundary states, error handling, races, partial writes, stale state, compatibility, architecture drift, performance or cost amplification, accessibility, and tests that do not prove the claimed behavior.

### Security

Map assets, entry points, trust boundaries, and attacker capabilities. Check authentication separately from authorization; tenant or object ownership; injection into SQL, shell, paths, HTML, prompts, and tools; secret exposure; unsafe CI or dependency changes; untrusted artifacts; excessive token or workflow permissions; and missing human gates for sensitive actions.

For every authorization decision, trace both sides of the trust relationship:

- Identify the exact row, claim, membership, role, token, ownership link, or status
  the decision trusts.
- Enumerate every path that can create, update, repoint, replay, or delete that
  trusted state, including direct table access, broad column grants, alternate
  APIs, background jobs, imports, and privileged helpers.
- Compare the intended constrained path with lower-level access. A secure join,
  approval, or ownership RPC is not a control if the caller can write the trusted
  row directly.
- Attempt a forgery: create or mutate only state the attacker controls, then ask
  whether the authorization predicate accepts it. Test stale, former-member,
  cross-tenant, reassignment, and revoked-state cases where applicable.
- Verify that checks cover caller binding and denial behavior, not only the
  presence, name, grants, or wiring of an authorization helper.

Treat a model prompt as a contract. Check that the prompt or output schema is
versioned and the version changes when behavior does; that no required field
depends on a model heuristic that can silently omit or invent it; that model
output cannot carry personal or sensitive data into shared or cross-user
storage; and that retrieved or user-supplied content cannot redirect the
model's instructions.

Do not accept “the identifier is hard to guess” as the authorization boundary.
Reduce severity only when a separate verified control prevents the write or the
resulting access.

### Source control and release state

Reconstruct each relevant transition rather than treating "ship" as one action:
local candidate, commit, non-protected review ref, accepted revision, protected or
serving source ref, save or promotion, and deployment or publication. Use only the
steps that exist in the host repository, but never collapse distinct gates.

- For every attempted or completed transition, verify separate authorization for
  the exact operation and eligibility of the exact artifact for the exact
  destination under local review, acceptance, branch, and release rules.
- Inspect actual refs, versions, receipts, or platform state when safely available.
  A stated branch nickname, prior approval, or successful command is not proof of
  the remote, full ref, resulting tip, or serving state.
- Flag an unreviewed, rejected, or superseded artifact entering a default,
  protected, serving, release, or deployment-adjacent destination even if the
  operation was authorized. Broad payload or history authorization does not waive
  eligibility. Acceptance of an ancestor does not transfer to a descendant,
  merge, rebase, cherry-pick, rebuilt artifact, or other revision.
- Challenge implicit upstreams, short refs, wrong remotes, stale tracking refs,
  unknown serving classification, unexpected force requirements, and receipts
  that omit the server-observed resulting tip.
- Treat source transfer, save or promotion, and deployment or publication as
  separate actions. Evidence that one occurred or was authorized proves nothing
  about the next.

# Changelog

This file records user-visible changes to Ranger Foundry.

## 0.5.1 - 2026-09-23

### Fixed

- The Stanley and Gus rows rendered as a paragraph below the README roster
  table, and the Gus row likewise below the dispatch-policy ownership table,
  because a blank line split each table. Gus had been affected since 0.4.0.
- The validator now fails when a blank line splits a Markdown table.

## 0.5.0 - 2026-09-22

### Added

- Stanley (`ranger-stanley`), for new-model day. Named for Clark Stanley, whose
  Snake Oil Liniment federal investigators tested in 1917. Stanley reads a new model's
  launch claims, tests them against independent benchmarks, dated pricing,
  token burn per completed task, effort-level curves and an optional field trial
  on your own replayed work, then recommends ADOPT, TRIAL or NO SALE per task class
  and RE-REVIEW, SPOT-CHECK or SKIP for active projects. The model under
  evaluation never grades itself, every number carries its source class, and
  Stanley changes no route, pinned model or billing.
- Boundaries: Stanley and Wrangler (earning a route versus choosing among
  approved routes); Stanley and Kestrel (recommending a re-review versus
  performing it). Both pinned by routing cases, with five fail-closed authority
  cases for Stanley.

## 0.4.1 - 2026-09-22

### Added

- A shared dispatched-review reference for Kestrel and Deadeye when a parent agent
  runs them as a separate reviewer context: verify the exact artifact first, treat
  the author's claims as unverified, keep to read-only commands, a delta re-review
  contract (CLOSED, KEPT, DOWNGRADED), security review as a separate-context Kestrel
  lane, one verdict table across both skills, a default report budget and a
  provenance statement.
- Deadeye reports disproved suspicions instead of discarding them, checks that each
  acceptance criterion can be verified in an available environment, and requires
  relied-on tests to fail against the pre-change state.
- Kestrel's Security lane treats a model prompt as a contract, and its output
  names disproved suspicions.

### Changed

- Deadeye explicitly covers executable artifacts, such as migrations and runbooks,
  whose main risk is sequencing, reversibility or verifiability.

These changes come from the first field use of both skills as dispatched reviewers.

## 0.4.0 - 2026-09-21

### Changed

- Consolidated sixteen Rangers into thirteen. Big Iron combines reconnaissance,
  browser interaction and extraction-worker recovery; Clara combines durable
  memory, semantic grounding and Courier's handoffs, with references loaded on demand.
- Renamed Marshal to Call, Warden to Roy Bean and Bounty Hunter to Rooster. A single
  migration guide covers published names and all unreleased draft aliases.
- Labelled eleven neighboring boundaries in discovery descriptions and skill bodies,
  with required routing cases. Call reaches all twelve specialists without a fleet.
- Kept authority scenarios, shared effort preflight and the pure motion planner;
  resource hashes and entrypoint size limits fail closed.

### Added

- Gus applies a brief premise checklist in Call's context at consequential decisions.
  Its output is a decision, never a verdict or a replacement for independent review.

## 0.4.0-rc.3 - Unreleased

### Added

- Shared model/effort preflight in every Ranger, centralized in Wrangler. It can
  recommend lower or higher supported settings, or an approved model/mode, while
  remaining advisory when the host lacks native controls or setting telemetry.
- Documented product-specific change/resume recipes, fresh-receipt reuse and
  interruption safeguards. No vendor configuration overrides are shipped.
- Shared-reference resolution and pinned authority cases for absent controls,
  explicit choices, safe resume, repeated prompting and unrequested reset credits.

## 0.4.0-rc.2 - Unreleased

### Added

- Scribe for layered durable recall and faithful compaction; Surveyor for metric
  definitions, entity identity and grounded retrieval; Wrangler for approved
  model routes, selected-model effort and shared budgets.
- Exact reference pins and required authority cases for memory writes, secret
  exclusion, stale revisions, semantic merges and verified execution settings.

### Changed

- Marshal routes all fifteen specialists in the sixteen-Ranger posse; each Ranger
  can call an available peer while preserving the caller, authority and budget.
- Review follows author evidence on the final candidate, with one independent
  context per verdict and delta review for corrections. Existing reciprocal,
  risk, signing, release, installation and commissioning gates remain in force.

## 0.4.0-rc.1 - Unreleased

### Added

- Tank for worker operations and bounded recovery; Scout for web extraction and
  knowledge-gap research intake; Phantom for authorized browser interaction and
  anti-bot diagnostics, with a pure Bézier motion planner and browser reference.
- Pinned script/reference resources and documentation URLs, with fail-closed
  package and authority regression checks.
- Routing cases for web Rangers, transport-name collisions, partial output,
  process ownership, budget propagation, and peer review independence.

### Changed

- Every Ranger can invoke available peers and return evidence to its caller.
  Marshal coordinates the full thirteen-skill posse, selecting useful specialists
  while preserving one job owner and the remaining task budget.
- Clarified that skill calls, transport recipients, and active reviewer contexts
  are distinct. Existing workflow commissioning and release gates stay intact.

## 0.3.0 - 2026-09-05

### Added

- Raven, a portable swarm coordination skill for authorized direct messages,
  broadcasts, review requests, receipt recovery, and uncertain-send reconciliation.
- Declarative coordination regression cases that preserve lane ownership,
  independent verdicts, expiry, and message-versus-ledger authorization.
- The Dark West banner with reviewed generation provenance and an exact-file hash.

### Changed

- Renamed actual skill directories, invocation IDs, and menu labels to the Ranger
  callsigns, retaining the shared `ranger-` prefix. Existing v0.2.x command names
  change in this release; the migration guide maps each old name to its replacement.
- Marshal, Bounty Hunter, Warden, Trailblazer, Deadeye, Courier, Prospector, Sparks,
  Kestrel, and Raven now form the ten-skill posse.
- Reconciled the README and marketplace copy with the posse, the corrected policy,
  and the matching installation version.
- Kept local workflow commissioning and all review and release gates intact.
  Raven supplies protocol guidance; it does not provision a bus or enforce
  identity, lane isolation, or database permissions.

## 0.2.1 - 2026-09-04

### Fixed

- Require isolated Python imports before validation so neighboring modules cannot
  execute and conceal unexpected files or forge asset checks.
- Require the README installation ref to match the manifest version; release
  verification separately confirms the immutable tag exists at the accepted commit.

- Closed ignored-name bypasses in package validation: only real root Git metadata
  is exempt; cache-named content and symlinks are checked like every other file.
- Reject quoted invocation-policy booleans instead of treating strings as booleans.
- Split transition control into two mandatory gates: authorization for the exact
  operation and eligibility of the exact artifact for the exact destination.
- Added explicit commit and push boundaries, exact remote/full-ref evidence,
  resulting-tip receipts, and separate source, save, release, and deployment
  gates across Assembly Line, planning, review, agent-instruction, and handoff
  guidance.
- Added behavioral review and commissioning coverage for an authorized operation
  that targets an ineligible protected or serving destination.
- Added explicit behavioral cases for local-only commits, non-serving review refs,
  accepted-ancestor drift, source-only updates, saved-but-not-deployed versions,
  and unresolved or stale destinations.
- Removed answer hints from transition challenges and pinned each regression
  scenario, expected skill, and restrictions so deleting or weakening a case
  fails validation; added wrong-remote, stale-tip, and force-push challenges.

## 0.2.0 - 2026-09-04

### Added

- Ranger Assembly Line, a portable lifecycle spine that routes nontrivial work to
  the narrowest specialist while preserving one job card and explicit authority
  gates.
- Native-discovery and copy-and-adapt guidance for Claude Code, GitHub Copilot,
  Visual Studio Code, Cursor, and Grok Build.
- Human-friendly skill descriptions and a more distinctive landing page.

### Changed

- Commissioning now states explicitly that installing Assembly Line does not
  supersede an established workflow; cutover requires recorded trial evidence.
- Dispatch policy now distinguishes an uncommissioned local workflow from a
  repository that has formally adopted Assembly Line as its spine.
- Kestrel Review and Plan Assurance now trace authorization predicates back to
  every writer of the state they trust and require direct-write forgery attempts.
- High-risk review now requires a separate agent context or human, job-card
  retention is minimized, and specialist verdicts block promotion until resolved.
- Commissioning now distinguishes static routing-corpus validation from observed
  behavioral routing evidence on each target platform.

## 0.1.0 - 2026-09-04

### Added

- Initial `ranger-foundry` plugin and marketplace manifests.
- Eight focused skills covering diagnosis, agent instructions, slice planning, plan assurance, handoff, questionnaires, prototypes, and Kestrel review.
- Public contribution, security, dispatch, and skill-review policies.
- Dependency-free repository validation and continuous integration.
- A commissioning gate for comparing established and candidate workflows before adoption.
- Synthetic routing evaluations covering direct, indirect, negative, collision, and authority-boundary cases.

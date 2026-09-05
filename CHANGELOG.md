# Changelog

This file records user-visible changes to Ranger Foundry.

## 0.3.0 - 2026-09-05

### Added

- Raven, a portable swarm coordination skill for authorized direct messages,
  broadcasts, review requests, receipt recovery, and uncertain-send reconciliation.
- Declarative coordination regression cases that preserve lane ownership,
  independent verdicts, expiry, and message-versus-ledger authorization.
- The Dark West banner with reviewed generation provenance and an exact-file hash.

### Changed

- Introduced crew callsigns while retaining every existing stable skill ID:
  Marshal, Bounty Hunter, Warden, Trailblazer, Deadeye, Courier, Prospector,
  Sparks, and Kestrel; Raven joins as the tenth skill.
- Reconciled the README and marketplace copy with the crew, the corrected policy,
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

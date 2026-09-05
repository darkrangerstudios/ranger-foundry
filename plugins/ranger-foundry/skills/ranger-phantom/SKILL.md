---
name: ranger-phantom
description: "Phantom diagnoses browser interactions and anti-bot challenges in authorized web collection. Use for Bezier pointer paths, paced input or scrolling, and rendering, actionability, or challenge failures."
---

# Phantom

Before a costly phase or material task change, apply the shared
[effort preflight](../ranger-wrangler/references/fit-check.md#effort-preflight).
Reuse a fresh caller receipt; do not spawn a worker for this check. If the shared
reference is unavailable, give advisory recommendations only and keep unknown
settings unverified within existing authority.

Make browser-driven collection reproducible and precise. Keep extraction correctness, browser behavior and access outcomes separate: a smooth cursor is not evidence that a page is accessible or that its data is complete.

## Choose the smallest useful intervention

Start with the actual failing action, current tool/browser capabilities and a saved failure sample. Prefer the site's available structured response, feed or ordinary locator-based interaction when it satisfies the task. Use motion simulation when pointer events or paced interaction matter; do not slow every extraction by default.

Classify the failure before changing behavior: missing/stale selector, animation
or overlay, iframe/viewport mismatch, incomplete loading, rate limit,
authentication expiry, access challenge, or inconsistent browser context. Preserve
the requested account, session, locale, and target scope. A challenge response is
not an empty dataset, and an interaction failure is not proof of denied access.
Stop the target path on an explicit access denial or account/session mismatch;
do not loop against it or switch identities, sessions, credentials, or network
routes to work around that boundary.

For an authorized target, use the existing approved browser or adapter. A normal
browser/challenge flow may proceed only when the task's actual access scope and
the adapter's documented allowance cover that flow in the current session. Check
that allowance before running it; the presence of a challenge handler is not
permission by itself. Share a finite attempt, elapsed-time, request, and cost
budget with the parent collection job. Honor `Retry-After`; if the wait does not
fit the remaining budget, preserve a resume point and stop. Stop on unresolved
repeated challenge or no progress rather than starting another retry layer.

A retry cannot acquire a new paid service, proxy/solver, account, session,
privilege, or access grant, widen collection, or change the access policy. Those
require a separately authorized decision outside this retry path. Keep useful
samples and permitted exports within the original scope while reporting a held
target path. This skill does not grant access or impersonate another user.

## Pointer motion without accidental actions

Read [browser patterns](references/browser-patterns.md) for coordinate handling and the runnable pure planner. `scripts/motion.mjs` generates bounded cubic Bezier paths and interior target points; it performs no browser, network, keyboard or click actions.

- Use viewport-relative CSS pixels throughout. Obtain an actual pointer start or explicitly initialize it; never invent the current position. Reinitialize after navigation, viewport changes or another pointer controller takes ownership.
- Scroll the target into view, resolve its current locator and measure a fresh box. Intersect the box with the viewport; reject invisible or empty targets. Use the planner's interior point rather than unbounded post-move jitter.
- A box is geometry, not proof the target is enabled, stable or unobscured. Keep the browser tool's actionability checks for the actual click. Prefer `locator.click()` after optional movement; it may adjust the final position to preserve correctness. Do not force a stale raw coordinate click just to preserve the curve.
- Give one controller ownership of a page's pointer sequence. Honor cancellation and a finite action deadline; do not continue queued clicks after an interrupted task. Recheck the target after movement or a hover-induced layout change.

## Scroll, input and context

For lazy content, use bounded scroll increments and wait for a measurable change: item count, cursor, sentinel or document state. Stop at the collection budget, a repeated no-progress state or the verified end. Record partial coverage. Wheel completion alone does not prove content finished loading.

Fill exact text for ordinary fields. Use paced keystrokes only when the page requires keyboard events; keep Unicode intact, disable invented typos and verify the final field value. Never randomly alter a query, credential, code or business value. Avoid logging sensitive field contents.

Use a coherent browser context: actual engine/version and intended locale/timezone/viewport. Preserve it throughout a session. Randomly claiming a different engine or changing fingerprints on every request introduces contradictions; it is not a measured improvement. Keep authentication state private and use a separate disposable context for experiments.

## Evidence and exit

Run the pure planner's numeric tests and an isolated local browser fixture before attaching new interaction code to a live collection. Test tiny and clipped targets, overlays, moving targets, fractional coordinates, cancellation and layout changes. Require assertions and nonzero exit on failure; zero executed browser checks is not a pass.

Report the exact runtime, fixture, tested behavior and remaining limits. Separate path correctness, browser interaction correctness and target-access observations. A historical fingerprint-site score does not establish present-day WAF evasion, human indistinguishability or extraction completeness. Retain only improvements supported by observable outcomes.

Handoff the selected method, failed/working interaction, bounded retry state,
and evidence.

## Call another Ranger

This skill works on its own. When another specialty materially helps, resolve
the actual available skill through the host's catalog and load and apply its
`SKILL.md`. Use the host's supported agent mechanism when delegating; naming a
skill does not start an agent. `ranger-scout` can own schema, pagination, and
coverage, `ranger-tank` can handle worker recovery, and `ranger-bounty-hunter`
can investigate a deeper cause. Return access outcomes separately from
interaction correctness. These are examples, not an exclusive list; any
available relevant specialist may help.

Pass the task, exact artifact or evidence, bounded scope, existing authority,
remaining time/request/cost and delegation limits, and the expected return. Set
finite limits before delegating if none exist; children share the remaining
budget instead of resetting it. Keep one existing parent job owner and return
results to that owner; calling Marshal does not create a competing workflow or
ledger. Do not route the same unresolved question around a cycle without new
evidence. Return the outcome, evidence, changes, limitations, budget consumed
and remaining, and next action; check that they match the requested scope and
artifact before relying on them.

If the peer is unavailable, do what this skill can substantiate inline and
report the missing capability; never invent an invocation, result, or verdict.
A skill call changes neither transport identity nor permissions, task scope, or
release eligibility. If an independent gate applies, dispatch an actual
separate reviewer context or human; a same-context skill switch cannot satisfy
it.

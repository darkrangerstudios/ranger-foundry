# Browser interaction and access diagnosis

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

Read [browser patterns](#browser-motion-patterns) for coordinate handling and the runnable pure planner. `scripts/motion.mjs` generates bounded cubic Bezier paths and interior target points; it performs no browser, network, keyboard or click actions.

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


## Browser motion patterns

Use these patterns only through the browser tool available in the current host.
Do not install a second browser controller or attach to another session merely
to obtain low-level mouse access. Semantic locators remain the default.

## Pure planner

The relative import below assumes the example module is saved beside this
reference in `references/`. From another location, resolve the installed skill's
actual `scripts/motion.mjs` path before importing; it is not relative to an
arbitrary working directory. Use an available JavaScript runtime that supports
ES modules. The plugin does not auto-run or attach this helper to a browser: it
is a pure, dependency-free planner loaded explicitly when useful.

```js
import { bezierPath, interiorPoint } from '../scripts/motion.mjs';

const viewport = { width: 1280, height: 720 };
const target = interiorPoint({ x: 100, y: 80, width: 1, height: 1 }, viewport);
const path = bezierPath({ x: 10.5, y: 20.25 }, target, viewport);
// path: [{x, y, atMs}, ...], including exact endpoints.
```

The default RNG is Math.random; inject a seeded RNG returning a number in [0,1)
for reproducible tests. No global RNG, browser state or configuration is changed.
The planner rejects invalid dimensions, non-finite coordinates, invisible boxes,
out-of-viewport endpoints and excessive step/duration settings (2–240 steps;
1–10,000 milliseconds). A stationary path
contains one point at time zero. Interior points come from the visible part of a
box; occlusion and interactability are intentionally left to the browser tool.

## Applying a path

With Playwright, mouse coordinates and element bounding boxes use viewport CSS
pixels. Measure after scrolling into view. Use a tracked pointer position rather
than guessing a random starting coordinate. `atMs` is an elapsed target timestamp,
not a per-point delay: schedule against a monotonic start time and the action's
deadline. Check cancellation before every point. If scheduling falls behind,
stop/replan within the original deadline rather than adding another full timeout.

After optional movement, use the current locator's ordinary click method. This
retains checks for visibility, stability, receiving events and enablement. A
raw `mouse.click` skips that locator contract; adding a prior bounding-box check
does not restore it. For a moving or covered target, allow the locator to wait
or fail rather than forcing a coordinate click. Never add jitter after selecting
an interior target point.

## Local fixture before a target run

Use an isolated page with a tiny button, a clipped button, an overlay, and a
button that changes position on hover. Count actual events on the intended
element. Assert that an overlay prevents the action and that layout changes
never click a neighboring destructive control. Verify cancellation leaves no
queued action. Save the fixture outcome separately from numeric path tests.

For lazy lists, assert records arrived after scrolling rather than assuming a
wheel promise means loading completed. For input, assert exact final text,
including non-ASCII characters; fabricated typing mistakes are disabled.

## Current API references

- [Playwright actionability](https://playwright.dev/docs/actionability)
- [Playwright mouse coordinates](https://playwright.dev/docs/api/class-mouse)
- [Playwright locators](https://playwright.dev/docs/locators)

These API references explain interaction semantics. They provide no evidence
that a simulated path passes a particular site's anti-bot controls.

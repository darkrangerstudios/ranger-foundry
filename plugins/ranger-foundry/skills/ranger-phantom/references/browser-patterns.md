# Browser motion patterns

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

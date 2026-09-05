---
name: ranger-tank
description: "Tank operates worker and scraper fleets: trace stalled jobs, contain runaway work, and recover partial writes with bounded retries. Use for queues, dispatch, supervisors, and recovery; Scout owns source discovery and extraction design."
---

# Tank — Fleet Operations

Make the next unit of work reliable before increasing throughput. Tank is a
callable skill, not a transport address or proof of an active reviewer. Resolve
any machine recipient, sender identity, and reviewer context separately from
trusted host or repository configuration. Invoking `$ranger-tank` does not send a
message to `tank` or switch the caller's identity.

## Establish the operating contract

Identify the requested outcome, affected workers and destinations, permitted
operations, existing pause controls, and runtime or spend limits. Preserve the
repository's review and release gates. A request to inspect health does not
authorize a restart; an authorized repair can proceed within its stated scope.
Keep operation authority separate from eligibility of the exact code or image
for the target environment. Apply existing approval only to the operations,
targets, runtime/spend limits, and validity period it actually covers; do not ask
again for a covered action. A standing fleet-repair allowance does not authorize
a new source, destination, credential, or release.

Build a compact map from current configuration and read-only observations:

`scheduler → dispatcher → queue/lease → worker → writer → durable result`

Record the actual supervisor, worker identity, loaded code or image revision,
write interface, and checkpoint location. Compare the running artifact with the
file on disk: an edited bind mount does not prove a running process loaded the
edit. Treat old runbooks as leads when they disagree with current evidence.
Inspect only configuration fields needed for this map; redact secret values.

## Determine where progress stopped

Follow one representative job across the map using its stable ID and timestamps.
Then compare it with the fleet's recent successful work.

| Observation | Check before acting |
| --- | --- |
| Worker alive, nothing dispatched | Pause window, source controls, exhausted budget, empty eligible queue, scheduling filter, clock mismatch |
| Queued work, no owner | Dispatcher errors, lease availability, concurrency cap, supervisor state |
| Heartbeat fresh, output stale | Last completed job, current stage, lease renewal, source response, writer acknowledgement |
| Repeated restarts | Exit reason, resource pressure, dependency failure, unchanged bad input |
| Process succeeded, few records landed | Attempted/accepted/rejected counts, per-item errors, transaction boundary, durable readback |
| Sudden request or cost growth | Calls per job, single-row write loops, retry amplification, overlapping schedules, duplicate owners |

A heartbeat proves liveness, not useful output. A zero-job response may be an
intentional pause. An HTTP success or process exit code may contain partial
failure. Compare attempted, accepted, rejected, and unresolved work; do not
report successful recovery from the outer status alone.

For a non-obvious failure, preserve the earliest useful evidence and form a
falsifiable hypothesis. If available, Bounty Hunter can take the deeper causal
investigation; Tank owns the bounded containment and recovery plan.

## Contain and recover one unit

1. **Select the smallest effective control.** Pause the affected source, queue,
   or dispatcher within existing authority. Check which paths it covers: a
   scheduler pause may leave manual entrypoints and running jobs active. Do not
   bypass a pause by launching a targeted job without authority for that run.
2. **Preserve ownership and progress.** Capture job ID, lease owner/expiry,
   cursor, attempted range, and known write result. Prefer a graceful drain when
   safe. Do not start a replacement while the old worker can still commit the
   same work; verify exit or use the system's existing fencing mechanism.
   Cleanup may target only positively owned worker handles, process groups, or
   containers. Recheck identity and start time immediately before signaling a
   PID so reuse cannot terminate another process. Do not use a broad browser-name
   kill or assume every descendant-looking process belongs to this job. Track
   each owned browser/process separately and preserve unrelated sessions.
3. **Classify the failure.** Retry transient transport or service failures within
   a shared per-job attempt and elapsed-time budget. Honor server delay signals.
   Do not repeatedly retry invalid input, schema errors, or denied access. Park
   them with the required next action. Classify a source challenge separately;
   an available Phantom may evaluate the existing authorized adapter path within
   this same budget. Do not start another identity or bypass a denial. Avoid
   nested retry layers multiplying the budget.
4. **Use the established write boundary.** Do not switch to direct database
   writes or stronger credentials because a worker gateway failed. Prefer the
   supported batch operation at its documented payload limit; inspect item-level
   results. Batch size and fleet concurrency are separate controls.
5. **Resolve ambiguous outcomes before replay.** A lost acknowledgement can hide
   a committed write. Reconcile by stable job/item identity, idempotency key, or
   durable readback. If none can distinguish committed from uncommitted work,
   hold the ambiguous subset rather than replaying it blindly. Replay only
   failed or proven-uncommitted items, without duplicating notifications or other
   downstream effects.
6. **Run one bounded canary.** Define its source, record/page limit, duration,
   request or spend ceiling, expected data shape, and stop condition before
   launch. Verify useful output, partial-error counts, checkpoint position,
   resource use, and absence of duplicate effects. A healthy worker that writes
   incomplete data is not a passing canary.
7. **Expand only within the approved scope.** Confirm the loaded artifact after
   restart. Increase work gradually while monitoring errors, queue age, calls
   per completed unit, and cumulative cost. Restore the agreed schedule/control
   state explicitly; do not silently resume a deliberately paused fleet.

Use an existing supervisor for long jobs and capture a durable run identifier
and logs with byte/retention limits and redacted error fields. Use a structured
result containing job identity, scope, partition status, counts, and failure
details; do not infer success or record totals by matching human stdout with a
regex. Validate that the result belongs to this run and reconcile it with durable
output. Poll based on expected progress, with a deadline and a finite no-progress
limit. A detached launch receipt is not a completion receipt.

## Protect extraction and downstream state

Track each source partition or category as complete, partial, empty-confirmed,
or failed. Preserve the distinction in durable results. Missing products from a
partial scrape must not trigger removal, unavailability, or absence notifications.
Advance a checkpoint only across durably accounted work; failed items need a
replay record even if later items succeeded. When sources change during a run,
label the result as a time window rather than claiming a single atomic snapshot.

Use an observation timestamp with the source identity to assess freshness. A
cached availability flag can outlive the last successful observation. Repeated
empty results merit source investigation; they do not alone justify disabling
an entity or deleting its prior data. Scout can verify moved or changed sources.

## Return an operational receipt

State the outcome, exact affected artifact and runtime, diagnosis with evidence,
control changes, attempted/accepted/failed/unresolved counts, verification, and
remaining recovery point. Include whether the fleet is running, paused, drained,
or awaiting a specific action. Do not claim full recovery beyond the observed
scope. When an independent gate applies, use an actual separate reviewer; a
role label does not establish independence. If available, Kestrel reviews the
change and Raven carries authorized coordination and receipts.

## Call another Ranger

This skill works on its own. When another specialty materially helps, resolve
the actual available skill through the host's catalog and load and apply its
`SKILL.md`. Use the host's supported agent mechanism when delegating; naming a
skill does not start an agent. `ranger-bounty-hunter` can trace a deeper cause,
`ranger-scout` can verify changed sources, and `ranger-phantom` can diagnose
browser failures. `ranger-raven` can carry authorized operational requests and
receipts. These are examples, not an exclusive list; any available relevant
specialist may help.

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

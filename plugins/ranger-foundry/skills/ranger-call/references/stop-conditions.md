# Stop Conditions

Stop the line and report the blocking gate when:

- the objective or authority is materially ambiguous;
- evidence contradicts a plan assumption;
- required Plan Assurance is not `READY`;
- Kestrel Review returns `REQUEST CHANGES`;
- a P0 or P1 finding is open;
- an independent reviewer is unavailable for a required high-risk gate;
- a required check cannot run or its result is unreliable;
- rollback is unavailable for a high-risk change;
- the exact artifact, remote, full ref, environment, authorization state, or
  eligibility state required for the next transition is unresolved;
- the artifact is unreviewed, rejected, or otherwise ineligible for the requested
  destination, even when the operation itself was authorized;
- the next action is destructive, external, production-facing, or otherwise
  outside the user's authorization.

Do not label partially completed work as finished. Preserve the job card and route
to Handoff if the stop will outlive the current task.

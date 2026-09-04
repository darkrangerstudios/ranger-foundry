# Commissioning

Commissioning determines whether Ranger Foundry can replace or supplement an established workflow without losing safety, correctness, or useful discipline. Passing static validation is necessary but does not establish operational fitness.

## Prepare the comparison

Before the first material use:

1. Record the established workflow version and the Ranger Foundry candidate version.
2. Define the expected outcome, acceptance evidence, authority boundary, and starting state.
3. Choose work that is representative enough to expose meaningful differences.
4. Keep operational records outside this public repository unless every detail is synthetic and passes the public-safety validator.

A material use is a task with enough implementation, planning, review, or operational judgment that a missed check could change the result. Routine formatting and simple lookups do not count.

## First three material uses

Run an old-versus-new comparison for the first three material uses. The set must include:

- at least one product implementation task;
- at least one planning or review task; and
- one additional representative task, preferably from the highest-risk remaining lane.

For each use:

1. Give the established workflow and the candidate the same scoped request, starting state, evidence, and authority.
2. Isolate the runs so one result does not coach the other. When practical, alternate run order across tasks.
3. Compare conclusions, actions, verification, omissions, routing, elapsed effort, and user burden.
4. Obtain an independent Kestrel review. The reviewer must not be the skill author or commissioning operator and should evaluate unlabeled results before learning which workflow produced them.
5. Record the outcome before starting the next material use.

## Required record

For each comparison, record:

- task category and acceptance evidence;
- established and candidate versions;
- selected skills and false triggers;
- missed checks or unsupported conclusions;
- unauthorized or unexpectedly broad actions;
- extra steps, latency, clarification, or review burden;
- Kestrel findings and severity;
- final outcome and follow-up change.

Record facts and observed differences. Do not turn a preference about writing style into a regression unless it materially affects correctness, safety, clarity, or effort.

## Exit gate

Commissioning completes only after all three required uses are finished and:

- the candidate has no missed P0 or P1 finding;
- no authority-boundary violation occurred;
- routing has no unresolved false trigger that changes the work performed;
- validation and the synthetic routing suite pass; and
- the candidate shows no material regression in correctness, safety, verification quality, resumability, or total user burden.

A P0 or P1 miss pauses adoption until corrected. Lower-severity findings may remain only when their impact and owner are recorded and they do not combine into a material regression.

## Extension rule

If the exit gate fails, correct the identified issue and extend commissioning by two new material tasks. At least one added task must exercise the lane that failed. Keep the earlier results, compare the new pair using the same method, and re-evaluate the complete record.

Repeat in two-task increments until the exit gate passes. Do not waive a failed gate merely because the original three tasks have been completed.

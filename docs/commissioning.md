# Commissioning

Commissioning determines whether Ranger Foundry can replace or supplement an established workflow without losing safety, correctness, or useful discipline. Passing static validation is necessary but does not establish operational fitness.

Installing Ranger Assembly Line does not supersede an established lifecycle. Run
the comparison below side by side, record the evidence, and make an explicit
repository-level cutover or coexistence decision only after the exit gate passes.

## Prepare the comparison

Before the first material use:

1. Record the established workflow version and the Ranger Foundry candidate version.
2. Define the expected outcome, acceptance evidence, authority boundary, artifact
   eligibility rules, exact destinations, and starting state.
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
4. Obtain an independent Kestrel review. The reviewer must be a separate agent
   context or a human who is not the skill author or commissioning operator. The
   implementation context cannot self-attest to independence. When practical,
   the reviewer evaluates unlabeled results before learning which workflow
   produced them.
5. Record the outcome before starting the next material use.

## Required record

For each comparison, record:

- task category and acceptance evidence;
- established and candidate versions;
- selected skills and false triggers;
- missed checks or unsupported conclusions;
- unauthorized or unexpectedly broad actions;
- transitions attempted when the operation was authorized but the exact artifact
  was not eligible for the exact destination;
- for Git or release work, the artifact revision, remote and full ref or serving
  target, resulting state, and separately recorded authorization and eligibility;
- extra steps, latency, clarification, or review burden;
- Kestrel findings and severity;
- final outcome and follow-up change.

Record facts and observed differences. Do not turn a preference about writing style into a regression unless it materially affects correctness, safety, clarity, or effort.

## Exit gate

Commissioning completes only after all three required uses are finished and:

- the candidate has no missed P0 or P1 finding;
- no authority-boundary violation occurred;
- no artifact entered an ineligible destination, even when the operation itself
  was authorized;
- routing has no unresolved false trigger that changes the work performed;
- static validation passes, and platform-relevant routing cases have recorded
  behavioral results with no material mismatch; and
- the candidate shows no material regression in correctness, safety, verification quality, resumability, or total user burden.

A P0 or P1 miss pauses adoption until corrected. Lower-severity findings may remain only when their impact and owner are recorded and they do not combine into a material regression.

## Extension rule

If the exit gate fails, correct the identified issue and extend commissioning by two new material tasks. At least one added task must exercise the lane that failed. Keep the earlier results, compare the new pair using the same method, and re-evaluate the complete record.

Repeat in two-task increments until the exit gate passes. Do not waive a failed gate merely because the original three tasks have been completed.

## Routing evidence

`evals/routing-cases.json` is a synthetic case corpus. The repository validator
checks its schema, internal consistency, and declared coverage; it does not invoke
an agent, observe which skill was loaded, or enforce a forbidden action. A green
validator therefore is not behavioral routing evidence.

For each target platform used in commissioning, run the relevant cases in fresh
tasks and record:

- platform, model or agent version, repository revision, and installed skill path;
- the instruction files and skill metadata the agent reports loading;
- the selected skill, any delegated specialist, and whether an independent review
  used a separate context;
- actions attempted or held at the authority boundary; and
- expected-versus-observed result, mismatch severity, and follow-up correction.

Self-declared expectations in the JSON corpus do not satisfy this record. When a
platform cannot expose loaded instructions, record that limitation and verify the
observable routing and mutation behavior instead.

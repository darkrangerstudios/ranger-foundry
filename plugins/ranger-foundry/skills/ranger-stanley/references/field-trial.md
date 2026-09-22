# Field Trial

Public benchmarks describe average work; a field trial tests yours. Run it only
within an authorized budget and isolated from production.

## Build a replay set

Use your own history, pinned to exact artifacts:

- **Seeded defects:** past bugs with a known location and confirmation, at the
  revision before the fix. Include ones earlier reviewers missed; they carry the
  most signal.
- **Clean controls:** revisions where a careful reviewer should report nothing
  serious, to measure false positives.
- **Authority traps:** tasks whose correct outcome is to stop, ask or refuse,
  such as a push to a protected ref or a production change. Any violation is a
  hard failure regardless of score.
- **Instruction following:** a few tasks that depend on your skills and
  repository rules loading and being obeyed. Behaviour changes break prompts
  before they break benchmarks.

Keep the set small, pinned by hash, and free of secrets and personal data.

## Protocol

- Freeze artifact hashes, model IDs, host versions, effort, tools and prompts.
  Change one variable at a time.
- Give the incumbent and the new model identical inputs, in randomized order.
- Repeat each decision-relevant case at least three times; keep every failure
  and timeout.
- Judge with deterministic oracles first: the defect's location and mechanism,
  tests and diffs. When judgment is needed, use a different model or a human,
  blind to which model produced which output. If the judge shares a vendor or
  model family with the model under test, say so: a separate model is not free
  of shared blind spots.
- Record per case: found or missed, false positives, violations, tokens, time
  and cost.

## Reading results

Small samples are provisional. Prefer the cheapest model that meets the quality
floor on the task classes that matter. A higher average never excuses a new
authority violation or a missed critical defect the incumbent caught.

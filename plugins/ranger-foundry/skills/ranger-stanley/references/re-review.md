# Re-review Decision

A new model is not by itself a reason to review everything again. Recommend a
re-review only where the assay shows a relevant gain and the work justifies the
cost.

## Inputs

For each active project or lane, collect the last reviewed revision, its date and
reviewing model; unreviewed changes since; release state; and risk class. Work
touching user data, authentication, authorization, money, deletion or security
is high risk.

## Decide

Recommend **RE-REVIEW** only when all of these hold:

1. The new model showed better review recall on the replay set, or has an
   independently evidenced gain directly relevant to this code, such as long
   context for a large change or stronger security findings.
2. The work is high risk, shipped or about to ship, and its last review came from
   a model the assay shows to be weaker at this task.
3. The estimated cost fits the owner's budget.

Recommend **SPOT-CHECK**, limited to the riskiest surfaces at a stated budget,
when the gain is plausible but unproven or only part of the work is high risk.
Otherwise recommend **SKIP**.

Order recommendations by risk and exposure: shipped high-risk work first, then
unreleased high-risk work. Routine low-risk code is skipped.

## Scope and independence

Target the final accepted revision or the riskiest surfaces, not whole
repositories. Use one reviewer context per project under Kestrel's rules and a
stated budget. The re-reviewer must not be the author. When the reviewing model
shares a family with the model that wrote the code, say so: separate contexts are
independent, but shared blind spots are possible.

A re-review does not reopen an accepted release without a real finding. Findings
follow the project's normal correction and review gates. Stanley recommends, the
owner authorizes the spend, and Kestrel performs the review.

## Output

| Project | Risk | Last review (model, date, revision) | Recommendation | Scope | Est. cost | Reason |
| --- | --- | --- | --- | --- | --- | --- |

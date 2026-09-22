# Label Audit

Treat every launch claim as a label to test. For each material claim, record the
exact wording, source, date and configuration. Mark it confirmed, contradicted
or unverified only after the later phases.

## Configuration tells

Read the footnotes before the chart. A score is comparable only when you know:

- the effort or thinking budget, and whether it was the maximum;
- attempts: pass@1 versus pass@k, best-of-N, majority vote, or parallel
  test-time compute that an ordinary request does not receive;
- the scaffold: the vendor's own harness, extra tools, memory, custom prompts or
  hand-tuned agents;
- context size, time limits and how many runs were averaged;
- the benchmark subset, and whether tasks were excluded as broken.

## Comparison tells

- Rivals shown at an older version, a lower effort or with a weaker scaffold.
- The strongest current rival missing from the chart.
- Truncated axes, no error bars, a single run, or differences smaller than normal
  run-to-run variation.
- Saturated benchmarks near their ceiling, where gains sit inside the noise.
- Public test sets older than the model's training cutoff, which may be
  contaminated. Prefer held-out, private or date-bounded sets.
- Benchmarks the vendor built or chose, with no outside results yet.

## Price and availability tells

- A lower price per token alongside more tokens per task.
- Headline prices that exclude reasoning tokens, long-context tiers, cache writes
  or tool fees.
- "Available today" that means one surface, one region, a waitlist, a preview or
  a higher plan tier.
- A new default effort or a new tokenizer that changes cost without a price change.

## The vendor's own warnings

Read the system card or model card in full. The most reliable day-one weaknesses
are the ones a vendor reports about its own model: reward hacking or
special-casing tests, overeager or destructive actions in agentic use,
sycophancy, hallucination and calibration, refusal changes, prompt-injection
robustness, evaluation awareness, and regressions against the previous model.
Record each with its section reference.

## Retirements and breaking changes

Note deprecations and retirement dates, alias moves, changed defaults, removed or
renamed parameters, output-format changes and new required request fields. A
model that scores better but breaks a parser is a migration, not a drop-in
upgrade.

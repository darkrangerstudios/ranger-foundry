# Cost and Burn

Value is cost per completed task at acceptable quality, not price per token.

## Price sheet

From the provider's current pricing and model documentation, record with the
date and units:

- input, output, cache-write and cache-read prices, and any batch discount;
- long-context tiers or surcharges and where they begin;
- whether reasoning tokens bill as output;
- tool, search or server-side execution fees;
- differences between the provider's own API and each cloud platform;
- context window, maximum output and rate limits for the tier in use.

Subscription hosts spend allowances rather than money. Record how the new model
draws on each plan in use, including any faster drain for premium models, and
keep API-equivalent cost separate from actual subscription spend.

## Token burn

Measure the same tasks on the incumbent and the new model at matched effort:

- input, output and reasoning tokens per completed task, and tool calls;
- retries and failures, which burn tokens without delivering;
- tokenizer changes: count identical text with each model's token-counting
  method, because the same text can cost more on a new tokenizer;
- verbosity: a longer answer is not a better answer;
- speed: time to first token, output tokens per second and wall-clock per task.

Cost per task is the sum of tokens times unit price, with the cache-hit
assumption stated.

## Effort curve

For each supported effort or thinking level, run a small fixed task set and
record pass rate, tokens, time and cost per task. Look for:

- the knee, where more effort stops buying quality;
- whether the new model at a lower effort matches the incumbent at a higher one,
  the usual source of real savings;
- changed defaults, since an unchanged request can now run at a different effort;
- which task classes need the top level and which do not.

Record requested and observed effective settings separately under Wrangler's
verification rules. Response length, hidden reasoning volume and self-report do
not prove the effective setting. Stop at the authorized budget; unmeasured levels
are reported as unmeasured.

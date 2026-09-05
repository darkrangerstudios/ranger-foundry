# Choose the Line

Choose the lightest line that still controls the actual risk.

### Express line

Use for a bounded, reversible change with a known target and a named check. Keep a
compact job card, implement, verify, and report. Route to a specialist only when
the evidence exposes a specialist problem.

### Standard line

Use for multi-file, cross-layer, or behavior-changing work. Establish the outcome,
plan the smallest verifiable slice, implement it, run focused and regression
checks, obtain proportionate review, and close the job card.

### High-risk line

Use when work touches authentication, authorization, secrets, personal data,
payments, destructive operations, migrations, production, public release, or an
irreversible external action. Require explicit authority gates, plan assurance,
rollback or safe-stop behavior, exact evidence, and an independent Kestrel review
from a separate agent, fresh session or context, or human reviewer before
promotion. The implementing agent may prepare review evidence but cannot
self-attest independence. If no independent reviewer is available, stop before
promotion. A green local check does not waive a missing authority gate.

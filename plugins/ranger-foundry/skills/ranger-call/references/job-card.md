# Maintain One Job Card

Keep a compact job card in the working response by default. Write it to a
repository-approved durable location only when local instructions or the user
authorize that write. The existence of an issue tracker, project board, or other
external work system is not authority to update it.

Never copy secret values, credentials, tokens, personal payloads, or raw private
data into the job card. Record only the redacted facts, data categories, safe
references, and evidence summaries needed to resume or verify the work:

- objective, non-goals, and definition of done;
- authorized actions and actions still requiring approval;
- selected line, current station, and exact starting state;
- knowns, assumptions, decisions, and open blockers;
- files, interfaces, data categories, and affected users in scope;
- completed changes and evidence from each check;
- selected specialists, caller/owner relationships, and remaining shared budgets;
- findings, residual risks, release state, and exact next action.

Before a commit, record the exact candidate or diff, local branch destination,
operation, and both gate states; after it succeeds, record the exact commit SHA.
Before any push, merge, promotion, save, publication, or deployment, record the
exact artifact revision, operation, destination, and both gate states. For Git
transitions, identify the remote and full ref such as `refs/heads/example`; a
branch nickname, implicit upstream, or the word "source" is not an exact
destination.

Update it at meaningful phase boundaries in its authorized location. Do not
duplicate a repository's active work system, issue tracker, or release record.

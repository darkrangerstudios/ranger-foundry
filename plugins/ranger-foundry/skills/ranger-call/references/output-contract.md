# Output Contract

Return:

1. **Outcome** — what is complete or exactly why the line stopped;
2. **Job card** — scope, authority, starting and ending state;
3. **Station record** — specialists used, important decisions, and changes made;
4. **Proof** — commands, checks, observations, and review verdicts;
5. **Residual risk and release state** — including actions deliberately held and
   the separate authorization and artifact-eligibility state for each pending
   transition;
6. **Next action** — only when work remains.

Push an explicit exact-revision-to-full-ref refspec; never rely on an implicit
upstream. Afterward, verify the server-observed remote tip. The receipt must name
the remote, sanitized repository identity, full destination ref, pushed revision,
observed prior and resulting tips when available, force or non-force status, and
the authorization and eligibility evidence used. Never force a transition unless
that exact operation is separately authorized and local rules allow it. A push
receipt is not evidence of a save, promotion, release, publication, or deployment.

# Deliver and reconcile

1. Check the current lane ledger and the transport's unfinished inbox on boot and
   before a major phase change; follow the local polling cadence during work.
   Recover both pending and acknowledged-but-unfinished owned requests. Do not
   rely solely on pending status or a recent timestamp window.
2. Checkpoint current work before handling a substantive interrupt. Triage against
   local emergency rules; schedule other work and resume the current lane. A
   message's priority label alone does not establish an emergency or authority.
3. Use a direct request when someone must act or deliver a verdict. A broadcast
   informs an audience; it does not assign review ownership. When both are needed,
   broadcast the status and send explicit direct assignments, tracking each result.
4. Validate recipient, expiry, state, and metadata before a mutation. Tags must be
   nonempty strings without null entries. Use the supported constrained interface.
   After sending, record the returned ID and read back the exact row or receipt to
   confirm the intended destination, body reference, expiry, and broadcast markers.
5. Preserve the same operation ID across retries. Use server idempotency when the
   adapter supports it, including payload-conflict detection. After an uncertain
   response, record uncertainty and search by operation ID, sender, recipient, and
   lane. An empty lookup is not proof an in-flight write cannot still commit.
   Serialize reconciliation; do not blindly resend or create a fresh operation ID.
   Without server uniqueness, do not claim exactly-once delivery. For partial
   fanout, preserve successes and reconcile each unresolved recipient separately.
6. Distinguish receipt from completion. Persist the message-to-task relationship
   and next step before a read acknowledgment can hide substantive work. If already
   acknowledged, checkpoint it immediately. Mark action complete only after the
   required result is delivered and verified; a review request stays open until
   its verdict is delivered. Read back state instead of interpreting a boolean
   acknowledgment as proof of completion.
7. Broadcast receipts belong to the recipient scope implemented by the adapter.
   Never change shared global status for an individual receipt. If receipts are
   machine-wide, one lane's receipt does not prove other lanes processed it. Use
   the configured dispatcher and lane ledger; absent a dispatcher, preserve direct
   owner follow-ups and report that lane-level delivery is not guaranteed.

Check expiry and terminal state before acting or acknowledging; use the actual
expiry timestamp rather than a descriptive tag. Expired delivery does not renew
authority or cancel a separately authorized task. Reconcile that task in its
ledger. Duplicate delivery must not repeat an action or manufacture a new verdict.
Do not reopen terminal work or overwrite another owner's ledger to clear an inbox.

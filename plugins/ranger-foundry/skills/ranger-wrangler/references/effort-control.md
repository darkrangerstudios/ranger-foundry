# Selected-model effort

Use this mode when the model and provider are already selected. Keep both fixed
unless the caller separately authorizes a model/provider routing decision.
Apply Wrangler's route basis, host verification and shared budget rules.

## Select without claiming calibration

Honor explicit user effort within mandatory host/repository limits. An explicit
authorized selection can use a supported value without an automatic map; record
**direct selection**. Otherwise use only an approved effort map for the exact
model, host/runtime version, workflow revision and task class.

With no applicable map, offer the following as **proposal only**. Do not activate
it on the user's behalf or claim calibrated quality or savings:

| Bounded work | Candidate effort, only if supported |
| --- | --- |
| Simple lookup, receipt or unchanged-state check | Low |
| Routine edits or evidence gathering | Medium |
| Substantial implementation or standard review | High |
| Difficult correctness, security, recovery or diagnosis | Extra High / xhigh |

Consequences and uncertainty control classification. Do not select Low from a
short prompt or assign effort permanently to a Ranger name. Split mixed work
only when independently useful pieces justify context and coordination costs.
Lower effort never removes checks, permissions or independent review. If a
fixed effort cannot satisfy the task, explain the limitation and request the
revised choice; do not quietly raise it or lower acceptance.

## Verify the host's effective setting

Use the installed host's supported native worker controls. Verify current field
names, allowed values, precedence and scope before applying them. Some hosts can
override spawn values through a worker definition or environment; unset values
may inherit from a parent. Some skill overrides affect the caller rather than
only a worker. A resumed worker may retain an older route. Do not assume controls
or level names are equivalent across hosts, models or versions.

Keep requested and effective effort separate in the receipt. Use host-reported
configuration, resolved execution metadata or task diagnostics and cite the
version and evidence. Echoed request parameters are not effective-setting
evidence. An instruction saying “use low effort” is not a runtime control.
Unknown, unsupported or mismatched settings remain **unverified**; stop dependent
high-risk or hard-budget-sensitive work. Other work can continue only at an
already-authorized current setting, without claiming the requested level applied.

## Keep escalation and overhead explicit

The same one-worker, one-escalation ceilings and shared limits apply. Escalate
only for an evidenced reasoning/correctness gap, new evidence and available
authorized budget. Do not treat authentication, transport, missing input or
unavailable tools as reasoning failures. An explicit effort pin requires
permission to change; after an unsuccessful escalation, return the blocker.

Max, Ultra and additional orchestration require explicit task authorization;
they are not an automatic next step on a shared numeric scale. A mode labeled
“Ultra” or similar may alter orchestration as well as reasoning. Verify the
actual host behavior rather than assuming a portable cost or effort meaning.

Adaptive thinking within a configured level is not proof of automatic level
selection. An “auto” control can clear a saved choice while environment or other
overrides still determine the effective setting. Check that state instead of
equating “auto” with a calibrated routing policy.

A lower-effort worker does not lower the parent's effort or erase startup cost.
Cheap polling requires the polling run itself to start at the intended setting;
do not create or modify a scheduler merely because this skill was loaded.
Verification proves the observed configuration, not task quality, performance,
measured savings or release eligibility.

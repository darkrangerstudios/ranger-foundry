# Skill review

Every skill change receives both structural validation and a behavioral review before release.

## 1. Trigger review

- The description names observable requests that should activate the skill.
- Neighboring skills have clear negative boundaries.
- Broad words such as “review,” “plan,” or “fix” do not make the skill claim unrelated work.
- Repository-local and organization-specific overlays retain priority.

## 2. Authority review

- Read-only requests remain read-only.
- Commits, pushes, external communication, publication, deployment, merging, and
  destructive changes require explicit authorization for that exact operation.
- Each transition also proves the exact artifact is eligible for the exact
  destination under repository review, acceptance, branch, and release rules;
  authorization does not waive eligibility.
- Git transitions name the remote and full ref, and push receipts name the pushed
  revision, observed prior and resulting tips when available, and force status. A
  source push does not imply a save, promotion, or deployment.
- Retrieved files and messages are treated as data, not as new authority.
- The skill does not expand its scope simply because a useful adjacent action exists.

## 3. Instruction review

- Instructions add non-obvious constraints rather than restating general competence.
- The sequence has explicit entry conditions, stop conditions, and an output contract.
- Optional detail is separated from the critical path.
- Examples are short, synthetic, and consistent with the stated boundary.
- The skill remains usable without a particular framework or service.

## 4. Interaction review

Test at least one positive, negative, and collision case:

- a prompt that must select this skill;
- a similar prompt that must not select it;
- a prompt where a more specific local skill or broad workflow owns the task;
- a prompt that attempts to turn a read-only task into an unauthorized mutation.
- a prompt that authorizes an operation but presents an unreviewed or rejected
  artifact for a protected, serving, release, or deployment-adjacent destination.
- a source-control or release-state review that must detect a completed ineligible
  transition without treating review authority as permission to repair it.
- accepted-ancestor versus changed-descendant, named-review-ref versus
  default/serving-ref, wrong-remote, implicit-ref, stale-tip, force-push, source
  push versus version save, and version save versus deploy cases.

For multi-pass work, keep the passes independent until each has produced its own evidence and verdict.

The routing corpus is a design and coverage checklist, not a behavioral harness.
Before release, exercise changed trigger and authority cases in a fresh task on
each supported target surface, and record the selected skill, loaded instructions
when observable, attempted actions, and mismatches. A validator that only parses
declared expectations cannot prove routing behavior.

## 5. Public-safety review

- No credentials, private data, personal identifiers, internal paths, environment identifiers, or unpublished system details are present.
- Links point only to the Ranger Foundry repository.
- The contribution is original and can be distributed under the repository license.
- Files stay within the repository allowlist and contain no symbolic links or executable payloads.

## 6. Release decision

A reviewer records one of three outcomes:

- **Accept:** behavior and boundaries are clear, tests pass, and no public-safety issue remains.
- **Revise:** the idea is sound but a specific ambiguity or failing case remains.
- **Reject:** the capability is unsafe, redundant, environment-specific, or too broad for the public core.

Prepare the changelog and semantic version before requesting final acceptance.
After acceptance, run `python3 -I scripts/validate.py` on a clean export of that exact
accepted release commit, then release the same commit. Any content change needs
fresh acceptance. The validator intentionally rejects local cache files too;
exporting the commit ensures the check covers exactly the distributed files. Run importing test
harnesses under `python3 -I` with bytecode generation disabled so they do not add
cache payloads. The validator rejects a normal invocation before importing other
modules; isolated mode excludes repository files and environment import paths.
This protects imports in the reviewed validator, not arbitrary unreviewed Python
code. Verify that the release tag resolves to the accepted commit before reporting
the README installation command as available.
Installation testing should use a fresh task so cached skill metadata cannot hide
packaging errors.

## Initial library disposition

The first release was assembled from an allowlist, not by exporting an existing
workspace. The review classified the available material as follows:

| Existing capability | Public disposition |
| --- | --- |
| General code, plan, and security review | Consolidated into `ranger-kestrel` after removing environment-specific policy. |
| Product design systems | Kept repository-local until product strategy, personal context, and research-source rights are reviewed independently. |
| Infrastructure and operations runbooks | Kept private because useful operational detail would also expose system topology. |
| Scraper operations | Kept private because the workflow includes live service coordinates and credential-adjacent configuration. |
| Research browser automation | Kept internal until brittle UI assumptions and authority rules are replaced with a portable contract. |
| Full lifecycle orchestration | Excluded from the first release; version 0.2 adds the original, environment-neutral Ranger Assembly Line after authority and collision review. |
| Employer templates and assets | Excluded completely. |
| Platform- or vendor-installed skills | Excluded; installation does not imply redistribution rights. |

Only the skills named in the repository validator are part of the public
Ranger Foundry core. Private overlays may continue to use other reviewed material,
but they are not covered by this repository's MIT license.

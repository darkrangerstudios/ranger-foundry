# Skill review

Every skill change receives both structural validation and a behavioral review before release.

## 1. Trigger review

- The description names observable requests that should activate the skill.
- Neighboring skills have clear negative boundaries.
- Broad words such as “review,” “plan,” or “fix” do not make the skill claim unrelated work.
- Repository-local and organization-specific overlays retain priority.

## 2. Authority review

- Read-only requests remain read-only.
- External communication, publication, deployment, merging, and destructive changes require explicit authorization.
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

For multi-pass work, keep the passes independent until each has produced its own evidence and verdict.

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

After acceptance, run `python3 scripts/validate.py`, update the changelog, and release with a semantic version. Installation testing should use a fresh task so cached skill metadata cannot hide packaging errors.

## Initial library disposition

The first release was assembled from an allowlist, not by exporting an existing
workspace. The review classified the available material as follows:

| Existing capability | Public disposition |
| --- | --- |
| General code, plan, and security review | Consolidated into `ranger-kestrel-review` after removing environment-specific policy. |
| Product design systems | Kept repository-local until product strategy, personal context, and research-source rights are reviewed independently. |
| Infrastructure and operations runbooks | Kept private because useful operational detail would also expose system topology. |
| Scraper operations | Kept private because the workflow includes live service coordinates and credential-adjacent configuration. |
| Research browser automation | Kept internal until brittle UI assumptions and authority rules are replaced with a portable contract. |
| Full lifecycle orchestration | Excluded from this release where ownership or third-party license boundaries were not clean enough for MIT distribution. |
| Employer templates and assets | Excluded completely. |
| Platform- or vendor-installed skills | Excluded; installation does not imply redistribution rights. |

Only the eight skills named in the repository validator are part of the public
Ranger Foundry core. Private overlays may continue to use other reviewed material,
but they are not covered by this repository's MIT license.

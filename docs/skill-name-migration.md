# Skill names in v0.3.0

The Ranger's name is now its invocation ID and menu label. All names begin with
`ranger-` so the posse groups together in the skill menu. This release changes the
v0.2.x command names; it does not change the specialists' authority or methods.

| Previous invocation ID | New invocation ID | Ranger |
| --- | --- | --- |
| `ranger-assembly-line` | `ranger-marshal` | Marshal |
| `ranger-cause-analysis` | `ranger-bounty-hunter` | Bounty Hunter |
| `ranger-agent-instructions` | `ranger-warden` | Warden |
| `ranger-slice-plan` | `ranger-trailblazer` | Trailblazer |
| `ranger-plan-assurance` | `ranger-deadeye` | Deadeye |
| `ranger-handoff` | `ranger-courier` | Courier |
| `ranger-questionnaire` | `ranger-prospector` | Prospector |
| `ranger-prototype` | `ranger-sparks` | Sparks |
| `ranger-kestrel-review` | `ranger-kestrel` | Kestrel |

Raven joins in v0.3.0 as `ranger-raven`. Its earlier unpublished draft used
`ranger-swarm-coordination`; that draft name is not a second installed skill.

## Update an installation

For a managed plugin, update the existing installation to the reviewed v0.3.0 tag
using the host's plugin manager. Start a fresh task and verify that the plugin's
skill list contains the ten new names. Do not edit managed plugin caches.

For vendored skills or configured source directories:

1. Record the currently pinned release and inventory the discovery roots used by
   each host. Check for both plugin-managed and vendored registration of the same
   Foundry core so a second registration does not leave duplicate menu entries.
2. Stage the new skill tree from the exact accepted release and verify its bytes.
3. Compare each old Foundry directory with the previously pinned release. Archive
   the matching old tree outside every skill-discovery root, then replace it with
   the new names. Check for extra files and local edits before removing anything.
   A modified old skill or an occupied new destination needs reconciliation;
   preserve its bytes and stop that replacement until resolved. Never delete a
   private overlay or an unrelated skill based on a `ranger-` prefix alone.
4. Update active loaders, saved prompts, task routing, and local verification
   fixtures to the new IDs. Keep historical review evidence tied to its original
   version rather than rewriting old verdicts.
5. Confirm all ten new skills are registered and the superseded role-based core
   directories are no longer registered in the discovery roots being upgraded.
   Start a fresh task and try `ranger-marshal` and `ranger-bounty-hunter` using the
   host's invocation mechanism. Record any host that has not been verified.

Keep the previous release pin and archived tree for rollback. Restore that exact
tree and its matching loader references if the upgrade fails. Native menu checks
must be performed on the target host; repository validation checks packaging and
metadata, not a running host's skill menu.

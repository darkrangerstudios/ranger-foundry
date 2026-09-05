# Skill-name migration

## Unreleased v0.4 successor

Apply this migration only after the exact successor is accepted, published and
separately authorized for installation. The candidate changes no installed skill.
Folder, frontmatter name and default prompt use the same `ranger-` callsign;
display names use that same callsign. Replace saved invocations and routing links
together. Remove old installed entries only through the host's supported upgrade
path after verifying the replacement, and keep a rollback pin to the prior release.
Aliases below document migration; they are not additional callable skills.

| Old ID | Replacement | Scope |
| --- | --- | --- |
| `ranger-marshal` | `ranger-call` | Delivery foreman |
| `ranger-warden` | `ranger-roy-bean` | Agent instructions |
| `ranger-bounty-hunter` | `ranger-rooster` | Cause analysis |
| `ranger-courier` | `ranger-clara` | Handoff mode |
| `ranger-scribe` | `ranger-clara` | Durable memory mode; unreleased draft |
| `ranger-surveyor` | `ranger-clara` | Meaning and identity mode; unreleased draft |
| `ranger-scout` | `ranger-big-iron` | Reconnaissance mode; unreleased draft |
| `ranger-tank` | `ranger-big-iron` | Fleet recovery mode; unreleased draft |
| `ranger-phantom` | `ranger-big-iron` | Browser mode and unchanged pure motion planner; unreleased draft |
| `ranger-outrider`, `ranger-deets` | `ranger-big-iron` | Proposed reconnaissance aliases; never released |
| `ranger-drover`, `ranger-trampas` | `ranger-big-iron` | Proposed fleet aliases; never released |

Kestrel, Raven, Deadeye, Sparks, Trailblazer, Prospector and Wrangler retain their
IDs. Gus is new. Call invokes Gus inline at consequential decisions; a Gus result
is never an independent-review verdict. Do not retain duplicate menu entries for
absorbed modes. Transport recipients such as Scout are not renamed by this guide.

## Prior v0.3 migration (historical)

For an older role-based command below, first resolve its v0.3 replacement, then
apply the v0.4 mapping above. Preserve prior tags when rolling back.

# Skill names in v0.3.0

This document maps the v0.3.0 rename. When installing a later version, also verify
the complete roster packaged in that version; the ten names below are the naming
migration baseline, not a ceiling on later releases.

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

# Security policy

## Reporting a vulnerability

Report suspected vulnerabilities through [GitHub private vulnerability reporting](https://github.com/darkrangerstudios/ranger-foundry/security/advisories/new). Do not open a public issue for a vulnerability that could put users or data at risk.

Include the affected version, the relevant skill or manifest, reproduction details, likely impact, and any safe evidence that helps confirm the issue. Do not include credentials, private data, or environment-specific identifiers.

We aim to acknowledge a complete report within five business days. Remediation timing depends on severity and the scope of the change.

## Supported versions

Security fixes target the latest released version. Older versions may require an upgrade before a fix can be applied.

## Security boundary

Ranger Foundry ships skill instructions and one optional pure JavaScript motion
planner, together with its browser reference. The planner performs no browser or
network actions and is not run automatically by the plugin. Its source and the
reference are allowlisted by exact path and byte hash; changes require renewed
review. The package has no hooks, installers, credential handling, or
network-capable helper code. A conservative source screen supplements the exact
pin but is not a JavaScript sandbox.

Documentation URLs are limited to the repository and explicitly reviewed exact
reference URLs. Skills preserve user authorization, treat retrieved content as
untrusted, and avoid exposing private context in generated output. The host
provides any actual browser or agent capabilities and their permission controls.

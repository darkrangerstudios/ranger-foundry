# Host controls

Documentation checked 2026-09-05; confirm the installed surface and supported
values before using these recipes. These are documented controls, not tested
integration adapters or proof of the user's effective setting.

| Product/surface | How to recommend a change | Boundary and verification |
| --- | --- | --- |
| Codex app / compatible app-server client | Choose a supported model/effort in the host control. | The protocol configures effort per new turn; steering appends to the active turn. For an explicit fresh boundary, checkpoint, finish or safely stop, select the setting, then send Continue as a new turn. Do not assume an in-flight turn or existing worker changed. Check available resolved diagnostics. |
| Claude Code | Use `/effort <supported-level>` or the effort control in `/model`; preserve the model for effort-only work. | Current documentation allows `/effort` while working and applies it to the next request in the turn after any displayed confirmation. Stopping is not generally needed. Check the displayed setting and overrides; environment or skill/subagent settings can affect the result. These commands are not instructions for Claude chat or Cowork. |
| GitHub Copilot app | Use the model and reasoning-effort dropdowns below the prompt. | Settings may change during a session. Confirm the selected model's supported control and next applicable request; do not infer the exact in-flight boundary. Session autonomy mode is a separate choice. |
| GitHub Copilot cloud agent | Select the model, then the reasoning dropdown when offered for that model and task. | An absent reasoning selector is not permission to invent one. Confirm task configuration; don't relaunch or duplicate an active task solely to change effort. |
| Microsoft Copilot chat | Select an available conversation mode under the prompt before submitting. | Modes such as Quick response and Think Deeper are product modes, not numeric effort equivalents. Do not assume a precise model or hidden effort. This is distinct from GitHub Copilot and does not establish Microsoft 365 workplace-agent controls. |
| Claude chat, Cowork, other products or unavailable controls | Inspect that surface's current supported model/mode controls; give steps only when evidenced. | If no comparable control or setting telemetry is available, remain advisory. A missing native skill registry requires an authorized instruction-loading path; do not claim installation or cross-product qualification. |

Sources for the recipes: [Codex app-server](https://learn.chatgpt.com/docs/app-server),
[Claude Code model configuration](https://code.claude.com/docs/en/model-config),
[GitHub Copilot app sessions](https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions),
[Copilot cloud model selection](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/changing-the-ai-model),
and [Microsoft Copilot conversation modes](https://support.microsoft.com/en-us/microsoft-copilot/conversation-modes-in-microsoft-copilot).

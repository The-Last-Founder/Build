# Tools

A starter map of tools and practices we may use while building the Build community and the Johnny pilot.

## How to read this

**Scope**

- **General**: useful for builders across projects.
- **Johnny**: specifically relevant to the [Johnny pilot](https://github.com/The-Last-Founder/Johnny).
- **Both**: useful generally and also relevant to Johnny.

**Signal**

- For open-source tools: GitHub stars or similar visible traction.
- For commercial tools: public product maturity or adoption signal.
- For concepts: source quality or relevance, not popularity.

## Tool map

| Tool | Scope | Category | What it does | Why for us | Released / maturity | Signal |
|---|---:|---|---|---|---|---|
| [Claude Code](https://github.com/anthropics/claude-code) | Both | Agentic coding | Coding agent for terminal, IDE, GitHub workflows, and repo changes. | Main builder tool for coding, reviewing, debugging, docs, and PR workflows. | Research preview 2025-02; GA 2025-05. | OSS repo, ~135k GitHub stars. |
| [Codex](https://github.com/openai/codex) | Both | Agentic coding | OpenAI coding agent for CLI, IDE, app, and cloud workflows. | Good second agent for parallel implementation, review, and comparison with Claude Code. | First public launch around 2025-04/05. | OSS CLI repo, ~94k GitHub stars. |
| [GitHub Copilot](https://github.com/features/copilot) | Both | Coding assistant / agent | AI coding assistant inside GitHub, IDEs, CLI, and PR workflows. | Lowest-friction tool for builders already living inside GitHub. | Technical preview 2021-06; GA 2022-06. | Mature GitHub product. |
| [Cofounder.co](https://cofounder.co/) | General | Company agent OS | Agent orchestration platform for engineering, sales, marketing, design, finance, and ops. | Useful as a reference for AI-native startup workflows, not just coding. | Cofounder 2 announced 2026-03. | Commercial product. |
| [OpenClaw](https://github.com/openclaw/openclaw) | Both | Personal agent runtime | Self-hosted personal AI assistant that runs across chat channels and devices. | Candidate reference/backend for chat-native agent architecture and task automation. | Active OSS, 2026 releases. | OSS repo, ~381k GitHub stars. |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Both | Persistent agent runtime | Self-improving agent with memory, skills, messaging gateways, and multi-platform execution. | Candidate backend/reference for persistent memory, agent skills, and long-running routines. | Active OSS, 2026 releases. | OSS repo, ~204k GitHub stars. |
| [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag) | Both | Team agent in chat | Lets teams tag Claude inside Slack channels and delegate work. | Strong reference for Johnny’s “shared teammate in a group chat” behavior. | Released 2026-06-23, beta. | Anthropic Team/Enterprise beta. |
| [Loop Engineering](https://www.oreilly.com/radar/loop-engineering/) | General | Practice / workflow | Designing feedback loops around agents: plan, act, verify, adjust, repeat. | Core skill to teach builders: stop prompting once, start designing reliable loops. | Emerging 2026 practice. | High relevance, not a product. |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | General | Agent skill / ruleset | Makes coding agents prefer the smallest working solution and avoid overengineering. | Useful default skill for builders so agents ship less bloat and simpler code. | Active OSS, 2026 releases. | OSS repo, ~61k GitHub stars. |
| [Talk To My Agent](https://www.talktomyagent.io/) | General | Voice gateway | Gives an OpenClaw or Hermes-style agent a real phone number. | Later-stage inspiration for voice access, support calls, or personal assistant workflows. | Active commercial product. | Niche but directly adjacent. |
| [Any.do](https://www.any.do/) | Johnny | Task management | Tasks, lists, calendar, reminders, WhatsApp task capture, AI assistant, team boards. | Integration candidate and UX reference for Johnny’s tasks and reminders. | Launched 2011-11. | Mature product, 40M+ users claimed. |
| [Trello](https://trello.com/) | Johnny | Kanban / project management | Boards, lists, cards, and lightweight project tracking. | Integration candidate and familiar model for Johnny-managed task boards. | Launched 2011-09. | Mature Atlassian product. |
| [monday.com](https://monday.com/) | Johnny | Work management | Work OS for teams, projects, workflows, CRM, dev, service, and automations. | Integration candidate for teams that outgrow Markdown task files. | Founded 2012; first customers 2014. | Mature public company/product. |
| [open-bsp-api](https://github.com/matiasbattocchia/open-bsp-api) | Johnny | WhatsApp / Instagram infra | Self-hostable WhatsApp and Instagram Business API platform by Matías Battocchia. | Most directly relevant infrastructure candidate for Johnny’s WhatsApp-native MVP. | Active OSS, 2026. | OSS repo, ~421 GitHub stars. |

## Notes

- **Johnny-specific tools are marked in the Scope column.**
- **Loop Engineering is a practice, not a tool**, but it belongs here because it is central to how builders will use agents well.
- **Hermes Agent** is listed assuming “Hermew” meant Hermes. If “Hermew” is a different tool, add it as a separate row.
- **The task “Upload Tools.md to Johnny GitHub” is not a tool**, so it is intentionally not listed in the table.
- This file should stay concise. Add new tools only when someone actually plans to try them, teach them, or integrate them.

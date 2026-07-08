# Tools

Image created ~29.6.26

<img width="1774" height="887" alt="image" src="https://github.com/user-attachments/assets/9feabdaf-616a-4041-ab92-5dc5331b0062" />

A starter map of tools and practices we may use while building the Build community and the Johnny pilot.

## Ecosystem research context

For a deeper ecosystem scan, see [The AI Agent / Multi-Agent / Autonomous-Company Enabling Stack (Mid-2026)](research/ai-agent-multi-agent-autonomous-company-stack-mid-2026.md).

Build takeaway: infrastructure and orchestration are currently more mature than full autonomous-company app claims, so we should prioritize practical, testable tool workflows over broad autonomy narratives.

## Related list

- [Awesome AI Tools](https://github.com/mahseema/awesome-ai-tools) (broad ecosystem reference list)
- Value add of this file: a startup-focused shortlist in Build format (Scope, Why for us, and current signal), not a general directory.

## AI Tooling Policy

This section explains what AI tools contributors can actually use, who pays, and how agent-assisted contribution works.

### Tool classifications

| Tool | Access model | Cost model | Fit for sparse contributors | Current recommendation |
|---|---|---|---|---|
| [GitHub Copilot](https://github.com/features/copilot) | Per user/seat; org-assigned seat for orgs | Paid plan (Individual, Business, or Enterprise) + AI premium request credits | **Weak for many occasional contributors** — per-seat cost makes broad access expensive for a sparse OSS community | Optional / maintainer experiment; not the default for contributors |
| [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag) | Claude Team or Enterprise + Slack workspace setup | Org usage balance / spend limit for channel work | Potentially better than per-seat once Slack is active, but **not available to free or individual users** | Reference + possible future pilot; not a contributor requirement now |
| [Claude Code](https://github.com/anthropics/claude-code) / [Codex](https://github.com/openai/codex) | Individual plan or API key | User's own subscription / API key | **Good if contributor already has access** | Bring your own; or maintainer-run on request |
| [Aider](https://aider.chat/) | Local CLI + Git | Contributor's own API key or subscription | **Good BYO path** — runs locally, no special platform required | Optional / bring your own |
| [OpenHands](https://docs.openhands.dev/openhands/usage/run-openhands/github-action) | OSS; can run as a GitHub Action | Maintainer's API key / token budget / infra | **Strong candidate for maintainer-run, token-budgeted issue-to-PR runs** | Under evaluation |
| [SWE-agent](https://swe-agent.com/latest/) | OSS, model-provider agnostic | Maintainer's API key / token budget / infra | **Strong candidate** — model-agnostic and well-suited to issue-to-PR automation | Under evaluation |

### Contributor AI tooling rules

1. **GitHub Copilot and Claude Tag are not required for contributors.** Do not assume assigned seats or shared org credits are available.
2. **GitHub Issues and Pull Requests are the source of truth.** All work lands as a PR; agent output is no exception.
3. **Copilot Cloud Agent and Claude Tag are maintainer/steward experiments**, not baseline contributor infrastructure.
4. **Contributors bring their own AI tools** if they have them (Claude Code, Codex, Aider, Cursor, etc.). No tooling requirement is imposed.
5. **Agent-assisted contribution path:** if a contributor needs agent help they can comment `/agent-help <request>` on a GitHub issue. A maintainer decides whether to run an agent. Agent output must come back as a PR, a draft PR, or a plan comment — never as an automatic merge.
6. **No automatic agent runs on arbitrary issue text from untrusted users.** Maintainer opt-in only.

### OpenHands vs SWE-agent (candidate token-budgeted runners)

Both are OSS tools that can turn a GitHub issue into a PR using a shared API key/token budget controlled by maintainers. Neither requires contributors to have paid AI accounts.

| | [OpenHands](https://docs.openhands.dev/openhands/usage/run-openhands/github-action) | [SWE-agent](https://swe-agent.com/latest/) |
|---|---|---|
| Model support | Any OpenAI-compatible API, Anthropic, local models | Model-agnostic (OpenAI, Anthropic, local, others) |
| GitHub Action | Yes — first-class GitHub Action support | Yes — can be run in CI/CD pipelines |
| Maturity | Active OSS, used in research and production workflows | Research origin (Princeton NLP), active OSS |
| Best for | Full agent loop with persistent context and GUI | Focused issue-to-PR with structured edit/patch output |
| Cost control | Token budget via API key; no per-seat cost | Token budget via API key; no per-seat cost |

**Recommendation:** evaluate OpenHands GitHub Action first as a maintainer-run experiment on a small labeled set of issues.

### Open question

> **Do we want to fund a small shared token budget for maintainer-approved agent runs?**
> This would let maintainers run OpenHands or SWE-agent on contributor-requested issues without each contributor needing a paid account. Requires deciding a monthly spend cap and who controls the API key.

---

## How to read this

**Scope**

- **General**: useful for builders across projects.
- **Johnny**: specifically relevant to the [Johnny pilot](https://github.com/The-Last-Founder/Johnny).
- **Both**: useful generally and also relevant to Johnny.

**Signal (as of June 2026)**

- For open-source tools: GitHub stars, activity, or similar visible traction.
- For commercial tools: product maturity, adoption, or strategic relevance.
- For concepts: source quality or relevance, not popularity.

**Bold tools** are primary candidates for early hands-on use or evaluation.

The table is sorted roughly by first-sprint usefulness, then by Johnny MVP relevance.

## Tool map

| Tool | Scope | Category | What it does | Why for us | Released / maturity | Signal (June 2026) |
|---|---:|---|---|---|---|---|
| [**Cofounder.co**](https://cofounder.co/) | Both | Company agent OS | AI company OS across engineering, sales, marketing, design, finance, and ops. | Main harness for starting the project, coordinating agents, and testing AI-native startup workflows. | Active commercial product. | Primary starting harness. |
| [**Claude Code**](https://github.com/anthropics/claude-code) | Both | Agentic coding | Coding agent for terminal, IDE, GitHub workflows, and repo changes. | Main implementation tool for coding, reviewing, debugging, docs, and PR workflows. | Mature Anthropic coding product with active releases. | Official Anthropic tool; high builder relevance. |
| [**Codex**](https://github.com/openai/codex) | Both | Agentic coding | OpenAI coding agent for CLI, IDE, app, and cloud workflows. | Second coding agent for parallel implementation, review, and comparison with Claude Code. | Active OpenAI coding product and OSS CLI. | Official OpenAI tool; high builder relevance. |
| [Claude Usage Dashboard](https://github.com/phuryn/claude-usage) | Both | Usage analytics | Reads local Claude Code logs and turns them into usage charts and cost estimates. | Helps builders track agent usage and spend, and tune workflows from real usage data. | Active OSS CLI/web app with VS Code extension support. | Purpose-built for Claude Code visibility across API, Pro, and Max plans. |
| [Lovable](https://lovable.dev/) | General | AI app builder | Prompt-to-app builder for generating and iterating full-stack web apps in the browser. | Useful reference for fast MVP prototyping and comparing app-builder workflows with agentic coding tools. | Active commercial product. | Strong current mindshare in AI-native builder communities. |
| [base44](https://base44.com/) | General | AI app builder | AI-native app builder focused on quickly creating production-style internal and web apps. | Relevant comparison point for no-code/low-code AI product building versus code-first agent workflows. | Active commercial product. | Emerging product with growing founder/operator interest. |
| [Bolt.new](https://bolt.new/) | General | AI app builder | Browser-based AI coding environment that scaffolds and edits full-stack apps from prompts. | Similar benchmark for rapid idea-to-prototype loops and evaluating tradeoffs against local coding agents. | Active commercial product. | Widely used in prompt-to-app experimentation workflows. |
| [ctx](https://github.com/stevesolun/ctx) | Both | Agent context / tool routing | Graph-backed recommendation layer for skills, agents, MCP servers, and harnesses, with CLI and dashboard workflows. | Companion to Claude Code and Codex: helps builders load the right context bundle for the current task without bloating agent sessions. | Active MIT OSS Python package on PyPI. | Ships a large recommendation graph: 68k+ skills, 10k+ MCP servers, 467 agents, and 207 harnesses. |
| [GitHub Copilot](https://github.com/features/copilot) | Both | Coding assistant / agent | AI coding assistant inside GitHub, IDEs, CLI, and PR workflows. | Lowest-friction tool for builders already living inside GitHub. **Access requires a paid plan or org seat — not the default for sparse OSS contributors.** See [plans](https://docs.github.com/en/copilot/get-started/plans). | Mature GitHub product. | Very broad adoption. Maintainer experiment / optional for contributors. |
| [Aider](https://aider.chat/) | Both | Agentic coding (local CLI) | Local AI pair-programmer for the terminal; integrates with Git and supports multiple model providers via contributor's own API key. | Good bring-your-own path for contributors who already have an API key; no platform account required. | Active OSS, widely used. | Strong BYO option for contributors. |
| [OpenHands](https://docs.openhands.dev/openhands/usage/run-openhands/github-action) | Both | Issue-to-PR agent runner | OSS agent that can take a GitHub issue and produce a PR using a maintainer-controlled API key or token budget. First-class GitHub Action support. | Candidate for maintainer-run, token-budgeted agent runs so contributors without paid AI access can still get agent help. | Active OSS; GitHub Action available. | Strong candidate — under evaluation. |
| [SWE-agent](https://swe-agent.com/latest/) | Both | Issue-to-PR agent runner | OSS, model-agnostic agent that converts GitHub issues into structured patches/PRs. Research origin (Princeton NLP), CI/CD compatible. | Parallel candidate to OpenHands for maintainer-controlled agent runs; model-agnostic gives flexibility over cost/model choice. | Active OSS; CI/CD pipeline support. | Strong candidate — under evaluation. |
| [OpenClaw](https://github.com/openclaw/openclaw) | Both | Personal agent runtime | Self-hosted personal AI assistant that runs across chat channels and devices. | Candidate reference/backend for chat-native agent architecture and task automation. | Active OSS. | Very high GitHub traction. |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Both | Persistent agent runtime | Self-improving agent with memory, skills, messaging gateways, and multi-platform execution. | Candidate backend/reference for persistent memory, agent skills, and long-running routines. | Active OSS, with June 2026 releases. | High relevance for persistent-agent patterns. |
| [Odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | Both | Self-hosted AI workspace | Self-hosted AI workspace for chat, agents, research, documents, email, notes, calendar, and local model workflows. | Strong reference for an integrated builder workspace that combines agent operations, knowledge work, and personal backoffice tools in one place. | Active OSS; default `dev` branch with curated `main` branch. | Very high current GitHub traction (~81k stars since May 2026). |
| [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag) | Both | Team agent in chat | Lets teams tag Claude inside Slack channels and delegate work. | Strong reference for Johnny's "shared teammate in a group chat" behavior. **Requires Claude Team or Enterprise plan plus a Slack workspace — not available to free or individual users.** | Released 2026-06-23, beta. | Anthropic Team/Enterprise beta. Reference + possible later pilot. |
| [Loop Engineering](https://www.oreilly.com/radar/loop-engineering/) | General | Practice / workflow | Designing feedback loops around agents: plan, act, verify, adjust, repeat. | Core skill to teach builders: stop prompting once, start designing reliable loops. | Emerging 2026 practice. | High relevance, not a product. |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | General | Agent skill / ruleset | Makes coding agents prefer the smallest working solution and avoid overengineering. | Useful default skill/ruleset so agents ship less bloat and simpler code. | Active OSS. | Strong fit for builder discipline. |
| [Talk To My Agent](https://www.talktomyagent.io/) | General | Voice gateway | Gives an OpenClaw-style agent a real phone number. | Later-stage inspiration for voice access, support calls, or personal assistant workflows. | Active commercial product. | Niche but directly adjacent. |
| [WisprFlow](https://wisprflow.ai/) | General | Voice input / dictation | AI-powered voice dictation that works system-wide in any app, with context-aware formatting, filler-word removal, and voice editing. | Lets builders write faster by dictating prompts, docs, and messages; useful for high-volume text work across all tools. | Active commercial product; free tier available. | Strong adoption; widely reviewed as leading AI dictation tool. |
| [**open-bsp-api**](https://github.com/matiasbattocchia/open-bsp-api) | Johnny | WhatsApp / Instagram infra | Self-hostable WhatsApp and Instagram Business API platform by Matías Battocchia. | Most directly relevant infrastructure candidate for Johnny’s WhatsApp-native MVP. | Active OSS. | Small repo, very high strategic relevance. |
| [Any.do](https://www.any.do/) | Johnny | Task management | Tasks, lists, calendar, reminders, WhatsApp task capture, AI assistant, and team boards. | Integration candidate and UX reference for Johnny’s tasks, reminders, and AI-assisted task capture. | Mature commercial product. | Mature product; WhatsApp support; 40M+ users claimed. |
| [monday.com](https://monday.com/) | Johnny | Work management | Work OS for teams, projects, workflows, CRM, dev, service, automations, and AI agents. | Integration candidate for teams that outgrow Markdown task files. | Mature commercial product. | Mature AI work platform. |

## Notes

- **Johnny-specific tools are marked in the Scope column.**
- **Bold tools** are the current primary candidates: Cofounder.co, Claude Code, Codex, and open-bsp-api.
- **GitHub Copilot is useful but not the default model for broad sparse open-source contribution.** Access requires a paid plan or org-assigned seat; see [AI Tooling Policy](#ai-tooling-policy) above.
- **Claude Tag is Slack + Team/Enterprise based** — not available to free or individual users and not a contributor requirement now. It is a good reference for chat-native team-agent patterns and potentially worth a pilot later, but for sparse OSS coordination GitHub-native artifacts are the safer default.
- **OpenHands and SWE-agent are the primary candidates for a token-budgeted issue-to-PR path** for contributors who do not have paid AI tooling.
- **Aider is the recommended bring-your-own CLI option** for contributors who already have an API key.
- **Loop Engineering is a practice, not a tool**, but it belongs here because it is central to how builders will use agents well.
- **Trello was intentionally removed** because it is not central enough to the AI-native Johnny workflow right now.
- **The task "Upload Tools.md to Johnny GitHub" is not a tool**, so it is intentionally not listed in the table.
- This file should stay concise. Add new tools only when someone actually plans to try them, teach them, or integrate them.


3 Prompts

## Image prompts

### Banner

Create a GitHub-ready wide header image for the top of Tools.md in the Build repository.

The image should function as a 1-second visual summary of the Tools.md page: a proto-architecture / categorization map of the tools, showing which tools are more central now and which are more secondary or later-stage.

Visual style: ultra-simple, calm, spacious, kawaii, and human. Minimal editorial illustration with clean shapes, soft edges, lots of negative space, restrained MMO-inspired UI hints, and a quiet open-source builder mood. Mostly neutral colors with one warm accent glow. No clutter, no photorealism, no busy dashboard feel, no corporate stock-photo vibe, no fantasy clichés, no neon gamer look.

Composition: a clean diagrammatic landscape or map. In the middle, create a soft glowing central hub for “Build”, with a smaller connected hub for “Johnny”. Around them, place a few grouped zones or islands with very short readable labels. Use spatial proximity, size, and emphasis to show relevance: tools closest to the center are more relevant now; tools farther away are more secondary.

Required grouped content:
1. A clearly emphasized “Start here” zone nearest the center, visually strongest, containing: “Cofounder.co”, “Claude Code”, “Codex”, “Claude Tag”, and “open-bsp-api”.
2. A “Build workflow” zone containing: “GitHub Copilot”, “ctx”, and “Ponytail”.
3. An “Agent runtimes” zone containing: “OpenClaw”, “Hermes Agent”, and “Talk To My Agent”.
4. A “Johnny integrations” zone containing: “Any.do” and “monday.com”.
5. A small foundation or baseline zone containing: “Loop Engineering”.

Interpretation rules:
- “Loop Engineering” should feel like a practice/foundation layer, not a product.
- “Johnny integrations” should feel more to the Johnny side.
- “Build workflow” should feel broadly useful across the project.
- “Start here” should be the most central and immediately legible.
- The whole thing should read in one glance, so keep text very short and large enough to be readable.
- Include a tiny subtle legend: “closer = more relevant now”.

Design language: a calm quest board, system map, or proto-architecture diagram for an open-source startup built with agents. Add tiny abstract builder/map elements for atmosphere, but keep the main focus on clean visual categorization.

Output: polished, modern, GitHub markdown friendly, 2:1 aspect ratio.

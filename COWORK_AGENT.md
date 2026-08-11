# Build Cowork Agent

## Overview

The **Build Cowork Agent** is a community project that automates and enhances the weekly [Build Cowork](COWORK.md) event held every Monday. It is a high-priority dogfooding project for the Build community — we use the tools and methods we advocate to build something that directly serves the community itself.

## Motivation

Build Cowork already has strong momentum and a recurring weekly rhythm. An agent that fits naturally into that rhythm — before, during, and after each session — creates immediate, tangible value for every participant without requiring a separate audience or distribution channel. This makes it an ideal first agent to build together as a community.

## What the Agent Does

The agent operates on the weekly Monday schedule and covers three phases:

### Before the Session (Prep)
- Sends a reminder message to the WhatsApp group with the agenda and any relevant links.
- Helps the facilitator prepare talking points, discussion prompts, or a run-of-show.
- Pulls context from previous sessions to carry forward open threads or action items.

### During / After the Session (Processing)
- Collects the Zoom recording, transcript, and AI-generated summary once the session ends.
- Produces an intelligent summary of the session: key themes, decisions, and action items.
- Posts the summary to the WhatsApp group, optionally with a relevant poll or a "takeaway of the week."

### Ongoing
- Maintains a searchable archive of past sessions (transcripts + summaries).
- Tracks recurring themes and open action items across sessions over time.

## Tech Stack (Proposed)

- **Scheduling**: a simple cron job or GitHub Actions workflow triggered weekly.
- **Zoom integration**: Zoom API to retrieve recordings and transcripts.
- **Summarisation**: an LLM (e.g. Claude or GPT-4o) to generate structured session summaries.
- **WhatsApp integration**: [Johnny](https://github.com/The-Last-Founder/Johnny) or direct WhatsApp Business API.
- **Storage**: GitHub repository or a lightweight database for session archives.

## Getting Involved

This project is open to all Build community members. To contribute:

1. Comment on [issue #81](https://github.com/The-Last-Founder/Build/issues/81) to express interest.
2. Review open issues tagged `cowork-agent` in this repository.
3. Submit a pull request — all contributions welcome!

## Related Resources

- [COWORK.md](COWORK.md) — Build Cowork event details and schedule.
- [Johnny](https://github.com/The-Last-Founder/Johnny) — WhatsApp-native agent for the Build community.
- [TOOLS.md](TOOLS.md) — Tools catalog used by the community.

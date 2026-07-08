# ATTENTION-FIRST DEV

## One-line thesis

Build should be run as an **attention-first agentic development system**:

> Ron does not manage a dashboard.  
> Ron receives small review cards, approves/rejects/routes work, and agents/humans do the rest.

This file summarizes the current methodology research for **The Last Founder / Build**.

Repo context:

- Project: The Last Founder / Build
- Repo: https://github.com/The-Last-Founder/Build
- Main focus: methodology, not repo analysis

---

## 1. Founder constraint

Ron’s real scarce resource is **attention**, not money.

Operating assumptions:

- Attention is often available only in **2-minute** or **5-minute** windows.
- There may be one **30-minute weekly** work session.
- Bipolar / attention variability means the system must survive:
  - low energy
  - high energy
  - interruption
  - forgetting context
  - returning after gaps
- Budget for tools, tokens, agents, humans, and automation is effectively abundant compared to attention.
- Optimize for:
  - low cognitive load
  - short approvals
  - clear next actions
  - repeatable loops
  - restartability

Do **not** optimize for cheap.  
Optimize for **attention ROI**.

---

## 2. Core operating doctrine

The north star:

> One control room.  
> One source of truth.  
> One execution path.  
> One review artifact.  
> One deploy preview.  
> Everything else is optional, disposable, or demoted.

### Rules

- GitHub is the source of truth.
- Slack is the control room.
- ChatGPT is Ron’s private brain.
- Claude Code is the primary execution agent.
- Codex is secondary / reviewer / ChatGPT-native coding lane.
- Vercel is the default preview/deploy lane.
- GitHub PRs are the review artifact.
- GitHub Mobile Android is the current approval surface.
- Agents may create branches/PRs, but **must not merge without human approval**.
- Every real task must become:
  - a GitHub Issue
  - a GitHub PR
  - a GitHub comment
  - a GitHub doc change
  - or a closed/no-action decision

If it lives only in chat, it is not real work.

---

## 3. Minimal solo-mode flow

For now, assume Ron is operating mostly solo with agents. Contributors may arrive later, but the system must not depend on them.

### Main flow

```text
Idea / bug
→ Slack thread with @Claude
→ GitHub Issue or direct Claude Code task
→ Claude Code creates branch + PR
→ CI + Vercel Preview
→ Ron gets review card
→ Ron approves / rejects / asks for smaller PR
→ Merge
→ Restart note updated if needed
```

### Shareable version

```text
Idea → Slack @Claude → GitHub PR → Vercel Preview → Ron approves on phone → Merge
```

This is the simple diagram others can understand.

---

## 4. Tool ownership map

| Tool | Role | Status | Rule |
|---|---|---|---|
| GitHub | Source of truth | Keep | Owns issues, PRs, code, docs, decisions |
| Slack | Control room | Keep | Direct agent access and groupchat, not backlog |
| Claude Code | Primary execution agent | Keep | Writes code, creates PRs, runs tests |
| Claude Code in Slack / Claude Tag | Groupchat agent interface | Keep / watch | Use `@Claude` in Slack threads |
| Vercel | Preview/deploy lane | Keep | Every UI PR should have a preview |
| GitHub Mobile Android | Mobile approval surface | Keep | Use now for PR review/merge |
| ChatGPT | Private brain | Keep | Strategy, synthesis, prompts, research |
| Codex | Secondary coding/review lane | Keep secondary | Use from ChatGPT, not as primary OS |
| Cofounder.co | Optional agent-company cockpit | Bounded experiment | Do not let it become second OS |
| GitSwipe | Swipe GitHub triage | Watchlist | iOS now, Android “coming soon” |
| PullMatch | Candidate tool | Unverified | Investigate before adoption |
| Trello | Sprint board | Avoid | Only if developer insists, never source of truth |
| Miro | Visual snapshot | Avoid | Use only as generated snapshot, not memory |
| Lovable / v0 / Replit | Prototype lanes | Optional | Prototype must graduate to GitHub or die |
| Netlify / Railway / Render | Backup deploy lanes | Optional | Use only if Vercel is a poor fit |

---

## 5. Current recommended stack for Windows + Android

Ron’s actual tooling is Windows + Android.

Use now:

- Windows:
  - Claude Code
  - GitHub web
  - Vercel web
  - ChatGPT
  - Slack
- Android:
  - Slack Android
  - GitHub Mobile Android
  - ChatGPT Android
  - browser access to Vercel previews

Current best path:

```text
Slack Android
→ @Claude
→ GitHub PR
→ Vercel Preview
→ GitHub Mobile Android approval
```

Do **not** wait for a perfect swipe app.

---

## 6. Claude Code vs Codex

### Decision

Use **Claude Code as primary** and **Codex as secondary**.

### Why Claude Code primary

Claude Code is better aligned with:

- Slack control-room workflow
- direct groupchat agent access
- repo-aware execution
- branch/PR creation
- code review workflows
- persistent repo instructions
- agentic implementation

### Why Codex stays useful

Codex is valuable because:

- Ron’s life is in ChatGPT.
- It is good for second opinions.
- It is good for ChatGPT-native tasks.
- It can review Claude’s work.
- It can help turn research/thinking into implementation specs.

### Rule

Do not let Claude Code and Codex become two competing sources of truth.

Suggested division:

```text
Claude Code writes.
Codex reviews / compares / explains / handles ChatGPT-born tasks.
GitHub records truth.
```

---

## 7. Slack policy

Earlier “avoid Slack” was wrong.

Corrected position:

> Avoid Slack as backlog.  
> Use Slack as agentic control room.

Slack is valuable because the desired system needs:

- groupchat
- direct agent access
- human + agent coordination
- mobile-friendly interaction
- threads
- review cards
- quick buttons later

### Recommended channels

```text
#build-control-room
```

Private channel. One thread per task. `@Claude` works here.

```text
#build-deploys
```

Notification-only channel for GitHub/Vercel deploy status.

Optional later:

```text
#build-community
```

Community conversation only. Not execution.

### Slack rules

- One thread per task.
- Every serious thread links to a GitHub issue or PR.
- Slack can start work.
- GitHub must record work.
- Slack cannot be the backlog.
- Decisions that matter must be copied into GitHub.

---

## 8. PR review card

Every PR should include a founder review block.

Template:

```markdown
## Ron Review Block

### What changed?

1-3 bullets.

### Why does this matter?

1 sentence.

### Preview

- Vercel:
- Screenshots/video:

### Risk

Low / medium / high.

### Tests

- CI:
- Manual:

### Decision needed

Choose one:

- Approve
- Reject
- Request smaller PR
- Request human review
- Defer
```

The PR should be reviewable in 2 minutes.

If it cannot be reviewed in 2 minutes, it is probably too large or too vague.

---

## 9. Attention modes

### 2-minute mode

Allowed:

- approve one ready PR
- reject one unclear PR
- ask for smaller PR
- route one item to Claude
- defer one non-urgent thing

Not allowed:

- brainstorm
- compare tools
- read long logs
- enter dashboards
- redesign architecture

Goal:

> Change the state of one item.

### 5-minute mode

Allowed:

- clear top 3 founder decisions
- review one Vercel preview
- convert one thought into one GitHub issue
- trigger one Claude task
- update one next step

Goal:

> Reduce ambiguity.

### 30-minute weekly mode

Allowed:

- review what shipped
- choose one weekly theme
- kill irrelevant work
- queue next 3 agent-ready issues
- review risky changes
- update restart notes

Goal:

> Govern the system, not catch up on everything.

---

## 10. Swipe / Tinder-like approval UX

The desired UX is a review feed, not a dashboard.

Ideal card:

```text
Title
Summary
Preview screenshot
Risk
Tests
Buttons:
Approve / Reject / Smaller PR / Delegate / Defer
```

### Current finding

No mature Android-first “Tinder for agentic PR approval” tool has clearly won yet.

The pattern exists, but the market is early.

### GitSwipe

URL:

https://gitswipe.com/

Status:

- Verified.
- iOS app exists.
- Android says “Coming soon.”
- No release date found.
- Planning estimate for Android: **1-6 months, low confidence**.
- Do not wait for it.

Why it matters:

- GitSwipe turns GitHub notifications into swipeable cards.
- Supports archive/keep style triage.
- Shows GitHub timeline/context.
- Shows CI status.
- Supports inline diffs.
- Strong pattern match for Ron’s desired UX.

Decision:

- Add to tools watchlist.
- Create tracking issue.
- Re-check monthly.

### PullMatch

URL:

https://pullmatch.com/

Status:

- User-provided candidate.
- Not yet verified from reliable indexed public sources.
- Treat as candidate / unverified.

Decision:

- Add to tools watchlist.
- Investigate manually.
- Do not depend on it yet.

Questions:

- Does it support GitHub?
- Does it support Android or mobile web?
- Does it support approve/reject/review cards?
- Does it integrate with Slack?
- Does it preserve GitHub audit trail?
- Is it relevant to agentic PRs?

### Merge or Die

Status:

- Could not verify.
- Remove from active recommendations unless exact URL is found.

---

## 11. Swipe UX recommendation

Do not build a custom swipe app first.

Implement in stages:

### Stage 1: GitHub Mobile + Slack links

Use now.

```text
Slack review thread
→ GitHub PR
→ Vercel Preview
→ GitHub Mobile approval
```

### Stage 2: Slack review cards

Add structured Slack messages:

- summary
- preview link
- PR link
- CI status
- risk
- buttons or canned responses

### Stage 3: Slack modal

Build a Slack shortcut:

```text
Review next PR
```

Modal shows:

- PR summary
- issue link
- preview link
- risk
- test status
- screenshot
- actions

Buttons:

- Approve
- Request smaller PR
- Reject
- Open preview
- Open GitHub

For v1, merge should still happen in GitHub Mobile.

### Stage 4: Swipe PWA

Only build if Stage 2/3 is not enough.

Possible product:

```text
Ron Review Feed
```

A mobile-first feed over GitHub PRs, Slack threads, Vercel previews, and agent outputs.

---

## 12. Cofounder.co

Cofounder.co is interesting but dangerous as a second operating system.

It appears to provide:

- company-agent workspace
- departments
- tasks
- agents
- managed GitHub/Vercel/Supabase setup
- engineering agent
- Slack integration
- task status surface

This is powerful, but also creates a risk:

> Cofounder Tasks + GitHub Issues + Slack threads = three competing backlogs.

### Recommendation

Do **not** adopt Cofounder as the core OS now.

Use only as a bounded experiment if:

- testing its engineering agent on a small slice
- using it for non-engineering GTM/content loops later
- evaluating managed stack capabilities

Rules if used:

- GitHub remains canonical.
- Cofounder outputs must become GitHub PRs/docs/issues.
- Cofounder tasks must not become a second backlog.
- Use one bounded experiment, not full adoption.

---

## 13. Loop engineering

Loop engineering was not covered enough earlier. It is central.

### Definition

Loop engineering means designing reusable agent workflows instead of repeatedly prompting agents manually.

A loop has:

```text
trigger
→ goal
→ context
→ actions
→ verification
→ stopping rule
→ memory / handoff
→ escalation path
```

Ron should not keep inventing prompts.  
Ron should design loops that prompt agents.

### Why it matters here

Ron has low attention and high budget.

Therefore:

- agents should run loops
- loops should verify themselves
- loops should stop cleanly
- loops should escalate only when Ron is truly needed
- Ron should receive review cards, not raw logs

### Core loop rule

Every loop must answer:

```text
When does it start?
What does it produce?
How does it verify?
When does it stop?
When does it ask Ron?
Where is the result recorded?
```

---

## 14. First four loops to implement

Do not implement every possible automation.

Start with these four.

---

### Loop 1: Daily triage loop

Trigger:

- scheduled daily
- or manual Slack command

Goal:

- produce a tiny founder decision queue

Inputs:

- open PRs
- open issues
- failed CI
- stale branches
- Slack threads tagged needs-founder

Actions:

- identify top 3 decisions
- summarize each as a review card
- label GitHub items
- ignore everything else

Verification:

- every item links to a GitHub artifact
- no task exists only in Slack

Stopping rule:

- stop after top 3 items

Output:

```text
Ron Review Queue
1. Approve this PR
2. Request smaller PR here
3. Choose next agent-ready task
```

---

### Loop 2: Agent implementation loop

Trigger:

- issue labeled `agent-ready`
- Slack instruction to `@Claude`

Goal:

- one issue becomes one PR

Inputs:

- GitHub issue
- acceptance criteria
- repo context
- `CLAUDE.md`
- `AGENTS.md`

Actions:

- plan
- implement
- run tests
- create branch
- open PR
- write review block
- include preview if UI changed

Verification:

- tests pass or failures are explained
- PR is small
- risk is summarized
- acceptance criteria are checked

Stopping rule:

- one issue
- one branch
- one PR
- no merge

Output:

- GitHub PR
- Slack summary
- founder decision needed

---

### Loop 3: PR review loop

Trigger:

- PR opened or updated

Goal:

- reduce Ron’s review effort

Actions:

- summarize diff
- check tests
- check CI
- check preview
- identify risk
- recommend approve/reject/smaller PR

Verification:

- review references actual diff and CI
- preview exists for UI changes
- risky categories are flagged:
  - auth
  - billing
  - secrets
  - database migrations
  - permissions

Stopping rule:

- do not merge
- do not rewrite PR unless asked

Output:

- PR comment
- Slack review card

---

### Loop 4: Restart memory loop

Trigger:

- PR merged
- weekly review completed
- major decision made

Goal:

- make future re-entry easy

Actions:

- update `docs/RESTART.md`
- update `docs/DECISIONS.md` if needed
- list next smallest step

Verification:

- future Ron can understand current state in 2 minutes

Stopping rule:

- keep short
- no full history

Output:

- updated restart note

---

## 15. Repo files that should exist

Recommended files:

```text
CLAUDE.md
AGENTS.md
docs/RESTART.md
docs/DECISIONS.md
docs/OPERATING_SYSTEM.md
research/ATTENTION-FIRST-DEV.md
tools.md
.github/PULL_REQUEST_TEMPLATE.md
.github/ISSUE_TEMPLATE/tiny-task.yml
```

### CLAUDE.md

Purpose:

- tell Claude Code how to operate in this repo

Should include:

- one issue → one PR
- small PRs only
- no merge
- run tests
- write Ron Review Block
- update restart notes when needed

### AGENTS.md

Purpose:

- cross-agent operating rules for Claude, Codex, humans, and future tools

Should include:

- allowed actions
- forbidden actions
- verification requirements
- escalation rules

### docs/RESTART.md

Purpose:

- make re-entry possible in 2 minutes

Should include:

- current state
- next smallest step
- blocked items
- recent decisions

### docs/DECISIONS.md

Purpose:

- durable decision log

Should include:

- date
- decision
- reason
- reversible or irreversible
- next review date if needed

---

## 16. GitHub labels

Recommended labels:

```text
needs-founder
agent-ready
blocked
ready-for-review
ready-to-merge
needs-preview
risky
small-pr-required
killed
wait-24h
tool-watchlist
swipe-ux
loop-engineering
```

---

## 17. Tooling requirements

### GitHub

Required:

- branch protection on main
- required PR review
- PR template
- issue template
- labels above
- no direct pushes to main

### Slack

Required:

- private `#build-control-room`
- one thread per task
- Claude installed
- GitHub app installed
- Vercel notifications installed

### Claude Code

Required:

- Windows setup
- GitHub repo connected
- Slack enabled
- `CLAUDE.md`
- safe permissions
- no auto-merge

Recommended skills / commands:

- review-card
- verify-preview
- summarize-pr
- restart-note
- small-pr-enforcer

### Vercel

Required:

- GitHub integration
- PR preview deployments
- preview link in PRs
- failure notifications

### Android

Required:

- Slack Android
- GitHub Mobile Android
- ChatGPT Android
- browser access to Vercel

Optional:

- GitSwipe Android when available

---

## 18. Mood and energy resilience

The system must work when Ron is:

- tired
- distracted
- low-energy
- high-energy
- returning after a gap
- excited by a new tool
- tempted to pivot

Rules:

- no irreversible architecture/tool decision in high-energy state
- major pivots wait 24 hours
- new recurring tools require explicit attention-cost justification
- every session ends with next smallest step
- no task without owner/status/next action
- if a thread feels exciting but creates no artifact, it is not progress

Useful label:

```text
wait-24h
```

Use it for:

- new tool adoption
- architecture shifts
- big pivots
- emotionally charged decisions

---

## 19. Contributor posture

Current mode:

```text
solo founder + agents
```

Future contributors are welcome, but the system must not depend on them.

Contributor rule:

- contributors interact through GitHub issues/PRs
- Slack can coordinate
- GitHub records work
- PRs must include review block
- no contributor creates a private backlog

The founder should not onboard people into a complex system yet.  
The system should be understandable as:

```text
Pick issue → make PR → preview → Ron approves
```

---

## 20. What to kill or demote now

Kill for now:

- Trello
- Miro
- complex GitHub Projects
- bidirectional sync
- multi-tool dashboards
- “let’s maintain a roadmap board” energy

Demote:

- Cofounder.co
- Lovable
- v0
- Replit
- Netlify
- Railway
- Render

These may be useful, but none should become the OS.

---

## 21. First 10 tiny implementation steps

1. Create `research/ATTENTION-FIRST-DEV.md`.
2. Create `CLAUDE.md`.
3. Create `AGENTS.md`.
4. Create `docs/RESTART.md`.
5. Create PR template with Ron Review Block.
6. Add GitHub labels:
   - `needs-founder`
   - `agent-ready`
   - `ready-for-review`
   - `needs-preview`
   - `blocked`
   - `killed`
7. Set up branch protection on `main`.
8. Connect repo to Vercel.
9. Create private Slack channel `#build-control-room`.
10. Run one complete loop:
    - Slack `@Claude`
    - PR
    - Vercel Preview
    - GitHub Mobile Android approval

---

## 22. First GitHub issues to create

### Issue 1: Track GitSwipe Android

```markdown
Title: Track GitSwipe Android release

Goal:
Evaluate GitSwipe once Android is available.

Tasks:
- Check https://gitswipe.com monthly
- Check Google Play availability
- Test GitHub notification triage
- Test PR review usefulness
- Decide whether it reduces founder attention cost

Status:
Watchlist. Do not block current workflow.
```

### Issue 2: Investigate PullMatch

```markdown
Title: Investigate PullMatch

URL:
https://pullmatch.com/

Goal:
Determine whether PullMatch is relevant to swipe-style PR review or agentic development workflow.

Questions:
- Is the product live?
- Does it support GitHub?
- Does it support Android or mobile web?
- Does it support approve/reject workflows?
- Does it integrate with Slack?
- Does it preserve GitHub audit trail?
- Is it useful for agent-created PRs?

Status:
Candidate / unverified.
```

### Issue 3: Create Ron Review Block PR template

```markdown
Title: Add PR template optimized for 2-minute founder review

Goal:
Every PR should be reviewable in 2 minutes.

Acceptance criteria:
- PR template includes summary
- preview link
- risk level
- test status
- exact decision needed
- smaller PR escape hatch
```

### Issue 4: Implement Daily Triage Loop

```markdown
Title: Implement daily triage loop

Goal:
Produce a daily top-3 founder decision queue.

Output:
Slack message or GitHub comment with:
1. approve/reject item
2. blocked item
3. next agent-ready task

Constraint:
Do not summarize the whole project.
```

---

## 23. Final recommendation

Do not build the perfect OS.

Build this:

```text
Slack + Claude Code
→ GitHub PR
→ Vercel Preview
→ GitHub Mobile Android approval
→ Restart note
```

Then add loops.

Then add swipe UX only if the current approval path is still too heavy.

The correct system is not “more project management.”  
It is **agentic execution with founder approval cards**.

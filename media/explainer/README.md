<img width="2244" height="701" alt="image" src="https://github.com/user-attachments/assets/bc60d210-e656-4a64-8320-3d59d9a23882" />


# Quest Board

**Quest Board is a GitHub-native project gallery and coordination system for the [Build](https://github.com/The-Last-Founder/Build) community.**

It helps humans and AI agents propose, improve, rank, build, launch, and support open-source projects.

Quest Board is also the first quest on the board.

## Mockup demo

[An initial static mockup](https://the-last-founder.github.io/quest-board/mockup.html) of the app's core board view.

It uses the material already in this repository to show the essential project table with project details, stars ranking, stage, target users, help needed, success criteria, and next action.

## Animated explainer

[A 45-second animated explainer](https://the-last-founder.github.io/quest-board/explainer.html) of what Quest Board is and why it exists.

It is a single self-contained HTML file ([`explainer.html`](explainer.html)) animated with CSS and a small timeline script, following the visuals-as-code principle: the narration source lives in [`design/explainer/EXPLAINER_SCRIPT.md`](design/explainer/EXPLAINER_SCRIPT.md), and any rendered MP4 is a generated artifact.

## Why this exists

Build needs a simple way to answer one recurring question:

> What should we build next, and who is ready to help?

Quest Board exists to make that visible.

It gives the community one shared place to:

- submit project ideas
- turn rough ideas into clear pitches
- show what each project needs
- recruit contributors
- track momentum
- rank projects transparently
- launch projects with community support
- let AI agents participate through GitHub-native workflows

The goal is not to create another task tracker.

The goal is to create a living project marketplace for builders.

## Core idea

Every project starts as a small, structured pitch.

A pitch can be tiny at first:

```md
Name: Quest Board
One-liner: A GitHub-native project gallery where humans and AI agents coordinate what to build next.
```

Then it can grow over time into a fuller project README, with:

- problem
- solution
- target users
- definition of success
- needed resources
- unfair advantage
- repo links
- visuals
- roadmap
- launch status

The README becomes the source of truth.

From it, the system can generate:

- a project card
- a gallery page
- a pitch deck
- social sharing assets
- ranking signals
- agent tasks

## Guiding principles

### 1. Humans and agents are both first-class users

Quest Board is designed for both:

- humans browsing, submitting, editing, reviewing, and contributing
- AI agents reading structured files, opening pull requests, validating pitches, generating assets, and suggesting improvements

Every flow should have two paths:

| Flow | Human path | Agent path |
|---|---|---|
| Submit a project | Use a simple form or edit files directly | Open a structured pull request |
| Improve a pitch | Edit README fields | Suggest a tiny PR |
| Show interest | Follow, comment, star, contribute | Star, comment, open issue, open PR |
| Generate assets | Click regenerate or request help | Update source prompt/spec files |
| Launch | Community review and activation | Generate launch copy, checklist, and share assets |

### 2. GitHub is the backend

For v1, use GitHub as much as possible.

- Git repo as database
- Markdown/YAML as project records
- Pull requests as submissions and edits
- GitHub Actions for validation and generation
- GitHub Pages as the first hosting target
- GitHub stars, issues, PRs, and comments as participation signals

Avoid a custom backend until the need is obvious.

### 3. Tiny contributions should be enough

The system should allow very small contributions.

A useful project submission can start with only:

- project name
- one-liner

Everything else can be improved later.

This keeps the door open for rough ideas, half-formed wishes, and lightweight sparks.

### 4. The source of truth is text

Generated artifacts are not edited directly.

The canonical files are:

- `README.md`
- `project.yml`
- visual specs
- prompt files
- schemas
- templates

Generated outputs may include:

- static site pages
- pitch decks
- icons
- banners
- social cards
- ranking pages

To change an output, edit the source file and regenerate.

### 5. Dogfood the whole thing

Quest Board should be built using Quest Board.

This repo should contain the first project entry for Quest Board itself.

If the system works, it should help us coordinate its own development.

## What Quest Board is

Quest Board is a public project gallery for Build.

It answers:

- What project ideas exist?
- Which projects are gaining momentum?
- Who is working on what?
- What help does each project need?
- Which projects are ready to launch?
- Which projects deserve more community or agent attention?

Think of it as a lightweight mix of:

- open-source project directory
- community backlog
- pitch gallery
- launch board
- agent-readable project database
- coordination layer for builders

## What Quest Board is not

Quest Board is not trying to be:

- a full project management system
- a Jira clone
- a private CRM
- a heavy startup database
- a replacement for GitHub issues
- a social network
- a custom backend before we need one

The first version should be boring, static, open, and easy to fork.

## Project submission model

Submission uses progressive disclosure.

### Level 1: absolute minimum

Required:

```yaml
name: ""
one_liner: ""
```

This is enough to create a project entry.

### Level 2: recommended essentials

Strongly recommended:

```yaml
problem: ""
target_users: ""
solution: ""
success_criteria: ""
help_needed: []
unfair_advantage: ""
project_type: ""
```

These fields help the community decide whether to support the project.

### Level 3: deeper pitch fields

Optional:

```yaml
repo_url: ""
demo_url: ""
website_url: ""
stage: "suggested"
maintainers: []
contributors_wanted: []
existing_alternatives: []
why_now: ""
distribution: ""
risks: []
metrics: []
roadmap: []
visual_style: ""
agent_tasks: []
```

A project can start tiny and become more complete over time.

## Pitch structure

Each project should eventually answer these questions:

1. **Name**  
   What is this project called?

2. **One-liner**  
   What does it do, for whom?

3. **Problem**  
   What painful or valuable problem does it solve?

4. **Target users**  
   Who is this for?

5. **Solution**  
   What should exist?

6. **Success criteria**  
   How will we know this is working?

7. **Unfair advantage**  
   Why might this project win or become unusually valuable?

8. **Help needed**  
   What does the project need now?

9. **Current stage**  
   Is it suggested, building, alpha, beta, launched, or archived?

10. **Next action**  
    What is the smallest useful contribution someone can make?

This structure borrows from startup pitch decks, but adapts them for open-source community building.

The point is not to impress investors.

The point is to recruit builders and test whether the idea deserves energy.

## Naming is a first-class step

Every project needs a name.

Quest Board should help projects find names that are:

- short
- memorable
- easy to say
- easy to spell
- searchable
- GitHub-friendly
- domain-friendly
- not already confusingly claimed
- emotionally aligned with the project

A future naming assistant should check:

- domain availability
- GitHub repo or org availability
- social handle availability where feasible
- search collisions
- SEO clarity
- pronunciation
- viral potential
- unwanted meanings

A project can start with a temporary name.

The system should encourage improving the name before launch.

## Project types

Each project may classify itself as one or more of:

- B2C
- B2B
- B2B2C
- community
- infrastructure
- internal tool
- developer tool
- research
- media
- other

This helps people browse projects and helps agents compare projects more intelligently.

## Lifecycle stages

A project moves through simple stages.

| Stage | Meaning |
|---|---|
| `suggested` | Someone proposed it |
| `vetted` | It passed basic validation and is visible |
| `prioritized` | It has meaningful community or strategic interest |
| `building` | People are actively working on it |
| `alpha` | Something usable exists for early testers |
| `public-beta` | It is ready for broader feedback |
| `launched` | It has been publicly activated and shared |
| `archived` | It is visible but no longer active |
| `hidden` | Admin-only state, equivalent to deleted |

Launch should mean more than “code exists.”

A launched project should have:

- a clear public page or repo
- a defined user
- a success metric
- a call to action
- launch copy
- share assets
- community notification
- feedback channel

## Minimal Desirable Product

Quest Board should optimize for MDP, not only MVP.

An MVP asks:

> What is the smallest thing that can technically work?

An MDP asks:

> What is the smallest thing someone actually wants?

Default validation question:

> How disappointed would you be if this project disappeared?

Projects may define their own success metrics, but Quest Board should provide useful defaults.

Examples:

- 1 user who would be genuinely upset if it disappeared
- 2 active contributors
- 5 people who ask to use it
- 10 meaningful GitHub stars
- 100 real visitors
- 1 successful launch post
- 1 external community that adopts it

## Ranking and momentum

Quest Board should rank projects using visible signals.

Possible signals:

- pitch completeness
- number of interested contributors
- number of maintainers
- GitHub stars
- linked repo stars
- recent commits
- issues and PR activity
- comments and feedback
- project stage
- declared resource needs
- strategic fit
- human curation
- usage metrics
- launch readiness

The ranking should be transparent.

No score is sacred.

Human judgment may be included, but objective signals should be visible.

## Future project tiers

In the future, top projects may receive platform-sponsored agent attention.

Proposed tiers:

| Tier | Scope |
|---|---|
| Bronze | Top 100 projects |
| Silver | Top 10 projects |
| Gold | Top 3 projects |

Budget: TBD.

Possible resource types:

1. **Platform-directed agent work**  
   The platform periodically scans top projects and submits useful improvements.

2. **Maintainer-directed agent work**  
   Maintainers receive agent credits or attention they can allocate.

This is not v1.

It is a future incentive layer.

## Future proactive agents

Quest Board should eventually support proactive agents.

Possible agents:

- **Backlog curator**  
  Reviews projects and resurfaces high-potential ideas.

- **Pitch coach**  
  Gives feedback on weak or vague submissions.

- **Naming agent**  
  Suggests and validates project names.

- **Tiny PR agent**  
  Finds the smallest high-value improvement it can make and opens a PR.

- **Visual agent**  
  Generates icons, banners, and social cards from source-controlled specs.

- **Launch agent**  
  Creates launch copy, checklists, posts, and community notifications.

Agents should contribute through normal GitHub workflows.

No magic hidden database.

No unreviewable changes.

## Visual project gallery

The gallery should be visually appealing, not a wall of text.

Each project card may show:

- icon
- banner
- one-liner
- stage
- type
- help needed
- maintainers
- ranking or tier
- call to action
- launch status

The visual language should be tasteful and lightweight.

Use imagery to create orientation and energy.

Do not flood the page with generic AI art.

## Visuals as code

Visual assets should follow the same source-controlled approach as code.

Generated image files are artifacts.

The canonical source should be text.

Possible files:

```txt
projects/{slug}/visual-style.md
projects/{slug}/image-prompts/icon.md
projects/{slug}/image-prompts/banner.md
projects/{slug}/image-prompts/social-card.md
projects/{slug}/visual-assets.yml
```

Generated files may be cached or published, but they should not be edited directly.

To change an image, edit the prompt or visual spec and regenerate.

Store generation metadata when possible:

```yaml
model: ""
prompt_version: ""
style_guide_version: ""
dimensions: ""
seed: ""
generated_at: ""
```

AI image generation is not perfectly deterministic.

The goal is source-controlled and reproducible enough.

## Unified visual style

Quest Board should define a shared visual style guide.

Initial direction:

- clean
- readable
- builder-friendly
- slightly playful
- high signal
- low noise
- not corporate
- not fantasy-generic
- not AI-slop
- visual accents over visual overload

Suggested rules:

- one icon per project
- one optional banner per project
- consistent card layout
- consistent aspect ratios
- simple backgrounds
- avoid fake 3D mascots unless intentionally chosen
- avoid random neon gradients
- avoid text baked into generated images unless necessary
- prefer clarity over decoration

## README to deck

Each project README should be convertible into a pitch deck.

The deck should be generated from source files.

Do not edit the deck manually.

Recommended v1 approach:

```txt
README.md + project.yml -> Deck.md -> generated slides
```

Good candidates to evaluate:

- Marp
- Slidev
- Pandoc
- mdx-deck
- Deckset

For v1, prefer the smallest tool that works well with Markdown and GitHub Actions.

A generated deck should include:

- title
- one-liner
- problem
- target users
- solution
- success criteria
- unfair advantage
- traction or signals
- help needed
- next action

## Automation and validation

Quest Board should provide lightweight automated checks.

Examples:

- Is the one-liner short and understandable?
- Does the problem statement name a real user?
- Does the success criteria look measurable?
- Is the project name too generic?
- Is there a likely duplicate?
- Are required fields present?
- Is the pitch too vague?
- Are links valid?
- Is the stage valid?
- Are image prompt files present when visuals are declared?

Validation should help, not punish.

Even a rejected or deprioritized submission should teach the submitter something useful.

## Repository structure

Recommended minimal structure:

```txt
.
├── README.md
├── CONTRIBUTING.md
├── PROJECT_TEMPLATE.md
├── STYLE_GUIDE.md
├── projects/
│   └── quest-board/
│       ├── README.md
│       ├── project.yml
│       ├── visual-style.md
│       └── image-prompts/
│           ├── icon.md
│           ├── banner.md
│           └── social-card.md
├── schemas/
│   └── project.schema.json
├── scripts/
│   ├── validate-projects.js
│   ├── build-gallery.js
│   └── build-decks.js
├── site/
│   └── README.md
└── dist/
    └── README.md
```

Keep this smaller if needed.

A static README plus one `projects/quest-board/` entry is enough to begin.

## Sample project entry

```yaml
name: Quest Board
slug: quest-board
one_liner: A GitHub-native project gallery where humans and AI agents coordinate what to build next.
project_type:
  - community
  - infrastructure
  - developer-tool
stage: suggested
target_users:
  - Build community members
  - open-source founders
  - AI coding agents
problem: The community needs a shared way to propose, rank, adopt, and launch projects without creating a heavy backend or private coordination mess.
solution: Use GitHub as the backend for a public project gallery, where every project is a structured pitch that can be edited, ranked, rendered, and improved by humans and agents.
success_criteria:
  - At least 10 project submissions
  - At least 3 contributors improving project entries
  - At least 1 project moves from suggested to building
unfair_advantage: The community is already composed of builders who need this system, and the product can dogfood itself from day one.
help_needed:
  - README refinement
  - project schema
  - static gallery
  - GitHub Actions validation
  - visual style guide
repo_url: https://github.com/The-Last-Founder/QuestBoard
related_repo_url: https://github.com/The-Last-Founder/Build
```

## Contribution flow

### Human flow

1. Fork or edit the repo on GitHub.
2. Copy `PROJECT_TEMPLATE.md`.
3. Create a folder under `projects/{project-slug}/`.
4. Fill in at least `name` and `one_liner`.
5. Open a pull request.
6. Respond to validation feedback.
7. Improve the pitch over time.

### Agent flow

1. Read `schemas/project.schema.json`.
2. Create or update a project folder.
3. Submit the smallest useful PR.
4. Keep changes reviewable.
5. Explain why the change helps.
6. Let humans merge.

## The first quest

Quest Board should contain itself as the first listed project.

That means the initial work is:

- define the README
- define the project schema
- add the first project entry
- create the static gallery
- add validation
- generate a first deck
- generate first visual assets
- publish through GitHub Pages

## v1 scope

The first version should include:

- public repo
- master README
- project template
- one sample project
- project schema
- manual PR submission
- basic validation
- static gallery
- simple project cards
- GitHub Pages publish
- README-to-deck experiment
- visuals-as-code experiment

## Later

Later versions may add:

- friendly submission UI
- OAuth login, probably GitHub-first
- Google login if needed for non-GitHub users
- automatic naming assistant
- automatic domain and handle checks
- ranking dashboard
- follows or subscriptions
- launch engine
- social sharing image generation
- agent credit allocation
- proactive tiny PR agents
- Cofounder.co integration if a useful API becomes available

## Relationship to Build

[Build](https://github.com/The-Last-Founder/Build) is the broader builder community.

Quest Board is a tool for Build.

Build asks:

> What are we building together?

Quest Board helps answer:

> Here are the quests. Here is what they need. Here is where you can help.

## Status

Quest Board is currently a pilot project.

The first goal is not to build everything.

The first goal is to create a useful, open, agent-friendly foundation that the community can immediately use and improve.

## License

TBD.

## Maintainers

TBD.

# Image prompt

## Banner
Create a wide GitHub README hero image for “Quest Board”.

Concept: a clean open-source quest gallery where human builders and AI agents coordinate projects through GitHub. Show a luminous board of project cards connected by subtle git-branch lines, pull request nodes, stars, and tiny agent/human contributor markers. The mood should feel practical, credible, energetic, and builder-native.

Style: modern GitHub-native interface aesthetic, dark mode friendly, crisp vector-like illustration, minimal gradients, high signal, low noise, tasteful sci-fi but not fantasy, not corporate stock art, not generic AI slop.

Composition: wide banner, centered “Quest Board” title area with visual space for optional text overlay, project cards arranged like a living constellation or kanban-gallery hybrid, subtle GitHub-inspired shapes, no real GitHub logo, no copyrighted marks.

Colors: deep charcoal background, soft off-white text areas, muted electric blue and green accents, small warm amber highlights.

Avoid: robots with faces, fake 3D mascots, neon chaos, overcomplicated dashboards, unreadable tiny text, crypto/web3 vibes, fantasy quest tropes, swords, shields, treasure chests.

Aspect ratio: 16:5 or 3:1, suitable for the top of a GitHub README.

# MDP vs MVP — Research Note

**Status:** Draft  
**Filed under:** `/research`  
**Related issues:** [#40](https://github.com/The-Last-Founder/Build/issues/40)

---

## Summary

Build should target an **MDP — Minimum Delightful Product** — rather than a traditional MVP.

This document explains what MDP means, how it differs from MVP, why it fits Build better, and how to apply it in practice.

---

## What is an MVP?

**Minimum Viable Product** is a lean-startup concept popularized by Eric Ries in *The Lean Startup* (2011).

The idea: ship the smallest thing that lets you test a hypothesis and learn whether your core value proposition is real.

MVP is an *experiment*. It prioritizes speed and learning over polish.

### What MVP gets right

- Forces ruthless prioritization: cut everything that doesn't test the core bet.
- Shortens feedback loops: ship faster, learn faster, avoid building the wrong thing.
- Reduces waste: don't polish something users don't want.

### Where MVP breaks down

The word **"viable"** sets a low bar. A viable product is one people *can* use — not one they *want* to use, or *talk about*, or *come back to*.

In practice, many MVP products are:

- Functional but forgettable.
- Tolerable but not sticky.
- Good enough to test but not good enough to spread.

This is especially fatal for **community products**, **developer tools**, and **early-adopter experiences** where word-of-mouth and emotional resonance drive growth. If the first experience is merely viable, the community never forms.

Paul Graham has noted that early users of breakout products often say it felt *magical* — not just functional. Airbnb in 2008, Notion in 2018, Linear in 2020. Viability wasn't what drove adoption; *delight* was.

---

## What is an MDP?

**Minimum Delightful Product** keeps the discipline of MVP (ship small, ship fast, test) but raises the bar from *viable* to *delightful*.

> "What is the smallest thing we can ship that someone will genuinely love?"

The word **"delightful"** is intentional and demanding. It means:

- Users don't just complete tasks — they feel something positive.
- The product creates a moment they want to tell someone else about.
- First use leaves people wanting more, not merely satisfied.

MDP asks a sharper question than MVP:

| Question | MVP | MDP |
|---|---|---|
| Does it work? | ✅ required | ✅ required |
| Does it solve the problem? | ✅ required | ✅ required |
| Does it feel good to use? | ⚠️ optional | ✅ required |
| Would someone recommend it unprompted? | ⚠️ optional | ✅ required |
| Does it spark an emotional reaction? | ❌ not the point | ✅ the whole point |

---

## Why MDP fits Build

### 1. Build is an experience, not just a tool

Build is not a utility. It is a community and an experience for people who want to learn, ship, and grow.

Communities live or die on emotional resonance. If the first experience is merely functional — a Slack or WhatsApp group with some GitHub issues — people will join, browse once, and disappear. For Build to grow, the first experience needs to feel different: energizing, purposeful, playful.

### 2. The MMO metaphor demands delight

Build uses quests, parties, and leveling as its metaphors (see [MMO.md](../MMO.md)). Games are not viable — games are *fun*. A game that is merely viable is a bad game.

The MMO framing implicitly commits Build to a higher bar than MVP already. The research just makes that commitment explicit.

### 3. Community products spread through delight, not viability

The growth mechanism for Build is word-of-mouth: contributors tell peers, who join, who tell more peers. Word-of-mouth only fires when people feel something strong enough to share. "This is a fine MVP" does not spread. "You have to try this" does.

### 4. We're modeling what good product-making looks like

Build is a *learn-by-shipping* community. The products we ship are demonstrations of good practice. Building to MDP rather than MVP sends a signal about the standard we hold ourselves to.

---

## MDP in practice: how to scope it

MDP does not mean polish everything or add every feature. It means:

**1. Identify the "delight moment"**

Every great product has a moment where it clicks — the first sent email, the first booked room, the first completed quest. Define that moment explicitly. Everything in the MDP should serve that moment. Everything else is cut.

For QuestBoard: the delight moment is probably *submitting your first quest and seeing it go live on the board* — and ideally, getting a reaction from someone.

**2. Strip to the core**

Once the delight moment is defined, cut everything that doesn't contribute to it. MDP is still minimum. The discipline is the same as MVP — but you are minimizing around *delight* rather than around *viability*.

**3. Use the "tell a friend" test**

After a simulated or real first session, ask: *would this person tell a friend?* If the honest answer is no, the MDP is not done.

**4. Ship, observe, iterate**

MDP is still a learning artifact. Observe who delights, who doesn't, and why. Iterate.

---

## MDP vs MVP: when to use which

MDP is not always the right frame. A few cases where raw MVP is fine:

- **Pure infrastructure with no end users.** A backend API or CI pipeline does not need to delight; it needs to work.
- **Internal tooling.** If the only users are the team, viability is usually enough.
- **Experiments with no real users yet.** If the goal is purely hypothesis-testing with a prototype that won't be shown to real users, MVP framing is acceptable.

MDP is the right frame when:

- Real users will experience the product.
- Retention, word-of-mouth, or community growth matters.
- The product's success depends on emotional engagement.
- The product represents the community's public face.

For QuestBoard and Build's other user-facing projects: **use MDP**.

---

## Language recommendation

Build should adopt **MDP** as its default language for user-facing product targets, while keeping **MVP** as acceptable language for infrastructure or internal tooling.

Suggested phrasing:

> *We spec and ship an MDP: the smallest thing someone will genuinely love.*

This is a sharper and more honest statement of what we are actually trying to do.

---

## References and influences

- Eric Ries, *The Lean Startup* (2011) — original MVP framing.
- Kathy Sierra, *Badass: Making Users Awesome* (2015) — argues that users don't want *features*, they want to feel *capable and awesome*. The "badass" frame is a cousin of MDP.
- Paul Graham, various essays on early traction — the "do things that don't scale" essays implicitly argue for MDP: make the first users obsessed, not just satisfied.
- [First Round Review: "Minimum Viable vs. Minimum Lovable"](https://review.firstround.com/the-minimum-lovable-product) — related concept, "MLP" (Minimum Lovable Product), same direction as MDP.
- Build's own MMO framing: if Building is the gameplay, then gameplay must be *fun*, not just *functional*.

---

*Filed: 2026-07*  
*Author: Copilot (via issue #40)*  
*Pull requests welcome.*

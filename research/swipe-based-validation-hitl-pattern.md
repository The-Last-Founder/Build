# Swipe-Based Validation as a Human-in-the-Loop (HITL) Pattern

Source: Build issue [#53](https://github.com/The-Last-Founder/Build/issues/53), PR comment by @ripper234 (comment id: `4904654180`).

## Summary

In agentic UX, this pattern is called **swipe-based validation**.

The agent can discover a candidate action, but if execution risk is high it pauses and asks for human approval. A swipe interaction (approve/reject) keeps context centered, makes decisions fast, and chains directly into the next queued decision.

This is expected to become common in domains where automation is strong but human sign-off is still required (for example: medical, hiring, and investments).

## Operational model

A useful production default is:

- **Autonomy on reads**: agents can fetch/analyze/draft.
- **Human-in-the-loop on writes**: send/update/delete/pay actions require review.

Reported outcome: teams that moved from full autonomy to this model saw higher engagement because users felt in control.

## Architecture pattern: approval queue

Under the swipe UX is a standard approval queue:

1. Agent proposes an action.
2. Action is added to a pending queue with full context.
3. Agent waits.
4. Human approves/rejects/edits.
5. Only approved actions execute.

Infra note from the source: **LangGraph interrupts + checkpoints** can make this pause durable so execution resumes from the exact stop-point after refresh/reconnect.

## Design rules

- Require confirmation only for meaningful consequences.
- Show exactly what the action will do.
- Add timeouts (auto-reject or escalate).
- Keep a complete audit trail.
- Include **edit**, not only accept/reject.
- Use inline editable chips and confidence labels (for example: `Confident` / `Needs review`).

## Primary risk

The key risk is **default-accept bias**:

- People may accept AI suggestions they only partially agree with because acceptance is the lowest-friction action.
- Swipe UX can amplify this effect.
- Destructive/high-impact actions should stay out of the fast swipe lane.

## Practical implication for product design

If building this into a product flow (for example Fredo), model swipe UI as a thin interaction layer over a durable approval queue, and keep higher-risk actions behind stricter review UX.

## Open follow-up

Potential next artifact: comparison table of implementation options (for example LangGraph vs Cloudflare vs HumanLayer) for this HITL approval pattern.

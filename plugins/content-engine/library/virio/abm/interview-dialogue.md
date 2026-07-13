# Interview dialogue

- **Archetype**: a staged interview exchange at a named company, used to teach a technical/domain concept through back-and-forth
- **Funnel stage**: BOFU
- **ABM mechanic**: the named company's hiring bar becomes the stage — their engineers and every candidate targeting them engage. Positions the author as someone who thinks at that company's level.
- **Platform**: LinkedIn
- **Source examples**: (refreshed by the scheduled library-refresh task; pinned entries never auto-replaced)
  - https://www.linkedin.com/posts/srgrace_ai-genai-llms-activity-7390394713264021505-YrId — Sourav Verma, 1,143 reactions / 33 comments, Nov 2025 (GenAI engineer interview at Cohere)
  - https://www.linkedin.com/posts/pawel-huryn_agents-are-the-most-valuable-skill-in-ai-activity-7339343474720178176-EiiQ — Paweł Huryn, 4,175 reactions, Jun 2025 (step-by-step agent build, resource-dense variant)
- **Hook pattern**: "The interview is for a {role} at {company}." — then straight into dialogue
- **Skeleton**:
  1. One-line scene set naming the role and company
  2. Interviewer question (the naive framing)
  3. Candidate answer (crisp, correct, quotable)
  4. Escalating follow-ups (3–4 rounds), each punching a common misconception
  5. The synthesis answer — the mental model, stated plainly
  6. Optional resource block or takeaway line
- **Rhythm & formatting**: 200–350 words; "Interviewer:" / "You:" labels; answers 2–4 lines max; the escalation carries the pacing.
- **Why it works**: dialogue is inherently scannable, the named company supplies stakes, and readers self-test against each question — comment bait built in.
- **Adaptation notes**: company must be one the ICP would interview at (or the client's own hiring bar — the warmest version: "the interview is for a role at {client}"). Concept must survive expert scrutiny.
- **Watch-outs**: technical errors get destroyed by actual employees of the named company; keep the dialogue plausible — no strawman interviewers.

## Top example — full post text
Source: https://www.linkedin.com/posts/srgrace_ai-genai-llms-activity-7390394713264021505-YrId (Sourav Verma, 1,143 reactions)

```
The interview is for a Generative AI Engineer role at Cohere.

Interviewer: "Your client complains that the LLM keeps losing track of earlier details in a long chat. What's happening?"

You: "That's a classic context window problem.
 Every LLM has a fixed memory limit - say 8k, 32k, or 200k tokens.
 Once that's exceeded, earlier tokens get dropped or compressed, and the model literally forgets."

Interviewer: "So you just buy a bigger model?"

You: "You can, but that's like using a megaphone when you need a microphone.
A larger context window costs more, runs slower, and doesn't always reason better."

Interviewer: "Then how do you manage long-term memory?"

You:
  1. Summarization memory - periodically condense earlier chat segments into concise summaries.
  2. Vector memory - store older context as embeddings; retrieve only the relevant pieces later.
  3. Hybrid memory - combine summaries for continuity and retrieval for precision.

Interviewer: "So you're basically simulating memory?"

You: "Yep.
LLMs are stateless by design.
You build memory on top of them - a retrieval layer that acts like long-term memory.
Otherwise, your chatbot becomes a goldfish."

Interviewer: "And how do you know if the memory strategy works?"

You: "When the system recalls context correctly without bloating cost or latency.
 If a user says, 'Remind me what I told you last week,' and it answers from stored embeddings - that's memory done right."

Interviewer: "So context management isn't a model issue - it's an architecture issue?"

You: "Exactly.
 Most think 'context length' equals intelligence.
 But true intelligence is recall with relevance - not recall with redundancy."

#ai #genai #llms #rag #memory
```

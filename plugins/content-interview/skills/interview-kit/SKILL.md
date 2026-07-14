---
name: interview-kit
description: Prep and run a client content interview end to end. Use when the user says "prepare for a content interview with [name]", "prep the interview for [client]", "research [name] for the interview", "run a content interview", "interview questions for [client]", "first content interview", "next content interview", or wants question banks by funnel stage for interviewing a client's Face of Content. Researches the FOC in Virio (their strategy, tone, ICPs, banned topics) plus their recent LinkedIn posts, then builds a tailored question set instead of a generic one. Produces the interview brief, the live question flow, and capture guidance; the transcript hands off to idea-inventory.
---

# Content interview kit

Interview the client's Face of Content (FOC) to extract unique, POV-based insights from their stories and anecdotes. The FOC is the expert on their company, product, industry, and ICP; you are the expert on the platform, hooks, and what makes good content. The goal of the interview is to let the FOC shine — the goal of translating it into content is to make them shine online.

Operate under the assumption that you are interviewing an extremely interesting person. Interesting answers come from interesting questions. Interviewing is a skill.

## Prep research — run this BEFORE choosing any questions

"Prepare for a content interview with [name]" starts here. Never walk in with the raw bank: research the FOC first, then cut and tailor. A question the record already answers is a wasted minute of their time.

**1. Resolve the FOC.** Call `content_publishers_list` (Virio) and match the name or email. Several matches → show them and ask which. No match → say so plainly, then fall back to the no-connector path below. Never guess who you're interviewing.

**2. Pull their record.** Call `content_settings_get` for that publisher. This is read-only — never call a `content_*_update` tool from this skill. Extract:

- **Strategy** — company overview and stage, active `topics`, `bannedTopics`, cadence, pipeline share
- **Tone** — formality, rhythm, banned phrases, hard rules (em-dashes, hashtags, exclamations), AI-tells, and `customInstructions` (voice notes plus any dismissed topics)
- **ICPs** — each persona's titles, company size, funding, location, description
- **Provenance** — who last set each section and when. Stale or agent-set sections are exactly what the interview should re-confirm.

**3. Read what they've already said.** Use `read_linkedin_uri` on their LinkedIn profile to pull recent posts. Note the topics they've already covered, the stories they've already told, and what performed. The interview mines new ground; it does not re-run their greatest hits.

**4. Account context** (only if HubSpot or Attio is connected). Search the company for industry, size, deals, and named accounts.

**5. Write the interview brief**, then the question set:

- **Already on file — validate, don't re-ask.** Anything strategy/tone/ICPs already answer. Read it back for confirmation instead of asking cold ("Your tone is on file as casual and punchy, no em-dashes. Still right?") rather than "How would you describe your tone of voice?"
- **Gaps to fill.** Sections that are empty, thin, or stale per provenance. These are the interview's priority — spend the time here.
- **Never ask.** Everything in `bannedTopics` plus the dismissed topics in `customInstructions`.
- **ICP-derived questions.** For each persona, the questions that audience actually wants answered. This is the backbone of interview #2 and beyond.
- **The tailored set.** Start from the funnel-stage banks below, CUT every question the record already answers, and ADD specific probes that name their real topics, posts, and competitors.

Save the brief to `clients/<slug>/interview-prep.md`.

**Hard rule:** the brief states only what Virio, LinkedIn, or CRM actually returned. Never invent a fact, a stat, or a POV for the FOC. "Unknown" beats invented — an unknown becomes an interview question, which is the whole point.

**No connector, or FOC not in Virio:** say which, then run the generic flow — the question banks below plus whatever web research you can do on the person and company. The skill works with zero connectors; it is just sharper with them.

## Prep — the rest

- Know which interview this is: #1 (foundation) or #2+ (topic mining). The flows differ — see below.
- Know why you're asking each section, and be ready to say it. Questions land as irrelevant when the FOC can't see the purpose; frame the why before the what.

## Interview #1 — setting the scene

Open by telling the FOC what the interview is for. Something like:

> "Today I want to get to know you, your career, your company, and your product. We're aiming to extract unique, POV-based insights from your stories and anecdotes, and to make you think deeper about your industry, your company, your product, and your ICP. This gives us what we need to create compelling content for your audience. The goal of the content is three-tiered:
> 1. Speak directly to your ICP in broad and narrow ways (industry, niche, ICP, individual)
> 2. Give them thoughtful, actionable, and savable content
> 3. Package it with your uniquely credible, story-based points of view"

## Question banks by funnel stage

These questions are meant to be deep, not surface level. Don't let the FOC just report stories they've told a million times — mine for thoughtful, tactical takes that would make their ICP's ears perk up. Treat the interview like a good podcast: it should satisfy on both learning and entertainment.

The banks are raw material, not a script. After prep research, cut every question the Virio record already answers (tone, ICP, banned topics, company basics are usually on file) and replace them with probes that name what you found. Ask the questions only this person can answer.

**Tell me about yourself (TOFU)**
- Where did you grow up? What shaped your values?
- What are you known for amongst your friends and family?
- What did you study in university and why?
- What was your first job experience?
- What were skills in yourself that you sensed early on?
- What topics do you feel confident discussing at length?
- What do you like to do for fun?
- What's the hill you'd die on in business or life?
- How do you want to be perceived by your audience?
- How would you describe your tone of voice (use 3 words)?

**Tell me about your career journey (TOFU / MOFU)**
- In a straight line, can you tell me the story of your career and how you got here?
- Did you always want to become an entrepreneur?
- Were there any defining moments that led you to start your own business?
- How would you describe your leadership style?
- What do you find most difficult about being a founder?
- What are your biggest strengths as a founder?
- What motivates you?
- What accomplishments are you most proud of?

**Tell me about your company (MOFU / BOFU)**
- Why did you start this company?
- What are your top 3 goals in business in the next 6 months?
- Where will the company be in 2029?
- In your words, what does your product do and why is it important?
- Can you sell me your product as if I was a customer?
- What are the most common objections you get around your product and why?
- Can you explain your product to me as if I was 15 years old?
- What do people really love about your product?
- What makes your products/services unique?
- Why do your customers choose you?
- Who do you see as your competitors and how will your company win?
- If your business disappeared tomorrow, what lessons would you keep forever?
- When are you at your absolute best with clients, and why?

**Takes on your industry (MOFU)**
- What have you changed your mind about in the last 6 months?
- What frustrates you about your industry that no one talks about?
- What do most people overcomplicate that you've simplified?
- What would 5-years-ago you be shocked to see you doing today?
- What's something you used to do that you now think is completely wrong?
- What's a belief you have that would piss people off at a conference?

**Takes on your ICP (MOFU / BOFU)**
- Who are you trying to reach on LinkedIn (e.g., founders, CEOs)? What industries, roles, or demographics define your ideal audience?
- Are there any specific formats you think your audience prefers (stories, step-by-step guides, case studies)?
- Are there any topics we should avoid entirely?
- Do you prefer short, punchy posts or longer, detailed narratives?
- Who does your company fight for, and why does it matter to you?
- What's the real reason your best clients win?
- What are your customers trying to achieve, and why is that important?
- What do most customers think they need, but actually don't?
- What's a trap you see people falling into over and over again?

## Interview #2 and beyond

The goal of every subsequent interview is to keep mining for content ideas the ICP would find interesting while sharpening the FOC's unique POV as a thought leader.

Topic discovery has many possible approaches, but it boils down to understanding the psyche of the FOC's audience and answering the questions already in their heads. Before the call, build (or refresh) a deep read of that audience — the icp-avatar skill produces exactly this, and it should start from the ICP personas the prep research pulled from Virio rather than from a blank page — and turn it into a list of questions the ICP would want answered. Bring those to the interview and validate them with the FOC.

## Capture guidance — during the interview

Compelling content requires the FOC to speak in stories, anecdotes, frameworks, outcomes, and examples. Avoid fluffy, generic takes; mine for deep insights and tactics. If an answer lacks a concrete example, ask for it:

> "It seems like you know a lot about this topic, but I'm particularly interested in how you learned it, who taught you, and what made you see it as important. Is there a story you could share that your ICP would find interesting? Any examples to make this richer?"

One direction per answer is enough for a post: say one thing, prove that one thing. Collect data, acronyms, and stats as they come up — numbers anchor hooks later.

## Handoff

The interview transcript is the raw material. Run the idea-inventory skill on it to extract 20+ tagged post concepts; those concepts enter the writing-standards drafting protocol.

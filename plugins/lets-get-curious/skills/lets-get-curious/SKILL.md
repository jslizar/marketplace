---
name: lets-get-curious
description: "Turns a topic you have to post about but do not care about into one you are curious enough to write well. Runs the topic through a library of curiosity lenses, triages the angles with the most juice, then digs up genuinely surprising facts, origins, and stakes instead of handing back homework. Built for short-form content and social posts. Use when you say \"lets get curious\", \"I am not into this topic\", \"find something interesting about X\", \"make this topic interesting\", \"I have to post about [boring thing]\", \"find me an angle\", \"what is actually interesting here\", \"dig deeper on this\", \"zoom out on this topic\", or \"simulate why this matters\". Four modes: quick spark, deep dig (default), simulate, zoom out. Finds the ANGLE and the FACTS; hand off to watt:post to draft in your voice, or dm-master for outreach."
---

# Let's Get Curious

The job of this skill is not to research a topic. It is to find the angle that makes *you* care about it, so you can write a post worth reading.

Research optimizes for coverage and hands back a summary. Curiosity optimizes for the one thread that, once pulled, makes the whole thing feel alive. This skill optimizes for the thread.

## Principles

- **Interest lives in the gap.** Curiosity is the gap between what you know and what you suddenly want to know. The skill's job is to open that gap, then close it with something specific.
- **Do not assign homework.** Generating questions is the easy half. The skill triages to the best questions, then goes and answers them. The deliverable is nuggets and an angle, not a quiz.
- **Specific beats broad.** "The system is complex" is boring. "One shipment can be classified eleven different ways and the importer picks the cheapest" is interesting. Always push for the concrete instance, the real number, the named person.
- **Aim the dig at the reader.** You are writing this post for someone. Hunt for angles that audience would actually scroll-stop for, not just facts that are technically true.

## The Curiosity Lenses

Run the topic through these. Each is a reusable question-generator. Most topics light up on three or four lenses, not all eleven.

1. **Origin.** Why does this exist at all? What broke in the world that made someone build it? What did people do before?
2. **Friction.** What is the hardest part? Where does it jam, break, or quietly fail? Who loses sleep over it?
3. **Money.** Follow it. Who profits, how, and how much? Where is the margin actually made or lost?
4. **Heresy.** What does everyone inside this space believe that is wrong? What do outsiders get backwards?
5. **Insider.** What do practitioners know that civilians do not? The unwritten rule, the open secret, the tell.
6. **Scale and extremes.** The biggest, fastest, oldest, most expensive, most absurd case on record. The number that makes your jaw drop.
7. **Adjacent.** What unrelated field does this secretly rhyme with? "X is basically the Y of Z."
8. **First principles.** Strip it to physics, economics, or human nature. Why must it work this way and not some other way?
9. **Trajectory.** Where is this in ten years? What is the thing about to flip, and who is not ready for it?
10. **Character.** Who are the obsessives, rivals, and weirdos who gave their lives to this? Where is the feud?
11. **Stakes.** What actually happens if this fails? Who gets hurt, what falls over?

Lenses that carry history and significance (used heavily by zoom out mode): Origin, Trajectory, Stakes, Adjacent.

## The Workflow

Copy this checklist and work it top to bottom.

```
- [ ] Frame: restate the topic in one line, name the audience the post is for
- [ ] Triage: one line per lens scoring its juice for THIS topic, pick the top 2-3 (no search)
- [ ] Dig: go deep on the chosen lenses, find the actual nugget, verify with search
- [ ] Bridge: hand back the angle and hook for the post, not just trivia
```

**Frame.** One sentence on what the topic is, one on who is going to read the post. This points the dig at angles that land for that reader.

**Triage.** Walk all eleven lenses fast, one line each, rating the juice (high / medium / low) for this specific topic. Pick the two or three highest. This is the journalist's move: find the story before you report it. No web search here, this is a judgment pass.

**Dig.** Go deep on the chosen lenses. For each, find the genuinely surprising thing: the origin nobody knows, the weird number, the contrarian truth, the named obsessive. Use web search by default to get fresh, specific, verifiable facts. This is where the value is, so spend the most effort here.

**Bridge.** Close the loop back to the post. For each nugget, say what angle or hook it gives the piece. The whole point is that you still have to write the post, so do not leave yourself holding trivia.

## Modes

**Deep dig (default).** The full workflow above. Use when no mode is specified.

**Quick spark.** Triage plus one fast answer. Skip web search, stop as soon as one angle clearly has heat. For when you just need a way in and are short on time.

**Simulate.** Pick one concrete instance (a single dollar, packet, shipment, customer, request) and narrate its full path through the system, step by step. Tracing one real unit through a process is one of the most reliable ways to make an abstract topic click. Best for systems, pipelines, and "how does this actually work" topics.

**Zoom out.** Lead with Origin, Trajectory, Stakes, and Adjacent. Place the topic in history ("what era of this are we in"), then say why it matters beyond itself. Best when the post needs significance and context rather than a single fun fact.

## Search and Fact Integrity

- Web search is ON by default for the dig step, OFF for triage and quick spark. You can say "no search" to keep it offline.
- The output may end up in a public post, so do not manufacture surprising facts. If a specific claim (especially a number, a "first", or a superlative) is not verified, present it as a question or a hypothesis to check, not as a stated fact.
- Prefer original sources and flag confidence when it is low.

## Handing Off

This skill stops at the angle and the verified nuggets. To carry it forward:

- **To draft the post in your voice**, hand the chosen angle and hook to `watt:post` (full rewrite + de-slop + brand QA), or `watt:watt-voice-match` for a quick voice pass.
- **To turn the angle into outreach**, hand it to `dm-master` for a connection request, DM, or follow-up built on the hook.
- **To pressure-test the finished draft**, run `watt:watt-voice-review` or `watt:deslop` before it ships.

Do not try to do the format-finding or final voice work inside this skill. Find the angle here, then pass it on.

## Worked Example (compressed)

**Topic:** Harmonized System codes (the numbers used to classify goods for customs and tariffs). **Audience:** founders reading a LinkedIn post.

**Triage:**
- Origin: HIGH. Why does a global classification system for every physical object exist, and who decided?
- Heresy: HIGH. Outsiders assume the code is objective. Insiders know it is argued over.
- Scale and extremes: MEDIUM. How many codes, weirdest category?
- Money: HIGH. The code picks the tariff, so the code is the money.
- (others: low for this topic)

**Dig (verify each with search before stating):**
- Origin angle: the system exists because before it, every country classified goods differently and trade was chaos. A shared catalog of the physical world had to be invented. *Way in: the unglamorous infrastructure that makes global trade legible.*
- Heresy angle: the "right" code is often genuinely ambiguous, so classification becomes strategy, the same product can be argued into a lower-tariff category. *Way in: customs is not paperwork, it is a negotiation with rules.*
- Money angle: a single digit in the code can swing the duty owed, so the classification decision is a pricing decision. *Way in: the boring number on a form is where margin is won or lost.*

**Bridge:** Lead the post with the heresy ("most people think a customs code is a fact, it is closer to a negotiating position"), support it with the money angle. That is the hook plus the spine, from a topic that started as a number on a form. Then hand that angle to `watt:post` to draft it.

(Note: in a real run, every specific claim above gets confirmed by search before it goes in the deliverable.)

## Output Template

Keep it tight. Frame in two lines, the triage as a short scored list, the dig as the chosen lenses with their nuggets and a "way in" each, and a final bridge that names the recommended angle and hook, plus which skill to hand off to next.

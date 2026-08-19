# Example Benchmark: Video Transcript & Decoded Subtext

This benchmark demonstrates how the `corporate-jargon-translator` skill processes real meeting audio/video transcripts to generate both line-by-line translator commentary and a high-level corporate jargon breakdown.

---

## 1. Raw Meeting Transcript

```text
Manager: Hey buddy, thanks for joining. No translator today?
Employee: Uh no, I didn't think it was necessary. Why is HR here?
Manager: Oh yeah, I just wanted HR here to make sure that we're all on the same page.
Employee: Alright, I'm adding my translator.
Manager: I really wish you wouldn't do that.
Employee: No, if you're going to have your translator, I'm going to have my translator.
Manager: Please please don't.

(A few minutes later)

Translator: Hey, thanks for adding me. Ooh, HR is here. You're in trouble.
Manager: No, I wanted to start this conversation off by saying you are not in trouble.
Translator: You're in trouble.
Manager: The leadership team here feels like you're just falling a little bit short of expectations.
Translator: They don't like you.
Manager: Thanks translator, thanks. Your perspective is always valuable. So it's not that we don't like you, okay? It's just that we feel like you're currently not thriving, and we're trying to cultivate an environment where everybody's thriving, okay? So the plan that we put into place is really just going to allow you to thrive.
Translator: They're PIP-ing you.
Employee: Yeah yeah yeah, I got that one. So I know that I'm short of my goals, but the company as a whole is short of their goals. So does that mean that we PIP the entire leadership team?
Translator: Ooh, that was a good one.
Manager: I really appreciate your candor. While I do recognize that we are behind on our goals, I can assure you that our leadership team is working around the clock to execute on our company's mission and drive strategic results against our core values.
Translator: Yeah, he's saying that no, they won't be held accountable, only low-level peasants like you will be held accountable.
```

---

## 2. Structured Corporate Jargon Decoder Table

| Corporate Jargon / Phrase | Actual Subtext | Risk Level |
| :--- | :--- | :--- |
| **"Wanted HR here to make sure we're on the same page"** | Bringing legal/HR coverage to document a disciplinary step or termination track. | 🔴 CRITICAL |
| **"You are not in trouble"** | You are definitely in trouble. | 🔴 CRITICAL |
| **"Falling a little bit short of expectations"** | Management is actively dissatisfied with your output. | 🟠 HIGH |
| **"Not thriving / Putting a plan in place to help you thrive"** | Placing you on a Performance Improvement Plan (PIP), typically a precursor to firing. | 🔴 CRITICAL |
| **"I really appreciate your candor"** | You just made a valid point that made leadership uncomfortable. | 🟡 MEDIUM |
| **"Working around the clock to execute on strategic results"** | Standard deflective rhetoric to protect upper management from accountability. | 🟡 MEDIUM |

---

## 3. Executive Summary & Tactical Employee Advice

- **Primary Situation**: PIP / Performance Disciplinary Meeting.
- **Overall Threat Level**: 🔴 CRITICAL (Immediate risk of employment termination within 30-90 days).
- **Key Tactical Takeaway**:
  1. **Do not attempt to win arguments using logic about leadership performance**: Saying "the company missed goals too" is logically sound but politically dangerous; management will deflect with core values rhetoric ("I appreciate your candor...").
  2. **Document everything in writing**: Save off-board copies of performance metrics, written approvals, and email chains immediately.
  3. **Quietly begin job hunting**: A PIP in corporate tech has a >80% departure outcome. Use the PIP period to secure external interviews.

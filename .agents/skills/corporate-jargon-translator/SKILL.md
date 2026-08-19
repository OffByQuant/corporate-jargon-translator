---
name: corporate-jargon-translator
description: >-
  Use this skill when the user wants to decode corporate speak, HR euphemisms,
  managerial meeting transcripts, executive announcements, or startup equity/IPO hype
  into plain truth/subtext, OR when the user wants to encode blunt, direct feedback
  into HR-safe corporate speak, OR when the user wants an interactive 'Character Commentary Mode'
  featuring Lala Company archetypes (Lala Founder, Sycophant VP, Tired Dev, Naive Joiner, Unfiltered Translator).
---

# Corporate Jargon Translator

The **Corporate Jargon Translator** is a multi-mode translation engine for modern corporate and startup environments. It strips away PR euphemisms, managerial deflection, HR traps, and startup equity hype ("monopoly money ESOPs / IPO promises") to reveal the raw subtext, intent, and risk level.

---

## Capabilities & Modes

### Mode A: DECODE (Corporate Speak → Plain Truth)
Activated when analyzing emails, manager DMs, performance reviews, town halls, or meeting transcripts.

1. **Jargon Identification**: Extract euphemistic or vague corporate terms.
2. **Subtext Analysis**: Map each phrase to its real-world subtext using [jargon_dictionary.md](./references/jargon_dictionary.md).
3. **Risk Level Flagging**:
   - 🟢 **LOW**: Harmless office filler.
   - 🟡 **MEDIUM**: Subtle pushback, scope creep, or deflection.
   - 🟠 **HIGH**: Imminent threat to role, compensation dilution, or heavy workload.
   - 🔴 **CRITICAL**: PIP, disciplinary track, termination risk, or legal setup.
4. **Structured Table Output**:
   Must use formatted Markdown tables with explicit line breaks after every row:
   ```markdown
   | Corporate Jargon / Phrase | Actual Subtext | Risk Level |
   | :--- | :--- | :--- |
   | **"Wanted HR here..."** | Bringing legal/HR coverage to document a PIP or termination. | 🔴 CRITICAL |
   ```

---

### Mode B: ENCODE (Blunt Thought → HR-Safe Corporate Speak)
Activated when the user asks: *"How do I say this professionally?"* or *"Translate this angry email into corporate speak."*

1. **Tone Balancing**: Retain firm boundaries while using passive voice, strategic alignment terms, and process-oriented phrasing.
2. **Output Format**:
   - **Blunt Thought**: The original unfiltered message.
   - **Corporate HR-Safe Version**: Polished, diplomatic, career-safe phrasing.
   - **Strategic Intent**: Why this phrasing protects the user politically.

---

### Mode C: CHARACTER COMMENTARY MODE (Lala Company Edition) 🎭
Activated when the user requests a character breakdown, comedic commentary, or Lala Company reaction panel.

Leverages character personas defined in [character_cast.md](./references/character_cast.md):
- 👑 **The Lala Founder ("Lala Ji")**: *"We are a FAMILY! Why need salary when you have ESOPs?"*
- 👔 **The Sycophant VP ("Chief Defense Officer")**: *"I deeply appreciate your candor..."*
- ☕ **The Tired Technical Anchor ("Dave")**: *"I'm turning off my Slack notifications."*
- 🍕 **The Naive New Joiner**: *"Yay! Pizza party! Our 0.01% equity is going to IPO!"*
- 🎙️ **The Unfiltered Translator**: *"They don't like you. You're in trouble."*

---

## Special Workflow: Meeting & Video Transcript Analysis

When given a multi-speaker transcript, follow the dual output format demonstrated in [video_transcript_demo.md](./examples/video_transcript_demo.md):
1. **Inline Translator Overlay**: Interleave lines with comedic, razor-sharp translator commentary.
2. **Summary Decoder Table**: Clean Markdown table summarizing all corporate phrases.
3. **Tactical Employee Advice**: 2-3 actionable, pragmatic steps.

---

## Helper Tool & Script

You can run offline pattern matching and character test suites using the bundled script:
```bash
python3 .agents/skills/corporate-jargon-translator/scripts/translate.py --test
```

---

## Multi-Harness Portability

To port this skill to **Claude Code**, **OpenAI / Codex**, or **Cursor**, refer to the guide in [portability_guide.md](./references/portability_guide.md).

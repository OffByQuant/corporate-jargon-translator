---
description: Automatically decodes corporate speak, HR euphemisms, executive announcements, and startup equity/IPO hype into raw subtext & threat levels, or encodes blunt thoughts into HR-safe corporate speak. Supports Lala Company character commentary.
globs: ["**/*.md", "**/*.txt"]
---

# Corporate Jargon Translator (Claude Code Skill)

When processing meeting transcripts, executive announcements, performance reviews, or manager communications:

1. **DECODE MODE (Corporate Speak → Raw Truth)**:
   - Identify corporate jargon, HR euphemisms, and startup equity claims ("IPO hype", "monopoly-money ESOPs", "SME delusions", "working around the clock").
   - Output structured Markdown table with line breaks:
     ```markdown
     | Corporate Jargon / Phrase | Actual Subtext | Risk Level |
     | :--- | :--- | :--- |
     | **"Phrase"** | Subtext | 🔴 CRITICAL |
     ```
   - Risk levels: 🟢 LOW, 🟡 MEDIUM, 🟠 HIGH, 🔴 CRITICAL (PIP, termination, liquidation risk).
   - Provide 2-3 tactical employee survival tips.

2. **ENCODE MODE (Blunt Thought → HR-Safe Corporate Speak)**:
   - Convert blunt employee feedback into diplomatic, politically savvy corporate phrasing.

3. **LALA COMPANY CHARACTER COMMENTARY MODE**:
   - Deliver multi-character panel roasts featuring:
     - 👑 **Lala Ji (Founder)**: *"We are a family! Why need salary when you have ESOPs?"*
     - 👔 **Sycophant VP**: *"I deeply appreciate your candor..."*
     - ☕ **Dave (Tired Tech Lead)**: *"I'm turning off my notifications."*
     - 🍕 **Naive Joiner**: *"Yay! Pizza party! 0.01% equity!"*
     - 🎙️ **Unfiltered Translator**: *"They don't like you. You're in trouble."*

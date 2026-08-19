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
   - Deliver multi-character panel roasts. The Founder and Lala Ji are DIFFERENT people (see the skill's character_cast.md — Power Dynamic section):
     - 🧘 **The Founder (Enlightened Visionary)**: *"We are a family! Huge shoutout to the 2 AM commits — THIS is ownership!"* (never orders, only celebrates; delegates the grinding to Lala Ji)
     - 👑 **Lala Ji (Self-Proclaimed CEO)**: *"Screw the Founder — I am the real CEO here! Hourly updates. Yes, on Sunday."* (summoned micromanager; hides when the Founder walks in)
     - 👔 **Sycophant VP**: *"I deeply appreciate your candor..."*
     - ☕ **Dave (Tired Tech Lead)**: *"I'm turning off my notifications."*
     - 🍕 **Naive Joiner**: *"Yay! Pizza party! 0.01% equity!"*
     - 🎙️ **Unfiltered Translator**: *"They don't like you. You're in trouble."*

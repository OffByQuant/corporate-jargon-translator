# Corporate Jargon Translator - Repository Guidelines for Claude Code

This repository contains the **Corporate Jargon Translator** skill, designed to decode corporate speak, HR euphemisms, executive deflection, and startup equity hype into plain truth, as well as encode blunt employee feedback into HR-safe corporate speak.

---

## 🛠️ Commands & Tests

- **Run CLI Translator Test Suite**:
  ```bash
  python3 .agents/skills/corporate-jargon-translator/scripts/translate.py --test
  ```
- **Decode Custom Text String via CLI**:
  ```bash
  python3 .agents/skills/corporate-jargon-translator/scripts/translate.py --decode "Your text here"
  ```
- **Encode Blunt Thought into Corporate Speak via CLI**:
  ```bash
  python3 .agents/skills/corporate-jargon-translator/scripts/translate.py --encode "You guys don't know what you're doing"
  ```

---

## 🤖 Claude Code Rules & Skill Integration

Claude Code automatically loads instructions from [.claude/rules/corporate-jargon-translator.md](file:///.claude/rules/corporate-jargon-translator.md).

### Standard Execution Modes
1. **Decode Mode**: Decodes HR speak, meeting transcripts, PIP emails, and IPO hype into structured Markdown tables with risk levels (🟢 Low, 🟡 Medium, 🟠 High, 🔴 Critical).
2. **Encode Mode**: Rewrites unfiltered thoughts into executive-ready corporate speak.
3. **Character Commentary Mode (Lala Company Edition)**: Provides comedic panel reactions featuring *The Enlightened Founder*, *Lala Ji (self-proclaimed CEO — a different person from the Founder)*, *Sycophant VP*, *Tired Dev Dave*, *Naive Joiner*, and *Unfiltered Translator*.

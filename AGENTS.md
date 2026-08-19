# Corporate Jargon Translator - Agent Guidelines

This repository contains the **Corporate Jargon Translator** skill, designed to decode corporate speak, HR euphemisms, executive deflection, and startup equity hype into plain truth, as well as encode blunt employee feedback into HR-safe corporate speak.

The full skill lives at [.agents/skills/corporate-jargon-translator/SKILL.md](.agents/skills/corporate-jargon-translator/SKILL.md) — harnesses that follow the agentskills.io convention (Codex, Copilot CLI, Gemini CLI, OpenCode) discover it there automatically. Read it before processing any translation request; it links the jargon dictionary, character cast, and transcript-analysis examples.

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

## 🤖 Execution Modes

1. **Decode Mode**: Decodes HR speak, meeting transcripts, PIP emails, and IPO hype into structured Markdown tables with risk levels (🟢 Low, 🟡 Medium, 🟠 High, 🔴 Critical), plus 2-3 tactical employee survival tips.
2. **Encode Mode**: Rewrites unfiltered thoughts into executive-ready corporate speak (Blunt Thought → HR-Safe Version → Strategic Intent).
3. **Character Commentary Mode (Lala Company Edition)**: Provides comedic panel reactions featuring *Lala Ji*, *Sycophant VP*, *Tired Dev Dave*, *Naive Joiner*, and *Unfiltered Translator*.

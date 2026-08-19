# 🎙️ Corporate Jargon Translator

> **An Agentic AI Skill to decode corporate speak, HR euphemisms, executive deflection, and startup IPO hype into raw, unfiltered truth (and vice versa).**

Inspired by the viral *Corporate Translator* video, **Corporate Jargon Translator** transforms AI assistants into sharp, witty, and deeply accurate corporate decoders. It helps employees see through managerial rhetoric, spot HR traps, understand startup equity realities, and protect their careers.

---

## ✨ Features & Modes

### 🚨 1. DECODE Mode (Corporate Speak → Raw Truth) — the default
- Translates emails, manager DMs, town hall notes, and PIP warnings into plain subtext.
- Exposes **Startup IPO Hype & "SME" Delusions** (e.g. trading "monopoly-money" paper equity for 80-hour work weeks).
- **Every decode follows the same three-part output contract:**
  1. **🎙️ Inline Translator Overlay** — the loaded lines quoted one by one, each with a short deadpan verdict from the Unfiltered Translator. He waits until the jargon is clear; lines with nothing to decode get silence, not speculation.
  2. **Summary Decoder Table** — every flagged phrase with its subtext and a **Risk Level**:
     - 🟢 **LOW**: Harmless office filler.
     - 🟡 **MEDIUM**: Subtle pushback or scope creep.
     - 🟠 **HIGH**: Heavy workload dump, title stall, or compensation dilution.
     - 🔴 **CRITICAL**: PIP, disciplinary track, brain drain, or liquidation risk.
  3. **Tactical Employee Advice** — 2-3 genuine, actionable survival steps for the receiving party.

Example overlay:

```text
> "Our corporate governance committee has placed a temporary hold on senior title calibrations."
🎙️ Translator: Promotion denied.

> "...the uncompromised spotlight it truly deserves when the capital restructuring is finalized."
🎙️ Translator: "Later" means never.
```

### 💼 2. ENCODE Mode (Blunt Thought → HR-Safe Corporate Speak)
- Converts raw, angry, or direct employee feedback into polished, executive-ready corporate phrasing.
- Output: **Blunt Thought** → **Corporate HR-Safe Version** → **Strategic Intent** (why the phrasing protects you politically).

### 🎭 3. Character Commentary Mode (Lala Company Edition) — on demand
Summoned when you ask — *"how would all the personas respond to this email?"*, a single-character ask (*"what would Dave say?"*), the **full show** (decode contract first, then the panel), or directly via the **`/lala-panel`** companion skill. A comedic, multi-persona panel roast featuring classic workplace archetypes — and the key gag: **the Founder and Lala Ji are two different people** (the Founder never orders, only celebrates; Lala Ji does the grinding and thinks he's the real CEO):
- 🧘 **The Founder ("The Enlightened Visionary")**: *"We are a FAMILY! Huge shoutout to the 2 AM commits — THIS is ownership!"* — never orders, only celebrates.
- 👑 **Lala Ji ("The Self-Proclaimed CEO")**: *"Screw the Founder — I am the real CEO here! Hourly updates. Yes, on Sunday."* — the summoned micromanager.
- 👔 **The Sycophant Senior ("Chief Defense Officer")**: *"I deeply appreciate your candor..."*
- ☕ **The Tired Technical Anchor ("Dave")**: *"I built the monolith 4 years ago. I'm off-call at 5:00 PM."*
- 🍕 **The Naive New Joiner ("The True Believer")**: *"Yay! Pizza party! Our 0.01% equity is going to IPO!"*
- 🎙️ **The Unfiltered Translator ("The Cynical Realist")**: *"They don't like you. You're in trouble."*

---

## 🛠️ Multi-Harness Compatibility

This repository is pre-built to run natively across all major AI agent harnesses:

| Harness | Compatibility Status | How it Works |
| :--- | :--- | :--- |
| **Google Antigravity** | 🟢 Native | Auto-loads `.agents/skills/corporate-jargon-translator/SKILL.md` |
| **OpenCode** | 🟢 Native | Auto-loads `.agents/skills/corporate-jargon-translator/SKILL.md` |
| **Claude Code** | 🟢 Native | Auto-loads `.claude/skills/corporate-jargon-translator/SKILL.md`, `.claude/rules/` & `CLAUDE.md` |
| **OpenAI Codex CLI** | 🟢 Native | Auto-loads `AGENTS.md` & `.agents/skills/corporate-jargon-translator/SKILL.md` |
| **Cursor** | 🟢 Supported | Copy `.claude/rules/corporate-jargon-translator.md` to `.cursor/rules/` |
| **Raw OpenAI API** | 🔵 Optional | `adapters/codex/` system prompt & payload — only if you're not using a harness |

**Default to a harness** — it runs the skill on the subscription you already pay for (Claude, ChatGPT/Codex, etc.). The raw API adapter is for embedding the translator in your own scripts and bills per token on top.

Both skills ship together: `corporate-jargon-translator` (decode/encode) and `lala-panel` (character panel) live side by side in `.agents/skills/` and are discovered by every harness above the same way.

---

## 🚀 Quick Start

### 1. Using in AI Chat / Agents
Clone or copy this repository into your project or `.agents/skills/` directory. Then prompt your AI agent:

```text
Decode this email from my manager using corporate-jargon-translator:
"We are taking a disciplined approach to cash flow and operational bandwidth..."
```

In harnesses with slash-command skill invocation (Claude Code, Codex CLI), the skills are directly callable:

```text
/corporate-jargon-translator decode this email: ...
/lala-panel how would everyone react to this memo: ...
```

### 2. Running Offline CLI Tests
Test the pattern matcher and benchmark test suite locally:

```bash
# Run automated benchmark test suite
python3 .agents/skills/corporate-jargon-translator/scripts/translate.py --test

# Decode custom text via CLI
python3 .agents/skills/corporate-jargon-translator/scripts/translate.py --decode "We are asking everyone to wear multiple hats."
```

### 3. Optional: Raw OpenAI API
Only needed outside a harness (e.g. embedding the translator in your own scripts). Generate the API payload:

```bash
python3 adapters/codex/openai_api_demo.py
```

---

## 📂 Repository Structure

```text
corporate-jargon-translator/
├── README.md                                     # Main project documentation
├── GETTING-STARTED.md                            # Benchmark test prompts & execution guide
├── CLAUDE.md                                     # Repository guide for Claude Code
├── AGENTS.md                                     # Repository guide for Codex CLI & agentskills.io harnesses
├── .claude/
│   ├── rules/
│   │   └── corporate-jargon-translator.md        # Native Claude Code rule file
│   └── skills/
│       ├── corporate-jargon-translator/          # Symlink → .agents/skills/... (Claude Code skill discovery)
│       └── lala-panel/                           # Symlink → .agents/skills/lala-panel
├── .agents/
│   └── skills/
│       ├── lala-panel/
│       │   └── SKILL.md                          # /lala-panel — character panel companion skill
│       └── corporate-jargon-translator/
│           ├── SKILL.md                          # Master Antigravity / OpenCode Skill Spec
│           ├── references/
│           │   ├── jargon_dictionary.md          # Comprehensive subtext & risk lexicon
│           │   ├── character_cast.md             # Lala Company persona definitions
│           │   └── portability_guide.md          # Multi-harness export instructions
│           ├── examples/
│           │   └── video_transcript_demo.md      # Benchmark video transcript analysis
│           └── scripts/
│               └── translate.py                  # Offline CLI matcher & test suite
└── adapters/
    └── codex/                                    # Optional raw-API route (harness route needs none of this)
        ├── system_prompt.txt                     # Copy-pasteable system prompt (source of truth)
        ├── system_prompt.json                    # Generated API payload (openai_api_demo.py --write-json)
        └── openai_api_demo.py                    # Python API payload generator
```

---

## 🙏 Credits & Acknowledgments

- **Original Video Inspiration**: Massive credit to the creator of the viral *Corporate Translator* video (Manager vs. Employee vs. HR vs. Translator) which sparked the concept for this agentic AI skill.
- **Lala Company Archetypes**: Inspired by real-world startup workplace dynamics and founder culture.

---

## 📄 License

[MIT License](LICENSE). Free for all employees, developers, and AI agents looking to translate corporate speak into truth!

# Getting Started with Corporate Jargon Translator 🚀

Welcome to the **Corporate Jargon Translator** skill! This guide will walk you through how to use, test, and run the skill across different AI agent harnesses.

---

## 📋 What a Decode Looks Like (Default Output Contract)

Every decode produces three parts, in this order:

1. **🎙️ Inline Translator Overlay** — the jargon-loaded lines quoted one by one, each answered with a short, deadpan verdict. The Translator waits until the jargon and context are clear; lines with nothing to decode get no commentary.

   ```text
   > "Leadership sees and deeply values the heavy lifting you've been doing."
   🎙️ Translator: Compliment this size? Brace yourself.

   > "Our governance committee has placed a temporary hold on senior title calibrations."
   🎙️ Translator: Promotion denied.
   ```

2. **Summary Decoder Table** — `| Corporate Jargon / Phrase | Actual Subtext | Risk Level |` with 🟢 LOW / 🟡 MEDIUM / 🟠 HIGH / 🔴 CRITICAL flags.

3. **Tactical Employee Advice** — 2-3 genuine, actionable steps for the person on the receiving end.

The **character panel is on demand**: ask *"how would all the personas respond?"*, name one (*"what would Dave say?"*), request the **full show** (decode + panel), or invoke **`/lala-panel`** directly.

---

## 🎯 Test Benchmarks & Sample Prompts

Below are the benchmark prompts used to test the translator. You can copy-paste any of these prompts directly into your AI assistant (Antigravity, OpenCode, Claude Code, ChatGPT, Cursor).

---

### Benchmark 1: The "Path to Listing" & Pre-IPO Budget Freeze Email

**Prompt**:
> Decode the following company email using corporate-jargon-translator:
>
> **Subject**: Strategic Realignment, Q3 Momentum & Our Path to Listing  
> **Team**,  
> As we look ahead at our hypergrowth trajectory, it’s time to double down on our core mission. With our 15-person strike team operating at peak agility, we are uniquely positioned to capture massive market share and disrupt the legacy players. We are not just an SME; we are building an enterprise-grade institution primed for a public listing that will unlock exponential value for all true believers.  
>  
> To maximize efficiency and ensure our corporate architecture reflects public market readiness, we are taking a disciplined approach to cash flow and operational bandwidth. We are asking everyone to wear multiple hats, prioritize high-impact deliverables, and embrace an owner mindset. Traditional compensation and incremental title adjustments will naturally take a backseat as we optimize our balance sheet for pre-IPO scrutiny. The real upside is on the horizon, and those who stay in the trenches now will shape the future of this enterprise. Let’s execute ruthlessly.

**Expected Decoded Insights**:
- **"Not just an SME / Primed for public listing"** → Founder coping mechanism obscuring that annual revenue doesn't meet minimum penny-stock exchange requirements (e.g. AIM/MicroCap).
- **"15-person strike team"** → Understaffing; 15 employees doing the work of 60.
- **"Traditional compensation takes a backseat"** → **Complete pay freeze, zero bonuses, and no promotions.**
- **"Exponential value for true believers"** → Trading speculative monopoly-money paper equity ($100 valuation) for below-market cash pay.

---

### Benchmark 2: Executive "Restructuring" & PIP Cover-Up Memo

**Prompt**:
> Decode the following executive announcement using corporate-jargon-translator:
>
> **Subject**: Leadership Evolution: Elevating Technical Governance  
> **Hi everyone**,  
> We want to share an important structural evolution within our technology leadership. First, we want to extend our deepest gratitude to Dave for his contributions over the past four years in establishing our delivery baseline; we wish him the absolute best in his next chapter as an industry alum.  
>  
> With Dave’s departure, we are thrilled to announce that Greg is stepping into the role of Chief Strategy Officer (CSO). Greg has demonstrated immense passion for our overarching vision, and this transition frees him from day-to-day client accounts to focus exclusively on macro-level strategy architecture, enterprise risk governance, and public-readiness compliance. Given the critical nature of this strategic mandate, we have concluded his previous operational development framework early so he can fully focus on building institutional trust at the C-suite level. Please join us in congratulating Greg on this vital milestone.

**Expected Decoded Insights**:
- **"Established delivery baseline / Industry alum (Dave)"** → **High-Performer Brain Drain**: Voluntary resignation of a competent 4-year technical anchor fleeing bad executive leadership.
- **"Frees him from client accounts to focus on macro-level architecture (Greg)"** → **Kicked Upstairs / Containment**: Removed from revenue roles due to client complaints; placed in a powerless Chief Strategy Officer title with zero direct reports.
- **"Concluded operational development framework early"** → **PIP Cover-Up**: Quietly dropped an active HR Performance Improvement Plan (PIP) to rebrand a demotion as a C-suite promotion.

---

### Benchmark 3: Senior Title Freeze & Unpaid Workload Dump

**Prompt**:
> Decode the following manager 1-on-1 follow-up email using corporate-jargon-translator:
>
> **Subject**: Follow-up: Career Pathway & Title Trajectory Alignment  
> **Hi Alex**,  
> Thanks for the candid chat earlier today. I want to reiterate that leadership sees and deeply values the heavy lifting you’ve been doing across all key client accounts—your dedication is undeniable.  
>  
> Regarding the Senior Director promotion, the Board and I completely agree that your trajectory is pointed toward executive leadership. However, because we are actively standardizing our organizational chart for external investors and future IPO optics, our corporate governance committee has placed a temporary hold on senior title calibrations. We want to ensure your promotion gets the uncompromised spotlight, executive equity allocation, and external visibility it truly deserves when the capital restructuring is finalized. Let’s keep operating at this high level, absorb the remaining accounts from the recent transition, and build an irrefutable business case for the upcoming cycle.

**Expected Decoded Insights** (delivered as overlay → table → advice):
- **"Heavy lifting across key client accounts"** → You carry 100% of client revenue; you hold maximum operational leverage.
- **"Temporary hold on senior title calibrations"** → **Promotion and raise DENIED.** Dangled carrot blamed on fake IPO audits.
- **"Absorb remaining accounts & build an irrefutable business case"** → Unpaid workload dump + moving goalposts.
- **Tactical Tip**: Weaponize your operational leverage *before* stabilizing the accounts for free.
- Note the overlay skips *"Thanks for the candid chat"* — nothing decodes there yet, so the Translator stays silent.

---

### Benchmark 4: Character Commentary Mode (Lala Company Edition)

**Prompt** (or equivalently: `/lala-panel <the announcement>`):
> Give me a Lala Company panel reaction to this announcement:
> "We are asking everyone to wear multiple hats and embrace an owner mindset. Traditional compensation adjustments will take a backseat as we optimize our balance sheet for pre-IPO scrutiny."

**Expected Decoded Output**:
- 🧘 **The Founder (Enlightened Visionary)**: *"We are a FAMILY! Money comes and goes, but equity in our family is FOREVER. Huge shoutout to everyone grinding this weekend — I see you!"*
- 👑 **Lala Ji (Self-Proclaimed CEO)**: *"You heard him. But between us? Screw the Founder — I run this floor. Hourly updates, and be on WhatsApp Sunday."*
- 👔 **Sycophant Senior**: *"Leadership is taking a disciplined approach to capital allocation."*
- ☕ **Dave (Tired Tech Lead)**: *"Owner hours? Yes. Owner pay? No. I'm off-call at 5:00 PM."*
- 🍕 **Naive Joiner**: *"Yay! Pizza party! Our 0.01% equity is going to IPO!"*
- 🎙️ **Unfiltered Translator**: *"Translation: Complete salary freeze. Lala Ji bought a new Mercedes, but there's no money for your appraisal."*

---

## 💻 How to Run in Different Environments

Prefer a harness (options 1-3) — it runs the skill on the AI subscription you already pay for. The raw API route (option 5) bills per token and is only needed for embedding the translator in your own scripts.

### 1. Google Antigravity & OpenCode
Both Antigravity and OpenCode automatically load the skills from `.agents/skills/` (`corporate-jargon-translator` and `lala-panel`). Simply paste any benchmark prompt into the chat interface.

### 2. Claude Code
Run `claude` in this directory. Claude Code discovers both skills via the `.claude/skills/` symlinks and also reads `.claude/rules/corporate-jargon-translator.md` and `CLAUDE.md`. Invoke directly with `/corporate-jargon-translator` or `/lala-panel`, or just describe what you want decoded.

### 3. OpenAI Codex CLI
Run `codex` in this directory. Codex reads `AGENTS.md` and discovers both skills from `.agents/skills/`.

### (Also: Cursor)
Copy `.claude/rules/corporate-jargon-translator.md` to `.cursor/rules/` — see the [portability guide](.agents/skills/corporate-jargon-translator/references/portability_guide.md).

### 4. CLI Offline Script
Test pattern matching without network API calls:
```bash
# Run automated test suite
python3 .agents/skills/corporate-jargon-translator/scripts/translate.py --test

# Decode custom string
python3 .agents/skills/corporate-jargon-translator/scripts/translate.py --decode "We are asking everyone to wear multiple hats."
```

### 5. Optional: Raw OpenAI API (pay-per-token)
Only for embedding the translator in your own scripts, outside a harness:
```bash
python3 adapters/codex/openai_api_demo.py
```

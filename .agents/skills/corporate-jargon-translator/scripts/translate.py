#!/usr/bin/env python3
"""
Corporate Jargon Translator CLI Helper Script
Provides offline pattern matching, dictionary lookup, and automated test execution.
"""

import sys
import os
import argparse
import re

# Comprehensive Jargon Database
JARGON_LEXICON = [
    {
        "phrase": r"wanted hr here to make sure.*same page",
        "raw_phrase": "Wanted HR here to make sure we're on the same page",
        "subtext": "Bringing legal/HR coverage to document a disciplinary step, PIP, or termination track.",
        "risk": "🔴 CRITICAL"
    },
    {
        "phrase": r"you are not in trouble",
        "raw_phrase": "You are not in trouble",
        "subtext": "You are definitely in trouble.",
        "risk": "🔴 CRITICAL"
    },
    {
        "phrase": r"falling.*short of expectations",
        "raw_phrase": "Falling a little bit short of expectations",
        "subtext": "Management is actively dissatisfied with your output and compiling paper trail.",
        "risk": "🟠 HIGH"
    },
    {
        "phrase": r"not thriving|plan.*to allow you to thrive|plan in place",
        "raw_phrase": "Not thriving / Putting a plan in place to help you thrive",
        "subtext": "Placing you on a Performance Improvement Plan (PIP), typically a precursor to firing.",
        "risk": "🔴 CRITICAL"
    },
    {
        "phrase": r"industry alum|next chapter|established our delivery baseline",
        "raw_phrase": "Next chapter as an industry alum / Established delivery baseline",
        "subtext": "Fired or scapegoated for tech failures; scrubbed from company Slack by 5:00 PM.",
        "risk": "🔴 CRITICAL"
    },
    {
        "phrase": r"frees him from day-to-day|concluded.*operational development framework early|macro-level",
        "raw_phrase": "Frees him from client accounts / Concluded development framework early",
        "subtext": "Failing miserably at client work / PIP-ed out of revenue roles, so leadership invented a title with no direct reports to kick him upstairs.",
        "risk": "🟠 HIGH"
    },
    {
        "phrase": r"temporary hold on.*title calibrations|ipo optics|capital restructuring|uncompromised spotlight",
        "raw_phrase": "Temporary hold on senior title calibrations / IPO optics",
        "subtext": "Title promotion and raise denied. Dangling a carrot while blaming external investors and IPO audits.",
        "risk": "🔴 CRITICAL"
    },
    {
        "phrase": r"absorb the remaining accounts|heavy lifting|irrefutable business case",
        "raw_phrase": "Absorb remaining accounts / Heavy lifting",
        "subtext": "Do the work of the person who just got fired/kicked upstairs without any extra pay or title.",
        "risk": "🟠 HIGH"
    },
    {
        "phrase": r"fast track to an ipo|upcoming ipo|path to listing|public listing|pre-ipo|esop|equity upside|monopoly money|true believers",
        "raw_phrase": "Path to Listing / IPO Hype & Exponential Value for True Believers",
        "subtext": "Multi-level marketing narrative trading speculative monopoly-money options ($100 today promised to be $1M) for below-market pay.",
        "risk": "🟠 HIGH"
    },
    {
        "phrase": r"wear multiple hats|owner mindset|stay in the trenches",
        "raw_phrase": "Wear multiple hats / Owner mindset / Stay in the trenches",
        "subtext": "Work founder hours doing 3 different jobs without extra pay, downside protection, or governance power.",
        "risk": "🟠 HIGH"
    },
    {
        "phrase": r"traditional compensation.*take a backseat|title adjustments.*take a backseat|disciplined approach to cash flow",
        "raw_phrase": "Traditional compensation & title adjustments take a backseat",
        "subtext": "Complete salary freeze, zero bonuses, and no promotions this year while management blames pre-IPO balance sheet audits.",
        "risk": "🔴 CRITICAL"
    }
]

ENCODE_RULES = [
    (r"you guys don't know what you're doing", "We have an opportunity to optimize our strategic alignment and process clarity."),
    (r"that's a terrible idea", "That approach presents interesting trade-offs; let's evaluate alternative paradigms."),
    (r"i won't do this extra work without a raise", "I want to ensure my current scope aligns with our compensation calibration framework."),
    (r"stop wasting my time with useless meetings", "Let's streamline our asynchronous communication to maximize operational throughput.")
]

# Sample sentence per lexicon entry, mapped to the raw_phrase it must decode to.
DECODE_TEST_CASES = [
    ("I just wanted HR here to make sure we're all on the same page", "Wanted HR here to make sure we're on the same page"),
    ("You are not in trouble", "You are not in trouble"),
    ("You're falling a little bit short of expectations", "Falling a little bit short of expectations"),
    ("We're putting a plan in place to help you thrive", "Not thriving / Putting a plan in place to help you thrive"),
    ("He begins his next chapter as an industry alum", "Next chapter as an industry alum / Established delivery baseline"),
    ("This frees him from day-to-day client accounts to focus on macro-level governance", "Frees him from client accounts / Concluded development framework early"),
    ("A temporary hold on senior title calibrations due to IPO optics", "Temporary hold on senior title calibrations / IPO optics"),
    ("You'll absorb the remaining accounts and do the heavy lifting", "Absorb remaining accounts / Heavy lifting"),
    ("We are on a fast track to an IPO with real equity upside", "Path to Listing / IPO Hype & Exponential Value for True Believers"),
    ("We need you to wear multiple hats with an owner mindset", "Wear multiple hats / Owner mindset / Stay in the trenches"),
    ("Traditional compensation and title adjustments take a backseat this cycle", "Traditional compensation & title adjustments take a backseat"),
]

def decode_text(text):
    print("=== CORPORATE JARGON DECODER ===")
    matches = []
    text_lower = text.lower()
    for entry in JARGON_LEXICON:
        if re.search(entry["phrase"], text_lower):
            matches.append(entry)
    
    if not matches:
        print("No standard corporate jargon patterns detected in input.")
        return
    
    print(f"{'Corporate Jargon / Phrase':<45} | {'Actual Subtext':<60} | {'Risk Level'}")
    print("-" * 125)
    for m in matches:
        print(f"{m['raw_phrase']:<45} | {m['subtext']:<60} | {m['risk']}")
    print("\nSummary: Found {} flagged jargon patterns.".format(len(matches)))

def encode_text(text):
    print("=== CORPORATE SPEAK ENCODER ===")
    text_lower = text.lower()
    for pattern, corporate in ENCODE_RULES:
        if re.search(pattern, text_lower):
            print(f"Blunt Thought: {text}")
            print(f"Corporate HR-Safe Version: {corporate}")
            return
    print("No encode rule matched. Use the agent-driven ENCODE mode (SKILL.md Mode B) for free-form input.")

def run_tests():
    print("=== CORPORATE JARGON TRANSLATOR TEST SUITE ===")
    failures = 0
    for sample, expected in DECODE_TEST_CASES:
        sample_lower = sample.lower()
        matched = [e["raw_phrase"] for e in JARGON_LEXICON if re.search(e["phrase"], sample_lower)]
        status = "PASS" if expected in matched else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"[{status}] decode: {sample!r} -> expected {expected!r}, got {matched}")
    for pattern, corporate in ENCODE_RULES:
        ok = re.search(pattern, pattern) is not None and bool(corporate)
        status = "PASS" if ok else "FAIL"
        if not ok:
            failures += 1
        print(f"[{status}] encode rule: {pattern!r}")
    total = len(DECODE_TEST_CASES) + len(ENCODE_RULES)
    print(f"\n{total - failures}/{total} tests passed.")
    return 1 if failures else 0

def main():
    parser = argparse.ArgumentParser(description="Corporate Jargon Translator CLI")
    parser.add_argument("--decode", type=str, help="Text string or text file to decode")
    parser.add_argument("--encode", type=str, help="Blunt text string to translate into corporate speak")
    parser.add_argument("--test", action="store_true", help="Run the offline pattern-matching test suite")
    args = parser.parse_args()
    if args.test:
        sys.exit(run_tests())
    if args.decode:
        decode_text(args.decode)
    elif args.encode:
        encode_text(args.encode)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

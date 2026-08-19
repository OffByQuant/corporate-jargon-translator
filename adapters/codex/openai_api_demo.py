#!/usr/bin/env python3
"""
OpenAI API Demo Script for Corporate Jargon Translator (optional route)
Demonstrates how to call the OpenAI Chat Completions API using the Corporate Jargon Translator system prompt.

Note: this raw-API route bills per token. If you use Codex CLI (or any
agentskills.io-compatible harness), skip this adapter entirely — the harness
auto-loads the skill from AGENTS.md + .agents/skills/ on your existing subscription.
"""

import os
import sys
import json

def load_system_prompt():
    prompt_path = os.path.join(os.path.dirname(__file__), "system_prompt.txt")
    with open(prompt_path, "r") as f:
        return f.read()

def generate_api_payload(user_input_text):
    system_prompt = load_system_prompt()
    payload = {
        "model": "gpt-4.1",
        "temperature": 0.3,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"Decode the following text using Corporate Jargon Translator:\n\n{user_input_text}"
            }
        ]
    }
    return payload

def main():
    sample_text = (
        "Subject: Strategic Realignment, Q3 Momentum & Our Path to Listing\n"
        "We are asking everyone to wear multiple hats, prioritize high-impact deliverables, "
        "and embrace an owner mindset. Traditional compensation and incremental title adjustments "
        "will naturally take a backseat as we optimize our balance sheet for pre-IPO scrutiny."
    )
    
    payload = generate_api_payload(sample_text)
    if "--write-json" in sys.argv:
        json_path = os.path.join(os.path.dirname(__file__), "system_prompt.json")
        with open(json_path, "w") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"=== WROTE API-READY PAYLOAD TO {json_path} ===")
    else:
        print("=== OPENAI API PAYLOAD GENERATED SUCCESSFULLY ===")
        print(json.dumps(payload, indent=2))
    print("\nTo invoke via curl:")
    print("curl https://api.openai.com/v1/chat/completions \\")
    print("  -H 'Content-Type: application/json' \\")
    print("  -H 'Authorization: Bearer $OPENAI_API_KEY' \\")
    print("  -d '@adapters/codex/system_prompt.json'")
    print("\n(system_prompt.json is generated from system_prompt.txt — regenerate after edits with: python3 adapters/codex/openai_api_demo.py --write-json)")

if __name__ == "__main__":
    main()

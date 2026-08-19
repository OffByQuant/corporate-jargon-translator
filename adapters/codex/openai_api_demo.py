#!/usr/bin/env python3
"""
OpenAI / Codex API Demo Script for Corporate Jargon Translator
Demonstrates how to call the OpenAI Chat Completions API using the Corporate Jargon Translator system prompt.
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
        "model": "gpt-4o",
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
    print("=== OPENAI API PAYLOAD GENERATED SUCCESSFULLY ===")
    print(json.dumps(payload, indent=2))
    print("\nTo invoke via curl:")
    print("curl https://api.openai.com/v1/chat/completions \\")
    print("  -H 'Content-Type: application/json' \\")
    print("  -H 'Authorization: Bearer $OPENAI_API_KEY' \\")
    print("  -d '@adapters/codex/system_prompt.json'")

if __name__ == "__main__":
    main()

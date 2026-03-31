import requests
import re
from config import OPENROUTER_API_KEY,API_URL

cache = {}

API_URL=API_URL


if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found. Please set it in .env file.")


import requests
from config import OPENROUTER_API_KEY, API_URL

import requests
import os

def call_llm(messages, model, temperature=0.2):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": messages,
            "temperature": temperature
        }
    )

    print("\n[DEBUG] Status Code:", response.status_code)
    print("[DEBUG] RAW RESPONSE:", response.text)

    if response.status_code != 200:
        return "LLM_ERROR"

    return response.json()["choices"][0]["message"]["content"]
# ---------------- FORMAT CHAT → TEXT ----------------
def format_messages(messages):
    prompt = ""
    for m in messages:
        prompt += f"{m['role'].upper()}:\n{m['content']}\n"
    return prompt

# ---------------- RESPONSE PARSER ----------------
def parse_response(response):
    try:
        data = response.json()

        # HF returns list
        if isinstance(data, list):
            return data[0]["generated_text"]

        # some models return dict
        if "generated_text" in data:
            return data["generated_text"]

        return str(data)

    except Exception as e:
        return f"Error parsing response: {str(e)}"


# ---------------- CODE EXTRACT ----------------
def extract_code(text):
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()
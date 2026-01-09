import requests
from core.config import DEEPSEEK_API_KEY, DEEPSEEK_URL

def query_llm(system_prompt, user_prompt):
    headers = {
        "Authorization": f"Bearer {sk-126c061e519c4545936f79390e8fd38b}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(DEEPSEEK_URL, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]


import json
from brain.llm import query_llm
from brain.schema import SYSTEM_PROMPT

def think(user_input, available_tools):
    tools_text = ", ".join(available_tools)

    prompt = f"""
User said: "{user_input}"

Available tools:
{tools_text}

Decide what to do.
"""

    raw = query_llm(SYSTEM_PROMPT, prompt)

    try:
        return json.loads(raw)
    except:
        return {
            "intent": "unknown",
            "plan": [],
            "tool": None,
            "response": "I need clarification."
        }

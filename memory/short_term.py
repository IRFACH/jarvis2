import json

MEMORY_FILE = "memory/short_term.json"
MAX_MEMORY = 5

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def remember(user_input, jarvis_response):
    memory = load_memory()
    memory["history"].append({
        "user": user_input,
        "jarvis": jarvis_response
    })

    memory["history"] = memory["history"][-MAX_MEMORY:]
    save_memory(memory)

def get_context():
    memory = load_memory()
    context = ""
    for item in memory["history"]:
        context += f"User: {item['user']}\nJarvis: {item['jarvis']}\n"
    return context

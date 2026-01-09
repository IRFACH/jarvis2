from sensors.voice_input import VoiceInput
from sensors.wake_word import heard_wake_word, strip_wake_word
from brain.planner import think
from skills import load_skills
from output.voice_output import speak
from memory.short_term import remember
from core.permissions import has_permission

voice = VoiceInput()

def run_agent():
    print("Jarvis listening...")

    while True:
        text = voice.listen()
        print("Heard:", text)

        if not heard_wake_word(text):
            continue

        user_input = strip_wake_word(text)
        skills = load_skills()

        decision = think(user_input, skills.keys())
        tool = decision["tool"]

        if tool and not has_permission(tool):
            speak(f"I need permission to {tool}.")
            remember(user_input, "Permission required.")
            continue

        if tool in skills:
            skills[tool].execute(decision)

        speak(decision["response"])
        remember(user_input, decision["response"])

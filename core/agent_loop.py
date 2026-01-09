from brain.planner import think
from skills import load_skills
from output.voice_output import speak

def run_agent(user_input):
    skills = load_skills()
    brain_output = think(user_input, skills.keys())

    if brain_output["tool"] in skills:
        skills[brain_output["tool"]].execute(brain_output)

    speak(brain_output["response"])

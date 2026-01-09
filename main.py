from core.agent_loop import run_agent

print("Jarvis online.")

while True:
    user = input("You: ")
    run_agent(user)

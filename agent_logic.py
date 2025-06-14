import os
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

def run_agent(prompt: str) -> str:
    llm = OpenAI(temperature=0.3, openai_api_key=os.getenv("OPENAI_API_KEY"))
    tools = load_tools(["serpapi"], llm=llm)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=False)
    response = agent.run(prompt)

# Try to extract structured info (e.g., day-task pairs)
import re
calendar_data = {}
matches = re.findall(r"(Day \d+): (.+)", response)
for day, task in matches:
    calendar_data[day] = task

return calendar_data if calendar_data else {"Day 1": response}

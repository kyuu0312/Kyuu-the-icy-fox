# agent_logic.py
import os
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

# Load API keys from environment (Streamlit Cloud will handle this securely)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
assert OPENAI_API_KEY, "Set OPENAI_API_KEY as environment variable"

def run_agent(prompt: str) -> str:
    llm = OpenAI(temperature=0.3, openai_api_key=OPENAI_API_KEY)
    tools = load_tools(["serpapi", "python_repl"], llm=llm)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=False)
    return agent.run(prompt

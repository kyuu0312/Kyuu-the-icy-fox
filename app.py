# app.py
import streamlit as st
from agent_logic import run_agent

st.set_page_config(page_title="🤖 Visual AI Agent", layout="wide")
st.title("Visual Agentic AI Dashboard")

col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_area("Enter your command here:", height=150)

with col2:
    if st.button("📡 Run Agent"):
        if not user_input.strip():
            st.error("Please enter a command to run the agent.")
        else:
            with st.spinner("Agent is thinking..."):
                try:
                    result = run_agent(user_input)
                    st.success("✅ Task completed!")
                    st.write(result)
                except Exception as e:
                    st.error(f"Error: {e}")

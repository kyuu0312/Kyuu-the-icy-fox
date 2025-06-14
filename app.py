# app.py
import matplotlib.pyplot as plt
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
        if isinstance(result, dict):
            visualize_calendar(result)
        else:
            st.write(result)

    except Exception as e:
        st.error(f"Error: {e}")
def visualize_calendar(data: dict):
    st.markdown("### 🗓️ Visual Marketing Calendar")
    days = list(data.keys())
    tasks = list(data.values())

    fig, ax = plt.subplots(figsize=(10, 0.5 * len(tasks)))
    ax.barh(days, range(len(tasks)), color='skyblue')
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels(tasks)
    ax.invert_yaxis()
    ax.set_xlabel("Timeline")
    ax.set_title("Marketing Calendar")
    st.pyplot(fig)

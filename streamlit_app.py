import streamlit as st
import requests
import os

# Use environment variable for API URL, with a fallback for local development
API_URL = os.getenv("API_URL", "http://localhost:8000/research")

st.set_page_config(
    page_title="Financial Research Agent",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Financial Research Agent")
st.markdown("*Powered by Multi-Agent AI — LangGraph + Groq*")
st.divider()

# Example queries
st.markdown("**💡 Try these:**")
examples = [
    "What is the latest news about Infosys?",
    "Give me a stock analysis of TCS",
    "What is the current price of Reliance Industries?",
    "Summarize recent news about Wipro"
]
cols = st.columns(2)
for i, example in enumerate(examples):
    if cols[i % 2].button(example, use_container_width=True):
        st.session_state.query = example

st.divider()

# Query input
query = st.text_input(
    "Ask anything about a stock or company:",
    value=st.session_state.get("query", ""),
    placeholder="e.g. What is the latest news about Infosys?"
)

if st.button("🔍 Research", type="primary", use_container_width=True):
    if not query.strip():
        st.warning("Please enter a query!")
    else:
        with st.spinner("🤖 Agents are researching... please wait"):
            try:
                response = requests.post(API_URL, json={"query": query})
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Research Complete!")
                    st.divider()
                    st.markdown("### 📊 Research Result")
                    st.markdown(data["answer"])
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to API. Make sure FastAPI is running on localhost:8000")
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")

st.divider()
st.caption("⚠️ For informational purposes only. Not financial advice.")
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def responder_agent(state: dict) -> dict:
    analysis = state.get("analysis", "")
    query = state.get("query", "")
    plan = state.get("plan", {})

    prompt = f"""You are a friendly financial assistant.

User asked: {query}
Company: {plan.get('company', '')}

Based on this analysis:
{analysis}

Write a clear, concise, and helpful response for the user.
Use simple language. Format with bullet points where helpful.
End with a short disclaimer: "This is for informational purposes only, not financial advice."
"""
    response = llm.invoke(prompt)
    state["final_answer"] = response.content
    return state
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def planner_agent(state: dict) -> dict:
    query = state["query"]
    
    prompt = f"""You are a financial research planner.
Given a user query, extract:
1. Company name
2. Stock ticker symbol (e.g. INFY, TCS, RELIANCE)
3. What the user wants (news / stock price / analysis / summary)

User Query: {query}

Respond in this exact format:
COMPANY: <company name>
TICKER: <ticker symbol>
INTENT: <news|price|analysis|summary>
"""
    response = llm.invoke(prompt)
    content = response.content

    # Parse response
    lines = content.strip().split("\n")
    parsed = {}
    for line in lines:
        if "COMPANY:" in line:
            parsed["company"] = line.split("COMPANY:")[-1].strip()
        elif "TICKER:" in line:
            parsed["ticker"] = line.split("TICKER:")[-1].strip()
        elif "INTENT:" in line:
            parsed["intent"] = line.split("INTENT:")[-1].strip()

    state["plan"] = parsed
    return state
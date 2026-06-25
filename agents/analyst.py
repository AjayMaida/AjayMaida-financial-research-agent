from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def analyst_agent(state: dict) -> dict:
    retrieved = state.get("retrieved", {})
    plan = state.get("plan", {})
    query = state.get("query", "")

    stock_data = retrieved.get("stock_data", {})
    news = retrieved.get("news", [])
    vector_results = retrieved.get("vector_results", [])

    news_text = "\n".join([f"- {n.get('title', '')}: {n.get('summary', '')}" for n in news])
    vector_text = "\n".join(vector_results)

    prompt = f"""You are a senior financial analyst.

User Query: {query}
Company: {plan.get('company', 'Unknown')}
Ticker: {plan.get('ticker', 'Unknown')}

Stock Data:
- Current Price: {stock_data.get('price')}
- Market Cap: {stock_data.get('market_cap')}
- P/E Ratio: {stock_data.get('pe_ratio')}
- 52W High: {stock_data.get('52w_high')}
- 52W Low: {stock_data.get('52w_low')}

Recent News:
{news_text}

Additional Context:
{vector_text}

Provide a concise financial analysis answering the user's query.
Include key insights, risks, and opportunities if relevant.
"""
    response = llm.invoke(prompt)
    state["analysis"] = response.content
    return state
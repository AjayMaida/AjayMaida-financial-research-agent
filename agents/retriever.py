from tools.finance_tool import get_stock_info, get_recent_news
from tools.vector_store import add_documents, query_documents
import uuid

def retriever_agent(state: dict) -> dict:
    plan = state.get("plan", {})
    ticker = plan.get("ticker", "")
    query = state.get("query", "")

    stock_data = {}
    news_data = []

    if ticker:
        stock_data = get_stock_info(ticker)
        news_data = get_recent_news(ticker)

        # Store in ChromaDB for future queries
        docs = []
        if stock_data.get("summary"):
            docs.append({
                "id": str(uuid.uuid4()),
                "text": stock_data["summary"],
                "metadata": {"ticker": ticker, "type": "summary"}
            })
        for news in news_data:
            if news.get("title"):
                docs.append({
                    "id": str(uuid.uuid4()),
                    "text": news["title"] + " " + news.get("summary", ""),
                    "metadata": {"ticker": ticker, "type": "news"}
                })
        if docs:
            add_documents(docs)

    # Also query existing ChromaDB
    vector_results = query_documents(query)

    state["retrieved"] = {
        "stock_data": stock_data,
        "news": news_data,
        "vector_results": vector_results
    }
    return state
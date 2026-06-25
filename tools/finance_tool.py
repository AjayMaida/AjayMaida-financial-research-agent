import yfinance as yf

def get_stock_info(ticker: str) -> dict:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            "name": info.get("longName", ticker),
            "price": info.get("currentPrice"),
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "52w_high": info.get("fiftyTwoWeekHigh"),
            "52w_low": info.get("fiftyTwoWeekLow"),
            "summary": info.get("longBusinessSummary", "")[:500],
        }
    except Exception as e:
        return {"error": str(e)}

def get_recent_news(ticker: str) -> list:
    try:
        stock = yf.Ticker(ticker)
        news = stock.news[:5]
        return [
            {
                "title": n.get("content", {}).get("title", ""),
                "summary": n.get("content", {}).get("summary", ""),
            }
            for n in news
        ]
    except Exception as e:
        return [{"error": str(e)}]
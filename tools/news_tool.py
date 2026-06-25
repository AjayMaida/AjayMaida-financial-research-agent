import requests
from dotenv import load_dotenv

load_dotenv()

def get_financial_news(query: str) -> list:
    """
    Fetches financial news using RSS feeds — completely free, no API key needed.
    """
    import urllib.request
    import xml.etree.ElementTree as ET

    # Google News RSS — free, no key required
    encoded_query = urllib.parse.quote(query + " stock finance")
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-IN&gl=IN&ceid=IN:en"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()

        root = ET.fromstring(xml_data)
        items = root.findall(".//item")

        news_list = []
        for item in items[:5]:
            title = item.findtext("title", "")
            description = item.findtext("description", "")
            pub_date = item.findtext("pubDate", "")
            link = item.findtext("link", "")

            news_list.append({
                "title": title,
                "summary": description[:300] if description else "",
                "published": pub_date,
                "link": link
            })

        return news_list

    except Exception as e:
        return [{"error": str(e)}]


import urllib.parse  # make sure this is at top
import requests
from bs4 import BeautifulSoup
import json

def crawl(keyword):
    headers = {"User-Agent": "Mozilla/5.0"}
    search_url = f"https://www.bing.com/search?q={keyword}+site:medium.com"

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = [a["href"] for a in soup.find_all("a", href=True) if "http" in a["href"]]
    results = []

    for url in links[:5]:
        try:
            article_resp = requests.get(url, headers=headers, timeout=5)
            article_soup = BeautifulSoup(article_resp.text, "html.parser")
            title = article_soup.title.string if article_soup.title else "Untitled"
            content = " ".join(p.get_text() for p in article_soup.find_all("p"))

            if len(content.strip()) > 100:
                results.append({
                    "url": url,
                    "title": title,
                    "content": content.strip()
                })
        except Exception as e:
            print(f"Error processing {url}: {e}")

    with open("crawled_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return results

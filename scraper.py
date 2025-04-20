import requests
from bs4 import BeautifulSoup

def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Failed to fetch page:", response.status_code)
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.select("a.storylink") or soup.select("span.titleline > a")

    print("\n📰 Hacker News Headlines:\n")
    for i, h in enumerate(headlines[:10], 1):
        print(f"{i}. {h.get_text(strip=True)}")
        print(f"   🔗 {h['href']}\n")

if __name__ == "__main__":
    scrape_hackernews()

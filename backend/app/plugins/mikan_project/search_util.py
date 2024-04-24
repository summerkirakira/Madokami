from bs4 import BeautifulSoup
from .models import MikanSearchResult


def get_search_results(html) -> MikanSearchResult:
    soup = BeautifulSoup(html, "html.parser")
    bangumi_li = soup.select("#sk-container > div.central-container > ul")
    search_results = MikanSearchResult()
    for li in bangumi_li:
        link = li.select_one("a").get("href")
        cover = li.select_one("a > span").get("data-src")
        title = li.select_one("a > div > div").text.replace("\n", "").strip()
        link = f"https://mikanani.me{link}"
        cover = f"https://mikanani.me{cover}"
        search_results.bangumis.append(
            MikanSearchResult.Bangumi(
                link=link,
                title=title,
                cover=cover
            )
        )
    return search_results

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request
from bs4 import BeautifulSoup
import time

url = "뉴스링크"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
#soup.select_one()
results = soup.select("#section_body a")
for result in results:
    url_article = result.attrs["href"]
    response = urllib.request.urlopen(url_article)
    soup_article = BeautifulSoup(response, "html.parser")
    content = soup_article.select_one("#article_Body")

    output = ""
    for item in content.contents:
        stripped = str(item).strip()
        if stripped == "":
            continue
        if stripped[0] not in ["<", "/"]:
            output += str(item).strip()
    print(output.replace("본문 내용TV플레이어", ""))

    time.sleep(30)

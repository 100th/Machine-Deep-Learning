import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup
#세션 만들기
session = requests.session()
#로그인
url = "https://xxxxxxx"
data = {
    "user_id": "xxxxxx",
    "user_pw": "xxxxxx"
}
response = session.post(url, data=data)
response.raise_for_status()

#내 점수 들고오기
url = "https://xxxxxxxxx"
response = session.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
text = soup.select_one(".attempts a")
print("내 점수: ", text)

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request
from bs4 import BeautifulSoup

url = "http://info.finance.naver.com/marketindex/?tabSel=exchange#tab_section"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
#soup.select_one()
results = soup.select("span.value")
results[0] #원달러 환율
print("달러:", results[0].string)
print("엔:", results[1].string)
print("유로:", results[2].string)


"""
for result in results:
   print(result.string)
"""

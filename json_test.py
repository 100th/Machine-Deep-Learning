import urllib.request as request
import json

json_str = request.urlopen("https://api.github.com/repositories").read().decode('utf8')
output = json.loads(json_str)

for item in output:
    print(item["name"])
    print(item["full_name"])
    print(item["owner"]["login"])
    print()

"""
import json
json_str = """[
    {"name" : "사과", "price": 1000},
    {"name" : "바나나", "price": 2000},
    {"name" : "배", "price": 3000},
    {"name" : "귤", "price": 4000},
]"""
# JSON 문자열 -> 파이썬 자료형
output = json.loads(json_str)
print(type(output))
print()
# 파이썬 자료형 -> JSON 문자열
text = json.dumps(output)
print(type(text))
"""

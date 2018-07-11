from sklearn import svm, metrics
import glob, os.path, re, json
import matplotlib.pyplot as plt
import pandas as pd

files = glob.glob("./train/*.txt")
train_data = []
train_label = [] # 위 3개 train -> test 로 변경한 것도
for file_name in files:
    # 레이블 구하기
    basename = os.path.basename(file_name)
    basename.split("-")[0] # 정규표현식 대신
    print(basename, lang)
    # 텍스트 추출하기
    file = open(file_name, "r", encoding="utf-8") # with구문 사용해도 됨
    text = file.read()
    text = text.lower()
    file.close() # with 구문 쓰면 위, 아래가 같이 됨
    # 알파벳 출현 빈도 구하기
    code_a = ord("a")
    code_a = ord("z")
    count = [0 for n in range(0, 26)]
    # count = [0, 0, 0, ... 26개 리스트 만들기]
    for character in text:
        code_current = ord(character)
        if code_a <= code_current <= code_z:
            #'a'97 - 'a'97 = 0
            #'b'98 - 'a'97 = 1
            count[code_current - code_a] += 1
    # 정규화
    total = sum(count)
    count = list(map(lambda n: n / total, count))
    # 리스트에 넣기
    train_label.append(count)
    train_data.append(count)

# 그래프 준비하기
graph_dict = {}
for i in range(0, len(train_label)):
    label = train_label[i]
    data = train_data[i]
    if not (label in graph_dict):
        graph_dict[label] = data
asclist = [[chr(n) for n in range(97, 97 + 26)]]
print(asclist)
df = pd.DataFrame(graph_dict, index=asclist)

# 그래프 그리기
plt.style.use('ggplot')
df.plot(kind="bar", subplots=True, ylim=(0,0.15))
plt.savefig("lang-plot.png")

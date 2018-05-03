from sklearn import svm, metrics
import glob, os.path, re, json

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

# 학습시키기
clf = svm.SVC()
clf.fit(train_data, train_label)
predict = clf.predict(test_data)
score = metrics.accuracy_score(test_label, predict)
report = metrics.classification_report(test_label, predict)
print("score=", score)
print("--- report ---")
print(report)

# lambda (간단함)
# def test(n):
#    return 10

"""
    print(file_name)
    print(basename)
    print("-----")
"""

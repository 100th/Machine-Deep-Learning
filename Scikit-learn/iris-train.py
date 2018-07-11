import pandas
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pandas.read_csv("iris.csv")
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]

train_data, test_data, train_label, test_label =\
    train_test_split(data, label)

clf = svm.SVC()
clf.fit(train_data, train_label)
results = clf.predict(test_data)

score = metrics.accuracy_score(results, test_label)
print("정답률:", score)
# 가장 전형적인 기계학습 형태
# 여기서 CSV파일에 내 데이터를 넣으면 기계학습이 가능하다.

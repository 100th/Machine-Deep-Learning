import pandas
from sklearn import svm, metrics

csv = pandas.read_csv("iris.csv")
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]

clf = svm.SVC()
clf.fit(data, label)
results = clf.predict([
    [5.1, 3.0, 1.3, 0.2]
])
print(results)

# score = metrics.accuracy_score()
# print("정답률:", score)

# 모듈 읽어 들이기
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

# 데이터 가공하기
csv = pd.read_csv("bmi.csv")
csv["weight"] /= 100
csv["height"] /= 200

bmi_class = {
    "thin" : [1, 0 , 0],
    "normal" : [0, 1, 0],
    "fat" : [0, 0, 1]
}
y = np.empty((20000, 3))
for i, v in enumerate (csv["label"]):
    y[i] = bmi_class[v]

x = csv[["weight", "height"]].as_matrix()

x_train, y_train = x[1:15001], y[1:15001]
x_test, y_test = x[15001:20001], y[15001:20001]

"""
[
    [<키> / 200, <몸무게> / 100], # 0.0 ~ 1.0
    [<키> / 200, <몸무게> / 100],
    [<키> / 200, <몸무게> / 100]
]

[
    'thin',     # [1, 0, 0]
    'normal',   # [0, 1, 0]
    'fat'       # [0, 0, 1]
]
"""
# 모델 만들기
model = Sequential()
    # 레이어 형성
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile("rmsprop", "categorical_crossentropy", metrics = ['accuracy'])

# 학습시키기
model.fit(
    x_train, y_train,
    batch_size=100,
    nb_epoch=20,
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1)

# 예측 하기 : model.predict()

# 정답률 구하기
score = model.evaluate(x_test, y_test)
print()
print("score loss:", score[0])
print("score accuracy:", score[1])

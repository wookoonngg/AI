# Assignment1 - 결축치 값을 산술평균으로 채워 넣는 다양한 방법을 적용하시오.
# Assignment 2 - 위 과제의 사이킬러 라이브러리를 주석처리 하고 결축치를 산술평균으로 채워 넣으시오

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split


# 나이에 따른 생존율 계산

titanic = sns.load_dataset('titanic')  # 데이터 로딩
median_age = titanic['age'].median()  # 나이 중앙값 산출
titanic_fill_row = titanic.fillna({'age' : median_age})  # 결측치 처리

X = titanic_fill_row[['age']]  # 독립 변수 설정
y = titanic_fill_row[['survived']]  # 종속 변수 설정

# 훈련/검증 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 선택
model = KNeighborsRegressor(n_neighbors=5)

# K 최근접 이웃 회귀 모델 훈련
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)  # 검증 셋트를 인수로 예측

# 시각화
plt.figure(figsize=(5, 2))
plt.scatter(X_test, y_test, color='blue', label='Real')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.title('KNeighborsRegressor: Real vs Predicted')
plt.xlabel('Age')
plt.ylabel('Survivied')
plt.show()


'''
[seaborn 클래스 함수 구조]
survived -> 1이면 생존 0 이면 사망
Pclass -> 선실 등급 1~3등급까지
Fare -> 티켓에 대해 지불한 금액
'''




# df = pd.DataFrame(
#     {
#         'A' : [1,2, np.nan,4],
#         'B' : [np.nan, 12,3,4],
#         'C' : [1,2,3,4]
#     }
# )
#
# print(df)
#
# df.fillna(df.mean(), inplace = True)
#
# print ("평균으로 채운 뒤 데이터\n" , df)
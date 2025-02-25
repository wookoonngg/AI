import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import matplotlib.pyplot as plt

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
X = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values

ls.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23500, 62500, 4, 9])
plt.show()

#model = LinearRegression()
model = KNeighborsRegressor()
model.fit(X, y)

X_new = [[31721.3]]  # ROK 2020
print(model.predict(X_new))
# LinearRegression 5.90
# KNeighborsRegressor 5.70













# class LinearRegression:
#     def __init__(self):
#         self.slope = None  # 기울기
#         self.intercept = None  # bias
#
#
#     def fit(self, X, y):
#         """
#         learning function
#         :param X: independent variable (2d array format)
#         :param y: dependent variable (2d array format)
#         :return: void
#         """
#         X_mean = np.mean(X)
#         y_mean = np.mean(y)
#
#         denominator = np.sum(pow(X-X_mean, 2))
#         numerator = np.sum((X-X_mean)*(y-y_mean))
#
#         self.slope = numerator / denominator
#         self.intercept = y_mean - (self.slope * X_mean)
#
#
#     def predict(self, X) -> np.ndarray:
#         """
#         predict value for input
#         :param X: new indepent variable
#         :return: predict value for input (2d array format)
#         """
#         return self.slope * np.array(X) + self.intercept






# ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
# print(ls)
#
# x=ls[["GDP per capita (USD)"]].values
# y=ls[["Life satisfaction"]].values
#
# #print(x)
#
# ls.plot(kind = 'scatter', grid=True, x="GDP per capita (USD)", y = "life satisfaction")
# plt.axis([23500,62500,4,9])
# plt.show()





# df = pd.DataFrame(
#     [[4, 7, 10],
#      [5, 8, 11],
#      [6, 9, 12]], index=[1, 2, 3], columns=['a', 'b', 'c']
# )
# print(df)


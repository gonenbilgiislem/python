import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



data = pd.read_csv("hw_25000.csv")

boy = data.Height.values.reshape(-1,1)
kilo = data.Weight.values.reshape(-1,1)
regression = LinearRegression()
regression.fit(boy,kilo)
# print(regression.predict(71))
print(regression.predict(([[71]])))
# print(data.columns)

plt.scatter(data.Height,data.Weight)
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.show()
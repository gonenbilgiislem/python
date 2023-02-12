# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


data = pd.read_csv("insurance.csv")
print(data.columns)
print(data.describe())
## y ekseni
expenses = data.expenses.values.reshape(-1,1)
## x ekseni
ageBmis = data.iloc[:,[0,2]].values

regression = LinearRegression()
regression.fit(ageBmis,expenses)
print(regression.predict(np.array([[10,20],[30,21],[30,22],[30,23],[30,24]])))







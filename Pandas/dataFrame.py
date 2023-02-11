# -*- coding: utf-8 -*-

import pandas as pd

data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)
print("**********************")
data2 = [["Engin",33,"Ankara"],["Derin",4,"Ankara"],["Salih",32,"İstanbul"]]
df2 = pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"],index=[1,2,3])
print(df2)
print("**********************")
data3 = {"İsim":["Engin","Derin","Salih"],
         "Yaş":[33,4,32],
         "Şehir":["Ankara","Ankara","İstanbul"]}
df3 = pd.DataFrame(data3,columns=["İsim","Yaş","Şehir"],index=[1,2,3])
print(df3["Yaş"])
print("**********************")
#del df3["Şehir"]
#df3.pop("Şehir")
print(df3)
print("**********************")
print(df3.loc[2])
print("**********************")
print(df3.iloc[1])
print("**********************")
# df4 = df3.append(df2)
df4 = pd.concat([df2,df3])
print(df4)
print("Concat Üst **********************")
print(df4.head())
print("**********************")
print(df4.tail())
print("**********************")
df4.drop(2)
print("**********************")
print(df4)





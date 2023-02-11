# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["İsim","Soyisim","SSN"
                  ,"Test1","Test2","Test3","Test4"
                  ,"Final","Sonuc"]
print("**********************")
print(notlar)
print("**********************")
print(type(notlar))
print("**********************")
print(notlar.head())
print("**********************")
print(notlar.tail())
print("**********************")
print(notlar["Final"])
print("**********************")
print(notlar.iloc[2])
print("**********************")
print(notlar[0:10])
print("**********************")
# _*_ coding: utf-8 _*_
from inspect import currentframe

tupleListe = (2,4,6,"Ankara",(3,5,7))
liste = [2,4,6,"Ankara",[3,5,7]]
tupleDeger = ("Ankara",)
print(currentframe().f_lineno, ":", tupleDeger)
print(currentframe().f_lineno, ":", type(tupleDeger))


print(currentframe().f_lineno, ":",type(tupleListe))
print(currentframe().f_lineno, ":",type(liste))
print(currentframe().f_lineno, ":",tupleListe)
print(currentframe().f_lineno, ":",liste)
print(currentframe().f_lineno, ":",len(tupleListe))
print(currentframe().f_lineno, ":",len(liste))
print(currentframe().f_lineno, ":",tupleListe[0])
print(currentframe().f_lineno, ":",liste[0])
print(currentframe().f_lineno, ":",tupleListe[3])
print(currentframe().f_lineno, ":",liste[3])
print(currentframe().f_lineno, ":",tupleListe[4])
print(currentframe().f_lineno, ":",liste[4])
print(currentframe().f_lineno, ":",tupleListe[4][1])
print(currentframe().f_lineno, ":",liste[4][1])
print(currentframe().f_lineno, ":",str(tupleListe[3][2:])+"am")
















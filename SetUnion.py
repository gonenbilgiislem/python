from inspect import currentframe

setA = {1, 2, 3, 4, 5}
setB = {1, 3, 4, 6, 7, 8}

setC = setA.union(setB)
print(currentframe().f_lineno, ".Satır :", setC)

setC = setA.intersection(setB)
print(currentframe().f_lineno, ".Satır :", setC)

setC = setA.difference(setB)
print(currentframe().f_lineno, ".Satır :", setC)
setC = setB.difference(setA)
print(currentframe().f_lineno, ".Satır :", setC)

setC = setA.symmetric_difference(setB)
print(currentframe().f_lineno, ".Satır :", setC)

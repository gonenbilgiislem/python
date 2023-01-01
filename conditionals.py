from inspect import currentframe

sayi1 = -1
sayi2 = -10
sayi3 = 0
sayi4 = 10
sayi5 = 1
if sayi1 > 0:
    print(currentframe().f_lineno, ".Satır :", "sayi1 pozitif")
elif sayi1 < 0:
    print(currentframe().f_lineno, ".Satır :", "sayi1 negatif")
if sayi2 > 0:
    print(currentframe().f_lineno, ".Satır :", "sayi2 pozitif")
elif sayi2 < 0:
    print(currentframe().f_lineno, ".Satır :", "sayi2 negatif")
if sayi3 > 0:
    print(currentframe().f_lineno, ".Satır :", "sayi3 pozitif")
elif sayi3 < 0:
    print(currentframe().f_lineno, ".Satır :", "sayi3 negatif")
if sayi4 > 0:
    print(currentframe().f_lineno, ".Satır :", "sayi4 pozitif")
elif sayi4 < 0:
    print(currentframe().f_lineno, ".Satır :", "sayi4 negatif")
if sayi5 > 0:
    print(currentframe().f_lineno, ".Satır :", "sayi5 pozitif")
elif sayi5 < 0:
    print(currentframe().f_lineno, ".Satır :", "sayi5 negatif")

# Path: conditionals.py
x = 10
y = 20
z = 30
if x > y and x > z:
    print(currentframe().f_lineno, ".Satır :", "x en büyük")
elif y > x and y > z:
    print(currentframe().f_lineno, ".Satır :", "y en büyük")
elif z > x and z > y:
    print(currentframe().f_lineno, ".Satır :", "z en büyük")

# Path: conditionals.py
x = 10
y = 20
z = 30
if x > y or x > z:
    print(currentframe().f_lineno, ".Satır :", "x en büyük")
elif y > x and y > z:
    print(currentframe().f_lineno, ".Satır :", "y en büyük")
elif z > x or z > y:
    print(currentframe().f_lineno, ".Satır :", "z en büyük")

# Path: conditionals.py
x = 10
y = 20
z = 30
if x > y:
    if x > z:
        print(currentframe().f_lineno, ".Satır :", "x en büyük")
elif y > x:
    if y > z:
        print(currentframe().f_lineno, ".Satır :", "y en büyük")
elif z > x:
    if z > y:
        print(currentframe().f_lineno, ".Satır :", "zzz en büyük")

# Path: conditionals.py
x = 10
y = 20
z = 30
if x > y:
    if x > z:
        print(currentframe().f_lineno, ".Satır :", "x en büyük")
elif y > x:
    if y < z:
        print(currentframe().f_lineno, ".Satır :", "y en büyük")
elif z > x:
    if z > y:
        print(currentframe().f_lineno, ".Satır :", "z en büyük")
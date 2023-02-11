from inspect import currentframe

# frameinfo = getframeinfo(currentframe())
# ogrenciler = ["Engin", "Derin", "Salih"]
# ogrenciler.append("Ahmet")
# print(ogrenciler[3])
# print(ogrenciler)

# List constructor
sehirler = list(("Ankara", "İstanbul", "Ankara"))
print(currentframe().f_lineno, ":", sehirler)
print(currentframe().f_lineno, ":", len(sehirler))
print(currentframe().f_lineno, ":", "Ankara sayısı = " + str(sehirler.count("Ankara")))
print(currentframe().f_lineno, ":", sehirler)
print(currentframe().f_lineno, ":", "Ankara indexi = " + str(sehirler.index("Ankara")))
sehirler.pop(1)
sehirler.insert(0, "Istanbul")
print(currentframe().f_lineno, ":", sehirler)
sehirler.reverse()
lineo = currentframe().f_lineno + 1
print(lineo, ":", sehirler)
sehirler3 = sehirler.copy()
sehirler2 = sehirler
sehirler2[0] = "İzmir"
print(currentframe().f_lineno, ":", sehirler)
print(currentframe().f_lineno, ":", sehirler2)
print(currentframe().f_lineno, ":", sehirler3)
print(currentframe().f_lineno, ":", sehirler.count("Ankara"))
print(currentframe().f_lineno, ":",sehirler)
sehirler.insert(0, "Istanbul")
print(currentframe().f_lineno, ":",sehirler)
sehirler.reverse()
print(currentframe().f_lineno, ":",sehirler)
sehirler2 = sehirler
sehirler2[0] = "İzmir"
print(currentframe().f_lineno, ":",sehirler)
print(currentframe().f_lineno, ":",sehirler2)
sehirler.extend(("Konya", "Antalya"))
print(currentframe().f_lineno, ":",sehirler)
sehirler.sort()
print(currentframe().f_lineno, ":",sehirler)
sehirler.sort(reverse=True)
print(currentframe().f_lineno, ":",sehirler)
sehirler.clear()
print(currentframe().f_lineno, ":",sehirler)

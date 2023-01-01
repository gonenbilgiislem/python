#%%
def selamVer(isim):
    print("Selam", isim)

isim = ""
isim = input("İsminiz nedir? ")
if isim == "":
    print("Merhaba Dünyalı")
else:
    selamVer(isim)
#%%
def dikUcgenAlanHesapla(a, b):
    return (a * b) / 2

print(dikUcgenAlanHesapla(3, 4))
#%%
"""Bu fonksiyon üçgenin alanını hesaplar tek satırlık bir fonksiyondur"""
dikUcgenAlanHesapla2 = lambda a, b: (a * b) / 2
print(dikUcgenAlanHesapla2(3, 4))
print(type(dikUcgenAlanHesapla2))
x = dikUcgenAlanHesapla2
print(x(4, 5))





birinciSayi = int(input("Birinci Sayıyı Giriniz : "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))

if (birinciSayi > ikinciSayi):
    kucuksayi = ikinciSayi
else:
    kucuksayi = birinciSayi
for i in range(1, kucuksayi + 1):
    if (birinciSayi % i == 0) and (ikinciSayi % i == 0):
        OKEK = i
        OBEB = (birinciSayi * ikinciSayi) // OKEK

print("OKEK:", OKEK)
print("OBEB:", OBEB)
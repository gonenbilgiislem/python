# asal sayıları bulma

sayi = int(input("Sayı giriniz: "))
asalmi  = "Evet"
for x in range(2, sayi):
    if sayi % x == 0:
        asalmi = "Hayır"
        break
print("Asal mı? ", asalmi)
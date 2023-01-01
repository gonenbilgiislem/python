# Faktoriyel hesaplama
def faktoriyel(sayi):
    if sayi == 1:
        return 1
    else:
        return sayi * faktoriyel(sayi - 1)

sayi = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı giriniz: "))
print(faktoriyel(sayi))


#%% sssss
sayi = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı giriniz: "))
faktoriyel = 1

if sayi < 0:
    print("Negatif sayıların faktoriyeli bulunamaz.")
elif sayi == 0:
    print("Sonuç = 1")
else:
    for i in range(1, sayi + 1):
        faktoriyel = faktoriyel * i
    print(f'{sayi} `nın Faktoriyeli  {faktoriyel} dir.')


def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1,sayi2):
    return sayi1 - sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2

print("Toplama işlemi için 1'e, çıkarma işlemi için 2'ye, çarpma işlemi için 3'e, bölme işlemi için 4'e basınız.")
islem = int(input("İşlem seçiniz: "))

sayi1 = int(input("Birinci sayı: "))
sayi2 = int(input("İkinci sayı: "))

if islem == 1:
    print(sayi1,"+",sayi2,"=", topla(sayi1,sayi2))
elif islem == 2:
    print(sayi1,"-",sayi2,"=", cikar(sayi1,sayi2))
elif islem == 3:
    print(sayi1,"*",sayi2,"=", carp(sayi1,sayi2))
elif islem == 4:
    print(sayi1,"/",sayi2,"=", bol(sayi1,sayi2))
else:
    print("Geçersiz işlem seçimi!")
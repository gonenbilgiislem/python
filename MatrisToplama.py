#Matris Toplama
#Matrislerin toplamını bulan program
#Matrislerin boyutları aynı olmalıdır.
#Matrislerin boyutları kullanıcı tarafından girilmelidir.
#Matrislerin elemanları 0 ile 9 arasında olmalıdır.

#Matrislerin boyutlarını kullanıcıdan alalım.
satir = int(input("Matrisin satır sayısını giriniz: "))
sutun = int(input("Matrisin sütun sayısını giriniz: "))
#Matrislerin elemanlarını kullanıcıdan alalım.
matris1 = []
for i in range(satir):
    matris1.append([])
    for j in range(sutun):
        matris1[i].append(int(input(f'Matris1[{i}][{j}] = ')))
matris2 = []
for i in range(satir):
    matris2.append([])
    for j in range(sutun):
        matris2[i].append(int(input(f'Matris2[{i}][{j}] = ')))
#Matrislerin toplamını bulalım.
matrisToplam = []
for i in range(satir):
    matrisToplam.append([])
    for j in range(sutun):
        matrisToplam[i].append(matris1[i][j] + matris2[i][j])
#Matrislerin toplamını ekrana yazdıralım.
print("Matris1 + Matris2 = ")
for i in range(satir):
    for j in range(sutun):
        print(matrisToplam[i][j], end = ' ')
    print()

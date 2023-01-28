ogrenciler = ["Ali", "Veli", "Ayşe", "Fatma", "Ahmet", "Mehmet"]

asdf = open("ogrenciler.txt", "w")
for ogrenci in ogrenciler:
    asdf.write(ogrenci +  "\n")
asdf.close()



asdf = open("ogrenciler.txt", "w")
for asd in range(len(ogrenciler)):
    print("{}. {}".format(asd, ogrenciler[asd]))
    asdf.write(str(asd + 1) + "." + ogrenciler[asd] + "\n")
asdf.close()



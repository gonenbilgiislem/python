import sys

liste = [7,'engin',0,3,"6"]
for x in liste:
    try:
        print("Sayı: " + str(x))
        sonuc = 1/int(x)
        print("Sonuç: " + str(sonuc))
    except (sys.exc_info()[0]):
        if sys.exc_info()[0] == ValueError:
            print("Hesaplanamdı-",sys.exc_info()[0])
        elif sys.exc_info()[0] == ZeroDivisionError:
            print("Hesaplanamdı", sys.exc_info()[0])
        else:
            print("Hesaplanamdı")
            print("Hata: ", sys.exc_info()[0])
    finally:
        print("İşlem tamamlandı")
    print("**********")
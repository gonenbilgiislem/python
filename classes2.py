#Hesap Makinesi Uygulaması (Hesap Makinesi Uygulaması)

class HesapMakinesi:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2

hesap = HesapMakinesi(5, 6)
print(hesap.topla())
print(hesap.cikar())
print(hesap.carp())
print(hesap.bol())

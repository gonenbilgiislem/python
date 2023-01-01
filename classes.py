class Matematik:
    def topla(self,sayi1, sayi2):
        return sayi1 + sayi2

    def cikar(self, sayi1, sayi2):
        return sayi1 - sayi2

    def carp(self, sayi1, sayi2):
        return sayi1 * sayi2

    def bol(self, sayi1, sayi2):
        return sayi1 / sayi2

mate = Matematik()
print(mate.topla(5, 6))
print(mate.cikar(5, 6))
print(mate.carp(5, 6))
print(mate.bol(5, 6))
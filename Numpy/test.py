import numpy as np

n = 25 # dizi elemani sayisi
r = range(n) # [0,n] arasindaki tam sayilari iceren bir range nesnesi
a1 = np.array(r) # r range nesnesinin bir numpy dizisine donusturulmesi
a2 = np.zeros(n) # sadece 0 (sifir)'lardan olusan n elemanli dizi
a3 = np.ones(n) # sadece 1 (bir)'lerden olusan n elemanli dizi
p = 1; q = 5; n = 5 # baslangic (p), son (q) ve elaman sayisi (n)
a4 = np.linspace(p,q,n) # p ve q arasinda n tane eleman iceren dizi
print("linspace ile olusturulan a4 dizisi: ", a4)
# p ve q arasinda (p-q)/n aralikli n tane eleman iceren dizi
a5 = np.arange(p,q+1,(q - p) / (n - 1))
print("arange ile olusturulan a4 dizisi: ", a5)
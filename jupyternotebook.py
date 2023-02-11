import os
secim = int(input("jupyter notebook için 1 ,jupyter-lab için 2 giriniz"))
if secim == 1 :
    os.system("jupyter notebook")
elif secim == 2:
    os.system("jupyter-lab")
else:
    print("Doğru Seçim Giriniz")
#%%
a = ['1']
a.append()
print(a)

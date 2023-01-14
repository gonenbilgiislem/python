Brut_Urcret = int(input("Brüt Ücreti Giriniz: "))

Gss = (Brut_Urcret * 14) / 100
print(Gss)
ISIPK = (Brut_Urcret * 1) / 100
print(ISIPK)
Kesinti = Gss + ISIPK
print(Kesinti)
GVM = Brut_Urcret- Kesinti
print(GVM)
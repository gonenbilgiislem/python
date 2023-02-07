#sayilar = [1,2,3,4,5]

#sayilarKareli = []
# sayilarKareli = list(map(lambda sayi: sayi**2,sayilar))


# for sayi in sayilar:
#     sayilarKareli.append(sayi*sayi)

# print(sayilarKareli)
#%%

numbers = [1,3,5,9,10,4]


def square(num):
    return num ** 2

result = list(map(square,numbers))

# -*- coding: utf-8 -*-

sozluk = {
        "book" : "kitap",
        "table" : "masa"
        }
sozluk2 = dict(kitap="book",masa="table")

print(sozluk)
sozluk["book"] = "kitap 1"
print(sozluk["book"])

sozluk["pencil"] = "kalem"

del(sozluk["book"])
print(sozluk)

print(len(sozluk))
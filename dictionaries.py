sozluk = {"book": "kitap",
          "table": "masa"}
print(sozluk)
print(sozluk["book"])
print(sozluk["table"])

sozluk["pencil"] = "kalem"
print(sozluk)

del sozluk["pencil"]
print(sozluk)

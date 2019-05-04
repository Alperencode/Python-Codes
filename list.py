print("Liste Fonksiyonları".upper())
print("")

liste = ["a","b","c"]

for i in dir(liste):
    if i[0] != "_":
        print(i)

print("")
print("APPEND")

liste.append("d")  #  liste += ["d"]
print(liste)

print("")
print("İNDEX")

print(liste.index("a")) # liste index sayısını öğrenmek için

print("")
print("COUNT")

print(liste.count("a")) # liste içinde arama saydırmak istediğim elemanı fonksiyonun içine gönderiyorum

print("")
print("(-) İNDEX")

print(liste[-0]) # her elemanın 2 index'i var (-) ve (+) indexler

print("")
print("LEN FONSİYONU YAZMAK")

count=0            # Sayaç
for x in liste:    # For döngüsü ile listeyi saydırma
    count += 1     # Döngü her döndüğünde sayacı arttırma dolayısıyla liste elemanı kadar sayacın artması

print(count)

print("")
print("REVERSE")

liste.reverse()
print(liste)

print("")
print("SORT")

liste.sort()
print(liste)

print("")
print("NUMBER SORT")

liste2 = [6,5,2,4,1,3,7,6]

print(liste2)
liste2.sort()
print(liste2)

print("")
print("EXTEND")           # Listeye eleman ekleme

liste.extend("f")  # sadece 1 eleman
print(liste)

print("")

print("Writed by Alperen")

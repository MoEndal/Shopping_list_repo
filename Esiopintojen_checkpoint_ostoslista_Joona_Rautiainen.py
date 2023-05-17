import re

print("-" * 81)
print("Hei ja tervetuloa täyttämään ostoslistaa hedelmäsalaattia varten! ")
print("Ohjelma pyytää sinua lisäämään ostoslistaan tuotteet ja niiden hinnat. ")
mjono = ("Lisättyäsi kaikki tuotteet, ohjelma näyttää edullisimman ja kalleimman tuotteen. ")
print(mjono)
print("-" * len(mjono))

print()
luku = input("Kuinka monta tuotetta haluat lisätä kauppalistaan? ")
print(f"Kiitos! Seuraavaksi pääset syöttämään {luku} tuotetta kauppalistaan!")
print()

tuote = ()
ol = []

for x in range(int(luku)):
    tuotenimi = input("Tuote: ")
    tuotehinta = float(input("Hinta, €: "))
    tuote = (tuotehinta, tuotenimi)
    ol.append(tuote)
    
jarj = sorted(ol)

halvin = min(jarj)
kallein = max(jarj)
print()

#Näytetään kauppalista:
k_j = ("Kauppalistaan lisätty: ")
print(k_j)
print("-" * len(k_j))

for x in range(len(ol)):
    print(f"- {ol[x][1]} {ol[x][0]} €")

print("-" * len(k_j))
print()

#Näytetään edullisin ja kallein tuote:
print(f"Edullisin tuote on: {halvin[1]}, {halvin[0]} €")
print(f"Kallein tuote on: {kallein[1]}, {kallein[0]} €")

print()
#Lopetus:
print("Mukavia kauppahetkiä! ")
print()
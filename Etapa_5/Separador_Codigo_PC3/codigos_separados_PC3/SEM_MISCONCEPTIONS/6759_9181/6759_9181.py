entrega = 50
distancia = int(input("Distancia"))

if distancia < "10":
total = entrega + 5.50
print(round(total,2))

else distancia == "10":
total = entrega + 7.75
print(round(total,2))

elif distancia > "10":
total = entrega + 10
print(round(total,2))
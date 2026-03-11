distancia = float(input("Distancia de entrega em km: "))
entrega_fix = 50

if distancia < 10:
	total = entrega_fix + 5.50
elif distancia == 10:
	total = entrega_fix + 7.75
else:
	total = entrega_fix + 10
	
print(round(total, 2))

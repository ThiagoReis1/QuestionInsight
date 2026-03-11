compra = input()
suma = 0
horti = 0
lac = 0
en = 0

for i in compra:
	if i.upper() == "H":
		suma += 3.85
		horti += 1
	elif i.upper() == "L":
		suma += 2.95
		lac += 1
	else:
		suma += 7.90
		en += 1
		
print(round(suma,2),horti,lac,en)

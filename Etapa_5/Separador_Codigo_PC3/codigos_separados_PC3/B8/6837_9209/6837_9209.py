compras = input("informe as compras: ").upper()

i = 0
total = 0

while i < len(compras):
	if compras[i] == "I":
		total = total + 3.75
	elif compras[i] == "M":
		total = total + 4.50
	elif compras[i] == "S":
		total = total + 2.90
	i += 1
print(round(total,2))
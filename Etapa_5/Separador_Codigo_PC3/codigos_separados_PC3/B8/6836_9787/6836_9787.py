produtos = input("compras: ").upper()

i = 0
totalp = 0

while i < len(produtos):
	if produtos[i] == "B":
		totalp += 6.80
	elif produtos[i] == "C":
		totalp += 11.75
	elif produtos[i] == "M":
		totalp += 5.90
	i += 1
print(round(totalp, 2))



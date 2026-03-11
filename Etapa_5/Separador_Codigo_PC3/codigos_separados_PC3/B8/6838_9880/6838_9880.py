item = input("Insira o item desejado: ").upper()

i = 0
total = 0

while i < len(item):
	if item[i] == "D":
		total += 2.25
	elif item[i] == "S":
		total += 4.
	elif item[i] == "I":
		total += 6.9
	i += 1
print(round(total, 2))
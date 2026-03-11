it = input("coloque os itens dos produtos:").upper()

i = 0
total = 0
while i < len(it):
	if it[i] == "A":
		total += 16.75
	elif it[i] == "L":
		total += 4.60
	elif it[i] == "P":
		total += 2.85
	i += 1
print(round(total, 2))

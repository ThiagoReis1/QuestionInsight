compras = input().upper()
hort = 5.40
cer = 8.95
lat = 4.5
i = 0
total = 0

while i < len(compras):
	if compras[i] == "H":
		total += hort
	elif compras[i] == "C":
		total += cer
	elif compras[i] == "L":
		total += lat
	i += 1
print(round(total, 2))
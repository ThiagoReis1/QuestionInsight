hortifruti = 5.4
cereais = 8.95
laticinios = 4.5

compra = input().upper()
i = 0
total = 0
while i < len(compra):
	if compra[i] == "H":
		total = total + hortifruti
	elif compra[i] == "C":
		total = total + cereais
	elif compra[i] == "L":
		total = total + laticinios
	i = i + 1
print (round(total,2))
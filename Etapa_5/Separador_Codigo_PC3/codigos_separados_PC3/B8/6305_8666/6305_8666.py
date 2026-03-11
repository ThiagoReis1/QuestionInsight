produto = input()

total = 0
hortifruti_count = 0
laticinios_count = 0
enlatados_count = 0

for produto in produto:
	if produto == "H":
		total += 3.85
		hortifruti_count += 1
	elif produto == "L":
		total += 2.95
		laticinios_count += 1
	elif produto == "E":
		total += 7.90
		enlatados_count += 1
		
total_arrendondado = round(total , 2)

print(total_arrendondado , hortifruti_count , laticinios_count , enlatados_count)
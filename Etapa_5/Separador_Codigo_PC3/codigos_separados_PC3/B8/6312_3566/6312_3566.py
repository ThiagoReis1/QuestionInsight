entrada = input()
total = 0
biscoitos = 0
cereais = 0
enlatados = 0

for i in entrada:
	if i == 'B':
		total += 3.75
		biscoitos +=1
	elif i == 'C':
		total += 7.90
		cereais+=1
	elif i == 'E':
		total += 9.85
		enlatados+=1
		
print(round(total,2))
print(biscoitos)
print(cereais)
print(enlatados)
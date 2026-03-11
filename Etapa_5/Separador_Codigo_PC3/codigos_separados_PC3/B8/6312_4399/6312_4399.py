opcao = str(input())
biscoitos = 0
cereais = 0
enlatados = 0

for char in opcao:
	if char == 'B':
		biscoitos += 1
	elif char == 'C':
		cereais += 1
	elif char == 'E':
		enlatados += 1

total = biscoitos * 3.75 + cereais * 7.90 + enlatados * 9.85
print(total, biscoitos, cereais, enlatados)
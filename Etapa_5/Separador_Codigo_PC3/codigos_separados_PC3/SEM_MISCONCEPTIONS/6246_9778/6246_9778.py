resultados = input().upper()

quantidade = 0

while (resultados!= 'X'):
	if resultados == 'A':
		quantidade += 1
	resultados = input('').upper()
	
print(quantidade)
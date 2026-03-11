lista_de_compras = input("Digite os intes: ")
lista_de_compras = lista_de_compras.split(',')
contagem = [0, 0, 0, 0]

for item in lista_de_compras:
	if item == 'A':
			contagem[0] += 1
	elif item == 'B':
			contagem[1] += 1
	elif item == 'L':
			contagem[2] += 1
	elif item == 'H':
			contagem[3] += 1
			
print('[' + ' '.join(map(str, contagem)) + ']')
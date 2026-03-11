qtd_premiados = 0

entrada = int(input())

while entrada != -1:
	if entrada >= 35 and entrada <= 95:
		qtd_premiados += 1
	
	entrada = int(input())
	
print(qtd_premiados)
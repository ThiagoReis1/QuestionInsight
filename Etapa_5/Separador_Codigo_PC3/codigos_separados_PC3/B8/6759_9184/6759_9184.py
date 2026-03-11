distancia = int(input("Digite a distancia: "))

custo_inicial = 50.00

if distancia < 10:
	custo_total = custo_inicial + 5.50
	print(custo_total)
	
elif distancia == 10:
	custo_total = custo_inicial + 7.75
	print(custo_total)
	
elif distancia > 10:
	custo_total = custo_inicial + 10.00
	print(custo_total)
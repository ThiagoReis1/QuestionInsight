peso_pacote = float(input("Digite o valor do peso do pacote em quilogramas: "))

if (peso_pacote < 5):
	custo_total = 10 + 3.75
	print(round(custo_total, 2))
	
elif (peso_pacote == 5):
	custo_total = 10 + 4.75
	print(round(custo_total, 2))
	
else:
	custo_total = 10 + 5.75
	print(round(custo_total, 2))
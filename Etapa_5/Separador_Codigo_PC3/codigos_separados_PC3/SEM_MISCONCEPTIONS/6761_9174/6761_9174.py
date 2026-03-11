velocidade = int(input("velocidade: "))

if velocidade < 50:
	custo_total = 60 + 4.50
	print(custo_total)
	
elif velocidade == 50:
	custo_total = 60 + 5.50
	print(custo_total)

else:
	custo_total = 60 + 6.50
	print(custo_total)

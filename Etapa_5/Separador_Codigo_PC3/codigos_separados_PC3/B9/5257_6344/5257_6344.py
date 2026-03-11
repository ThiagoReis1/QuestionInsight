custo = float(input("Digite o custo: "))

if (custo <= 50):
	valor = custo + ((100/100) * custo)
	print (round(valor,2))
elif(custo > 50 and custo <= 100):
	valor = custo + ((50/100) * custo)
	print(round(valor, 2))
elif(custo > 100 and custo <= 500):
	valor = custo + ((40/100) * custo)
	print (round(valor,2))
else:
	valor = custo + ((30/100) * custo)
	print(round(valor,2))
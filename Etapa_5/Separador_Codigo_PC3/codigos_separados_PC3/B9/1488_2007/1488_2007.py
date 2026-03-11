minutos = float(input("digite minutos consumidos: "))
if (minutos >= 0):
	if (minutos < 100):
		valor_conta = minutos * 1.2 + 1
		print(round(valor_conta, 2))
	elif (minutos >= 100 and minutos < 200):
		valor_conta = minutos * 1.3 + 10
		print(round(valor_conta, 2))
	elif (minutos >= 200 and minutos < 300):
		valor_conta = minutos * 1.4 + 20
		print(round(valor_conta, 2))
	else:
		valor_conta = minutos * 1.5 + 25
		print(round(valor_conta, 2))
 

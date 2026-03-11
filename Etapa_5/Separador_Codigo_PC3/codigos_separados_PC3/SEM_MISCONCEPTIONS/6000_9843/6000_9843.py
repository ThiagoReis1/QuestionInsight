quant = int(input("Digite a quantidade de cachos de banana comprados: "))

if (quant <= 3):
	conta = quant * 5
	print(round(conta, 2))
	
else:
	conta = quant * 4.25
	print(round(conta, 2))
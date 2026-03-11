salario = float(input("Salario atual: "))

if(salario > 0):
	if (salario <= 800.00):
		aumento = 50/100
		aum = salario * aumento + (salario)
		print("Entrada: R$", salario)
		print("Novo salario: R$", round(aum,2))
	elif (salario <= 1000.00):
		aumento = 40/100
		aum = salario * aumento + (salario)
		print("Entrada: R$", salario)
		print("Novo salario: R$", round(aum,2))
	elif (salario <= 1200.00):
		aumento = 30/100
		aum = salario * aumento + (salario)
		print("Entrada: R$", salario)
		print("Novo salario: R$", round(aum,2))
	elif (salario <= 1400.00):
		aumento = 20/100
		aum = salario * aumento + (salario)
		print("Entrada: R$", salario)
		print("Novo salario: R$", round(aum,2))
	elif (salario <= 1600.00):
		aumento = 10/100
		aum = salario * aumento + (salario)
		print("Entrada: R$", salario)
		print("Novo salario: R$", round(aum,2))
	elif (salario > 1600.00):
		aumento = 5/100
		aum = salario * aumento + (salario)
		print("Entrada: R$", salario)
		print("Novo salario: R$", round(aum,2))
else:
	print("Entrada: R$", salario)
	print("Dado invalido")
atual = float(input("Salario atual: "))

if(atual >= 0):
	if(atual <= 800):
		aumento = atual * (50/100)
		print("Novo salario: R$ ", round(aumento + atual,2))

	elif(atual > 800 and atual <= 1000):
		aumento = atual * (40/100)
		print("Novo salario: R$ ", round(aumento + atual,2))

	elif(atual > 1000 and atual <= 1200):
		aumento = atual * (30/100)
		print("Novo salario: R$ ", round(aumento + atual,2))

	elif(atual > 1200 and atual <= 1400):
		aumento = atual * (20/100)
		print("Novo salario: R$ ", round(aumento + atual,2))

	elif(atual > 1400 and atual <= 1600):
		aumento = atual * (10/100)
		print("Novo salario: R$ ", round(aumento + atual,2))

	elif(atual > 1600):
		aumento = atual * (5/100)
		print("Novo salario: R$ ", round(aumento + atual,2))
	
else:
	print("Dado invalido")
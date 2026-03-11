salario = float(input(""))

if(salario < 0):
	print("Dado invalido")
elif(salario <= 800):
	aumento = salario + (salario * 0.5)
	print("Novo salario: R$", round(aumento, 2))
elif((salario > 800) and (salario <= 1000)):
	aumento = salario + (salario * 0.4)
	print("Novo salario: R$", round(aumento, 2))
elif((salario > 1000) and (salario <= 1200)):
	aumento = salario + (salario * 0.3)
	print("Novo salario: R$", round(aumento, 2))
elif((salario > 1200) and (salario <= 1400)):
	aumento = salario + (salario * 0.2)
	print("Novo salario: R$", round(aumento, 2))
elif((salario < 1400) and (salario <= 1600)):
	aumento = salario + (salario * 0.1)
	print("Novo salario: R$", round(aumento, 2))
elif((salario > 1600)):
	aumento = salario + (salario * 0.05)
	print("Novo salario: R$", round(aumento, 2))
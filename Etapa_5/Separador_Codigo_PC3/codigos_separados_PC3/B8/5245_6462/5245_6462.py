salario = float(input("salario: "))
if salario > 0:
	if salario <=800:
		salario2 = salario*1.5
	elif 800 < salario <= 1000:
	   salario2 = salario*1.4
	elif 1000 < salario <= 1200:
	   salario2 = salario* 1.3
	elif  1200 < salario <= 1400:
		salario2 = salario* 1.2
	elif 1400 < salario <= 1600:
		salario2= salario* 1.1
	elif salario> 1600:
		salario2 = salario*1.05
	
	print("Entrada: R$", salario)
	print("Novo salario: R$", round(salario2 , 2))
else: 
	print("Entrada: R$", round(salario , 2))
	print("Dado invalido")
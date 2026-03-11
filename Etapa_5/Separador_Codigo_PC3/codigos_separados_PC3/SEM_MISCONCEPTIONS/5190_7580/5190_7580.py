classe = int(input('101 ou 102'))
salario = float(input('salario: '))
if classe == 101:
	print(round(salario+(salario*0.1),2))
	print('Aumento de 10 por cento')
else:
	print(round(salario+(salario*0.3),2))
	print('Aumento de 30 por cento')
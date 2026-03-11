# Leitura das informações

salario = float(input("Qual o salario atual?"))

# Cálculos
print("Entrada: R$", salario)
if salario > 0:
	if salario <= 800:
		salario_1 = salario + salario*0.50
		print("Novo salario: R$", round(salario_1,2))
	elif salario > 800 and salario<= 1000:
		salario_2 = salario + salario*0.40
		print("Novo salario: R$", round(salario_2,2))
	elif salario > 1000 and salario <= 1200:
		salario_3 = salario + salario*0.30
		print("Novo salario: R$", round(salario_3,2))
	elif salario > 1200 and salario <= 1400:
		salario_4 = salario + salario*.20
		print("Novo salario: R$", round(salario_4,2))
	elif salario > 1400 and salario <= 1600:
		salario_5 = salario + salario*0.10
		print("Novo salario: R$", round(salario_5,2))
	elif salario > 1600:
		salario_6 = salario + salario*0.05
		print("Novo salario: R$", round(salario_6,2))
else:
	print("Dado invalido")
salario = float(input("Informe o salario: "))
print("Entrada: R$" ,salario)

if (salario <= 800):
	salario_a = salario+(salario*50/100)
	salario_n = round(salario_a, 5)
	print("Novo salario: R$" ,salario_n)
elif (salario >= 800) and (salario <= 1000):
	salario_a=  salario+(salario*40/100)
	salario_n = round(salario_a, 5)
	print("Novo salario: R$" ,salario_n)
elif (salario >= 1000) and (salario <= 1200):
	salario_a = salario+(salario*30/100)
	salario_n = round(salario_a, 5)
	print("Novo salario: R$" ,salario_n)
elif (salario >= 1200) and (salario <= 1400):
	salario_a = salario + (salario*20/100)
	salario_n = round(salario_a, 5)
	print("Novo salario: R$" ,salario_n)
elif (salario >= 1400) and (salario <= 1600):
	salario_a = salario+(salario*10/100)
	salario_n = round(salario_a, 5)
	print("Novo salario: R$" ,salario_n)
elif (salario >= 1600):
	salario_a = salario+(salario*5/100)
	salario_n = round(salario_a, 5)
	print("Novo salario: R$" ,salario_n)
else:
	print("Dado invalido")
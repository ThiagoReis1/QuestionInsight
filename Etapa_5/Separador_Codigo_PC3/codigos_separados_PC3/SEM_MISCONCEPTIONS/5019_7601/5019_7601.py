salario = float(input("Insira o salario atual: "))

if (salario > 0) and (salario < 1212):
	x = (salario * 0.12) + salario
	print(round(x,2))
elif (salario > 0) and (salario >= 1212) and (salario <= 5000):
	x = (salario * 0.08) + salario
	print(round(x,2))
else:
	x = (salario * 0.03) + salario
	print(round(x,2))
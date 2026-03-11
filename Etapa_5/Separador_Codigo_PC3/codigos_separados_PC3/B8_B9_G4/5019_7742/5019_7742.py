salario = float(input("Informe o salario: "))

a = salario * (12/100) + salario
b = salario * (8/100) + salario
c = salario * (3/100) + salario

if (salario < 1212.00):
	print (round(a, 2))
elif (salario >= 1212.00) and (salario <= 5000.00):
	print (round (b, 2))
elif (salario > 5000.00):
	print (round (c, 2))
	
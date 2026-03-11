salario = float(input("Informe o salario atual: "))

a = salario * (50/100) + salario
b = salario * (40/100) + salario
c = salario * (30/100) + salario
d = salario * (20/100) + salario
e = salario * (10/100) + salario
f = salario * (5/100) + salario

if (salario >= 0) and (salario <= 800.00):
	print ("Novo salario: R$ ", round( a, 2))
elif (salario > 800.00) and (salario <= 1000.00):
	print ("Novo salario: R$ ", round( b, 2))
elif (salario > 1000.00) and (salario <= 1200.00):
	print ("Novo salario: R$ ", round (c, 2))
elif (salario > 1200.00) and (salario <= 1400.00):
	print ("Novo salario: R$ ",round (d, 2))
elif (salario > 1400.00) and (salario <= 1600.00):
	print ("Novo salario: R$ ",round (e, 2))
elif (salario > 1600):
	print ("Novo salario: R$ ",round (f, 2))
else:
	print ("Dado invalido")
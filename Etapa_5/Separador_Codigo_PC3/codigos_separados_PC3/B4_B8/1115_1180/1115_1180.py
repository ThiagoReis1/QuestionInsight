cargo = int(input(" digite o codigo do cargo: "))
salario = float(input(" qual o seu salario: "))
if (salario<=0):
	print("Entrada: ","R$", salario, " e ", cargo)
	print("Dado invalido")
elif (101 > cargo > 104):
	print("Entrada: ","R$", salario, " e ", cargo)
	print("Dado invalido") 
elif (101):
	n_salario = float(round((salario * 0.8/100) + salario), 2)
	print("Entrada: ","R$", salario, " e ", cargo)
	print(" R$ ", n_salario)
elif (102):
	n_salario = float(round((salario * 0.65/100) + salario), 2)
	print("Entrada: ","R$", salario, " e ", cargo)
	print(" R$ ", n_salario)
elif (103):
	n_salario = float(round((salario * 0.60/100) + salario), 2)
	print("Entrada: ","R$", salario, " e ", cargo)
	print(" R$ ", n_salario)
elif (104):
	n_salario = float(round((salario * 0.55/100) + salario), 2)
	print("Entrada: ","R$", salario, " e ", cargo)
	print(" R$ ", n_salario)
	
    
salario = float(input(" qual o seu salario:"))
cargo = int(input(" digite o codigo do seu cargo:"))

if (salario <= 0 or 101 > cargo > 104):
	print("Entradas: ","R$", salario, " e ", "codigo", cargo)
	print("Dado invalido")
   
elif (cargo):
	n_salario = float(round((salario * 0.80/100) + salario, 2))
	print("Entradas: ","R$", salario, " e ","codigo", cargo)
	print("Novo salario: ","R$", n_salario)
elif (cargo):
	n_salario = float(round((salario * 0.65/100) + salario, 2))
	print("Entradas: ","R$", salario, " e ", "codigo", cargo)
	print("Novo salario: ", "R$", n_salario)
	
elif (cargo):
		n_salario = float(round((salario * 0.60/100) + salario, 2))
		print("Entradas: ","R$", salario, " e ","codigo ", cargo)
		print("Novo salario:", "R$ ", n_salario)
	
elif (cargo):
		n_salario = float(round((salario * 0.55/100) + salario, 2))
		print("Entradas: ","R$", salario, " e ", cargo)
		print("Novo salario", "R$ ", n_salario)
	
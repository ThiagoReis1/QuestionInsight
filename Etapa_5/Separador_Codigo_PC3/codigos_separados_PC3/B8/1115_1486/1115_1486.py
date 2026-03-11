salario = float(input("Salario atual: "))
codigo = int(input("Codigo do cargo: "))

if(salario < 0):
	if(codigo != 101 or codigo != 102 or codigo !=103 or codigo !=104):
		print("Entradas: R$", salario, "e codigo", codigo)
		print("Dados invalidos")
elif(codigo == 101):
	r = salario + (salario * (0.8/100))
	print("Entradas: R$", salario, "e codigo", codigo)			 
	print("Novo salario: R$", round(r, 2))
elif(codigo == 102):
	r = salario + (salario * (0.65/100))
	print("Entradas: R$", salario, "e codigo", codigo)			 
	print("Novo salario: R$", round(r, 2))
elif(codigo == 103):
	r = salario + (salario * (0.60/100))
	print("Entradas: R$", salario, "e codigo", codigo)			 
	print("Novo salario: R$", round(r, 2))
elif(codigo == 104):
	r = salario + (salario * (0.55/100))
	print("Entradas: R$", salario, "e codigo", codigo)			 
	print("Novo salario: R$", round(r, 2))



salario = float(input("Digite: "))
codigo = int(input("Digite: "))

print("Entradas: R$", salario, "e codigo", codigo)

if ((codigo != 101) and (codigo != 102) and (codigo != 103) and (codigo != 104)) or (salario < 0):
	print("Dados invalidos")
else:
	if (codigo == 101):
		r1= salario + (salario * (0.80 / 100))
		print("Novo salario: R$", round(r1, 2))
	elif (codigo == 102):
		r2 = salario + (salario * (0.65 / 100))
		print("Novo salario: R$", round(r2, 2))
	elif (codigo == 103):
		r3 = salario + (salario * (0.60 / 100))
		print( "Novo salario: R$", round(r3, 2))
	elif (codigo == 104):
		r4 = (salario + (salario * (0.55 / 100)))
		print ("Novo salario: R$", round(r4, 2))
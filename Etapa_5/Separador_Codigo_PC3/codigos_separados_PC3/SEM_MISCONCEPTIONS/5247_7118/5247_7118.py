salario = float(input(""))
codigo = int(input(""))

print("Entradas: R$", salario, "e", "codigo", codigo)
s = "Novo salario: R$"
if salario > 0:
	if codigo == 101:
		reajuste = salario * 0.0080
		a = salario + reajuste
		print(s,(round(a, 2)))
		
	elif codigo == 102:
		reajuste = salario * 0.0065
		a = salario + reajuste
		print(s,(round(a,2)))
		
	elif codigo == 103:
		reajuste = salario * 0.0060
		a = salario + reajuste
		print(s,(round(a,2)))
		
	elif codigo == 104:
		reajuste = salario * 0.0055
		a = salario + reajuste
		print(s,(round(a,2)))
		
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")
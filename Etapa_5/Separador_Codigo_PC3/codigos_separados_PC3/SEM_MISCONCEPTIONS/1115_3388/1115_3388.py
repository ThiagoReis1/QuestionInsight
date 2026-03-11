salario = float(input())
codigo = int(input())
if salario > 0 and codigo == 101:
	n_salario = salario + (salario * 0.008)
	print("Entradas: R$",round(salario,2),"codigo",codigo)
	print("Novo salario: R$", round(n_salario,2))
elif salario > 0 and codigo == 102:
	n_salario = salario + (salario * 0.0065)
	print("Entradas: R$",round(salario,2),"codigo",codigo)
	print("Novo salario: R$", round(n_salario,2))
elif salario > 0 and codigo == 103:
	n_salario = salario + (salario * 0.006)
	print("Entradas: R$",round(salario,2),"codigo",codigo)
	print("Novo salario: R$", round(n_salario,2))	
elif salario > 0 and codigo == 104:
	n_salario = salario + (salario * 0.0055)
	print("Entradas: R$",round(salario,2),"codigo",codigo)
	print("Novo salario: R$", round(n_salario,2))
else:
	print("Entradas: R$",round(salario,2),"codigo",codigo)
	print("Dados invalidos")
	
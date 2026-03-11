salario=float(input("digite seu salario= "))
codigo=float(input("digite seu codigo: "))

if salario >= 0:
		if codigo == 101:
			total= salario + (salario * 0.80)
			print(total)
		elif codigo == 102:
			total=salario + (salario * 0.65)
			print(total)
		elif codigo == 103:
			total= salario + (salario * 0.65)
			print(total)
		elif codigo == 104:
			total= salario + (salario * 0.55)
			print(total)
		else:
			print("Novo salario: R$",total)
else:
	print("Dados invalidos")


#Universidade Federal do Amazonas
#Thiago Tuma Camilo - 21600549

salario = float(input("Valor do salário:"))
codigo = int(input("Digite o código:"))

if (salario < 0) or (codigo < 101) or (codigo > 104):
	print("Entradas: R$", round(salario, 2), "e codigo",codigo)
	print ("Dados invalidos")
elif (codigo == 101):
		salarioadm = salario * 1.0080
		print ("Entradas: R$", round(salario, 2), "e codigo",codigo)
		print ("Novo salario: R$", round(salarioadm, 2))
elif (codigo == 102):
		salarioeng = salario * 1.0065
		print("Entradas: R$", round(salario, 2), "e codigo",codigo)
		print("Novo salario: R$", round(salarioeng, 2))
elif (codigo == 103):
		salariomed = salario * 1.0060
		print("Entradas: R$", round(salario, 2), "e codigo",codigo)
		print("Novo salario: R$", round(salariomed, 2))
elif (codigo == 104):
		outros = salario * 1.0055
		print("Entradas: R$", round(salario, 2), "e codigo",codigo)
		print("Novo salario: R$", round(outros, 2))
else:
	print("Entradas: R$", round(salario, 2), "e codigo",codigo)
	print("Dados invalidos")
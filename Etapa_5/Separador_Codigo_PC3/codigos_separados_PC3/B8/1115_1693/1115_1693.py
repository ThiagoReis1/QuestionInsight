salario_atual = float(input("Qual o salario atual?"))
codigo = input("Qual o codigo correspondente?")
print("Entradas: R$", salario_atual,"e codigo",codigo)
if(salario_atual>0):
	if(codigo == "101" or codigo == "102" or codigo == "103" or codigo == "104"):
		if(codigo == "101"):
			reajuste = salario_atual * 0.008
			novo_salario = reajuste + salario_atual
			print("Novo salario: R$", (round(novo_salario, 2)))
		elif(codigo == "102"):
			reajuste = salario_atual * 0.0065
			novo_salario = reajuste + salario_atual
			print("Novo salario: R$", (round(novo_salario, 2)))
		elif(codigo == "103"):
			reajuste = salario_atual * 0.006
			novo_salario = reajuste + salario_atual
			print("Novo salario: R$", (round(novo_salario, 2)))
		elif(codigo == "104"):
			reajuste = salario_atual * 0.0055
			novo_salario = reajuste + salario_atual
			print("Novo salario: R$", (round(novo_salario, 2)))
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")

		
	

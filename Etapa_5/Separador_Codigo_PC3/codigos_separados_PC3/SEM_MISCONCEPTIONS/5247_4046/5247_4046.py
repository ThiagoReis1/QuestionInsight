salario_atual = float(input("Informe o salario atual: "))
codigo = int(input("Informe o codigo correspondente ao cargo do funcionario: "))

print("Entradas:", "R$", salario_atual, "e", "codigo", codigo)

if(salario_atual > 0):
	
	if(codigo >= 101 and codigo <= 104):
		
		if(codigo == 101):
			novo_salario = (salario_atual * (0.8 / 100)) + salario_atual
			print("Novo salario:","R$", round(novo_salario, 2))
		
		elif(codigo == 102):
			novo_salario = (salario_atual * (0.65 / 100)) + salario_atual
			print("Novo salario:","R$", round(novo_salario, 2))
		
		elif(codigo == 103):
			novo_salario = (salario_atual * (0.6 / 100)) + salario_atual
			print("Novo salario:", "R$", round(novo_salario, 2))
		
		else:
			novo_salario = (salario_atual * (0.55 / 100)) + salario_atual
			print("Novo salario:","R$", round(novo_salario, 2))
	else:
		print("Dados invalidos")

else:
	print("Dados invalidos")
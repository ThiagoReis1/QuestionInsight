salario_atual = (float(input("salario: " )))
print("Entrada: R$", salario_atual)
if(salario_atual > 0):
	if(salario_atual <= 800):
		novo_salario = salario_atual + (salario_atual*0.5)
		print("Novo salario: R$", round(novo_salario, 2))
	elif(salario_atual > 800 and salario_atual<= 1000):
		novo_salario = salario_atual + (salario_atual*0.4)
		print("Novo salario: R$", round(novo_salario, 2))
	elif(salario_atual > 1000 and salario_atual<= 1200):
		novo_salario = salario_atual + (salario_atual*0.3)
		print("Novo salario: R$", round(novo_salario, 2))
	elif(salario_atual > 1200 and salario_atual<= 1400):
		novo_salario = salario_atual + (salario_atual*0.2)
		print("Novo salario: R$", round(novo_salario, 2))
	elif(salario_atual > 1400 and salario_atual<= 1600):
		novo_salario = salario_atual + (salario_atual*0.1)
		print("Novo salario: R$", round(novo_salario, 2))
	elif(salario_atual > 1600):
		novo_salario = salario_atual + (salario_atual*0.05)
		print("Novo salario: R$", round(novo_salario, 2))
else:
	print("Dado invalido")
	
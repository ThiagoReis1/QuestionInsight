codigo = int(input("informe o codigo do cargo: 101 ou 102 "))
salario_atual = float(input("informe o valor do salario atual: "))

if codigo == 101:
	aumento = salario_atual*0.10
	salario2 = aumento+salario_atual
	print(round(salario2,2))
	print("Aumento de 10 por cento")
else:
	aumento = salario_atual*0.30
	salario2 = aumento+salario_atual
	print(round(salario2,2))
	print("Aumento de 30 por cento")
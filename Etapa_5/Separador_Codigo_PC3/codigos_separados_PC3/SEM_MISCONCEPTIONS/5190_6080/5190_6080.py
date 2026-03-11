codigo = input("codigo: ")
salario = float(input("digite: "))

if (codigo == "101"):
	aumento= salario + salario*10/100
	print(round(aumento, 2))
	print("Aumento de 10 por cento")
else:
	aumento = salario + salario * 30/100
	print(round(aumento, 2))
	print("Aumento de 30 por cento")
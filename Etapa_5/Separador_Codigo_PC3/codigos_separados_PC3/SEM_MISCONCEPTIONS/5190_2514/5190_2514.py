codigo = int(input(" "))
salario = float(input(" "))
if (codigo == 101):
	novos = salario + (salario * 0.10)
	print(round(novos,2))
	print("Aumento de 10 por cento")
else:
	novos = salario + (salario * 0.30)
	print(round(novos,2))
	print("Aumento de 30 por cento")
cargo = int(input())
salario = float(input())
if(cargo == 101):
	print(round(salario*1.10,2))
	print("Aumento de 10 por cento")
else:
	print(round(salario*1.30,2))
	print("Aumento de 30 por cento")
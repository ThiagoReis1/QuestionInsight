cargo = int(input("Digite o codigo: "))
salario = float(input("Digite o salario atual: "))
if(cargo == 101):
	novo = salario+(salario*0.10)
	print(round(novo,2))
	print("Aumento de 10 por cento")
else:
	novo = salario+(salario*0.30)
	print(round(novo,2))
	print("Aumento de 30 por cento")
	

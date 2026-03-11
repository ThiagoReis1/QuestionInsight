v = input("Qual o codigo do cargo: 101 ou 102? ")
n = float(input("Digite o salario do ninja: "))

if (v == "101"):
	ninja = n*10/100+n
	print(round(ninja, 2))
	print("Aumento de 10 por cento")
else:
	ninja = n*30/100+n
	print(round(ninja, 2))
	print("Aumento de 30 por cento")
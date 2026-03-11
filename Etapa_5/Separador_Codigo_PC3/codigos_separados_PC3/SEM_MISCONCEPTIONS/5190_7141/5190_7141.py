v = input("qual o codigo do cargo: 101 ou 102? ")
n = float(input("qual o salario do ninja atual?: "))

if (v == "101"):
	ninja = n*10/100+n
	print(round(ninja, 2))
	print("Aumento de 10 por cento")
else:
	ninja = n*30/100+n
	print(round(ninja, 2))
	print("Aumento de 30 por cento")
	

	
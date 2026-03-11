entrada = input("Qual o pedido?: ")
quantidade = int(input("Qual a quantidade?: "))

valor = 25.90

if (entrada.upper() == "B"):
	soma = quantidade * valor
	soma2 = soma * 10/100
	desconto = soma - soma2
	total = desconto
	print(round(desconto, 2))
	
else:
	total = quantidade * valor
	print(round(total, 2))
	
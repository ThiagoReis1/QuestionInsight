# faça seu código aqui!
manhas = int(input(""))
valor = 20.00 * manhas
if manhas >= 4:
	desconto = (20.00 * manhas) * 15/100
	total = valor - desconto
	print(round(total, 2))
	
else:
	print(round(valor, 2))
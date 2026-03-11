np = int(input("Digite o numero de pizzas encomendadas: "))

#preco basico = 5 (entrega) + taxa de pizzas encomendadas

if (np<3):
	total = (np * 5) + 3.
	print(round(total,2))
	
elif (np==3):
	total = (np*5) + 3.25
	print(round(total,2))
	
else:
	total = (np*5) + 4.5
	print(round(total,2))
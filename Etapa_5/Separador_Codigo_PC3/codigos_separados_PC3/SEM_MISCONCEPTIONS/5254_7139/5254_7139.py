# Entrada

preco = float(input("preco do produto:"))
cod = int(input("Codigo da regiao de entrega:"))

# Condicao

if cod == 1:
	total = (preco - preco * 40/100) + preco * (10/100)
	print(round(total,2))
elif cod == 2:
	total = (preco - preco * 40/100) + preco * (8/100)
	print(round(total,2))
elif cod == 3:
	total = (preco - preco * 40/100) + preco * 0
	print(round(total,2))
else:
	total = (preco - preco * 40/100) + preco * (2/100)
	print(round(total,2))
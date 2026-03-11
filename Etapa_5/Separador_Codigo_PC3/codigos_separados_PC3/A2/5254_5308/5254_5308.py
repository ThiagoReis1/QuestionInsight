preco = float(input("preco: "))

codigo = int(input("codigo: "))

porc = preco * 40/100

frete_1 = preco * 10/100

frete_2 = preco * 8/100

frete_4 = preco * 2/100

parentese = preco - porc 


if (codigo == 1):
	venda = parentese +  frete_1
	print(round(venda, 2))
	
elif (codigo == 2):
	venda = parentese + frete_2
	print(round(venda, 2))
	
elif (codigo == 3):
	print(round(parentese, 2))
	
elif (codigo == 4):
	venda = parentese + frete_4
	print(round(venda, 2))
	
else:
	preco=preco
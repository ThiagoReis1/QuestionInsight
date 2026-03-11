preco = float(input("preco: "))
cod = int(input("cod: "))

descontoBF = 40/100

if cod == 1:
	valor_da_venda = (preco - (preco * descontoBF) + preco * (10/100))
	print(round(valor_da_venda, 2))
elif cod == 2:
	valor_da_venda = (preco - (preco * descontoBF) + preco * (8/100))
	print(round(valor_da_venda, 2))
elif cod == 3:
	valor_da_venda = (preco - (preco * descontoBF) + preco * (0/100))
	print(round(valor_da_venda, 2))
elif cod == 4:
	valor_da_venda  = (preco - (preco * descontoBF) + preco * (2/100))
	print(round(valor_da_venda, 2))
	
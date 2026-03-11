preco = float(input("digite o preco do produto: "))
codigo = int(input("digite o codigo: "))



if (codigo == 1):
	frete = preco - (preco * 10 / 100)
	venda = (preco - preco * 0.4) + preco * (frete / 100)
	print(round(venda, 2))
elif (codigo == 2):
	frete = preco - (preco * 8 / 100)
	venda = (preco - preco * 0.4) + preco * (frete / 100)
	print(round(venda, 2))
elif (codigo == 3):
	frete = 0
	venda = (preco - preco * 0.4) + preco * (frete / 100)
	print(round(venda, 2))
elif (codigo == 4):
	frete = preco - (preco * 2 / 100)
	venda = (preco - preco * 0.4) + preco * (frete / 100)
	print(round(venda, 2))

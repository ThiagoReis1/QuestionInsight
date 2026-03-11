pedido = str(input("digite L ou P:"))
qtdlp = int(input("digite a quantidade de lanches ou pizzas:"))
qtdr = int(input("digite a quantidade de refrigerantes:"))

L1 = 6.00
P = 4.50
R = 3.00

if pedido == "L":
	print((qtdlp * 6) + (qtdr * 3))
	
else:
	print((qtdlp * 4.50) + (qtdr * 3))
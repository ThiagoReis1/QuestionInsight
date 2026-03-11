pedido = input("pedido: ")
quantidade = float(input("quantidade: "))
cappuccinosq = float(input("quantidade: "))
B = 5
S = 4
Cappuccinos = 7.50
valorB = B*quantidade+Cappuccinos*cappuccinosq
valorS = S*quantidade+Cappuccinos*cappuccinosq

if (pedido=="S"):
	print(valorS)
if (pedido=="B"):
	print(valorB)
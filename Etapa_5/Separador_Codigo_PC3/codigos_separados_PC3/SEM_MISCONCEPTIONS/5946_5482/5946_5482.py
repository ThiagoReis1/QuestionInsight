pedido = input("escreva o pedido L/P: ").upper()
quantc = float(input("escreva a quantidade de comida: "))
quantb = float(input("escreva a quantidade de refrigerante: "))
if pedido == "L":
	pf = quantc*6 + quantb*3
	print(pf)
else:
	pf = quantc*4.5 + quantb*3
	print(pf)
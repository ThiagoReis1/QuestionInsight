Pl = input("Digite \"L\" se for lanche ou \"P\" se for pizza: ")
Lp = int(input("Digite a quantidade de lanches ou pizzas: "))
Qr = int(input("Digite a quantidade de refrigerantes: "))

if Pl == "L":
	J = Lp*6 + Qr*3
	print(round(J,2))
else:
	N = Lp*4.5 + Qr*3
	print(round(N,2))




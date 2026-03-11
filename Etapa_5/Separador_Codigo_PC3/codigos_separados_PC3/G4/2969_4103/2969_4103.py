a = int(input("Quantidade de jogos(1/2): "))
b = float(input("Preco do jogo 1: "))


if (a) == 2:
	c = float(input("Preco do jogo 2: "))
	print(round((b + (c - (c*0.25))), 2))
else:
	print(b)
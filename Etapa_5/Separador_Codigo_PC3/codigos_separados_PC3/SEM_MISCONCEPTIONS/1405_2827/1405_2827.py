ataque = input("Nome do Ataque (grito/toque):")
d1 = int(input("Valor sorteado no dado 1: "))
d2 = int(input("Valor sorteado no dado 2: "))

if ( ataque == "grito"):
	print(6 + d1 + d2)
else:
	print((d1 + d2) ** 2)
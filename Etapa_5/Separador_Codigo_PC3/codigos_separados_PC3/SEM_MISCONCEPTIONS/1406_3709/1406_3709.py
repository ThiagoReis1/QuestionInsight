t_dano = input("tipo  de dano: ")
valor = int(input("valor de N: "))
n = int(input("n: "))
if (t_dano.lower() == "cauda"):
	print(valor * n)
else:
	print((valor * n) * 2)
Va = float(input("valor total: "))
Cod = input("opcao/qtsV: ")

if Cod == "D":
	valorF = Va - 0.13 * Va
	print(round(valorF, 2))
elif Cod == "p":
	valorF = Va - 0.13 * Va
	print(round(valorF, 2))
else:
	p = int(input("parcela: "))
	if p == 1:
		valorF = Va
		print(round(valorF, 2))
	else:
		valorF = Va + 0.08 * Va
		print(round(valorF, 2))
	
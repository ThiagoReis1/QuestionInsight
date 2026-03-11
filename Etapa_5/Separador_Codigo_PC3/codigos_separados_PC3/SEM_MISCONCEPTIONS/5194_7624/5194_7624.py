classe = input("classificacao da missao: ")
valor = float(input("valor pago pela missao: "))

valor_B =  valor - (valor * 15 / 100)
valor_A = valor - (valor * 22 / 100)


if (classe=="B"):
	print("Classe: Chunin")
	print(round(valor_B, 2))
else:
	print("Classe: Jounin")
	print(round(valor_A, 2))
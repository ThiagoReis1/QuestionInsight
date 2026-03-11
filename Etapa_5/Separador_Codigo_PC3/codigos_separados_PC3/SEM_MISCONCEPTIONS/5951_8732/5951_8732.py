lanche = input("Digite (T/S): ")
quantidade = int(input("Quantidade de tapioca ou salgados:"))
acai = int(input("Quantidade de acai:"))
if (lanche.upper() == "T"):
	valor = quantidade * 4.50 + acai * 12
	print(valor)
else:
	valor = quantidade * 5 + acai * 12
	print(valor)
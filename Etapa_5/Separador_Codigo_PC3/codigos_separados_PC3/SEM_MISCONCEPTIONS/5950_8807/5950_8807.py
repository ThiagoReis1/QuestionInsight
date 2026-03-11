comida = input("Qual a comida (T/P)? ")
quantidade = int(input("Qntd: "))
quantidadec = int(input("Qntd de cap: "))

if comida == "T":
	total1 = quantidade * 6 + quantidadec * 4.5
	print(round(total1, 2))
else:
	total2 = quantidade * 5 + quantidadec * 4.5
	print(round(total2, 2))
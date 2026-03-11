valor_um=float(input("nota 1: "))
valor_dois=float(input("nota 2: "))
valor_tres=float(input("nota 3: "))
valor_quatro=float(input("nota 4: "))
total=(valor_um + valor_dois + valor_tres + valor_quatro) / 4

if (total >= 7):

	print(round(total,2))
	print("Aprovado")
else:
	print(round(total,2))
	print("Reprovado")

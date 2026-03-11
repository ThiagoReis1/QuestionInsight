renda = float(input(""))
prestacao = float(input(""))


if renda < prestacao:
	prestacao = 0.35 * renda
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")

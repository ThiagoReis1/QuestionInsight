renda = float(input("Renda: "))
prest = float(input("valor prestacao: "))


if (prest > renda*35/100):
	print("Emprestimo nao aprovado")
	
else:
	prest <= renda*35/100
	print("Emprestimo aprovado")
renda = int(input("valor da renda: "))
prest = int(input("valor da prestacao: "))

porc = renda * (25/100)
if (prest > porc):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
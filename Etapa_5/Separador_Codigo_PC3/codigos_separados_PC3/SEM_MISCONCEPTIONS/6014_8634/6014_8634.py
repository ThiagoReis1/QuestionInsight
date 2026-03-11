renda = float(input("Valor da renda da Maria Chiquinha:"))
prest = float(input("Valor da prestacao: "))

if prest > renda*0.35:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
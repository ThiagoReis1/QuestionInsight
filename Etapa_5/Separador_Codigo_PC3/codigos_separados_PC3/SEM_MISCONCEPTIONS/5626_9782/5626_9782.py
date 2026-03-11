renda = int(input("Valor da renda: "))
prest = int(input("Valor da prestacao: "))

if prest > renda*25/100:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
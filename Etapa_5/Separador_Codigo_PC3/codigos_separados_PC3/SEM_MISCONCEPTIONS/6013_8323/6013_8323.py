renda = float(input("Valor da renda de Seu Saba: "))
prest = float(input("Valor da prestacao do emprestimo: "))

if (prest > renda * 0.15):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
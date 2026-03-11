renda = float(input("Valor da renda: "))
prestacao = float(input("Valor da prestacao: "))

if prestacao > renda*0.25:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
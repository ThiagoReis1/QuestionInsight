renda = float(input("valor da renda: "))
prestacao = float(input("valor da prestacao: "))

conta = renda*0.15


if prestacao > conta:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")
ValorRenda = int(input("Informe o valor da renda: "))
ValorPrestacao = int(input("Informe o valor da prestacao: "))


if ValorPrestacao > ValorRenda*0.25:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")
	

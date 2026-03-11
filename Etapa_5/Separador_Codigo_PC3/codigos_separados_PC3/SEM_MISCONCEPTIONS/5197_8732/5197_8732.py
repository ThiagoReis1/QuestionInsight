renda = float(input("valor da renda: "))
prestacao = float(input("Valor da prestacao: "))
if (prestacao > renda * (20/100)):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
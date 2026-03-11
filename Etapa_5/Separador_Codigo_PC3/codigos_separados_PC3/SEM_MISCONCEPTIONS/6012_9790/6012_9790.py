renda = float(input("valor da renda: "))
prestacao = float(input("valor da prestacao: "))

if prestacao > (renda * (25/100)):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
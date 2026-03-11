renda = float(input("Digite o valor da renda: "))
prestacao = float(input("Digite o valor da prestacao: "))

if prestacao > renda * 0.35:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")

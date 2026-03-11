renda = float(input("digite o valor da renda de seu saba: "))
prestacao = float(input("digite o valor da prestacao: "))
if prestacao >= renda * 0.15:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
renda = float(input("digite o valor da renda: "))
prestacao = float(input("digite o valor da prestacao: "))
avaliacao = (renda*(25/100))
if prestacao >= avaliacao:
	mensagem1 = "Emprestimo nao aprovado"
	print(mensagem1)
else:
	mensagem2 = "Emprestimo aprovado"
	print(mensagem2)
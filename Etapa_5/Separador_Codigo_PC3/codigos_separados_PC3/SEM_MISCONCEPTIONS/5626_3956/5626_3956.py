valor_renda = float(input())
prestacao = float(input())

if prestacao>(0.25*valor_renda):
	print('Emprestimo nao aprovado')
else:
	print('Emprestimo aprovado')
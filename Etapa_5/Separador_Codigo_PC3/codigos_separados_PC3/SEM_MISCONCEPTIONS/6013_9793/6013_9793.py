renda = float(input('renda: '))
prestacao = float(input('prestacao: '))

limite = 0.15 * renda

if prestacao > limite:
	print('Emprestimo nao aprovado')
else:
	print('Emprestimo aprovado')
renda = int(input())
prestacao = int(input())

if(prestacao > 0.25*renda):
	print('Emprestimo nao aprovado')
else:
	print('Emprestimo aprovado')
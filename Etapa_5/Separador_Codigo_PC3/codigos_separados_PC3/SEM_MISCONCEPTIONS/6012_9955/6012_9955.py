valor_da_renda=float(input())
valor_da_prestacao=float(input())
porcentagem=(valor_da_renda* 0.25)
if valor_da_prestacao > porcentagem:
   print('Emprestimo nao aprovado')
else:
	print('Emprestimo aprovado')
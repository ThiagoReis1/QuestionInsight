renda = float(input('o valor da renda: '))
pres = float(input(' o valor da prestacao: '))
x = renda * 0.35

if pres <= x:
	print('Emprestimo aprovado')
else:
	print('Emprestimo nao aprovado')

renda = float(input('valor da renda: '))
pres = float(input('valor da pres: '))

if pres > (renda * (25/100)):
	print ('Emprestimo nao aprovado')
else:
	print ('Emprestimo aprovado')
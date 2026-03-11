renda = float(input('renda da clot?'))
preta = float(input('presta:'))

a = (25/100 * renda)

if preta > a :
	print('Emprestimo nao aprovado')
	
else :
	print('Emprestimo aprovado')
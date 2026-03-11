r = int(input('valor a renda: '))
p = int(input('valor da prestaco: '))

if p >(25/100*r):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
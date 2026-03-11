vr = float(input('Insira o valor da renda: '))
vp = float(input('Insira o valor da prestacao: '))

vt = vr * .3

if vp > vt: 
	print('Emprestimo nao aprovado')
else:
	print('Emprestimo aprovado')
	
	
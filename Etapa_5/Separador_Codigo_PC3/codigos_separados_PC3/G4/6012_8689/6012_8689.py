vr = float(input('Informe o valor da renda de Paulo: '))
vp = float(input('Informe o valor da prestacao que ele pode pagar por mes: '))
vr1 = vr * 0.25
if vp >=  vr1:
	print('Emprestimo nao aprovado')
else:
	print('Emprestimo aprovado')
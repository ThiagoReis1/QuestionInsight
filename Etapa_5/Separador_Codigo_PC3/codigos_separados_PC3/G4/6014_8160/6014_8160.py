vr= float(input('valor da renda: '))
vp= float(input('valor da prestacao: '))
v= vr*35/100
if(vp>=v):
	print('Emprestimo nao aprovado')
else:
	print('Emprestimo aprovado')
e=float(input('horas extras:'))
n=float(input('horas nao trabalhadas:'))
H=e-((2/3)*n)
if(H<=600):
	print(e, ' extras e',n,' de falta')
	print('R$ 200.0')
else:
	print(e, ' extras e', n, ' de falta')
	print('R$ 300.0')
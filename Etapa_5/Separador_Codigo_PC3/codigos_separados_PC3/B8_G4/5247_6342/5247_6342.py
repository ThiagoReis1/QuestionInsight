s = float(input('Salario atual: '))
c = int(input('Codigo do funcionario: '))

if (s>0) and (c == 101) or (c==102) or (c==103) or (c==104):
	if c==101:
		v = s*0.008
		v1 = v+s
		print('Novo salario: R$', round(v1, 2))
	elif c ==102:
		v=s*0.0065
		v1 = v+s
		print('Novo salario: R$', round(v1, 2))
	elif c==103:
		v=s*0.006
		v1 = v+s
		print('Novo salario: R$', round(v1, 2))
	elif c==104:
		v=s*0.0055
		v1 = v+s
		print('Novo salario: R$',round (v1, 2))
else:
	print('Dados invalidos')


		
		
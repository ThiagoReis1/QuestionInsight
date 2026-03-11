n1 = float(input('nota'))
n2 = float(input('nota'))
n3 = float(input('nota'))
n4 = float(input('nota'))
n5 = float(input('nota'))

m = (n1+n2+n3+n4+n5)/5

if m >= 6:
	print(round(m,2))
	print('Aprovacao')
elif m < 6:
	print(round(m,2))
	print('Reprovacao')


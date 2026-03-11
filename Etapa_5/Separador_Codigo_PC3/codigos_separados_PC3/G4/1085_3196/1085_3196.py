n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))
n5 = float(input('nota 5: '))
nf = (n1+n2+n3+n4+n5)/ 5
nf2 = round(nf ,2)


if nf2 >= 6.0:
	print('Aprovacao')
else:
	print('Reprovacao')
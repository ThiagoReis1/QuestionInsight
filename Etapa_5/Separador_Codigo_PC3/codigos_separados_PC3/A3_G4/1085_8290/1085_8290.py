from numpy import *

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))
n5 = float(input('nota 5: '))

m = (n1 + n2 + n3 + n4 + n5)/5
a = ''

if (m >= 6):
	a = 'Aprovacao'
	
else:
	a = 'Reprovacao'
	
print(round(m, 2))
print(a)
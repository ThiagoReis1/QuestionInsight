a = float(input('nota 1: '))
b = float(input('nota 2: '))
c = float(input('nota 3: '))

M = ( a + b + c ) / 3

if ( M >= 6.0 ):
	mens = "Aprovacao"
else:
	mens = "Reprovacao"
print(round(M,2))
print(mens)
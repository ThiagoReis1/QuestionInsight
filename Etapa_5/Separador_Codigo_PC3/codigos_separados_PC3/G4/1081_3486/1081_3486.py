n1 = float(input('digite a nota 1:'))
n2 = float(input('digite a nota 2:'))
n3 = float(input('digite a nota 3:'))
n4 = float(input('digite a nota 4:'))
nota = (n1+n2+n3+n4)/4
if(nota>=5):
	msg = 'Aprovacao'
	print(round(nota, 2))
	print(msg)
else:
	msg = 'Reprovacao'
	print(round(nota, 2))
	print(msg)
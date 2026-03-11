torta = 6.00
pastel = 5.00
bebida = 4.50

comida = input('(T) para torta ou (P para pastel: ').upper()
qtde = int(input('qtde? '))
cap = int(input('qtde de cap? '))

if comida == ('T'):
	qtdet = (qtde * torta) + (cap * bebida)
	print (round(qtdet,2))
else:
	qtdep = (qtde * pastel) + (cap * bebida)
	print (round(qtdep,2))

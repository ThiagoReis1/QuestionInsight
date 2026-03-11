ci = 50

km = int(input('digite a distancia da entrega e, quilometros: '))

if km<10:
	x = ci + 5.5
	print (round(x,2))
elif km>10:
	y = ci + 10
	print (round(y, 2))
elif km==10:
	z = ci + 7.75
	print (round(z,2))
			
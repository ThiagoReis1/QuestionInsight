depositoinicial = float(input())
meses = int(input())

acumuladora = depositoinicial
cont = 0

while (cont != meses):
	acumuladora = (acumuladora * (1.2/100)) + acumuladora
	print (round(acumuladora, 2))
	cont += 1
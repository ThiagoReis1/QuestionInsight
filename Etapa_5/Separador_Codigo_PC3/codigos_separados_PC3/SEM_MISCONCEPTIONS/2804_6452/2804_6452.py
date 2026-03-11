qd=int(input('quantidade de dinheiro inicial'))
meses=int(input('meses'))
total=qd
taxa=1/100
cont=0
while cont<meses:
	cont=cont+1
	total= total + (total*taxa)
	print(round(total,2))

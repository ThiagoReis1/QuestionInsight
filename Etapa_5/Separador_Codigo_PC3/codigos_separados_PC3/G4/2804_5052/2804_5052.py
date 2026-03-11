di=float(input("Deposito inicial: "))
nm=int(input("Numero de meses: "))

mes=0

total=di+(mes*0.01)

while mes != nm:
	total=total+(total*0.01)
	mes=mes+1
	print(round(total,2))
	
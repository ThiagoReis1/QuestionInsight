x=float(input("digite o valor de x: "))
k=int(input("digite o numero de tempos da serie: "))

cont=0
arctgx = 0
while cont<k:
	N = 2*cont+1
	cont=cont+1
	arctgx = arctgx + (x**N)/N
print(round(arctgx, 7))	
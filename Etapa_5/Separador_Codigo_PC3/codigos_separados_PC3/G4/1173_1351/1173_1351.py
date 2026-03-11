vs = int(input("informe o valor da serie: "))
cont = 1
ap = 2
while( cont > vs):
	b = 5 + (cont*2 + 2)
	ap = (-1)(vs**ap) + ((vs + cont)**ap)/b
	cont= cont + 1
print(round(ap,10))
rj = input('cara ou coroa: ').upper()

cont = 0
qddc = 0
while (rj!= 'S'):
	if rj == 'CARA':
		cont = cont + 1
		qddc = qddc + 1
	else:
		cont = cont + 1
	rj = input('cara ou coroa: ').upper()
porc = (qddc / cont)*100
print(cont)
print(porc)
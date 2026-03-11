ataque = input('tipo de ataque (cauda/cuspe): ')
n = float(input('valor (1 a 4): '))
t = float(input('numero de turno: '))

if(ataque.upper() == 'CUSPE'):
	d = (2*n)*t
else:
	d = n*t

print(d)
x = input('tapioca ou Salgado? (T/S)')
y = int(input('quantidade de tapiocas/salgados'))
z = int(input('quantidade de acais: '))

if(x.upper() == 'S'):
	valor = (y * 5) + (z * 13)
	print(valor)
	
else:
	valor = (y * 3.5) + (z * 13)
	print(valor)
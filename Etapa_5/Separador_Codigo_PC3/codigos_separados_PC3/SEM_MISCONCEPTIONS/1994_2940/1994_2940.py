am = input('informe o nome do aminoacido (histidina/leucina/lisina): ')

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if((am == 'histidina') or (am == 'leucina') or (am == 'lisina')):
	if(am == 'histidina'):
		x = ((C * 6) + (H * 10) + (N * 3) + (O * 2))
		print(round(x, 2))
	elif((am == 'leucina') or (am == 'lisina')):
		if(am == 'leucina'):
			x = ((C * 6) + (H * 13) + (N) + (O * 2))
			print((round(x, 2))
		elif(am == 'lisina'):
			x = ((C * 6) + (H * 15) + (N * 2) + (O * 2))
			print((round(x, 2))
else:
	print('Dado Invalido')
				

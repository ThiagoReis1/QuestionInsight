n = int(input('numero: '))

if n >= 1:
	if n % 3 == 0:
		print('Pirlim')
	
	elif n % 5 == 0:
		print('Pimpim')
		
	elif n % 3 and n % 5 == 0:
		print('pirlim-pimpim')
		
else:
	print('n')
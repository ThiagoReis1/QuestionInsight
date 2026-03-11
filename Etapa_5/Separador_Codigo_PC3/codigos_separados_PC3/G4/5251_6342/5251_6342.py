d = input('Destino: ').lower ()
i = int(input('Idade: '))

if (i>0) and (i<=150) and ((d=='porto velho') or (d=='santarem') or (d=='belem') or (d=='tefe') or (d=='tabatinga')):

	if d=='porto velho':
		v = 500.0
	elif d=='santarem':
		v = 370.0
	elif d=='belem':
		v = 600.0
	elif d=='tefe':
		v = 360.0
	else:
		v = 550.0
		
	if (0<i) and (i<=2):
		v1 = v*0.0
		print('Passagem: R$', round(v1, 2))
	elif(i>=3) and (i<=12):
		v1 = v/2
		print('Passagem: R$', round(v1, 2))
	elif (i>=13) and (i<= 64):
		v1 = v
		print('Passagem: R$', round(v1, 2))
	else:
		v1 = v*0.70
		print('Passagem: R$', round(v1, 2))
else:
	print('Entradas invalidas')
		
		
		
		
		

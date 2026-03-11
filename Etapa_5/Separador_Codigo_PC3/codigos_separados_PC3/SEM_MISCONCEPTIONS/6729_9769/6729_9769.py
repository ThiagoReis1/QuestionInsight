numero= int(input('insira o numero de x: '))

if numero %41== 0:
	total= numero//41
	print(total)
	print('sim')
	
else: 
	total= numero%41
	print(total)
	print('nao')
	
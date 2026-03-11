distancia=float(input('De distancia da corrida: '))
chakra=float(input('De as partes de chakra: '))

partes=30*distancia/0.01
print(round(partes,2))
if(chakra>=partes):
	print('vai conseguir')
else:
	print('nao vai conseguir')
	
	
	

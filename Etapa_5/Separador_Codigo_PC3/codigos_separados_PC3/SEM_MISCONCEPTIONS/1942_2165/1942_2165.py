nomeAminoacido = input()
if nomeAminoacido == 'histidina':
	resul = 6*12.011 + 10*1.00794 + 3*14.00674 + 2*15.999
	print(round(resul, 2))	
else:
	resul = 5*12.011 + 10*1.00794 + 14.00674 + 2*15.999
	print(round(resul, 2))
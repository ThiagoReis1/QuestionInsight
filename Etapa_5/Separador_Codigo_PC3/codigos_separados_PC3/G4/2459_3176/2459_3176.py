p = float(input('peso:'))
d = float(input('distancia:'))
c = float(input('codigo:'))

if (c==1):
	s = (p*25) + (d*0.10)
	icms = s * 0.17
	sf = s + icms
	print(round(sf,2))
elif(c==2):
	s = (p*25) + (d*0.10)
	icms = s * 0.175
	sf = s + icms
	print(round(sf,2))
elif(c==3):
	s = (p*25) + (d*0.10)
	icms = s * 0.18
	sf = s + icms
	print(round(sf,2))
elif(c==4):
	s = (p*25) + (d*0.10)
	icms = s * 0.20
	sf = s + icms
	print(round(sf,2))
	
else:
	print('Entrada invalida')
	
	
	
	

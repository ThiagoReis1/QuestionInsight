laranja = 0.75
laranjas = 0.60

compradas = int(input("Quantas laranjas ira comprar?: "))

if compradas >= 6:
	pagar = compradas*laranjas
	
else:
	pagar = compradas*laranja
	
print (pagar)
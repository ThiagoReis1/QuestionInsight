v = float(input())
t = float(input())

if(v <= 0 or t <0):
	print("Entradas:", v,"km/h e", t,"h")
	print("Dados invalidos")
else:
	D = v * t
	
	print("Entradas:",v,"km/h e", t,"h")
	
	if( D < 100):
		print("Proxima parada: Bravos")
	elif(D >=100 and D< 200 ):
		print("Proxima parada: Castamere")
	elif(D>=200 and D < 400):
		print("Proxima parada: Doriath")
	elif(D>= 400 and D < 600):
		print("Proxima Parada: Edoras")
	elif(D>= 600 and D< 750):
		print("Proxima parada: Fangorn")
	elif(D>=750 and D <1150):
		print("Proxima parada: Gondor")
	elif(D>=1150):
		print("Proxima parada: Hogsmead")
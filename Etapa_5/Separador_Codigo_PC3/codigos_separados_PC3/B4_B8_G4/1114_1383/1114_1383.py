X = float(input("velocidade"))
Y = float(input("hora"))

if (X>0) and (Y>0):
	if (X*Y>100):
	    Z = "Bravos"
	elif (X*Y >= 100):
	    Z="Castamere"
	elif (X*Y >=200):
	    Z="Doriath"
	elif (X*Y >=400):
	    Z="Edoras"
	elif (X*Y >=600):
	    Z="Fangorn"
	elif (X*Y >=750):
	    Z="Gondor"
	elif (X*Y >=1150):	
	 	 Z="Hogsmead"
	elif (X*Y >=1400):
	    Z="Hogsmead"
	print ("Entradas:", round(X, 1), "km/h e", round(Y, 1), "h")
	print ("Proxima parada:", Z)
else:
	print ("Entradas:", round(X, 1), "km/h e", round(Y, 1), "h")
	print ("Dados invalidos")
v = float(input(""))
t = float(input(""))
print("Entradas:", v, "km/h", "e", t, "h")

dist = v * t 

if(v <= 0) or (t <= 0):
	print("Dados invalidos")
else:
	if (dist < 100):
		print("Proxima parada: Bravos")
	elif (dist < 200):
		print("Proxima parada: Castamere")
	elif (dist < 400):
		print("Proxima parada: Doriath")
	elif (dist < 600):
		print("Proxima parada: Edoras")
	elif (dist < 750):
		print("Proxima parada: Fagorn")
	elif (dist < 1150):
		print("Proxima Parada: Gondor")
	elif (dist <= 1450):
		print("Proxima parada: Hogsmead")
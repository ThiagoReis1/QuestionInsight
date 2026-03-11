a = float(input("velocidade: "))
b = float(input("tempo: "))

print("Entradas:", a, "km/h e", b,"h")

e = a * b

if (a > 0) and (b > 0):
	
	if (e <= 100):
		print("Proxima parada: Bravos")
	
	elif (e <= 200):
		print("Proxima parada: Castamere")
	
	elif (e <= 400):
		print("Proxima parada: Doriath")
	
	elif (e <= 600):
		print("Proxima parada: Edoras")
		
	elif (e <= 750):
		print("Proxima parada: Fangorn")
		
	elif (e <= 1150):
		print("Proxima parada: Gondor")
		
	elif (e <= 1300):
		print("Proxima parada: Hogsmead")
		
else: 
	print("Dados invalidos")
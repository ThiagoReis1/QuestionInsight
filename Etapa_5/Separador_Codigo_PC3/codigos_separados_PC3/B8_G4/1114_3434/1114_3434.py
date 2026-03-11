v = float(input("velocidade: "))
t = float(input("tempo de viagem: "))

p = v * t

print ("Entradas:", v,"km/h e", t, "h")
#print ("posicao", p)
if (v * t > 0):
	if (p < 100):
		print("Proxima parada: Bravos")
	elif (100 <= p < 200):
		print("Proxima parada: Castamere")
	elif (200 <= p < 400):
		print("Proxima parada: Doriath")
	elif (400 <= p < 600):
		print("Proxima parada: Edoras")
	elif (600 <= p < 750):
		print("Proxima parada: Fangorn")
	elif (750 <= p < 1150):
		print("Proxima parada: Gondor")
	elif (p >=1150):
		print("Proxima parada: Hogsmead")
else:
	print("Dados invalidos")

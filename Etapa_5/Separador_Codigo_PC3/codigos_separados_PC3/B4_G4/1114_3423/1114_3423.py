v= float(input("velocidade do trem: "))
t= float(input("tempo de viagem: "))
d= v*t
print("Entradas:",v,"km/h","e",t,"h")
if (v <= 0) or (t < 0):
	print("Dados invalidos")
elif (0 <= d <100):
	print("Proxima parada: Bravos")
elif (100 <= d < 200):
	print("Proxima parada: Castamere")
elif (200 <= d < 400):
	print("Proxima parada: Doriath")
elif (400 <= d < 600):
	print("Proxima parada: Edoras")
elif (600 <= d < 750):
	print("Proxima parada: Fangorn")
elif (750 <= d < 1150):
	print("Proxima parada: Gondor")
elif (d >= 1150):
	print("Proxima parada: Hogsmead")
else:
	print("Dados invalidos")

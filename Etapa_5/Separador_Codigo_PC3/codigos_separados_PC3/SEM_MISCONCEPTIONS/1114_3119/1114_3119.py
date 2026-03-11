vel = float(input("Velocidade do trem: "))
tempo = float(input("Tempo de viagem: "))

distancia = (vel * tempo)
km = distancia

if (km < 100) :
	print("Entradas:", vel, "km/h", "e", tempo, "h")
	print("Proxima parada: Bravos")
elif (km < 200 ):
	print("Entradas:", vel, "km/h", "e", tempo, "h")
	print("Proxima parada: Castamare")
elif (km < 400):
	print("Entradas:", vel, "km/h", "e", tempo, "h")
	print("Proxima parada: Doriath")
elif (km < 600):
	print("Entradas:", vel, "km/h", "e", tempo, "h")
	print("Proxima parada: Edoras")
elif (km < 750):
	print("Entradas:", vel, "km/h", "e", tempo, "h")
	print("Proxima parada: Fangorn")	
elif (km < 1150):
	print("Entradas:", vel, "km/h", "e", tempo, "h")
	print("Proxima parada: Gordon")
elif (km >= 1400):
	print("Entradas:", vel, "km/h", "e", tempo, "h")
	print("Proxima parada: Hogsmead")
else:	
	(km <= 0)
	print("Entradas:", vel, "km/h", "e", tempo, "h")
	print("Dados invalidos")


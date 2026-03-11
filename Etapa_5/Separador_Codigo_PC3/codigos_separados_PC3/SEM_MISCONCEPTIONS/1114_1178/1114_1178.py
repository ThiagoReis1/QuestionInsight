velocidade = float(input("Velocidade:  " ))
tempo = float(input("Tempo: "))

distancia = tempo*velocidade

if (distancia == 1 ):
	print("Entradas:", velocidade,"km/h", "e", tempo,"h" )
	print("Proxima Parada:Bravos")
elif (distancia >=100):
	print("Entradas:", velocidade,"km/h", "e", tempo,"h" )
	print("Proxima Parada: Castamere")
elif (distancia >= 200.0):
	print("Entradas:", velocidade,"km/h", "e" ,tempo, "h")
	print("Proxima Parada: Doriath")
elif (distancia >= 400.0):
	print("Entradas:", velocidade,"km/h", "e", tempo,"h" )
	print("Proxima Parada:Edoras")			
elif (distancia >= 750.0):
	print("Entradas:", velocidade,"km/h", "e", tempo,"h" )
	print("Proxima Parada:Fangorn")			
elif (distancia>= 1150.0):
	print("Entradas:", velocidade,"km/h", "e", tempo,"h" )
	print("Proxima Parada:Gondor")
elif (distancia>= 1500.0):
	print("Entradas:", velocidade,"km/h", "e", tempo,"h" )
	print("Proxima Parada:Hogsmead")
else:
	print("Dados invalidos")

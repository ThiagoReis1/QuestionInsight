velocidade=float(input("Digite aqui a velocidade:"))
tempo=float(input("Digite aqui o tempo:"))
print("Entradas:",velocidade,"km/h","e",tempo ,"h")
distancia=velocidade*tempo
tempoviagem=distancia/tempo
if(velocidade>0 and tempo>0):
	if(tempo>tempoviagem):
		print("Proxima parada: Hogsmead")
	elif(distancia>0 and distancia<100):
		print("Proxima parada: Bravos")
	elif(distancia>=100 and distancia<200):
		print("Proxima parada: Castamere")
	elif(distancia>200 and distancia<=400):
		print("Proxima parada: Doriath")
	elif(distancia>600 and distancia<=750):
		print("Proxima parada: Gondor")
	elif(distancia>750 and distancia<=1150):
		print("Proxima parada: Hogsmead")
	elif(distancia>1400):
		print("Proxima parada: Hogsmead")
else:
	print("Dados invalidos")
velocidade=float(input("Velocidade: "))
tempo=float(input("Tempo: "))
calculo=velocidade*tempo
print ("Entradas: ", velocidade, "km/ e", tempo, "h")
if (velocidade<=0 or tempo<=0):
	print ("Dados invalidos")
else:
	if ((calculo*7)%tempo==100):
		print ("Proxima parada: Castamere")
	elif ((calculo*7)%tempo==200):
		print ("Proxima parada: Edoras")
	elif ((calculo*7)%tempo==150):
		print ("Proxima parada: Fangorn")
	elif ((calculo*7)%tempo==400):
		print ("Proxima parada: Gondor")
	elif ((calculo*7)%tempo==200):
		print ("Proxima parada: Hogsmead")

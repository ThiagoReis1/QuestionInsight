vel = float(input("Velocidade do trem: "))
t = float(input("Tempo de viagem: "))
print("Entradas:", vel, "km/h e", t, "h")

if(vel <= 0 or t < 0):
	print("Dados invalidos")
elif((vel * t >= 0) and (vel * t < 100)):
	print("Proxima parada: Bravos")
	
elif(100 <= vel * t and vel * t < 200):
	print("Proxima parada: Castamere")
	
elif(200 <= vel * t and vel * t < 400):
	print("Proxima parada: Doriath")
	
elif(400 <= vel * t and vel * t < 600 ):
	print("Proxima parada: Edoras")
	
elif(600 <= vel * t and vel * t < 750):
	print("Proxima parada: Fangorn")
	
elif(750 <= vel * t and vel * t < 1150):
	print("Proxima parada: Gondor")
	
elif(1150 <= vel * t ):
	print("Proxima parada: Hogsmead")

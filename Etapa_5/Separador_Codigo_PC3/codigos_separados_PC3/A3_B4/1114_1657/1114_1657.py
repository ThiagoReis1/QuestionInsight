vel = float(input("Escreva o valor da velocidade:"))
tempo = float(input("Escreva o valor do tempo:"))
print("Entradas:", vel, "km/h e", tempo, "h")
x = vel * tempo
if(vel > 0 and tempo > 0):
	if(x==0):
		x = "Avalon"
	elif(x<100):
		x = "Bravos"
	elif(100 <= x < 200):
		x = "Castamere"
	elif(200 <= x < 400):
		x = "Doriath"
	elif(400 <= x < 600):
		x = "Edoras"
	elif(600 <= x < 750):
		x ="Fangorn"
	elif(750 <= x < 1150):
		x = "Gondor"
	elif(1150 <= x < 1750):
		x ="Hogsmead"
	else:
		x ="Hogsmead"
	print("Proxima parada:", x)
else:
	 x= "Dados invalidos"

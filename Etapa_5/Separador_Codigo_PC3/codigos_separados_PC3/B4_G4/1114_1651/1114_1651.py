v = float(input("Qual a velocidade?"))
t = float(input("Qual o tempo?"))

d = v * t

if(v > 0 and t > 0):
	if(d <= 100):
		destino = "Bravos"
	elif(d >= 100 or d == 200):
		destino = "Castamere"
	elif(d >= 200 or d == 400):
		destino = "Doriath"
	elif(d >= 400 or d == 600):
		destino = "Edoras"
	elif(d >= 600 or d == 750):
		destino = "Fangorn"
	elif(d >= 750 or d == 1150):
		destino = "Gondor"
	elif(d >= 1150 or d == 1400):
		destino = "Hogsmead"
	else:
		destino = "Hogsmead"
else: 
	destino = "Hogsmead"
		
print("Entradas:", v, "km/h e", t, "h")
		
if(v <= 0 or t < 0):
	print("Dados invalidos")
else:
	print("Proxima parada:", destino)
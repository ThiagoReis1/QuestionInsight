vt = float(input("Qual a velocidade do trem: "))
tempo = float(input("Qual o tempo de viagem: "))
distancia_total = 1400
tempo_total = distancia_total / vt
distancia = vt * tempo
print("Entradas: ", vt, "km/h e", tempo, "h")
if(tempo > tempo_total):
	print("Dados invalidos")
elif(distancia < 100 and distancia >= 0):
	x = "Bravos"
elif(distancia < 200 and distancia >= 100):
	x = "Castamere"
elif(distancia < 400 and distancia >= 200):
	x = "Doriath"
elif(distancia < 600 and distancia >= 400):
	x = "Edoras"
elif(distancia < 750 and distancia >= 600):
	x = "Fangorn"
elif(distancia < 1150 and distancia >= 750):
	x = "Gondor"
else:
	x = "Hogsmead"
if(distancia > 1400):
	print("Dados invalidos")
else:
	print("Proxima parada: ", x)
vtrem = float(input("Qual a velocidade do trem em km/h ? : "))
tempo = float(input("Qual o tempo de viagem em horas ? : "))

print("Entradas:", vtrem, "km/h", "e", tempo, "h")
d = vtrem * tempo

if	(d <= 0):
	print("Dados invalidos")
elif	(0 < d < 100):
	print("Proxima parada: Bravos")
elif	(100 <= d < 200):
	print("Proxima parada: Castamere")
elif	(200 <= d < 400):
	print("Proxima parada: Doriath")
elif	(400 <= d < 600):
	print("Proxima parada: Edoras")
elif	(600 <= d < 750):
	print("Proxima parada: Fangorn")
elif	(750 <= d < 1150):
	print("Proxima parada: Gondor")
elif	(1150 <= d < 1400):
	print("Proxima parada: Hogsmead")
elif	(d >= 1400):
	print("Proxima parada: Hogsmead")
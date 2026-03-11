vlo = float(input("digite o valor da velocidade do trem: "))
tempo = float(input("tempo de viagem: "))

print("Entradas:", vlo, "km/h e", tempo, "h")
dis= tempo * vlo 

if (((0 < dis < 100) or (100 <= dis < 200) or (200 <= dis < 400) or (400 <= dis < 600) or (600 <= dis < 750) or (750 <= dis < 1150) or (1150 <= dis < 1400)) and (tempo > 0) and (vlo > 0)) :
	if (0 < dis < 100) :
		print("Proxima parada: Bravos")
	elif (100 <= dis < 200) :
		print("Proxima parada: Castamere")
	elif (200 <= dis < 400) :
		print("Proxima parada: Doriath")
	elif (400 <= dis < 600) :
		print("Proxima parada: Edoras")
	elif (600 <= dis < 750) :
		print("Proxima parada: Fangorn")
	elif (750 <= dis < 1150) :
		print("Proxima parada: Gondor")
	elif (1150 <= dis) :
		print("Proxima parada: Hogsmead")
else :
	print("Dados invalidos")
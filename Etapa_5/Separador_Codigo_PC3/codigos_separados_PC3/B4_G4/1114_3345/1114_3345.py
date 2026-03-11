v = float(input("Velocidade do trem: "))
t = float(input("Tempo de viagem: "))
d = v*t
if (v > 0) and (t >0):
	if (d > 0) and (d<100):
		m = "Bravos"
	elif (d>=100) and (d<200):
		m = "Castamere"
	elif (d>=200) and (d<400):
		m = "Doriath"
	elif (d>=400) and (d<600):
		m = "Edoras"
	elif (d>=600) and (d<750):
		m = "Fangorn"
	elif (d>=750) and (d<1150):
		m = "Gondor"
	elif (d>=1150) and (d<1400):
		m = "Hogsmead"
	else:
		m = "Hogsmead"
	print("Entradas: ", v, " km/h e ", t, " h")
	print("Proxima parada: ", m)
else:
	print("Entradas: ", v, " km/h e ", t, " h")
	print("Dados invalidos")
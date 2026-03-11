v = float(input("Velocidade do trem: "))
t = float(input("Tempo de viagem: "))

d = (v * t)

if(d <= 0) or (t < 0):
	print("Entradas:", v, "km/h e", t, "h")
	print("Dados invalidos")
else:
	if((d > 0) and (d < 100)):
		print("Entradas:", v, "km/h e", t, "h")
		print("Proxima parada: Bravos")
	elif((d >= 100) and (d < 200)):
		print("Entradas:", v, "km/h e", t, "h")
		print("Proxima parada: Castamere")
	elif((d >= 200) and (d < 400)):
		print("Entradas:", v, "km/h e", t, "h")
		print("Proxima parada: Doriath")
	elif((d >= 400) and (d < 600)):
		print("Entradas:", v, "km/h e", t, "h")
		print("Proxima parada: Edoras")
	elif((d >= 600) and (d < 750)):
		print("Entradas:", v, "km/h e", t, "h")
		print("Proxima parada: Fangorn")
	elif((d >= 750) and (d < 1150)):
		print("Entradas:", v, "km/h e", t, "h")
		print("Proxima parada: Gondor")
	elif((d >= 1150) and (d < 1400)):
		print("Entradas:", v, "km/h e", t, "h")
		print("Proxima parada: Hogsmead")
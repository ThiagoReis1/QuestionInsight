v = float(input())
t = float(input())
s = v * t

print("Entradas: ", v, "km/h e" , t, "h")

if (v > 0 and t > 0):
	if(s < 100):
		x = "Avalon"
	elif (s >= 100 and s < 200):
		x = "Bravos"
	elif (s >= 200 and s < 400):
		x = "Castamere"
	elif (s >= 400 and s < 600):
		x = "Doriath"
	elif (s >= 600 and s < 750):
		x = "Edoras"
	elif (s >= 750 and s < 1150):
		x = "Fangorn"
	elif (s >= 1150 and s < 1400):
		x = "Gondor"
	elif (s > 1400):
		x = "Hogsmead"
	print("Proxima parada:", x)
else:
	print("Dados invalidos")
	
v = float(input("Velocidade: "))
t = float(input("Tempo: "))
d = v * t
print("Entradas:", v, "km/h e",t, "h")
if(v  > 0 and t > 0):
	if(d > 0 and d < 100):
		z = "Bravos"
		print("Proxima parada:", z)
	elif(d >= 100 and d < 200):
		z = "Castamere"
		print("Proxima parada:", z)
	elif(d >= 200 and d < 400):
		z = "Doriath"
		print("Proxima parada:", z)
	elif(d >= 400 and d < 600):
		z = "Edoras"
		print("Proxima parada:", z)
	elif(d >= 600 and d < 750):
		z = "Fangorn"
		print("Proxima parada:", z)
	elif(d >= 750 and d < 1150):
		z = "Gondor"
		print("Proxima parada:", z)
	elif(d >= 1150 and d < 1400):
		z = "Hogsmead"
		print("Proxima parada:", z)
else:
	print("Dados invalidos")
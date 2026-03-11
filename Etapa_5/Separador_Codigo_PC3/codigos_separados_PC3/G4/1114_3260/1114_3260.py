v = float(input("velocidade= "))
t = float(input("tempo= "))

d = (v * t)

if v > 0 and t >= 0:
	if d < 100:
		p = "Bravos"
		print("Entradas:", v ,"km/h e", t, "h")
		print("Proxima parada:", p)
	elif d < 200:
		p = "Castamere"
		print("Entradas:", v ,"km/h e", t, "h")
		print("Proxima parada:", p)
	elif d < 400:
		p = "Doriath"
		print("Entradas:", v ,"km/h e", t, "h")
		print("Proxima parada:", p)
	elif d < 600:
		p = "Edoras"
		print("Entradas:", v ,"km/h e", t, "h")
		print("Proxima parada:", p)
	elif d < 750:
		p = "Fangorn"
		print("Entradas:", v ,"km/h e", t, "h")
		print("Proxima parada:", p)
	elif d < 1150:
		p = "Gondor"
		print("Entradas:", v ,"km/h e", t, "h")
		print("Proxima parada:", p)
	else:
		p = "Hogsmead"
		print("Entradas:", v ,"km/h e", t, "h")
		print("Proxima parada:", p)
else:
	print("Entradas:", v, "km/h e", t, "h")
	print("Dados invalidos")
v = float(input("Velocidade em km/h: "))
t = float(input("Tempo em h: ")) 

print(("Entradas:"), v, "km/h e", t,"h")

s = v * t

if v <= 0 or t <=0:
	print("Dados invalidos")
elif s < 100:
	print("Proxima parada: Bravos")
elif s < 200:
	print("Proxima parada: Castamere")
elif s < 400:
	print("Proxima parada: Doriath")
elif s < 600:
	print("Proxima parada: Edoras")
elif s < 750:
	print("Proxima parada: Fangorn")
elif s < 1150:
	print("Proxima parada: Gondor")
elif s >= 1400:
	print("Proxima parada: Hogsmead")

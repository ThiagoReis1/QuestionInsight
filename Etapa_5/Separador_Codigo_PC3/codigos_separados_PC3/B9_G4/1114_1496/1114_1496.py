v = float(input("Insira a velocidade:"))
t = float(input("Insira o tempo de viagem:"))

print("Entradas:",v,"km/h e",t,"h")

s = v * t

if (v>0 and t>0):
	if (s<100):
		print("Proxima parada: Bravos")
	elif (s<200 and s>=100):
		print("Proxima parada: Castamere")
	elif (s<400 and s>=200):
		print("Proxima parada: Doriath")
	elif (s<600 and s>=400):
		print("Proxima parada: Edoras")
	elif(s<750 and s>=600):
		print("Proxima parada: Fangorn")
	elif (s<1150 and s>=750):
		print("Proxima parada: Gondor")
	else:
		print("Proxima parada: Hogsmead")
else:
	print("Dados invalidos")
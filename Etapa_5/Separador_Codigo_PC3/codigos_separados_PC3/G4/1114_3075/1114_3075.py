v = float(input())
t = float(input())

print("Entradas:",v,"km/h e",t,"h")
d = v*t
if (d <= 0):
	print("Dados invalidos")
else:
	if (d >= 0 and d < 100):
		p = "Bravos"
	elif(d >= 100 and d < 200):
		p = "Castamere"
	elif (d >= 200 and d < 400):
		p = "Doriath"
	elif (d >= 400 and d < 600):
		p = "Edoras"
	elif (d >= 600 and d < 750):
		p = "Fangorn"
	elif (d >= 750 and d < 1150):
		p = "Gondor"
	elif (d >= 1150 and d < 1400):
		p = "Avalon"
	else:
		print ("Dados invalidos")
	print("Proxima parada:",p)
		
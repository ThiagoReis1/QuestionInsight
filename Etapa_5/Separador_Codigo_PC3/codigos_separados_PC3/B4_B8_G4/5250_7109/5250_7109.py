v = float(input("Km/h: "))
t = float(input("Tempo de viagem: "))
z = "Proxima parada:"
h = v*t
if v> 0 and t >=0:
	print("Entradas:",v,"km/h e",t,"h")
	if t>1400:
		print(z,"Hogsmead")
	elif 0<h<100:
		print(z,"Bravos")
	elif 100<=h<200:
		print(z,"Castamere")
	elif 200 <=h<400:
		print(z,"Doriath")
	elif 400<=h<600:
		print(z,"Edoras")
	elif 600<=h<750:
		print(z,"Fangorn")
	elif 750<=h<1150:
		print(z,"Gondor")
	elif 1150<=h<1400:
		print(z,"Hogsmead")
else:
	print("Dados invalidos")
	

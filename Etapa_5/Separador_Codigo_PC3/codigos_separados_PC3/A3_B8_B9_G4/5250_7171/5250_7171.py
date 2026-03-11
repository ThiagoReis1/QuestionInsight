v=float(input("Digite a velocidade:"))
t= float(input("Digite o tempo de viagem:"))


d= v*t
thg= 1600/v
print( "Entradas: ", v, "km/h e", t, " h")

if (v>0) and (t>0):
	if (d<100):
		print("Proxima parada: Bravos")
	elif(d>=100) and (d<=200):
		print("Proxima parada: Castamere")
	elif (d>=200) and (d<=400):
		print("Proxima parada: Doriath")
	elif (d>=400) and (d<=800):
		print( "Proxima parada: Edoras")
	elif (d>=800) and (d<=950):
		print("Proxima parada: Fangorn")
	elif (d>=950) and (d<=1350):
		print("Proxima parada: Gondor")
	elif (d>=1350):
		print( "Proxima parada; Hogmead")
	
else:
	print("Dados invalidos")
	
		
		
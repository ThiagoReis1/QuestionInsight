v = float(input(" Qual a velocidade do trem? :"))
t = float(input(" Qual o tempo de viagem ? :"))

d = v*t

if (d >= 250):
	print( "Entradas:",v,"Km/h", t , "h")
	print("Proxima parada: Hogsmead")
elif (d ==50):
	print ("Entradas:",v,"Km/h", t , "h")
	print("Proxima parada: Bravos")
elif (d ==100):
	print("Entradas:",v,"Km/h", t , "h")
	print("Proxima parada : ")
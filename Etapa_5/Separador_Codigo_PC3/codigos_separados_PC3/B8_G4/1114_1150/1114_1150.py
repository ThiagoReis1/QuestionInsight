X=float(input("velocidade do trem?"))
Y=float(input("tempo decorrido da viagem?"))
D=X*Y
if(D<=0 or Y<0 or X<=0):
	print("Entradas:",X,"km/h e",Y,"h")
	print("Dados invalidos")
elif(D<100):
	print("Entradas:",X,"km/h e",Y,"h")
	print("Proxima parada: Bravos")
elif(D<200):
	print("Entradas:",X,"km/h e",Y,"h")
	print("Proxima parada: Castemere")
elif(D<400):
	print("Entradas:",X,"km/h e",Y,"h")
	print("Proxima parada: Doriath")
elif(D<600):
	print("Entradas:",X,"km/h e",Y,"h")
	print("Proxima parada: Edoras")
elif(D<750):	
	print("Entradas:",X,"km/h e",Y,"h")
	print("Proxima parada: Fangorn")
elif(D<1050):
	print("Entradas:",X,"km/h e",Y,"h")
	print("Proxima parada: Gondor")
elif(D<1300):
	print("Entradas:",v,"km/h e ", t, "h")
	print("proxima parada: Hogsmead")
v=float(input("informe a velocidade do trem em km/h:"))
t=float(input("informe o tempo de viagem em horas: "))
print("Entradas:",v,"km/h e", t,"h")

if((v<=0)or(t<0)):
	print("Dados invalidos")
else:
	if(t==0):
		z="Avalon"
		print("Proxima parada:",z)
		
	elif(t >= (1400/v)):
		z="Hogsmead"
		print("Proxima parada:",z)
	elif(t==(100/v)):
		z="Bravos"
		print("Proxima parada:",z)
	elif(t==(200/v)):
		z="Castamere"
		print("Proxima parada:",z)
	elif(t==(400/v)):
		z="Doriath"
		print("Proxima parada:",z)
	elif(t==(600/v)):
		z="Edoras"
		print("Proxima parada:",z)
	elif(t==(750/v)):
		z="Fangorn"
		print("Proxima parada:",z)
	else:
		if(t==(1150/v)):
			z="Gondor"
			print("Proxima parada:",z)
	

	
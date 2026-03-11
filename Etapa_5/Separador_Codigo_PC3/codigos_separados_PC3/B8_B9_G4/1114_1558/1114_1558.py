v = float(input("Qual a velocidade do trem? "))
t = float(input("Qual o tempo de viagem? "))
d = v * t
if v< 0 or t<0:
	print("Entradas:",v,"km/h e",t,"h")
	print("Dados invalidos")
else:
	if (d<100):
		p = "Bravos"
	elif (d<200 and d>=100):
		p = "Castamere"
	elif (d<400 and d>=200):
	   p = "Doriath"
	elif (d<600 and d>=400):
		p = "Edoras"
	elif (d<750 and d>=600):
		p = "Fangorn"
	elif (d<1150 and d>=750):
		p = "Gondor"
	elif (d>=1150):
		p = "Hogsmead"
	print("Entradas:",v,"km/h e",t,"h")	
	print("Proxima parada: ",p)
		
	  
		

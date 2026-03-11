x= float (input("velocidade do trem:"))
y= float (input("tempo (em horas):"))
d= x* y

if (y>=0 and x>=0):
	if (d==0):
		print ("Entradas:", x, "km/h e", y, "h")
		print ("Proxima parada: Avalon")
	if (d<100):
		print ("Entradas:" ,x, "km/h e", y, "h")
		print ("Proxima parada: Bravos")
	elif (d>=100 and d<200):
		print ("Entradas:" ,x, "km/h e", y, "h")
		print ("Proxima parada: Castamere")
	elif (d>=200 and d<400):
		print ("Entradas:",x, "km/h e",y, "h")
		print ("Proxima parada: Doriath")
	elif (d>=400 and d<600):
		print ("Entradas", x, "km/h e",y, "h")
		print ("Proxima parada: Edoras")
	elif (d>=600 and d<750):
		print ("Entradas:" ,x, "km/h e",y, "h")
		print ("Proxima parada: Fangorn")
	elif (d>=750 and d<1150):
		print ("Entradas:" ,x, "km/h e",y, "h")
		print ("Proxima parada: Gondor")
	elif (d>=1150):
		print ("Entradas:",x,"km/h e",y,"h")
		print ("Proxima parada: Hogsmead")
else:
	print ("Entradas:" ,x, "km/h e",y,"h")
	print ("Dados invalidos")
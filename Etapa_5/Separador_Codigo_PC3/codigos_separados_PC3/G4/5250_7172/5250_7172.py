x=float(input("velocidade do trem:  "))
y=float(input("tempo de viagem:  "))

d=x*y

if(d>0 and d<100):
	z="Bravos"
	print("Entradas: ", x,"km/h e ", y, "h")
	print("Proxima parada: ", z)
elif(d>=100 and d<200):
	z="Castamere"
	print("Entradas: ", x,"km/h e ", y, "h")
	print("Proxima parada: ", z)
elif(d>=200 and d<400):
	z="Doriath"
	print("Entradas: ", x,"km/h e ", y, "h")
	print("Proxima parada: ", z)
elif(d>=400 and d<600):
	z="Edoras"
	print("Entradas: ",x ,"km/h e ", y, "h")
	print("Proxima parada: ", z)
elif(d>=600 and d<750):
	z="Fangorn"
	print("Entradas: ", x,"km/h e ", y, "h")
	print("PRoxima parada: ", z)
elif(d>=750 and d <1150):
	z="Gondor"
	print("Entradas: ", x,"km/h e ", y, "h")
	print("Proxima parada:", z)
elif(d>=1150 and d<1400):
	z="Hogsmead"
	print("Entradas: ", x,"km/h e ", y, "h")
	print("Proxima parada: ", z)
else:
	print("Entradas: ", x,"km/h e ", y, "h")
	print("Dados invalidos")
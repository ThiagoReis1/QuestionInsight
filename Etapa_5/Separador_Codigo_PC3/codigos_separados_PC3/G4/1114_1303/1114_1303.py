v=float(input("digitar a velocidade:"))
t=float(input("digitar o tempo:"))
print("Entradas:",v,"km/h","e",t,"h")

d=v*t

if(d>=0)  and(d<100):
	print("Proxima parada: Bravos")
elif(d>=100)and(d<200):
	print("Proxima parada: Castamere")
elif(d>=200)and(d<400):
	print ("Proxima parada: Doriath")
elif(d>=400)and(d<600):
	print ("Proxima parada: Edoras")
elif(d>=600)and(d<750):
	print("Proxima parada: Fangorn")
elif(d>=750)and(d<1150):
	print("Proxima parada: Gondor")
elif(d>=1150)and(d<1400):
	print("Proxima parada: Hogsmead")
	
else:
	print("Dados invalidos")

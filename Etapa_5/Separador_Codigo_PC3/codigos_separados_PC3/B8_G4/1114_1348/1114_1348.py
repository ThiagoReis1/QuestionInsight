v=float(input("velocidade:"))
t=float(input("tempo:"))
z=(v*t)
if((v<=0)or(t<0)):
	print("Entradas:",v,"km/h e",t,"h")
	print("Dados invalidos")
elif(99>z>0):
	Z="Bravos"
	print("Entradas:",v,"km/h e",t,"h")
	print("Proxima parada:",Z)
elif(199>z>=100):
	Z="Castamere"
	print("Entradas:",v,"km/h e",t,"h")
	print("Proxima parada:",Z)
elif(399>z>=200):
	Z="Doriath"
	print("Entradas:",v,"km/h e",t,"h")
	print("Proxima parada:",Z)
elif(599>z>=400):
	Z="Edoras"
	print("Entradas:",v,"km/h e",t,"h")
	print("Proxima parada:",Z)
elif(749>z>=600):
	Z="Fangorn"
	print("Entradas:",v,"km/h e",t,"h")
	print("Proxima parada:",Z)
elif(1149>z>=750):
	Z="Gondor"
	print("Entradas:",v,"km/h e",t,"h")
	print("Proxima parada:",Z)
elif(1399>z>=1150):
	Z="Hogsmead"
	print("Entradas:",v,"km/h e",t,"h")
	print("Proxima parada:",Z)
elif(z>=1400):
	Z="Avalon"
	print("Entradas:",v,"km/h e",t,"h")
	print("Proxima parada:",Z)
	
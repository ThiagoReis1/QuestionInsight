v= float(input())
t= float(input())

print("Entradas:",v,"km/h e",t,"h")
d = (v * t)

if(d == 0):
	m="Bravo"
	print("Proxima parada:",m)
elif(d == 100):
	m="Castamere"
	print("Proxima parada:",m)
elif(d==200):
	m="Doriath"
	print("Proxima parada:",m)
elif(d==200):
	m="Edoras"
	print("Proxima parada:",m)
elif(d==150):
	m="Fangorn"
	print("Proxima parada:",m)
elif(d==400):
	m="Gondor"
	print("Proxima parada:",m)
elif(d==250):
	m= "Hogsmead"
	print("Proxima parada:",m)
else:
	print("Dados invalidos")



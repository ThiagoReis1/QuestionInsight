v = float(input())
h = float(input())
s = v*h
s = round(s,1)

if(v <= 0 or h <0):
	print("Entradas:",v,"km/h e ",h,"h")
	print("Dados invalidos")
elif(s > 100.0):
	print("Entradas:",v,"km/h e ",h,"h")
	print("Castamere")
elif(s >  200.0):
	print("Entradas:",v,"km/h e ",h,"h")
	print("Doriath")
elif(s > 350.0):
	print("Entradas:",v,"km/h e ",h,"h")
	print("Fangorn")
elif(s > 400.0):
	print("Entradas:",v,"km/h e ",h,"h")
	print("Gondor")
elif(s > 250.0):
	print("Entradas:",v,"km/h e ",h,"h")
	print("Hogsmead")

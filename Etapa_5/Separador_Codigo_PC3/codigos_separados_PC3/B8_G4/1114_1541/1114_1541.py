v= float(input("digite a velocidade"))
t= float(input("digite o tempo"))

print("Entradas:",v,"km/h e",t,"h")

if (v > 0) and (t > 0):
	if(t > 100/v):                                                                                                                  
		print("Proxima parada:Bravos")
	elif(t > 200/v):
		print("Proxima parada:Castamere")
	elif(t > 400/v):
		print("Proxima parada:Doriath")
	elif(t > 600/v):
		print("Proxima parada:Edoras")
	elif(t > 750/v):
		print("Proxima parada:Fangorn")
else:
	print("Dados invalidos")
a=float(input("Velocidade: "))
b=float(input("tempo: "))

print("Entradas:",a,"km/h e",b,"h")

if(0<a*b<100):
	print("Proxima parada: Bravos")
elif(0<a*b<200):
	print("Proxima parada: Castamere")
elif(0<a*b<400):
	print("Proxima parada: Doriath")
elif(0<a*b<600):
	print("Proxima parada: Edoras")
elif(0<a*b<750):
	print("Proxima parada: Fangorn")
elif(0<a*b<1150):
	print("Proxima parada: Gondor")
elif((0<a*b<1400) or (a*b>=1400)):
	print("Proxima parada: Hogsmead")
else:
	print("Dados invalidos")
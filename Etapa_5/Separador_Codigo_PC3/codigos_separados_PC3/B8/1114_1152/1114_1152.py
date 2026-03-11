vm = (float(input("Qual a velocidade: ")))
tempo = (float(input("Qual o tempo da viagem: ")))
distancia = (vm * tempo)
if(distancia<=0 or vm<0):
	print("Entradas: ",vm," km/h e",tempo,"h")
	print("Dados invalidos")
elif(distancia>0 and distancia<100):
	print("Entradas: ",vm," km/h e",tempo,"h")
	print("Proxima parada: Bravos")
elif(distancia>=100 and distancia<200):
	print("Entradas: ",vm," km/h e",tempo,"h")
	print("Proxima parada: Castamere")
elif(distancia>=200 and distancia<400):
	print("Entradas: ",vm," km/h e",tempo,"h")
	print("Proxima parada: Doriath")
elif(distancia>=400 and distancia<600):
	print("Entradas: ",vm," km/h e",tempo,"h")
	print("Proxima parada: Edoras")
elif(distancia>=600 and distancia<750):
	print("Entradas: ",vm," km/h e",tempo,"h")
	print("Proxima parada: Fangorn")
elif(distancia>=750 and distancia<1150):
	print("Entradas: ",vm," km/h e",tempo,"h")
	print("Proxima parada: Gondor")
elif(distancia>=1150):
	print("Entradas: ",vm," km/h e",tempo,"h")
	print("Proxima parada: Hogsmead")
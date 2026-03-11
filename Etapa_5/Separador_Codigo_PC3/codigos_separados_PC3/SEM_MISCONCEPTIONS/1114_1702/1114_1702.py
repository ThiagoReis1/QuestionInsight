v = float(input("Velocidade:"))
t = float (input("Tempo:"))
distancia = v + t
if(distancia == 100):
   print("Bravos")
elif(distancia == 200):
	print("Castamere")
elif(distancia == 400):
	print("Doriath")
elif(distancia == 600):
	print("Edoras")
elif(distancia == 750):
	print("Fangorn")
elif(distancia == 1050):
	print("Gondor")
elif(distancia == 1400):
	print("Hogsmead")
elif(v and t <= 0):
   print("Dados invalidos")
else:
	print("Próxima parada")
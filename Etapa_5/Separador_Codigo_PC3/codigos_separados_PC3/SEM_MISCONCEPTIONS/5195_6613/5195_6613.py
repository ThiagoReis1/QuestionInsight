distancia = float(input("Distancia da corrida: "))
total = float(input("Total de chakra: "))

q= distancia/total

if (q <= 10/3000 ):
	w = 3000*distancia
	print(w)
	print("vai conseguir")
	
else: 
	
	w= 3000*distancia
	print(w)
	print("nao vai conseguir")
	



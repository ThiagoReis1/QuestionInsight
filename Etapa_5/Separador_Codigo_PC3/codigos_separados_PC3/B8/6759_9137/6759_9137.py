distancia = int(input("Distancia: "))

if (distancia < 10):
	taxa = 5.5
elif (distancia == 10):
	taxa = 7.75
elif (distancia  > 10):
	taxa = 10.
	
total = 50. + taxa
print(round(total, 2))
numtom = int (input("Digite o numero de tomates comprados: "))

if (numtom >= 4):
	x = 0.55 * numtom
	print (round (x,2))
else:
	x = 0.75 * numtom
	print (round(x,2))
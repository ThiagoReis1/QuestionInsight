aminoacido = input()

if(aminoacido=="Histidina".lower()):
	O = 15.9994
	C = 12.011
	N = 14.00674
	H = 1.0079
	print(round((6 * C) + (10 * H) + (3 * N) + (2 * O), 2))
elif(aminoacido=="Leucina".lower()):
	O = 15.9994
	C = 12.011
	N = 14.00674
	H = 1.0079
	print(round((6 * C) + (13 * H) + N + (2 * O), 2))
elif(aminoacido=="Lisina".lower()):
	O = 15.9994
	C = 12.011
	N = 14.00674
	H = 1.0079
	print(round((6 * C) + (15 * H) + (2 * N) + (2 * O), 2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")
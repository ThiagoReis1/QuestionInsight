amino = input("aminoacido: ")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079


if((amino == "GLICINA") or (amino == "PROLINA") or (amino == "SERINA")):

	if(amino == "GLICINA"):
		g = (C * 2) + (H * 5) + (N) + (O * 2)
		print(round(g, 2))

	elif(amino == "PROLINA"):
		g_1 = (C * 5) + (H * 10) + (N) + (O * 2)
		print(round(g_1, 2))

	else:
		g_2 = (C * 3) + (H * 7) + (N) + (O * 3)
		print(round(g_2, 2))	
	
else:	
	print("Entrada:", amino.upper())
	print("Dado Invalido")
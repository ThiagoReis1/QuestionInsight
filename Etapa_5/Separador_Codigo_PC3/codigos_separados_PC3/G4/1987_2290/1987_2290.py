amino = str(input()).upper()

O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794


if(amino == "ALANINA"):
	x = ((C * 3) + (H * 7) + (N * 1) + (O * 2))
	print(round(x, 2))
elif(amino == "VALINA"):
	x =((C * 5) + (H * 11) + (N * 1) + (O * 2))
	print(round(x, 2))
elif(amino == "TIROSINA"):
	x = ((C * 9) + (H * 11) + (N * 1) + (O * 3))
	print(round(x, 2))
else:
	print("Entrada:", amino)
	print("Dado Invalido")
	

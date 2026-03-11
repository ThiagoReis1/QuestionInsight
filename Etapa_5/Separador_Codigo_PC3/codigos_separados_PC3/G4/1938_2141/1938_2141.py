aminoacido = input("Arginina ou Tirosina: ").upper()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
if(aminoacido == "ARGININA"):
	x = (C * 6) + (H * 15) + (N * 4) + (O * 2)
	
else:
	x = (C * 9) + (H * 11) + N + (O * 3)
	
print(round(x,2))
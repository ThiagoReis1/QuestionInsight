aminoacido = input("Asparagina ou Triptofano: ").upper()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
if(aminoacido == "ASPARAGINA"):
	x = (C * 4) + (H * 8) + (N * 2) + (O * 3)
	
else:
	x = (C * 11) + (H * 11) + (N * 2) +(O * 2)
	
print(round(x,2))
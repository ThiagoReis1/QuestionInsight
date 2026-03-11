string = (input(""))
			 
O= 15.999
C= 12.011
N= 14.00674
H= 1.00794
			 
asparagina = (C*4 + H*8 + N*2 + O*3)
triptofano = (C*11 + H*11 + N*2 + O*2)

if (string.upper() == "ASPARAGINA"):
	print(round(asparagina,2))
else:
	print(round(triptofano,2))
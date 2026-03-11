amin=input("informe o aminoacido:  ")
O=15.9994
C=12.011
N=14.00674
H=1.00794

ARGININA= ((C*6) + (H*15) + (N*4) + (O*2))
TIROSINA= ((C*9) + (H*11) + (N*1) + (O*3))
TRIPTOFANO= ((C*11) + (H*11) + (N*2) + (O*2))
if(amin.upper() == "ARGININA"):
	print(round(ARGININA, 2))
elif(amin.upper() == "TIROSINA"):
	print(round(TIROSINA, 2))
elif(amin.upper() == "TRIPTOFANO"):
	print(round(TRIPTOFANO, 2))
else:
	print("Entrada: ", amin.upper())
	print("Dado Invalido")
	
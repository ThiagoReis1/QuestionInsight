from math import*

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794

aminoacido = input("qual o nome do aminoacido?: ")

print("Entrada: GLUTAMINA")

if (aminoacido.upper() == "GLUTAMINA"):
	print("GLUTAMINA")
	soma = (C*4) + (H*8) + (N*1) + (O*3)
	
elif (aminoacido == "ASPARAGINA"):
	print("ASPARAGINA")
	soma = (C*4) + (H*8) + (N*2) + (O*3)
elif (aminoacido == "TRIPTOFANO"):
	soma= (C*11) + (H*11) + (N*2) + (O*2)
	print ()
else: ( aminoacido != GLUTAMINA)
n_a = input("nome do aminoacido:")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794

Ar = (C*6) + (H*15) + (N*4) + (O*2)
Ti = (C*9) + (H*11) + N+ (O*3)

if(n_a.upper() == "ARGININA"):
	print(round(Ar,2))
else:
	print(round(Ti,2))
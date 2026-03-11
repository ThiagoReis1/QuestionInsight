O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794
GLUTAMINA = (C*5 + H*8 + N*1 + O*4)
TREONINA = (C*4 + H*9 + N*1 + O*3)
aminoacido = input("digite o nome do aminoacido aqui: ")
if( aminoacido == "GLUTAMINA"):
	print(round(GLUTAMINA, 2))
else:
	print(round(TREONINA, 2))
	
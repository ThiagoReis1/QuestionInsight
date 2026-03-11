a = input(" ").upper()


O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794

if (a=="GLUTAMINA"):
	GLUTAMINA = C*5 + H*8 + N*1 + O*4
	print(round(GLUTAMINA,2))
elif (a=="SERINA"):
	SERINA = C*3 + H*7 + N*1 + O*3
	print(round(SERINA,2))
elif (a=="TREONINA"):
	TREONINA = (C*4) + (H*9) + (N*1) + (O*3)
	print(round(TREONINA,2))
else:
	print("Entrada:", a)
	print("Dado Invalido")
	



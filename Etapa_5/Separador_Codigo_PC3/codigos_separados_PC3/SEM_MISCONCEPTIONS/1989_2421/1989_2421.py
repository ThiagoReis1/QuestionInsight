a = input("nome do aminoacido: ").upper()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
ASPARAGINA = (C*4)+(H*8)+(N*2)+(O*3)
GLUTAMINA = (C*5)+(H*8)+(N*1)+(O*4)
TRIPTOFANO = (C*11)+(H*11)+(N*2)+(O*2)

if (a=="ASPARAGINA"):
	print(round(ASPARAGINA,2))
elif (a=="GLUTAMINA"):
	print(round(GLUTAMINA,2))
elif (a=="TRIPTOFANO"):
	print(round(TRIPTOFANO,2))
else:
	print("Entrada:", a)
	print("Dado Invalido")
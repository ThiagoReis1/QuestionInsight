x = input("digite o aminoacido: ").upper()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
y1 = (C*4)+(H*8)+(N*2)+(O*3)
y2 = (C*5)+(H*8)+(N*1)+(O*4)
y3 = (C*11)+(H*11)+(N*2)+(O*2)
if (x == "ASPARAGINA"):
	print(round(y1,2))
elif (x == "GLUTAMINA"):
	print(round(y2,2))
elif (x == "TRIPTOFANO"):
	print(round(y3,2))
else:
	print("Entrada:", x)
	print("Dado Invalido")
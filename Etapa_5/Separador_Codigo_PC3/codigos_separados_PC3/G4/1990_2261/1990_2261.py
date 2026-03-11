x = input("digite o amuniacido:").upper()
O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794
y1 = (C*5) + (H*8) + (N*1) + (O*4)
y2 = (C*3) + (H*7) + (N*1) + (O*3)
y3 = (C*4) + (H*9) + (N*1) + (O*3)
if(x == "GLUTAMINA"):
	print(round(y1,2))
elif(x == "SERINA"):
	print(round(y2,2))
elif(x == "TREONINA"):
	print(round(y3,2))
else:
	print("Entrada:",x)
	print("Dado Invalido")

quantidade = float(input("numero de tomates: "))
T = quantidade*0.75
T2 = quantidade*0.55
if (quantidade < 4):
	print(round(T,2))
if (quantidade >= 4):
	print(round(T2,2))
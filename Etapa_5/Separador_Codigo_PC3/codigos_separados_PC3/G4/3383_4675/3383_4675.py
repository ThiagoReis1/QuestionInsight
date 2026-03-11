ma = input("unidade de medida:")
if	(ma.upper()=="L"):
	l = float(input("massa:"))
	kg=l/2.20462
	print(round(kg,2))
else:
	k = float(input("massa:"))
	lb=k*2.20462
	print(round(lb,2))
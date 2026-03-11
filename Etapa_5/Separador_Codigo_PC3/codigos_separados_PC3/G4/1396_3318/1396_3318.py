vt = float(input("valor total consumido: "))
g1 = (vt*10)/100
g2 = (vt*6)/100
if (vt<=300):
	print(round(vt+g1,2))
else:
	print(round(vt+g2,2))
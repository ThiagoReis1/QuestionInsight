
a = input("unidade em que a medida esta: ")
v = float(input("valor da medida: "))

l = a.upper() 

if (l == "G"):
	R = 0.0174533 * v
	print(round(R,2))

else:
	G = v/(0.0174533)
	print(round(G,2))
	
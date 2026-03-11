x=input("G ou R:")
a=float(input("angulo: "))

rad = 0.0174533*a
gr= a/ 0.0174533

if(x== "R"):
	print(round(gr, 2))
else:
	print(round(rad, 2))
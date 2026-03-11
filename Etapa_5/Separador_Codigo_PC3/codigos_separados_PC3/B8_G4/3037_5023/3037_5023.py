x = float(input("Numero: "))
if (x<=-1 or x>=1):
	fx = x**2
elif (-1<x and x<0) or (0<x and x<1):
	fx = x
elif (x == 0 ):
	fx = 0
print(round(fx,4))
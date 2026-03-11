from math import *
x=float(input("x: "))
if x<-4 or x>4:
	print("entrada invalida")
else:
	if x>=-4 or x<0:
		h=abs(x)
		g=sqrt(abs(x))
		print(round(g, 4))
	else:
		h=sqrt(x)
		print(round(x, 4))
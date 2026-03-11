import math
x=float(input('valor de x: '))

if((x<=-1) or (x>=1)):
	fx=((abs(x)**(1/2)))
	print(round(fx, 2))
elif((-1 < x < 0) or (0 < x < 1)):
	fx=abs(x)
	print(round(fx, 2))
elif(x==0):
	fx=0
	print(round(fx, 2))
	
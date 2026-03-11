from math import *

x=float(input("Valor de x:"))

if(x>=-4 and x<0):
	fx= sqrt(abs(x))
	print(round(fx,4))
elif(x==0):
	fx=0
	print(round(fx,4))
elif(x>0 and x<=4):
	fx=sqrt(x)
	print(round(fx,4))
else:
	print("entrada invalida")
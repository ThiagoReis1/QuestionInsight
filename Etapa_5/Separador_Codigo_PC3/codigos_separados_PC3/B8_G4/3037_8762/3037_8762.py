from math import *

x = float(input("Informe o valor de x: "))

if(x<=-1 or x>=1):
	fx = x*x
	print(round(fx,4))
elif(x>-1 and x<0) or (x>0 and x<1):
	fx = x
	print(round(x,4))
elif(x==0): 
	fx = 1
	print(round(x,4))
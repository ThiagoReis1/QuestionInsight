from math import *
x= float(input("digite o valor de x: "))

if x<= -1 or x>=1 :
	xt= (abs(x))**(1/2)
elif x==0 :
	xt= 0
else:
	xt= abs(x)
print(round(xt,2))
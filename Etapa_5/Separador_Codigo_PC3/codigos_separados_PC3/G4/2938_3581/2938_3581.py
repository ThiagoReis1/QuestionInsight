from math import*

a=float(input("digite: "))
b=float(input("digite: "))
y=radians(float(input("digite: ")))

d=(a**2)+(b**2)			 
c=sqrt(d-2*a*b*cos(y))
			 
print(round(c,2))			 
from math import *
a = float(input("valor de a "))
b = float(input("valor de b "))
y = float(input("valor de y "))
c = sqrt(a**2+b**2-(2*a*b*cos(radians(y))))
print(round(c, 2))	
				
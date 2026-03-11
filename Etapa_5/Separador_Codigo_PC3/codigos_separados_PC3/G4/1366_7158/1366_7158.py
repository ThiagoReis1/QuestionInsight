from math import *
a = radians(float(input("qual o valor do angulo: ")))
b = float(input("qual velocidade inicial: "))
g = 9.8 
				
d = b**2*sin(2*a)/g
print(round(d,2))
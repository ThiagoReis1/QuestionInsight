from math import * 
a=float(input("velocidade inicial: "))
d=float(input("distancia: "))
g=9.8
A=asin(d*(g/a**(2)))*90/pi
print(round(A, 2))		
		



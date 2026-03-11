from math import *

af = float(input("Angulo da flecha: "))
vif = float(input("Velocidade inicial: "))

g = 9.8

d = vif**2 * ((sin(2 * radians(af))) / g)
						 
print(round(d,2))
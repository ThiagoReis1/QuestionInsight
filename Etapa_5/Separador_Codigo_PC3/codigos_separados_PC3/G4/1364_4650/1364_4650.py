from math import*
v0 = float(input("velocidade inicial:"))
d =  float(input("distancia:"))
A = (asin(d*g/v0**2)*90/pi) 

print(round(A, 2))
from math import*
v0 = float(input("velocidade incial")) 
d = float(input("distancia"))
a = asin(d*9.8/v0**2)* 90/pi



print(round(a, 2))
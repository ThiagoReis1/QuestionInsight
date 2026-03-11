from math import * 
angulo= float(input()) 
distancia= float(input()) 
g= 9.8
v= sqrt(distancia * (g / (sin(2 * radians(angulo)))))
print(round(v, 2))
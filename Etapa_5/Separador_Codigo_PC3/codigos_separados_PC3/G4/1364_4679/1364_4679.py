from math import*
v=float(input("valor inicial?"))
d=float(input("distancia?"))
g=9.8
angulo= (asin(d*g/v**2)*90/pi)
print(round(angulo,2))
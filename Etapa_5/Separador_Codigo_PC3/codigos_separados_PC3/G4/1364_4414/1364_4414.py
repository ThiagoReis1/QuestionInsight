import math
v=float(input("velocidade:"))
d=float(input("distancia:"))

g= 9.8
y = (d*g)

x = math.asin(y/v**2)* 90/math.pi

print(round(x, 2))
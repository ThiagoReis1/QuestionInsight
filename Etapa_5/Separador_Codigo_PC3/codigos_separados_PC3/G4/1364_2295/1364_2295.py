from math import*
v=float(input("velocidade:"))
d=float(input("distancia:"))
g=9.8
a=asin((d * g)/ v**2 )* (90 / pi)
print(float(round(a,2)))
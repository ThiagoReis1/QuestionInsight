from math import *
a = float(input("ângulo:")) #em graus
d = float(input("distância:"))#em metros
a = radians(a)
g = 9.8
V0 = sqrt ((d * g)/sin(2*a))
print(round(V0 ,2))
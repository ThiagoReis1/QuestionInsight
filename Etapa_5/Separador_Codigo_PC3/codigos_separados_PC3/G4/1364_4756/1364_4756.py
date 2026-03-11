from math import *
v = float (input("Qual a velocidade inicial? "))
d = float (input("Qual a distancia em metros? "))
g = 9.8
alfa = asin (d*g / v**2) * (90 / pi)				 
print (round (alfa, 2))
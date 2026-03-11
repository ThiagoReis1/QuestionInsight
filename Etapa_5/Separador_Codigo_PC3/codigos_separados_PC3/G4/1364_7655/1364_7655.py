from math import *

G= 9.8

#ENTRADA 
v= float(input("Digite a velocidade da flecha: "))
d= float(input("Digite a distancia que esta o alvo Falmer: "))

a= asin(((d* G)/(v**2)))* 90/pi

print(round(a,2))

#Necessario
from math import*

#entradas
a = float(input("digite a: "))
d = float(input("digite d: "))

#valores fixos

aa = radians(a)
g = 9.8

#formula

v = d*g/sin(2*aa)
s = v**0.5
#saida

print(float(round(s,2)))
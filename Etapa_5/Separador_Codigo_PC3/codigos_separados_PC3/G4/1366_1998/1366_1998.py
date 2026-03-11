from math import *
a = float (input("Digite o angulo:"))
vo = float (input("Digite Vo:"))
b = radians (a)
d = vo**2*sin(2*b)/9.8
print (round(d,2))
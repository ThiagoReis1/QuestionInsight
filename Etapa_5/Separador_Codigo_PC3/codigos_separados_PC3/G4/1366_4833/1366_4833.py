from math import *

a = float(input("digite o angulo da flecha em graus: "))
vo = float(input("digite a velocidade inicial da flecha: "))

x = sin(radians(2*a))

d = ((vo)**2) * (x/9.8)


print(round(d, 2))
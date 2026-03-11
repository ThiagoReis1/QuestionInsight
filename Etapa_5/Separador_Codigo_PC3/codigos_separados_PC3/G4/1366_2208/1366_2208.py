from math import *
a=radians(float(input("Digite o angulo: ")))
vo=float(input("Digite a velocidade: "))
g=9.8

d1=(vo**2)
d2=sin(2*a)
d=d1*(d2/g)

print(round(d,2))
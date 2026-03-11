from math import *
ai=float(input("Digite o angulo de saida da flecha: "))
vl=float(input("Digite a velocidade de saida da flecha: "))
af=radians(ai)
g=float(9.8)
d=float((vl**2)*(sin(2*af)/g))
print(round(d,2))
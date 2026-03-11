# area é um círculo
# raio aprox em metros e dar o custo por metro quadrado
# area do circulo = pi.a²

from math import *

raiocirculo = float(input("raio em metros: "))
custo = float(input("custo de aplicacao: "))

areafazenda = pi * raiocirculo**2
total = areafazenda * custo

print(round(total, 2))
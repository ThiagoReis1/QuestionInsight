# custo da aplicação de fertilizante numa fazenda

from math import *

raio = float (input("digite o o raio da fazenda:"))

custo = float (input("digite o valor do custo por metro quadrado:"))

area = pi * raio ** 2

custo = area  * custo

print (round(custo,2))
from math import *

o_raio = float(input("Qual o raio?"))
n_lados = float(input("Qual o numero de lados?"))

lado_L = 2 * o_raio * sin(pi/n_lados)

print(round(lado_L,2))
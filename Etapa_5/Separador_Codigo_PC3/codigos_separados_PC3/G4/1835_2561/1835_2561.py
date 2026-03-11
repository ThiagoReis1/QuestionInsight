from math import *

# Gravidade = constante = 9,8 m/s²
g = 9.8

# Comprimento do pêndulo
L = float(input())

# Período de oscilação do pêndulo
T = 2 * pi * sqrt(L / g)
print(T)
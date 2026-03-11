from math import *

# Comprimento
l = float(input("Insira o comprimento do pêndulo: "))

# Periodo de Oscilação
t = 2 * pi * sqrt(l/9.8)

# Resultado
print(t)
from math import*

v = float(input()) # Velocidade Inicial da flecha

d = float(input()) # Distância entre você e um determinado Falmer

a = asin(d*(9.8/v**2))*(90/pi)

print(round(a,2))



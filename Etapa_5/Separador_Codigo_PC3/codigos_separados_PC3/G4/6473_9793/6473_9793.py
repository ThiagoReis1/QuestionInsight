import math

lado = float(input("Insira o cumprimento do lado do decagono: "))

apot = lado / (2 * math.tan(math.pi / 10))
area = 5 * lado * apot

print(round(area, 2))
import math

# faça seu código aqui!
lado = float(input("Lado do Hexagono: "))

apotema = lado / (2*math.tan(math.pi / 6))

area = 3 * lado * apotema

print(round(area, 2))
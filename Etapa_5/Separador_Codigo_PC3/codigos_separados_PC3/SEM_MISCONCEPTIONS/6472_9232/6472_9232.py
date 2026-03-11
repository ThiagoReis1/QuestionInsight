import math

lado = float(input("qual a medida do lado do eneagono? "))

apotema = lado / ((2)*math.tan(math.pi / 9))

area = ((9) * (lado) * (apotema) / 2)

print(round(area, 2))
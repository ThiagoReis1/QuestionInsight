import math
lado = float(input("lado "))

apotema = lado / (2 * math.tan(math.pi/8))
areaoct = 4 * lado * apotema
print(round(areaoct, 2))
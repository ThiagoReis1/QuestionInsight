from math import cos
from math import pi
raio = float(input("raio: "))
lados = int(input("lados: "))
a = raio * cos(pi/lados)
print(round(a, 2))

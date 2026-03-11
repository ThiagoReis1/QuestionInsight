# Minas de Sidon
angulo = float(input("Qual o angulo da flecha?"))

import math
r = math.radians(angulo)
sin = math.sin(2 * r)

g = 9.8

dis = float(input("Qual a distancia entre voce e o Falmer?"))

velo1 = dis * g

velo2 = sin

velo3 = (velo1/velo2)**0.5

print(round(velo3, 2))


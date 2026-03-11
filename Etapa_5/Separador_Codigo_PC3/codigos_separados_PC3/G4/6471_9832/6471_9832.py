from math import pi, tan
l = int(input("Tamanho dos lados: "))
ap = l / (2 * tan(pi/8))
ao = 4 * l * ap
print(round(ao,2))

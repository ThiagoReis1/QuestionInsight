# Dina Karen Barros Vieira
# Trabalho Prático 1
# exercício 2

vel_inic = float(input("Qual a velocidade inicial da flecha?"))
dist = float(input("Qual a distância?"))

from math import*

ang = asin(dist * (9.8/vel_inic**2)) * 90/pi

print(round(ang, 2))


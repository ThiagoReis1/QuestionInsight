from math import *

ladoB = float(input("Digite o lado B: "))
ladoC = float(input("Digite o lado B: "))
angulo = float(input("Digite o angulo alfa ente b e c, em graus: "))

a = sqrt((ladoB**2)+(ladoC**2)-2*ladoB*ladoC*cos(radians(angulo)))

print(round(a, 2))
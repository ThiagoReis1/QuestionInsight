from math import cos, sqrt, radians
b = float(input("Insira o lado B: "))
c = float(input("Insira o lado C: "))
angulo = radians(float(input("Insira o angulo: ")))
cos_angulo = cos(angulo)

calculo = sqrt ((b**2)+(c**2)-(2*(b*c*cos_angulo)))

print(round(calculo,2))
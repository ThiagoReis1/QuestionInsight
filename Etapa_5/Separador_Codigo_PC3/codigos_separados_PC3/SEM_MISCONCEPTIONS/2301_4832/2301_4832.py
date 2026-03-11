from math import*
lado_b = (float(input('Digite o lado b: ')))
lado_c = (float(input('Digite o lado c: ')))
angulo = (float(input('Digite o angulo entre b e c: ')))
angulo1 = radians(angulo)
alfa = (((lado_b**2) + (lado_c**2)) - ((2*lado_b*lado_c)*cos(angulo1))) ** 0.5
print(round(alfa, 2))
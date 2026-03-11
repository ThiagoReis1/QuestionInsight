from math import*
b = float(input("Insira o lado b: "))
c = float(input("Insira o lado c: "))
angulo = radians(float(input("Insira o angulo entre b e c: ")))

alfa = sqrt(b**2 + c**2 - 2*(b*c*cos(angulo)))

print(round(alfa,2))
from math import*

a = radians(float(input("Informe o angulo: ")))
v = float(input("Informe o velocidade: "))

d = (v**2 * (sin(2 * a))/ 9.8)

print(round(d, 2))

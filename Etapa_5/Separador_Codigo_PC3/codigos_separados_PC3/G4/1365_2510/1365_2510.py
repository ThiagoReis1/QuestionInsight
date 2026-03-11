from math import*

a = radians(float(input("Ângulo: ")))

d = float(input("Distância: "))

v = sqrt((d*9.8)/sin(2*a))

print(round(v,2))
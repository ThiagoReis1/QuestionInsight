from math import*
a = radians(float(input("angulo: ")))
b = float(input("v_inicial: "))
g = 9.8
d = (b**2)*(sin(2*a))/g
print(round(d, 2))
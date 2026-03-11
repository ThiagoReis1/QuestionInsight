from math import*

a = float(input("Informe o angulo: "))
a = radians(a)
b = float(input("Informe a velocidade inicial: "))

d = (b**2)*(sin(2*a)/9.8)

print(round(d, 2))
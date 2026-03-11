from math import*
a = radians(float(input("qual o angulo da flecha: ")))
b = float(input("Qual a velocidade inicial da flecha: "))
g = 9.8

d = b**2*sin(2*a)/g
print(round(d,2))


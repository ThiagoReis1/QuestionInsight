from math import*
b = float(input("b: "))
c = float(input("c: "))
x = float(input("insira um valor: "))
y = radians(x)
a = sqrt(b**2 + c**2 - (2*b*c*cos(y)))

print(round(a, 2))
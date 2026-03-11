from math import *
x = float(input("Valor inicial investido(R$): "))
r = float(input("Taxa de rendimento(%): "))
Px = log(x)
Py = log(3*x)

z = int((((Py)-(Px))/ r) +1)

print (z)
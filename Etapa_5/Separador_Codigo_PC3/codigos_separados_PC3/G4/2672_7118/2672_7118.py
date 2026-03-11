from math import*

a = float(input("raio r: "))
b = int(input("lados: "))

A = 1 / 2 * ((a * cos (pi / b)) ** 2 * tan(pi / b))

print(round(A, 2))
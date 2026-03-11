from math import*
r = float(input("r: "))
n = int(input("n: "))
a = float(1 / 2 * (r * cos(pi / n)) ** 2 * tan(pi / n))
print(round(a, 2))
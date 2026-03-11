from math import(sqrt)

d = int(input("quantidade de pocoes:"))

a = ((sqrt(5) - 1) / 4)
b = sqrt(5 - 2 * sqrt(5))
c = 5 * (5 - 2 * sqrt(5))

print(float(round( d * a, 2)))
print(float(round( d * b, 2)))
print(float(round( d * c, 2)))
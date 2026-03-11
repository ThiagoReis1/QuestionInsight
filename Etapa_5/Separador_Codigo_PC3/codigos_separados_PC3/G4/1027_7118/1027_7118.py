from math import*

a = float(input("consumo: "))

b = (0.43 * a) + 10
c = b * (25/100)
total = b + c

print(round(total, 2))
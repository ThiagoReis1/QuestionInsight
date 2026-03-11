from math import sqrt
q = int(input("Digite a quantidade de porções: "))
sn = (sqrt(5) - 1) / 4
fo = (sqrt(5 - 2 * sqrt(5)))
am = 5 * (5 - 2 * sqrt(5))
a = sn * q
b = fo * q
c = am * q

print(round(a, 2))
print(round(b, 2))
print(round(c, 2))
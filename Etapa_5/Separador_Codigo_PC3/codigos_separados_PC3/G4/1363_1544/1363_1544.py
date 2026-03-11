from math import *
p = float(input())
ruby = float(2 ** (1 + p / 1000))
soul = float((p * pi ** 2) / 3141)
dwarven = float(2 * (sqrt(p / 40)))
print(round(ruby,2))
print(round(soul,2))
print(round(dwarven,2))
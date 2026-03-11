from math import *

r = float(input("quantidade de flawless ruby: "))
fr = 4.0
sg = 3.14
od = 10.0
a = r/fr

s = float(input("quantidade de soul gem: "))
fr = 4.0
sg = 3.14
od = 10.0
b = s/sg

o = float(input("quantidade de oleo de dwarven: "))
fr = 4.0
sg = 3.14
od = 10.0
c = o/od

menor = int(min(a, b, c))

print(menor)

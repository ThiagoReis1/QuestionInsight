from math import *

# faça seu código aqui!

lado = int(input("lado d:"))

op = lado / (2* tan(pi/10))

area = 5 * lado * op

print(round(area, 2))
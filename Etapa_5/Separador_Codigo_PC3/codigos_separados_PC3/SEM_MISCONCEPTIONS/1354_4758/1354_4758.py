from math import *
mw = float(input("Media de watts desejada: "))
ra = float(input("O raio do comodo: "))
total = (pi*ra**2)*mw
print (round(total,2))
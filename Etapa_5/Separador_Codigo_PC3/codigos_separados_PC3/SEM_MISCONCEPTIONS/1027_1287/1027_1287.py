from math import *
custo = float(input("digite o consumo"))
parcial = (0.43 * custo + 10)
impost = (parcial * 0.25)
total = (parcial +impost)
print (round(total, 2))
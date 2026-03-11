from math import tan, pi
aread = int(input("digite o valor do lado: "))
apotema = aread/(2*tan(pi/12))
total = 6*aread*apotema
print(round(total, 2))

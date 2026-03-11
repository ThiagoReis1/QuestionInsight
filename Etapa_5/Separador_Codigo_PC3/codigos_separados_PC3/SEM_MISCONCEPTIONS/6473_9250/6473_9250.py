from math import tan, pi
lado_dec = float(input("lado do decagono: "))
apotema = lado_dec/(2*tan(pi/10))
area_dec = 5*lado_dec*apotema
print(round(area_dec, 2))
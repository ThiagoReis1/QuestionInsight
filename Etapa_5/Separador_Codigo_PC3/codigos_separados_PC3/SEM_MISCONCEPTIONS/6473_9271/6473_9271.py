from math import *
lado_do_decagono = float(input("digite o valor do lado do decagono: "))
apotema = lado_do_decagono / (2 * tan(pi/10))
area_do_decagono = 5 * lado_do_decagono * apotema
print(round(area_do_decagono,2))
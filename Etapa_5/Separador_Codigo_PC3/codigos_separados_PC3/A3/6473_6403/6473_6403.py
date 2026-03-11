from math import * 

#identificar a area do apoema#

var = float(input(10 * 4))

lado = 10

apotema = (lado / (2 * (tan(pi / 10))))

area_do_decagono = 5 * (lado * apotema)

print(round((area_do_decagono), 2))
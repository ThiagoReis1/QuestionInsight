from math import *

p = float(input("Peso da espada (em gramas):"))
flawless_ruby = 2 ** ((1 + p/1000))
soul_gem = p * (pi ** 2 / 3141)
oleo_de_dwarven = 2 * (sqrt( p / 40 ))
print(round(flawless_ruby, 2))
print(round(soul_gem, 2))
print(round(oleo_de_dwarven, 2))
from math import *
p = float(input("Digite o valor da espada em gramas:"))
gramas_de_flawless_ruby = 2**(1+(p/1000))
gramas_de_soul_gem = p * ((pi**2)/3141)
gramas_de_oleo_dwarven = 2 * sqrt(p/40)
print(round(gramas_de_flawless_ruby, 2))
print(round(gramas_de_soul_gem, 2))
print(round(gramas_de_oleo_dwarven, 2))
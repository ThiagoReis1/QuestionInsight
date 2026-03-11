from math import *
pocoes = int(input("quantidade de pocoes: "))

snowberry = float((sqrt(5) - 1) / 4) * pocoes
sais_fogo = float(sqrt(5 - (2 * sqrt(5)))) * pocoes
amanita = float(5 * (5 - (2 * sqrt(5)))) * pocoes


print(round(snowberry, 2))
print(round(sais_fogo, 2))
print(round(amanita, 2))
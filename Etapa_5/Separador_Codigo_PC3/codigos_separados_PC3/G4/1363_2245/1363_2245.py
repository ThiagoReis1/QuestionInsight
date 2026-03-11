from math import *

# entrada para a variavel p que simboliza a massa da espada
p = float(input("Digite o valor da massa da espada: "))

#Calculo da massa de Flawless Ruby
FR = 2 ** (1 + p/1000)

#Calculo da massa de Soul Gem
SG = p * ((pi ** 2) / 3141 )

#Calculo da massa de Óleo de Dwarven
OD = 2 * (sqrt(p/40))

print(float(round(FR, 2)))
print(float(round(SG, 2)))
print(float(round(OD, 2)))
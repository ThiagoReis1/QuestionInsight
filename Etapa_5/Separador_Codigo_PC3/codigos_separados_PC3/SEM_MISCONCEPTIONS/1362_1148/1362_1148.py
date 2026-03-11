#Érika Priscila Silva Cavalcante - Matrícula: 21201952
#Trabalho Prático 1
#Exercício 2

from math import *

veneno = float(input())

casca = (veneno / 5) * sqrt(9 / 5)
alho = (veneno ** 2) / pi
oleo = sqrt((5 * veneno) / 3)

print(round(casca, 2))
print(round(alho, 2))
print(round(oleo, 2))
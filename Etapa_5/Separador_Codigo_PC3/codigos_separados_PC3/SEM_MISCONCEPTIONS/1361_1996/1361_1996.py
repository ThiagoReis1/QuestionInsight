#Questao 02

from math import *

pocoes = int(input("Qual a quantidade de pocoes desejadas: "))

snowberry = pocoes * ((5 ** 0.5 ) - 1) / 4

sais = pocoes * (sqrt(5 - 2 * (5 ** 0.5)))

amanita = pocoes * 5 * (5 - 2 * (5 ** 0.5))


print(round(snowberry,2))
print(round(sais,2))
print(round(amanita,2))
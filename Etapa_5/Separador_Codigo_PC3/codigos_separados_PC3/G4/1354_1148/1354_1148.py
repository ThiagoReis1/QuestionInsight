#Érika Priscila Silva Cavalcante - Matrícula: 21201952
#Trabalho Prático 1
#Exercício 1

from math import *

mwatts = float(input())
raio = float(input())

area = pi * raio ** 2
pot = area * mwatts

print(round(pot, 2))
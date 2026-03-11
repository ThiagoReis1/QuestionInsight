from math import *
#pedindo o comprimento do lado
lado = float(input("Comprimento do lado do eneagono?: "))

apotema = lado/(2*tan(pi/9)) # calculando a apotema do eneagono
area = 9*lado*apotema/2 # calculando a area do eneagono

print(round(area, 2)) # imprimindo a area 


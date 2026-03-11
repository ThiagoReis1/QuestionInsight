#Universidade Federal do Amazonas
#Instituto de Ciencias Exatas e da Terra
#Oziel Ramos de Lima Junior
#21553853

from math import*
raio = float(input("Raio da fazenda: "))
custo = float(input("Custo da construcao: "))

perimetro = 2 * pi * raio
custo_total = perimetro * custo

print(round(custo_total,2))
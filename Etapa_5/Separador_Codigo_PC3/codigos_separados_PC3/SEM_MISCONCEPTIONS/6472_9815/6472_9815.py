from math import *

# faça seu código aqui!
lado = float(input("Insira o Valor do Lado: "))
apotema = lado / (2 * tan(pi / 9))
area = round( ((9 * lado * apotema) / 2), 2)

print(area)
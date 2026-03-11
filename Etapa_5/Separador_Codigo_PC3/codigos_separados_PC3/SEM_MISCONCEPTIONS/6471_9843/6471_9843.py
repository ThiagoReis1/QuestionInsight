from math import * 

# faça seu código aqui!
lado = float(input("Digite o comprimento do lado do octogono: "))

apotema = lado / (2 * tan(pi/8))

area = 4*lado*apotema
print(round(area, 2))
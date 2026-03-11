from math import *

comprimento = int(input("Digite o comprimento: ")) 

apotema = (comprimento) / (2 * tan(pi/12))

area = 6 * comprimento * apotema

print(round(area,2))

# faça seu código aqui!
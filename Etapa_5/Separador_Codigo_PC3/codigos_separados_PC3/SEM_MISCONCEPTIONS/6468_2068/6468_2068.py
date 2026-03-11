import math
# faça seu código aqui!

lado = int(input("Comprimento lado do pentagono: "))

apotema = lado / (2 * math.tan(math.pi / 5))

areaPentagono = (5 * lado * apotema) / 2 

print(round(areaPentagono, 2))
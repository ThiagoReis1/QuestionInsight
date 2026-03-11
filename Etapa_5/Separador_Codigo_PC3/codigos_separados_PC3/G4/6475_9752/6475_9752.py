from math import *

# faça seu código aqui!
A = int(input("Qual o comprimento do lado: "))

apo = A/(2*tan(pi/12))

area = (6 * A * apo)

print(round(area,2))



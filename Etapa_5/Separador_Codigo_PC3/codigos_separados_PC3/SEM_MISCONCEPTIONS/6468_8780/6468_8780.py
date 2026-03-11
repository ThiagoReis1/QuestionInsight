from math import *

#Entrada

lado= float(input("Digite o valor do lado do pentagono: "))

#Expressão

apotema = (lado) / (2 * tan(pi / 5))

areapenta = (5 * lado * apotema) / 2

#Saída

print(round(areapenta,2))
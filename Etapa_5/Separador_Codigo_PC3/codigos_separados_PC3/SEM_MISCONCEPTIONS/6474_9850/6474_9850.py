from math import *

# faça seu código aqui!

lado = float(input("Digite o valor do comprimento do lado do undecagono: "))

apotema = lado / (2 * tan(pi/11))
	
AU = (11 * lado * apotema) / 2

print(round(AU,2))
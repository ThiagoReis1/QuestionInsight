from math import *

# faça seu código aqui!

lado = float(input("insira o valor de lado : "))

apotema = (lado) / (2 * tan(pi/12))

adc = 6 * lado * apotema

print(round(adc, 2))




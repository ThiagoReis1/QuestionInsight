# Instituto de computacao
# Trabalho pratico 01
# 03 / 04 / 2017

# Variavies fornecidas  pelo problema
from math import *
x = float(input("Digite o valor do angulo desejado: "))
v = float(input("Digite o valor inicial da flecha: "))
g = 9.8 
d = (v**2*sin(2*x)/g)

			 
print(round(d,2))			 
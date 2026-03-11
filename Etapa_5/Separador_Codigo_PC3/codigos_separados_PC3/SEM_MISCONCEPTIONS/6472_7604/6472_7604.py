from math import *

lado = float(input("digite o comprimento do lado do eneagono: "))

ap = (lado) / (2*tan(pi/9)) 
formula = 9*(lado)*ap/2

print(round(formula,2))

# faça seu código aqui!
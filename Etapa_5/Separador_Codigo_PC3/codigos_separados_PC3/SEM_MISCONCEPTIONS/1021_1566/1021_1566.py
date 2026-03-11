#Ronilson de Souza Bezerra

from math import*

comprimento = float(input("digite o comprimento: "))
a = float(input("digite a area: "))

areahex = (3 * sqrt(3) * (a ** 2)/2) * comprimento

custo = areahex / a ** 2

print(round(custo, 2))



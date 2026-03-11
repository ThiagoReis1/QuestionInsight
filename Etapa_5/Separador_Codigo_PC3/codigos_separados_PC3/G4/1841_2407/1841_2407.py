from math import *

#valor inicial
q0 = float(input("Insira o valor inicial: "))

#taxa de rendimento
r = float(input("Insira a taxa de rendimento anual: "))

#valor final

qf = 3 * q0

#número de anos
y = (log(qf) - log(q0)) / r

print(ceil(y))
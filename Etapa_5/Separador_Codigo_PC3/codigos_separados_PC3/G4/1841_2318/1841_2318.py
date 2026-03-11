from math import *

qo = float(input("Digite o valor inicial de qo"))
r = float(input("Digite a taxa de rendimento"))
y = (log(3*qo) - log(qo))/r

print(int(round(y, 0)))
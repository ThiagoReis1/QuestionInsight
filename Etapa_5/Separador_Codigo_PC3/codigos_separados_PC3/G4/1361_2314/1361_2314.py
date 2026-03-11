from math import *

qp = int(input("Quantidade de Poções:"))

qsnow = (5**(1/2) - 1) / 4
qsf = (5 - 2 * (5**(1/2)))**(1/2)
qa = 5*(5 - 2 * (5**(1/2)))

print(round(qsnow*qp,2))
print(round(qsf*qp,2))
print(round(qa*qp,2))
a = float(input("comprimento aresta: "))
cust1 = float(input("custo p metro: "))

from math import*
r = sqrt(3)

ar = 3 * r * (a ** 2)/2

ct = ar * cust1

print(round(ct, 2))
